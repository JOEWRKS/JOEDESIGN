import importlib
import sys
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
