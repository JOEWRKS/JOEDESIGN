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


if __name__ == '__main__':
    unittest.main()
