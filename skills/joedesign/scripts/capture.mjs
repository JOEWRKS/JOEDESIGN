// Optional collector: use an existing Playwright package and browser, never install.
import fs from 'node:fs';
import path from 'node:path';
import {createRequire} from 'node:module';
import {createHash} from 'node:crypto';
import {measureLayout} from './measure-layout.mjs';

const require = createRequire(import.meta.url);
const input = JSON.parse(fs.readFileSync(0, 'utf8'));
const base = new URL(input.browser.base_url);
if (!['http:', 'https:'].includes(base.protocol) || !['localhost', '127.0.0.1', '[::1]'].includes(base.hostname)) {
  throw new Error('Collector only operates an explicitly configured local preview');
}
const {chromium} = require(input.browser.playwright_module || 'playwright');
const out = path.resolve(input.output_dir);
fs.mkdirSync(out, {recursive: true});
const captures = [], errors = [];
const browser = await chromium.launch({headless: true,
  ...(input.browser.executable ? {executablePath: input.browser.executable} : {})});
try {
  for (const [index, target] of input.targets.entries()) {
    const probe = input.browser.probes?.[target.id];
    if (!probe || !Array.isArray(probe.assertions) || probe.assertions.length === 0) {
      errors.push({target_id: target.id, error: 'State assertions required'});
      continue;
    }
    const url = new URL(target.route, base);
    if (url.origin !== base.origin) throw new Error('Target escapes configured preview origin');
    const context = await browser.newContext({viewport: {width: target.viewport[0], height: target.viewport[1]},
      locale: target.locale, colorScheme: target.theme === 'dark' ? 'dark' : 'light',
      reducedMotion: probe.reduced_motion ? 'reduce' : 'no-preference'});
    const page = await context.newPage();
    const log = {target, requested_url: url.href, build_id: input.build_id, actions: [], assertions: [],
      console_errors: [], frames: [], motion_observation: 'FRAME_SAMPLES_ONLY'};
    page.on('pageerror', error => log.console_errors.push(String(error)));
    const frame = async suffix => {
      const file = path.join(out, `${index}-${suffix}.png`);
      await page.screenshot({path: file, animations: 'allow'});
      log.frames.push(file);
      return file;
    };
    try {
      await page.goto(url.href, {waitUntil: 'load', timeout: 30000});
      await page.evaluate(() => document.fonts.ready);
      await frame('start');
      for (const [n, action] of (probe.actions || []).entries()) {
        const locator = action.selector ? page.locator(action.selector) : null;
        if (action.type === 'click') await locator.click();
        else if (action.type === 'fill') await locator.fill(action.value);
        else if (action.type === 'press') {
          if (locator) await locator.press(action.key);
          else await page.keyboard.press(action.key);
        }
        else if (action.type === 'hover') await locator.hover();
        else if (action.type === 'scroll') await page.mouse.wheel(action.x || 0, action.y || 0);
        else if (action.type === 'wait') {
          if (!Number.isInteger(action.ms) || action.ms < 0 || action.ms > 10000) throw new Error('Invalid observation wait');
          await page.waitForTimeout(action.ms);
        } else throw new Error('Unsupported action: ' + action.type);
        const focus = await page.evaluate(() => ({tag: document.activeElement?.tagName,
          id: document.activeElement?.id, visible: document.activeElement?.matches(':focus-visible')}));
        log.actions.push({...action, focus});
        await frame(`action-${n}`);
      }
      for (const assertion of probe.assertions) {
        const locator = page.locator(assertion.selector);
        if (assertion.visible !== undefined) {
          await locator.waitFor({state: assertion.visible ? 'visible' : 'hidden', timeout: 10000});
        }
        if (assertion.text !== undefined && !(await locator.innerText()).includes(assertion.text)) {
          throw new Error('Text assertion failed: ' + assertion.selector);
        }
        if (assertion.count !== undefined && await locator.count() !== assertion.count) {
          throw new Error('Count assertion failed: ' + assertion.selector);
        }
        if (assertion.focused !== undefined && await locator.evaluate(el => el === document.activeElement) !== assertion.focused) {
          throw new Error('Focus assertion failed: ' + assertion.selector);
        }
        if (assertion.visible === undefined && assertion.text === undefined && assertion.count === undefined && assertion.focused === undefined) {
          throw new Error('Assertion needs visible, text, count or focused');
        }
        log.assertions.push(assertion);
      }
      log.actual_url = page.url();
      if (input.design) {
        log.design = {baseline_sha256: input.design.baseline_sha256,
          input_fingerprints: input.design.input_fingerprints,
          measurements: await measureLayout(page, input.design.checks.filter(c=>c.target_id===target.id))};
      }
      if (new URL(log.actual_url).origin !== base.origin) throw new Error('Preview navigated outside configured origin');
      const screenshot = await frame('result');
      const full = path.join(out, `${index}-full.png`);
      await page.screenshot({path: full, fullPage: true, animations: 'allow'});
      log.frames.push(full);
      log.frame_hashes = Object.fromEntries(log.frames.map(p=>[p,createHash('sha256').update(fs.readFileSync(p)).digest('hex')]));
      const record = path.join(out, `${index}-observation.json`);
      fs.writeFileSync(record, JSON.stringify(log, null, 2));
      captures.push({target_id: target.id, kind: 'render', path: screenshot,
        action: '', result: 'Configured state predicates observed', frames: log.frames});
      if (log.actions.some(a => a.type !== 'wait')) {
        captures.push({target_id: target.id, kind: 'interaction', path: record,
          action: JSON.stringify(log.actions), result: JSON.stringify(log.assertions), frames: log.frames});
      }
      // Browser diagnostics are technical evidence of this capture, not a test suite PASS.
      captures.push({target_id: target.id, kind: 'technical', path: record,
        action: 'browser diagnostics', result: JSON.stringify(log.console_errors), frames: []});
    } catch (error) {
      errors.push({target_id: target.id, error: String(error)});
      fs.writeFileSync(path.join(out, `${index}-failed.json`), JSON.stringify(log, null, 2));
    } finally {
      await context.close();
    }
  }
} finally {
  await browser.close();
}
process.stdout.write(JSON.stringify({captures, errors}));
