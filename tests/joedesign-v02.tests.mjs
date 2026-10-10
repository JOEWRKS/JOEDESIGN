import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const read=p=>fs.readFileSync(path.join(root,p));
const json=p=>JSON.parse(read(p).toString('utf8').replace(/^\uFEFF/,''));
const hash=b=>createHash('sha256').update(b).digest('hex');
const ev='fixtures/contract-cases/evidence/visual-translation-v02';
const freeze=json(`${ev}/baseline-and-freeze.json`);
const fixture='fixtures/contract-cases/visual-translation-v02';
const walk=dir=>fs.readdirSync(dir,{withFileTypes:true}).flatMap(e=>e.isDirectory()?walk(path.join(dir,e.name)):[path.join(dir,e.name)]);
// Historical evidence stays bound to the exact pre-unification package.
// Current public package behavior is checked by the Python integration suite.
const packageRoot='fixtures/package-history/pre-unification-20261009/skills/joedesign';
const skill=path.join(root,packageRoot);
const files=['SKILL.md','agents/openai.yaml','templates/DESIGN.md'];
const inventory=()=>walk(skill).map(p=>path.relative(skill,p).replaceAll('\\','/')).sort();

test('history — archived v0.2 package identity and inventory',()=>{
  assert.deepEqual(inventory(),files);
  const source=read(`${packageRoot}/SKILL.md`).toString();
  assert.match(source,/^---\r?\nname: joedesign\r?\ndescription: [^\n]+\r?\n---/);
  const meta=read(`${packageRoot}/agents/openai.yaml`).toString();
  assert.match(meta,/\$joedesign/);
  assert.doesNotMatch(meta,/dependencies:|transport:|url:/);
});

test('package — a project-local copy resolves its shipped relative links without repo docs',()=>{
  const temp=fs.mkdtempSync(path.join(os.tmpdir(),'joedesign-v02-copy-'));
  try {
    const dest=path.join(temp,'.agents/skills/joedesign');
    fs.cpSync(skill,dest,{recursive:true});
    assert.deepEqual(walk(dest).map(p=>path.relative(dest,p).replaceAll('\\','/')).sort(),files);
    for(const file of files) assert.equal(hash(fs.readFileSync(path.join(dest,file))),hash(fs.readFileSync(path.join(skill,file))));
    const source=fs.readFileSync(path.join(dest,'SKILL.md'),'utf8');
    for(const m of source.matchAll(/\[[^\]]+\]\(([^)]+)\)/g)) {
      if(/^https?:/.test(m[1])) continue;
      const target=path.resolve(dest,m[1].split('#')[0]);
      assert.ok(target.startsWith(dest+path.sep),'Link escapes shipped package');
      assert.ok(fs.existsSync(target),`Unshipped link ${m[1]}`);
    }
  } finally { fs.rmSync(temp,{recursive:true,force:true}); }
});

test('history — original failures, semantic responses, Smokes, doctrines and test source bytes survive',()=>{
  for(const f of freeze.preserved) assert.equal(hash(read(f.path)),f.sha256,f.original);
  assert.equal(freeze.baselinePass,72); assert.equal(freeze.baselineFail,0);
  assert.equal(freeze.baselineExitCode,0);
});

test('inputs — pre-execution scenarios and reviewer expectations were not tuned after output',()=>{
  for(const f of freeze.frozen) assert.equal(hash(read(f.path)),f.sha256,f.path);
  assert.deepEqual(json(`${fixture}/inputs.json`).map(c=>c.id),['B01','B02','B03','B04','B05','B06','B07','B08','B09']);
});

function fresh() {
  const record=json(`${ev}/fresh-review.json`);
  assert.equal(record.kind,'text-only functional decisions; not visual quality');
  assert.equal(record.runtime.model,'gpt-6-astra');
  assert.equal(record.runtime.effort,'xhigh');
  assert.match(record.runtime.threadId,/^[a-f0-9-]{36}$/);
  assert.equal(record.realProjectVisualValidation,'PENDING');
  assert.equal(record.expectationsSha256,hash(read(`${fixture}/expectations.json`)));
  assert.deepEqual(Object.keys(record.package).sort(),files);
  for(const file of files) assert.equal(record.package[file],hash(read(`${packageRoot}/${file}`)),'Historical evidence must remain bound to the archived v0.2 package');
  for(const f of Object.values(record.artifacts)) assert.equal(hash(read(`${ev}/${f.path}`)),f.sha256,f.path);
  assert.notEqual(record.artifacts.eventStream.sha256,record.artifacts.response.sha256,'Execution stream and response are different artifacts');
  const native=json(`${ev}/${record.artifacts.nativeProvenance.path}`);
  assert.equal(native.threadId,record.runtime.threadId);
  assert.equal(native.model,record.runtime.model);
  assert.equal(native.effort,record.runtime.effort);
  assert.match(native.nativeRolloutSha256,/^[a-f0-9]{64}$/);
  assert.notEqual(native.nativeRolloutSha256,record.artifacts.response.sha256);
  assert.equal(native.input.normalizedMatch,true);
  assert.equal(native.response.normalizedMatch,true);
  assert.equal(native.input.fileSha256,record.artifacts.input.sha256);
  assert.equal(native.response.fileSha256,record.artifacts.response.sha256);
  assert.equal(native.toolCalls,0);
  const events=read(`${ev}/${record.artifacts.eventStream.path}`).toString().trim().split(/\r?\n/).map(JSON.parse);
  assert.equal(events.find(e=>e.type==='thread.started').thread_id,record.runtime.threadId);
  assert.ok(events.some(e=>e.type==='turn.completed'));
  assert.ok(!events.some(e=>e.type==='turn.failed'||e.type==='error'));
  const agents=events.filter(e=>e.type==='item.completed'&&e.item?.type==='agent_message');
  assert.equal(agents.at(-1).item.text.trim(),read(`${ev}/${record.artifacts.response.path}`).toString().trim());
  const execution=json(`${ev}/${record.artifacts.execution.path}`);
  assert.equal(execution.exitCode,0);
  assert.deepEqual(execution.package.map(f=>f.path).sort(),files);
  for(const f of execution.package) {
    assert.equal(f.sha256,record.package[f.path],'Execution package cannot be rebound by reviewer metadata');
    assert.equal(f.bytes,read(`${packageRoot}/${f.path}`).length);
  }
  assert.equal(execution.inputSha256,record.artifacts.input.sha256);
  assert.equal(execution.inputsSha256,hash(read(`${fixture}/inputs.json`)));
  assert.equal(execution.expectationsSha256,record.expectationsSha256);
  const input=read(`${ev}/${record.artifacts.input.path}`).toString();
  assert.ok(input.includes(read(`${fixture}/inputs.json`).toString()));
  assert.ok(input.includes(read(`${packageRoot}/SKILL.md`).toString()));
  assert.ok(input.includes(read(`${packageRoot}/templates/DESIGN.md`).toString()));
  assert.ok(!input.includes(read(`${fixture}/expectations.json`).toString()));
  return record;
}

test('historical evidence — response, input, actual execution and archived v0.2 package are linked',()=>{fresh();});

// These replay a recorded qualitative review, not a policy engine or live model.
// A PASS count here does not turn text-only decisions into rendered evidence.
for(const id of ['B01','B02','B03','B04','B05','B06','B07','B08','B09']) {
  test(`recorded decision ${id} — fixed qualitative obligations satisfied`,()=>{
    const r=fresh();
    assert.deepEqual(r.cases.map(c=>c.id),['B01','B02','B03','B04','B05','B06','B07','B08','B09']);
    const c=r.cases.find(c=>c.id===id);
    assert.equal(c.verdict,'PASS');
    const expectation=json(`${fixture}/expectations.json`).cases.find(c=>c.id===id);
    assert.equal(c.findings.length,expectation.required.length);
    const response=JSON.parse(read(`${ev}/${r.artifacts.response.path}`).toString()).responses.find(c=>c.id===id).response;
    for(let i=0;i<c.findings.length;i++) {
      assert.equal(c.findings[i].requirement,expectation.required[i]);
      assert.equal(c.findings[i].satisfied,true);
      assert.ok(c.findings[i].note.length>0);
      assert.ok(response.includes(c.findings[i].quote),'Review quotation must exist in actual response');
    }
  });
}
