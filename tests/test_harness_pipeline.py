import copy
import tempfile
import unittest
from harness_support import module, proof_bundle


class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.api = module(self, 'pipeline')
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.b, self.host = proof_bundle(self.tmp.name)

    def test_cannot_skip_contract_to_implementation(self):
        with self.assertRaisesRegex(ValueError, 'transition'):
            self.api.transition(self.b, 'IMPLEMENTED', self.host)

    def test_user_review_allowed_early_without_fabricating_prior_stages(self):
        result = self.api.transition(self.b, 'USER_REVIEW')
        self.assertEqual(result['history'][-1]['to'], 'USER_REVIEW')
        self.assertEqual(self.api.current_stage(self.b), 'DRAFT')

    def test_complete_scoped_transition_chain_and_stale_contract(self):
        for stage in self.api.STAGES[1:]:
            self.b['evidence'] = self.api.transition(self.b, stage, self.host)
        self.assertEqual(self.api.current_stage(self.b), 'APPROVED')
        self.b['contract']['translations'][0]['spatial_rule'] = 'changed composition'
        self.assertNotEqual(self.api.current_stage(self.b), 'APPROVED')

    def test_structural_fail_stops_first_attempt_without_local_polish(self):
        self.assertEqual(self.api.repair_disposition([], [{'kind': 'structural', 'verdict': 'FAIL'}]), 'MATERIAL_REWORK_REQUIRED')

    def test_structural_failure_blocks_craft_bundle_and_stage(self):
        self.b['critique']['findings'] = [{'kind': 'structural', 'verdict': 'FAIL'}]
        with self.assertRaisesRegex(ValueError, 'REWORK'):
            self.api.make_role_bundle(self.b, 'craft', self.host)
        for stage in self.api.STAGES[1:6]:
            self.b['evidence'] = self.api.transition(self.b, stage, self.host)
        with self.assertRaisesRegex(ValueError, 'REWORK'):
            self.api.transition(self.b, 'CRAFTED', self.host)

    def test_two_same_root_failures_trigger_rework_and_no_hypothesis_stops(self):
        attempts = [{'cause_id': 'density', 'outcome': 'FAIL', 'hypothesis': 'change gap'},
                    {'cause_id': 'density', 'outcome': 'FAIL', 'hypothesis': 'change gap again'}]
        self.assertEqual(self.api.repair_disposition(attempts, []), 'MATERIAL_REWORK_REQUIRED')
        self.assertEqual(self.api.repair_disposition([{'cause_id': 'density', 'outcome': 'FAIL', 'hypothesis': ''}], []), 'UNRESOLVED')

    def test_later_observed_improvement_can_close_prior_unresolved_cycle(self):
        attempts = [{'cause_id': 'density', 'outcome': 'FAIL', 'hypothesis': ''},
                    {'cause_id': 'density', 'outcome': 'IMPROVED', 'hypothesis': 'Recompose related evidence'}]
        self.assertEqual(self.api.repair_disposition(attempts, []), 'CONTINUE')

    def test_structural_proof_required_before_expansion(self):
        with self.assertRaisesRegex(ValueError, 'STRUCTURE'):
            self.api.make_role_bundle(self.b, 'expand')
        result = self.api.make_role_bundle(self.b, 'expand', self.host)
        self.assertEqual(result['role'], 'expand')

    def test_critic_bundle_excludes_implementer_rationale_and_scores(self):
        self.b['evidence']['self_score'] = 100
        self.b['contract']['builder_rationale'] = 'My design is perfect'
        result = self.api.make_role_bundle(self.b, 'critic')
        self.assertNotIn('evidence', result)
        self.assertNotIn('builder_rationale', result['contract'])
        self.assertNotIn('rationale', result['contract']['translations'][0])
        self.assertNotIn('reviews', result)

    def test_handoff_must_equal_computed_scope_and_verdicts(self):
        proposed = {'categories': {'VisualInternal': 'PASS'}, 'approved': True, 'scope': {'scope_id': 'all-routes'}}
        with self.assertRaisesRegex(ValueError, 'HANDOFF'):
            self.api.validate_handoff(self.b, proposed)


if __name__ == '__main__':
    unittest.main()
