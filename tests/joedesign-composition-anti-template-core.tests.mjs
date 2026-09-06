import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const skill = readFileSync(path.join(root, 'skills/joedesign/SKILL.md'), 'utf8');
const template = readFileSync(path.join(root, 'skills/joedesign/templates/DESIGN.md'), 'utf8');
const composition = skill.match(/^## [^\r\n]*composition[^\r\n]*\r?\n[\s\S]*?(?=^## |(?![\s\S]))/im)?.[0] ?? '';
const compositionTemplate = template.match(/^## Composition\r?\n[\s\S]*?(?=^## |(?![\s\S]))/m)?.[0] ?? '';

test('composition — Product priority and task or narrative flow precede pattern choice', () => {
  assert.match(composition, /Product priority/i);
  assert.match(composition, /task|narrative/i);
  assert.match(composition, /before.*(?:pattern|layout)|structure before pattern/i);
});

test('composition — cards and containers require semantic containment rather than decoration', () => {
  assert.match(composition, /semantic containment/i);
  assert.match(composition, /card|container/i);
  assert.match(composition, /do not|challenge|not.*merely/i);
});

test('composition — familiar AI SaaS patterns are challenge triggers not blanket bans', () => {
  assert.match(composition, /hero.*right image|three.*feature|3.*card|pill/i);
  assert.match(composition, /challenge trigger/i);
  assert.match(composition, /not.*blanket ban|not.*ban/i);
});

test('composition — repetition expresses equivalence and variation expresses meaningful change', () => {
  assert.match(composition, /repetition.*equivalence|equivalence.*repetition/i);
  assert.match(composition, /variation.*(?:change|priority|role)|(?:change|priority|role).*variation/i);
});

test('composition — intentional asymmetry may support hierarchy without novelty for its own sake', () => {
  assert.match(composition, /intentional asymmetry/i);
  assert.match(composition, /hierarchy|narrative|focal/i);
  assert.match(composition, /novelty/i);
});

test('composition — distinctiveness never overrides Product Truth usability or accessibility', () => {
  assert.match(composition, /Product Truth|Product/i);
  assert.match(composition, /usability|interaction cost|reachability/i);
  assert.match(composition, /accessibility/i);
});

test('composition — mobile recomposes priority instead of shrinking desktop coordinates', () => {
  assert.match(composition, /recompose/i);
  assert.match(composition, /mobile/i);
  assert.match(composition, /desktop coordinates|compressed desktop|shrink/i);
});

test('composition — DESIGN persists compact structural authority and material claims require actual renders', () => {
  assert.match(compositionTemplate, /## Composition/);
  assert.match(compositionTemplate, /### Structural Sequence/);
  assert.match(compositionTemplate, /### Major Region Roles/);
  assert.match(compositionTemplate, /### Containment Rules/);
  assert.match(compositionTemplate, /### Repetition \/ Variation/);
  assert.match(compositionTemplate, /### Responsive Composition/);
  assert.match(compositionTemplate, /### Approved Evidence/);
  assert.match(composition, /actual target render|actual render/i);
});
