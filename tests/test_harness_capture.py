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


if __name__ == '__main__':
    unittest.main()
