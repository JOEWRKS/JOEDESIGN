#!/usr/bin/env node
// Read the colour of a drawn stroke from a capture: the direct observation for a colour rule.
//
// usage: node sample-pixels.mjs CAPTURE.png [--region x,y,w,h] [--bg #RRGGBB] [--rows stroke|all]
//          [--min-diff N] [--expect #RRGGBB] [--tolerance N] [--json]
//
// Node only (zlib): reads 8-bit non-interlaced PNG (grey, grey+alpha, RGB, RGBA, palette).
// Alpha is composited over white. Region coordinates are capture pixels (a DPR-2 capture
// has two per CSS pixel).
//   1. background: --bg, or the most frequent colour in the region
//   2. ink pixels: pixels whose largest channel difference from the background exceeds
//      --min-diff (default 40; a #E5E5E5 hairline on white differs by 26 and stays background); anti-aliased edges are ink too, so the reading is a spread
//   3. --rows stroke (default): keep the row with the most ink pixels, the centre row of a
//      horizontal stroke (a strikethrough, an underline, the middle of a letter); --rows all
//      keeps every ink pixel in the region
//   4. report per channel median and range, the count, and the contrast of the median
//      against the background
// Output: `median #8E8E8E, range 118–158, n 12 px (row 22, bg #FFFFFF, contrast 3.28)`.
// With --expect: `expect #8A8A8A: channel diff 4 / contrast diff 0.18 -> within (±8 and ±0.2)`.
// Exit 0: read (and within tolerance when --expect is given). 1: outside tolerance or no ink.
// 2: usage or decode error.
import { readFileSync } from 'node:fs';
import { inflateSync } from 'node:zlib';

const SIGNATURE = '89504e470d0a1a0a';

export function decodePng(buffer) {
  if (buffer.subarray(0, 8).toString('hex') !== SIGNATURE) throw new Error('not a PNG file');
  let offset = 8;
  let header = null;
  let palette = null;
  let transparency = null;
  const data = [];
  while (offset < buffer.length) {
    const length = buffer.readUInt32BE(offset);
    const type = buffer.toString('latin1', offset + 4, offset + 8);
    const body = buffer.subarray(offset + 8, offset + 8 + length);
    if (type === 'IHDR') {
      header = { width: body.readUInt32BE(0), height: body.readUInt32BE(4), depth: body[8],
        colorType: body[9], interlace: body[12] };
    } else if (type === 'PLTE') palette = body;
    else if (type === 'tRNS') transparency = body;
    else if (type === 'IDAT') data.push(body);
    else if (type === 'IEND') break;
    offset += 12 + length;
  }
  if (!header) throw new Error('PNG has no IHDR');
  const { width, height, depth, colorType, interlace } = header;
  if (depth !== 8) throw new Error(`PNG bit depth ${depth} is not supported (8 only); re-save the capture as 8-bit`);
  if (interlace) throw new Error('interlaced PNG is not supported; re-save the capture without interlace');
  const channels = { 0: 1, 2: 3, 3: 1, 4: 2, 6: 4 }[colorType];
  if (!channels) throw new Error(`PNG colour type ${colorType} is not supported`);
  if (colorType === 3 && !palette) throw new Error('palette PNG has no PLTE');
  const raw = inflateSync(Buffer.concat(data));
  const stride = width * channels;
  const pixels = Buffer.alloc(stride * height);
  let previous = Buffer.alloc(stride);
  for (let y = 0; y < height; y += 1) {
    const filter = raw[y * (stride + 1)];
    const line = raw.subarray(y * (stride + 1) + 1, (y + 1) * (stride + 1));
    const out = pixels.subarray(y * stride, (y + 1) * stride);
    for (let x = 0; x < stride; x += 1) {
      const a = x >= channels ? out[x - channels] : 0;
      const b = previous[x];
      const c = x >= channels ? previous[x - channels] : 0;
      let v = line[x];
      if (filter === 1) v += a;
      else if (filter === 2) v += b;
      else if (filter === 3) v += (a + b) >> 1;
      else if (filter === 4) {
        const p = a + b - c;
        const pa = Math.abs(p - a);
        const pb = Math.abs(p - b);
        const pc = Math.abs(p - c);
        v += pa <= pb && pa <= pc ? a : pb <= pc ? b : c;
      } else if (filter !== 0) throw new Error(`PNG row ${y} has unknown filter ${filter}`);
      out[x] = v & 255;
    }
    previous = out;
  }
  // to RGB over white
  const rgb = new Uint8Array(width * height * 3);
  for (let i = 0; i < width * height; i += 1) {
    let r;
    let g;
    let bl;
    let alpha = 255;
    const p = pixels.subarray(i * channels, (i + 1) * channels);
    if (colorType === 0) { r = g = bl = p[0]; }
    else if (colorType === 4) { r = g = bl = p[0]; alpha = p[1]; }
    else if (colorType === 2) { [r, g, bl] = p; }
    else if (colorType === 6) { [r, g, bl, alpha] = p; }
    else {
      const k = p[0];
      [r, g, bl] = palette.subarray(k * 3, k * 3 + 3);
      if (transparency && k < transparency.length) alpha = transparency[k];
    }
    const over = (v) => Math.round((v * alpha + 255 * (255 - alpha)) / 255);
    rgb[i * 3] = over(r);
    rgb[i * 3 + 1] = over(g);
    rgb[i * 3 + 2] = over(bl);
  }
  return { width, height, rgb };
}

export function parseHex(text) {
  const m = /^#?([0-9a-f]{6})$/i.exec(String(text).trim());
  if (!m) throw new Error(`colour ${text} is not #RRGGBB`);
  const n = parseInt(m[1], 16);
  return [(n >> 16) & 255, (n >> 8) & 255, n & 255];
}

export function hex(rgb) {
  return `#${rgb.map((v) => v.toString(16).padStart(2, '0')).join('').toUpperCase()}`;
}

function luminance(rgb) {
  const [r, g, b] = rgb.map((v) => {
    const s = v / 255;
    return s <= 0.03928 ? s / 12.92 : ((s + 0.055) / 1.055) ** 2.4;
  });
  return 0.2126 * r + 0.7152 * g + 0.0722 * b;
}

export function contrast(a, b) {
  const [hi, lo] = [luminance(a), luminance(b)].sort((x, y) => y - x);
  return (hi + 0.05) / (lo + 0.05);
}

function median(values) {
  const s = [...values].sort((x, y) => x - y);
  const mid = s.length >> 1;
  return s.length % 2 ? s[mid] : Math.round((s[mid - 1] + s[mid]) / 2);
}

export function sample(image, options = {}) {
  const { width, height, rgb } = image;
  const [rx, ry, rw, rh] = options.region || [0, 0, width, height];
  if (rx < 0 || ry < 0 || rw < 1 || rh < 1 || rx + rw > width || ry + rh > height) {
    throw new Error(`region ${[rx, ry, rw, rh].join(',')} is outside the ${width}x${height} capture`);
  }
  const at = (x, y) => [rgb[(y * width + x) * 3], rgb[(y * width + x) * 3 + 1], rgb[(y * width + x) * 3 + 2]];
  let bg = options.bg;
  if (!bg) {
    const counts = new Map();
    for (let y = ry; y < ry + rh; y += 1) {
      for (let x = rx; x < rx + rw; x += 1) {
        const key = at(x, y).join(',');
        counts.set(key, (counts.get(key) || 0) + 1);
      }
    }
    bg = [...counts.entries()].sort((a, b) => b[1] - a[1])[0][0].split(',').map(Number);
  }
  const minDiff = options.minDiff ?? 40;
  const rows = new Map();
  for (let y = ry; y < ry + rh; y += 1) {
    const ink = [];
    for (let x = rx; x < rx + rw; x += 1) {
      const p = at(x, y);
      if (Math.max(...p.map((v, i) => Math.abs(v - bg[i]))) > minDiff) ink.push(p);
    }
    if (ink.length) rows.set(y, ink);
  }
  let row = null;
  let ink = [];
  if ((options.rows || 'stroke') === 'stroke') {
    for (const [y, list] of rows) if (list.length > ink.length) { row = y; ink = list; }
  } else {
    ink = [...rows.values()].flat();
  }
  if (!ink.length) return { n: 0, bg, row };
  const med = [0, 1, 2].map((i) => median(ink.map((p) => p[i])));
  const min = [0, 1, 2].map((i) => Math.min(...ink.map((p) => p[i])));
  const max = [0, 1, 2].map((i) => Math.max(...ink.map((p) => p[i])));
  return { n: ink.length, bg, row, median: med, min, max, contrast: contrast(med, bg) };
}

export function compare(result, expected, tolerance = 8, contrastTolerance = 0.2) {
  const channel = Math.max(...result.median.map((v, i) => Math.abs(v - expected[i])));
  const contrastDiff = Math.abs(result.contrast - contrast(expected, result.bg));
  return { channel, contrastDiff, within: channel <= tolerance && contrastDiff <= contrastTolerance };
}

export function format(result, options = {}) {
  if (!result.n) return `no ink: no pixel differs from bg ${hex(result.bg)} by more than ${options.minDiff ?? 40}`;
  const same = result.min.every((v) => v === result.min[0]) && result.max.every((v) => v === result.max[0]);
  const range = same ? `${result.min[0]}–${result.max[0]}`
    : `R ${result.min[0]}–${result.max[0]} G ${result.min[1]}–${result.max[1]} B ${result.min[2]}–${result.max[2]}`;
  const where = result.row === null ? 'all ink rows' : `row ${result.row}`;
  let line = `median ${hex(result.median)}, range ${range}, n ${result.n} px ` +
    `(${where}, bg ${hex(result.bg)}, contrast ${result.contrast.toFixed(2)})`;
  if (options.expect) {
    const c = compare(result, options.expect, options.tolerance ?? 8);
    line += `\nexpect ${hex(options.expect)}: channel diff ${c.channel} / contrast diff ${c.contrastDiff.toFixed(2)} ` +
      `-> ${c.within ? 'within' : 'outside'} (±${options.tolerance ?? 8} and ±0.2)`;
  }
  return line;
}

function parseArgs(argv) {
  const options = {};
  let file = null;
  for (let i = 0; i < argv.length; i += 1) {
    const a = argv[i];
    const next = () => {
      if (i + 1 >= argv.length) throw new Error(`${a} needs a value`);
      i += 1;
      return argv[i];
    };
    if (a === '--region') {
      options.region = next().split(',').map(Number);
      if (options.region.length !== 4 || options.region.some((v) => !Number.isInteger(v))) {
        throw new Error('--region is x,y,w,h in whole capture pixels');
      }
    } else if (a === '--bg') options.bg = parseHex(next());
    else if (a === '--expect') options.expect = parseHex(next());
    else if (a === '--rows') {
      options.rows = next();
      if (!['stroke', 'all'].includes(options.rows)) throw new Error('--rows is stroke or all');
    } else if (a === '--min-diff') options.minDiff = Number(next());
    else if (a === '--tolerance') options.tolerance = Number(next());
    else if (a === '--json') options.json = true;
    else if (a.startsWith('--')) throw new Error(`unknown option ${a}`);
    else if (file === null) file = a;
    else throw new Error('one capture at a time');
  }
  if (!file) throw new Error('give a PNG capture');
  return { file, options };
}

function main(argv) {
  let parsed;
  let result;
  try {
    parsed = parseArgs(argv);
    result = sample(decodePng(readFileSync(parsed.file)), parsed.options);
  } catch (error) {
    process.stderr.write(`sample-pixels: ${error.message}\n` +
      'usage: node sample-pixels.mjs CAPTURE.png [--region x,y,w,h] [--bg #RRGGBB] [--rows stroke|all] ' +
      '[--min-diff N] [--expect #RRGGBB] [--tolerance N] [--json]\n');
    return 2;
  }
  const { options } = parsed;
  const verdict = result.n && options.expect ? compare(result, options.expect, options.tolerance ?? 8) : null;
  if (options.json) {
    process.stdout.write(`${JSON.stringify({ ...result,
      median: result.median && hex(result.median), bg: hex(result.bg),
      expect: options.expect && hex(options.expect), verdict }, null, 1)}\n`);
  } else {
    process.stdout.write(`${format(result, options)}\n`);
  }
  if (!result.n) return 1;
  return verdict && !verdict.within ? 1 : 0;
}

if (process.argv[1] && import.meta.url.endsWith(process.argv[1].replace(/\\/g, '/').split('/').pop())) {
  process.exitCode = main(process.argv.slice(2));
}
