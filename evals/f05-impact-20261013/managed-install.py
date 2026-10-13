"""Pinned F05 installation plan/apply/rollback. Apply requires Manager entry notice."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import tempfile

REPO=Path(__file__).resolve().parents[2]
TARGET=Path('C:/Users/tjdwo/.codex/skills/joedesign').resolve()
SOURCE=(REPO/'.local/f05-impact-20261013/isolated-r2/package/joedesign').resolve()
BACKUP=(REPO/'.local/f05-impact-20261013/managed-backup-r2').resolve()

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def inventory(root):
    result={}
    for p in sorted(root.rglob('*')):
        if p.is_symlink():raise ValueError('Symlinks are not supported in this exact package transition')
        if p.is_file():result[p.relative_to(root).as_posix()]=sha(p)
    return result
def write_new(p,data):
    with p.open('x',encoding='utf-8',newline='\n') as f:json.dump(data,f,indent=2);f.write('\n')
def destination(root,name):
    p=(root/name).resolve()
    if not p.is_relative_to(root) or p==root:raise ValueError('Path outside named package')
    return p
def atomic_copy(src,dest):
    dest.parent.mkdir(parents=True,exist_ok=True)
    fd,temp=tempfile.mkstemp(prefix='.f05-',dir=dest.parent)
    try:
        with os.fdopen(fd,'wb') as f:f.write(src.read_bytes())
        os.replace(temp,dest)
    finally:
        if os.path.exists(temp):os.unlink(temp)

def main():
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['plan','apply','rollback'])
    p.add_argument('--plan',type=Path,required=True);p.add_argument('--plan-sha256')
    p.add_argument('--receipt',type=Path)
    args=p.parse_args()
    if args.mode=='plan':
        before=inventory(TARGET);package_after=inventory(SOURCE)
        extra=set(before)-set(package_after)
        preserved={n:before[n] for n in extra if '__pycache__' in Path(n).parts and n.endswith('.pyc')}
        after={**package_after,**preserved}
        deleted=sorted(set(before)-set(after))
        if deleted:raise ValueError('Unexpected installed files; no deletion permitted: '+repr(deleted))
        plan=dict(schema='joedesign.managed-install-plan.v1',target=str(TARGET),source=str(SOURCE),backup=str(BACKUP),
            before=before,after=after,source_files=package_after,preserved_generated_files=preserved,
            replace=sorted(n for n in before if before[n]!=after[n]),
            create=sorted(set(after)-set(before)),delete=[],script_sha256=sha(__file__),
            entry='Pending Manager notification after joint gate validation; plan creation is not permission to apply',
            rollback='Verify backup and every current byte is either its before or after value. Restore replacements only; unlink only the exact two newly created files with matching after hashes. Refuse unexpected drift.')
        assert len(before)-len(preserved)==28 and len(package_after)==30
        write_new(args.plan,plan);print(json.dumps(dict(plan=str(args.plan.resolve()),sha256=sha(args.plan),replace=plan['replace'],create=plan['create'],delete=[])));return
    if not args.plan_sha256 or sha(args.plan)!=args.plan_sha256:raise ValueError('Plan pin mismatch')
    plan=json.loads(args.plan.read_text(encoding='utf-8'))
    assert plan['target']==str(TARGET) and plan['source']==str(SOURCE) and plan['backup']==str(BACKUP)
    assert plan['script_sha256']==sha(__file__) and plan['delete']==[]
    if not args.receipt or args.receipt.exists():raise ValueError('A new external receipt path is required')
    if args.receipt.resolve().is_relative_to(TARGET):raise ValueError('Receipt must stay outside installed package')
    if args.mode=='apply':
        if inventory(TARGET)!=plan['before']:raise ValueError('Installed package drift; stop before mutation')
        if inventory(SOURCE)!=plan['source_files']:raise ValueError('Reviewed isolated package drift')
        BACKUP.mkdir(parents=True,exist_ok=False)
        for name in plan['before']:
            dest=destination(BACKUP,name);dest.parent.mkdir(parents=True,exist_ok=True)
            shutil.copyfile(destination(TARGET,name),dest)
        if inventory(BACKUP)!=plan['before'] or inventory(TARGET)!=plan['before']:raise ValueError('Backup mismatch or concurrent drift; no installation started')
        for name in plan['replace']+plan['create']:
            dest=destination(TARGET,name)
            if name in plan['before']:
                if not dest.is_file() or sha(dest)!=plan['before'][name]:raise ValueError('Concurrent target drift; use pinned rollback')
            elif dest.exists():raise ValueError('Unexpected new target; use pinned rollback')
            src=destination(SOURCE,name)
            if sha(src)!=plan['after'][name]:raise ValueError('Concurrent source drift; use pinned rollback')
            atomic_copy(src,dest)
        if inventory(TARGET)!=plan['after']:raise ValueError('Final mismatch; use pinned rollback')
    else:
        if inventory(BACKUP)!=plan['before']:raise ValueError('Backup bytes changed; no rollback')
        current=inventory(TARGET)
        if set(current)-set(plan['after']):raise ValueError('Unexpected new installed file; no rollback')
        for name in plan['before']:
            if current.get(name) not in (plan['before'][name],plan['after'][name]):raise ValueError('Unexpected installed drift; no rollback')
        for name in plan['create']:
            if name in current and current[name]!=plan['after'][name]:raise ValueError('New file changed; do not remove')
        for name in plan['replace']:atomic_copy(destination(BACKUP,name),destination(TARGET,name))
        for name in plan['create']:
            dest=destination(TARGET,name)
            if dest.exists():
                if sha(dest)!=plan['after'][name]:raise ValueError('Concurrent new-file drift; do not remove')
                dest.unlink()  # Exact pinned file only, never recursive directory removal.
        if inventory(TARGET)!=plan['before']:raise ValueError('Restoration mismatch')
    write_new(args.receipt,dict(mode=args.mode,plan_sha256=args.plan_sha256,installed=inventory(TARGET),backup=inventory(BACKUP)))
    print(json.dumps(dict(mode=args.mode,verified=True,receipt=str(args.receipt.resolve()))))

if __name__=='__main__':main()
