"""Motion quality cannot be certified from successful endpoint screenshots."""
import copy
import tempfile
import unittest
from harness_support import module, proof_bundle, canonical_hash


class MotionQualityTests(unittest.TestCase):
    def setUp(self):
        self.api = module(self, 'evidence')
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.b, self.host = proof_bundle(self.tmp.name)
        self.b['intent']['required_axes'].append('motion')
        self.b['lock']['references'][0]['owns'].append('motion')
        motion = copy.deepcopy(self.b['contract']['translations'][1])
        motion.update(id='continuous-focus', axis='motion')
        self.b['contract']['translations'].append(motion)
        self.bind_matrix()

    def bind_matrix(self):
        self.b['matrix']['bindings'] = {k: canonical_hash(self.b[k]) for k in ('intent', 'lock', 'contract')}

    def add_motion_claims(self):
        for target in self.b['intent']['targets']:
            for category in ('VisualConformance', 'VisualQuality'):
                self.b['matrix']['claims'].append({
                    'id': category + '-motion-' + target['id'], 'category': category,
                    'target_id': target['id'], 'kind': 'interaction', 'required': True,
                    'translation_id': 'continuous-focus', 'reviewers': ['J', 'I'],
                    'expected': 'Continuous focus preserves the focal entity and reading pauses in both directions'})

    def codes(self):
        return {e['code'] for e in self.api.validate_matrix(self.b)}

    def test_motion_requires_visual_interaction_claims_beyond_static_claims(self):
        self.assertIn('MOTION_QUALITY_PROOF_REQUIRED', self.codes())

    def test_visual_motion_claims_are_allowed_and_complete_required_coverage(self):
        self.add_motion_claims()
        self.assertEqual(self.api.validate_matrix(self.b), [])

    def test_unrelated_interaction_claim_cannot_stand_in_for_motion_quality(self):
        self.add_motion_claims()
        self.b['matrix']['claims'][-1]['translation_id'] = 'interaction'
        self.assertIn('MOTION_QUALITY_PROOF_REQUIRED', self.codes())

    def test_motion_claims_do_not_replace_whole_screen_render_review(self):
        self.add_motion_claims()
        self.b['matrix']['claims'] = [c for c in self.b['matrix']['claims']
            if not (c['category'] == 'VisualQuality' and c['kind'] == 'render')]
        self.assertIn('VISUAL_RENDER_PROOF_REQUIRED', self.codes())

    def test_optional_motion_claim_does_not_clear_required_motion_coverage(self):
        self.add_motion_claims()
        self.b['matrix']['claims'][-1]['required'] = False
        self.assertIn('MOTION_QUALITY_PROOF_REQUIRED', self.codes())


if __name__ == '__main__':
    unittest.main()
