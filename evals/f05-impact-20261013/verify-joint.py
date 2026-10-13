"""Independent real producer -> explicit reuse consumer linkage, no new render."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys

REPO=Path(__file__).resolve().parents[2]
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def inventory(root):return {str(p):sha(p) for p in root.rglob('*') if p.is_file()}
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--producer',type=Path,required=True)
    ap.add_argument('--gate',type=Path,required=True);ap.add_argument('--owner-run',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
    out=a.output.resolve();out.mkdir(parents=True,exist_ok=False)
    owner=json.loads(a.owner_run.read_text(encoding='utf-8'))
    fixtures=REPO/'.local/f05-impact-20261013/real-v1';before=inventory(fixtures)
    results=[];codepins={str(p.resolve()):sha(p) for p in [a.producer,a.gate,a.gate.with_name('impact-review.mjs')]}
    for case in ['P01','P02']:
        row=next(r for r in owner['results'] if r['case']==case+'-reviewed-visual')
        command=row['command'];original_review=Path(command[command.index('--impact-review')+1])
        root=fixtures/case;dest=out/case;dest.mkdir()
        producer=[sys.executable,'-B',str(a.producer.resolve()),'inspect-impact','--project',str(root),
            '--request',str(root/'request.json'),'--request-sha256',sha(root/'request.json'),'--review-sha256',sha(root/'review.json')]
        run=subprocess.run(producer,capture_output=True,text=True,encoding='utf-8',timeout=60)
        assert run.returncode==0,run.stderr+run.stdout
        impact=dest/'impact.json';impact.write_text(run.stdout,encoding='utf-8',newline='\n')
        review=json.loads(original_review.read_text(encoding='utf-8'));review['impact_sha256']=sha(impact)
        review['review_context']='joedesign-joint-review-of-manager-reviewed-transition'
        review['rationale']+=' Independently matched the isolated producer output and immutable fixture definitions against the Manager scoped review; no new observation or acceptance.'
        reviewed=dest/'consumer-review.json';reviewed.write_text(json.dumps(review,indent=2)+'\n',encoding='utf-8')
        base=['node',str(a.gate.resolve()),'--root',str(root),'--baseline','new.json','--baseline-sha256',sha(root/'new.json'),
            '--previous-baseline','old.json','--previous-baseline-sha256',sha(root/'old.json'),'--result','old-result.json','--claim','visual']
        extras=['--evidence-root',str(out),'--evidence-root',str(fixtures),'--evidence-root','D:/JOEWRKS/JOEQASAM/evidence/t035-joe-implementation',
            '--impact',str(impact),'--impact-sha256',sha(impact),'--impact-review',str(reviewed),'--impact-review-sha256',sha(reviewed),
            '--old-result','old-result.json','--old-result-sha256',sha(root/'old-result.json')]
        def execute(name,cmd,allowed):
            r=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',timeout=60);data=json.loads(r.stdout)
            assert r.returncode==(0 if allowed else 2) and data['allowed'] is allowed,(name,data,r.stderr)
            assert data['project_complete'] is False and data.get('lanes',{}).get('user_acceptance','NOT_GRANTED')!='ACCEPTED'
            if allowed:assert data['impact_reuse']['reused_check_ids']==['c0','c1','c2','c3']
            results.append(dict(case=case+'-'+name,command=cmd,exit=r.returncode,output=data,passed=True))
        execute('no-transition',base,False)
        execute('reviewed-visual',base+extras,True)
        complete=base+extras;complete[complete.index('--claim')+1]='complete';execute('no-acceptance',complete,False)
        missing=base+extras;start=missing.index('--impact-review-sha256');del missing[start:start+2];execute('missing-review-pin',missing,False)
        tampered=base+extras;tampered[tampered.index('--impact-sha256')+1]='0'*64;execute('tampered-impact-pin',tampered,False)
        negative=dest/'changed-runtime';shutil.copytree(root,negative)
        with (negative/'index.html').open('a',encoding='utf-8') as f:f.write('<!-- CSS/runtime bytes changed -->')
        changed=base+extras;changed[changed.index('--root')+1]=str(negative);execute('changed-runtime',changed,False)
        results.append(dict(case=case+'-producer',command=producer,exit=run.returncode,impact_sha256=sha(impact),
            review_sha256=sha(reviewed),counts=json.loads(run.stdout)['counts'],passed=True))
    assert inventory(fixtures)==before and all(sha(p)==h for p,h in codepins.items())
    report=dict(results=results,passed=len(results),total=len(results),source_pins=codepins,fixtures_unchanged=before,
        new_renders=0,new_geometry_measurements=0,new_screenshots=0,
        limits=['Local explicit pins and scoped review only, no authenticated acceptance','Only geometry of static P01/P02 fixtures; no general CSS/dynamic precision','Current served observation and human review costs remain'])
    (out/'summary.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(dict(passed=len(results),total=len(results),summary=str(out/'summary.json'))))

if __name__=='__main__':main()
