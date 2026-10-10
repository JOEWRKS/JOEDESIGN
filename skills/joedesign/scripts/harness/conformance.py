"""Scoped, pinned design checks. Local evidence is not authenticated acceptance."""
import hashlib
import json
import math
from pathlib import Path, PurePosixPath
import unicodedata

from .io import digest, file_hash, read_artifact, unique_pairs


def input_path(project, name):
    if (not isinstance(name, str) or not name or '\\' in name or ':' in name or
            any(ord(ch) < 32 for ch in name) or
            unicodedata.normalize('NFC', name) != name or
            PurePosixPath(name).is_absolute() or any(p in ('', '.', '..') for p in name.split('/'))):
        raise ValueError('INVALID_INPUT_PATH')
    path = (Path(project) / name).resolve(strict=True)
    if not path.is_relative_to(Path(project).resolve()) or not path.is_file():
        raise ValueError('INPUT_PATH_ESCAPE')
    return path


def input_fingerprint(project, inputs):
    if not isinstance(inputs, list) or not inputs or len(inputs) != len(set(inputs)):
        raise ValueError('INVALID_CHECK_INPUTS')
    pairs = [[p, file_hash(input_path(project, p))] for p in sorted(inputs, key=lambda p: p.encode('utf-8'))]
    return hashlib.sha256(json.dumps(pairs, ensure_ascii=False, separators=(',', ':')).encode('utf-8')).hexdigest()


def load_baseline(path, expected_hash, project, targets=None):
    raw = Path(path).read_bytes()
    if not expected_hash or hashlib.sha256(raw).hexdigest() != expected_hash:
        raise ValueError('DESIGN_BASELINE_PIN_MISMATCH')
    baseline = json.loads(raw.decode('utf-8-sig'), object_pairs_hook=unique_pairs,
                          parse_constant=lambda v: (_ for _ in ()).throw(ValueError(v)))
    if not isinstance(baseline, dict):
        raise ValueError('DESIGN_BASELINE_INVALID')
    if baseline.get('schema') != 'joeness.review-baseline.v1' or not baseline.get('scope_id') or not baseline.get('authorization_ref'):
        raise ValueError('DESIGN_BASELINE_INVALID')
    authority = baseline.get('authority')
    if not isinstance(authority, list) or not authority:
        raise ValueError('DESIGN_AUTHORITY_MISSING')
    for source in authority:
        if file_hash(input_path(project, source['path'])) != source['sha256']:
            raise ValueError('DESIGN_AUTHORITY_STALE')
    declared = baseline.get('targets', [])
    target_map = {t['id']: t for t in declared}
    if not declared or len(target_map) != len(declared) or (targets is not None and declared != targets):
        raise ValueError('DESIGN_TARGET_COVERAGE')
    checks = baseline.get('required_checks', [])
    if not checks or len({c['check_id'] for c in checks}) != len(checks):
        raise ValueError('DESIGN_CHECK_COVERAGE')
    for check in checks:
        criterion = check.get('criterion', {})
        if (check.get('lane') != 'visual' or check.get('method') not in ('geometry', 'specialist') or
                check.get('target_id') not in target_map or not check.get('rule_id') or
                check.get('criterion_sha256') != digest(criterion)):
            raise ValueError('DESIGN_CRITERION_INVALID')
        input_fingerprint(project, check.get('inputs'))
        if check['method'] == 'geometry':
            if (criterion.get('kind') not in ('pair', 'gap', 'inset') or
                    type(criterion.get('expected_count')) is not int or criterion['expected_count'] < 1 or
                    any(type(criterion.get(k)) not in (int, float) or not math.isfinite(criterion[k])
                        for k in ('min', 'max', 'tolerance')) or
                    criterion['min'] > criterion['max'] or criterion['tolerance'] < 0):
                raise ValueError('DESIGN_MEASUREMENT_INVALID')
            if 'max_spread' in criterion and (type(criterion['max_spread']) not in (int, float) or
                    not math.isfinite(criterion['max_spread']) or criterion['max_spread'] < 0):
                raise ValueError('DESIGN_MEASUREMENT_INVALID')
        elif (not criterion.get('claim_id') or not criterion.get('expected') or criterion.get('category') not in
              ('Structure', 'VisualConformance', 'VisualQuality', 'Craft', 'Accessibility', 'Responsive', 'Experience')):
            raise ValueError('DESIGN_SPECIALIST_CRITERION_INVALID')
    # The independently reviewed rule inventory is the coverage authority. Natural
    # language completeness cannot be inferred from a JSON file or self-attestation.
    rules = baseline.get('rules', [])
    if not rules or len({r['id'] for r in rules}) != len(rules):
        raise ValueError('DESIGN_RULE_COVERAGE')
    expected = {(r['id'], t, m) for r in rules for t in r['target_ids'] for m in r['methods']}
    actual = {(c['rule_id'], c['target_id'], c['method']) for c in checks}
    if expected != actual or not all(r.get('source_ref') and r['target_ids'] and r['methods'] and
            r['source_ref'].split('#')[0] in {s['path'] for s in authority} for r in rules):
        raise ValueError('DESIGN_RULE_COVERAGE')
    if set(target_map) != {c['target_id'] for c in checks}:
        raise ValueError('DESIGN_TARGET_COVERAGE')
    return baseline


def bindings(baseline, project, target_ids):
    return {c['check_id']: input_fingerprint(project, c['inputs']) for c in baseline['required_checks']
            if c['target_id'] in target_ids}


def evaluate(baseline, baseline_hash, project, observations, review_path=None, target_ids=None):
    """Recompute verdicts; required missing observations remain UNVERIFIED."""
    target_ids = target_ids or [t['id'] for t in baseline['targets']]
    targets = {t['id']: t for t in baseline['targets']}
    try:
        reviews = read_artifact(review_path) if review_path else {}
    except (OSError, ValueError):
        reviews = {}
    logs = []
    for path in observations:
        try:
            log = read_artifact(path)
            if 'design' in log:
                logs.append((Path(path), log))
        except (ValueError, OSError):
            continue
    results, unresolved = [], []
    for check in baseline['required_checks']:
        if check['target_id'] not in target_ids:
            continue
        fingerprint = input_fingerprint(project, check['inputs'])
        row = {k: check[k] for k in ('check_id', 'target_id', 'method', 'criterion_sha256')}
        row.update(status='UNVERIFIED', input_fingerprint=fingerprint, evidence=[])
        reason = 'Required current observation missing'
        matches = [(p, log) for p, log in logs if log.get('target') == targets[check['target_id']] and
                   log['design'].get('baseline_sha256') == baseline_hash and
                   log['design'].get('input_fingerprints', {}).get(check['check_id']) == fingerprint]
        if len(matches) == 1:
            path, log = matches[0]
            try:
                paths = [path, *map(Path, log['frames'])]
                if len(paths) < 2:
                    raise ValueError('No rendered frame')
                # Hash-map keys belong to the recorded observation. Path() can
                # change slash spelling on Windows; use it only to read bytes.
                if any(file_hash(p) != log.get('frame_hashes', {}).get(name)
                       for name, p in zip(log['frames'], paths[1:])):
                    raise ValueError('Rendered frame changed since observation')
                row['evidence'] = [{'path': str(p.resolve()), 'sha256': file_hash(p)} for p in paths]
                if check['method'] == 'geometry':
                    measurements = [m for m in log['design'].get('measurements', []) if m.get('check_id') == check['check_id']]
                    if len(measurements) != 1:
                        raise ValueError('Measurement missing/duplicate')
                    m, criterion = measurements[0], check['criterion']
                    values = m.get('values')
                    if (m.get('error') or m.get('criterion_sha256') != check['criterion_sha256'] or
                            not isinstance(values, list) or len(values) != criterion['expected_count'] or
                            any(type(v) not in (int, float) or not math.isfinite(v) for v in values)):
                        raise ValueError('Incomplete or invalid rendered measurement')
                    tolerance = criterion['tolerance']
                    passed = all(criterion['min'] - tolerance <= v <= criterion['max'] + tolerance for v in values)
                    if 'max_spread' in criterion:
                        passed &= max(values) - min(values) <= criterion['max_spread'] + tolerance
                    row.update(status='PASS' if passed else 'FAIL', measured_values=values)
                    reason = 'Rendered relationship outside pinned criterion' if not passed else ''
                else:
                    # Only the ordered existing review report supplies specialist
                    # judgments. A geometric PASS never fills this lane.
                    from .evidence import RACI_ROUTES
                    claim = check['criterion']['claim_id']
                    route = RACI_ROUTES[check['criterion']['category']]
                    rs = [r for r in (reviews or {}).get('reviews', []) if r.get('claim_id') == claim]
                    critic = [r for r in (reviews or {}).get('critic', {}).get('claims', []) if r.get('claim_id') == claim]
                    if (reviews.get('baseline_sha256') != baseline_hash or
                            reviews.get('input_fingerprints', {}).get(check['check_id']) != fingerprint or
                            reviews.get('build_id') != log.get('build_id') or
                            not all(any(r.get('reviewer') == who and r.get('raci_step') == rank for r in rs)
                                    for who, rank in zip(route[:2], ('R', 'C1'))) or len(critic) != 1):
                        raise ValueError('Specialist/critic coverage missing')
                    bound_claim = next((c for c in reviews.get('claims', []) if c.get('id') == claim), {})
                    if (bound_claim.get('target_id') != check['target_id'] or
                            bound_claim.get('expected') != check['criterion']['expected'] or
                            bound_claim.get('category') != check['criterion']['category']):
                        raise ValueError('Specialist criterion binding missing')
                    contexts = [r.get('context_id') for r in rs]
                    if (not all(contexts) or len(set(contexts)) != len(contexts) or
                            not reviews.get('critic_context_id') or reviews['critic_context_id'] in contexts):
                        raise ValueError('Independent review contexts missing')
                    captures = {c['id']: c for c in reviews.get('captures', []) if
                        c.get('target') == targets[check['target_id']] and
                        c.get('build_id') == log.get('build_id') and c.get('kind') == bound_claim.get('kind') and
                        file_hash(c['path']) == c.get('sha256')}
                    for verdict in rs + critic:
                        if not verdict.get('observed') or not set(verdict.get('evidence_ids', [])) & set(captures):
                            raise ValueError('Specialist actual evidence missing')
                    for capture in captures.values():
                        row['evidence'].append({'path': capture['path'], 'sha256': capture['sha256']})
                    verdicts = [r.get('verdict') for r in rs + critic]
                    row['status'] = 'FAIL' if 'FAIL' in verdicts else 'PASS' if all(v == 'PASS' for v in verdicts) else 'UNVERIFIED'
                    row['evidence'].append({'path': str(Path(review_path).resolve()), 'sha256': file_hash(review_path)})
                    reason = 'Specialist or critic finding unresolved' if row['status'] != 'PASS' else ''
            except (ValueError, OSError, KeyError, TypeError) as error:
                row['status'], reason = 'UNVERIFIED', str(error)
        if row['status'] != 'PASS':
            unresolved.append({'check_id': check['check_id'], 'reason': reason})
        results.append(row)
    return {'schema': 'joedesign.conformance.v1', 'scope_id': baseline['scope_id'],
            'baseline_sha256': baseline_hash, 'results': results, 'unresolved': unresolved,
            'acceptance': 'NOT_GRANTED', 'trust': 'LOCAL_UNAUTHENTICATED',
            'eligible': bool(results) and not unresolved,
            'unreviewed_check_ids': [c['check_id'] for c in baseline['required_checks'] if c['target_id'] not in target_ids]}
