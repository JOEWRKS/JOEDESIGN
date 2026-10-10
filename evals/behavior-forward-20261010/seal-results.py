"""Save byte-identical selected reports and an index of the retained local run.

Run only after direct reviews and verify-design finish. This script neither runs
reviewers nor supplies missing verdicts. Local hashes are not host attestation.
"""
import hashlib
import json
from pathlib import Path

EVAL = Path(__file__).resolve().parent
ROOT = EVAL.parents[1] / '.local/behavior-forward-20261010'
SELECTED = {
    'new': {
        'conformance': 'final-conformance-fresh.json',
        'baseline': 'baseline.json', 'direct-reviews': 'direct-reviewed-fresh.json',
        'r': 'review-r/results.json', 'c1': 'review-c1/results.json',
        'critic': 'critic-fresh/results.json',
    },
    'repair': {
        'conformance': 'final-conformance.json',
        'baseline': 'baseline.json', 'direct-reviews': 'direct-reviewed.json',
        'r': 'review-r/results.json', 'c1': 'review-c1/results.json',
        'critic': 'critic/results.json',
    },
    'extension': {
        'conformance': 'final-integration-conformance.json',
        'baseline': 'integration-baseline.json',
        'direct-reviews': 'integration-direct-reviewed.json',
        'r': 'integration-review-r/results.json',
        'c1': 'integration-review-c1/results.json',
        'c1-behavior': 'integration-review-c1-behavior/results.json',
        'critic': 'integration-critic-fresh/results.json',
        'stale-proof': 'stale-proof-on-integrated-build.json',
        'dependencies': 'dependency-validation.json',
    },
}

def read(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

records = EVAL / 'records'
records.mkdir(exist_ok=True)
index = {'version': '0.3.0-dev', 'trust': 'LOCAL_UNAUTHENTICATED',
         'acceptance': 'NOT_GRANTED', 'cases': {}}
for case, selected in SELECTED.items():
    evidence = ROOT / 'cases' / case / 'evidence'
    baseline = read(evidence / selected['baseline'])
    result = read(evidence / selected['conformance'])
    expected = {c['check_id'] for c in baseline['required_checks']}
    assert {r['check_id'] for r in result['results']} == expected, case
    assert len(result['results']) == len(expected), case
    assert result['eligible'] and not result['unresolved'], case
    assert all(r['status'] == 'PASS' for r in result['results']), case
    assert result['acceptance'] == 'NOT_GRANTED', case
    assert result['baseline_sha256'] == sha(evidence / selected['baseline']), case
    copies = []
    for label, relative in selected.items():
        source = evidence / relative
        target = records / f'{case}-{label}.json'
        if target.exists():
            assert target.read_bytes() == source.read_bytes(), str(target)
        else:
            target.write_bytes(source.read_bytes())
        copies.append({'label': label, 'source': str(source.relative_to(ROOT)),
                       'saved': str(target.relative_to(EVAL)), 'sha256': sha(source)})
    index['cases'][case] = {'checks': len(expected), 'eligible': True,
                           'records': copies}

# Keep local paths explicit: the manifest identifies bytes, not portable raw assets.
manifest = {path.relative_to(ROOT).as_posix(): sha(path)
            for path in sorted(ROOT.rglob('*')) if path.is_file()
            and path.suffix != '.pyc' and '__pycache__' not in path.parts}
(EVAL / 'final-artifact-manifest.json').write_text(
    json.dumps(manifest, indent=2), encoding='utf-8')
index['local_artifact_count'] = len(manifest)
(EVAL / 'results.json').write_text(json.dumps(index, indent=2), encoding='utf-8')
print(json.dumps({case: data['checks'] for case, data in index['cases'].items()}))
