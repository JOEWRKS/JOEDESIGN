"""F05 boundary tests. Synthetic logs here do not establish rendered quality."""
import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from harness_support import SCRIPTS
from harness.conformance import bindings, evaluate
from harness.impact import inspect_impact
from harness.io import digest, file_hash, write_artifact
from test_design_conformance import baseline_fixture, GOOD_HTML


class ImpactFixture:
    def __init__(self, root):
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)
        (self.root/'index.html').write_text(GOOD_HTML, encoding='utf-8')
        self.old = baseline_fixture(self.root)
        self.put('old.json', self.old)
        (self.root/'authority-before.md').write_bytes((self.root/'DESIGN.md').read_bytes())
        (self.root/'frame.txt').write_text('Synthetic unit-test frame; NOT browser evidence')
        frame = str(self.root/'frame.txt')
        self.log = dict(target=self.old['targets'][0], build_id='static-fixture', frames=[frame],
            frame_hashes={frame:file_hash(Path(frame))}, design=dict(
                baseline_sha256=self.ref('old.json')['sha256'],
                input_fingerprints=bindings(self.old, self.root, ['wide']),
                measurements=[dict(check_id=c['check_id'],criterion_sha256=c['criterion_sha256'],
                    values=[c['criterion']['min']]) for c in self.old['required_checks']]))
        self.put('observation.json', self.log)
        self.receipt = evaluate(self.old,self.ref('old.json')['sha256'],self.root,[self.root/'observation.json'])
        self.put('old-result.json', self.receipt)
        self.new = copy.deepcopy(self.old)
        self.append('\n<!-- Editorial note; no rule change. -->\n')
        self.served = dict(schema='joedesign.served-build.v1',scope_id=self.old['scope_id'],
            baseline_sha256=self.ref('new.json')['sha256'],targets=[dict(
                target=copy.deepcopy(self.old['targets'][0]),build_id='static-fixture',
                dependencies_complete=True,limitations=[],resources=[dict(path='index.html',
                    sha256=file_hash(self.root/'index.html'),response_sha256=file_hash(self.root/'index.html'))])])
        self.review = dict(schema='joedesign.impact-review.v1',scope_id=self.old['scope_id'],
            implementation_context='synthetic-implementer',review_context='synthetic-reviewer',
            scope_analysis='Synthetic scoped assessment: existing criteria, defaults and coverage are unchanged.',
            authority_analysis=[dict(path='DESIGN.md',kind='COMMENT_APPEND',rationale='Only an appended editorial comment.')],
            checks=[dict(check_id=c['check_id'],verdict='UNAFFECTED',rationale='Existing spacing and inputs are unchanged.',
                source_refs=[self.ref('DESIGN.md')],blocking_findings=[]) for c in self.old['required_checks']])
        self.sync()

    def put(self, name, data):
        write_artifact(self.root/name, data, overwrite=True)

    def ref(self, name):
        return dict(path=name,sha256=file_hash(self.root/name))

    def append(self, text):
        (self.root/'DESIGN.md').write_bytes((self.root/'authority-before.md').read_bytes()+text.encode())
        self.new['authority'][0]['sha256']=file_hash(self.root/'DESIGN.md')
        self.put('new.json',self.new)

    def sync(self):
        self.put('new.json',self.new)
        self.put('old-result.json',self.receipt)
        self.served['baseline_sha256']=self.ref('new.json')['sha256']
        self.put('served.json',self.served)
        self.request=dict(schema='joedesign.impact-request.v1',old_baseline=self.ref('old.json'),
            new_baseline=self.ref('new.json'),old_result=self.ref('old-result.json'),served=self.ref('served.json'),
            authority_before=[dict(path='DESIGN.md',snapshot=self.ref('authority-before.md'))])
        self.review['transition_sha256']=digest(self.request)
        self.put('review.json',self.review)
        self.request['review']=self.ref('review.json')
        self.put('request.json',self.request)

    def run(self, review_pin=True):
        return inspect_impact(self.root,self.root/'request.json',self.ref('request.json')['sha256'],
                              self.ref('review.json')['sha256'] if review_pin else None)


class ImpactTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.f=ImpactFixture(Path(self.temp.name)/'project')

    def assert_no_reuse(self, result):
        self.assertFalse(result['reuse_authorized'])
        self.assertEqual(result['counts']['reusable-candidate'],0,result)

    def test_comment_and_reviewed_unrelated_section_candidates_are_read_only(self):
        for suffix,kind in [('\n<!-- Editorial only -->\n','COMMENT_APPEND'),
                            ('\n## Print export\nFuture print-only notes, outside this screen.\n','UNRELATED_SECTION_APPEND'),
                            ('\r\n## Print export\r\nFuture print-only notes, outside this screen.\r\n','UNRELATED_SECTION_APPEND')]:
            with self.subTest(kind=kind):
                self.f.append(suffix)
                self.f.review['authority_analysis'][0]['kind']=kind
                for c in self.f.review['checks']:c['source_refs']=[self.f.ref('DESIGN.md')]
                self.f.sync()
                before={p:file_hash(p) for p in self.f.root.iterdir() if p.is_file()}
                result=self.f.run()
                self.assertEqual(result['counts']['reusable-candidate'],4,result)
                self.assertFalse(result['reuse_authorized'])
                self.assertEqual(result['acceptance'],'NOT_GRANTED')
                self.assertEqual(before,{p:file_hash(p) for p in self.f.root.iterdir() if p.is_file()})

    def test_missing_review_pin_and_mismatched_request_pin_fail_closed(self):
        self.assert_no_reuse(self.f.run(False))
        self.assert_no_reuse(inspect_impact(self.f.root,self.f.root/'request.json','0'*64))
        self.assert_no_reuse(inspect_impact(self.f.root,self.f.root/'request.json',self.f.ref('request.json')['sha256'],'0'*64))

    def test_criterion_relaxation_coverage_target_and_acceptance_changes_block(self):
        original=copy.deepcopy(self.f.new)
        for change in ('criterion','delete','duplicate','target','acceptance','opaque'):
            with self.subTest(change=change):
                self.f.new=copy.deepcopy(original)
                if change=='criterion':
                    c=self.f.new['required_checks'][0];c['criterion']['max']=100
                    c['criterion_sha256']=digest(c['criterion'])
                elif change=='delete':self.f.new['required_checks'].pop()
                elif change=='duplicate':self.f.new['required_checks'].append(self.f.new['required_checks'][0])
                elif change=='target':self.f.new['targets'][0]['viewport']=[390,844]
                elif change=='acceptance':self.f.new['required_acceptance']=False
                else:self.f.new['opaque_override']=True
                self.f.sync();self.assert_no_reuse(self.f.run())

    def test_changed_existing_authority_cannot_be_called_an_append(self):
        (self.f.root/'DESIGN.md').write_text('Relax all spacing rules.\n<!-- unchanged -->')
        self.f.new['authority'][0]['sha256']=file_hash(self.f.root/'DESIGN.md')
        self.f.sync();self.assert_no_reuse(self.f.run())

    def test_css_even_comment_requires_rerun(self):
        with (self.f.root/'index.html').open('a') as out:out.write('<!-- runtime comment -->')
        result=self.f.run();self.assert_no_reuse(result)
        self.assertEqual(result['counts']['rerun'],4)

    def test_unverified_dependencies_changed_build_and_served_bytes_block(self):
        saved=copy.deepcopy(self.f.served)
        for change in ('late','build','response','missing','extra','target'):
            with self.subTest(change=change):
                self.f.served=copy.deepcopy(saved);target=self.f.served['targets'][0]
                if change=='late':target['dependencies_complete']=False
                elif change=='build':target['build_id']='new-build'
                elif change=='response':target['resources'][0]['response_sha256']='0'*64
                elif change=='missing':target['resources']=[]
                elif change=='extra':target['resources'].append(dict(path='extra.css',sha256='0'*64,response_sha256='0'*64))
                else:target['target']['state']='different'
                self.f.sync();self.assert_no_reuse(self.f.run())

    def test_failure_and_current_rejection_never_promoted(self):
        self.f.receipt['results'][0]['status']='FAIL'
        self.f.receipt['unresolved']=[dict(check_id='c0',status='FAIL')]
        self.f.review['checks'][1]['blocking_findings']=['Current user rejection']
        self.f.sync();result=self.f.run()
        self.assertEqual(result['counts']['reusable-candidate'],2,result)
        self.assertEqual(result['checks'][0]['previous_result']['status'],'FAIL')

    def test_partial_review_preserves_only_independently_reviewed_checks(self):
        self.f.review['checks']=self.f.review['checks'][:1]
        self.f.sync();result=self.f.run()
        self.assertEqual(result['counts'],{'reusable-candidate':1,'rerun':0,'unknown':3})

    def test_affected_review_requires_fresh_observation(self):
        self.f.review['checks'][0]['verdict']='AFFECTED'
        self.f.sync();self.assertEqual(self.f.run()['checks'][0]['classification'],'rerun')

    def test_corrupted_frame_blocks_old_evidence(self):
        (self.f.root/'frame.txt').write_text('changed after observation')
        self.assert_no_reuse(self.f.run())

    def test_forged_pass_cannot_override_failing_raw_measurement(self):
        self.f.log['design']['measurements'][0]['values']=[500]
        self.f.put('observation.json',self.f.log)
        for row in self.f.receipt['results']:
            for proof in row['evidence']:
                if Path(proof['path']).name=='observation.json':proof['sha256']=file_hash(self.f.root/'observation.json')
        self.f.sync();result=self.f.run()
        self.assertEqual(result['checks'][0]['classification'],'unknown',result)
        self.assertEqual(result['counts']['reusable-candidate'],3)

    def test_cli_emits_candidates_without_writing_inputs_or_overwriting_output(self):
        command=[sys.executable,str(SCRIPTS/'harness_cli.py'),'inspect-impact','--project',str(self.f.root),
            '--request',str(self.f.root/'request.json'),'--request-sha256',self.f.ref('request.json')['sha256'],
            '--review-sha256',self.f.ref('review.json')['sha256'],'--output',str(self.f.root/'impact.json')]
        run=subprocess.run(command,capture_output=True,text=True,encoding='utf-8')
        self.assertEqual(run.returncode,0,run.stderr+run.stdout)
        self.assertFalse(json.loads(run.stdout)['reuse_authorized'])
        saved=file_hash(self.f.root/'impact.json')
        run=subprocess.run(command,capture_output=True,text=True,encoding='utf-8')
        self.assertNotEqual(run.returncode,0)
        self.assertEqual(file_hash(self.f.root/'impact.json'),saved)


if __name__=='__main__':unittest.main()
