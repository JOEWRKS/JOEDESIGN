// node evals/check-coverage-20261104/part17/regress.mjs : 1.3.3 candidate R7 vs the v1.3.2 script
// v1.3.2's report-check.mjs is read from the tag (git show) into the OS temp folder.
// writes rule-counts-274.txt, sets.tsv and r7-changes.tsv next to this file
import { readFileSync, writeFileSync, mkdtempSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { pathToFileURL } from 'node:url';
import { check, splitStamp } from '../../../skills/joedesign/scripts/report-check.mjs';
const root = new URL('../../../', import.meta.url);
const here = new URL('./', import.meta.url);
const dir = mkdtempSync(join(tmpdir(), 'rc132-'));
const oldPath = join(dir, 'report-check.mjs');
writeFileSync(oldPath, execFileSync('git', ['show', 'v1.3.2:skills/joedesign/scripts/report-check.mjs'], { cwd: root }));
const { check: oldCheck } = await import(pathToFileURL(oldPath).href);
const read = (f) => splitStamp(readFileSync(new URL(f, root), 'utf8').replace(/^﻿/, '')).body;
const tally = (found) => found.reduce((m, x) => ({ ...m, [x[1]]: (m[x[1]] || 0) + 1 }), {});
const tag = (found) => found.map((x) => `${x[1]}@${x[0]}`).join(',') || 'ok';

// the 274 regression reports (part14 list)
const files = readFileSync(new URL('evals/check-coverage-20261104/part14/regression/files-274.txt', root), 'utf8').trim().split(/\r?\n/);
const sum = (fn) => files.reduce((m, f) => { for (const [k, v] of Object.entries(tally(fn(read(f))))) m[k] = (m[k] || 0) + v; return m; }, {});
const oldC = sum(oldCheck);
const newC = sum(check);
const changes = [];
for (const f of files) {
  const a = tag(oldCheck(read(f)).filter((x) => x[1] === 'R7'));
  const b = tag(check(read(f)).filter((x) => x[1] === 'R7'));
  if (a !== b) changes.push(`${f}\t1.3.2 ${a}\t1.3.3 ${b}`);
}
writeFileSync(new URL('rule-counts-274.txt', here),
  `${files.length} reports\n1.3.2: ${JSON.stringify(oldC)}\n1.3.3 candidate: ${JSON.stringify(newC)}\n`);
writeFileSync(new URL('r7-changes.tsv', here), changes.length ? `${changes.join('\n')}\n` : '');

// named sets: part16 runs, part14 behavior A/B, part15 verify-stamped reports that were ok on 1.3.2
const sets = [];
const p16 = JSON.parse(readFileSync(new URL('evals/check-coverage-20261104/part16/behavior-ab/blind-map.json', root), 'utf8'));
for (const { id, arm } of p16.sort((x, y) => x.id.localeCompare(y.id))) sets.push(['part16', arm, `evals/check-coverage-20261104/part16/behavior-ab/runs/${id}/REPORT.md`]);
const p14 = JSON.parse(readFileSync(new URL('evals/check-coverage-20261104/part14/behavior-ab/blind-map.json', root), 'utf8'));
for (const { id, arm } of p14.sort((x, y) => x.id.localeCompare(y.id))) sets.push(['part14', arm, `evals/check-coverage-20261104/part14/behavior-ab/runs/${id}/REPORT.md`]);
for (const line of readFileSync(new URL('evals/check-coverage-20261104/part15/verify-stamped-1.3.2.tsv', root), 'utf8').trim().split(/\r?\n/)) {
  const [f, out] = line.split('\t');
  if (/text ok/.test(out)) sets.push(['part15-ok', '-', f]);
}
const rows = sets.map(([set, arm, f]) => {
  const o = oldCheck(read(f));
  const n = check(read(f));
  return [set, arm, f, tag(o.filter((x) => x[1] === 'R7')), tag(n.filter((x) => x[1] === 'R7')), tag(o.filter((x) => x[1] !== 'R7')) === tag(n.filter((x) => x[1] !== 'R7')) ? 'same' : 'DIFF'];
});
writeFileSync(new URL('sets.tsv', here), `set\tarm\tfile\tR7 1.3.2\tR7 1.3.3\tR1-R6\n${rows.map((r) => r.join('\t')).join('\n')}\n`);
console.log(`274: 1.3.2 ${JSON.stringify(oldC)}\n     1.3.3 ${JSON.stringify(newC)}\n     R7 changed in ${changes.length} files`);
for (const c of changes) console.log(`  ${c}`);
const groups = {};
for (const r of rows) { const k = `${r[0]} ${r[1]}`; const g = groups[k] ||= { n: 0, old: 0, new: 0, diff: 0 }; g.n += 1; if (r[3] !== 'ok') g.old += 1; if (r[4] !== 'ok') g.new += 1; if (r[5] !== 'same') g.diff += 1; }
for (const [k, g] of Object.entries(groups)) console.log(`${k}: ${g.n} reports, R7 1.3.2 ${g.old}, R7 1.3.3 ${g.new}, R1-R6 changed ${g.diff}`);
