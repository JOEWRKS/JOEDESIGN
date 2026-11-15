// node evals/check-coverage-20261104/part15/run-ab.mjs : report-check findings for the 32 part14 behavior A/B reports
import { readFileSync } from 'node:fs';
import { check, splitStamp } from '../../../skills/joedesign/scripts/report-check.mjs';
const base = new URL('../part14/behavior-ab/', import.meta.url);
const map = JSON.parse(readFileSync(new URL('blind-map.json', base), 'utf8'));
const grades = JSON.parse(readFileSync(new URL('grades.json', base), 'utf8'));
const order = new Map((Array.isArray(grades) ? grades : Object.values(grades)).flat().map((g) => [g.id ?? g.run ?? g.packet, g]));
for (const { id, arm, scene } of map) {
  const text = readFileSync(new URL(`runs/${id}/REPORT.md`, base), 'utf8');
  const f = check(splitStamp(text).body);
  const g = order.get(id);
  const seen = g ? (g.order_seen ?? '') : '';
  console.log(`${id}\t${arm}\t${scene}\t${f.map((x) => `${x[1]}@${x[0]}`).join(',') || 'ok'}\t${seen}`);
}
