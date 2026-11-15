// node evals/check-coverage-20261104/part15/regress.mjs : 1.3.2 candidate on the part14 regression sets
// writes rule-counts-274.txt, verify-stamped-1.3.2.tsv and r6ab-hits.tsv next to this file
import { readFileSync, writeFileSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { check } from '../../../skills/joedesign/scripts/report-check.mjs';
const here = new URL('./', import.meta.url);
const reg = new URL('../part14/regression/', import.meta.url);
const root = new URL('../../../', import.meta.url);
const files = readFileSync(new URL('files-274.txt', reg), 'utf8').trim().split(/\r?\n/);
const counts = {};
const hits = [];
for (const f of files) {
  const found = check(readFileSync(new URL(f, root), 'utf8').replace(/^﻿/, ''));
  for (const x of found) counts[x[1]] = (counts[x[1]] || 0) + 1;
  const r6 = found.filter((x) => x[1].startsWith('R6'));
  if (r6.length) hits.push(`${f}\t${r6.map((x) => `${x[1]}@${x[0]}`).join(',')}`);
}
writeFileSync(new URL('rule-counts-274.txt', here), `1.3.2 candidate:\n${files.length} ${JSON.stringify(counts)}\n`);
writeFileSync(new URL('r6ab-hits-274.tsv', here), `${hits.join('\n')}\n`);
const script = new URL('../../../skills/joedesign/scripts/report-check.mjs', import.meta.url);
const old = readFileSync(new URL('verify-stamped-1.3.1.tsv', reg), 'utf8').trim().split(/\r?\n/);
const rows = old.map((line) => {
  const f = line.split('\t')[0];
  let out;
  try { out = execFileSync('node', [script.pathname.replace(/^\/(\w:)/, '$1'), '--verify', f], { cwd: root, encoding: 'utf8' }); }
  catch (e) { out = e.stdout; }
  return `${f}\t${out.trim()}`;
});
writeFileSync(new URL('verify-stamped-1.3.2.tsv', here), `${rows.join('\n')}\n`);
const changed = rows.filter((r, i) => r !== old[i]);
console.log(`274: ${JSON.stringify(counts)}; R6* hits in ${hits.length} files`);
console.log(`stamped 118: ${changed.length} changed vs 1.3.1`);
for (const c of changed) console.log(`  ${c}`);
