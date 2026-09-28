import copy
import tempfile
import unittest
from pathlib import Path
from harness_support import module, proof_bundle


class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.api = module(self, 'evidence')
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.b, self.host = proof_bundle(self.tmp.name)

    def test_verified_contract_service_can_close_exact_scope(self):
        report = self.api.assess(self.b, self.host)
        self.assertTrue(report['proof_complete'])
        self.assertEqual(report['categories']['VisualInternal'], 'PASS')
        self.assertEqual(report['user_acceptance'], 'APPROVED')
        self.assertTrue(report['approved'])

    def test_local_receipt_json_cannot_authenticate_itself(self):
        report = self.api.assess(self.b)
        self.assertFalse(report['proof_complete'])
        self.assertEqual(report['user_acceptance'], 'PENDING')
        self.assertEqual(report['categories']['VisualInternal'], 'UNVERIFIED')

    def test_f4_desktop_only_leaves_responsive_unverified(self):
        self.b['evidence']['items'] = [e for e in self.b['evidence']['items'] if e['target_id'] == 'wide']
        self.assertEqual(self.api.assess(self.b, self.host)['categories']['Responsive'], 'UNVERIFIED')

    def test_f5_png_does_not_prove_interaction(self):
        self.b['evidence']['items'] = [e for e in self.b['evidence']['items'] if e['kind'] == 'render']
        report = self.api.assess(self.b, self.host)
        self.assertFalse(report['proof_complete'])
        self.assertEqual(report['categories']['Accessibility'], 'UNVERIFIED')

    def test_f6_required_matrix_row_cannot_be_removed(self):
        self.b['matrix']['targets'].pop()
        self.assertFalse(self.api.assess(self.b, self.host)['proof_complete'])

    def test_f7_critic_failure_dominates_other_passes(self):
        self.b['critique']['results'][0]['verdict'] = 'FAIL'
        self.assertEqual(self.api.assess(self.b, self.host)['categories']['VisualInternal'], 'FAIL')

    def test_f8_no_critic_cannot_pass(self):
        self.b['critique'] = {}
        self.assertEqual(self.api.assess(self.b, self.host)['categories']['VisualInternal'], 'UNVERIFIED')

    def test_f9_implementation_permission_not_exact_acceptance(self):
        self.host.records['acceptance']['decision'] = 'PROCEED'
        self.host.records['acceptance']['message'] = 'ㄱㄱ'
        self.assertEqual(self.api.assess(self.b, self.host)['user_acceptance'], 'PENDING')

    def test_f12_technical_success_without_images_is_not_visual_pass(self):
        self.b['evidence']['items'] = []
        self.b['evidence']['technical'] = {'build': 'PASS'}
        self.assertEqual(self.api.assess(self.b, self.host)['categories']['VisualInternal'], 'UNVERIFIED')

    def test_tampered_bytes_and_fake_receipt_rejected(self):
        Path(self.b['evidence']['items'][0]['path']).write_text('changed', encoding='utf-8')
        self.assertFalse(self.api.assess(self.b, self.host)['proof_complete'])

    def test_target_state_and_candidate_mixing_rejected(self):
        for key, value in [('state', 'default'), ('viewport', [1280, 720])]:
            b = copy.deepcopy(self.b)
            b['evidence']['items'][0]['target'][key] = value
            self.assertFalse(self.api.assess(b, self.host)['proof_complete'])
        self.b['evidence']['run']['candidate_id'] = 'B'
        self.assertFalse(self.api.assess(self.b, self.host)['approved'])

    def test_missing_secondary_review_and_self_critic_do_not_pass(self):
        self.b['evidence']['reviews'] = [r for r in self.b['evidence']['reviews'] if r['reviewer'] != 'I']
        self.assertEqual(self.api.assess(self.b, self.host)['categories']['Craft'], 'UNVERIFIED')
        self.b['critique']['context_id'] = 'builder'
        self.assertEqual(self.api.assess(self.b, self.host)['categories']['VisualInternal'], 'UNVERIFIED')

    def test_calibration_and_quality_affect_internal_not_actual_user_event(self):
        del self.host.records['calibration']
        report = self.api.assess(self.b, self.host)
        self.assertEqual(report['categories']['VisualInternal'], 'UNVERIFIED')
        self.assertEqual(report['user_acceptance'], 'APPROVED')
        self.assertFalse(report['approved'])

    def test_asset_change_invalidates_entire_snapshot(self):
        self.b['intent']['assets'] = [{'id': 'hero', 'status': 'PROVISIONAL', 'critical': True}]
        self.assertFalse(self.api.assess(self.b, self.host)['approved'])

    def test_unknown_verdict_and_duplicate_evidence_fail_closed(self):
        self.b['evidence']['reviews'][0]['verdict'] = 'probably'
        self.assertFalse(self.api.assess(self.b, self.host)['approved'])
        self.b['evidence']['items'].append(copy.deepcopy(self.b['evidence']['items'][0]))
        self.assertFalse(self.api.assess(self.b, self.host)['proof_complete'])

    def test_new_build_cannot_reuse_old_review_receipts_with_same_evidence_ids(self):
        self.b['evidence']['run'].update(run_id='run-2', build_id='build-2')
        for item in self.b['evidence']['items']:
            item.update(run_id='run-2', build_id='build-2')
            self.host.records[item['receipt_id']] = copy.deepcopy(item) | {'kind': 'capture', 'evidence_kind': item['kind']}
        self.host.records['acceptance']['build_id'] = 'build-2'
        report = self.api.assess(self.b, self.host)
        self.assertFalse(report['approved'])
        self.assertEqual(report['categories']['VisualInternal'], 'UNVERIFIED')

    def test_changed_capture_bytes_in_same_run_invalidate_old_reviews(self):
        import hashlib
        item = self.b['evidence']['items'][0]
        Path(item['path']).write_text('Different actual content', encoding='utf-8')
        item['sha256'] = hashlib.sha256(Path(item['path']).read_bytes()).hexdigest()
        self.host.records[item['receipt_id']] = copy.deepcopy(item) | {'kind': 'capture', 'evidence_kind': item['kind']}
        self.assertFalse(self.api.assess(self.b, self.host)['approved'])

    def test_structural_findings_block_assessment_not_only_transition(self):
        self.b['critique']['findings'] = [{'kind': 'structural', 'verdict': 'FAIL', 'reason': 'task flow absent'}]
        self.host.records['critic'] = copy.deepcopy(self.b['critique']) | {'kind': 'critic'}
        report = self.api.assess(self.b, self.host)
        self.assertFalse(report['approved'])
        self.assertEqual(report['categories']['Structure'], 'FAIL')

    def test_technical_only_cannot_replace_visual_or_interaction_requirements(self):
        from harness_support import canonical_hash
        for target in self.b['intent']['targets']:
            target['required_kinds'] = ['technical']
        self.b['matrix']['targets'] = copy.deepcopy(self.b['intent']['targets'])
        for claim in self.b['matrix']['claims']:
            claim['kind'] = 'technical'
        self.b['matrix']['bindings'] = {k: canonical_hash(self.b[k]) for k in ('intent', 'lock', 'contract')}
        errors = self.api.validate_matrix(self.b)
        self.assertTrue(errors, 'Visual gates must demand their own evidence kinds')

    def test_contract_structure_claim_cannot_be_made_optional(self):
        row = next(c for c in self.b['matrix']['claims'] if c['id'] == 'structure')
        row['required'] = False
        replacement = copy.deepcopy(row)
        replacement.update(id='generic-structure', required=True)
        self.b['matrix']['claims'].append(replacement)
        self.assertTrue(self.api.validate_matrix(self.b))

    def test_historical_pass_does_not_duplicate_current_review(self):
        old = copy.deepcopy(self.b['evidence']['reviews'][0])
        old.update(id='old-pass', snapshot='old-snapshot', run_id='old-run', build_id='old-build')
        self.b['evidence']['reviews'].append(old)
        self.assertTrue(self.api.assess(self.b, self.host)['approved'])

    def test_historical_failure_requires_attested_current_resolution(self):
        old = copy.deepcopy(self.b['evidence']['reviews'][0])
        old.update(id='old-fail', snapshot='old-snapshot', run_id='old-run', build_id='old-build', verdict='FAIL')
        self.b['evidence']['reviews'].append(old)
        self.assertFalse(self.api.assess(self.b, self.host)['approved'])
        current = self.b['evidence']['reviews'][0]
        resolution = {k: copy.deepcopy(current[k]) for k in ('snapshot', 'run_id', 'build_id', 'evidence_hash', 'evidence_ids')}
        resolution.update(id='resolution-1', receipt_id='resolution-1', resolves=['old-fail'], observed='Retested corrected output')
        self.b['evidence']['resolutions'] = [resolution]
        self.assertFalse(self.api.assess(self.b, self.host)['approved'])
        self.host.records['resolution-1'] = copy.deepcopy(resolution) | {'kind': 'resolution'}
        self.assertTrue(self.api.assess(self.b, self.host)['approved'])
        self.assertEqual(self.b['evidence']['reviews'][-1]['verdict'], 'FAIL')

    def test_other_consultant_failure_cannot_be_ignored(self):
        claim = next(r for r in self.b['evidence']['reviews'] if r['claim_id'] == 'structure')
        additional = copy.deepcopy(claim)
        additional.update(id='extra-V', reviewer='V', verdict='FAIL', receipt_id='extra-V')
        self.b['evidence']['reviews'].append(additional)
        self.host.records['extra-V'] = copy.deepcopy(additional) | {'kind': 'review'}
        self.assertFalse(self.api.assess(self.b, self.host)['approved'])

    def test_dangling_active_records_block_assessment(self):
        for collection, key in [('items', 'target_id'), ('reviews', 'claim_id')]:
            b = copy.deepcopy(self.b)
            bad = copy.deepcopy(b['evidence'][collection][0])
            bad.update(id='dangling')
            bad[key] = 'nonexistent'
            b['evidence'][collection].append(bad)
            self.assertFalse(self.api.assess(b, self.host)['approved'])
        self.b['critique']['results'].append({'claim_id': 'nonexistent', 'verdict': 'FAIL'})
        self.host.records['critic'] = copy.deepcopy(self.b['critique']) | {'kind': 'critic'}
        self.assertFalse(self.api.assess(self.b, self.host)['approved'])

    def test_structural_failure_resolution_requires_structural_evidence(self):
        finding = {'id': 'structure-fail', 'kind': 'structural', 'verdict': 'FAIL'}
        self.b['critique']['findings'] = [finding]
        self.host.records['critic'] = copy.deepcopy(self.b['critique']) | {'kind': 'critic'}
        technical = self.b['evidence']['reviews'][0]
        resolution = {k: copy.deepcopy(technical[k]) for k in ('snapshot', 'run_id', 'build_id', 'evidence_hash', 'evidence_ids')}
        resolution.update(id='resolution-1', receipt_id='resolution-1', resolves=['structure-fail'], observed='Retested')
        self.b['evidence']['resolutions'] = [resolution]
        self.host.records['resolution-1'] = copy.deepcopy(resolution) | {'kind': 'resolution'}
        self.assertFalse(self.api.assess(self.b, self.host)['approved'])
        structure_review = next(r for r in self.b['evidence']['reviews'] if r['claim_id'] == 'structure')
        for key in ('evidence_ids', 'evidence_hash'):
            resolution[key] = copy.deepcopy(structure_review[key])
        self.host.records['resolution-1'] = copy.deepcopy(resolution) | {'kind': 'resolution'}
        self.assertTrue(self.api.assess(self.b, self.host)['approved'])
        self.assertEqual(self.b['critique']['findings'], [finding])


if __name__ == '__main__':
    unittest.main()
