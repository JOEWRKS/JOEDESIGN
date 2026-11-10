#!/usr/bin/env node
// Check a design report draft against the JOEDESIGN result-form contract.
//
// usage: node report-check.mjs REPORT.md
//
// Exit 0: no findings. Exit 1: findings (one per line, with the report line number).
// Exit 2: usage or read error.
//
// It reads the text only; it does not judge whether a number is true.
//   R1  a results list exists: at least one line in the form
//       check | result | sizes x states, mode | rendered or code | spot check
//   R2  a fix line's result is `fixed` or `changed`; `fixed` needs an observation
//       in its spot check cell
//   R3  outside the list, a sentence that states a design-check outcome (pass, count,
//       no failures) also carries, in that same sentence, the scope (sizes x states),
//       rendered or code, and the spot check outcome
//   R4  a fix whose list line says `changed` is not named in the report's 해결 (resolved)
//       line; an unconfirmed fix belongs under 남은 문제 (remaining)
//   R5  a report that says it moved, overlapped, hid or merged an existing element
//       carries `before: element | content shown | route` and `after: ...` lines for
//       each element (or one `display unchanged` line); when a pair differs, the report
//       records it as `product decision pending` (제품 결정 대기)
//   A report with no design check run says so in one line, `design checks: none ran`
//   (or `디자인 검사: 실행 안 함`); that line satisfies R1 instead of a results list.
//
// On `ok` the output carries a stamp: `report-check: ok <chars> chars <sha8>`, the
// length and SHA-256 prefix of the checked text. The sent report ends with that stamp
// line so a reader can confirm the checked text is the sent text:
//   node report-check.mjs --verify SENT.md   (exit 0 when the stamp matches the text above it)
import { readFileSync } from 'node:fs';
import { createHash } from 'node:crypto';

const NONE_RAN = /design checks?:\s*none ran|디자인 검사\s*[:：]\s*(?:실행\s*안\s*함|없음|돌리지\s*않음)/i;
const RESOLVED_LINE = /^\s*(?:[-*+]\s*)?\**\s*해결\s*\**\s*[:：]\s*(.*)$/;
const STAMP_LINE = /^report-check: ok (\d[\d,]*) chars ([0-9a-f]{8})\s*$/;

export function normalize(text) {
  return text.replace(/^﻿/, '').replace(/\r\n?/g, '\n').replace(/\s+$/, '');
}

export function stamp(text) {
  const t = normalize(text);
  const sha8 = createHash('sha256').update(t, 'utf8').digest('hex').slice(0, 8);
  return `report-check: ok ${t.length.toLocaleString('en-US')} chars ${sha8}`;
}

// split a sent report into the text above the stamp and the stamp line (null when absent)
export function splitStamp(text) {
  const lines = normalize(text).split('\n');
  const last = lines[lines.length - 1];
  if (!STAMP_LINE.test(last)) return { body: normalize(text), stampLine: null };
  return { body: normalize(lines.slice(0, -1).join('\n')), stampLine: last };
}

const PASS = new RegExp(
  '통과|\\bpass(?:es|ed)?\\b|no failures|0 failures|' +
  '(?:위반|실패|넘침|잘림|문제|어긋남)[은이도가]?\\s*(?:0\\s*건|없)|' +
  '규칙대로|모두 맞|전부 맞|이상[은이]?\\s*없|\\ball (?:checks )?(?:pass|green)', 'i');
// describing how a check behaves, a plan, a condition or a denial is not an outcome claim
const NOT_CLAIM = new RegExp(
  '통과(?:하지|되지|시키지)|통과\\s*못|통과로\\s*(?:나오|나옵|잡|기록|처리|적|치)|' +
  '통과(?:하는지|했는지|할지|하면|해야|시켜)|' +
  '(?:0\\s*건|없)(?:이면|으면|는지|음을\\s*확인하겠|는\\s*것을\\s*확인하겠)|' +
  '(?:0\\s*건|없음)[을를]\\s*확인(?:하겠|할)|' +
  '(?:did|does|do) not pass|not passed|fail(?:s|ed)? to pass|' +
  '\\b(?:if|once|until|whether)\\b[^.]{0,40}\\bpass', 'i');
const COUNT = /(?<![\d.×x/])(\d{1,6})\s*\/\s*(\d{1,6})(?![\d/×x])/g;
const TECH = new RegExp(
  '\\btsc\\b|타입\\s*검사|type\\s*-?check|vitest|단위\\s*테스트|unit tests?|빌드|\\bbuild\\b|' +
  'E2E|playwright|\\blint\\b|npm (?:run )?test|node --test|unittest', 'i');
// a technical-check sentence is exempt unless it also names a design check
const DESIGN = new RegExp(
  'spacing|간격\\s*검사|넘침|overflow|잘림|clipp|규칙\\s*검사|design[- ]check|' +
  '\\bS\\d(?![\\w가-힣])|capture-matrix|감사|audit', 'i');
const SCOPE = new RegExp(
  '\\d+\\s*(?:개\\s*)?(?:화면\\s*)?(?:크기|sizes?)|\\d+\\s*(?:개\\s*)?(?:상태|states?)|' +
  '\\d{3,4}\\s*[x×]\\s*\\d{3,4}|문맥|contexts?', 'i');
const MODE = /렌더|render|코드|\bcode\b|CSS/i;
const SPOT = new RegExp(
  'not spot-checked|spot check|spot-check|대조|직접\\s*(?:비교|확인|재|관찰|측정)|' +
  '검사값|observed|check\\s*\\d+\\s*/|검사\\s*\\d+\\s*/\\s*(?:실제|캡처|관찰)|' +
  '(?:확인|재|보|대조)(?:하지|지)\\s*(?:못|않)', 'i');
// "the outcome is in the list below" is a pointer, not the outcome
const SPOT_POINTER = /(?:대조|spot check)[^.]{0,12}(?:아래|목록|below|list)/i;
const FIX_NAME = /수정(?!\s*전)|고침|\bfix(?:e[sd])?\b(?!\s+before)/i;
const BEFORE_FIX = /수정\s*전|before (?:the )?fix/i;
const NO_OBS = new RegExp(
  '^\\s*[-—]?\\s*$|not spot-checked|대조\\s*안|직접\\s*(?:비교|확인)\\s*안|확인\\s*안\\s*함|' +
  '(?:확인|대조)(?:하지|지)\\s*(?:못|않)', 'i');
const RULE_ROW = /^[\s:\-|]+$/;
// R5: words that say this work moved, overlapped, hid or merged an element (done, not described)
const RELOCATE = new RegExp(
  '옮겼|옮김|옮겨\\s*(?:놓|두|넣|달|붙|배치)|이동(?:시켰|했|함)|재배치|' +
  '겹쳤|겹치게|겹쳐\\s*(?:띄|놓|두|배치|올|표시|얹)|숨겼|숨김\\s*처리|숨기도록|합쳤|합침|병합|' +
  '\\b(?:moved|relocated|repositioned|overlaid|merged|hid)\\b|made\\s+\\S+\\s+overlap', 'i');
const BA_LINE = /^\s*(?:[-*+]\s*)?\**\s*(before|after)\s*\**\s*[:：]\s*(.*)$/i;
const DISPLAY_SAME = /display unchanged|표시\s*(?:변화|변경)\s*없음/i;
const PENDING = /product decision pending|제품\s*결정\s*대기/i;

function baKey(s) {
  return s.replaceAll('`', '').replace(/["'“”‘’]/g, '').replace(/\s+/g, ' ').trim().toLowerCase();
}

function cellsOf(line) {
  let body = line.trim().replace(/^(?:[-*+]|\d+[.)])\s+/, '');
  body = body.replaceAll('`', '').replaceAll('**', '');
  if ((body.match(/\|/g) || []).length < 4) return null;
  if (RULE_ROW.test(body)) return null;
  const parts = body.replace(/^\|+|\|+$/g, '').split('|').map((p) => p.trim());
  return parts.length < 5 ? null : parts;
}

function sentences(text) {
  const out = [];
  let depth = 0;
  let start = 0;
  for (let i = 0; i < text.length; i += 1) {
    const ch = text[i];
    if (ch === '(' || ch === '[') depth += 1;
    else if (ch === ')' || ch === ']') depth = Math.max(0, depth - 1);
    else if ('.?!'.includes(ch) && depth === 0) {
      const next = text[i + 1];
      if (next === undefined || /\s/.test(next)) {
        out.push(text.slice(start, i + 1).trim());
        start = i + 1;
      }
    }
  }
  out.push(text.slice(start).trim());
  return out.filter(Boolean);
}

function isCount(sentence) {
  for (const m of sentence.matchAll(COUNT)) {
    const a = Number(m[1]);
    const b = Number(m[2]);
    if (a <= b && b >= 30) return true;
  }
  return false;
}

export function check(text) {
  const findings = [];
  let listLines = 0;
  let inCode = false;
  let shortRow = null;
  let noneRan = false;
  const changedFixes = []; // [lineNo, name]
  const resolvedLines = []; // [lineNo, text]
  const baLines = []; // [lineNo, 'before'|'after', cells]
  let relocateAt = 0;
  let displaySame = false;
  let pending = false;
  text.split(/\r?\n/).forEach((raw, index) => {
    const no = index + 1;
    if (raw.trim().startsWith('```')) { inCode = !inCode; return; }
    if (!raw.trim()) return;
    if (STAMP_LINE.test(raw.trim())) return; // a stamp from an earlier run is not part of the report
    if (NONE_RAN.test(raw)) noneRan = true;
    if (!inCode) {
      const ba = raw.replaceAll('**', '').match(BA_LINE);
      if (ba) {
        baLines.push([no, ba[1].toLowerCase(), ba[2].split('|').map((c) => c.trim())]);
        return; // a before/after line is a record, not prose or a result row
      }
      if (DISPLAY_SAME.test(raw)) displaySame = true;
      if (PENDING.test(raw)) pending = true;
      if (!relocateAt && RELOCATE.test(raw.replaceAll('`', ''))) relocateAt = no;
    }
    const resolved = raw.match(RESOLVED_LINE);
    if (resolved) resolvedLines.push([no, resolved[1]]);
    const cells = cellsOf(raw);
    if (cells) {
      listLines += 1;
      if (FIX_NAME.test(cells[0]) && !BEFORE_FIX.test(cells[0])) {
        const word = cells[1].trim().toLowerCase();
        if (word === 'changed') changedFixes.push([no, cells[0]]);
        if (word !== 'fixed' && word !== 'changed') {
          findings.push([no, 'R2', cells[0],
            `a fix line's result is \`fixed\` or \`changed\`, not \`${cells[1]}\``]);
        } else if (word === 'fixed' && NO_OBS.test(cells[cells.length - 1])) {
          findings.push([no, 'R2', cells[0],
            '`fixed` needs the direct observation in its spot check cell; without it the word is `changed`']);
        }
      }
      return;
    }
    if (inCode) return;
    if (raw.trim().startsWith('|') || (raw.match(/\|/g) || []).length >= 3) {
      // a table or short result row is not prose; one that states an outcome in
      // fewer than five cells is reported once
      if (RULE_ROW.test(raw.trim())) return;
      if (shortRow === null && (PASS.test(raw) || isCount(raw))) shortRow = no;
      return;
    }
    const plain = raw.replaceAll('`', '').replaceAll('**', '')
      .replace(/^\s*(?:[-*+]|\d+[.)])\s+/, '');
    for (const s of sentences(plain)) {
      const claim = (PASS.test(s) && !NOT_CLAIM.test(s)) || isCount(s);
      if (!claim) continue;
      if (/report-check/i.test(s)) continue; // a note about this script is not a design-check outcome
      if (TECH.test(s) && !DESIGN.test(s)) continue;
      const missing = [];
      if (!SCOPE.test(s)) missing.push('sizes x states');
      if (!MODE.test(s)) missing.push('rendered or code');
      if (!SPOT.test(s) || SPOT_POINTER.test(s)) missing.push('spot check outcome');
      if (missing.length) {
        const short = s.length <= 90 ? s : `${s.slice(0, 87)}...`;
        findings.push([no, 'R3', short,
          `check outcome without ${missing.join(', ')}: add the parenthesis copied from ` +
          'its result line, or name the check and leave the outcome to the line']);
      }
    }
  });
  if (shortRow !== null) {
    findings.push([shortRow, 'R1', '',
      'a row states a check outcome in fewer than five cells: use ' +
      '`check | result | sizes x states, mode | rendered or code | spot check`']);
  }
  if (listLines === 0 && !noneRan) {
    findings.unshift([0, 'R1', '',
      'no results list: give each check that ran one line ' +
      '`check | result | sizes x states, mode | rendered or code | spot check`, ' +
      'or say `design checks: none ran`']);
  }
  // R4: a `changed` fix named in the 해결 line
  for (const [fixNo, name] of changedFixes) {
    const tokens = name.replace(/\bfix\b|수정|고침|변경/gi, ' ').split(/[^\p{L}\p{N}]+/u)
      .filter((t) => t.length >= 2);
    for (const [no, resolvedText] of resolvedLines) {
      if (/^\s*없음/.test(resolvedText)) continue;
      if (tokens.some((t) => resolvedText.includes(t))) {
        findings.push([no, 'R4', name,
          `this fix is \`changed\` on line ${fixNo} (no direct observation yet); an unconfirmed fix ` +
          'goes under 남은 문제, not 해결']);
        break;
      }
    }
  }
  // R5: display before/after for a move, overlap, hide or merge
  if (relocateAt && !baLines.length && !displaySame) {
    findings.push([relocateAt, 'R5', '',
      'this report moves, overlaps, hides or merges an element: add `before: element | content shown | route` ' +
      'and `after: element | content shown | route` lines for each element (`hidden` when it is no longer shown), ' +
      'or one `display unchanged` line']);
  }
  const pairs = new Map(); // element -> {before, after, no}
  for (const [no, side, cells] of baLines) {
    if (cells.length < 3 || !cells[0]) {
      findings.push([no, 'R5', cells.join(' | '),
        'a before/after line has three cells: `element | content shown | route to reach it`']);
      continue;
    }
    const key = baKey(cells[0]);
    const entry = pairs.get(key) || { name: cells[0], before: null, after: null, no };
    entry[side] = cells.slice(1).map(baKey).join(' | ');
    entry.no = no;
    pairs.set(key, entry);
  }
  const differs = [...pairs.values()].filter((e) => e.before !== e.after);
  if (differs.length && !pending) {
    for (const e of differs) {
      const why = e.before === null ? 'no before line' : e.after === null ? 'no after line' : 'content or route differs';
      findings.push([e.no, 'R5', e.name,
        `before and after differ (${why}): what the user sees or how they reach it changed, so record it as ` +
        '`product decision pending` for JOEFLOW re-entry; a pair that only moved has the same content and route']);
    }
  }
  return findings;
}

function verify(path) {
  let text;
  try {
    text = readFileSync(path, 'utf8');
  } catch (error) {
    process.stderr.write(`report-check: cannot read ${path}: ${error.message}\n`);
    return 2;
  }
  const { body, stampLine } = splitStamp(text);
  if (!stampLine) {
    process.stdout.write('stamp: missing (the sent report does not end with a report-check stamp)\n');
    return 1;
  }
  const expected = stamp(body);
  const findings = check(body);
  if (expected !== stampLine) {
    process.stdout.write(`stamp: mismatch (stamp says ${stampLine.slice(17)}; the text above it is ${expected.slice(17)})\n`);
    return 1;
  }
  process.stdout.write(`stamp: match (${expected.slice(17)}); text ${findings.length ? `${findings.length} finding(s)` : 'ok'}\n`);
  return findings.length ? 1 : 0;
}

function main(argv) {
  if (argv.length === 2 && argv[0] === '--verify') return verify(argv[1]);
  if (argv.length !== 1) {
    process.stderr.write('usage: node report-check.mjs REPORT.md | node report-check.mjs --verify SENT.md\n');
    return 2;
  }
  let text;
  try {
    text = readFileSync(argv[0], 'utf8').replace(/^\uFEFF/, '');
  } catch (error) {
    process.stderr.write(`report-check: cannot read ${argv[0]}: ${error.message}\n`);
    return 2;
  }
  const findings = check(text);
  if (!findings.length) {
    process.stdout.write(`${stamp(splitStamp(text).body)}\n`);
    return 0;
  }
  const lines = [`report-check: ${findings.length} finding(s)`];
  for (const [no, rule, quote, msg] of findings) {
    lines.push(`${no ? `line ${no}` : 'report'} [${rule}] ${quote ? `${quote} -- ` : ''}${msg}`);
  }
  process.stdout.write(`${lines.join('\n')}\n`);
  return 1;
}

if (process.argv[1] && import.meta.url.endsWith(process.argv[1].replace(/\\/g, '/').split('/').pop())) {
  process.exitCode = main(process.argv.slice(2));
}
