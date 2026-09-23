import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const skill = readFileSync(path.join(root, 'skills/joedesign/SKILL.md'), 'utf8');
const template = readFileSync(path.join(root, 'skills/joedesign/templates/DESIGN.md'), 'utf8');

test('color — semantic role is chosen before local color value', () => {
  assert.match(skill, /Role before color value/i);
  assert.match(skill, /semantic color role/i);
  assert.match(skill, /local (?:color )?value/i);
});

test('color — contrast hierarchy and accent ownership reinforce Product priority', () => {
  assert.match(skill, /contrast hierarchy/i);
  assert.match(skill, /accent ownership|accent owner/i);
  assert.match(skill, /Product priority/i);
  assert.match(skill, /not .*every(?:thing| element).*equally loud|do not make every(?:thing| element).*equally loud/i);
});

test('color — neutral surfaces express real layer and containment relationships', () => {
  assert.match(skill, /neutral|surface color/i);
  assert.match(skill, /layer|containment/i);
  assert.match(skill, /actual|real .*relationship/i);
  assert.match(skill, /not .*panel .*every group|does not require .*panel .*every group/i);
});

test('color — functional state colors preserve Product semantics without color-only meaning', () => {
  assert.match(skill, /state color/i);
  assert.match(skill, /preserve.*Product semantics|may not invent or change .*state/i);
  assert.match(skill, /color .*only cue|sole .*color|color alone/i);
});

test('color — applicable WCAG 2.2 AA ratios are minimum gates, not an aesthetic preset', () => {
  assert.match(skill, /WCAG 2\.2 AA/i);
  assert.match(skill, /4\.5:1/);
  assert.match(skill, /3:1/);
  assert.match(skill, /minimum .*gate/i);
  assert.match(skill, /not an aesthetic preset|not .*aesthetic/i);
});

test('color — material contrast is evaluated in actual foreground/background context', () => {
  assert.match(skill, /actual foreground\/background|foreground\/background .*actual/i);
  assert.match(skill, /token existence .*not .*proof|do not treat token existence as proof/i);
  assert.match(skill, /actual render|actual rendering/i);
});

test('color — responsive and light-dark translation preserves roles while values may change', () => {
  assert.match(skill, /responsive/i);
  assert.match(skill, /light\/dark|light and dark/i);
  assert.match(skill, /preserve semantic .*role|semantic .*role.*preserv/i);
  assert.match(skill, /value(?:s)? may change|values? .*change/i);
});

test('color — project DESIGN template persists compact color authority', () => {
  assert.match(template, /Color Roles/);
  assert.match(template, /Accent Ownership/);
  assert.match(template, /Surface \/ Layer Relationships/);
  assert.match(template, /State \/ Contrast Constraints/);
  assert.match(template, /sourced\/approved|sourced or approved/i);
});
