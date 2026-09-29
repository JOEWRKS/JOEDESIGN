"""RACI routing is ordered work with attested skill use, not a reviewer-name set."""
import copy
import tempfile
import unittest
from harness_support import canonical_hash, module, proof_bundle


class RaciExecutionTests(unittest.TestCase):
    def setUp(self):
        self.api = module(self, 'evidence')
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.bundle, self.host = proof_bundle(self.tmp.name)

    def claim(self, category='Structure'):
        return next(c for c in self.bundle['matrix']['claims'] if c['category'] == category)

    def rebind(self):
        self.bundle['matrix']['bindings'] = {
            key: canonical_hash(self.bundle[key]) for key in ('intent', 'lock', 'contract')}

    def test_existing_fixture_has_ordered_raci_proof(self):
        self.assertEqual(self.api.validate_matrix(self.bundle), [])
        self.assertTrue(self.api.assess(self.bundle, self.host)['approved'])

    def test_reversed_or_duplicate_reviewers_are_not_a_valid_route(self):
        claim = self.claim()
        claim['reviewers'] = ['I', 'J']
        self.rebind()
        self.assertIn('RACI_ORDER_REQUIRED', {e['code'] for e in self.api.validate_matrix(self.bundle)})
        claim['reviewers'] = ['J', 'J']
        self.assertIn('RACI_ORDER_REQUIRED', {e['code'] for e in self.api.validate_matrix(self.bundle)})

    def test_declared_escalation_requires_correct_third_consultant(self):
        claim = self.claim()
        claim['escalation_reason'] = 'R and C1 disagree on the observed hierarchy'
        self.rebind()
        self.assertIn('RACI_ESCALATION_REQUIRED', {e['code'] for e in self.api.validate_matrix(self.bundle)})
        claim['reviewers'].append('V')
        self.assertIn('RACI_ORDER_REQUIRED', {e['code'] for e in self.api.validate_matrix(self.bundle)})
        claim['reviewers'][-1] = 'U'
        self.assertEqual(self.api.validate_matrix(self.bundle), [])

    def test_product_action_requires_experience_owner_and_consultant(self):
        self.bundle['matrix']['claims'] = [c for c in self.bundle['matrix']['claims']
            if not (c['category'] == 'Experience' and c['target_id'] == 'wide')]
        self.assertIn('REQUIRED_CLAIM_MISSING', {e['code'] for e in self.api.validate_matrix(self.bundle)})

    def test_conditional_performance_claim_uses_its_specialist_route(self):
        claim = copy.deepcopy(self.claim('Technical'))
        claim.update(id='animation-cost', category='AnimationPerformance',
                     reviewers=['M', 'V'], expected='Offscreen animation is paused')
        self.bundle['matrix']['claims'].append(claim)
        self.assertEqual(self.api.validate_matrix(self.bundle), [])
        claim['reviewers'] = ['V', 'M']
        self.assertIn('RACI_ORDER_REQUIRED', {e['code'] for e in self.api.validate_matrix(self.bundle)})

    def test_role_label_without_skill_use_event_is_unverified(self):
        claim = self.claim()
        review = next(r for r in self.bundle['evidence']['reviews']
                      if r['claim_id'] == claim['id'] and r['reviewer'] == 'J')
        del self.host.records[review['skill_receipt_id']]
        report = self.api.assess(self.bundle, self.host)
        self.assertEqual(report['claims'][claim['id']], 'UNVERIFIED')
        self.assertFalse(report['approved'])

    def test_skill_event_for_other_source_cannot_prove_this_review(self):
        claim = self.claim()
        review = next(r for r in self.bundle['evidence']['reviews']
                      if r['claim_id'] == claim['id'] and r['reviewer'] == 'J')
        self.host.records[review['skill_receipt_id']]['source_sha256'] = 'b' * 64
        self.assertEqual(self.api.assess(self.bundle, self.host)['claims'][claim['id']], 'UNVERIFIED')

    def test_attested_consultation_before_responsible_review_does_not_pass(self):
        claim = self.claim()
        responsible = next(r for r in self.bundle['evidence']['reviews']
                           if r['claim_id'] == claim['id'] and r['reviewer'] == 'J')
        consultant = next(r for r in self.bundle['evidence']['reviews']
                          if r['claim_id'] == claim['id'] and r['reviewer'] == 'I')
        consultant['sequence'] = responsible['sequence'] - 1
        self.host.records[consultant['receipt_id']] = copy.deepcopy(consultant) | {'kind': 'review'}
        self.host.records[consultant['skill_receipt_id']]['sequence'] = consultant['sequence'] - 1
        report = self.api.assess(self.bundle, self.host)
        self.assertIn('RACI_SEQUENCE_UNVERIFIED', {e['code'] for e in report['issues']})
        self.assertEqual(report['claims'][claim['id']], 'UNVERIFIED')

    def test_attested_review_with_wrong_raci_step_does_not_pass(self):
        claim = self.claim()
        review = next(r for r in self.bundle['evidence']['reviews']
                      if r['claim_id'] == claim['id'] and r['reviewer'] == 'J')
        review['raci_step'] = 'C1'
        self.host.records[review['receipt_id']] = copy.deepcopy(review) | {'kind': 'review'}
        self.assertEqual(self.api.assess(self.bundle, self.host)['claims'][claim['id']], 'UNVERIFIED')

    def test_conflicting_attested_judgments_raise_third_consultation(self):
        claim = self.claim()
        consultant = next(r for r in self.bundle['evidence']['reviews']
                          if r['claim_id'] == claim['id'] and r['reviewer'] == 'I')
        consultant['verdict'] = 'FAIL'
        self.host.records[consultant['receipt_id']] = copy.deepcopy(consultant) | {'kind': 'review'}
        report = self.api.assess(self.bundle, self.host)
        self.assertIn(claim['id'], report['raci_escalations'])
        self.assertIn('RACI_ESCALATION_REQUIRED', {e['code'] for e in report['issues']})
        self.assertEqual(report['claims'][claim['id']], 'FAIL')


if __name__ == '__main__':
    unittest.main()
