#!/usr/bin/env node
// Optional collector without Playwright: drives an installed Chrome or Edge over the
// DevTools protocol (Node 22+: global WebSocket and fetch; nothing to install).
//
// Two ways to run it:
//   collector  stdin JSON, stdout {captures, errors}: the same request and result as
//              capture.mjs (the runner's collector_command), used by capture.mjs itself when
//              no Playwright package is found
//   direct     node capture-cdp.mjs --url http://localhost:5173/ --sizes 1024x768,360x640
//                --out captures/ [--dpr 2] [--reduce-motion emulate|inject] [--dark]
//                [--settle 800] [--name home]
//              one full-page PNG per size and a summary JSON (stylesheets loaded, page errors)
//
// Browser: input.browser.executable, else CHROME_PATH, else the usual Chrome/Edge install
// paths. Headless, a fresh temporary profile, port 0 (never attaches to another debugger).
// Only a loopback preview (localhost, 127.0.0.1, [::1]) or a file: page is opened.
// Reduced motion: `emulate` sets the prefers-reduced-motion media feature (a real
// emulation); `inject` copies the page's own `prefers-reduced-motion: reduce` rules into a
// style element without the media condition, the substitute observation SKILL.md accepts,
// and its rendered lines are labelled `rendered (reduce injected)`.
import { spawn } from 'node:child_process';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { createHash } from 'node:crypto';
import { measureLayout } from './measure-layout.mjs';

const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

// the page's own `prefers-reduced-motion: reduce` rules, appended without the media condition
// (shared with capture.mjs); returns {rules, unreadable} (cross-origin sheets cannot be read)
export const REDUCE_INJECT_JS = `(() => { let rules = 0, unreadable = 0; const text = [];
  const walk = (list) => { for (const r of list) {
    if (r.media && /prefers-reduced-motion\\s*:\\s*reduce/.test(r.conditionText || r.media.mediaText)) {
      for (const inner of r.cssRules) { text.push(inner.cssText); rules += 1; } }
    else if (r.cssRules) walk(r.cssRules); } };
  for (const s of document.styleSheets) { try { walk(s.cssRules); } catch { unreadable += 1; } }
  const style = document.createElement('style'); style.dataset.joedesign = 'reduce-injected';
  style.textContent = text.join('\\n'); document.head.append(style); return {rules, unreadable}; })()`;

export function browserCandidates(env = process.env, platform = process.platform) {
  if (platform === 'win32') {
    const roots = [env.ProgramFiles, env['ProgramFiles(x86)'], env.LOCALAPPDATA].filter(Boolean);
    return roots.flatMap((r) => [path.win32.join(r, 'Google', 'Chrome', 'Application', 'chrome.exe'),
      path.win32.join(r, 'Microsoft', 'Edge', 'Application', 'msedge.exe')]);
  }
  if (platform === 'darwin') {
    return ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
      '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge',
      '/Applications/Chromium.app/Contents/MacOS/Chromium'];
  }
  return ['/usr/bin/google-chrome', '/usr/bin/google-chrome-stable', '/usr/bin/chromium',
    '/usr/bin/chromium-browser', '/usr/bin/microsoft-edge', '/usr/bin/microsoft-edge-stable', '/snap/bin/chromium'];
}

export function findBrowser(explicit, env = process.env) {
  if (explicit) {
    if (!fs.existsSync(explicit)) throw new Error(`browser executable not found: ${explicit}`);
    return explicit;
  }
  if (env.CHROME_PATH) {
    if (!fs.existsSync(env.CHROME_PATH)) throw new Error('CHROME_PATH does not name an existing file');
    return env.CHROME_PATH;
  }
  const found = browserCandidates(env).find((p) => fs.existsSync(p));
  if (!found) throw new Error('no Chrome or Edge found: set CHROME_PATH to a Chrome/Edge executable');
  return found;
}

export function allowedUrl(url) {
  const u = new URL(url);
  if (u.protocol === 'file:') return u;
  if (['http:', 'https:'].includes(u.protocol) && ['localhost', '127.0.0.1', '[::1]'].includes(u.hostname)) return u;
  throw new Error('Collector only operates an explicitly configured local preview');
}

export async function launch(executable) {
  if (typeof WebSocket !== 'function') throw new Error('Node 22 or later is needed (global WebSocket)');
  const exe = findBrowser(executable);
  const profile = fs.mkdtempSync(path.join(os.tmpdir(), 'joedesign-cdp-'));
  const proc = spawn(exe, ['--headless=new', '--remote-debugging-port=0', `--user-data-dir=${profile}`,
    '--no-first-run', '--no-default-browser-check', '--hide-scrollbars', '--mute-audio', 'about:blank'], { stdio: 'ignore' });
  let port;
  for (let i = 0; i < 100 && !port; i += 1) {
    try {
      port = Number(fs.readFileSync(path.join(profile, 'DevToolsActivePort'), 'utf8').trim().split(/\s+/)[0]);
    } catch { await sleep(150); }
  }
  if (!port) { proc.kill(); throw new Error('browser did not start (no DevToolsActivePort)'); }
  const version = await (await fetch(`http://127.0.0.1:${port}/json/version`)).json();
  return {
    product: version.Browser,
    async page() {
      const target = await (await fetch(`http://127.0.0.1:${port}/json/new?about:blank`, { method: 'PUT' })).json();
      return openPage(target.webSocketDebuggerUrl);
    },
    async close() {
      proc.kill();
      await sleep(300);
      try { fs.rmSync(profile, { recursive: true, force: true }); } catch { /* the profile may still be locked */ }
    },
  };
}

const KEYS = { Tab: [9, ''], Enter: [13, '\r'], Escape: [27, ''], ' ': [32, ' '], Space: [32, ' '],
  Backspace: [8, ''], Delete: [46, ''], ArrowLeft: [37, ''], ArrowUp: [38, ''], ArrowRight: [39, ''],
  ArrowDown: [40, ''], Home: [36, ''], End: [35, ''], PageUp: [33, ''], PageDown: [34, ''] };

async function openPage(wsUrl) {
  const ws = new WebSocket(wsUrl);
  await new Promise((resolve, reject) => { ws.onopen = resolve; ws.onerror = reject; });
  let id = 0;
  const pending = new Map();
  const listeners = [];
  ws.onmessage = (m) => {
    const msg = JSON.parse(m.data);
    if (msg.id && pending.has(msg.id)) {
      const { resolve, reject } = pending.get(msg.id);
      pending.delete(msg.id);
      if (msg.error) reject(new Error(msg.error.message)); else resolve(msg.result);
    } else if (msg.method) for (const l of [...listeners]) l(msg);
  };
  const send = (method, params = {}) => new Promise((resolve, reject) => {
    id += 1;
    pending.set(id, { resolve, reject });
    ws.send(JSON.stringify({ id, method, params }));
  });
  await send('Page.enable');
  await send('Runtime.enable');
  const errors = [];
  listeners.push((m) => {
    if (m.method === 'Runtime.exceptionThrown') {
      const d = m.params.exceptionDetails;
      errors.push(`${d.text} ${d.exception?.description ?? ''}`.trim());
    }
  });
  let viewport = [1024, 768];
  let scale = 1;
  const evaluate = async (expression) => {
    const r = await send('Runtime.evaluate', { expression, awaitPromise: true, returnByValue: true, timeout: 60000 });
    if (r.exceptionDetails) throw new Error(r.exceptionDetails.exception?.description ?? r.exceptionDetails.text);
    return r.result.value;
  };
  const center = async (selector) => {
    const box = await evaluate(`(() => { const el = document.querySelector(${JSON.stringify(selector)});
      if (!el) return null; el.scrollIntoView({block: 'center', inline: 'center'});
      const r = el.getBoundingClientRect(); return {x: r.left + r.width / 2, y: r.top + r.height / 2, w: r.width, h: r.height}; })()`);
    if (!box || !box.w || !box.h) throw new Error(`no visible element for ${selector}`);
    return box;
  };
  const mouse = (type, x, y, extra = {}) => send('Input.dispatchMouseEvent', { type, x, y, ...extra });
  const page = {
    errors,
    send,
    // measure-layout.mjs calls page.evaluate(fn, arg)
    evaluate: (fn, arg) => evaluate(typeof fn === 'function' ? `(${fn})(${JSON.stringify(arg)})` : fn),
    async setup({ width, height, dpr = 1, theme = 'light', reduce = false, locale }) {
      viewport = [width, height];
      scale = dpr;
      await send('Emulation.setDeviceMetricsOverride', { width, height, deviceScaleFactor: dpr, mobile: false });
      await send('Emulation.setEmulatedMedia', { features: [
        { name: 'prefers-color-scheme', value: theme === 'dark' ? 'dark' : 'light' },
        { name: 'prefers-reduced-motion', value: reduce ? 'reduce' : 'no-preference' }] });
      if (locale) { try { await send('Emulation.setLocaleOverride', { locale }); } catch { /* unsupported locale */ } }
    },
    async goto(url, settle = 500) {
      const loaded = new Promise((resolve) => {
        const l = (m) => { if (m.method === 'Page.loadEventFired') { listeners.splice(listeners.indexOf(l), 1); resolve(); } };
        listeners.push(l);
      });
      const r = await send('Page.navigate', { url });
      if (r.errorText) throw new Error(`navigation failed: ${r.errorText}`);
      await Promise.race([loaded, sleep(30000)]);
      await evaluate('document.fonts ? document.fonts.ready.then(() => true) : true');
      await sleep(settle);
    },
    url: () => evaluate('location.href'),
    stylesheets: () => evaluate(`[...document.styleSheets].map((s) => s.href || 'inline')`),
    // the page's own prefers-reduced-motion: reduce rules, applied without the media condition
    injectReduce: () => evaluate(REDUCE_INJECT_JS),
    async click(selector) {
      const { x, y } = await center(selector);
      await mouse('mouseMoved', x, y);
      await mouse('mousePressed', x, y, { button: 'left', clickCount: 1 });
      await mouse('mouseReleased', x, y, { button: 'left', clickCount: 1 });
    },
    async hover(selector) {
      const { x, y } = await center(selector);
      await mouse('mouseMoved', x, y);
    },
    async fill(selector, value) {
      await center(selector);
      await evaluate(`(() => { const el = document.querySelector(${JSON.stringify(selector)}); el.focus();
        if (typeof el.select === 'function') el.select(); })()`);
      await send('Input.insertText', { text: String(value) });
    },
    async press(key, selector) {
      if (selector) await evaluate(`document.querySelector(${JSON.stringify(selector)})?.focus()`);
      const [code, text] = KEYS[key] || [key.length === 1 ? key.toUpperCase().charCodeAt(0) : 0, key.length === 1 ? key : ''];
      const base = { key: key === 'Space' ? ' ' : key, windowsVirtualKeyCode: code, nativeVirtualKeyCode: code };
      await send('Input.dispatchKeyEvent', { type: text ? 'keyDown' : 'rawKeyDown', ...base, ...(text ? { text } : {}) });
      await send('Input.dispatchKeyEvent', { type: 'keyUp', ...base });
    },
    async wheel(dx, dy) {
      await mouse('mouseWheel', viewport[0] / 2, viewport[1] / 2, { deltaX: dx, deltaY: dy });
      await sleep(100);
    },
    async shot(file, { full = false } = {}) {
      let params = { format: 'png' };
      if (full) {
        const m = await send('Page.getLayoutMetrics');
        const size = m.cssContentSize || m.contentSize;
        const height = Math.min(Math.max(Math.ceil(size.height), viewport[1]), 16000);
        const width = Math.max(Math.ceil(size.width), viewport[0]);
        params = { ...params, captureBeyondViewport: true, clip: { x: 0, y: 0, width, height, scale: 1 } };
      }
      const r = await send('Page.captureScreenshot', params);
      fs.mkdirSync(path.dirname(file), { recursive: true });
      fs.writeFileSync(file, Buffer.from(r.data, 'base64'));
      return file;
    },
    state: (selector) => evaluate(`(() => { const all = [...document.querySelectorAll(${JSON.stringify(selector)})];
      const el = all[0]; const visible = (e) => { const r = e.getBoundingClientRect(), s = getComputedStyle(e);
        return r.width > 0 && r.height > 0 && s.visibility !== 'hidden' && s.display !== 'none'; };
      return {count: all.length, visible: !!el && visible(el), text: el ? el.innerText : null,
        focused: !!el && el === document.activeElement}; })()`),
    focus: () => evaluate(`({tag: document.activeElement?.tagName, id: document.activeElement?.id,
      visible: document.activeElement?.matches(':focus-visible')})`),
    close: () => ws.close(),
    get scale() { return scale; },
  };
  return page;
}

const hash = (file) => createHash('sha256').update(fs.readFileSync(file)).digest('hex');

// the capture.mjs contract: same request in, same {captures, errors} out
export async function collect(input) {
  const base = allowedUrl(input.browser.base_url);
  if (base.protocol === 'file:') throw new Error('Collector only operates an explicitly configured local preview');
  const out = path.resolve(input.output_dir);
  fs.mkdirSync(out, { recursive: true });
  const captures = [];
  const errors = [];
  const browser = await launch(input.browser.executable);
  try {
    for (const [index, target] of input.targets.entries()) {
      const probe = input.browser.probes?.[target.id];
      if (!probe || !Array.isArray(probe.assertions) || probe.assertions.length === 0) {
        errors.push({ target_id: target.id, error: 'State assertions required' });
        continue;
      }
      const url = new URL(target.route, base);
      if (url.origin !== base.origin) throw new Error('Target escapes configured preview origin');
      const page = await browser.page();
      const log = { target, requested_url: url.href, build_id: input.build_id, actions: [], assertions: [],
        console_errors: page.errors, frames: [], motion_observation: 'FRAME_SAMPLES_ONLY',
        driver: 'cdp', browser: browser.product, reduced_motion: probe.reduced_motion ? 'emulated' : 'no-preference' };
      const frame = async (suffix) => {
        const file = path.join(out, `${index}-${suffix}.png`);
        await page.shot(file);
        log.frames.push(file);
        return file;
      };
      try {
        await page.setup({ width: target.viewport[0], height: target.viewport[1], dpr: input.browser.device_scale_factor || 1,
          theme: target.theme, reduce: probe.reduced_motion === true, locale: target.locale });
        await page.goto(url.href, input.browser.settle_ms ?? 300);
        log.stylesheets = await page.stylesheets();
        if (probe.reduced_motion === 'inject') {
          log.reduced_motion = 'injected';
          log.reduce_injection = await page.injectReduce();
        }
        await frame('start');
        for (const [n, action] of (probe.actions || []).entries()) {
          if (action.type === 'click') await page.click(action.selector);
          else if (action.type === 'fill') await page.fill(action.selector, action.value);
          else if (action.type === 'press') await page.press(action.key, action.selector);
          else if (action.type === 'hover') await page.hover(action.selector);
          else if (action.type === 'scroll') await page.wheel(action.x || 0, action.y || 0);
          else if (action.type === 'wait') {
            if (!Number.isInteger(action.ms) || action.ms < 0 || action.ms > 10000) throw new Error('Invalid observation wait');
            await sleep(action.ms);
          } else throw new Error(`Unsupported action: ${action.type}`);
          await sleep(50);
          log.actions.push({ ...action, focus: await page.focus() });
          await frame(`action-${n}`);
        }
        for (const assertion of probe.assertions) {
          if (assertion.visible === undefined && assertion.text === undefined && assertion.count === undefined && assertion.focused === undefined) {
            throw new Error('Assertion needs visible, text, count or focused');
          }
          let state = await page.state(assertion.selector);
          if (assertion.visible !== undefined) {
            for (let t = 0; state.visible !== assertion.visible && t < 100; t += 1) {
              await sleep(100);
              state = await page.state(assertion.selector);
            }
            if (state.visible !== assertion.visible) throw new Error(`Visibility assertion failed: ${assertion.selector}`);
          }
          if (assertion.text !== undefined && !(state.text ?? '').includes(assertion.text)) {
            throw new Error(`Text assertion failed: ${assertion.selector}`);
          }
          if (assertion.count !== undefined && state.count !== assertion.count) throw new Error(`Count assertion failed: ${assertion.selector}`);
          if (assertion.focused !== undefined && state.focused !== assertion.focused) throw new Error(`Focus assertion failed: ${assertion.selector}`);
          log.assertions.push(assertion);
        }
        log.actual_url = await page.url();
        if (input.design) {
          log.design = { baseline_sha256: input.design.baseline_sha256, input_fingerprints: input.design.input_fingerprints,
            measurements: await measureLayout(page, input.design.checks.filter((c) => c.target_id === target.id)) };
        }
        if (new URL(log.actual_url).origin !== base.origin) throw new Error('Preview navigated outside configured origin');
        const screenshot = await frame('result');
        const full = path.join(out, `${index}-full.png`);
        await page.shot(full, { full: true });
        log.frames.push(full);
        log.frame_hashes = Object.fromEntries(log.frames.map((p) => [p, hash(p)]));
        const record = path.join(out, `${index}-observation.json`);
        fs.writeFileSync(record, JSON.stringify(log, null, 2));
        captures.push({ target_id: target.id, kind: 'render', path: screenshot, action: '',
          result: 'Configured state predicates observed', frames: log.frames });
        if (log.actions.some((a) => a.type !== 'wait')) {
          captures.push({ target_id: target.id, kind: 'interaction', path: record,
            action: JSON.stringify(log.actions), result: JSON.stringify(log.assertions), frames: log.frames });
        }
        captures.push({ target_id: target.id, kind: 'technical', path: record,
          action: 'browser diagnostics', result: JSON.stringify(log.console_errors), frames: [] });
      } catch (error) {
        errors.push({ target_id: target.id, error: String(error) });
        fs.writeFileSync(path.join(out, `${index}-failed.json`), JSON.stringify(log, null, 2));
      } finally {
        page.close();
      }
    }
  } finally {
    await browser.close();
  }
  return { captures, errors };
}

// direct: full-page captures of one page at several sizes
export async function tour(options) {
  const url = allowedUrl(options.url);
  const out = path.resolve(options.out);
  fs.mkdirSync(out, { recursive: true });
  const browser = await launch(options.executable);
  const summary = { url: url.href, browser: browser.product, dpr: options.dpr, theme: options.theme,
    reduced_motion: options.reduce || 'no-preference', captures: [] };
  try {
    for (const [width, height] of options.sizes) {
      const page = await browser.page();
      try {
        await page.setup({ width, height, dpr: options.dpr, theme: options.theme, reduce: options.reduce === 'emulate' });
        await page.goto(url.href, options.settle);
        const entry = { size: `${width}x${height}`, stylesheets: await page.stylesheets() };
        if (options.reduce === 'inject') entry.reduce_injection = await page.injectReduce();
        if (options.reduce) await page.evaluate('new Promise((r) => requestAnimationFrame(() => requestAnimationFrame(r)))');
        const file = path.join(out, `${options.name}-${width}x${height}${options.dpr !== 1 ? `@${options.dpr}x` : ''}` +
          `${options.reduce ? `-reduce-${options.reduce}` : ''}-full.png`);
        await page.shot(file, { full: true });
        entry.path = path.relative(process.cwd(), file).split(path.sep).join('/');
        entry.sha256 = hash(file);
        entry.page_errors = [...page.errors];
        if (options.probe) entry.probe = await page.evaluate(options.probe);
        summary.captures.push(entry);
      } finally {
        page.close();
      }
    }
  } finally {
    await browser.close();
  }
  return summary;
}

function parseArgs(argv) {
  const o = { sizes: [[1024, 768], [360, 640]], dpr: 1, theme: 'light', reduce: '', settle: 500, name: 'page' };
  for (let i = 0; i < argv.length; i += 1) {
    const a = argv[i];
    const v = () => { i += 1; if (i >= argv.length) throw new Error(`${a} needs a value`); return argv[i]; };
    if (a === '--url') o.url = v();
    else if (a === '--out') o.out = v();
    else if (a === '--sizes') {
      o.sizes = v().split(',').map((s) => s.split('x').map(Number));
      if (o.sizes.some((s) => s.length !== 2 || s.some((n) => !Number.isInteger(n) || n < 1))) throw new Error('--sizes is WxH,WxH');
    } else if (a === '--dpr') o.dpr = Number(v());
    else if (a === '--dark') o.theme = 'dark';
    else if (a === '--reduce-motion') {
      o.reduce = v();
      if (!['emulate', 'inject'].includes(o.reduce)) throw new Error('--reduce-motion is emulate or inject');
    } else if (a === '--settle') o.settle = Number(v());
    else if (a === '--name') o.name = v();
    else if (a === '--probe') o.probe = v();
    else if (a === '--browser') o.executable = v();
    else throw new Error(`unknown option ${a}`);
  }
  if (!o.url || !o.out) throw new Error('--url and --out are required');
  return o;
}

async function main(argv) {
  if (argv.length) {
    let options;
    try { options = parseArgs(argv); } catch (error) {
      process.stderr.write(`capture-cdp: ${error.message}\nusage: node capture-cdp.mjs --url URL --out DIR ` +
        '[--sizes 1024x768,360x640] [--dpr 2] [--reduce-motion emulate|inject] [--dark] [--settle ms] [--name page] ' +
        '[--probe JS] [--browser PATH]   (or a capture.mjs request on stdin)\n');
      return 2;
    }
    const summary = await tour(options);
    fs.writeFileSync(path.join(path.resolve(options.out), `${options.name}-summary.json`), `${JSON.stringify(summary, null, 1)}\n`);
    process.stdout.write(`${JSON.stringify(summary, null, 1)}\n`);
    return summary.captures.some((c) => c.page_errors.length) ? 1 : 0;
  }
  const input = JSON.parse(fs.readFileSync(0, 'utf8'));
  process.stdout.write(JSON.stringify(await collect(input)));
  return 0;
}

if (process.argv[1] && import.meta.url.endsWith(process.argv[1].replace(/\\/g, '/').split('/').pop())) {
  main(process.argv.slice(2)).then((code) => { process.exitCode = code; }, (error) => {
    process.stderr.write(`capture-cdp: ${error.message}\n`);
    process.exitCode = 2;
  });
}
