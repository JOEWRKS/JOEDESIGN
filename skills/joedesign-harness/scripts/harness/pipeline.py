"""Scoped state transitions and role input bundles."""
import copy
from datetime import datetime, timezone
from pathlib import Path
from .io import digest, read_artifact, write_artifact
from .contracts import validate_intent, validate_lock, validate_contract
from .evidence import assess, snapshot, validate_matrix, repair_disposition

ARTIFACTS = {'intent': 'DESIGN_INTENT.json', 'candidates': 'REFERENCE_CANDIDATES.json',
             'lock': 'REFERENCE_LOCK.md', 'contract': 'DESIGN_CONTRACT.md',
             'matrix': 'STATE_MATRIX.md', 'critique': 'CRITIQUE.md',
             'evidence': 'EVIDENCE_MANIFEST.json'}
STAGES = ['DRAFT', 'INTENT_READY', 'REFERENCES_FOUND', 'REFERENCE_LOCKED', 'CONTRACT_READY',
          'IMPLEMENTED', 'CRAFTED', 'PROOF_COMPLETE', 'CRITIC_REVIEWED', 'APPROVED']


def load_bundle(root):
    return {key: read_artifact(Path(root) / name) for key, name in ARTIFACTS.items()}


def init_bundle(root, intent):
    errors = validate_intent(intent)
    if errors:
        raise ValueError(str(errors))
    root = Path(root)
    if root.exists() and any(root.iterdir()):
        raise FileExistsError('initialization requires a new or empty artifact directory')
    identity = {k: intent[k] for k in ('candidate_id', 'revision', 'scope_id')}
    package = Path(__file__).resolve().parents[2]
    bundle = {}
    for key, name in ARTIFACTS.items():
        data = read_artifact(package / 'templates' / name)
        data.update(identity)
        if key == 'intent':
            data = intent
        elif key == 'matrix':
            data['targets'] = copy.deepcopy(intent['targets'])
        elif key == 'evidence':
            data['run'].update(identity)
        bundle[key] = data
    # Read/validate all templates before making any writes.
    for key, name in ARTIFACTS.items():
        write_artifact(root / name, bundle[key])
    return bundle


def bindings(bundle, stage):
    index = STAGES.index(stage)
    keys = ['intent']
    if index >= STAGES.index('REFERENCES_FOUND'):
        keys.append('lock')
    if index >= STAGES.index('CONTRACT_READY'):
        keys += ['contract', 'matrix']
    result = {k: digest(bundle[k]) for k in keys}
    if index >= STAGES.index('IMPLEMENTED'):
        result['run'] = digest(bundle['evidence'].get('run', {}))
    if index >= STAGES.index('PROOF_COMPLETE'):
        result['items'] = digest(bundle['evidence'].get('items', []))
        result['reviews'] = digest(bundle['evidence'].get('reviews', []))
    if index >= STAGES.index('CRITIC_REVIEWED'):
        result['critique'] = digest(bundle['critique'])
    return result


def current_stage(bundle):
    stage = 'DRAFT'
    for event in bundle['evidence'].get('history', []):
        target = event.get('to')
        if target in ('USER_REVIEW', 'REWORK'):
            if target == 'REWORK':
                stage = 'DRAFT'
            continue
        if target not in STAGES or STAGES.index(target) != STAGES.index(stage) + 1:
            continue
        if event.get('from') == stage and event.get('bindings') == bindings(bundle, target):
            stage = target
    return stage


def contract_errors(bundle):
    errors = validate_intent(bundle['intent'])
    if not errors:
        errors += validate_lock(bundle['intent'], bundle['lock'])
    if not errors:
        errors += validate_contract(bundle['intent'], bundle['lock'], bundle['contract'])
    return errors


def transition(bundle, target, host=None):
    stage = current_stage(bundle)
    report = assess(bundle, host)
    disposition = report['disposition']
    if target in ('CRAFTED', 'APPROVED') and (disposition != 'CONTINUE' or report['categories']['Structure'] == 'FAIL'):
        raise ValueError('MATERIAL_REWORK_REQUIRED: unresolved structure/repair must return to synthesis')
    if target not in ('USER_REVIEW', 'REWORK'):
        if target not in STAGES or STAGES.index(target) != STAGES.index(stage) + 1:
            raise ValueError(f'invalid transition {stage} -> {target}')
        errors = validate_intent(bundle['intent'])
        if STAGES.index(target) >= STAGES.index('REFERENCES_FOUND'):
            refs = bundle['lock'].get('references', [])
            if not refs or any(not r.get('observation', {}).get('pointer') for r in refs):
                errors.append({'code': 'REFERENCE_UNINSPECTED'})
        if STAGES.index(target) >= STAGES.index('REFERENCE_LOCKED'):
            errors += validate_lock(bundle['intent'], bundle['lock'])
        if STAGES.index(target) >= STAGES.index('CONTRACT_READY'):
            errors += contract_errors(bundle)
            if not errors:
                errors += validate_matrix(bundle)
        if errors:
            raise ValueError(str(errors))
        if target == 'IMPLEMENTED' and (bundle['evidence'].get('run', {}).get('snapshot') != snapshot(bundle) or
                                        not bundle['evidence'].get('items')):
            raise ValueError('IMPLEMENTATION_UNVERIFIED: current run and actual output records required')
        if target == 'CRAFTED' and not any(r.get('reviewer') == 'I' for r in bundle['evidence'].get('reviews', [])):
            raise ValueError('CRAFT_UNVERIFIED: craft observations required')
        if target in ('PROOF_COMPLETE', 'CRITIC_REVIEWED', 'APPROVED') and not report['proof_complete']:
            raise ValueError('PROOF_INCOMPLETE')
        if target in ('CRITIC_REVIEWED', 'APPROVED') and not report['critic_reviewed']:
            raise ValueError('CRITIC_UNVERIFIED')
        if target == 'APPROVED' and not report['approved']:
            raise ValueError('APPROVAL_BLOCKED: required gates and exact user event needed')
    manifest = copy.deepcopy(bundle['evidence'])
    event = {'from': stage, 'to': target, 'at': datetime.now(timezone.utc).isoformat(),
             'bindings': bindings(bundle, target) if target in STAGES else {},
             'report_status': report['categories']}
    manifest.setdefault('history', []).append(event)
    return manifest


def make_role_bundle(bundle, role, host=None):
    if role not in ('synthesis', 'craft', 'critic', 'expand'):
        raise ValueError('unknown role')
    errors = validate_intent(bundle['intent']) + validate_lock(bundle['intent'], bundle['lock'])
    if role != 'synthesis':
        errors += contract_errors(bundle)
    if errors:
        raise ValueError(str(errors))
    if role in ('craft', 'expand'):
        report = assess(bundle, host)
        disposition = report['disposition']
        if disposition != 'CONTINUE' or report['categories']['Structure'] == 'FAIL':
            raise ValueError('MATERIAL_REWORK_REQUIRED: stop polishing and diagnose structure')
    if role == 'expand':
        report = assess(bundle, host)
        if report['categories']['Structure'] != 'PASS' or not report['proof_complete']:
            raise ValueError('STRUCTURE_PROOF_REQUIRED: do not expand or polish a failed structure')
    result = {'role': role, 'intent': copy.deepcopy(bundle['intent']), 'lock': copy.deepcopy(bundle['lock'])}
    if role != 'synthesis':
        contract = bundle['contract']
        # Whitelist critic inputs; do not pass arbitrary builder notes or scores.
        result['contract'] = {k: copy.deepcopy(contract[k]) for k in
                              ('candidate_id', 'revision', 'scope_id', 'product_invariants', 'reference_ids',
                               'patterns', 'structure_claims', 'protected_regions', 'translations') if k in contract}
        if role == 'critic':
            allowed = {'id', 'reference_id', 'axis', 'requirement_ids', 'constraint_ids', 'source_observation',
                       'source_kind', 'spatial_rule', 'responsive_rule', 'implementation', 'expected',
                       'falsifier', 'target_ids', 'motion'}
            result['contract']['translations'] = [{k: v for k, v in row.items() if k in allowed}
                                                  for row in result['contract'].get('translations', [])]
            result['matrix'] = copy.deepcopy(bundle['matrix'])
            result['captures'] = copy.deepcopy(bundle['evidence'].get('items', []))
            result['instruction'] = 'Fresh context: inspect original and actual captures; diagnose each claim. No new direction or self-score.'
        elif role == 'craft':
            result['instruction'] = 'Refine local type/spacing/states within locked relationships. Material structure failure returns to synthesis immediately.'
    else:
        result['instruction'] = 'Use JOEDESIGN with original sources. Map every required content/action/constraint to concrete spatial, responsive and interaction rules. No brand/style copying as rationale.'
    return result


def validate_handoff(bundle, proposed, host=None):
    actual = assess(bundle, host)
    if proposed != actual:
        raise ValueError('HANDOFF_EXCEEDS_EVIDENCE: use the generated report without promoting states')
    return actual
