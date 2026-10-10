"""Observe the prepared scope, audit served dependencies and selective staleness."""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
import json,os,subprocess,sys,threading
from pathlib import Path
REPO=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(REPO/'skills/joedesign/scripts'))
from harness.conformance import bindings,evaluate,load_baseline
from harness.io import file_hash,write_artifact
p=argparse.ArgumentParser();p.add_argument('--root',type=Path,required=True);p.add_argument('--package',type=Path,default=REPO/'skills/joedesign');a=p.parse_args()
root=a.root.resolve();project=root/'project';artifacts=root/'artifacts';artifacts.mkdir(exist_ok=False)
review=json.loads((root/'scope-review.json').read_text(encoding='utf-8'))
baseline_path=project/review['baseline'];pin=review['baseline_sha256'];b=load_baseline(baseline_path,pin,project)
prefix='examples/geo-fresh-market/wireframes/'
class Quiet(SimpleHTTPRequestHandler):
    extensions_map={**SimpleHTTPRequestHandler.extensions_map,'.mjs':'text/javascript'}
    def log_message(self,*a):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(project/prefix)))
t=threading.Thread(target=server.serve_forever,daemon=True);t.start()
browser=dict(base_url=f'http://127.0.0.1:{server.server_port}',playwright_module=os.environ['JOEDESIGN_PLAYWRIGHT_MODULE'],executable=os.environ['JOEDESIGN_BROWSER_EXECUTABLE'])
def run(script,request):
    p=subprocess.run(['node',str(script)],input=json.dumps(request),capture_output=True,text=True,encoding='utf-8',timeout=180)
    assert p.returncode==0,p.stderr
    return json.loads(p.stdout)
try:
    audit=run(Path(__file__).with_name('audit-runtime.mjs'),dict(**browser,project=str(project),prefix=prefix,targets=b['targets'],checks=b['required_checks']))
    write_artifact(artifacts/'dependencies.json',audit)
    assert all(t['valid'] for t in audit),[(t['target_id'],[r for r in t['resources'] if not r['valid']]) for t in audit if not t['valid']]
    browser['probes']={t['id']:dict(assertions=[dict(selector='#main',visible=True),dict(selector='.product-card' if t['surface']=='products' else '.campaign-copy',count=9 if t['surface']=='products' else 2)]) for t in b['targets']}
    capture=run(a.package/'scripts/capture.mjs',dict(output_dir=str(artifacts/'capture'),targets=b['targets'],build_id=pin,browser=browser,
      design=dict(baseline_sha256=pin,input_fingerprints=bindings(b,project,[t['id'] for t in b['targets']]),checks=b['required_checks'])))
    write_artifact(artifacts/'capture.json',capture);assert not capture['errors'],capture['errors']
    obs=[Path(c['path']) for c in capture['captures'] if c['kind']=='technical']
    result=evaluate(b,pin,project,obs);write_artifact(artifacts/'receipt.json',result)
    assert result['eligible'],result['unresolved']
    outcomes={'original':True,'network_targets':len(audit),'checks':len(result['results'])}
    old=project/prefix/'design/old-review.png';old.write_bytes(b'unrelated review evidence')
    outcomes['unrelated_capture_keeps_proof']=evaluate(b,pin,project,obs)['eligible']
    html=project/prefix/'design/site/collections/index.html';saved=html.read_bytes()
    try:
        html.write_bytes(saved+b'\n<!-- changed output -->')
        rows=evaluate(b,pin,project,obs)['results']
        outcomes['collection_change_only_stales_collection']=all(r['status']==('PASS' if r['target_id'].startswith('products-') else 'UNVERIFIED') for r in rows)
    finally:html.write_bytes(saved)
    css=project/prefix/'design/visual.css';saved=css.read_bytes()
    try:
        css.write_bytes(saved+b'\n/* changed shared style */')
        outcomes['shared_style_stales_all']=all(r['status']=='UNVERIFIED' for r in evaluate(b,pin,project,obs)['results'])
    finally:css.write_bytes(saved)
    outcomes['recovery']=evaluate(b,pin,project,obs)['eligible']
    assert all(outcomes.values()),outcomes
    outcomes['source_changes']=[x['source'] for x in review['provenance'] if file_hash(Path(x['source']))!=x['sha256']]
    write_artifact(root/'validation.json',outcomes);print(json.dumps(outcomes))
finally:server.shutdown();server.server_close();t.join()
