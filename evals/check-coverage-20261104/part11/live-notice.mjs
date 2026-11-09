// live-notice.mjs <trialRoot> <port> : serve the trial's built dist, force the two notice rows visible with real text, measure their height at 390x844 and 1440x900; also .bubble .caption font size.
import { spawn } from 'node:child_process';
import { chromium } from 'playwright';
const [root, port] = process.argv.slice(2);
const srv = spawn(process.execPath, [root + '/node_modules/vite/bin/vite.js', 'preview', '--host', '127.0.0.1', '--port', port, '--strictPort'], { cwd: root, stdio: 'ignore' });
await new Promise(r => setTimeout(r, 2500));
const browser = await chromium.launch({ channel: 'chrome' });
const out = {};
for (const [w, h] of [[390, 844], [1440, 900]]) {
  const page = await browser.newPage({ viewport: { width: w, height: h } });
  await page.goto(`http://127.0.0.1:${port}/`, { waitUntil: 'load' });
  await page.waitForTimeout(800);
  out[`${w}x${h}`] = await page.evaluate(() => {
    const r = {};
    for (const sel of ['.forbid-notice', '.engine-alert']) {
      const el = document.querySelector(sel); if (!el) { r[sel] = 'missing'; continue; }
      el.hidden = false; el.removeAttribute('hidden'); el.style.display = ''; el.textContent = sel === '.forbid-notice' ? '여기는 3·3 금수 자리라 둘 수 없어요.' : '엔진을 다시 띄우는 중이에요…';
      const cs = getComputedStyle(el); const b = el.getBoundingClientRect();
      r[sel] = { height: Math.round(b.height * 10) / 10, padding: cs.padding, lineHeight: cs.lineHeight, display: cs.display, visible: b.width > 0 };
    }
    const cap = document.querySelector('.bubble .caption, #current-card .caption');
    r.caption = cap ? getComputedStyle(cap).fontSize : 'missing';
    r.replayResult = document.querySelector('#replay-result') ? getComputedStyle(document.querySelector('#replay-result')).fontSize : 'missing';
    return r;
  });
  await page.close();
}
await browser.close(); srv.kill();
console.log(JSON.stringify(out));
