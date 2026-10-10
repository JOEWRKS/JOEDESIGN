"""Pinned scoped checks, real rendered geometry, and stale evidence rejection."""
import copy
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import threading
import unittest

from harness_support import SCRIPTS
from harness.conformance import bindings, evaluate, input_fingerprint, load_baseline
from harness.io import digest, file_hash, read_artifact, write_artifact


def baseline_fixture(project):
    (project / 'DESIGN.md').write_text('Fixture authority: sibling gap 16, section gap 40, card gap 8, inset 32. Not a universal design rule.')
    target = dict(id='wide', route='/', surface='fixture', family='fixture', viewport=[1000, 700],
                  state='default', theme='light', locale='en', required_kinds=['render', 'technical'])
    criteria = [
        dict(kind='gap', container='.group', items=':scope > div', axis='y', expected_count=1, min=16, max=16, tolerance=.1),
        dict(kind='pair', **{'from': '.before', 'to': '.after > div'}, from_edge='bottom', to_edge='top', expected_count=1, min=40, max=40, tolerance=.1),
        dict(kind='gap', container='.card', items=':scope > div', axis='y', expected_count=1, min=8, max=8, tolerance=.1),
        dict(kind='inset', container='.panel', items=':scope > div', edge='bottom', expected_count=1, min=32, max=32, tolerance=.1)]
    checks = [dict(check_id='c'+str(i), target_id='wide', method='geometry', rule_id='r'+str(i), lane='visual',
                   criterion=c, criterion_sha256=digest(c), inputs=['index.html']) for i,c in enumerate(criteria)]
    return dict(schema='joeness.review-baseline.v1', scope_id='spacing-fixture',
        authority=[dict(path='DESIGN.md', sha256=file_hash(project/'DESIGN.md'))],
        authorization_ref='Synthetic fixture scope; not real user approval', targets=[target],
        rules=[dict(id=c['rule_id'],source_ref='DESIGN.md',target_ids=['wide'],methods=['geometry']) for c in checks],
        required_checks=checks, required_lanes=['visual'], required_acceptance=True)


BAD_HTML = '''<!doctype html><html lang="en"><title>Geometry fixture</title><style>
*{box-sizing:border-box} body{margin:0} .group,.card{display:flex;flex-direction:column}
.group{gap:16px}.group>div,.card>div,.before,.after>div{height:20px}
.group>div+div{margin-top:8px}.before{margin-bottom:40px}.after{padding-top:40px}
.card{height:200px}.price{margin-top:auto}.panel{display:flex;padding:32px;gap:16px}
.panel>div:first-child{height:80px}.panel>div:last-child{height:20px}
</style><main id="page"><section class="group"><div>Title</div><div>Body</div></section>
<div class="before">Before</div><section class="after"><div>Form</div></section>
<article class="card"><div>Product wraps</div><div class="price">Price</div></article>
<section class="panel"><div>Tall</div><div>Short</div></section></main></html>'''
GOOD_HTML = BAD_HTML.replace('margin-top:8px', 'margin-top:0').replace('padding-top:40px', 'padding-top:0').replace('height:200px', 'height:auto;gap:8px').replace('margin-top:auto', 'margin-top:0')


class ConformanceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.project = self.root / 'project'
        self.project.mkdir()
        (self.project/'index.html').write_text(GOOD_HTML)
        self.baseline = baseline_fixture(self.project)
        self.path = self.root/'baseline.json'
        write_artifact(self.path,self.baseline)
        self.pin = file_hash(self.path)

    def observation(self):
        frame=self.root/'frame.txt';frame.write_text('Synthetic frame, not a rendered screenshot')
        log=dict(target=self.baseline['targets'][0],build_id='fixture',frames=[str(frame)],frame_hashes={str(frame):file_hash(frame)},design=dict(
            baseline_sha256=self.pin,input_fingerprints=bindings(self.baseline,self.project,['wide']),
            measurements=[dict(check_id=c['check_id'],criterion_sha256=c['criterion_sha256'],values=[c['criterion']['min']]) for c in self.baseline['required_checks']]))
        p=self.root/'observation.json';write_artifact(p,log,overwrite=True)
        return p

    def test_missing_measurement_or_partial_pass_never_completes(self):
        p=self.observation()
        original=read_artifact(p)
        for measurements in ([],original['design']['measurements'][:-1]):
            log=copy.deepcopy(original);log['design']['measurements']=measurements
            write_artifact(p,log,overwrite=True)
            result=evaluate(self.baseline,self.pin,self.project,[p])
            self.assertFalse(result['eligible'])
            self.assertEqual(len(result['results']),4)
            self.assertTrue(result['unresolved'])
        write_artifact(p,original,overwrite=True)
        self.assertTrue(evaluate(self.baseline,self.pin,self.project,[p])['eligible'])

    def test_old_output_or_corrupt_observation_is_not_a_pass(self):
        p=self.observation()
        (self.project/'index.html').write_text(BAD_HTML)
        self.assertFalse(evaluate(self.baseline,self.pin,self.project,[p])['eligible'])
        p.write_text('{broken')
        self.assertFalse(evaluate(self.baseline,self.pin,self.project,[p])['eligible'])

    def test_frame_changed_after_capture_cannot_be_rebound_as_current_proof(self):
        p=self.observation()
        (self.root/'frame.txt').write_text('Changed after capture')
        self.assertFalse(evaluate(self.baseline,self.pin,self.project,[p])['eligible'])

    def test_frame_hash_uses_recorded_path_spelling(self):
        p=self.observation();log=read_artifact(p)
        # A CUA collector can emit forward-slash absolute Windows paths.
        # Lookup must use the original frame key, not str(Path(key)).
        names=[Path(name).as_posix() for name in log['frames']]
        log['frames']=names
        log['frame_hashes']={name:file_hash(Path(name)) for name in names}
        write_artifact(p,log,overwrite=True)
        self.assertTrue(evaluate(self.baseline,self.pin,self.project,[p])['eligible'])
        Path(names[0]).write_text('Changed pixels')
        self.assertFalse(evaluate(self.baseline,self.pin,self.project,[p])['eligible'])

    def test_unrelated_file_does_not_invalidate_scoped_inputs(self):
        before=input_fingerprint(self.project,['index.html'])
        (self.project/'unrelated.txt').write_text('independent work')
        self.assertEqual(before,input_fingerprint(self.project,['index.html']))

    def test_same_target_id_cannot_reuse_changed_viewport_state_or_route(self):
        p = self.observation()
        for field, value in [('viewport', [390,844]), ('state', 'error'), ('route', '/other')]:
            with self.subTest(field=field):
                changed = copy.deepcopy(self.baseline)
                changed['targets'][0][field] = value
                # Even if someone rebinds the pin, the full observed target must match.
                pin = digest(changed)
                log = read_artifact(p)
                log['design']['baseline_sha256'] = pin
                write_artifact(p, log, overwrite=True)
                result = evaluate(changed, pin, self.project, [p])
                self.assertFalse(result['eligible'])
                self.assertTrue(all(r['status'] == 'UNVERIFIED' for r in result['results']))

    def test_pin_prevents_rule_relaxation_and_inventory_prevents_deletion(self):
        modified=copy.deepcopy(self.baseline)
        modified['required_checks'][0]['criterion']['max']=500
        modified['required_checks'][0]['criterion_sha256']=digest(modified['required_checks'][0]['criterion'])
        write_artifact(self.path,modified,overwrite=True)
        with self.assertRaisesRegex(ValueError,'PIN_MISMATCH'):load_baseline(self.path,self.pin,self.project)
        modified=copy.deepcopy(self.baseline);modified['required_checks'].pop()
        write_artifact(self.path,modified,overwrite=True)
        with self.assertRaisesRegex(ValueError,'RULE_COVERAGE'):load_baseline(self.path,file_hash(self.path),self.project)

    def test_changed_design_authority_blocks(self):
        (self.project/'DESIGN.md').write_text('changed criteria')
        with self.assertRaisesRegex(ValueError,'AUTHORITY_STALE'):load_baseline(self.path,self.pin,self.project)

    def test_repeated_roles_are_all_measured_and_consistency_is_checked(self):
        c=self.baseline['required_checks'][0]
        c['criterion'].update(expected_count=2,min=0,max=100,max_spread=1)
        c['criterion_sha256']=digest(c['criterion'])
        p=self.observation();log=read_artifact(p)
        log['design']['measurements'][0]['values']=[16,24]
        write_artifact(p,log,overwrite=True)
        self.assertEqual(evaluate(self.baseline,self.pin,self.project,[p])['results'][0]['status'],'FAIL')

    @unittest.skipUnless(os.environ.get('JOEDESIGN_PLAYWRIGHT_MODULE'),'Existing browser runtime not configured')
    def test_real_rendered_stacking_auto_space_and_union_inset_then_recovery(self):
        class Quiet(SimpleHTTPRequestHandler):
            def log_message(self,*args):pass
        server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(self.project)))
        thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
        try:
            def capture(html,name):
                (self.project/'index.html').write_text(html)
                request=dict(output_dir=str(self.root/name),targets=self.baseline['targets'],build_id=name,
                    browser=dict(base_url=f'http://127.0.0.1:{server.server_port}',
                        playwright_module=os.environ['JOEDESIGN_PLAYWRIGHT_MODULE'],
                        executable=os.environ.get('JOEDESIGN_BROWSER_EXECUTABLE'),
                        probes={'wide':dict(assertions=[dict(selector='#page',visible=True)])}),
                    design=dict(baseline_sha256=self.pin,input_fingerprints=bindings(self.baseline,self.project,['wide']),checks=self.baseline['required_checks']))
                process=subprocess.run(['node',str(SCRIPTS/'capture.mjs')],input=json.dumps(request),capture_output=True,text=True,encoding='utf-8',timeout=60)
                self.assertEqual(process.returncode,0,process.stderr)
                result=json.loads(process.stdout);self.assertEqual(result['errors'],[])
                return [c['path'] for c in result['captures'] if c['kind']=='technical']
            before=capture(BAD_HTML,'bad')
            result=evaluate(self.baseline,self.pin,self.project,before)
            self.assertEqual([r['status'] for r in result['results']],['FAIL','FAIL','FAIL','PASS'])
            self.assertEqual([r['measured_values'][0] for r in result['results']],[24,80,160,32])
            after=capture(GOOD_HTML,'good')
            self.assertTrue(evaluate(self.baseline,self.pin,self.project,after)['eligible'])
            self.assertFalse(evaluate(self.baseline,self.pin,self.project,before)['eligible'])
        finally:
            server.shutdown();server.server_close();thread.join()


if __name__=='__main__':unittest.main()
