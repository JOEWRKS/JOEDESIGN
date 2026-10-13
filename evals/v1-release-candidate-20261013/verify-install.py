"""Execute the README copy block in isolated Codex homes; no personal changes."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

REPO=Path(__file__).resolve().parents[2]
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def inventory(root):return {p.relative_to(root).as_posix():sha(p) for p in sorted(root.rglob('*')) if p.is_file()}
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--ps7',required=True);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
    out=a.output.resolve();out.mkdir(parents=True,exist_ok=False)
    temp=Path(tempfile.mkdtemp(prefix='joedesign-v1-install-'));distribution=temp/'distribution'
    source=REPO/'skills/joedesign';source_names=subprocess.check_output(['git','ls-files','skills/joedesign'],cwd=REPO,text=True).splitlines()
    for name in source_names:
        dest=distribution/name;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(REPO/name,dest)
    expected=inventory(distribution/'skills/joedesign');assert len(expected)==30
    readme=(REPO/'README.md').read_text(encoding='utf-8')
    block=re.findall(r'```powershell\n(.*?)\n```',readme,re.S)[1]
    script=temp/'readme-install.ps1';script.write_text(block+'\n',encoding='utf-8-sig')
    shells={'ps5':'C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe','ps7':a.ps7}
    results=[];installed=[]
    for shell_name,shell in shells.items():
        for mode in ['fresh','existing-core','legacy-harness','default-home']:
            case=shell_name+'-'+mode;home=temp/case/'codex';home.mkdir(parents=True)
            if mode=='existing-core':
                p=home/'skills/joedesign/user-note.txt';p.parent.mkdir(parents=True);p.write_text('Preserve existing install')
            if mode=='legacy-harness':
                p=home/'skills/joedesign-harness/SKILL.md';p.parent.mkdir(parents=True);p.write_text('Legacy placeholder for collision guard, not specialist evidence')
            env=os.environ.copy();env['CODEX_HOME']=str(home)
            if mode=='default-home':
                env.pop('CODEX_HOME',None);env['USERPROFILE']=str(temp/case/'profile');home=Path(env['USERPROFILE'])/'.codex'
            before=inventory(home)
            run=subprocess.run([shell,'-NoProfile','-ExecutionPolicy','Bypass','-File',str(script)],cwd=distribution,env=env,capture_output=True,timeout=60)
            (out/(case+'-stdout.txt')).write_bytes(run.stdout);(out/(case+'-stderr.txt')).write_bytes(run.stderr)
            if mode in ['existing-core','legacy-harness']:
                assert run.returncode!=0 and inventory(home)==before,(case,run.stdout,run.stderr)
                results.append(dict(case=case,exit=run.returncode,refused_without_mutation=True));continue
            assert run.returncode in (0,2),(case,run.stdout,run.stderr)
            package=home/'skills/joedesign';assert inventory(package)==expected,case
            version=subprocess.run([sys.executable,'-B',str(package/'scripts/harness_cli.py'),'version'],capture_output=True,text=True,encoding='utf-8',check=True)
            value=json.loads(version.stdout);assert value['version']=='1.0.0' and Path(value['operating_core'])==package/'SKILL.md'
            empty=temp/case/'no-specialists';empty.mkdir()
            doctor=subprocess.run([sys.executable,'-B',str(package/'scripts/harness_cli.py'),'doctor','--skills-root',str(empty)],capture_output=True,text=True,encoding='utf-8')
            data=json.loads(doctor.stdout);assert doctor.returncode==2 and data['ready_for_synthesis'] is False
            assert all(data['dependencies'][n]['status']=='UNAVAILABLE' for n in ['impeccable','ui-ux-pro-max','web-design-guidelines'])
            assert inventory(package)==expected
            results.append(dict(case=case,exit=run.returncode,package=str(package),version=value,exact_files=30,missing_specialists_blocked=True))
            installed.append(str(package))
    links=[]
    for name in ['README.md','docs/INSTALL.md','docs/VALIDATION.md']:
        p=REPO/name
        for link in re.findall(r'\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
            if '://' in link:continue
            target=(p.parent/link.split('#')[0]).resolve();assert target.is_file(),(name,link)
            links.append(dict(source=name,link=link))
    version_changes=[]
    for name in source_names:
        original=subprocess.check_output(['git','show','1d9502e:'+name],cwd=REPO)
        if original!=(REPO/name).read_bytes():version_changes.append(name)
    assert sorted(version_changes)==['skills/joedesign/VERSION','skills/joedesign/agents/openai.yaml']
    protected=json.loads((REPO/'.local/v1-release-candidate-20261013/protected-before.json').read_text(encoding='utf-8'))
    assert all(inventory(Path(root))==saved for root,saved in protected['directories'].items())
    assert all(sha(p)==h for p,h in protected['configs'].items())
    result=dict(isolation=str(temp),distribution=str(distribution),installed_packages=installed,results=results,
        readme_block_sha256=hashlib.sha256(block.encode()).hexdigest(),package_files=expected,package_changes=version_changes,
        links_checked=links,protected_unchanged=True,python=sys.version,node=subprocess.check_output(['node','--version'],text=True).strip())
    (out/'summary.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps(dict(cases=len(results),all_passed=True,installed_packages=installed,summary=str(out/'summary.json'))))

if __name__=='__main__':main()
