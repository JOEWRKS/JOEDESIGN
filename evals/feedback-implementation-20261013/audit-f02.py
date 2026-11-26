"""Inspect fixture provenance and intentional negative cases without judging delivery.

This is not JOENESS consumption, a semantic reviewer, or a production validator.
"""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent

def read(path):
    return json.loads(path.read_text(encoding='utf-8'))

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def resolve(value, pointer):
    if pointer == '':
        return value
    for token in pointer[1:].split('/'):
        token = token.replace('~1', '/').replace('~0', '~')
        value = value[int(token)] if isinstance(value, list) else value[token]
    return value

expected = {
    'F02-N04': {'target_stale'}, 'F02-N06': {'missing_exclusion_authorization'},
    'F02-N08': {'target_mismatch'}, 'F02-N09': {'duplicate_required'},
    'F02-N10': {'source_claim_mismatch'}, 'F02-N11': {'missing_mapping_review'},
}
results = []
for case in read(HERE / 'f02-expectations.json')['cases']:
    path = HERE / case['input']
    root = path.parent
    assert sha(path) == case['input_sha256'], 'Expectation/input drift'
    packet = read(path)
    issues = set()
    refs = [packet['scope_source'], packet['scope_authorization']]
    if packet['mapping_review'] is None:
        issues.add('missing_mapping_review')
    else:
        refs.append(packet['mapping_review'])
    required = packet['required_outcomes']
    if len({r['id'] for r in required}) != len(required):
        issues.add('duplicate_required')
    by_id = {r['id']: r for r in required}
    for item in required + packet['excluded_outcomes']:
        refs.append(item['source'])
    for item in packet['excluded_outcomes']:
        if item['authorization'] is None:
            issues.add('missing_exclusion_authorization')
        else:
            refs.append(item['authorization'])
    for observation in packet['observations']:
        refs.append(observation['source'])
        source_claim = observation['source']['value']
        if any(source_claim.get(k) != observation.get(k) for k in
               ['outcome_id', 'lane', 'status', 'targets']):
            issues.add('source_claim_mismatch')
        if observation['outcome_id'] in by_id and observation['targets'] != by_id[observation['outcome_id']]['targets']:
            issues.add('target_mismatch')
        for target in observation['targets']:
            if sha(root / target['path']) != target['sha256']:
                issues.add('target_stale')
    for item in refs:
        source = root / item['path']
        assert source.resolve().is_relative_to(root.resolve())
        assert sha(source) == item['sha256'], str(source)
        value = read(source)
        assert value.get('synthetic') is True, str(source)
        assert resolve(value, item['pointer']) == item['value'], item
    assert issues == expected.get(case['id'], set()), (case['id'], issues)
    results.append({'case': case['id'], 'intentional_structural_findings': sorted(issues),
                    'source_references_verified': len(refs)})

report = {'purpose': 'Synthetic fixture provenance audit, not delivery/consumer PASS',
          'cases': results, 'files': {p.relative_to(HERE).as_posix(): sha(p)
          for p in sorted((HERE / 'f02-fixtures').rglob('*')) if p.is_file()}}
(HERE / 'f02-fixture-audit.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
print(json.dumps({'fixture_cases': len(results), 'source_binding_audit': 'PASS',
                  'consumer_executed': False}))
