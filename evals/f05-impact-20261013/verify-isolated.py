"""Exact package copy and CLI runtime checks; never installs a discoverable skill."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys

REPO=Path(__file__).resolve().parents[2]
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def inventory(root):return {p.relative_to(root).as_posix():sha(p) for p in sorted(root.rglob('*'))
                           if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc'}
def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True)
    p.add_argument('--fixtures',type=Path,required=True);p.add_argument('--gate',type=Path,required=True)
    args=p.parse_args();out=args.output.resolve();out.mkdir(parents=True,exist_ok=False)
    source=REPO/'skills/joedesign';package=out/'package/joedesign';package.mkdir(parents=True)
    original=inventory(source)
    installed=Path('C:/Users/tjdwo/.codex/skills/joedesign');installed_before=inventory(installed)
    for name in original:
        dest=package/name;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(source/name,dest)
    assert inventory(package)==original
    fixture_root=args.fixtures.resolve();frozen=inventory(fixture_root)
    records=[];gate_sha=sha(args.gate)
    for case in ['P01','P02']:
        root=fixture_root/case
        command=[sys.executable,'-B',str(package/'scripts/harness_cli.py'),'inspect-impact','--project',str(root),
            '--request',str(root/'request.json'),'--request-sha256',sha(root/'request.json'),
            '--review-sha256',sha(root/'review.json')]
        result=subprocess.run(command,capture_output=True,text=True,encoding='utf-8',timeout=60)
        data=json.loads(result.stdout)
        assert result.returncode==0 and data['counts']=={'reusable-candidate':4,'rerun':0,'unknown':0}
        assert data['reuse_authorized'] is False and data['acceptance']=='NOT_GRANTED'
        (out/(case+'-impact.json')).write_text(result.stdout,encoding='utf-8',newline='\n')
        records.append(dict(case=case,command=command,exit=result.returncode,stderr=result.stderr,counts=data['counts']))
        gate=['node',str(args.gate.resolve()),'--root',str(root),'--baseline','new.json','--baseline-sha256',sha(root/'new.json'),
            '--previous-baseline','old.json','--previous-baseline-sha256',sha(root/'old.json'),
            '--result','old-result.json','--claim','visual']
        run=subprocess.run(gate,capture_output=True,text=True,encoding='utf-8',timeout=60)
        consumed=json.loads(run.stdout)
        assert run.returncode==2 and consumed['allowed'] is False and all(c['status']=='STALE' for c in consumed['checks'])
        (out/(case+'-existing-gate.json')).write_text(run.stdout,encoding='utf-8',newline='\n')
        records.append(dict(case=case,command=gate,exit=run.returncode,stderr=run.stderr,allowed=False,checks='STALE'))
    assert sha(args.gate)==gate_sha
    assert inventory(source)==inventory(package)==original
    assert inventory(installed)==installed_before and inventory(fixture_root)==frozen
    summary=dict(source=str(source),package=str(package),source_files=original,package_files=len(original),
        existing_gate=dict(path=str(args.gate.resolve()),sha256=gate_sha),commands=records,
        installed_unchanged=installed_before,fixtures_unchanged=frozen,
        limitations=['Semantic review draft inspected separately by Manager; no authenticated reviewer identity',
                    'Existing gate remains stale without explicit reviewed transition',
                    'No personal installation; no new observation; no visual acceptance'])
    (out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(dict(package=str(package),files=len(original),checks=len(records),summary=str(out/'summary.json'))))

if __name__=='__main__':main()
