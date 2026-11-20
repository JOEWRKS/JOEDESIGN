import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from harness_support import SCRIPTS, intent, proof_bundle


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

    def test_raci_command_returns_assignment_without_claiming_execution(self):
        from harness.io import write_artifact
        from harness.pipeline import ARTIFACTS
        target = self.root / 'proof'
        self.run_cli('init', target, '--intent', self.source)
        bundle, _ = proof_bundle(self.root)
        for key in ('intent', 'lock', 'contract', 'matrix', 'critique', 'evidence'):
            write_artifact(target / ARTIFACTS[key], bundle[key], overwrite=True)
        result = self.run_cli('raci', target, '--claim-id', 'structure')
        self.assertEqual(result.returncode, 0, result.stderr)
        plan = json.loads(result.stdout)
        self.assertEqual([step['step'] for step in plan['steps']], ['R', 'C1'])
        self.assertEqual([step['skill_id'] for step in plan['steps']], ['joedesign', 'impeccable'])
        self.assertEqual(plan['execution'], 'UNVERIFIED')

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

    def test_doctor_default_roots_follow_codex_home_not_the_real_home(self):
        import os
        fake_home = self.root / 'home'
        codex_home = self.root / 'codex-home'
        skill = codex_home / 'skills' / 'impeccable' / 'SKILL.md'
        skill.parent.mkdir(parents=True)
        skill.write_text('fixture', encoding='utf-8')
        (fake_home / '.codex' / 'skills' / 'ui-ux-pro-max').mkdir(parents=True)
        (fake_home / '.codex' / 'skills' / 'ui-ux-pro-max' / 'SKILL.md').write_text('home fixture', encoding='utf-8')
        env = {k: v for k, v in os.environ.items() if k != 'CODEX_HOME'}
        env.update(HOME=str(fake_home), USERPROFILE=str(fake_home), CODEX_HOME=str(codex_home))
        run = lambda env: subprocess.run([sys.executable, str(self.entry), 'doctor'], capture_output=True,
                                         text=True, encoding='utf-8', env=env)
        report = json.loads(run(env).stdout)['dependencies']
        self.assertEqual(Path(report['impeccable']['path']), skill.resolve())
        # CODEX_HOME replaces ~/.codex; the fake home's .codex copy is not read.
        self.assertEqual(report['ui-ux-pro-max']['status'], 'UNAVAILABLE')
        real_home = str(Path.home().resolve()).casefold()
        for entry in report.values():
            if entry['path'] and entry['status'] == 'AVAILABLE' and Path(entry['path']).name == 'SKILL.md':
                self.assertFalse(entry['path'].casefold().startswith(real_home) and
                                 not entry['path'].casefold().startswith(str(self.root.resolve()).casefold()))
        del env['CODEX_HOME']
        report = json.loads(run(env).stdout)['dependencies']
        self.assertEqual(Path(report['ui-ux-pro-max']['path']),
                         (fake_home / '.codex/skills/ui-ux-pro-max/SKILL.md').resolve())
        self.assertEqual(report['impeccable']['status'], 'UNAVAILABLE')

    def test_retrieve_with_string_requirements_names_the_required_row_shape(self):
        corpus = self.root / 'corpus'
        corpus.mkdir()
        (corpus / 'DESIGN.md').write_text('---\nid: a\nname: A\n---\nData comparison', encoding='utf-8')
        index = self.root / 'index.json'
        self.assertEqual(self.run_cli('index', corpus, '--output', index).returncode, 0)
        bad = intent()
        bad['requirements'] = ['Compare selected evidence']
        self.source.write_text(json.dumps(bad), encoding='utf-8')
        result = self.run_cli('retrieve', index, '--intent', self.source)
        self.assertEqual(result.returncode, 1)
        error = json.loads(result.stderr)
        self.assertEqual(error['status'], 'NOT_READY')
        self.assertNotIn('string indices', error['error'])
        for field in ('id', 'kind', 'description'):
            self.assertIn(field, error['error'])

    def test_shipped_intent_template_rows_have_the_validated_shape(self):
        from harness.contracts import validate_intent
        template = json.loads((SCRIPTS.parent / 'templates/DESIGN_INTENT.json').read_text(encoding='utf-8'))
        codes = {e['code'] for e in validate_intent(template)}
        self.assertNotIn('INVALID_ARTIFACT', codes)
        self.assertNotIn('INVALID_TARGET', codes)
        self.assertNotIn('INVALID_ID', codes)

    def test_bind_second_replace_failure_restores_both_original_artifacts(self):
        import importlib
        from unittest.mock import patch
        import os
        cli = importlib.import_module('harness_cli')
        target = self.root / 'proof'
        self.run_cli('init', target, '--intent', self.source)
        before = {p.name: p.read_bytes() for p in target.iterdir()}
        real_replace = os.replace
        failed = False

        def fail_manifest_once(source, destination):
            nonlocal failed
            if Path(destination).name == 'EVIDENCE_MANIFEST.json' and not failed:
                failed = True
                raise OSError('simulated Windows sharing violation')
            return real_replace(source, destination)

        with patch('harness.io.os.replace', side_effect=fail_manifest_once):
            with self.assertRaises(OSError):
                cli.main(['bind', str(target), '--run-id', 'run', '--build-id', 'build', '--context-id', 'builder'])
        self.assertEqual(before, {p.name: p.read_bytes() for p in target.iterdir() if p.is_file()})


if __name__ == '__main__':
    unittest.main()
