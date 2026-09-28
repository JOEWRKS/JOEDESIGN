import copy
import unittest
from harness_support import module, intent, lock, contract


class ContractTests(unittest.TestCase):
    def setUp(self):
        self.api = module(self, 'contracts')
        self.intent, self.lock, self.contract = intent(), lock(), contract()

    def codes(self, issues):
        return {i['code'] for i in issues}

    def test_grounded_contract_permits_proof_not_quality_pass(self):
        self.assertEqual(self.api.validate_intent(self.intent), [])
        self.assertEqual(self.api.validate_lock(self.intent, self.lock), [])
        self.assertEqual(self.api.validate_contract(self.intent, self.lock, self.contract), [])

    def test_f1_no_primary_blocks_implementation(self):
        self.lock['references'] = []
        self.assertIn('REFERENCE_INSUFFICIENT', self.codes(self.api.validate_lock(self.intent, self.lock)))

    def test_f2_same_axis_has_one_owner(self):
        other = copy.deepcopy(self.lock['references'][0])
        other.update(id='other', role='secondary')
        self.lock['references'].append(other)
        self.assertIn('REFERENCE_LOCK_CONFLICT', self.codes(self.api.validate_lock(self.intent, self.lock)))

    def test_f3_craft_cannot_change_composition(self):
        issues = self.api.guard_change(self.intent, self.contract,
                    {'role': 'craft', 'changed_axes': ['composition'], 'routes': ['/evidence'],
                     'families': ['utility'], 'product_mutation': False, 'ownership_mutation': False})
        self.assertIn('CRAFT_SCOPE_VIOLATION', self.codes(issues))

    def test_f10_css_cross_family_scope_expansion(self):
        issues = self.api.guard_change(self.intent, self.contract,
                    {'role': 'implementer', 'changed_axes': ['spacing'], 'routes': ['/evidence', '/home'],
                     'families': ['utility', 'narrative'], 'selectors': ['.text-sm']})
        self.assertIn('SCOPE_EXPANSION_REQUIRED', self.codes(issues))
        self.assertIn('SHARED_SELECTOR_REVIEW', self.codes(issues))

    def test_f11_rejected_grammar_cannot_return(self):
        self.contract['patterns'] = ['decorative-evidence']
        self.assertIn('AUTHORITY_CONFLICT', self.codes(self.api.validate_contract(self.intent, self.lock, self.contract)))

    def test_bio_decorative_reference_without_content_link_is_blocked(self):
        # Reported BIO/02 failure class; synthetic contract, not a replay of old UI.
        for row in self.contract['translations']:
            row.update(requirement_ids=[], spatial_rule='', rationale='looks like Dala',
                       expected='nice lines and panels', falsifier='')
        codes = self.codes(self.api.validate_contract(self.intent, self.lock, self.contract))
        self.assertIn('PRODUCT_GROUNDING_MISSING', codes)
        self.assertIn('SYNTHESIS_INCOMPLETE', codes)

    def test_no_interaction_rule_for_data_action_blocks_static_slide(self):
        self.contract['translations'] = self.contract['translations'][:1]
        self.assertIn('AXIS_TRANSLATION_MISSING', self.codes(self.api.validate_contract(self.intent, self.lock, self.contract)))

    def test_still_cannot_be_claimed_as_observed_motion(self):
        self.contract['translations'][1]['motion']['origin'] = 'observed'
        self.assertIn('MOTION_EVIDENCE_MISSING', self.codes(self.api.validate_contract(self.intent, self.lock, self.contract)))

    def test_lost_content_or_invented_product_requirement_blocks(self):
        self.contract['product_invariants'] = ['compare']
        self.contract['translations'][0]['requirement_ids'] = ['imaginary']
        codes = self.codes(self.api.validate_contract(self.intent, self.lock, self.contract))
        self.assertIn('PRODUCT_MUTATION', codes)
        self.assertIn('UNKNOWN_REQUIREMENT', codes)

    def test_wrong_candidate_and_unknown_target_rejected(self):
        self.lock['candidate_id'] = 'B'
        self.lock['references'][0]['applies_to'] = ['missing']
        codes = self.codes(self.api.validate_lock(self.intent, self.lock))
        self.assertIn('IDENTITY_MISMATCH', codes)
        self.assertIn('UNKNOWN_TARGET', codes)

    def test_missing_product_and_malformed_viewport_rejected(self):
        self.intent['product_source'] = ''
        self.intent['targets'][0]['viewport'] = [True, 0]
        codes = self.codes(self.api.validate_intent(self.intent))
        self.assertIn('NEEDS_PRODUCT_INPUT', codes)
        self.assertIn('INVALID_TARGET', codes)

    def test_duplicate_targets_and_ids_rejected(self):
        self.intent['targets'].append(copy.deepcopy(self.intent['targets'][0]))
        self.assertIn('DUPLICATE_ID', self.codes(self.api.validate_intent(self.intent)))

    def test_metadata_only_reference_is_not_observed(self):
        self.lock['references'][0]['observation']['kind'] = 'metadata'
        self.assertIn('REFERENCE_UNINSPECTED', self.codes(self.api.validate_lock(self.intent, self.lock)))


if __name__ == '__main__':
    unittest.main()
