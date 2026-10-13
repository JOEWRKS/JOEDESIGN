"""Create immutable real-browser F05 P01/P02 fixtures in a NEW directory."""
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

REPO=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(REPO/'tests'))
from harness_support import SCRIPTS
from harness.conformance import bindings,evaluate
from harness.io import digest,file_hash,write_artifact
from test_design_conformance import baseline_fixture,GOOD_HTML

class Quiet(SimpleHTTPRequestHandler):
    def log_message(self,*args):pass

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();out=args.output.resolve();out.mkdir(parents=True,exist_ok=False)
    summary=[]
    for case,suffix,kind in [('P01','\n<!-- Editorial note: fixture review record only. -->\n','COMMENT_APPEND'),
                             ('P02','\n## Print-only future export\nThis note concerns a future print export, outside the existing web screen. Existing screen rules, defaults and exceptions remain unchanged.\n','UNRELATED_SECTION_APPEND')]:
        root=out/case;root.mkdir()
        def put(name,data):write_artifact(root/name,data)
        def ref(name):return dict(path=name,sha256=file_hash(root/name))
        (root/'index.html').write_text(GOOD_HTML,encoding='utf-8')
        old=baseline_fixture(root);put('old.json',old)
        (root/'authority-before.md').write_bytes((root/'DESIGN.md').read_bytes())
        server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(root)))
        thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
        base=f'http://127.0.0.1:{server.server_port}'
        try:
            capture=dict(output_dir=str(root/'old-capture'),targets=old['targets'],build_id='f05-static-v1',
                browser=dict(base_url=base,playwright_module=os.environ['JOEDESIGN_PLAYWRIGHT_MODULE'],
                    executable=os.environ['JOEDESIGN_BROWSER_EXECUTABLE'],
                    probes={'wide':dict(assertions=[dict(selector='#page',visible=True)])}),
                design=dict(baseline_sha256=ref('old.json')['sha256'],input_fingerprints=bindings(old,root,['wide']),checks=old['required_checks']))
            run=subprocess.run(['node',str(SCRIPTS/'capture.mjs')],input=json.dumps(capture),capture_output=True,text=True,encoding='utf-8',timeout=90)
            put('capture-process.json',dict(exit=run.returncode,stderr=run.stderr))
            if run.returncode:raise RuntimeError(run.stderr)
            manifest=json.loads(run.stdout);put('capture-manifest.json',manifest)
            if manifest['errors']:raise RuntimeError(manifest['errors'])
            logs=[c['path'] for c in manifest['captures'] if c['kind']=='technical']
            receipt=evaluate(old,ref('old.json')['sha256'],root,logs)
            put('old-result.json',receipt)
            if not receipt['eligible']:raise RuntimeError(receipt)
            protected={str(p):file_hash(p) for p in root.rglob('*') if p.is_file()}
            (root/'DESIGN.md').write_bytes((root/'authority-before.md').read_bytes()+suffix.encode())
            new=copy.deepcopy(old);new['authority'][0]['sha256']=file_hash(root/'DESIGN.md');put('new.json',new)
            served_request=dict(project=str(root),base_url=base,baseline=new,baseline_sha256=ref('new.json')['sha256'],build_id='f05-static-v1')
            run=subprocess.run(['node',str(Path(__file__).with_name('collect-served.mjs'))],input=json.dumps(served_request),capture_output=True,text=True,encoding='utf-8',timeout=60)
            put('served-process.json',dict(exit=run.returncode,stderr=run.stderr))
            if run.returncode:raise RuntimeError(run.stderr)
            put('served.json',json.loads(run.stdout))
            request=dict(schema='joedesign.impact-request.v1',old_baseline=ref('old.json'),new_baseline=ref('new.json'),old_result=ref('old-result.json'),
                served=ref('served.json'),authority_before=[dict(path='DESIGN.md',snapshot=ref('authority-before.md'))])
            review=dict(schema='joedesign.impact-review.v1',scope_id=old['scope_id'],transition_sha256=digest(request),
                implementation_context='f05-fixture-builder',review_context='candidate-for-manager-source-review',
                scope_analysis='CANDIDATE REVIEW FOR INDEPENDENT INSPECTION: appended text explicitly excludes the existing web screen; the original authority prefix and full baseline definitions are unchanged. All four existing spacing checks remain required. This local draft is not authenticated independent approval.',
                authority_analysis=[dict(path='DESIGN.md',kind=kind,rationale='Append-only fixture text; existing screen spacing and defaults unchanged.')],
                checks=[dict(check_id=c['check_id'],verdict='UNAFFECTED',rationale='This check still covers the same web spacing rule; appended editorial/print-only material introduces no web default or exception.',
                    source_refs=[ref('DESIGN.md'),ref('authority-before.md'),ref('index.html')],blocking_findings=[]) for c in old['required_checks']])
            put('review.json',review);request['review']=ref('review.json');put('request.json',request)
            command=[sys.executable,'-B',str(SCRIPTS/'harness_cli.py'),'inspect-impact','--project',str(root),'--request',str(root/'request.json'),
                '--request-sha256',ref('request.json')['sha256'],'--review-sha256',ref('review.json')['sha256'],'--output',str(root/'impact.json')]
            run=subprocess.run(command,capture_output=True,text=True,encoding='utf-8',timeout=60)
            put('diagnostic-process.json',dict(command=command,exit=run.returncode,stderr=run.stderr))
            if run.returncode:raise RuntimeError(run.stderr+run.stdout)
            immutable={p:h for p,h in protected.items() if Path(p).name!='DESIGN.md'}
            assert all(file_hash(Path(p))==h for p,h in immutable.items())
            impact=json.loads(run.stdout)
            summary.append(dict(case=case,project=str(root),pins={n:ref(n)['sha256'] for n in ['old.json','new.json','old-result.json','served.json','review.json','request.json','impact.json']},
                counts=impact['counts'],old_geometry_checks=4,new_geometry_checks=0,new_screenshots=0,old_inputs_unchanged=immutable,
                independent_review='PENDING Manager inspection; draft semantic review only',reuse_authorized=False))
        finally:
            server.shutdown();server.server_close();thread.join()
    write_artifact(out/'summary.json',summary)
    print(json.dumps(summary,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
