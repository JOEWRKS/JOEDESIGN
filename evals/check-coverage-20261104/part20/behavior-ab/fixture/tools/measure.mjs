// tools/measure.mjs — 이 프로젝트의 미리보기 도구(헤드리스 Chrome, CDP). 환경 제공물이며 고치지 않는다.
// 사용:
//   node tools/measure.mjs --page src/index.html --width 375 --height 700 \
//        [--before "<JS, 측정 전 실행: 상태 만들기>"] --eval "<JS 식, 결과를 JSON으로 출력>" \
//        [--inject src/style.css] [--screenshot out.png] [--dark]
// --eval/--before는 페이지 안에서 실행된다. 결과는 {"value": ..., "linkedCss": [...]} JSON 한 줄.
// linkedCss: 페이지의 <link rel=stylesheet>마다 {href, loaded} (loaded=false면 그 CSS가 적용되지 않은 것).
import { spawn } from 'node:child_process';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { pathToFileURL } from 'node:url';

const BLOCK_LINKED_CSS = /confirm\.html$/; // 환경 설정값

const args = process.argv.slice(2);
const opt = (k, d) => { const i = args.indexOf('--' + k); return i < 0 ? d : args[i + 1]; };
const flag = k => args.includes('--' + k);
const page = opt('page'); if (!page) { console.error('--page required'); process.exit(2); }
const width = +opt('width', 1280), height = +opt('height', 800);
const evalExpr = opt('eval', 'null'), before = opt('before', ''), inject = opt('inject'), shot = opt('screenshot');
const CANDS = ['C:/Program Files/Google/Chrome/Application/chrome.exe', 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'];
const exe = CANDS.find(p => fs.existsSync(p)); if (!exe) { console.error('no chrome'); process.exit(2); }
const udd = fs.mkdtempSync(path.join(os.tmpdir(), 'measure-'));
const proc = spawn(exe, ['--headless=new', '--remote-debugging-port=0', `--user-data-dir=${udd}`, '--no-first-run', '--no-default-browser-check', '--disable-gpu', 'about:blank'], { stdio: 'ignore' });
const sleep = ms => new Promise(r => setTimeout(r, ms));
let port;
for (let i = 0; i < 100 && !port; i++) { await sleep(100); try { port = fs.readFileSync(path.join(udd, 'DevToolsActivePort'), 'utf8').split('\n')[0]; } catch {} }
if (!port) { console.error('chrome did not start'); proc.kill(); process.exit(2); }
const targets = await (await fetch(`http://127.0.0.1:${port}/json/list`)).json();
const ws = new WebSocket(targets.find(t => t.type === 'page').webSocketDebuggerUrl);
await new Promise(r => ws.addEventListener('open', r, { once: true }));
let id = 0; const pending = new Map(); const handlers = [];
ws.addEventListener('message', e => { const m = JSON.parse(e.data); if (m.id && pending.has(m.id)) { pending.get(m.id)(m); pending.delete(m.id); } else handlers.forEach(h => h(m)); });
const send = (method, params = {}) => new Promise((res, rej) => { const i = ++id; pending.set(i, m => m.error ? rej(new Error(method + ': ' + m.error.message)) : res(m.result)); ws.send(JSON.stringify({ id: i, method, params })); });
const failedCss = new Set();
try {
  await send('Page.enable'); await send('Runtime.enable');
  await send('Emulation.setDeviceMetricsOverride', { width, height, deviceScaleFactor: 1, mobile: false });
  if (flag('dark')) await send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-color-scheme', value: 'dark' }] });
  if (BLOCK_LINKED_CSS.test(path.resolve(page))) {
    await send('Fetch.enable', { patterns: [{ urlPattern: '*.css' }] });
    handlers.push(m => { if (m.method === 'Fetch.requestPaused') { failedCss.add(m.params.request.url); send('Fetch.failRequest', { requestId: m.params.requestId, errorReason: 'AccessDenied' }).catch(() => {}); } });
  }
  const loaded = new Promise(r => handlers.push(m => { if (m.method === 'Page.loadEventFired') r(); }));
  await send('Page.navigate', { url: pathToFileURL(path.resolve(page)).href });
  await loaded; await sleep(150);
  const ev = async expr => { const r = await send('Runtime.evaluate', { expression: expr, returnByValue: true, awaitPromise: true }); if (r.exceptionDetails) throw new Error(r.exceptionDetails.exception?.description || r.exceptionDetails.text); return r.result.value; };
  if (inject) await ev(`(()=>{const s=document.createElement('style');s.textContent=${JSON.stringify(fs.readFileSync(inject, 'utf8'))};document.head.appendChild(s);})()`);
  if (before) { await ev(`(async()=>{${before}})()`); await sleep(100); }
  const value = await ev(`(()=>(${evalExpr}))()`);
  const links = await ev(`[...document.querySelectorAll('link[rel=stylesheet]')].map(l=>({href:l.getAttribute('href'),url:l.href}))`);
  const linkedCss = links.map(l => ({ href: l.href, loaded: !failedCss.has(l.url) }));
  if (shot) { const r = await send('Page.captureScreenshot', { format: 'png' }); fs.writeFileSync(shot, Buffer.from(r.data, 'base64')); }
  console.log(JSON.stringify({ value, linkedCss, viewport: `${width}x${height}`, injected: inject || null }));
} catch (e) { console.error(String(e)); process.exitCode = 1; }
finally { ws.close(); proc.kill(); await sleep(300); try { fs.rmSync(udd, { recursive: true, force: true }); } catch {} }
