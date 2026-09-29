import importlib
import sys
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / 'skills/joedesign-harness/scripts'
sys.path.insert(0, str(SCRIPTS))


def module(case, name):
    case.assertTrue((SCRIPTS / 'harness' / (name + '.py')).is_file(),
                    f'Missing implemented harness capability: {name}')
    return importlib.import_module('harness.' + name)


def intent():
    return {
        'candidate_id': 'A', 'revision': 'r1', 'scope_id': 'evidence',
        'product_source': 'PRODUCT.md#evidence',
        'requirements': [
            {'id': 'compare', 'kind': 'action', 'description': 'Compare selected evidence'},
            {'id': 'metrics', 'kind': 'content', 'description': 'Read source-backed metrics'}],
        'constraints': [{'id': 'real-data', 'description': 'No fictional results'}],
        'required_axes': ['composition', 'interaction'],
        'search_terms': ['data', 'comparison'],
        'targets': [
            {'id': 'wide', 'route': '/evidence', 'surface': 'evidence', 'family': 'utility',
             'viewport': [1440, 900], 'state': 'selected', 'theme': 'light', 'locale': 'ko',
             'required_kinds': ['render', 'interaction']},
            {'id': 'narrow', 'route': '/evidence', 'surface': 'evidence', 'family': 'utility',
             'viewport': [390, 844], 'state': 'selected', 'theme': 'light', 'locale': 'ko',
             'required_kinds': ['render', 'interaction']}],
        'assets': [], 'rejected_patterns': ['decorative-evidence'],
    }


def lock():
    return {'candidate_id': 'A', 'revision': 'r1', 'scope_id': 'evidence', 'references': [
        {'id': 'reference-data', 'role': 'primary', 'owns': ['composition', 'interaction'],
         'source': 'references/data/DESIGN.md', 'source_sha256': 'a' * 64,
         'observation': {'kind': 'render', 'pointer': 'capture/reference.png',
                         'description': 'Selecting a record reveals adjacent evidence'},
         'take': ['persistent comparison anchor'], 'do_not_take': ['brand colors'],
         'applies_to': ['wide', 'narrow'], 'unknown': ['original animation duration']} ]}


def contract():
    base = {'candidate_id': 'A', 'revision': 'r1', 'scope_id': 'evidence',
            'product_invariants': ['compare', 'metrics'], 'reference_ids': ['reference-data'],
            'patterns': ['adjacent-evidence'], 'structure_claims': ['structure'],
            'protected_regions': ['global navigation'], 'translations': []}
    for axis in ['composition', 'interaction']:
        base['translations'].append({
            'id': axis, 'reference_id': 'reference-data', 'axis': axis,
            'requirement_ids': ['compare', 'metrics'], 'constraint_ids': ['real-data'],
            'source_observation': 'Selection stays visible beside its dependent evidence',
            'source_kind': 'render', 'rationale': 'Keep comparison context during inspection',
            'spatial_rule': 'Persistent selection column adjacent to evidence detail',
            'responsive_rule': 'Stack selection before detail, preserve selected record',
            'implementation': {'component': 'EvidenceExplorer', 'selector': '[data-evidence]'},
            'expected': 'Selection and source-backed metrics remain connected',
            'falsifier': 'Changing selection leaves unrelated evidence visible',
            'target_ids': ['wide', 'narrow'],
            'motion': {'origin': 'proposed', 'trigger': 'select record', 'start': 'previous detail',
                       'end': 'selected detail', 'interrupt': 'latest selection wins',
                       'reduced': 'immediate replacement without animation'}})
    return base


def canonical_hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
                                    separators=(',', ':')).encode()).hexdigest()


class FixtureHost:
    """Synthetic receipt service for contract tests; not live host evidence."""
    def __init__(self):
        self.records = {}

    def resolve(self, receipt_id):
        return copy.deepcopy(self.records.get(receipt_id))


def proof_bundle(folder):
    b = {'intent': intent(), 'lock': lock(), 'contract': contract()}
    b['matrix'] = {k: b['intent'][k] for k in ('candidate_id', 'revision', 'scope_id')}
    b['matrix'].update(targets=copy.deepcopy(b['intent']['targets']), claims=[])
    reviewer_map = {'Technical': ['implementer'], 'Accessibility': ['V', 'U'],
                    'Responsive': ['V', 'U'], 'Craft': ['I', 'J'],
                    'Structure': ['J', 'I'], 'VisualConformance': ['J', 'I'],
                    'VisualQuality': ['J', 'I'], 'Experience': ['U', 'V']}
    for category, reviewers in reviewer_map.items():
        for target in b['intent']['targets']:
            claim_id = 'structure' if category == 'Structure' and target['id'] == 'wide' else category + '-' + target['id']
            b['matrix']['claims'].append({'id': claim_id, 'category': category, 'target_id': target['id'],
                'kind': 'technical' if category == 'Technical' else 'interaction' if category in ('Accessibility', 'Experience') else 'render',
                'required': True, 'expected': 'Expected ' + claim_id, 'reviewers': reviewers})
    b['matrix']['bindings'] = {k: canonical_hash(b[k]) for k in ('intent', 'lock', 'contract')}
    snapshot = canonical_hash({k: b[k] for k in ('intent', 'lock', 'contract', 'matrix')})
    host = FixtureHost()
    b['evidence'] = {'run': {'candidate_id': 'A', 'revision': 'r1', 'scope_id': 'evidence',
                            'run_id': 'run-1', 'implementation_context': 'builder',
                            'build_id': 'build-1', 'snapshot': snapshot},
                     'items': [], 'reviews': [], 'repairs': [], 'history': []}
    for target in b['intent']['targets']:
        for kind in ['render', 'interaction', 'technical']:
            eid = target['id'] + '-' + kind
            p = Path(folder) / (eid + '.txt')
            p.write_text('Synthetic test output ' + eid, encoding='utf-8')
            item = {'id': eid, 'target_id': target['id'], 'target': target,
                    'kind': kind, 'path': str(p), 'sha256': hashlib.sha256(p.read_bytes()).hexdigest(),
                    'receipt_id': eid, 'action': 'select second record' if kind == 'interaction' else '',
                    'result': 'selected details visible', 'run_id': 'run-1', 'build_id': 'build-1',
                    'snapshot': snapshot}
            b['evidence']['items'].append(item)
            host.records[eid] = copy.deepcopy(item) | {'kind': 'capture', 'evidence_kind': kind}
    sequence = 0
    skill_ids = {'J': 'joedesign', 'I': 'impeccable', 'U': 'ui-ux-pro-max',
                 'V': 'web-design-guidelines'}
    for claim in b['matrix']['claims']:
        for index, reviewer in enumerate(claim['reviewers']):
            review_id = claim['id'] + '-' + reviewer
            sequence += 2
            review = {'id': review_id, 'claim_id': claim['id'], 'verdict': 'PASS',
                      'observed': 'Synthetic observation', 'evidence_ids': [claim['target_id'] + '-' + claim['kind']],
                      'reviewer': reviewer, 'context_id': reviewer, 'receipt_id': review_id,
                      'snapshot': snapshot, 'raci_step': ('R', 'C1', 'C2')[index],
                      'sequence': sequence}
            review.update(run_id='run-1', build_id='build-1')
            if reviewer in skill_ids:
                review.update(skill_id=skill_ids[reviewer], skill_sha256='a' * 64,
                              skill_receipt_id=review_id + '-skill-use')
                host.records[review['skill_receipt_id']] = {
                    'kind': 'skill_use', 'reviewer': reviewer, 'skill_id': review['skill_id'],
                    'source_sha256': review['skill_sha256'], 'claim_id': claim['id'],
                    'context_id': reviewer, 'snapshot': snapshot, 'run_id': 'run-1',
                    'build_id': 'build-1', 'sequence': sequence - 1}
            review['evidence_hash'] = canonical_hash([{k: item[k] for k in
                ('id', 'target', 'kind', 'sha256', 'run_id', 'build_id', 'snapshot')}
                for item in sorted(b['evidence']['items'], key=lambda i: i['id']) if item['id'] in review['evidence_ids']])
            b['evidence']['reviews'].append(review)
            host.records[review_id] = copy.deepcopy(review) | {'kind': 'review'}
    b['critique'] = {'candidate_id': 'A', 'revision': 'r1', 'scope_id': 'evidence',
                     'context_id': 'fresh-critic', 'receipt_id': 'critic', 'snapshot': snapshot,
                     'calibration_id': 'calibration', 'results': [
                         {'claim_id': c['id'], 'verdict': 'PASS', 'observed': 'Synthetic critic observation',
                          'evidence_ids': [c['target_id'] + '-' + c['kind']]}
                         for c in b['matrix']['claims'] if c['category'] in ('VisualConformance', 'VisualQuality')]}
    b['critique'].update(run_id='run-1', build_id='build-1')
    b['critique']['evidence_ids'] = sorted({eid for row in b['critique']['results'] for eid in row['evidence_ids']})
    b['critique']['evidence_hash'] = canonical_hash([{k: item[k] for k in
        ('id', 'target', 'kind', 'sha256', 'run_id', 'build_id', 'snapshot')}
        for item in sorted(b['evidence']['items'], key=lambda i: i['id']) if item['id'] in b['critique']['evidence_ids']])
    host.records['critic'] = copy.deepcopy(b['critique']) | {'kind': 'critic'}
    host.records['calibration'] = {'kind': 'calibration', 'status': 'IN_SCOPE',
                                  'snapshot': snapshot, 'approved_by': 'design-authority',
                                  'evaluation_id': 'held-out-evaluation', 'criteria_id': 'frozen-criteria',
                                  'held_out': True}
    b['evidence']['acceptance_receipt_id'] = 'acceptance'
    host.records['acceptance'] = {'kind': 'user_acceptance', 'snapshot': snapshot,
                                  'candidate_id': 'A', 'revision': 'r1', 'scope_id': 'evidence',
                                  'decision': 'APPROVE_EXACT_OUTPUT', 'actor': 'user',
                                  'build_id': 'build-1', 'message': 'Approve this exact proof'}
    return b, host
