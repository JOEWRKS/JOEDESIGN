"""Create synthetic, source-bound design observations for JOENESS F02 integration.

No product reads/writes, no real acceptance or browser result is manufactured.
Every source explicitly labels its assertions synthetic. Consumer expectations
are kept outside each fixture root and never passed as authority inputs.
"""
import copy
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEST = HERE / 'f02-fixtures'

def raw(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode('utf-8')

def write(root, name, value):
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(raw(value))

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def ref(root, path, pointer, value):
    return {'path': path, 'sha256': sha(root / path), 'pointer': pointer,
            'value': copy.deepcopy(value)}

CASES = [
    ('F02-P01', 'demo complete, operations outside scope, Manifest unapproved', 'ready'),
    ('F02-N01', 'technical PASS but required mobile output rejected', 'blocked'),
    ('F02-N02', 'desktop accepted, mobile acceptance absent', 'blocked'),
    ('F02-N03', 'required mobile observation unverified', 'unknown'),
    ('F02-N04', 'current output changed after observations', 'unknown'),
    ('F02-N05', 'same current exact output accepted and rejected', 'conflict'),
    ('F02-P02', 'authorized removal of former required mobile outcome, failure retained', 'ready'),
    ('F02-N06', 'exclusion lacks authorization', 'invalid_or_unknown'),
    ('F02-N07', 'visual PASS, technical not verified', 'unknown'),
    ('F02-N08', 'same output but different viewport identity in observation', 'unknown'),
    ('F02-N09', 'duplicate required outcome', 'invalid'),
    ('F02-N10', 'normalized PASS contradicts bound raw FAIL', 'invalid_or_conflict'),
    ('F02-N11', 'mapping semantic review absent', 'unknown'),
]

def build(case_id):
    root = DEST / case_id
    root.mkdir(parents=True, exist_ok=False)
    targets = {}
    for name, width in [('desktop', 1240), ('mobile', 390)]:
        output = f'outputs/{name}.json'
        write(root, output, {'synthetic': True, 'text': 'Fixture output, not rendered UI'})
        identity = f'targets/{name}.json'
        write(root, identity, {'synthetic': True, 'scope_id': 'synthetic-demo',
              'build_id': 'fixture-build-r1', 'route': '/demo', 'state': 'initial',
              'viewport': [width, 900], 'theme': 'light', 'locale': 'ko',
              'output': {'path': output, 'sha256': sha(root / output)}})
        targets[name] = [{'path': p, 'sha256': sha(root / p)} for p in [identity, output]]

    acceptance_required = case_id in ('F02-N01', 'F02-N02', 'F02-N05')
    scope = {'synthetic': True, 'scope_id': 'synthetic-demo', 'revision': 1,
             'manifest_approval': 'UNAPPROVED', 'delivery': 'non-launch demo',
             'required': [], 'excluded': []}
    for name in targets:
        scope['required'].append({'id': f'{name}-view', 'label': f'{name} scoped review',
            'required_lanes': ['implementation', 'technical', 'visual'],
            'acceptance_required': acceptance_required,
            'targets': targets[name],
            'visual_meaning': 'Fixture-scoped conformance; not global aesthetic acceptance'})
    scope['excluded'].append({'id': 'production-operations', 'label': 'Live operations',
                              'reason': 'The synthetic scope explicitly excludes launch'})
    if case_id in ('F02-P02', 'F02-N06'):
        scope['required'] = scope['required'][:1]
        scope['excluded'].append({'id': 'mobile-view', 'label': 'Prior mobile outcome',
                                  'reason': 'Explicit synthetic scoped change'})
    decision = {'synthetic': True, 'scope_id': scope['scope_id'], 'revision': 1,
                'actor': 'SYNTHETIC_USER_NOT_REAL_APPROVAL',
                'decision': 'Use this fixture scope, preserve Manifest UNAPPROVED',
                'scope': scope}
    write(root, 'sources/scope.json', scope)
    write(root, 'sources/authorization.json', decision)
    observations = []
    acceptance = []
    for name, target in targets.items():
        for lane in ['implementation', 'technical', 'visual']:
            status = 'PASS'
            if name == 'mobile' and lane == 'visual' and case_id in ('F02-N03',):
                status = 'UNVERIFIED'
            if name == 'mobile' and lane == 'technical' and case_id == 'F02-N07':
                status = 'UNVERIFIED'
            if name == 'mobile' and lane == 'visual' and case_id in ('F02-P02', 'F02-N06', 'F02-N10'):
                status = 'FAIL'
            observations.append({'outcome_id': f'{name}-view', 'lane': lane, 'status': status,
                                 'targets': copy.deepcopy(target)})
        status = 'NOT_GRANTED'
        if acceptance_required:
            status = 'ACCEPTED' if name == 'desktop' else ('REJECTED' if case_id == 'F02-N01' else 'NOT_GRANTED')
        acceptance.append({'outcome_id': f'{name}-view', 'lane': 'acceptance',
                           'status': status, 'targets': copy.deepcopy(target)})
    if case_id == 'F02-N05':
        acceptance[-1]['status'] = 'ACCEPTED'
        rejected = copy.deepcopy(acceptance[-1]); rejected['status'] = 'REJECTED'
        acceptance.append(rejected)
    if case_id == 'F02-N08':
        alternate = {'synthetic': True, 'route': '/demo', 'state': 'initial',
                     'viewport': [767, 900], 'theme': 'light', 'locale': 'ko'}
        write(root, 'targets/mobile-other.json', alternate)
        observations[-1]['targets'][0] = {'path': 'targets/mobile-other.json',
                                         'sha256': sha(root / 'targets/mobile-other.json')}
    observed_source = {'synthetic': True, 'not_real_measurement': True,
                       'scope_id': scope['scope_id'], 'claims': observations}
    acceptance_source = {'synthetic': True, 'not_real_user_acceptance': True,
                         'scope_id': scope['scope_id'], 'claims': acceptance}
    write(root, 'sources/design-observations.json', observed_source)
    write(root, 'sources/exact-acceptance.json', acceptance_source)
    review = {'synthetic': True, 'kind': 'scope-to-source mapping review fixture',
              'scope': {'path': 'sources/scope.json', 'sha256': sha(root / 'sources/scope.json')},
              'reviewed_meaning': [
                  'Current demo scope is distinct from full Manifest approval and launch.',
                  'Visual observations do not create exact user acceptance.',
                  'Per-target evidence does not transfer to other viewport or output.',
                  'Excluded former failures are retained as history, not erased.'],
              'reviewed_sources': [{'path': p, 'sha256': sha(root / p)} for p in
                  ['sources/design-observations.json', 'sources/exact-acceptance.json']],
              'unreviewed_meaning': []}
    write(root, 'sources/mapping-review.json', review)
    packet = {'schema': 'joeness.roadmap-review.v1', 'scope_id': scope['scope_id'],
              'scope_source': ref(root, 'sources/scope.json', '', scope),
              'scope_authorization': ref(root, 'sources/authorization.json', '', decision),
              'mapping_review': ref(root, 'sources/mapping-review.json', '', review),
              'required_outcomes': [], 'excluded_outcomes': [], 'observations': []}
    for n, outcome in enumerate(scope['required']):
        row = {k: copy.deepcopy(outcome[k]) for k in ['id', 'label', 'required_lanes', 'acceptance_required', 'targets']}
        row['source'] = ref(root, 'sources/scope.json', f'/required/{n}', outcome)
        packet['required_outcomes'].append(row)
    for n, outcome in enumerate(scope['excluded']):
        packet['excluded_outcomes'].append({'id': outcome['id'], 'label': outcome['label'],
            'source': ref(root, 'sources/scope.json', f'/excluded/{n}', outcome),
            'authorization': ref(root, 'sources/authorization.json', '', decision)})
    for path, claims in [('sources/design-observations.json', observations),
                         ('sources/exact-acceptance.json', acceptance)]:
        for n, claim in enumerate(claims):
            packet['observations'].append(copy.deepcopy(claim) | {
                'source': ref(root, path, f'/claims/{n}', claim)})
    if case_id == 'F02-N04':
        write(root, 'outputs/mobile.json', {'synthetic': True, 'text': 'Changed output revision2'})
    if case_id == 'F02-N06':
        packet['excluded_outcomes'][-1]['authorization'] = None
    if case_id == 'F02-N09':
        packet['required_outcomes'].append(copy.deepcopy(packet['required_outcomes'][0]))
    if case_id == 'F02-N10':
        next(x for x in packet['observations'] if x['outcome_id'] == 'mobile-view' and x['lane'] == 'visual')['status'] = 'PASS'
    if case_id == 'F02-N11':
        packet['mapping_review'] = None
    write(root, 'input.json', packet)
    # Hand-off fragment: no requiredness, no delivery judgment, no manufactured approval.
    write(root, 'design-fragment.json', {'synthetic': True, 'scope_id': scope['scope_id'],
        'observations': [r for r in packet['observations'] if r['lane'] in ('technical', 'visual', 'acceptance')]})
    return root

if __name__ == '__main__':
    assert not DEST.exists(), 'Preserve earlier fixtures; do not overwrite an observed run'
    index = []
    for case_id, meaning, expected in CASES:
        root = build(case_id)
        index.append({'id': case_id, 'meaning': meaning, 'expected_class': expected,
                      'input': str((root / 'input.json').relative_to(HERE)),
                      'input_sha256': sha(root / 'input.json')})
    write(HERE, 'f02-expectations.json', {'synthetic': True,
          'expectations_frozen_before_consumer_execution': True, 'cases': index})
    print(json.dumps({'cases': len(index), 'directory': str(DEST)}))
