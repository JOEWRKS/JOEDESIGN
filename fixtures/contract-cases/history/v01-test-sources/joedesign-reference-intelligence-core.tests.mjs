import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const skill = readFileSync(path.join(root, 'skills/joedesign/SKILL.md'), 'utf8');
const template = readFileSync(path.join(root, 'skills/joedesign/templates/DESIGN.md'), 'utf8');

test('reference — material adoption records source and evidence quality without mandatory ceremony for casual inspiration', () => {
  assert.match(skill, /material reference adoption/i);
  assert.match(skill, /source|provenance/i);
  assert.match(skill, /evidence quality|confidence/i);
  assert.match(skill, /do not require|ordinary inspiration|casual reference/i);
});

test('reference — unknown facts remain unknown instead of being invented', () => {
  assert.match(skill, /unknown.*remain unknown|unknown.*not.*invent|do not invent.*unknown/i);
});

test('reference — relationships are extracted rather than whole-brand recipes copied', () => {
  assert.match(skill, /TAKE/);
  assert.match(skill, /DO NOT TAKE/);
  assert.match(skill, /WHY/);
  assert.match(skill, /APPLIES TO/);
  assert.match(skill, /relationship/i);
});

test('reference — references never override Product Truth or approved project design authority', () => {
  assert.match(skill, /reference.*cannot override|reference.*never.*override/i);
  assert.match(skill, /Product Truth|Product authority/i);
  assert.match(skill, /APPROVED.*DESIGN\.md|approved.*design/i);
});

test('reference — multiple references stay scoped and conflicts are surfaced instead of silently blended', () => {
  assert.match(skill, /multiple references/i);
  assert.match(skill, /conflict/i);
  assert.match(skill, /silently blend|silent.*blend|do not blend/i);
});

test('reference — evidence quality affects trust, not aesthetic authority', () => {
  assert.match(skill, /evidence quality/i);
  assert.match(skill, /not.*aesthetic|does not.*aesthetic|not.*style authority/i);
});

test('reference — external corpora are optional sources, not bundled runtime dependencies or automatic routers', () => {
  assert.match(skill, /optional.*reference source|reference source.*optional/i);
  assert.match(skill, /no bundled.*corpus|do not bundle.*corpus/i);
  assert.match(skill, /no automatic.*router|do not automatically route/i);
});

test('reference — DESIGN template can persist material reference relationships compactly', () => {
  assert.match(template, /Reference Relationships/);
  assert.match(template, /Source/);
  assert.match(template, /Evidence/);
  assert.match(template, /Known/);
  assert.match(template, /Unknown/);
  assert.match(template, /Take/);
  assert.match(template, /Do Not Take/);
  assert.match(template, /Applies To/);
});
