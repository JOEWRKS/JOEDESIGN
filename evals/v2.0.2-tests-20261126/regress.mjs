// node evals/v2.0.2-tests-20261126/regress.mjs : 2.0.2 candidate report-check vs the v2.0.1 tag
// on the 274 regression reports (part14 list) and the 2.0.2 ATELIER fixtures.
// v2.0.1's report-check.mjs is read from the tag (git show) into the OS temp folder.
// writes regress-274.txt and regress-changes.tsv next to this file
import { readFileSync, writeFileSync, mkdtempSync, readdirSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { pathToFileURL } from 'node:url';
import { check, splitStamp } from '../../skills/joedesign/scripts/report-check.mjs';
const root = new URL('../../', import.meta.url);
const here = new URL('./', import.meta.url);
const dir = mkdtempSync(join(tmpdir(), 'rc201-'));
const oldPath = join(dir, 'report-check.mjs');
writeFileSync(oldPath, execFileSync('git', ['show', 'v2.0.1:skills/joedesign/scripts/report-check.mjs'], { cwd: root }));
const { check: oldCheck } = await import(pathToFileURL(oldPath).href);
const read = (f) => splitStamp(readFileSync(new URL(f, root), 'utf8').replace(/^﻿/, '')).body;
const tally = (found) => found.reduce((m, x) => ({ ...m, [x[1]]: (m[x[1]] || 0) + 1 }), {});
const tag = (found) => found.map((x) => `${x[1]}@${x[0]}`).join(',') || 'ok';
const files = readFileSync(new URL('evals/check-coverage-20261104/part14/regression/files-274.txt', root), 'utf8').trim().split(/\r?\n/);
const fixtures = readdirSync(new URL('fixtures/report-check-202/', root)).sort().map((f) => `fixtures/report-check-202/${f}`);
const sum = (list, fn) => list.reduce((m, f) => { for (const [k, v] of Object.entries(tally(fn(read(f))))) m[k] = (m[k] || 0) + v; return m; }, {});
const changes = [];
for (const f of [...files, ...fixtures]) {
  const a = tag(oldCheck(read(f)));
  const b = tag(check(read(f)));
  if (a !== b) changes.push(`${f}\t2.0.1 ${a}\t2.0.2 ${b}`);
}
const out = `${files.length} reports\n2.0.1: ${JSON.stringify(sum(files, oldCheck))}\n2.0.2 candidate: ${JSON.stringify(sum(files, check))}\n` +
  `files whose findings changed: ${changes.filter((c) => !c.startsWith('fixtures/')).length}\n` +
  `${fixtures.length} fixtures\n2.0.1: ${JSON.stringify(sum(fixtures, oldCheck))}\n2.0.2 candidate: ${JSON.stringify(sum(fixtures, check))}\n`;
writeFileSync(new URL('regress-274.txt', here), out);
writeFileSync(new URL('regress-changes.tsv', here), `file\tv2.0.1\t2.0.2\n${changes.join('\n')}\n`);
process.stdout.write(out + changes.join('\n') + '\n');
