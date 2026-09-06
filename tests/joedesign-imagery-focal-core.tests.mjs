import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const skill = readFileSync(path.join(root, 'skills/joedesign/SKILL.md'), 'utf8');
const template = readFileSync(path.join(root, 'skills/joedesign/templates/DESIGN.md'), 'utf8');
const imagery = skill.match(/^## [^\r\n]*imagery[^\r\n]*\r?\n[\s\S]*?(?=^## |\s*$)/im)?.[0] ?? '';
const imageryTemplate = template.match(/^## Imagery \/ Artwork\r?\n[\s\S]*?(?=^## |\s*$)/m)?.[0] ?? '';

test('imagery — role precedes treatment and informative imagery remains Product content', () => {
  assert.match(imagery, /Role before (?:asset )?treatment/i);
  assert.match(imagery, /FOCAL/);
  assert.match(imagery, /SUPPORT/);
  assert.match(imagery, /DECORATIVE/);
  assert.match(imagery, /informative imagery.*Product (?:content|meaning)|Product (?:content|meaning).*informative imagery/i);
});

test('imagery — focal ownership or visual sequence is intentional', () => {
  assert.match(imagery, /intentional focal (?:owner|ownership)|focal (?:owner|ownership).*intentional/i);
  assert.match(imagery, /sequence/i);
});

test('imagery — text-image dominance is deliberate rather than accidental co-dominance', () => {
  assert.match(imagery, /text[- ↔]+image dominance/i);
  assert.match(imagery, /deliberate|intentional/i);
  assert.match(imagery, /accidental co-dominance/i);
});

test('imagery — crop and focal point preserve important or required image content', () => {
  assert.match(imagery, /important (?:subject|focal region)/i);
  assert.match(imagery, /blind [`'“”"]?center(?:ed)?(?: center)?[`'“”"]? crop|blind center-crop/i);
  assert.match(imagery, /preserv\w*.*(?:important|required).*(?:image )?content|(?:important|required).*(?:image )?content.*preserv\w*/i);
});

test('imagery — scale and negative space express image priority without fixed ratios', () => {
  assert.match(imagery, /scale (?:and|\/) negative space (?:express|communicate) (?:image )?priority/i);
  assert.match(imagery, /no fixed.*(?:ratio|percentage)|do not (?:enforce|require).*fixed.*(?:ratio|percentage)/i);
});

test('imagery — references contribute imagery relationships without copied assets or invented source facts', () => {
  assert.match(imagery, /(?:image|imagery|reference) relationships?/i);
  assert.match(imagery, /reference relationship\s*(?:≠|is not|does not mean)\s*(?:a )?copied asset|not (?:a )?copied asset|do not copy.*assets?/i);
  assert.match(imagery, /unknown source (?:facts|truth).*unknown|do not invent.*source (?:facts|truth)|invented source (?:facts|truth)/i);
});

test('imagery — responsive translation may recrop reposition or recompose while preserving role and required content', () => {
  assert.match(imagery, /recrop/i);
  assert.match(imagery, /reposition/i);
  assert.match(imagery, /recompose/i);
  assert.match(imagery, /preserv\w*.*(?:image )?role/i);
  assert.match(imagery, /preserv\w*.*required (?:image )?content|required (?:image )?content.*remain/i);
});

test('imagery — project DESIGN persists compact focal authority and material claims require actual target renders', () => {
  assert.match(imageryTemplate, /## Imagery \/ Artwork/);
  assert.match(imageryTemplate, /### Role/);
  assert.match(imageryTemplate, /### Focal Owner/);
  assert.match(imageryTemplate, /### Text-Image Relationship/);
  assert.match(imageryTemplate, /### Important Focal \/ Crop Rule/);
  assert.match(imageryTemplate, /### Responsive Translation/);
  assert.match(imageryTemplate, /### Approved Evidence/);
  assert.match(imagery, /actual target render.*(?:crop|focal)|(?:crop|focal).*actual target render/i);
});
