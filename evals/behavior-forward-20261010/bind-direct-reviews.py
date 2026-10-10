"""Bind actual trial review records for verify-design; no invented review verdicts.

This evaluation-only adapter consumes saved R, C1 and fresh-critic outputs. It
does not invoke reviewers, authenticate them, or represent a harness runner run.
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('case')
parser.add_argument('--baseline', default='evidence/baseline.json')
parser.add_argument('--observations', required=True)
parser.add_argument('--r', default='evidence/review-r/results.json')
parser.add_argument('--c1', action='append', help='Repeat for separately assigned C1 workers')
parser.add_argument('--critic', default='evidence/critic/results.json')
parser.add_argument('--output', required=True)
args = parser.parse_args()
repo = Path(__file__).resolve().parents[2]
root = repo / '.local/behavior-forward-20261010'
case = root / 'cases' / args.case
sys.path.insert(0, str(root / 'package/joedesign/scripts'))
from harness.conformance import input_fingerprint

def read(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

baseline = read(case / args.baseline)
c1_paths = args.c1 or ['evidence/review-c1/results.json']
reports = [read(case / path) for path in [args.r, *c1_paths]]
critic = read(case / args.critic)
logs = [(p, read(p)) for p in sorted(case.glob(args.observations))]
assert logs, 'No observations'
builds = {log['build_id'] for _, log in logs}
assert len(builds) == 1, 'Mixed builds'
captures = []
for path, log in logs:
    for kind, paths in [('interaction', [str(path.resolve())]), ('render', log['frames'])]:
        for n, capture_path in enumerate(paths):
            p = Path(capture_path)
            captures.append({'id': f'{log["target"]["id"]}-{kind}-{n}',
                             'target': log['target'], 'kind': kind,
                             'build_id': log['build_id'], 'path': str(p.resolve()),
                             'sha256': sha(p)})

checks = [c for c in baseline['required_checks'] if c['method'] == 'specialist']
claims = [{'id': c['criterion']['claim_id'], 'target_id': c['target_id'],
           'category': c['criterion']['category'], 'expected': c['criterion']['expected'],
           'kind': 'interaction' if c['criterion']['category'] in ('Experience', 'Accessibility') else 'render'}
          for c in checks]
by_claim = {c['id']: c for c in claims}

def bind(row, context):
    c = by_claim[row['claim_id']]
    cited = {str((Path(p) if Path(p).is_absolute() else case / p).resolve()).casefold()
             for p in row['evidence_paths']}
    ids = [cap['id'] for cap in captures if cap['target']['id'] == c['target_id']
           and cap['kind'] == c['kind'] and cap['path'].casefold() in cited]
    assert ids, f'No actually cited matching evidence: {context} {c["id"]}'
    return {k: v for k, v in row.items() if k != 'evidence_paths'} | {
        'context_id': context, 'evidence_ids': ids}

reviews = [bind(row, report['context_id']) for report in reports for row in report['reviews']]
critic_rows = critic.get('reviews', critic.get('claims', []))
bound_critic = [bind(row, critic['context_id']) for row in critic_rows]
report = {
    'origin': 'Evaluation adapter of actual direct-tool reviews; NOT a runner-produced or authenticated report',
    'baseline_sha256': sha(case / args.baseline), 'build_id': next(iter(builds)),
    'input_fingerprints': {c['check_id']: input_fingerprint(case, c['inputs']) for c in baseline['required_checks']},
    'claims': claims, 'captures': captures, 'reviews': reviews,
    'critic_context_id': critic['context_id'], 'critic': {'claims': bound_critic},
    'source_reports': [{'path': str((case / p).resolve()), 'sha256': sha(case / p)}
                       for p in (args.r, *c1_paths, args.critic)],
    'trust': 'LOCAL_UNAUTHENTICATED', 'acceptance': 'NOT_GRANTED'}
with (case / args.output).open('x', encoding='utf-8') as stream:
    json.dump(report, stream, ensure_ascii=False, indent=2)
print(json.dumps({'reviews': len(reviews), 'critic_claims': len(bound_critic), 'output': args.output}))
