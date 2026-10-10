"""Check grounded, scoped decisions. Text presence is not proof of good design."""
import re

IDENTITY = ('candidate_id', 'revision', 'scope_id')
AXES = {'composition', 'interaction', 'mobile', 'typography', 'spacing', 'imagery',
        'color', 'motion', 'icons', 'states'}


def issue(code, detail):
    return {'code': code, 'detail': detail}


def text(value):
    return isinstance(value, str) and bool(value.strip())


def strings(value, nonempty=True):
    return isinstance(value, list) and (bool(value) or not nonempty) and all(text(v) for v in value)


def rows(value, name, errors, nonempty=True):
    if not isinstance(value, list) or (nonempty and not value) or any(not isinstance(v, dict) for v in value):
        errors.append(issue('INVALID_ARTIFACT', f'{name} must be a list of objects'))
        return []
    return value


def ids(items, name, errors):
    result = []
    for item in items:
        value = item.get('id')
        if not text(value):
            errors.append(issue('INVALID_ID', name))
        elif value in result:
            errors.append(issue('DUPLICATE_ID', f'{name}: {value}'))
        else:
            result.append(value)
    return set(result)


def identity(intent, other):
    return [issue('IDENTITY_MISMATCH', key) for key in IDENTITY
            if not text(intent.get(key)) or intent.get(key) != other.get(key)]


def validate_intent(intent):
    if not isinstance(intent, dict):
        return [issue('INVALID_ARTIFACT', 'intent must be object')]
    errors = identity(intent, intent)
    if not text(intent.get('product_source')):
        errors.append(issue('NEEDS_PRODUCT_INPUT', 'product_source required'))
    requirements = rows(intent.get('requirements'), 'requirements', errors)
    ids(requirements, 'requirements', errors)
    for row in requirements:
        if row.get('kind') not in ('content', 'action', 'state') or not text(row.get('description')):
            errors.append(issue('NEEDS_PRODUCT_INPUT', 'requirement kind/description missing'))
    constraints = rows(intent.get('constraints'), 'constraints', errors, False)
    ids(constraints, 'constraints', errors)
    for row in constraints:
        if not text(row.get('description')):
            errors.append(issue('NEEDS_PRODUCT_INPUT', 'constraint description missing'))
    axes = intent.get('required_axes')
    if not strings(axes) or not set(axes) <= AXES or 'composition' not in axes:
        errors.append(issue('INVALID_ARTIFACT', 'required_axes must include composition and known axes'))
    targets = rows(intent.get('targets'), 'targets', errors)
    ids(targets, 'targets', errors)
    for target in targets:
        size = target.get('viewport')
        good_size = isinstance(size, list) and len(size) == 2 and all(type(v) is int and v > 0 for v in size)
        kinds = target.get('required_kinds')
        if (not good_size or any(not text(target.get(k)) for k in
                ('route', 'surface', 'family', 'state', 'theme', 'locale')) or
                not strings(kinds) or not set(kinds) <= {'render', 'interaction', 'technical'}):
            errors.append(issue('INVALID_TARGET', str(target.get('id'))))
    return errors


def validate_lock(intent, lock):
    errors = identity(intent, lock)
    refs = rows(lock.get('references'), 'references', errors, False)
    ids(refs, 'references', errors)
    if sum(r.get('role') == 'primary' for r in refs) != 1:
        errors.append(issue('REFERENCE_INSUFFICIENT', 'exactly one Primary required'))
    if sum(r.get('role') == 'secondary' for r in refs) > 2:
        errors.append(issue('REFERENCE_LOCK_CONFLICT', 'at most two Secondary references'))
    targets = {r['id'] for r in intent.get('targets', [])}
    owners = {}
    for ref in refs:
        if ref.get('role') not in ('primary', 'secondary'):
            errors.append(issue('REFERENCE_LOCK_CONFLICT', 'unknown reference role'))
        owns = ref.get('owns')
        if not strings(owns) or not set(owns) <= AXES:
            errors.append(issue('REFERENCE_LOCK_CONFLICT', 'invalid ownership axes'))
            owns = []
        for axis in owns:
            if axis in owners:
                errors.append(issue('REFERENCE_LOCK_CONFLICT', f'two owners for {axis}'))
            owners[axis] = ref.get('id')
        for field in ('take', 'do_not_take', 'applies_to'):
            if not strings(ref.get(field)):
                errors.append(issue('REFERENCE_INCOMPLETE', field))
        if not strings(ref.get('unknown'), False):
            errors.append(issue('REFERENCE_INCOMPLETE', 'unknown must be explicit list'))
        if strings(ref.get('applies_to')) and not set(ref['applies_to']) <= targets:
            errors.append(issue('UNKNOWN_TARGET', str(ref.get('id'))))
        observation = ref.get('observation', {})
        if not isinstance(observation, dict) or observation.get('kind') not in ('render', 'interaction') or any(
                not text(observation.get(k)) for k in ('pointer', 'description')):
            errors.append(issue('REFERENCE_UNINSPECTED', str(ref.get('id'))))
        if not text(ref.get('source')) or not re.fullmatch('[0-9a-f]{64}', str(ref.get('source_sha256', ''))):
            errors.append(issue('REFERENCE_INCOMPLETE', 'source and SHA256 required'))
    if not set(intent.get('required_axes', [])) <= set(owners):
        errors.append(issue('REFERENCE_INCOMPLETE', 'required axis has no owner'))
    return errors


def validate_contract(intent, lock, contract):
    errors = identity(intent, contract)
    requirements = {r['id'] for r in intent.get('requirements', [])}
    constraints = {r['id'] for r in intent.get('constraints', [])}
    targets = {r['id'] for r in intent.get('targets', [])}
    refs = {r['id']: r for r in lock.get('references', [])}
    invariants = contract.get('product_invariants')
    if not strings(invariants) or set(invariants) != requirements:
        errors.append(issue('PRODUCT_MUTATION', 'all product requirements must be preserved'))
    reference_ids = contract.get('reference_ids')
    if not strings(reference_ids) or set(reference_ids) != set(refs):
        errors.append(issue('REFERENCE_LOCK_CONFLICT', 'contract reference set differs from lock'))
    patterns = contract.get('patterns')
    if not strings(patterns, False):
        errors.append(issue('INVALID_ARTIFACT', 'patterns must be list'))
    elif set(patterns) & set(intent.get('rejected_patterns', [])):
        errors.append(issue('AUTHORITY_CONFLICT', 'rejected grammar reused'))
    if not strings(contract.get('structure_claims')):
        errors.append(issue('STRUCTURE_PROOF_REQUIRED', 'early structural claims missing'))
    translations = rows(contract.get('translations'), 'translations', errors)
    ids(translations, 'translations', errors)
    covered, covered_constraints, axes = set(), set(), set()
    for row in translations:
        ref = refs.get(row.get('reference_id'), {})
        axis = row.get('axis')
        if not text(axis) or axis not in ref.get('owns', []):
            errors.append(issue('REFERENCE_LOCK_CONFLICT', 'translation not owned by selected reference'))
        else:
            axes.add(axis)
        linked = row.get('requirement_ids')
        if not strings(linked):
            errors.append(issue('PRODUCT_GROUNDING_MISSING', str(row.get('id'))))
        else:
            covered.update(linked)
            if not set(linked) <= requirements:
                errors.append(issue('UNKNOWN_REQUIREMENT', str(row.get('id'))))
        linked_constraints = row.get('constraint_ids')
        if not strings(linked_constraints, False) or not set(linked_constraints) <= constraints:
            errors.append(issue('UNKNOWN_CONSTRAINT', str(row.get('id'))))
        else:
            covered_constraints.update(linked_constraints)
        for field in ('source_observation', 'rationale', 'spatial_rule', 'responsive_rule', 'expected', 'falsifier'):
            if not text(row.get(field)):
                errors.append(issue('SYNTHESIS_INCOMPLETE', f'{row.get("id")}: {field}'))
        implementation = row.get('implementation')
        if not isinstance(implementation, dict) or any(not text(implementation.get(k)) for k in ('component', 'selector')):
            errors.append(issue('SYNTHESIS_INCOMPLETE', 'implementation component/selector required'))
        applicable = row.get('target_ids')
        if not strings(applicable) or not set(applicable) <= targets or not set(applicable) <= set(ref.get('applies_to', [])):
            errors.append(issue('UNKNOWN_TARGET', str(row.get('id'))))
        if row.get('source_kind') not in ('render', 'interaction'):
            errors.append(issue('REFERENCE_UNINSPECTED', 'translation needs observed source kind'))
        motion = row.get('motion')
        if axis in ('interaction', 'motion') or motion is not None:
            if not isinstance(motion, dict) or any(not text(motion.get(k)) for k in
                    ('trigger', 'start', 'end', 'interrupt', 'reduced')) or motion.get('origin') not in ('proposed', 'observed'):
                errors.append(issue('SYNTHESIS_INCOMPLETE', 'interaction needs trigger/start/end/interruption/reduced rules'))
            elif motion['origin'] == 'observed' and (row.get('source_kind') != 'interaction' or
                    ref.get('observation', {}).get('kind') != 'interaction'):
                errors.append(issue('MOTION_EVIDENCE_MISSING', 'still source cannot establish observed motion'))
    if not requirements <= covered or not constraints <= covered_constraints:
        errors.append(issue('PRODUCT_GROUNDING_MISSING', 'content/actions/constraints not translated'))
    if not set(intent.get('required_axes', [])) <= axes:
        errors.append(issue('AXIS_TRANSLATION_MISSING', 'required structural/interaction axis missing'))
    return errors


def guard_change(intent, contract, change):
    errors = []
    if change.get('product_mutation') or change.get('ownership_mutation'):
        errors.append(issue('AUTHORITY_CONFLICT', 'change mutates product or reference ownership'))
    changed = change.get('changed_axes', [])
    if change.get('role') == 'craft' and set(changed) & {'composition', 'imagery', 'color', 'interaction'}:
        errors.append(issue('CRAFT_SCOPE_VIOLATION', 'material axes require synthesis, not craft'))
    for field, target_field in [('routes', 'route'), ('families', 'family')]:
        allowed = {t[target_field] for t in intent['targets']}
        if not set(change.get(field, [])) <= allowed:
            errors.append(issue('SCOPE_EXPANSION_REQUIRED', field))
    for selector in change.get('selectors', []):
        if re.search(r'\.(?:text|bg)-|!important', selector):
            errors.append(issue('SHARED_SELECTOR_REVIEW', selector))
    return errors
