"""Read-only GEO source snapshot: real render and producer/consumer exercise.

This is tool validation, not a product ledger, install, or visual acceptance.
Expectations are derived from DESIGN before capture; no baseline auto-tuning.
"""
import argparse
from collections import Counter
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import threading

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO/'skills/joedesign/scripts'))
from harness.conformance import bindings, load_baseline
from harness.io import digest, file_hash, write_artifact

parser = argparse.ArgumentParser()
parser.add_argument('--product', type=Path, required=True)
parser.add_argument('--consumer', type=Path, required=True)
parser.add_argument('--output', type=Path, required=True)
args = parser.parse_args()
out = args.output.resolve(); out.mkdir(parents=True, exist_ok=False)
project = out/'project'; project.mkdir()
artifacts = out/'artifacts'; artifacts.mkdir()
consumer = artifacts/'consumer-source.mjs'
shutil.copyfile(args.consumer, consumer)
consumer_hash = file_hash(consumer)
assert consumer_hash == file_hash(args.consumer), 'Consumer changed during snapshot'
source = args.product.resolve()/'examples/geo-fresh-market/wireframes'
provenance = []

def copy_file(original, relative):
    before = file_hash(original)
    destination = project/relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(original, destination)
    assert before == file_hash(original) == file_hash(destination), 'Source changed during snapshot'
    provenance.append(dict(source=str(original), relative=relative, sha256=before))

copy_file(args.product/'DESIGN.md', 'DESIGN.md')
# Preserve actual runtime dependencies and built routes, not the product's ledgers.
for name in ('design', 'foundation'):
    for original in sorted((source/name).rglob('*')):
        if original.is_file(): copy_file(original, original.relative_to(source).as_posix())
for original in sorted(source.iterdir()):
    if original.is_file(): copy_file(original, original.name)
write_artifact(out/'provenance-before.json', provenance)

targets, checks, rules = [], [], []
runtime = [p['relative'] for p in provenance if p['relative'] != 'DESIGN.md']

def add(target, name, value, count=1, **criterion):
    criterion.update(expected_count=count, min=value, max=value, tolerance=.25, max_spread=.25)
    ident = target['id']+'-'+name
    checks.append(dict(check_id=ident, rule_id=ident, target_id=target['id'], lane='visual',
                       method='geometry', criterion=criterion, criterion_sha256=digest(criterion), inputs=runtime))
    rules.append(dict(id=ident, source_ref='DESIGN.md#여백-적용검사-기준--2026-10-10-보정',
                      target_ids=[target['id']], methods=['geometry']))

def pair(target, name, a, b, value, count=1, start='bottom', end='top'):
    add(target, name, value, count, kind='pair', **{'from':a,'to':b}, from_edge=start, to_edge=end)

for route, widths in [('products', [320,390,768,1023,1024,1440]), ('collections',[320,390,1440])]:
    for width in widths:
        t = dict(id=f'{route}-{width}', route=f'/design/site/{route}/', surface=route, family=route,
                 viewport=[width,900], state='fresh-session-default', theme='light', locale='ko-KR',
                 required_kinds=['render','technical'])
        targets.append(t)
        pair(t, 'header-height', '.site-header', '.site-header', 154, start='top', end='bottom')
        if width <= 1023:
            pair(t, 'logo-top', '.header-inner', '.brand-approved', 16, start='top')
            pair(t, 'logo-search', '.brand-approved', '.site-header .search-form', 16)
            pair(t, 'search-bottom', '.site-header .search-form', '.header-inner', 16, end='bottom')
        if route == 'products':
            pair(t,'name-price','.card-content h3','.card-price-row',8,9)
            pair(t,'price-review','.card-price-row','.card-reviews',8,9)
            if width in (320,390,1440):
                # Text starts at the heading box, not its padded wrapper boundary.
                pair(t,'image-text','.product-photo','.card-content h3',8 if width<768 else 16,9)
        else:
            add(t,'copy-gaps',16,4,kind='gap',container='.campaign-copy',items=':scope > h3, :scope > p, :scope > a',axis='y')
            for edge in ('top','bottom'):
                add(t,'copy-'+edge,24 if width<768 else 32,2,kind='inset',container='.campaign-copy',
                    items=':scope > h3, :scope > p, :scope > a',edge=edge)

baseline = dict(schema='joeness.review-baseline.v1', scope_id='geo-readonly-header-card-campaign-geometry',
                authorization_ref='JOEDESIGN tool validation request; DESIGN observed mapping; NOT product approval or independently reviewed completeness',
                authority=[dict(path='DESIGN.md',sha256=file_hash(project/'DESIGN.md'))], targets=targets,
                rules=rules, required_checks=checks, required_lanes=['visual'], required_acceptance=True)
baseline_path = project/'baseline.json'; write_artifact(baseline_path,baseline)
pin = file_hash(baseline_path)
load_baseline(baseline_path,pin,project)
write_artifact(out/'frozen-expectations.json', dict(baseline_sha256=pin, targets=len(targets), checks=len(checks),
    expected_mutation='Changing only copied card gap to 24 must fail name-price and price-review, consumer visual blocked.',
    expected_complete='Blocked regardless of geometry success; no whole-product acceptance supplied.',
    exclusions=['checkout/my/policy/PDP','functional flows','optical/glyph bounds','independent specialist judgment','live model adherence','product activation']))

class Quiet(SimpleHTTPRequestHandler):
    extensions_map = {**SimpleHTTPRequestHandler.extensions_map,'.mjs':'text/javascript; charset=utf-8'}
    def log_message(self,*args): pass
server = ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(project)))
thread = threading.Thread(target=server.serve_forever,daemon=True); thread.start()
results = {}

def consume(name, receipt, claim='visual'):
    command = ['node',str(consumer),'--root',str(project),'--baseline','baseline.json',
               '--baseline-sha256',pin,'--result',str(receipt),'--evidence-root',str(artifacts),'--claim',claim]
    p = subprocess.run(command,capture_output=True,text=True,encoding='utf-8',timeout=120)
    result = dict(exit_code=p.returncode,result=json.loads(p.stdout))
    write_artifact(artifacts/(name+'.json'),result)
    results[name] = result
    return result

def capture(name):
    request = dict(output_dir=str(artifacts/name),targets=targets,build_id=digest([[p,file_hash(project/p)] for p in runtime]),
        browser=dict(base_url=f'http://127.0.0.1:{server.server_port}',
            playwright_module=os.environ['JOEDESIGN_PLAYWRIGHT_MODULE'],executable=os.environ['JOEDESIGN_BROWSER_EXECUTABLE'],
            probes={t['id']:dict(assertions=[dict(selector='#main',visible=True),dict(selector='.product-card' if t['surface']=='products' else '.campaign-copy',count=9 if t['surface']=='products' else 2)]) for t in targets}),
        design=dict(baseline_sha256=pin,input_fingerprints=bindings(baseline,project,[t['id'] for t in targets]),checks=checks))
    p = subprocess.run(['node',str(REPO/'skills/joedesign/scripts/capture.mjs')],input=json.dumps(request),capture_output=True,text=True,encoding='utf-8',timeout=240)
    assert p.returncode==0,p.stderr
    raw=json.loads(p.stdout);write_artifact(artifacts/(name+'-capture.json'),raw)
    assert not raw['errors'],raw['errors']
    receipt=artifacts/(name+'-receipt.json')
    command=[sys.executable,str(REPO/'skills/joedesign/scripts/harness_cli.py'),'verify-design','--project',str(project),
             '--baseline',str(baseline_path),'--baseline-sha256',pin,'--output',str(receipt)]
    for c in raw['captures']:
        if c['kind']=='technical':command+=['--observation',c['path']]
    p=subprocess.run(command,capture_output=True,text=True,encoding='utf-8',timeout=120)
    assert p.returncode in (0,2),p.stderr+p.stdout
    report=json.loads(receipt.read_text(encoding='utf-8'))
    results[name]=dict(exit_code=p.returncode,counts=dict(Counter(r['status'] for r in report['results'])),
                       nonpass=[r for r in report['results'] if r['status']!='PASS'])
    print(json.dumps({name:dict(exit_code=p.returncode,counts=results[name]['counts'],
        nonpass=[dict(check_id=r['check_id'],status=r['status'],values=r.get('measured_values')) for r in results[name]['nonpass']])},ensure_ascii=False),flush=True)
    return receipt

css=project/'design/visual.css';saved=css.read_bytes()
try:
    original=capture('observed')
    consume('observed-visual',original)
    assert consume('observed-complete',original,'complete')['exit_code']==2
    css.write_bytes(saved+b'\nbody[data-visual=true] .card-content{gap:24px!important}\n')
    assert consume('stale-after-mutation',original)['exit_code']==2
    mutated=capture('injected-gap')
    assert any(r['status']=='FAIL' and r['check_id'].endswith('name-price') for r in results['injected-gap']['nonpass'])
    assert consume('injected-visual',mutated)['exit_code']==2
    css.write_bytes(saved)
    consume('restored-visual',original)
finally:
    css.write_bytes(saved)
    server.shutdown();server.server_close();thread.join()
    changed=[p['source'] for p in provenance if file_hash(Path(p['source']))!=p['sha256']]
    write_artifact(out/'results.json',dict(baseline_sha256=pin,consumer_sha256=consumer_hash,
        source_changes_during_run=changed,scenarios=results))
print(json.dumps(dict(output=str(out),source_changes=changed),ensure_ascii=False))
