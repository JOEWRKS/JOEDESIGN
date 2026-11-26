"""Preserve v1 fixtures and adapt to the mutually reviewed F02 consumer contract.

Adds a current view, explicit limits, and a canonical mapping-review binding.
Synthetic review content is a test input, not evidence of human acceptance.
"""
import copy
import hashlib
import json
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEST = HERE / 'f02-fixtures-v2'

def read(path):
    return json.loads(path.read_text(encoding='utf-8'))

def write(path, data):
    path.write_bytes((json.dumps(data, ensure_ascii=False, indent=2) + '\n').encode('utf-8'))

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def ref(root, name, pointer, value):
    return {'path': name, 'sha256': sha(root / name), 'pointer': pointer, 'value': value}

assert not DEST.exists(), 'Preserve previously observed fixtures'
expectations = copy.deepcopy(read(HERE / 'f02-expectations.json'))
for case in expectations['cases']:
    original = HERE / case['input']
    root = DEST / case['id']
    shutil.copytree(original.parent, root)
    packet = read(root / 'input.json')
    view = {'synthetic': True, 'current': {'scope': packet['scope_id'],
            'stage': 'Consume the fixed synthetic observations; no real product work'}}
    write(root / 'sources/current-view.json', view)
    packet['views'] = [{'id': 'current', 'kind': 'current',
        'source': ref(root, 'sources/current-view.json', '/current', view['current']),
        'claims': [{'key': 'scope', 'value': packet['scope_id'],
          'source': ref(root, 'sources/current-view.json', '/current/scope', packet['scope_id'])}]}]
    packet['limitations'] = [{'text': 'Synthetic only; full Manifest approval remains UNAPPROVED.',
        'source': ref(root, 'sources/scope.json', '/manifest_approval', 'UNAPPROVED')}]
    without_review = {k: v for k, v in packet.items() if k != 'mapping_review'}
    mapping_hash = hashlib.sha256(json.dumps(without_review, ensure_ascii=False,
        sort_keys=True, separators=(',', ':')).encode('utf-8')).hexdigest()
    old_review = read(root / 'sources/mapping-review.json')
    review = {'scope_id': packet['scope_id'], 'status': 'CONFIRMED',
              'mapping_sha256': mapping_hash}
    write(root / 'sources/mapping-review-v2.json', {'synthetic': True,
          'review': review, 'review_content': old_review,
          'limits': 'Canonical binding detects changed mapping; not author authentication or semantic proof.'})
    if case['id'] != 'F02-N11':
        packet['mapping_review'] = ref(root, 'sources/mapping-review-v2.json', '/review', review)
    write(root / 'input.json', packet)
    case['input'] = (root / 'input.json').relative_to(HERE).as_posix()
    case['input_sha256'] = sha(root / 'input.json')
expectations['contract_adaptation'] = 'Current view + explicit limits + canonical mapping digest; original case meaning unchanged.'
write(HERE / 'f02-expectations-v2.json', expectations)
print(json.dumps({'adapted_cases': len(expectations['cases']), 'original_fixtures_preserved': True}))
