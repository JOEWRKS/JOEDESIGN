import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from harness_support import module, proof_bundle


class FakeRunner:
    """Policy fixture, not model behavior or host attestation."""
    def __init__(self):
        self.calls = []
        self.fail_once = None
        self.conflict = False
        self.mutate_review = False
        self.repair_needed = False
        self.evidence_mode = ''
        self.persistent_failure = False
        self.fail_after_write = False
        self.controller_statuses = []
        self.skill_paths = []
        self.uncertain_quality = False

    def run(self, task, folder, project, skill_paths, images, writable):
        self.calls.append(copy.deepcopy(task))
        self.skill_paths.append(list(skill_paths))
        state = json.loads((project.parent / 'artifacts/EXECUTION_STATE.json').read_text())
        self.controller_statuses.append(state['status'])
        if task['role'] == self.fail_once:
            self.fail_once = None
            raise ValueError('simulated process failure')
        if writable:
            (project / 'result.txt').write_text('implementation ' + str(len(self.calls)))
            if self.fail_after_write:
                raise ValueError('simulated failure after partial write')
        elif self.mutate_review and task.get('raci_step'):
            (project / 'result.txt').write_text('invalid review edit')
        rows = []
        for claim in task.get('claims', []):
            verdict = 'FAIL' if (self.conflict and claim['category'] == 'Structure' and
                                 task.get('raci_step') == 'C1') else 'PASS'
            if self.uncertain_quality and claim['category'] == 'VisualQuality':
                verdict = 'UNVERIFIED'
            if self.repair_needed and claim['category'] == 'Craft' and task['role'] == 'critic' and (
                    self.persistent_failure or not any(c['role'] == 'repair' for c in self.calls)):
                verdict = 'FAIL'
            rows.append(dict(claim_id=claim['id'], verdict=verdict, observed='Synthetic scoped observation',
                evidence_ids=[i['id'] for i in task['captures'] if i['target_id'] == claim['target_id'] and i['kind'] == claim['kind']],
                cause='synthetic cause' if verdict == 'FAIL' else '', hypothesis='bounded local correction' if verdict == 'FAIL' else ''))
            if self.evidence_mode:
                ref = task['lock']['references'][0]['id']
                if self.evidence_mode == 'reference':
                    rows[-1]['evidence_ids'].append(ref)
                else:
                    rows[-1]['evidence_ids'] = [ref if self.evidence_mode == 'reference-only' else 'invented-evidence']
        return {'context_id': 'fixture-context-' + str(len(self.calls)),
                'result': {'status': 'COMPLETED', 'summary': 'Synthetic task', 'claims': rows}}


class ExecutionTests(unittest.TestCase):
    def setUp(self):
        self.api = module(self, 'execution')
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.project = self.base / 'project'
        self.project.mkdir()
        subprocess.run(['git', 'init', '-q', str(self.project)], check=True)
        (self.project / 'input.txt').write_text('authorized input')
        self.root = self.base / 'artifacts'
        self.root.mkdir()
        bundle, _ = proof_bundle(self.base)
        bundle['candidates'] = {}
        from harness.pipeline import ARTIFACTS
        from harness.io import write_artifact
        for key, name in ARTIFACTS.items():
            write_artifact(self.root / name, bundle[key])
        self.before = {p.name: p.read_bytes() for p in self.root.iterdir()}
        skill = self.base / 'SKILL.md'
        skill.write_text('Synthetic specialist fixture')
        collector = self.base / 'collector.py'
        collector.write_text('''import json, sys
from pathlib import Path
r=json.load(sys.stdin)
p=Path(r['output_dir']); p.mkdir(parents=True)
items=[]
for target in r['targets']:
 for kind in ('render','interaction','technical'):
  f=p/(target['id']+'-'+kind+'.txt'); f.write_text('Synthetic capture')
  items.append(dict(target_id=target['id'],kind=kind,path=str(f),action='select',result='observed',frames=[]))
print(json.dumps(dict(captures=items,errors=[])))
''')
        self.settings = {'request': 'Implement the bounded fixture', 'codex_executable': sys.executable,
                         'work_kind': 'new_direction', 'proof_target_ids': ['wide', 'narrow'],
                         'collector_command': [sys.executable, str(collector)], 'max_cycles': 1,
                         'skills': {role: str(skill) for role in ('J', 'I', 'U', 'V')}}
        self.runner = FakeRunner()

    def execution(self):
        return self.api.Execution(self.root, self.project, self.settings, self.runner)

    def add_second_family(self):
        from harness.pipeline import load_bundle, ARTIFACTS
        from harness.io import write_artifact, digest
        b = load_bundle(self.root)
        target = dict(b['intent']['targets'][0], id='catalog', family='catalog', route='/catalog')
        b['intent']['targets'].append(target)
        b['matrix']['targets'].append(copy.deepcopy(target))
        for ref in b['lock']['references']:
            ref['applies_to'].append('catalog')
        for translation in b['contract']['translations']:
            translation['target_ids'].append('catalog')
        for claim in list(b['matrix']['claims']):
            if claim['target_id'] == 'wide':
                b['matrix']['claims'].append(dict(claim, id=claim['id']+'-catalog', target_id='catalog'))
        b['matrix']['bindings'] = {k: digest(b[k]) for k in ('intent', 'lock', 'contract')}
        for key, name in ARTIFACTS.items():
            write_artifact(self.root / name, b[key], overwrite=True)

    def test_missing_or_partial_proof_scope_cannot_launch_writer(self):
        for selection in (None, [], ['wide'], ['missing'], ['wide', 'wide']):
            with self.subTest(selection=selection):
                self.settings['proof_target_ids'] = selection
                with self.assertRaisesRegex(ValueError, 'PROOF_'):
                    self.execution().run()
                self.assertEqual(self.runner.calls, [])

    def test_unknown_work_kind_and_multifamily_local_repair_are_blocked(self):
        self.settings.pop('work_kind')
        with self.assertRaisesRegex(ValueError, 'WORK_KIND_REQUIRED'):
            self.execution().run()
        self.add_second_family()
        self.settings['work_kind'] = 'local_repair'
        with self.assertRaisesRegex(ValueError, 'LOCAL_REPAIR_SCOPE'):
            self.execution().run()
        self.settings['work_kind'] = 'material_extension'
        self.settings['proof_target_ids'].append('catalog')
        with self.assertRaisesRegex(ValueError, 'PROOF_FAMILY_REQUIRED'):
            self.execution().run()
        self.assertEqual(self.runner.calls, [])

    def test_proof_review_precedes_expansion_and_new_build_rechecks_every_target(self):
        self.add_second_family()
        result = self.execution().run()
        self.assertEqual(result['phase'], 'expansion')
        self.assertEqual(result['execution'], 'REVIEW_COMPLETE_UNCERTIFIED')
        calls = self.runner.calls
        writers = [c for c in calls if c['role'] == 'implementer' and not c['claims']]
        self.assertEqual([[t['id'] for t in c['phase_targets']] for c in writers],
                         [['wide', 'narrow'], ['wide', 'narrow', 'catalog']])
        expansion = next(i for i,c in enumerate(calls) if c.get('phase') == 'expansion')
        self.assertEqual(calls[expansion-1]['role'], 'critic')
        self.assertEqual({c['target_id'] for c in calls[expansion-1]['claims']}, {'wide','narrow'})
        proof = json.loads((self.root/'EXECUTION_REPORT-proof-0.json').read_text())
        self.assertNotEqual(proof['build_id'],result['build_id'])
        self.assertEqual({c['target_id'] for c in result['captures']}, {'wide','narrow','catalog'})
        self.assertEqual(result['unreviewed_target_ids'], [])
        self.assertFalse(result['approved'])
        self.assertTrue(all(self.api.Path(p[0]).name == 'SKILL.md' and
                            self.api.Path(p[0]).parent.name == 'joedesign-harness'
                            for p in self.runner.skill_paths))

    def test_failed_proof_blocks_expansion_and_preserves_unreviewed_scope(self):
        self.add_second_family()
        self.runner.conflict = True
        result = self.execution().run()
        self.assertEqual(result['execution'], 'NEEDS_REPAIR')
        self.assertEqual(result['phase'], 'proof')
        self.assertEqual(result['unreviewed_target_ids'], ['catalog'])
        self.assertFalse(any(c.get('phase') == 'expansion' for c in self.runner.calls))

    def test_uncertain_visual_quality_cannot_be_replaced_by_technical_passes(self):
        self.add_second_family()
        self.runner.uncertain_quality = True
        result = self.execution().run()
        self.assertEqual(result['execution'], 'NEEDS_REPAIR')
        self.assertTrue(any(c.get('raci_step') == 'C2' for c in self.runner.calls))
        self.assertFalse(any(c.get('phase') == 'expansion' for c in self.runner.calls))

    def test_changed_harness_guidance_invalidates_resume(self):
        execution = self.execution()
        execution.run()
        original = self.api.file_hash
        with patch.object(self.api, 'file_hash', side_effect=lambda p:
                          'b'*64 if Path(p) == execution.harness_skill else original(p)):
            with self.assertRaisesRegex(ValueError, 'STALE_EXECUTION'):
                self.execution().run(resume=True)

    def test_review_only_needs_no_production_scope(self):
        self.settings.pop('work_kind')
        self.settings.pop('proof_target_ids')
        self.add_second_family()
        result = self.execution().run(review_only=True)
        self.assertEqual(result['phase'], 'review')
        self.assertEqual(set(result['target_ids']), {'wide','narrow','catalog'})
        self.assertFalse((self.project/'result.txt').exists())

    def test_resume_expansion_reuses_proof_but_rejects_changed_proof_capture(self):
        self.add_second_family()
        original = self.runner.run
        def fail_expansion(task, *args):
            if task.get('phase') == 'expansion':
                raise ValueError('expansion interrupted before write')
            return original(task, *args)
        self.runner.run = fail_expansion
        self.assertEqual(self.execution().run()['execution'], 'BLOCKED')
        count = len(self.runner.calls)
        self.runner.run = original
        result = self.execution().run(resume=True)
        self.assertEqual(result['execution'], 'REVIEW_COMPLETE_UNCERTIFIED')
        self.assertTrue(all(c.get('phase') != 'proof' for c in self.runner.calls[count:]))
        state=json.loads((self.root/'EXECUTION_STATE.json').read_text())
        Path(state['proof_report']['captures'][0]['path']).write_text('changed proof')
        with self.assertRaisesRegex(ValueError, 'CHANGED_CAPTURE'):
            self.execution().run(resume=True)

    def test_runs_ordered_roles_and_fresh_critic_without_certifying(self):
        result = self.execution().run()
        self.assertEqual(result['execution'], 'REVIEW_COMPLETE_UNCERTIFIED')
        self.assertFalse(result['approved'])
        self.assertFalse(result['assessment']['approved'])
        calls = self.runner.calls
        self.assertEqual([c['role'] for c in calls[:2]], ['synthesis', 'implementer'])
        self.assertEqual(calls[-1]['role'], 'critic')
        self.assertNotIn('diagnosis_request', calls[-1])
        self.assertNotIn('plan', calls[-1])
        for claim in result['assessment']['claims']:
            steps = [c['raci_step'] for c in calls if 'raci_step' in c and any(x['id'] == claim for x in c['claims'])]
            self.assertEqual(steps, ['R'] if claim.startswith('Technical') else ['R', 'C1'])
        self.assertEqual(self.before, {name: (self.root / name).read_bytes() for name in self.before})

    def test_resume_does_not_repeat_completed_work_and_detects_changed_capture(self):
        result = self.execution().run()
        count = len(self.runner.calls)
        again = self.execution().run(resume=True)
        self.assertEqual(result, again)
        self.assertEqual(len(self.runner.calls), count)
        Path(result['captures'][0]['path']).write_text('changed')
        with self.assertRaisesRegex(ValueError, 'CHANGED_CAPTURE'):
            self.execution().run(resume=True)

    def test_failed_read_only_step_can_resume_without_reimplementing(self):
        self.runner.fail_once = 'V'
        self.assertEqual(self.execution().run()['execution'], 'BLOCKED')
        self.assertEqual(self.execution().run(resume=True)['execution'], 'REVIEW_COMPLETE_UNCERTIFIED')
        self.assertEqual(sum(c['role'] == 'implementer' and not c['claims'] for c in self.runner.calls), 1)
        self.assertEqual(set(self.runner.controller_statuses), {'RUNNING'})
        self.assertNotIn('error', json.loads((self.root / 'EXECUTION_STATE.json').read_text()))

    def test_conflict_invokes_c2_and_cannot_vote_away_failure(self):
        self.runner.conflict = True
        report = self.execution().run()
        self.assertEqual(report['execution'], 'NEEDS_REPAIR')
        self.assertTrue(any(c.get('raci_step') == 'C2' and c['role'] == 'U' for c in self.runner.calls))
        self.assertTrue(any(r['verdict'] == 'FAIL' for r in report['findings']))

    def test_read_only_mutation_blocks_and_preserves_changed_project(self):
        self.runner.mutate_review = True
        report = self.execution().run()
        self.assertEqual(report['execution'], 'BLOCKED')
        self.assertIn('READ_ONLY_PHASE_CHANGED_PROJECT', report['error'])
        self.assertEqual((self.project / 'result.txt').read_text(), 'invalid review edit')
        with self.assertRaisesRegex(ValueError, 'STALE_EXECUTION'):
            self.execution().run(resume=True)

    def test_repair_recollects_and_rechecks_new_build(self):
        self.settings['max_cycles'] = 2
        self.runner.repair_needed = True
        report = self.execution().run()
        self.assertEqual(report['execution'], 'REVIEW_COMPLETE_UNCERTIFIED')
        self.assertEqual(report['cycle'], 1)
        old = json.loads((self.root / 'EXECUTION_REPORT-0.json').read_text())
        self.assertNotEqual(old['build_id'], report['build_id'])
        self.assertTrue(all(i['build_id'] == report['build_id'] for i in report['captures']))

    def test_structural_failure_does_not_launch_local_repair(self):
        self.settings['max_cycles'] = 5
        self.runner.conflict = True
        report = self.execution().run()
        self.assertEqual(report['repair_disposition'], 'MATERIAL_REWORK_REQUIRED')
        self.assertEqual(report['cycle'], 0)
        self.assertFalse(any(c['role'] == 'repair' for c in self.runner.calls))

    def test_repeated_unresolved_claim_stops_even_with_larger_cycle_allowance(self):
        self.settings['max_cycles'] = 5
        self.runner.repair_needed = self.runner.persistent_failure = True
        report = self.execution().run()
        self.assertEqual(report['execution'], 'NEEDS_REPAIR')
        self.assertEqual(report['repair_disposition'], 'MATERIAL_REWORK_REQUIRED')
        self.assertEqual(report['cycle'], 1)
        self.assertEqual(sum(c['role'] == 'repair' for c in self.runner.calls), 1)

    def test_changed_source_cannot_resume(self):
        self.execution().run()
        (self.project / 'input.txt').write_text('new material')
        with self.assertRaisesRegex(ValueError, 'STALE_EXECUTION'):
            self.execution().run(resume=True)

    def test_bad_contract_or_missing_specialist_cannot_launch_writer(self):
        self.settings['skills']['V'] = str(self.base / 'absent.md')
        with self.assertRaisesRegex(ValueError, 'SPECIALIST_UNAVAILABLE'):
            self.execution()
        self.assertEqual(self.runner.calls, [])

    def test_invalid_contract_cannot_launch_writer(self):
        from harness.io import read_artifact, write_artifact
        from harness.pipeline import ARTIFACTS
        path = self.root / ARTIFACTS['contract']
        contract = read_artifact(path)
        contract['reference_ids'] = ['nonexistent-source']
        write_artifact(path, contract, overwrite=True)
        with self.assertRaisesRegex(ValueError, 'EXECUTION_CONTRACT_INVALID'):
            self.execution()
        self.assertEqual(self.runner.calls, [])

    def test_partial_writer_failure_is_preserved_and_not_blindly_replayed(self):
        self.runner.fail_after_write = True
        self.assertEqual(self.execution().run()['execution'], 'BLOCKED')
        partial = (self.project / 'result.txt').read_bytes()
        self.runner.fail_after_write = False
        report = self.execution().run(resume=True)
        self.assertIn('PARTIAL_WRITE_REQUIRES_INSPECTION', report['error'])
        self.assertEqual((self.project / 'result.txt').read_bytes(), partial)
        self.assertEqual(sum(c['role'] == 'implementer' and not c['claims'] for c in self.runner.calls), 1)

    def test_concurrent_execution_refused(self):
        (self.root / 'execution.lock').write_text('{}')
        with self.assertRaisesRegex(ValueError, 'EXECUTION_LOCKED'):
            self.execution().run()
        self.assertEqual(self.runner.calls, [])

    def test_review_only_observes_current_build_without_any_writer(self):
        before = self.api.project_fingerprint(self.project)
        self.runner.conflict = True
        result = self.execution().run(review_only=True)
        self.assertEqual(result['mode'], 'review')
        self.assertEqual(result['execution'], 'NEEDS_REPAIR')
        self.assertFalse(any(c['role'] in ('synthesis', 'repair') or
                             (c['role'] == 'implementer' and not c['claims']) for c in self.runner.calls))
        self.assertEqual(before, self.api.project_fingerprint(self.project))
        self.assertFalse(result['approved'])
        with self.assertRaisesRegex(ValueError, 'EXECUTION_MODE_MISMATCH'):
            self.execution().run(resume=True)
        count = len(self.runner.calls)
        self.assertEqual(result, self.execution().run(resume=True, review_only=True))
        self.assertEqual(count, len(self.runner.calls))

    def test_locked_reference_can_support_but_not_replace_capture(self):
        self.runner.evidence_mode = 'reference'
        self.assertEqual(self.execution().run()['execution'], 'REVIEW_COMPLETE_UNCERTIFIED')

    def test_reference_only_cannot_prove_implementation(self):
        self.runner.evidence_mode = 'reference-only'
        result = self.execution().run()
        self.assertEqual(result['execution'], 'BLOCKED')
        self.assertIn('REVIEW_EVIDENCE_MISSING', result['error'])

    def test_invalid_review_is_failed_and_retry_does_not_repeat_writer(self):
        self.runner.evidence_mode = 'invented'
        result = self.execution().run()
        self.assertIn('UNKNOWN_REVIEW_EVIDENCE', result['error'])
        state = json.loads((self.root / 'EXECUTION_STATE.json').read_text())
        self.assertTrue(any(s['status'] == 'FAILED' for s in state['steps'].values()))
        self.runner.evidence_mode = ''
        self.assertEqual(self.execution().run(resume=True)['execution'], 'REVIEW_COMPLETE_UNCERTIFIED')
        self.assertEqual(sum(c['role'] == 'implementer' and not c['claims'] for c in self.runner.calls), 1)


if __name__ == '__main__':
    unittest.main()
