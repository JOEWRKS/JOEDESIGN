import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const skill = readFileSync(path.join(root, 'skills/joedesign/SKILL.md'), 'utf8');
const template = readFileSync(path.join(root, 'skills/joedesign/templates/DESIGN.md'), 'utf8');

test('craft — hierarchy and visual flow precede decoration', () => {
  assert.match(skill, /Hierarchy before decoration/i);
  assert.match(skill, /visual entry point/i);
  assert.match(skill, /visual flow/i);
});

test('craft — material spacing follows a semantic Visual Block Tree', () => {
  assert.match(skill, /Visual Block Tree/);
  assert.match(skill, /semantic visual/i);
  assert.doesNotMatch(skill, /DOM depth determines visual hierarchy/i);
});

test('craft — spacing belongs to relationships, not isolated elements', () => {
  assert.match(skill, /Spacing belongs to .*relationship/i);
  assert.match(skill, /boundar/i);
  assert.match(skill, /same .*relationship.*same .*role/i);
});

test('craft — structural separation and binding hierarchy stay distinct', () => {
  assert.match(skill, /structural hierarchy/i);
  assert.match(skill, /binding hierarchy/i);
  assert.match(skill, /parent-child/i);
  assert.match(skill, /sibling/i);
});

test('craft — 4px base uses a deliberately restricted canonical token set', () => {
  assert.match(skill, /4px.*base/i);
  assert.match(skill, /4, 8, 16, 24, 48, 160/);
  assert.match(skill, /not .*every .*multiple of four/i);
});

test('craft — one-off spacing is challenged and density changes systemically', () => {
  assert.match(skill, /arbitrary|one-off/i);
  assert.match(skill, /systemic|profile/i);
  assert.match(skill, /160px/);
  assert.match(skill, /48px/);
  assert.match(skill, /24px/);
  assert.match(skill, /16px/);
});

test('craft — responsive work preserves hierarchy roles, not raw coordinates', () => {
  assert.match(skill, /responsive spatial profile/i);
  assert.match(skill, /hierarchy role/i);
  assert.match(skill, /not .*coordinates/i);
});

test('craft — project DESIGN template can persist the chosen spatial profile', () => {
  assert.match(template, /Spatial Profile/);
  assert.match(template, /Visual Flow/);
});
