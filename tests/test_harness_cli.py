import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from harness_support import SCRIPTS, intent


class CLITests(unittest.TestCase):
    def setUp(self):
        self.entry = SCRIPTS / 'harness_cli.py'
        self.assertTrue(self.entry.is_file(), 'Missing runnable harness CLI')
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.source = self.root / 'intent.json'
        self.source.write_text(json.dumps(intent()), encoding='utf-8')

    def run_cli(self, *args):
        return subprocess.run([sys.executable, str(self.entry), *map(str, args)],
                              capture_output=True, text=True, encoding='utf-8')

    def test_init_seven_artifacts_and_second_init_preserves_bytes(self):
        target = self.root / 'proof'
        first = self.run_cli('init', target, '--intent', self.source)
        self.assertEqual(first.returncode, 0, first.stderr)
        before = {p.name: p.read_bytes() for p in target.iterdir()}
        self.assertEqual(len(before), 7)
        second = self.run_cli('init', target, '--intent', self.source)
        self.assertNotEqual(second.returncode, 0)
        self.assertEqual(before, {p.name: p.read_bytes() for p in target.iterdir()})
        report = self.run_cli('check', target)
        self.assertEqual(report.returncode, 2)
        self.assertFalse(json.loads(report.stdout)['approved'])

    def test_failed_transition_preserves_manifest(self):
        target = self.root / 'proof'
        self.run_cli('init', target, '--intent', self.source)
        p = target / 'EVIDENCE_MANIFEST.json'
        before = p.read_bytes()
        result = self.run_cli('advance', target, 'IMPLEMENTED')
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(p.read_bytes(), before)

    def test_real_index_retrieve_cli_and_unicode(self):
        corpus = self.root / 'corpus'
        corpus.mkdir()
        (corpus / 'DESIGN.md').write_text('---\nid: korean\nname: 한글\n---\nData comparison', encoding='utf-8')
        index = self.root / 'index.json'
        result = self.run_cli('index', corpus, '--output', index)
        self.assertEqual(result.returncode, 0, result.stderr)
        result = self.run_cli('retrieve', index, '--intent', self.source)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)['candidates'][0]['name'], '한글')

    def test_doctor_reports_missing_dependencies_without_installing(self):
        empty = self.root / 'skills'
        empty.mkdir()
        result = self.run_cli('doctor', '--skills-root', empty)
        self.assertEqual(result.returncode, 2)
        self.assertTrue(result.stdout.strip(), 'Doctor capability is not implemented')
        report = json.loads(result.stdout)
        self.assertFalse(report['ready_for_synthesis'])
        self.assertEqual(report['host_verifier'], 'UNAVAILABLE')
        self.assertEqual(list(empty.iterdir()), [])


if __name__ == '__main__':
    unittest.main()
