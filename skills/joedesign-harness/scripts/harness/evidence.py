"""Evidence policy. HostVerifier is supplied by a trusted deployment, never JSON.

The shipped CLI has no trusted host adapter: local records remain UNVERIFIED.
This module authenticates neither its caller nor the machine on which it runs.
"""
from typing import Protocol
from .io import digest, file_hash
from .contracts import identity, issue, ids, rows, strings, text, validate_intent, validate_lock, validate_contract

VERDICTS = {'PASS', 'FAIL', 'UNVERIFIED'}
REVIEWERS = {'Technical': ['implementer'], 'Accessibility': ['V', 'U'],
             'Responsive': ['V', 'U'], 'Craft': ['I', 'J'], 'Structure': ['J', 'I'],
             'VisualConformance': ['J', 'I'], 'VisualQuality': ['J', 'I']}


class HostVerifier(Protocol):
    """Host-owned service resolving immutable events outside the writer's authority.

    A local file reader is NOT an implementation of this trust guarantee.
    The integration must bind calibration to the model/rules/domain and user events
    to an authenticated actor, and approve the exact current snapshot/build.
    """
    def resolve(self, receipt_id: str) -> dict | None: ...


def resolve(host, receipt_id):
    if host is None or not text(receipt_id):
        return None
    try:
        receipt = host.resolve(receipt_id)
        return receipt if isinstance(receipt, dict) else None
    except Exception:
        # Unavailable host verification is absence of evidence, never success.
        return None


def attested(record, host, kind, expected=None):
    receipt = resolve(host, record.get('receipt_id'))
    expected = expected if expected is not None else {k: v for k, v in record.items() if k != 'receipt_id'}
    return bool(receipt and receipt.get('kind') == kind and
                all(receipt.get(k) == v for k, v in expected.items()))


def aggregate(values):
    return 'FAIL' if 'FAIL' in values else 'PASS' if values and all(v == 'PASS' for v in values) else 'UNVERIFIED'


def snapshot(bundle):
    return digest({k: bundle[k] for k in ('intent', 'lock', 'contract', 'matrix')})


def capture_binding(items, evidence_ids):
    """Bind observations to exact capture content, targets, build and run."""
    return digest([{k: item[k] for k in ('id', 'target', 'kind', 'sha256', 'run_id', 'build_id', 'snapshot')}
                   for item in sorted(items, key=lambda row: row['id']) if item['id'] in evidence_ids])


def repair_disposition(attempts, findings):
    if any(f.get('kind') == 'structural' and f.get('verdict') == 'FAIL' for f in findings):
        return 'MATERIAL_REWORK_REQUIRED'
    consecutive, unresolved = {}, set()
    for attempt in attempts:
        cause = attempt.get('cause_id')
        if attempt.get('outcome') in ('FAIL', 'UNVERIFIED', 'REGRESSION'):
            if not attempt.get('hypothesis'):
                unresolved.add(cause)
            consecutive[cause] = consecutive.get(cause, 0) + 1
        elif attempt.get('outcome') == 'IMPROVED':
            consecutive[cause] = 0
            unresolved.discard(cause)
    if unresolved:
        return 'UNRESOLVED'
    return 'MATERIAL_REWORK_REQUIRED' if any(v >= 2 for v in consecutive.values()) else 'CONTINUE'


def validate_matrix(bundle):
    intent, matrix = bundle['intent'], bundle['matrix']
    errors = identity(intent, matrix)
    targets = rows(matrix.get('targets'), 'matrix.targets', errors)
    ids(targets, 'matrix.targets', errors)
    if targets != intent['targets']:
        errors.append(issue('REQUIRED_TARGET_MISMATCH', 'matrix must preserve intent target identities and states'))
    if matrix.get('bindings') != {k: digest(bundle[k]) for k in ('intent', 'lock', 'contract')}:
        errors.append(issue('STALE_CONTRACT', 'matrix bindings differ from current inputs'))
    claims = rows(matrix.get('claims'), 'matrix.claims', errors)
    claim_ids = ids(claims, 'claims', errors)
    target_ids = {t['id'] for t in intent['targets']}
    visual_categories = {'VisualConformance', 'VisualQuality'}
    motion_translations = {r['id']: r for r in bundle['contract'].get('translations', [])
                           if r.get('axis') == 'motion'}
    for claim in claims:
        category = claim.get('category')
        reviewers = claim.get('reviewers')
        if (category not in REVIEWERS or claim.get('target_id') not in target_ids or
                claim.get('kind') not in ('render', 'interaction', 'technical') or
                type(claim.get('required')) is not bool or not text(claim.get('expected')) or
                not strings(reviewers)):
            errors.append(issue('INVALID_CLAIM', str(claim.get('id'))))
            continue
        if not set(REVIEWERS[category]) <= set(reviewers):
            errors.append(issue('MISSING_REVIEWER', str(claim['id'])))
        expected_kind = 'technical' if category == 'Technical' else 'interaction' if category == 'Accessibility' else 'render'
        visual_motion = category in visual_categories and claim['kind'] == 'interaction'
        if visual_motion:
            translation = motion_translations.get(claim.get('translation_id'), {})
            if claim['target_id'] not in translation.get('target_ids', []):
                errors.append(issue('INVALID_CLAIM', 'visual interaction claim requires an applicable motion translation'))
        elif claim['kind'] != expected_kind:
            errors.append(issue('INVALID_CLAIM', f'{category} requires {expected_kind} evidence'))
    for target_id in target_ids:
        categories = {c.get('category') for c in claims if c.get('target_id') == target_id and c.get('required') is True}
        if not set(REVIEWERS) <= categories:
            errors.append(issue('REQUIRED_CLAIM_MISSING', target_id))
        render_categories = {c.get('category') for c in claims if c.get('target_id') == target_id
                             and c.get('required') is True and c.get('kind') == 'render'}
        if not visual_categories <= render_categories:
            errors.append(issue('VISUAL_RENDER_PROOF_REQUIRED', target_id))
    # Endpoints and successful button presses do not establish expressive motion.
    # Keep still-image review AND require a separate observation of each sequence.
    for translation_id, translation in motion_translations.items():
        for target_id in translation.get('target_ids', []):
            categories = {c.get('category') for c in claims if c.get('target_id') == target_id
                          and c.get('required') is True and c.get('kind') == 'interaction'
                          and c.get('translation_id') == translation_id}
            if not visual_categories <= categories:
                errors.append(issue('MOTION_QUALITY_PROOF_REQUIRED', f'{translation_id}: {target_id}'))
    mandated = set(bundle['contract'].get('structure_claims', []))
    eligible = {c['id'] for c in claims if c.get('category') == 'Structure' and c.get('required') is True and c.get('kind') == 'render'}
    if not mandated <= eligible:
        errors.append(issue('STRUCTURE_PROOF_REQUIRED', 'structure claims missing in matrix'))
    return errors


def assess(bundle, host=None):
    categories = {key: 'UNVERIFIED' for key in REVIEWERS} | {'VisualInternal': 'UNVERIFIED'}
    report = {'categories': categories, 'proof_complete': False, 'approved': False,
              'user_acceptance': 'PENDING', 'critic_reviewed': False,
              'issues': [], 'claims': {}, 'verified_evidence': [],
              'disposition': 'UNRESOLVED', 'active_findings': [],
              'trust': 'HOST_ADAPTER' if host else 'LOCAL_UNAUTHENTICATED',
              'operational_validation': 'UNVERIFIED'}
    errors = report['issues']
    if not isinstance(bundle, dict) or any(not isinstance(bundle.get(k), dict) for k in
                                          ('intent', 'lock', 'contract', 'matrix', 'critique', 'evidence')):
        errors.append(issue('INVALID_ARTIFACT', 'six artifact objects required'))
        return report
    intent, lock, contract = bundle['intent'], bundle['lock'], bundle['contract']
    errors.extend(validate_intent(intent))
    if errors:
        return report
    errors.extend(validate_lock(intent, lock))
    errors.extend(validate_contract(intent, lock, contract))
    if errors:
        return report
    errors.extend(validate_matrix(bundle))
    if errors:
        return report
    current = snapshot(bundle)
    report.update(snapshot=current, scope={k: intent[k] for k in ('candidate_id', 'revision', 'scope_id')})
    manifest, critic = bundle['evidence'], bundle['critique']
    run = manifest.get('run', {})
    if not isinstance(run, dict):
        errors.append(issue('INVALID_RUN', 'run must be object'))
        return report
    errors.extend(identity(intent, run))
    if run.get('snapshot') != current or any(not text(run.get(k)) for k in
                                            ('run_id', 'build_id', 'implementation_context')):
        errors.append(issue('STALE_RUN', 'run identity/build/input snapshot required'))
    if errors:
        return report
    targets = {t['id']: t for t in intent['targets']}
    items = rows(manifest.get('items'), 'evidence.items', errors, False)
    ids(items, 'evidence.items', errors)
    reviews = rows(manifest.get('reviews'), 'evidence.reviews', errors, False)
    ids(reviews, 'evidence.reviews', errors)
    if errors:
        return report
    verified = {}
    for item in items:
        target = targets.get(item.get('target_id'))
        expected = {k: v for k, v in item.items() if k not in ('receipt_id', 'kind')}
        expected['evidence_kind'] = item.get('kind')
        valid = (target is not None and item.get('target') == target and
                 item.get('kind') in ('render', 'interaction', 'technical') and
                 all(item.get(k) == run.get(k) for k in ('run_id', 'build_id', 'snapshot')))
        if item.get('kind') == 'interaction':
            valid = valid and text(item.get('action')) and text(item.get('result'))
        try:
            valid = valid and file_hash(item.get('path', '')) == item.get('sha256')
        except (OSError, ValueError, TypeError):
            valid = False
        if valid and attested(item, host, 'capture', expected):
            verified[item['id']] = item
        else:
            errors.append(issue('EVIDENCE_UNVERIFIED', str(item.get('id'))))
    report['verified_evidence'] = list(verified)
    required_pairs = {(t['id'], kind) for t in targets.values() for kind in t['required_kinds']}
    required_pairs.update((t['id'], 'render') for t in targets.values())
    if any(r['kind'] in ('action', 'state') for r in intent['requirements']):
        required_pairs.update((t['id'], 'interaction') for t in targets.values())
    required_pairs.update((c['target_id'], c['kind']) for c in bundle['matrix']['claims'] if c['required'])
    present_pairs = {(e['target_id'], e['kind']) for e in verified.values()}
    report['proof_complete'] = required_pairs <= present_pairs
    if not report['proof_complete']:
        errors.append(issue('PROOF_INCOMPLETE', 'required target/state/kind observations missing'))

    def evidence_matches(record, claim):
        keys = record.get('evidence_ids')
        return (strings(keys) and all(k in verified for k in keys) and
                any(verified[k]['target_id'] == claim['target_id'] and
                    verified[k]['kind'] == claim['kind'] for k in keys))

    def current_observation(record):
        keys = record.get('evidence_ids')
        return (all(record.get(k) == run[k] for k in ('snapshot', 'run_id', 'build_id')) and
                strings(keys) and all(k in verified for k in keys) and
                record.get('evidence_hash') == capture_binding(verified.values(), keys))

    grouped = {key: [] for key in REVIEWERS}
    claims = {c['id']: c for c in bundle['matrix']['claims']}
    findings = rows(critic.get('findings', []), 'critic.findings', errors, False)
    repairs = rows(manifest.get('repairs', []), 'repairs', errors, False)
    resolutions = rows(manifest.get('resolutions', []), 'resolutions', errors, False)
    ids(resolutions, 'resolutions', errors)
    invalid_active = False
    for item in items:
        if item.get('snapshot') == current and item.get('target_id') not in targets:
            errors.append(issue('UNKNOWN_TARGET', str(item.get('id'))))
            invalid_active = True
    for review in reviews:
        if review.get('snapshot') == current and (review.get('claim_id') not in claims or
                review.get('verdict') not in VERDICTS or not text(review.get('reviewer'))):
            errors.append(issue('INVALID_REVIEW', str(review.get('id'))))
            invalid_active = True
    failure_ids = {r['id'] for r in reviews if r.get('verdict') == 'FAIL'}
    failure_ids.update(f.get('id', f'finding:{i}') for i, f in enumerate(findings) if f.get('verdict') == 'FAIL')
    failure_ids.update(r.get('id', f'repair:{i}') for i, r in enumerate(repairs) if r.get('outcome') != 'IMPROVED')
    failures = {r['id']: r for r in reviews if r.get('verdict') == 'FAIL'}
    failures.update({f.get('id', f'finding:{i}'): f for i, f in enumerate(findings) if f.get('verdict') == 'FAIL'})

    def resolution_matches(resolution, links):
        for link in links:
            failure = failures.get(link, {})
            claim = claims.get(failure.get('claim_id'))
            if claim and not evidence_matches(resolution, claim):
                return False
            if failure.get('kind') == 'structural' and not any(
                    verified[e]['kind'] == 'render' for e in resolution['evidence_ids']):
                return False
        return True

    resolved = set()
    for resolution in resolutions:
        links = resolution.get('resolves')
        if (strings(links) and set(links) <= failure_ids and text(resolution.get('observed')) and
                current_observation(resolution) and resolution_matches(resolution, links) and
                attested(resolution, host, 'resolution')):
            resolved.update(links)
        else:
            errors.append(issue('RESOLUTION_UNVERIFIED', str(resolution.get('id'))))
    report['active_findings'] = [f for i, f in enumerate(findings) if f.get('id', f'finding:{i}') not in resolved]
    if any(r.get('verdict') == 'FAIL' and r['id'] not in resolved and r.get('claim_id') not in claims for r in reviews):
        invalid_active = True
        errors.append(issue('UNRESOLVED_HISTORY', 'removed claim still has an unresolved failure'))
    active_repairs = []
    for i, repair in enumerate(repairs):
        if repair.get('id', f'repair:{i}') in resolved:
            continue
        if repair.get('outcome') == 'IMPROVED' and not (current_observation(repair) and attested(repair, host, 'repair')):
            repair = dict(repair, outcome='UNVERIFIED')
        active_repairs.append(repair)
    report['disposition'] = repair_disposition(active_repairs, report['active_findings'])
    for claim_id, claim in claims.items():
        results = []
        claim_reviews = [r for r in reviews if r.get('claim_id') == claim_id and r['id'] not in resolved]
        unresolved_failures = [r for r in claim_reviews if r.get('verdict') == 'FAIL']
        for reviewer in claim['reviewers']:
            matching = [r for r in claim_reviews if r.get('reviewer') == reviewer and current_observation(r)]
            verdict = 'UNVERIFIED'
            # Historical FAIL requires an attested resolution; historical PASS
            # is simply stale. Any consultant can report a blocking current failure.
            if unresolved_failures:
                verdict = 'FAIL'
            elif matching:
                checked = [r['verdict'] if r.get('verdict') in VERDICTS and text(r.get('observed')) and
                           text(r.get('context_id')) and evidence_matches(r, claim) and attested(r, host, 'review')
                           else 'UNVERIFIED' for r in matching]
                verdict = aggregate(checked)
            results.append(verdict)
        verdict = aggregate(results)
        report['claims'][claim_id] = verdict
        if claim['required']:
            grouped[claim['category']].append(verdict)
    for category, values in grouped.items():
        categories[category] = aggregate(values)
    for finding in report['active_findings']:
        claim = claims.get(finding.get('claim_id'), {})
        category = 'Structure' if finding.get('kind') == 'structural' else claim.get('category', finding.get('category'))
        required = claim.get('required', finding.get('required', True))
        if finding.get('claim_id') and not claim:
            invalid_active = True
            errors.append(issue('INVALID_FINDING', 'unknown claim'))
        if required:
            if category not in categories or finding.get('verdict') not in VERDICTS:
                invalid_active = True
                errors.append(issue('INVALID_FINDING', 'category/verdict required'))
            else:
                categories[category] = aggregate([categories[category], finding['verdict']])
                if category == 'Structure' and finding['verdict'] == 'FAIL':
                    categories['VisualQuality'] = 'FAIL'
    # Missing any declared interaction also blocks responsive completion, even if
    # a still-frame responsive review passed.
    if not report['proof_complete'] and categories['Responsive'] == 'PASS':
        categories['Responsive'] = 'UNVERIFIED'
    resources_ready = all(a.get('status') == 'VERIFIED' for a in intent.get('assets', []) if a.get('critical'))
    if not resources_ready:
        errors.append(issue('ASSET_UNVERIFIED', 'critical asset/font/content provisional'))
        for category in ('Craft', 'VisualQuality'):
            if categories[category] == 'PASS':
                categories[category] = 'UNVERIFIED'
    context_ids = {r.get('context_id') for r in reviews} | {run['implementation_context']}
    critic_valid = (not identity(intent, critic) and text(critic.get('context_id')) and
                    critic['context_id'] not in context_ids and current_observation(critic) and
                    attested(critic, host, 'critic'))
    report['critic_reviewed'] = bool(critic_valid)
    critic_results = critic.get('results', [])
    if not isinstance(critic_results, list) or any(not isinstance(r, dict) for r in critic_results):
        critic_results = []
        invalid_active = True
    if any(r.get('claim_id') not in claims or r.get('verdict') not in VERDICTS for r in critic_results):
        errors.append(issue('INVALID_CRITIC_RESULT', 'unknown claim or verdict'))
        invalid_active = True
    for category in ('VisualConformance', 'VisualQuality'):
        expected_claims = [c for c in claims.values() if c['category'] == category and c['required']]
        verdicts = []
        for claim in expected_claims:
            matches = [r for r in critic_results if r.get('claim_id') == claim['id']]
            if any(r.get('verdict') == 'FAIL' for r in matches):
                verdicts.append('FAIL')
            elif critic_valid and len(matches) == 1 and matches[0].get('verdict') in VERDICTS and text(
                    matches[0].get('observed')) and evidence_matches(matches[0], claim):
                verdicts.append(matches[0]['verdict'])
            else:
                verdicts.append('UNVERIFIED')
        categories[category] = aggregate([categories[category], aggregate(verdicts)])
    calibration = resolve(host, critic.get('calibration_id')) or {}
    calibrated = (calibration.get('kind') == 'calibration' and calibration.get('status') == 'IN_SCOPE' and
                  calibration.get('snapshot') == current and calibration.get('held_out') is True and
                  all(text(calibration.get(k)) for k in ('approved_by', 'evaluation_id', 'criteria_id')) and
                  calibration.get('approved_by') not in context_ids | {critic.get('context_id')})
    if not calibrated and categories['VisualQuality'] == 'PASS':
        categories['VisualQuality'] = 'UNVERIFIED'
    categories['VisualInternal'] = aggregate([categories['VisualConformance'], categories['VisualQuality']])
    acceptance = resolve(host, manifest.get('acceptance_receipt_id')) or {}
    if (acceptance.get('kind') == 'user_acceptance' and acceptance.get('actor') == 'user' and
            acceptance.get('decision') in ('APPROVE_EXACT_OUTPUT', 'REJECT_EXACT_OUTPUT') and text(acceptance.get('message')) and
            acceptance.get('snapshot') == current and acceptance.get('build_id') == run['build_id'] and
            not identity(intent, acceptance)):
        if acceptance['decision'] == 'APPROVE_EXACT_OUTPUT':
            report['user_acceptance'] = 'APPROVED'
        else:
            report['user_acceptance'] = 'REJECTED'
            report['disposition'] = 'MATERIAL_REWORK_REQUIRED'
    report['approved'] = (not invalid_active and report['disposition'] == 'CONTINUE' and
                          report['proof_complete'] and all(v == 'PASS' for v in categories.values()) and
                          report['user_acceptance'] == 'APPROVED')
    if invalid_active:
        report['proof_complete'] = False
    return report
