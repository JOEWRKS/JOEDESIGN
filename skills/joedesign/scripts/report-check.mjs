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
import { readFileSync } from 'node:fs';

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
  text.split(/\r?\n/).forEach((raw, index) => {
    const no = index + 1;
    if (raw.trim().startsWith('```')) { inCode = !inCode; return; }
    if (!raw.trim()) return;
    const cells = cellsOf(raw);
    if (cells) {
      listLines += 1;
      if (FIX_NAME.test(cells[0]) && !BEFORE_FIX.test(cells[0])) {
        const word = cells[1].trim().toLowerCase();
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
  if (listLines === 0) {
    findings.unshift([0, 'R1', '',
      'no results list: give each check that ran one line ' +
      '`check | result | sizes x states, mode | rendered or code | spot check`']);
  }
  return findings;
}

function main(argv) {
  if (argv.length !== 1) {
    process.stderr.write('usage: node report-check.mjs REPORT.md\n');
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
    process.stdout.write('report-check: ok\n');
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
