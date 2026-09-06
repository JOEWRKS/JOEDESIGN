import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync, readdirSync, existsSync} from 'node:fs';
import {createHash} from 'node:crypto';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const skillRoot = path.join(root, 'skills/joedesign');
const read = p => readFileSync(path.join(root, p), 'utf8');
const hash = s => createHash('sha256').update(s).digest('hex');
const walk = dir => existsSync(dir) ? readdirSync(dir, {withFileTypes:true}).flatMap(e => e.isDirectory() ? walk(path.join(dir,e.name)) : [path.join(dir,e.name)]) : [];
const expectActions = {
  '02':['preserve-retry-and-state-semantics','refine-presentation-within-product-truth'],
  '03':['absent-create-draft','retain-approved-rev3-and-propose-draft-rev4','require-explicit-approval-for-promotion'],
  '04':['produce-2-or-3-materially-distinct-directions','keep-product-facts-identical-across-candidates'],
  '05':['bounded-refinement','preserve-approved-direction'],
  '06':['identify-take-do-not-take-why-applies-to','treat-reference-as-advisory'],
  '07':['bounded-browser-render-proof-before-expansion','inspect-actual-render','show-candidate-without-self-approval'],
  '08':['inspect-exact-current-render','bounded-hero-typography-change','rerender-same-surface-state-viewport'],
  '09':['retain-composition-and-adjust-type-hierarchy','preserve-unrelated-components'],
  '10':['diagnose-direction-against-rejected-evidence','reenter-bounded-exploration-and-proof','stop-dependent-expansion'],
  '11':['recompose-for-mobile-hierarchy-crop-reachability','preserve-required-content-and-actions','inspect-mobile-render'],
  '12':['managed-route-affected-scope-via-joeflow-to-product-definition','unmanaged-raise-to-current-product-authority-or-user','continue-independent-work'],
  '13':['A-PASS','B-FAIL','C-UNVERIFIED','record-source-target-expected-observed-verdict'],
  '14':['technical-pass','visual-unverified','report-exact-unverified-boundary'],
  '15':['visual-pass-with-evidence','user-acceptance-not-granted','continue-authorized-bounded-work']
};
const casesText = read('fixtures/contract-cases/decisions.json');
const cases = JSON.parse(casesText);
// Deterministic replay of real Astra decisions, NOT a simulated policy engine or
// a claim that prose matching proves behavior. The actual producer/rollout is
// pinned in observed.json; any skill or case change requires fresh evidence.
function observed() {
  assert.ok(existsSync(path.join(skillRoot,'SKILL.md')), 'JOEDESIGN implementation missing');
  assert.ok(existsSync(path.join(root,'fixtures/contract-cases/observed.json')), 'Fresh contract decision evidence missing');
  const record = JSON.parse(read('fixtures/contract-cases/observed.json'));
  const files = walk(skillRoot).map(p=>path.relative(skillRoot,p).replaceAll('\\','/')).sort();
  assert.deepEqual(Object.keys(record.skillSha256).sort(), files, 'Evidence must cover the entire shipped skill');
  for (const file of files) assert.equal(hash(readFileSync(path.join(skillRoot,file))), record.skillSha256[file], 'Skill changed: rerun contract decisions');
  assert.match(record.casesSha256,/^[a-f0-9]{64}$/, 'Original runtime input byte hash required');
  assert.equal(hash(JSON.stringify(cases)), record.casesDataSha256, 'Contract scenario data changed: rerun decisions');
  assert.equal(record.runtime.model,'gpt-6-astra');
  assert.equal(record.runtime.effort,'xhigh');
  assert.match(record.runtime.threadId,/^[a-f0-9-]{36}$/);
  assert.match(record.runtime.rolloutSha256,/^[a-f0-9]{64}$/);
  assert.equal(record.responses.length,14);
  assert.equal(new Set(record.responses.map(r=>r.id)).size,14);
  return record;
}
test('01 — single public entrypoint', () => {
  const skills = walk(path.join(root,'skills')).filter(p=>path.basename(p)==='SKILL.md');
  assert.deepEqual(skills.map(p=>path.relative(root,p).replaceAll('\\','/')), ['skills/joedesign/SKILL.md']);
  const source = read('skills/joedesign/SKILL.md');
  const frontmatter = source.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  assert.ok(frontmatter,'Discoverable skill frontmatter required');
  assert.match(frontmatter[1],/^name: joedesign$/m);
  assert.match(frontmatter[1],/^description: .+/m);
  const metadata = read('skills/joedesign/agents/openai.yaml');
  assert.match(metadata,/display_name: "JOEDESIGN"/);
  assert.match(metadata,/\$joedesign/);
  assert.doesNotMatch(metadata,/allow_implicit_invocation: false|dependencies:/);
});
for (const c of cases) {
  test(c.id+' — '+c.name, () => {
    const record = observed();
    const actual = record.responses.find(r=>r.id===c.id);
    assert.ok(actual,'Missing actual Astra decision');
    assert.deepEqual([...actual.actions].sort(),[...expectActions[c.id]].sort(),c.request);
    assert.equal(new Set(actual.actions).size,actual.actions.length);
    for (const action of actual.actions) assert.ok(c.choices.includes(action),'Unknown action');
    assert.ok(typeof actual.reason==='string' && actual.reason.trim().length>0,'Actual rationale required');
  });
}
test('16 — external competitor dependencies absent in repository and installable skill', () => {
  const files = walk(root).filter(p=>!p.startsWith(path.join(root,'.git')+path.sep)).map(p=>path.relative(root,p).replaceAll('\\','/')).sort();
  const allowed = new Set(['AGENTS.md','README.md','docs/architecture/JOEDESIGN_OPERATING_MODEL_V1.md','docs/handoffs/JOEDESIGN_REFERENCE_INTELLIGENCE_VALIDATION_V1.md','docs/specs/joedesign-v0.1.md','docs/specs/joedesign-craft-core-v0.1.md','docs/specs/joedesign-typography-scale-core-v0.1.md','docs/specs/joedesign-reference-intelligence-core-v0.1.md','skills/joedesign/SKILL.md','skills/joedesign/agents/openai.yaml','skills/joedesign/templates/DESIGN.md','tests/joedesign-contract.tests.mjs','tests/joedesign-craft-core.tests.mjs','tests/joedesign-typography-scale-core.tests.mjs','tests/joedesign-reference-intelligence-core.tests.mjs']);
  for (const file of files) assert.ok(allowed.has(file)||file.startsWith('fixtures/contract-cases/'),'Unexpected runtime/vendor surface: '+file);
  const expectedSkill = ['SKILL.md','agents/openai.yaml','templates/DESIGN.md'];
  assert.deepEqual(walk(skillRoot).map(p=>path.relative(skillRoot,p).replaceAll('\\','/')).sort(),expectedSkill);
  assert.doesNotMatch(read('skills/joedesign/agents/openai.yaml'),/dependencies:|transport:|url:/);
  const runtime = read('skills/joedesign/SKILL.md');
  assert.doesNotMatch(runtime,/vendor\//i);
  // An optional installed copy must be a byte-exact three-file pure-core copy.
  if (process.env.JOEDESIGN_INSTALLED_SKILL) {
    const installed=path.resolve(process.env.JOEDESIGN_INSTALLED_SKILL);
    assert.deepEqual(walk(installed).map(p=>path.relative(installed,p).replaceAll('\\','/')).sort(),expectedSkill);
    for (const file of expectedSkill) assert.equal(hash(readFileSync(path.join(installed,file))),hash(readFileSync(path.join(skillRoot,file))));
  }
});
