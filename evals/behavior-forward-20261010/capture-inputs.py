import hashlib,json,os,shutil,subprocess,threading
from pathlib import Path
from functools import partial
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
repo=Path(__file__).resolve().parents[2];root=repo/'.local/behavior-forward-20261010'
class Quiet(SimpleHTTPRequestHandler):
    def log_message(self,*args):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(root/'reference')))
t=threading.Thread(target=server.serve_forever,daemon=True);t.start()
try:
    targets=[dict(id=name,route='/approved.html',surface='reference',family='overview',viewport=[width,900],state='fresh',theme='light',locale='en',required_kinds=['render']) for name,width in [('wide',1240),('narrow',390)]]
    request=dict(output_dir=str(root/'reference/capture'),targets=targets,build_id='fixture-original',browser=dict(base_url=f'http://127.0.0.1:{server.server_port}',playwright_module=os.environ['JOEDESIGN_PLAYWRIGHT_MODULE'],executable=os.environ['JOEDESIGN_BROWSER_EXECUTABLE'],probes={t['id']:dict(assertions=[dict(selector='main',visible=True),dict(selector='.row',count=3)]) for t in targets}))
    p=subprocess.run(['node',str(root/'package/joedesign/scripts/capture.mjs')],input=json.dumps(request),capture_output=True,text=True,encoding='utf-8',timeout=90)
    assert p.returncode==0,p.stderr
    output=json.loads(p.stdout);assert not output['errors'],output
    for c in output['captures']:
        if c['kind']=='render':
            for case in ('new','extension','repair'):shutil.copyfile(c['path'],root/'cases'/case/'reference'/(c['target_id']+'.png'))
    (root/'reference/capture-result.json').write_text(json.dumps(output,indent=2),encoding='utf-8')
finally:server.shutdown();server.server_close();t.join()
manifest={str(p.relative_to(root)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in root.rglob('*') if p.is_file()}
(root/'frozen-input-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
(repo/'evals/behavior-forward-20261010/freeze.json').write_text(json.dumps({'protocol_sha256':hashlib.sha256((repo/'evals/behavior-forward-20261010/PROTOCOL.md').read_bytes()).hexdigest(),'input_manifest_sha256':hashlib.sha256((root/'frozen-input-manifest.json').read_bytes()).hexdigest(),'root':str(root),'candidate_execution_started':False},indent=2)+'\n',encoding='utf-8')
print('Frozen source, package and two original viewports; no candidate executed.')
