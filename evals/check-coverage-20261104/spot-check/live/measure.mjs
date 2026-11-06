// measure.mjs <port> : second instrument (m.js from 2026-11-05): lowest painted edge incl. drop shadow -> next block top, start screen + synthetic all-blocks state
import { chromium } from '@playwright/test';
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
const port = process.argv[2]; const m = readFileSync(fileURLToPath(new URL('../live/m.js', import.meta.url)), 'utf8');
const browser = await chromium.launch({ channel: 'chrome' });
for (const [w, h] of [[1440, 900], [390, 844]]) {
  const page = await browser.newPage({ viewport: { width: w, height: h }, hasTouch: w < 700, isMobile: w < 700 });
  await page.goto(`http://127.0.0.1:${port}/`); await page.waitForSelector('#app'); await page.evaluate(() => document.fonts.ready); await page.waitForTimeout(800);
  await page.addScriptTag({ content: m }); console.log(await page.evaluate(() => window.__run())); await page.close();
}
await browser.close();
