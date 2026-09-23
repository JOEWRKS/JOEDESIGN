import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const skill = readFileSync(path.join(root, 'skills/joedesign/SKILL.md'), 'utf8');
const template = readFileSync(path.join(root, 'skills/joedesign/templates/DESIGN.md'), 'utf8');

test('type — semantic role is chosen before numeric value', () => {
  assert.match(skill, /Role before value/i);
  assert.match(skill, /semantic .*role/i);
  assert.match(skill, /reusable .*type role/i);
});

test('type — hierarchy uses multiple axes rather than font size alone', () => {
  assert.match(skill, /Font size alone is not hierarchy/i);
  assert.match(skill, /weight/i);
  assert.match(skill, /line height/i);
  assert.match(skill, /tone|text color/i);
  assert.match(skill, /placement|position/i);
});

test('type — scale is restrained and independent from the spatial 4px grid', () => {
  assert.match(skill, /12, 14, 16, 20, 24, 32, 40, 48, 64/);
  assert.match(skill, /not .*spatial 4px grid/i);
  assert.match(skill, /subset .*project needs|use only .*subset/i);
});

test('type — near-duplicate roles and arbitrary local sizes are challenged', () => {
  assert.match(skill, /1–2px|1-2px/);
  assert.match(skill, /collapse .*role|merge .*role/i);
  assert.match(skill, /arbitrary|one-off/i);
});

test('type — family and weight strategy is restrained and role-based', () => {
  assert.match(skill, /fewest .*famil/i);
  assert.match(skill, /fewest .*weight/i);
  assert.match(skill, /do not synthesize unsupported font weights/i);
  assert.match(skill, /bold everywhere/i);
});

test('type — readability couples measure, line height, language, and actual face', () => {
  assert.match(skill, /reading measure/i);
  assert.match(skill, /60–80 characters|60-80 characters/i);
  assert.match(skill, /Korean|CJK/i);
  assert.match(skill, /1\.45–1\.6|1\.45-1\.6/);
  assert.match(skill, /actual face|actual typeface/i);
});

test('type — responsive translation preserves role hierarchy instead of proportional shrinking', () => {
  assert.match(skill, /responsive typography/i);
  assert.match(skill, /not proportionally shrink|not .*shrink desktop/i);
  assert.match(skill, /preserve .*role/i);
  assert.match(skill, /line breaks/i);
});

test('type — project DESIGN template can persist type roles and reading system', () => {
  assert.match(template, /Type Roles/);
  assert.match(template, /Type Scale/);
  assert.match(template, /Reading Measure/);
  assert.match(template, /Responsive Type Translation/);
});
