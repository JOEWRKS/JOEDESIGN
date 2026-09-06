import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const read = p => readFileSync(path.join(root, p), 'utf8');
const skill = read('skills/joedesign/SKILL.md');
const spec = read('docs/specs/joedesign-implementation-bridge-v0.1.md');

test('bridge — implementation mapping is derivative, not visual authority', () => {
  assert.match(skill, /Implementation Bridge/i);
  assert.match(skill, /derivative|does not create.*authority|cannot.*amend/i);
  assert.match(skill, /APPROVED.*DESIGN\.md/i);
});

test('bridge — exact approved values may map while unknown values remain unresolved', () => {
  assert.match(skill, /exact approved|exact.*value/i);
  assert.match(skill, /unknown.*remain.*unresolved|do not invent.*token/i);
});

test('bridge — existing project-native token roles are preferred over forced renaming', () => {
  assert.match(skill, /project-native/i);
  assert.match(skill, /existing.*token|existing.*role/i);
  assert.match(skill, /do not.*rename|not.*force.*naming/i);
});

test('bridge — structured tokens remain distinct from visual rationale', () => {
  assert.match(skill, /structured.*token|machine-readable/i);
  assert.match(skill, /rationale|intent/i);
  assert.match(skill, /do not.*manufacture|do not.*invent/i);
});

test('bridge — Google design.md interoperability is optional and dependency-free', () => {
  assert.match(skill, /Google.*design\.md/i);
  assert.match(skill, /optional|when present|when.*benefit/i);
  assert.match(skill, /not.*dependency|do not require.*Google/i);
  assert.doesNotMatch(skill, /@google\/design\.md.*required/i);
});

test('bridge — custom JOEDESIGN sections survive structured interoperability', () => {
  assert.match(skill, /custom.*section|unknown.*section|preserve.*section/i);
  assert.match(skill, /Visual Flow|Approved Visual Evidence|Open Visual Decisions/);
});

test('bridge — material mapping changes use bounded semantic diff or review', () => {
  assert.match(skill, /mapping.*change|token.*mapping/i);
  assert.match(skill, /diff|compare/i);
  assert.match(skill, /material/i);
});

test('bridge — token mapping success never replaces actual rendered verification', () => {
  assert.match(skill, /mapping.*PASS|token.*success|lint.*success|export.*success/i);
  assert.match(skill, /actual.*render|rendered.*observation/i);
  assert.match(skill, /Visual.*PASS|visual conformance/i);
  assert.match(spec, /Token Mapping PASS[\s\S]*Visual Conformance PASS/);
});
