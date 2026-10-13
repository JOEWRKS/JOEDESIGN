"""Exercise installation recovery only in temporary package directories."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile

spec=importlib.util.spec_from_file_location('managed',Path(__file__).with_name('managed-install.py'))
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
results=[]
for case in ['apply-rollback','target-drift','source-drift','backup-drift','new-file-drift','unexpected-file']:
    with tempfile.TemporaryDirectory(prefix='f05-managed-test-') as temp:
        root=Path(temp);m.TARGET=root/'installed';m.SOURCE=root/'source';m.BACKUP=root/'backup'
        m.TARGET.mkdir();m.SOURCE.mkdir()
        for i in range(28):
            (m.TARGET/f'f{i}.txt').write_text('old '+str(i))
            (m.SOURCE/f'f{i}.txt').write_text(('changed ' if i<2 else 'old ')+str(i))
        (m.TARGET/'__pycache__').mkdir();(m.TARGET/'__pycache__/old.pyc').write_bytes(b'preserve generated cache')
        for i in [28,29]:(m.SOURCE/f'f{i}.txt').write_text('new '+str(i))
        plan=root/'plan.json';receipt=root/'apply.json'
        def call(mode,expected=None):
            sys.argv=[str(Path(m.__file__)),mode,'--plan',str(plan)]
            if mode!='plan':sys.argv+=['--plan-sha256',m.sha(plan),'--receipt',str(receipt if mode=='apply' else root/'rollback.json')]
            try:
                with contextlib.redirect_stdout(io.StringIO()):m.main()
            except ValueError as error:
                if expected and expected in str(error):return
                raise
            if expected:raise AssertionError('Expected failure: '+expected)
        call('plan');original=m.inventory(m.TARGET)
        if case=='target-drift':
            (m.TARGET/'f0.txt').write_text('outside change');call('apply','Installed package drift')
            assert not m.BACKUP.exists()
        elif case=='source-drift':
            (m.SOURCE/'f0.txt').write_text('outside change');call('apply','Reviewed isolated package drift')
            assert m.inventory(m.TARGET)==original and not m.BACKUP.exists()
        else:
            call('apply');assert m.inventory(m.BACKUP)==original
            if case=='apply-rollback':call('rollback');assert m.inventory(m.TARGET)==original
            elif case=='backup-drift':
                (m.BACKUP/'f0.txt').write_text('corrupt');now=m.inventory(m.TARGET)
                call('rollback','Backup bytes changed');assert m.inventory(m.TARGET)==now
            elif case=='new-file-drift':
                (m.TARGET/'f28.txt').write_text('user edited');now=m.inventory(m.TARGET)
                call('rollback','New file changed');assert m.inventory(m.TARGET)==now
            else:
                (m.TARGET/'unexpected.txt').write_text('preserve');now=m.inventory(m.TARGET)
                call('rollback','Unexpected new installed file');assert m.inventory(m.TARGET)==now
        results.append(dict(case=case,passed=True,scope='Temporary directories only'))
print(json.dumps(results,indent=2))
