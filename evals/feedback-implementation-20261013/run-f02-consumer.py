"""Cross-check JOEDESIGN fixtures against an explicitly selected JOENESS source CLI.

Candidate-source test only. No installation, gate activation, or product writes.
"""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument('--cli', type=Path, required=True)
parser.add_argument('--run-id', required=True)
parser.add_argument('--expectations', default='f02-expectations-v2.json')
args = parser.parse_args()
assert args.run_id and all(c.isalnum() or c in '-_' for c in args.run_id)
output = HERE / 'consumer-runs' / args.run_id
output.mkdir(parents=True, exist_ok=False)

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def read(path):
    return json.loads(path.read_text(encoding='utf-8'))

def inventory(root):
    return {p.relative_to(root).as_posix(): sha(p) for p in root.rglob('*') if p.is_file()}

cases = read(HERE / args.expectations)['cases']
fixture_root = (HERE / cases[0]['input']).parent.parent
before = inventory(fixture_root)
cli_before = sha(args.cli)
checks = []
for case in cases:
    path = HERE / case['input']
    assert sha(path) == case['input_sha256']
    command = ['node', str(args.cli.resolve()), '--root', str(path.parent),
               '--input', path.name, '--input-sha256', case['input_sha256']]
    run = subprocess.run(command, capture_output=True, timeout=30)
    (output / f'{case["id"]}.stdout.json').write_bytes(run.stdout)
    (output / f'{case["id"]}.stderr.txt').write_bytes(run.stderr)
    data = json.loads(run.stdout.decode('utf-8'))
    kinds = {f['kind'] for f in data.get('findings', [])}
    lanes = [status for outcome in data.get('outcomes', []) for status in outcome.get('lanes', {}).values()]
    expected = case['expected_class']
    ok = data.get('project_complete') is False
    if expected == 'ready':
        ok &= run.returncode == 0 and data.get('delivery') == 'complete'
        ok &= any('UNAPPROVED' in row.get('text', '') for row in data.get('limitations', []))
    elif expected == 'blocked':
        ok &= run.returncode != 0 and data.get('delivery') == 'incomplete'
        ok &= ('REJECTED' in lanes if case['id'] == 'F02-N01' else 'ACCEPTED' in lanes and 'NOT_GRANTED' in lanes)
    elif expected == 'unknown':
        ok &= run.returncode != 0 and data.get('delivery') != 'complete'
        ok &= 'unknown' in kinds or 'UNVERIFIED' in lanes
    elif expected == 'conflict':
        ok &= run.returncode != 0 and 'conflict' in kinds and data.get('delivery') != 'complete'
    elif expected == 'invalid':
        ok &= run.returncode != 0 and 'invalid' in kinds
    else:
        ok &= run.returncode != 0 and data.get('delivery') != 'complete'
        ok &= bool(kinds & ({'invalid', 'conflict'} if case['id'] == 'F02-N10' else {'invalid', 'unknown'}))
    checks.append({'case': case['id'], 'command': command, 'exit': run.returncode,
                   'expected': expected, 'delivery': data.get('delivery'),
                   'finding_kinds': sorted(kinds), 'lanes': lanes, 'expectation_met': bool(ok)})

after = inventory(fixture_root)
report = {'cli': str(args.cli.resolve()), 'cli_sha256_before': cli_before,
          'cli_sha256_after': sha(args.cli), 'fixtures_unchanged': before == after,
          'input_hashes': before, 'cases': checks,
          'limit': 'Synthetic source-candidate contract cross-check; not isolated installation, live measurement, user acceptance or semantic authentication.'}
(output / 'results.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
passed = before == after and cli_before == report['cli_sha256_after'] and all(c['expectation_met'] for c in checks)
print(json.dumps({'cases': len(checks), 'expectations_met': sum(c['expectation_met'] for c in checks),
                  'fixtures_unchanged': before == after, 'cli_unchanged': cli_before == report['cli_sha256_after'],
                  'report': str(output / 'results.json')}))
raise SystemExit(0 if passed else 1)
