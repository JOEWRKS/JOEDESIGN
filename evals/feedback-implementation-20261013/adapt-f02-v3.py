"""Correct excluded historical observations after preserved source-r1 failure.

No source verdict or expectation changes: move only excluded observations out of
the normalized CURRENT list; preserve their source bytes and explicit history.
"""
import copy
import hashlib
import json
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEST = HERE / 'f02-fixtures-v3'

def read(path):
    return json.loads(path.read_text(encoding='utf-8'))

def write(path, value):
    path.write_bytes((json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode('utf-8'))

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def ref(root, name, pointer, value):
    return {'path': name, 'sha256': sha(root / name), 'pointer': pointer, 'value': value}

assert not DEST.exists()
expectations = copy.deepcopy(read(HERE / 'f02-expectations-v2.json'))
for case in expectations['cases']:
    old = HERE / case['input']
    root = DEST / case['id']
    shutil.copytree(old.parent, root)
    if case['id'] in ('F02-P02', 'F02-N06'):
        packet = read(root / 'input.json')
        required = {o['id'] for o in packet['required_outcomes']}
        prior = [o for o in packet['observations'] if o['outcome_id'] not in required]
        historical = {'synthetic': True, 'reason': 'Past excluded target findings retained',
                      'observations': prior}
        write(root / 'sources/excluded-history.json', historical)
        history_ref = ref(root, 'sources/excluded-history.json', '', historical)
        packet['views'].append({'id': 'excluded-history', 'kind': 'history',
                                'source': history_ref, 'claims': []})
        packet['observations'] = [o for o in packet['observations'] if o['outcome_id'] in required]
        mapping = {k: v for k, v in packet.items() if k != 'mapping_review'}
        digest = hashlib.sha256(json.dumps(mapping, sort_keys=True, ensure_ascii=False,
                                          separators=(',', ':')).encode('utf-8')).hexdigest()
        review = {'scope_id': packet['scope_id'], 'status': 'CONFIRMED', 'mapping_sha256': digest}
        write(root / 'sources/mapping-review-v3.json', {'synthetic': True, 'review': review,
          'reviewed_delta': 'Only current/excluded-history classification corrected; all underlying source verdicts retained.',
          'previous_input_sha256': sha(old), 'history_source': history_ref})
        packet['mapping_review'] = ref(root, 'sources/mapping-review-v3.json', '/review', review)
        write(root / 'input.json', packet)
        write(root / 'design-fragment.json', {'synthetic': True, 'scope_id': packet['scope_id'],
          'observations': [o for o in packet['observations'] if o['lane'] in ('technical', 'visual', 'acceptance')],
          'history_sources': [history_ref]})
        for source in ['sources/design-observations.json', 'sources/exact-acceptance.json',
                       'sources/scope.json', 'sources/authorization.json']:
            assert (root / source).read_bytes() == (old.parent / source).read_bytes()
    case['input'] = (root / 'input.json').relative_to(HERE).as_posix()
    case['input_sha256'] = sha(root / 'input.json')
expectations['contract_adaptation'] = 'Preserved original meaning; excluded observations now explicitly historical, not current.'
write(HERE / 'f02-expectations-v3.json', expectations)
print(json.dumps({'cases': len(expectations['cases']), 'corrected_mappings': 2,
                  'underlying_sources_unchanged': True}))
