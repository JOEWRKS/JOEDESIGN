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
        collector.write_text('''import json, sys, hashlib
from pathlib import Path
r=json.load(sys.stdin)
p=Path(r['output_dir']); p.mkdir(parents=True)
items=[]
for target in r['targets']:
 image=p/(target['id']+'-render.txt'); image.write_text('Synthetic capture')
 log=dict(target=target,build_id=r['build_id'],frames=[str(image)],
  frame_hashes={str(image):hashlib.sha256(image.read_bytes()).hexdigest()},design=dict(r['design'],measurements=[]))
 for check in r['design']['checks']:
  if check['target_id']==target['id'] and check['method']=='geometry':
   log['design']['measurements'].append(dict(check_id=check['check_id'],criterion_sha256=check['criterion_sha256'],
     values=[check['criterion']['min']+r['browser'].get('geometry_offset',0)]*check['criterion']['expected_count']))
 for kind in ('render','interaction','technical'):
  f=image if kind=='render' else p/(target['id']+'-observation.json')
  if kind!='render': f.write_text(json.dumps(log))
  items.append(dict(target_id=target['id'],kind=kind,path=str(f),action='select',result='observed',frames=[]))
print(json.dumps(dict(captures=items,errors=[])))
''')
        self.settings = {'request': 'Implement the bounded fixture', 'codex_executable': sys.executable,
                         'work_kind': 'new_direction', 'proof_target_ids': ['wide', 'narrow'],
                         'collector_command': [sys.executable, str(collector)], 'max_cycles': 1,
                         'skills': {role: str(skill) for role in ('I', 'U', 'V')}}
        self.runner = FakeRunner()
        (self.project / 'DESIGN.md').write_text('Synthetic approved design fixture')
        self.freeze_design_baseline(bundle)

    def freeze_design_baseline(self, bundle):
        from harness.io import digest, file_hash, write_artifact
        targets = bundle['intent']['targets']
        checks = []
        for target in targets:
            claim = next(c for c in bundle['matrix']['claims'] if c['target_id']==target['id'] and c['category']=='VisualQuality')
            criterion = {'claim_id': claim['id'], 'category': claim['category'], 'expected': claim['expected']}
            checks.append(dict(check_id='design-'+target['id'], target_id=target['id'], rule_id='composition',
                method='specialist', lane='visual', criterion=criterion, criterion_sha256=digest(criterion), inputs=['input.txt']))
        baseline = dict(schema='joeness.review-baseline.v1', scope_id=bundle['intent']['scope_id'],
            authority=[dict(path='DESIGN.md', sha256=file_hash(self.project/'DESIGN.md'))],
            authorization_ref='Synthetic test scope, not user approval', targets=targets,
            rules=[dict(id='composition',source_ref='DESIGN.md',target_ids=[t['id'] for t in targets],methods=['specialist'])],
            required_checks=checks)
        self.baseline_path = self.base / 'design-baseline.json'
        write_artifact(self.baseline_path, baseline, overwrite=True)
        self.settings['design_validation'] = dict(baseline=str(self.baseline_path),baseline_sha256=file_hash(self.baseline_path))

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
        self.freeze_design_baseline(b)

    def test_missing_or_partial_proof_scope_cannot_launch_writer(self):
        for selection in (None, [], ['wide'], ['missing'], ['wide', 'wide']):
            with self.subTest(selection=selection):
                self.settings['proof_target_ids'] = selection
                with self.assertRaisesRegex(ValueError, 'PROOF_'):
                    self.execution().run()
                self.assertEqual(self.runner.calls, [])

    def test_missing_design_baseline_cannot_launch_writer(self):
        self.settings.pop('design_validation')
        with self.assertRaisesRegex(ValueError, 'DESIGN_VALIDATION_REQUIRED'):
            self.execution()
        self.assertEqual(self.runner.calls, [])

    def test_failed_measured_gap_blocks_expansion_even_when_all_reviewers_pass(self):
        from harness.io import read_artifact, write_artifact, digest, file_hash
        self.add_second_family()
        baseline = read_artifact(self.baseline_path)
        criterion = dict(kind='gap',container='.fixture',items=':scope > *',axis='y',
                         expected_count=1,min=16,max=16,tolerance=0)
        baseline['rules'].append(dict(id='spacing',source_ref='DESIGN.md',target_ids=['wide'],methods=['geometry']))
        baseline['required_checks'].append(dict(check_id='spacing-wide',rule_id='spacing',target_id='wide',
            method='geometry',lane='visual',criterion=criterion,criterion_sha256=digest(criterion),inputs=['input.txt']))
        write_artifact(self.baseline_path,baseline,overwrite=True)
        self.settings['design_validation']['baseline_sha256']=file_hash(self.baseline_path)
        self.settings['browser']={'geometry_offset':8}
        result=self.execution().run()
        self.assertEqual(result['execution'],'NEEDS_REPAIR')
        self.assertTrue(all(r['verdict']=='PASS' for r in result['reviews']))
        self.assertTrue(any(r['status']=='FAIL' for r in result['design_conformance']['results']))
        self.assertFalse(any(c.get('phase')=='expansion' for c in self.runner.calls))

    def test_changed_conformance_output_cannot_be_reused_on_resume(self):
        result=self.execution().run()
        Path(result['design_conformance_path']).write_text('{"eligible":true}')
        with self.assertRaisesRegex(ValueError,'CHANGED_DESIGN_RESULT'):
            self.execution().run(resume=True)

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
                            self.api.Path(p[0]).parent.name == 'joedesign'
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

    def test_changed_operating_core_invalidates_resume(self):
        execution = self.execution()
        execution.run()
        original = self.api.file_hash
        with patch.object(self.api, 'file_hash', side_effect=lambda p:
                          'b'*64 if Path(p) == execution.operating_core else original(p)):
            with self.assertRaisesRegex(ValueError, 'STALE_EXECUTION'):
                self.execution().run(resume=True)

    def test_external_core_override_is_rejected_before_any_role(self):
        self.settings['skills']['J'] = str(self.base / 'SKILL.md')
        with self.assertRaisesRegex(ValueError, 'OPERATING_CORE_OVERRIDE'):
            self.execution()
        self.assertFalse(self.runner.calls)

    def test_visual_modules_reach_J_roles_and_changes_invalidate_resume(self):
        execution = self.execution()
        execution.run()
        for task, paths in zip(self.runner.calls, self.runner.skill_paths):
            self.assertEqual(paths[0], execution.operating_core)
            self.assertEqual(paths.count(execution.operating_core), 1)
            if task['role'] in ('synthesis', 'repair', 'critic', 'J') or (
                    task['role'] == 'implementer' and not task.get('claims')):
                for p in execution.visual_modules:
                    self.assertIn(p, paths)
        original = self.api.file_hash
        with patch.object(self.api, 'file_hash', side_effect=lambda p:
                          'c'*64 if Path(p) == execution.visual_modules[0] else original(p)):
            with self.assertRaisesRegex(ValueError, 'STALE_EXECUTION'):
                self.execution().run(resume=True)

    def test_missing_internal_module_cannot_launch_a_role(self):
        original = Path.is_file
        with patch.object(Path, 'is_file', lambda p:
                          False if p.name == 'visual-translation.md' else original(p)):
            with self.assertRaisesRegex(ValueError, 'JOEDESIGN_MODULE_UNAVAILABLE'):
                self.execution()
        self.assertFalse(self.runner.calls)

    def test_copied_package_production_keeps_one_core_through_proof_and_expansion(self):
        import shutil
        from harness_support import ROOT
        self.add_second_family()
        dest = self.base / 'installed/joedesign'
        shutil.copytree(ROOT / 'skills/joedesign', dest, ignore=shutil.ignore_patterns('__pycache__'))
        runtime = self.base / 'runtime.json'
        runtime.write_text(json.dumps(self.settings), encoding='utf-8')
        result_file = self.base / 'copied-result.json'
        # Fixture role responses are synthetic. All runtime modules must come from
        # the copied package; the original repo contributes test fixtures only.
        script = '''import json,sys
from pathlib import Path
sys.path.insert(0,sys.argv[1])
from harness.execution import Execution
sys.path.insert(0,sys.argv[2])
from test_harness_execution import FakeRunner
runner=FakeRunner()
execution=Execution(sys.argv[3],sys.argv[4],json.loads(Path(sys.argv[5]).read_text()),runner)
report=execution.run()
Path(sys.argv[6]).write_text(json.dumps(dict(report=report,
    sources=[[str(p) for p in paths] for paths in runner.skill_paths],
    modules={k:v.__file__ for k,v in sys.modules.items() if k.startswith('harness.')})))
'''
        result = subprocess.run([sys.executable, '-c', script, str(dest / 'scripts'), str(ROOT / 'tests'),
                                 str(self.root), str(self.project), str(runtime), str(result_file)],
                                capture_output=True, text=True, encoding='utf-8', cwd=self.base)
        self.assertEqual(result.returncode, 0, result.stderr)
        data = json.loads(result_file.read_text())
        self.assertEqual(data['report']['execution'], 'REVIEW_COMPLETE_UNCERTIFIED')
        self.assertEqual(data['report']['phase'], 'expansion')
        self.assertFalse(data['report']['approved'])
        self.assertTrue(all(Path(paths[0]) == dest / 'SKILL.md' for paths in data['sources']))
        self.assertTrue(all(Path(p).is_relative_to(dest) for p in data['modules'].values()))

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
