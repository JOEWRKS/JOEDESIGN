// truth.mjs : measuring instrument for this run. Visible gap = next block's top - (box bottom + hard drop shadow), expected S1 = 16 (12 when width<=700 or height<=700).
// 간격 규칙 검사 (DESIGN.md "간격 규칙" 표의 S1~S6). 빌드한 앱을 실제 Chrome으로 열어 상태별 렌더 상자를 잰다.
// 준비: npx vite build → npx vite preview --host 127.0.0.1 --port <포트> --strictPort
// 실행: GOMOKU_DEV_PORT=<포트> node work/design/spacing-check.mjs [--sizes 1440x900,390x844] [--shots <폴더>]
// 엔진 파일 없이 돌도록 engine-worker.js 요청을 합성 엔진(fake-engine-worker.js)으로 바꾼다. 승률 숫자는 합성값.
// 기대값은 CSS에서 읽지 않고 아래 RULES(=DESIGN 표)에서 정한다. 위반이 하나라도 있으면 종료 코드 1.
import { chromium } from '@playwright/test';
import { readFileSync, mkdirSync } from 'node:fs';
import { fileURLToPath } from 'node:url';

const arg = name => { const i = process.argv.indexOf(name); return i > 0 ? process.argv[i + 1] : undefined; };
const ALL_SIZES = [[1920, 1080], [1440, 900], [1366, 768], [1280, 720], [1024, 768], [820, 1180], [768, 1024], [489, 866], [430, 932], [390, 844], [375, 667], [360, 640]];
const sizes = arg('--sizes') ? arg('--sizes').split(',').map(s => s.split('x').map(Number)) : ALL_SIZES;
const shots = arg('--shots'); if (shots) mkdirSync(shots, { recursive: true });
const port = process.env.GOMOKU_DEV_PORT; if (!port) { console.error('GOMOKU_DEV_PORT가 필요합니다'); process.exit(2); }
const fake = readFileSync(fileURLToPath(new URL('./fake-engine-worker.js', import.meta.url)), 'utf8');
const rowsOut = [];

/** DESIGN.md 간격 규칙 표의 값. 화면 크기에 따라 줄이는 값도 여기서만 정한다. */
const RULES = (w, h) => ({
  tight: 4, inner: 8, inline: 10, inlineCompact: 8,
  stack: w <= 700 || h <= 700 ? 12 : 16,
  section: h <= 720 ? 12 : 24,
  card: w <= 700 ? [12, 14] : [18, 22], cardCompact: [10, 14],
  small: w <= 700 ? [8, 12] : [10, 16],
});

const measure = (page, rules) => page.evaluate(R => {
  const out = [], tol = 1;
  const shown = el => { if (!el || el.closest('[hidden]')) return false; const s = getComputedStyle(el), r = el.getBoundingClientRect(); return s.display !== 'none' && s.visibility !== 'hidden' && r.width > 0 && r.height > 0; };
  const kids = el => [...el.children].filter(shown);
  const name = el => el.id ? `#${el.id}` : `.${[...el.classList].join('.')}`;
  // 입체 그림자: 흐림 0인 바깥 그림자의 아래쪽 깊이(offsetY + spread)
  const depth = el => { let d = 0; for (const part of getComputedStyle(el).boxShadow.split(/,(?![^(]*\))/)) { if (part.includes('inset') || part === 'none') continue; const n = (part.replace(/rgba?\([^)]*\)/g, '').match(/-?[\d.]+px/g) ?? []).map(parseFloat); if (n.length >= 2 && (n[2] ?? 0) === 0) d = Math.max(d, n[1] + (n[3] ?? 0)); } return d; };
  const vBottom = el => Math.max(el.getBoundingClientRect().bottom + depth(el), ...kids(el).filter(k => !k.closest('#board')).map(vBottom));
  const check = (rule, where, got, want) => { const ok = Math.abs(got - want) <= tol; out.push({ rule, where, got: Math.round(got * 10) / 10, want, ok }); };
  const vstack = (rule, container, want) => { const list = kids(container).sort((a, b) => a.getBoundingClientRect().top - b.getBoundingClientRect().top);
    for (let i = 1; i < list.length; i++) check(rule, `${name(list[i - 1])}→${name(list[i])}`, list[i].getBoundingClientRect().top - vBottom(list[i - 1]), typeof want === 'function' ? want(list[i - 1], list[i]) : want); };
  const app = document.querySelector('#app'), intro = app.dataset.phase === 'intro';
  const hud = document.querySelector('.hud'), cta = document.querySelector('.cta-area');
  const hudItems = kids(hud), ctaItems = kids(cta);
  // S1 쌓기: 말풍선 영역·버튼 영역 안의 세로 간격
  vstack('S1 stack', hud, R.stack); vstack('S1 stack', cta, R.stack);
  const board = document.querySelector('.board');
  if (!intro && hudItems.length && hud.getBoundingClientRect().top > board.getBoundingClientRect().bottom) check('S1 stack', '.board→' + name(hudItems[0]), hudItems[0].getBoundingClientRect().top - vBottom(board), R.stack);
  if (intro) {
    const title = document.querySelector('#title-screen');
    check('S2 section', '#title-screen→' + name(hudItems[0]), hudItems[0].getBoundingClientRect().top - vBottom(title), R.section);
    check('S1 stack', name(hudItems.at(-1)) + '→' + name(ctaItems[0]), ctaItems[0].getBoundingClientRect().top - vBottom(hudItems.at(-1)), R.stack);
  }
  // S3 카드 안쪽 여백: 위=아래, 왼=오른쪽, 값은 카드 종류별
  const hudContentH = hud.clientHeight - 8;
  for (const [sel, pad] of [['#current-card', !intro && hudContentH <= 330 ? R.cardCompact : R.card], ['#tutorial', R.card], ['#review-card', R.small], ['#replay-controls', R.small]]) {
    const card = document.querySelector(sel); if (!shown(card)) continue;
    const r = card.getBoundingClientRect(), s = getComputedStyle(card), list = kids(card);
    const inner = { top: r.top + parseFloat(s.borderTopWidth), bottom: r.bottom - parseFloat(s.borderBottomWidth), left: r.left + parseFloat(s.borderLeftWidth), right: r.right - parseFloat(s.borderRightWidth) };
    check('S3 inset', `${sel} 위`, Math.min(...list.map(k => k.getBoundingClientRect().top)) - inner.top, pad[0]);
    check('S3 inset', `${sel} 아래`, inner.bottom - Math.max(...list.map(vBottom)), pad[0]);
    check('S3 inset', `${sel} 왼쪽`, Math.min(...list.map(k => k.getBoundingClientRect().left)) - inner.left, pad[1]);
    // 오른쪽은 폭을 채우는 묶음으로만 잰다(라벨처럼 글자 폭만큼인 것만 있으면 잴 대상 없음)
    const full = list.filter(k => !['flex-start', 'start'].includes(getComputedStyle(k).alignSelf));
    if (full.length) check('S3 inset', `${sel} 오른쪽`, inner.right - Math.max(...full.map(k => k.getBoundingClientRect().right)), pad[1]);
  }
  // S4 카드 안 묶음: 보조 줄은 tight, 나머지 inner
  const tightPairs = new Set(['#hero→#hero-sub', '#card-title→#card-text', '.small→#review-text', '#review-text→#review-context']);
  const inCard = (a, b) => tightPairs.has(`${name(a)}→${name(b)}`) ? R.tight : R.inner;
  for (const sel of ['#current-card', '#review-card', '#tutorial', '#setup']) { const c = document.querySelector(sel); if (shown(c)) vstack('S4 in-card', c, inCard); }
  // S5 한 줄 버튼 사이(가로)
  const compactCta = cta.clientWidth <= 380;
  for (const row of document.querySelectorAll('.turn-actions, .alts, .setup-row, .replay-buttons, .tut-actions')) {
    if (!shown(row)) continue;
    const list = kids(row).sort((a, b) => a.getBoundingClientRect().left - b.getBoundingClientRect().left);
    const want = row.matches('.turn-actions.with-mini') && compactCta ? R.inlineCompact : R.inline;
    for (let i = 1; i < list.length; i++) { const a = list[i - 1].getBoundingClientRect(), b = list[i].getBoundingClientRect(); if (Math.abs(a.top - b.top) > a.height / 2) continue; check('S5 inline', `${name(row)} ${name(list[i - 1])}→${name(list[i])}`, b.left - a.right, want); }
  }
  // S6 한 화면: 규칙을 맞춘 뒤에도 세로·가로 스크롤이 생기지 않는다
  out.push({ rule: 'S6 no-scroll', where: 'page', got: `${document.documentElement.scrollWidth}x${document.documentElement.scrollHeight}`, want: `${innerWidth}x${innerHeight}`, ok: document.documentElement.scrollWidth <= innerWidth && document.documentElement.scrollHeight <= innerHeight + 1 });
  // 간격을 넓혀 말풍선·버튼 영역 안에서 가로로 삐져나간 요소가 없는지(overflow:hidden이라 페이지 스크롤로는 안 보임)
  const spill = [hud, cta].flatMap(c => { const cr = c.getBoundingClientRect(); return [...c.querySelectorAll('*')].filter(e => shown(e) && e.getBoundingClientRect().right > cr.right + 1).map(name); });
  out.push({ rule: 'S6 no-scroll', where: 'hud/cta 가로 넘침', got: spill.slice(0, 3).join(' ') || '없음', want: '없음', ok: !spill.length });
  return out;
}, rules);

const browser = await chromium.launch({ channel: 'chrome' });
let fails = 0, total = 0; const perRule = {};
for (const [w, h] of sizes) {
  const mobile = w < 700, rules = RULES(w, h);
  const page = await browser.newPage({ viewport: { width: w, height: h }, hasTouch: mobile, isMobile: mobile });
  await page.route('**/engine/engine-worker.js', r => r.fulfill({ contentType: 'text/javascript', body: fake }));
  const errors = []; page.on('pageerror', e => errors.push(e.message));
  const tap = s => mobile ? page.tap(s) : page.click(s);
  const run = async state => {
    await page.evaluate(() => document.fonts.ready); await page.waitForTimeout(150);
    if (shots) await page.screenshot({ path: `${shots}/spacing-${w}x${h}-${state}.png` });
    for (const r of await measure(page, rules)) {
      total++; perRule[r.rule] ??= [0, 0]; perRule[r.rule][0]++;
      if (!r.ok) { fails++; perRule[r.rule][1]++; }
      if (r.rule === 'S1 stack') rowsOut.push(`${w}x${h} ${state} ${r.where} = ${r.got} (${r.want})${r.ok ? '' : ' X'}`);
    }
  };
  await page.goto(`http://127.0.0.1:${port}/`); await page.waitForSelector('#app[data-engine="ready"]', { timeout: 30000 });
  await tap('#color-black'); await tap('#strength-normal'); await run('intro');
  await tap('#main-action'); await page.waitForSelector('.coach .mark.m1'); await run('tutorial');
  await tap('#tut-skip'); await tap('[data-coord="H8"]'); await tap('[data-coord="H8"]');
  await page.waitForSelector('#app[data-ply="2"][data-phase="human"]'); await page.waitForSelector('.coach .mark.m1'); await run('candidates');
  const free = await page.evaluate(() => ['J10', 'G6', 'K11', 'F5', 'L4'].find(c => { const el = document.querySelector(`[data-coord="${c}"]`); return !el.classList.contains('black') && !el.classList.contains('white') && !el.classList.contains('has-coach'); }));
  await tap(`[data-coord="${free}"]`); await page.waitForSelector('.coach .ghost-stone'); await run('preview');
  await tap('#cancel-preview'); await tap('#guide-toggle'); await run('guide-off'); await tap('#guide-toggle');
  await tap('#undo-button'); await page.waitForSelector('#undo-notice:not([hidden])'); await page.waitForSelector('.coach .mark.m1'); await run('undo');
  if (errors.length) { fails++; console.log(`FAIL ${w}x${h} 페이지 오류`, errors); }
  await page.close();
}
await browser.close();
console.log(rowsOut.join(String.fromCharCode(10)));
console.log(Object.entries(perRule).map(([k, [n, f]]) => `${k}: ${n - f}/${n}`).join(' · '));
console.log(fails ? `간격 검사 실패 ${fails}건 / ${total}` : `간격 검사 통과 ${total}건 (${sizes.length}크기 × 6상태)`);
process.exit(fails ? 1 : 0);
