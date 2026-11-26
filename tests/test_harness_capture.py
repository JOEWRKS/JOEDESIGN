"""Opt-in real browser integration; never substitutes for visual/user acceptance."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
import os
from pathlib import Path
import subprocess
import tempfile
import threading
import unittest

from harness_support import SCRIPTS


@unittest.skipUnless(os.environ.get('JOEDESIGN_PLAYWRIGHT_MODULE'), 'Existing Playwright runtime not configured')
class CaptureTests(unittest.TestCase):
    def test_actual_click_state_capture_and_failed_state(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            project = root / 'project'
            project.mkdir()
            (project / 'index.html').write_text('<!doctype html><html lang="en"><title>Fixture</title>'
                '<button onclick="document.querySelector(\'p\').textContent=\'Selected\'">Select</button>'
                '<p>Initial</p></html>', encoding='utf-8')
            class QuietHandler(SimpleHTTPRequestHandler):
                def log_message(self, *args):
                    pass
            server = ThreadingHTTPServer(('127.0.0.1', 0), partial(QuietHandler, directory=str(project)))
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            try:
                target = dict(id='narrow-selected', route='/', viewport=[390, 844], locale='en', theme='light', state='selected')
                settings = dict(base_url=f'http://127.0.0.1:{server.server_port}',
                    playwright_module=os.environ['JOEDESIGN_PLAYWRIGHT_MODULE'],
                    executable=os.environ.get('JOEDESIGN_BROWSER_EXECUTABLE'), probes={target['id']: {
                        'actions': [{'type': 'press', 'key': 'Tab'}, {'type': 'press', 'key': 'Enter'}],
                        'assertions': [{'selector': 'p', 'text': 'Selected', 'visible': True},
                                       {'selector': 'button', 'focused': True}]}})
                request = dict(output_dir=str(root / 'captures'), targets=[target], build_id='real-fixture', browser=settings)
                argv = [os.environ.get('JOEDESIGN_NODE', 'node'), str(SCRIPTS / 'capture.mjs')]
                result = subprocess.run(argv, input=json.dumps(request), capture_output=True, text=True,
                                        encoding='utf-8', timeout=60)
                self.assertEqual(result.returncode, 0, result.stderr)
                output = json.loads(result.stdout)
                self.assertEqual(output['errors'], [])
                self.assertEqual({i['kind'] for i in output['captures']}, {'render', 'interaction', 'technical'})
                render = next(i for i in output['captures'] if i['kind'] == 'render')
                self.assertTrue(Path(render['path']).read_bytes().startswith(b'\x89PNG\r\n\x1a\n'))
                action = next(i for i in output['captures'] if i['kind'] == 'interaction')
                observed = json.loads(Path(action['path']).read_text())
                self.assertEqual(observed['assertions'][0]['text'], 'Selected')
                self.assertEqual(observed['build_id'], 'real-fixture')
                self.assertEqual(observed['actions'][0]['focus']['tag'], 'BUTTON')
                self.assertTrue(observed['actions'][0]['focus']['visible'])
                request['output_dir'] = str(root / 'failed')
                settings['probes'][target['id']]['assertions'][0]['text'] = 'Never present'
                result = subprocess.run(argv, input=json.dumps(request), capture_output=True, text=True,
                                        encoding='utf-8', timeout=60)
                output = json.loads(result.stdout)
                self.assertTrue(output['errors'])
                self.assertEqual(output['captures'], [])
            finally:
                server.shutdown()
                server.server_close()
                thread.join()



def _cdp_ready():
    import shutil
    from harness.execution import collector_sources
    found = collector_sources(cwd=SCRIPTS)
    return bool(shutil.which('node') and found['cdp_browser'] and not found['playwright']
                and not os.environ.get('JOEDESIGN_SKIP_BROWSER'))


@unittest.skipUnless(_cdp_ready(), 'No Chrome/Edge (CHROME_PATH or usual paths), Playwright present, or JOEDESIGN_SKIP_BROWSER set')
class CdpCaptureTests(unittest.TestCase):
    """2.0.2: capture.mjs without a Playwright package drives the installed browser over the DevTools protocol."""

    def test_capture_falls_back_to_cdp_with_actions_assertions_and_reduce_injection(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            project = root / 'project'
            project.mkdir()
            (project / 'index.html').write_text('<!doctype html><html lang="en"><title>Fixture</title>'
                '<link rel="stylesheet" href="s.css">'
                '<button onclick="document.querySelector(\'p\').textContent=\'Selected\'">Select</button>'
                '<p>Initial</p><div id="r">r</div></html>', encoding='utf-8')
            (project / 's.css').write_text('#r{animation:spin 1s infinite}@keyframes spin{to{opacity:0}}'
                '@media (prefers-reduced-motion: reduce){#r{animation:none}}', encoding='utf-8')
            class QuietHandler(SimpleHTTPRequestHandler):
                def log_message(self, *args):
                    pass
            server = ThreadingHTTPServer(('127.0.0.1', 0), partial(QuietHandler, directory=str(project)))
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            try:
                narrow = dict(id='narrow-selected', route='/', viewport=[390, 844], locale='en', theme='light', state='selected')
                wide = dict(id='wide-reduce', route='/', viewport=[1024, 768], locale='en', theme='light', state='default')
                settings = dict(base_url=f'http://127.0.0.1:{server.server_port}', probes={
                    narrow['id']: {'actions': [{'type': 'press', 'key': 'Tab'}, {'type': 'press', 'key': 'Enter'}],
                                   'assertions': [{'selector': 'p', 'text': 'Selected', 'visible': True},
                                                  {'selector': 'button', 'focused': True}]},
                    wide['id']: {'reduced_motion': 'inject', 'assertions': [{'selector': '#r', 'visible': True}]}})
                request = dict(output_dir=str(root / 'captures'), targets=[narrow, wide], build_id='cdp-fixture', browser=settings)
                argv = [os.environ.get('JOEDESIGN_NODE', 'node'), str(SCRIPTS / 'capture.mjs')]
                result = subprocess.run(argv, input=json.dumps(request), capture_output=True, text=True,
                                        encoding='utf-8', timeout=120)
                self.assertEqual(result.returncode, 0, result.stderr)
                output = json.loads(result.stdout)
                self.assertEqual(output['errors'], [])
                render = next(i for i in output['captures'] if i['kind'] == 'render')
                self.assertTrue(Path(render['path']).read_bytes().startswith(bytes.fromhex('89504e470d0a1a0a')))
                action = next(i for i in output['captures'] if i['kind'] == 'interaction')
                observed = json.loads(Path(action['path']).read_text(encoding='utf-8'))
                self.assertEqual(observed['driver'], 'cdp')
                self.assertEqual(observed['actions'][0]['focus']['tag'], 'BUTTON')
                self.assertTrue(observed['actions'][0]['focus']['visible'])
                self.assertEqual(observed['stylesheets'], [f"{settings['base_url']}/s.css"])
                record = json.loads((root / 'captures' / '1-observation.json').read_text(encoding='utf-8'))
                self.assertEqual(record['reduced_motion'], 'injected')
                self.assertEqual(record['reduce_injection'], {'rules': 1, 'unreadable': 0})
                request['output_dir'] = str(root / 'failed')
                settings['probes'][narrow['id']]['assertions'][0]['text'] = 'Never present'
                request['targets'] = [narrow]
                output = json.loads(subprocess.run(argv, input=json.dumps(request), capture_output=True, text=True,
                                                   encoding='utf-8', timeout=120).stdout)
                self.assertTrue(output['errors'])
                self.assertEqual(output['captures'], [])
            finally:
                server.shutdown()
                server.server_close()
                thread.join()

if __name__ == '__main__':
    unittest.main()
