"""Explicit isolated browser producer -> JOENESS consumer integration exercise."""
import argparse
import copy
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
import os
from pathlib import Path
import subprocess
import sys
import threading

REPO = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(REPO/'tests'),str(REPO/'skills/joedesign/scripts')]
from test_design_conformance import baseline_fixture, BAD_HTML, GOOD_HTML
from harness.conformance import bindings
from harness.io import file_hash, write_artifact, read_artifact

parser=argparse.ArgumentParser()
parser.add_argument('--consumer',type=Path,required=True)
parser.add_argument('--output',type=Path,required=True)
args=parser.parse_args()
root=args.output.resolve();root.mkdir(parents=True,exist_ok=False)
project=root/'project';project.mkdir()
artifacts=root/'artifacts';artifacts.mkdir()
(project/'index.html').write_text(BAD_HTML)
baseline=baseline_fixture(project)
baseline_path=project/'baseline.json';write_artifact(baseline_path,baseline)
baseline_bytes=baseline_path.read_bytes();pin=file_hash(baseline_path)
results={}

class Quiet(SimpleHTTPRequestHandler):
    def log_message(self,*args):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(project)))
thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()

def producer(name,html,expected):
    (project/'index.html').write_text(html)
    request=dict(output_dir=str(artifacts/name),targets=baseline['targets'],build_id=name,
        browser=dict(base_url=f'http://127.0.0.1:{server.server_port}',
            playwright_module=os.environ['JOEDESIGN_PLAYWRIGHT_MODULE'],executable=os.environ['JOEDESIGN_BROWSER_EXECUTABLE'],
            probes={'wide':dict(assertions=[dict(selector='#page',visible=True)])}),
        design=dict(baseline_sha256=pin,input_fingerprints=bindings(baseline,project,['wide']),checks=baseline['required_checks']))
    capture=subprocess.run(['node',str(REPO/'skills/joedesign/scripts/capture.mjs')],input=json.dumps(request),capture_output=True,text=True,encoding='utf-8',timeout=60)
    assert capture.returncode==0,capture.stderr
    raw=json.loads(capture.stdout);assert not raw['errors'],raw
    observation=next(c['path'] for c in raw['captures'] if c['kind']=='technical')
    receipt=artifacts/(name+'-receipt.json')
    argv=[sys.executable,str(REPO/'skills/joedesign/scripts/harness_cli.py'),'verify-design',
          '--project',str(project),'--baseline',str(baseline_path),'--baseline-sha256',pin,
          '--observation',observation,'--output',str(receipt)]
    checked=subprocess.run(argv,capture_output=True,text=True,encoding='utf-8')
    assert checked.returncode==expected,checked.stderr+checked.stdout
    results['producer-'+name]={'exit_code':checked.returncode,'receipt':str(receipt),'result':json.loads(checked.stdout)}
    return receipt

def consume(name,receipt,expected,claim='visual'):
    argv=['node',str(args.consumer),'--root',str(project),'--baseline','baseline.json',
          '--baseline-sha256',pin,'--evidence-root',str(artifacts),'--claim',claim]
    if receipt:argv+=['--result',str(receipt)]
    p=subprocess.run(argv,capture_output=True,text=True,encoding='utf-8')
    result=json.loads(p.stdout)
    results[name]={'exit_code':p.returncode,'result':result,'command':argv}
    assert p.returncode==expected,(name,p.returncode,p.stdout,p.stderr)

try:
    bad=producer('stacked',BAD_HTML,2);consume('stacked-gap-blocked',bad,2)
    good=producer('corrected',GOOD_HTML,0);consume('corrected-visual-pass',good,0)
    consume('visual-is-not-user-acceptance',good,2,'complete')
    consume('missing-result-blocked',None,2)
    receipt=read_artifact(good)
    altered=copy.deepcopy(receipt);altered['results'].pop()
    partial_path=artifacts/'partial.json';write_artifact(partial_path,altered)
    consume('one-check-missing-blocked',partial_path,2)
    broken=artifacts/'broken.json';broken.write_text('{broken')
    consume('corrupt-result-blocked',broken,2)
    (project/'index.html').write_text(BAD_HTML)
    consume('old-output-blocked',good,2)
    (project/'index.html').write_text(GOOD_HTML)
    changed=copy.deepcopy(baseline);changed['required_checks'][0]['criterion']['max']=500
    write_artifact(baseline_path,changed,overwrite=True)
    consume('relaxed-baseline-blocked',good,2)
    baseline_path.write_bytes(baseline_bytes)
    evidence=Path(receipt['results'][0]['evidence'][0]['path']);saved=evidence.read_bytes()
    evidence.write_text('{tampered')
    consume('changed-evidence-blocked',good,2)
    evidence.write_bytes(saved)
    (project/'unrelated.txt').write_text('Independent scope work')
    consume('unrelated-work-keeps-valid-proof',good,0)
    consume('normal-recovery',good,0)
finally:
    server.shutdown();server.server_close();thread.join()
    write_artifact(root/'results.json',{'consumer':str(args.consumer.resolve()),'consumer_sha256':file_hash(args.consumer),
        'project':str(project),'baseline':str(baseline_path),'baseline_sha256':pin,'scenarios':results})
print(json.dumps({'scenario_count':len(results),'results':str(root/'results.json'),'baseline_sha256':pin,'receipt':str(good)},indent=2))
