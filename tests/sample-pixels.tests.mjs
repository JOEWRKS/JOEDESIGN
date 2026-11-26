// node --test tests/sample-pixels.tests.mjs : the pixel sampler reads a capture's stroke colour as a spread.
import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { deflateSync } from 'node:zlib';
import { execFileSync, spawnSync } from 'node:child_process';
import { decodePng, sample, compare, contrast, format, parseHex } from '../skills/joedesign/scripts/sample-pixels.mjs';

const SCRIPT = new URL('../skills/joedesign/scripts/sample-pixels.mjs', import.meta.url);
// ATELIER Stage 1 capture (copied): 160x44 crop of the sold-out size chips M and L, the C1 row's spot check
const CHIPS = new URL('../fixtures/sample-pixels/scr002-360x640-soldout-chips-M-L.png', import.meta.url);

function crc32(buffer) {
  let c;
  let crc = 0xffffffff;
  for (const byte of buffer) {
    c = (crc ^ byte) & 0xff;
    for (let k = 0; k < 8; k += 1) c = c & 1 ? 0xedb88320 ^ (c >>> 1) : c >>> 1;
    crc = (crc >>> 8) ^ c;
  }
  return (crc ^ 0xffffffff) >>> 0;
}
function chunk(type, body) {
  const head = Buffer.alloc(8);
  head.writeUInt32BE(body.length, 0);
  head.write(type, 4, 'latin1');
  const crc = Buffer.alloc(4);
  crc.writeUInt32BE(crc32(Buffer.concat([Buffer.from(type, 'latin1'), body])), 0);
  return Buffer.concat([head, body, crc]);
}
// encode rows of channel bytes, filtering row y with filter (y % 5) so every unfilter path runs
function png(width, height, colorType, channels, rows, extra = []) {
  const ihdr = Buffer.alloc(13);
  ihdr.writeUInt32BE(width, 0);
  ihdr.writeUInt32BE(height, 4);
  ihdr[8] = 8;
  ihdr[9] = colorType;
  const stride = width * channels;
  const raw = [];
  let prev = Buffer.alloc(stride);
  rows.forEach((row, y) => {
    const cur = Buffer.from(row);
    const f = y % 5;
    const out = Buffer.alloc(stride);
    for (let x = 0; x < stride; x += 1) {
      const a = x >= channels ? cur[x - channels] : 0;
      const b = prev[x];
      const c = x >= channels ? prev[x - channels] : 0;
      let pred = 0;
      if (f === 1) pred = a;
      else if (f === 2) pred = b;
      else if (f === 3) pred = (a + b) >> 1;
      else if (f === 4) {
        const p = a + b - c;
        const pa = Math.abs(p - a);
        const pb = Math.abs(p - b);
        const pc = Math.abs(p - c);
        pred = pa <= pb && pa <= pc ? a : pb <= pc ? b : c;
      }
      out[x] = (cur[x] - pred) & 255;
    }
    raw.push(Buffer.from([f]), out);
    prev = cur;
  });
  return Buffer.concat([Buffer.from('89504e470d0a1a0a', 'hex'), chunk('IHDR', ihdr), ...extra,
    chunk('IDAT', deflateSync(Buffer.concat(raw))), chunk('IEND', Buffer.alloc(0))]);
}

test('ATELIER sold-out chip M: the strike row reads median #8E8E8E, range 118-158, 12 px', () => {
  const image = decodePng(readFileSync(CHIPS));
  assert.equal(image.width, 160);
  assert.equal(image.height, 44);
  const r = sample(image, { region: [0, 0, 78, 44] });
  assert.equal(r.row, 22);
  assert.equal(r.n, 12);
  assert.deepEqual(r.min, [118, 118, 118]);
  assert.deepEqual(r.max, [158, 158, 158]);
  assert.deepEqual(r.median, [142, 142, 142]);
  assert.match(format(r), /^median #8E8E8E, range 118–158, n 12 px \(row 22, bg #FFFFFF, contrast 3\.28\)$/);
});

test('the fixed colour #8A8A8A is within tolerance; the colour before the fix (#9A9A9A) is not', () => {
  const r = sample(decodePng(readFileSync(CHIPS)), { region: [0, 0, 78, 44] });
  assert.equal(compare(r, parseHex('#8A8A8A')).within, true);
  const before = compare(r, parseHex('#9A9A9A'));
  assert.equal(before.within, false);
  assert.ok(before.channel > 8 && before.contrastDiff > 0.2);
});

test('agreement needs both: channel ±8 and contrast ±0.2 (2026-11-26 user decision)', () => {
  const white = [255, 255, 255];
  const reading = (median) => ({ median, bg: white, contrast: contrast(median, white) });
  // ATELIER chip M stays within: diff 4 / 0.18
  const chip = compare(sample(decodePng(readFileSync(CHIPS)), { region: [0, 0, 78, 44] }), parseHex('#8A8A8A'));
  assert.equal(chip.channel, 4);
  assert.ok(chip.contrastDiff <= 0.2);
  assert.equal(chip.within, true);
  // channel over, contrast within: grey expected, blue-grey read at about the same lightness
  const hue = compare(reading([138, 138, 156]), parseHex('#8A8A8A'));
  assert.ok(hue.channel > 8 && hue.contrastDiff <= 0.2, JSON.stringify(hue));
  assert.equal(hue.within, false);
  // contrast over, channel within: dark ink where 8 levels move the contrast a lot
  const dark = compare(reading([40, 40, 40]), parseHex('#202020'));
  assert.ok(dark.channel <= 8 && dark.contrastDiff > 0.2, JSON.stringify(dark));
  assert.equal(dark.within, false);
});

test('a chip border hairline (#E5E5E5 on white) is background at the default threshold', () => {
  const r = sample(decodePng(readFileSync(CHIPS)));
  assert.equal(r.row, 22);
  assert.ok(r.min[0] >= 118 && r.median[0] < 160);
});

test('every PNG filter and colour type decodes to the same pixels', () => {
  const grey = [[255, 255, 255, 255], [255, 100, 100, 255], [255, 255, 255, 255], [10, 20, 30, 40], [50, 60, 70, 80], [255, 255, 255, 255]];
  const rgb = grey.map((row) => row.flatMap((v) => [v, v, v]));
  const rgba = grey.map((row) => row.flatMap((v) => [v, v, v, 255]));
  const ga = grey.map((row) => row.flatMap((v) => [v, 255]));
  const values = [...new Set(grey.flat())];
  const plte = chunk('PLTE', Buffer.from(values.flatMap((v) => [v, v, v])));
  const indexed = grey.map((row) => row.map((v) => values.indexOf(v)));
  const expected = decodePng(png(4, 6, 2, 3, rgb)).rgb;
  assert.deepEqual([...expected.slice(0, 12)], [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]);
  assert.deepEqual([...expected.slice(12, 18)], [255, 255, 255, 100, 100, 100]);
  for (const image of [png(4, 6, 0, 1, grey), png(4, 6, 6, 4, rgba), png(4, 6, 4, 2, ga), png(4, 6, 3, 1, indexed, [plte])]) {
    assert.deepEqual(decodePng(image).rgb, expected);
  }
});

test('alpha is composited over white', () => {
  const image = decodePng(png(1, 1, 6, 4, [[0, 0, 0, 128]]));
  assert.deepEqual([...image.rgb], [127, 127, 127]);
});

test('rows all keeps every ink pixel; a region outside the capture and 16-bit PNG are refused', () => {
  const image = decodePng(readFileSync(CHIPS));
  const all = sample(image, { region: [0, 0, 78, 44], rows: 'all' });
  assert.equal(all.row, null);
  assert.ok(all.n > 12);
  assert.throws(() => sample(image, { region: [150, 0, 20, 10] }), /outside the 160x44 capture/);
  const sixteen = png(1, 1, 0, 1, [[0]]);
  sixteen[24] = 16; // IHDR bit depth (CRC is not checked)
  assert.throws(() => decodePng(sixteen), /bit depth 16/);
});

test('CLI: the record line, exit 1 outside tolerance, exit 2 on usage errors', () => {
  const out = execFileSync(process.execPath, [SCRIPT.pathname.replace(/^\/([A-Za-z]:)/, '$1'),
    CHIPS.pathname.replace(/^\/([A-Za-z]:)/, '$1'), '--region', '0,0,78,44', '--expect', '#8A8A8A'], { encoding: 'utf8' });
  assert.match(out, /median #8E8E8E, range 118–158, n 12 px/);
  assert.match(out, /expect #8A8A8A: channel diff 4 \/ contrast diff 0\.18 -> within/);
  const outside = spawnSync(process.execPath, [SCRIPT.pathname.replace(/^\/([A-Za-z]:)/, '$1'),
    CHIPS.pathname.replace(/^\/([A-Za-z]:)/, '$1'), '--region', '0,0,78,44', '--expect', '#9A9A9A'], { encoding: 'utf8' });
  assert.equal(outside.status, 1);
  assert.match(outside.stdout, /-> outside/);
  const bad = spawnSync(process.execPath, [SCRIPT.pathname.replace(/^\/([A-Za-z]:)/, '$1'), '--region', '1,2'], { encoding: 'utf8' });
  assert.equal(bad.status, 2);
  assert.match(bad.stderr, /x,y,w,h/);
});
