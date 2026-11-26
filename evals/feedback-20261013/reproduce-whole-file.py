"""Read-only GEO input snapshot; mutate temporary copies only, no browser or repin.

Diagnoses current whole-file invalidation; does not implement selective reuse.
"""
import hashlib
import json
import shutil
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
GEO = Path('D:/JOEWRKS/GEOTest/FnBShop')
sys.path.insert(0, str(REPO / 'skills/joedesign/scripts'))
from harness.conformance import input_fingerprint, load_baseline

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

source = GEO / '.design-harness/conformance/spacing-baseline.json'
pin = sha(source)
baseline = load_baseline(source, pin, GEO)
paths = {a['path'] for a in baseline['authority']} | {
    p for c in baseline['required_checks'] for p in c['inputs']}
before = {p: sha(GEO / p) for p in paths}
with tempfile.TemporaryDirectory(prefix='joedesign-f05-') as directory:
    root = Path(directory)
    for name in paths:
        target = root / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(GEO / name, target)
    copied_baseline = root / 'baseline.json'
    shutil.copyfile(source, copied_baseline)
    load_baseline(copied_baseline, pin, root)
    design = root / 'DESIGN.md'
    original_design = design.read_bytes()
    design.write_bytes(original_design + b'\n<!-- isolated diagnostic: no rule change -->\n')
    try:
        load_baseline(copied_baseline, pin, root)
        authority_result = 'UNEXPECTED_ACCEPT'
    except ValueError as error:
        authority_result = str(error)
    design.write_bytes(original_design)
    old = {c['check_id']: input_fingerprint(root, c['inputs'])
           for c in baseline['required_checks']}
    css_name = 'examples/geo-fresh-market/wireframes/design/visual.css'
    css = root / css_name
    css.write_bytes(css.read_bytes() + b'\n/* isolated diagnostic comment */\n')
    changed = [c['check_id'] for c in baseline['required_checks']
               if old[c['check_id']] != input_fingerprint(root, c['inputs'])]

after = {p: sha(GEO / p) for p in paths}
assert before == after and sha(source) == pin
assert authority_result == 'DESIGN_AUTHORITY_STALE'
assert len(changed) == sum(css_name in c['inputs'] for c in baseline['required_checks'])
report = {
    'source_commit': '3f76319f6c8a5929c2f55dc47b3c0e4f6a825bdb',
    'version': '0.3.0-dev', 'baseline_sha256': pin,
    'scope': baseline['scope_id'], 'checks': len(baseline['required_checks']),
    'targets': len(baseline['targets']), 'copied_inputs': len(paths),
    'design_comment_change': authority_result,
    'css_comment_changed_fingerprint_count': len(changed),
    'changed_check_ids': changed, 'product_input_hashes_before': before,
    'product_inputs_unchanged': before == after,
    'limits': 'Temporary-copy validation/fingerprints only. No rendering, consumer run, '
              'selective-reuse implementation, source repin, receipt edit or product mutation.'}
(Path(__file__).parent / 'whole-file-reproduction.json').write_text(
    json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({k: report[k] for k in ['checks', 'targets', 'copied_inputs',
      'design_comment_change', 'css_comment_changed_fingerprint_count', 'product_inputs_unchanged']}))
