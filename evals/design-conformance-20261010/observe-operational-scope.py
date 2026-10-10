"""Observe a live project read-only using an independently pinned baseline.

Output is outside the product or in its explicit conformance evidence directory.
Does not mutate source, baseline or ledgers.
"""
import argparse,json,os,subprocess,sys,threading
from functools import partial
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
parser=argparse.ArgumentParser()
for name in ('project','baseline','output','package'):parser.add_argument('--'+name,type=Path,required=True)
parser.add_argument('--baseline-sha256',required=True)
a=parser.parse_args()
project=a.project.resolve();out=a.output.resolve()
if out.is_relative_to(project) and not out.is_relative_to(project/'.design-harness/conformance/evidence'):
    raise ValueError('Product output allowed only under .design-harness/conformance/evidence')
out.mkdir(parents=True,exist_ok=False)
sys.path.insert(0,str(a.package/'scripts'))
from harness.conformance import bindings,load_baseline
from harness.io import file_hash,write_artifact
b=load_baseline(a.baseline,a.baseline_sha256,project)
before=bindings(b,project,[t['id'] for t in b['targets']])
prefix='examples/geo-fresh-market/wireframes/'
class Quiet(SimpleHTTPRequestHandler):
    extensions_map={**SimpleHTTPRequestHandler.extensions_map,'.mjs':'text/javascript'}
    def log_message(self,*args):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(project/prefix)))
thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
browser=dict(base_url=f'http://127.0.0.1:{server.server_port}',playwright_module=os.environ['JOEDESIGN_PLAYWRIGHT_MODULE'],executable=os.environ['JOEDESIGN_BROWSER_EXECUTABLE'])
def run(script,request):
    p=subprocess.run(['node',str(script)],input=json.dumps(request),capture_output=True,text=True,encoding='utf-8',timeout=180)
    assert p.returncode==0,p.stderr
    return json.loads(p.stdout)
try:
    deps=run(Path(__file__).with_name('audit-runtime.mjs'),dict(**browser,project=str(project),prefix=prefix,targets=b['targets'],checks=b['required_checks']))
    write_artifact(out/'dependencies.json',deps)
    assert all(r['valid'] for r in deps),'Uncovered/mismatched browser dependency; inspect dependencies.json'
    browser['probes']={t['id']:dict(assertions=[dict(selector='#main',visible=True),dict(selector='.product-card' if t['surface']=='products' else '.campaign-copy',count=9 if t['surface']=='products' else 2)]) for t in b['targets']}
    raw=run(a.package/'scripts/capture.mjs',dict(output_dir=str(out/'capture'),targets=b['targets'],build_id=a.baseline_sha256,browser=browser,
          design=dict(baseline_sha256=a.baseline_sha256,input_fingerprints=before,checks=b['required_checks'])))
    write_artifact(out/'capture.json',raw);assert not raw['errors'],raw['errors']
    after=bindings(b,project,[t['id'] for t in b['targets']])
    command=[sys.executable,'-B',str(a.package/'scripts/harness_cli.py'),'verify-design','--project',str(project),
             '--baseline',str(a.baseline),'--baseline-sha256',a.baseline_sha256,'--output',str(out/'receipt.json')]
    for c in raw['captures']:
        if c['kind']=='technical':command+=['--observation',c['path']]
    p=subprocess.run(command,capture_output=True,text=True,encoding='utf-8')
    write_artifact(out/'execution.json',dict(exit_code=p.returncode,input_changes=[k for k in before if before[k]!=after[k]],
          package=str(a.package),core_sha256=file_hash(a.package/'SKILL.md'),baseline_sha256=a.baseline_sha256,
          stdout=p.stdout,stderr=p.stderr,project=str(project)))
    print(json.dumps(dict(exit_code=p.returncode,input_changes=before!=after,output=str(out))))
    sys.exit(p.returncode if before==after else 2)
finally:server.shutdown();server.server_close();thread.join()
