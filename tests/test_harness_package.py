import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from harness_support import ROOT


class PackageTests(unittest.TestCase):
    def test_historical_package_bytes_stay_bound_to_original_evidence(self):
        archive = ROOT / 'fixtures/package-history/pre-unification-20261009'
        frozen = json.loads((ROOT / 'evals/harness-v0.1/baseline-package.json').read_text(encoding='utf-8-sig'))
        for entry in frozen:
            self.assertEqual(hashlib.sha256((archive / entry['path']).read_bytes()).hexdigest(), entry['sha256'])
        for entry in json.loads((archive / 'manifest.json').read_text())['files']:
            self.assertEqual(hashlib.sha256((archive / entry['path']).read_bytes()).hexdigest(), entry['sha256'])

    def test_single_self_contained_skill_copy_runs_cli_without_sibling_harness(self):
        source = ROOT / 'skills/joedesign'
        self.assertEqual(list((ROOT / 'skills').rglob('SKILL.md')), [source / 'SKILL.md'])
        self.assertTrue((source / 'SKILL.md').is_file(), 'Public skill missing')
        with tempfile.TemporaryDirectory() as folder:
            dest = Path(folder) / 'joedesign'
            shutil.copytree(source, dest, ignore=shutil.ignore_patterns('__pycache__'))
            for p in [dest / 'SKILL.md', *(dest / 'references').glob('*.md')]:
                content = p.read_text(encoding='utf-8')
                for link in re.findall(r'\]\(([^)]+)\)', content):
                    if '://' not in link:
                        target = (p.parent / link.split('#')[0]).resolve()
                        self.assertTrue(target.is_relative_to(dest.resolve()))
                        self.assertTrue(target.is_file(), link)
            result = subprocess.run([sys.executable, str(dest / 'scripts/harness_cli.py'), '--help'],
                                    capture_output=True, text=True, encoding='utf-8', cwd=folder)
            self.assertEqual(result.returncode, 0, result.stderr)
            version = subprocess.run([sys.executable, str(dest / 'scripts/harness_cli.py'), 'version'],
                                     capture_output=True, text=True, encoding='utf-8', cwd=folder)
            self.assertEqual(version.returncode, 0, version.stderr)
            self.assertEqual(json.loads(version.stdout)['version'], (dest / 'VERSION').read_text().strip())
            self.assertEqual(Path(json.loads(version.stdout)['operating_core']), dest / 'SKILL.md')

    def test_copied_doctor_uses_own_core_even_with_an_old_installed_core(self):
        with tempfile.TemporaryDirectory() as folder:
            dest = Path(folder) / 'standalone/joedesign'
            shutil.copytree(ROOT / 'skills/joedesign', dest, ignore=shutil.ignore_patterns('__pycache__'))
            external = Path(folder) / 'installed'
            for name in ('joedesign', 'impeccable', 'ui-ux-pro-max', 'web-design-guidelines'):
                p = external / name / 'SKILL.md'
                p.parent.mkdir(parents=True)
                p.write_text('Old installed core' if name == 'joedesign' else 'Synthetic external specialist')
            command = [sys.executable, str(dest / 'scripts/harness_cli.py'), 'doctor', '--skills-root', str(external)]
            result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8', cwd=folder)
            self.assertEqual(result.returncode, 0, result.stderr)
            report = json.loads(result.stdout)
            self.assertTrue(report['ready_for_synthesis'])
            self.assertEqual(Path(report['dependencies']['joedesign']['path']), dest / 'SKILL.md')
            self.assertFalse(report['automatic_certification'])
            (external / 'impeccable/SKILL.md').unlink()
            missing = subprocess.run(command, capture_output=True, text=True, encoding='utf-8', cwd=folder)
            self.assertEqual(missing.returncode, 2, missing.stderr)
            self.assertFalse(json.loads(missing.stdout)['ready_for_synthesis'])
            (external / 'impeccable/SKILL.md').write_text('Synthetic external specialist')
            (dest / 'references/visual-translation.md').unlink()
            incomplete = subprocess.run(command, capture_output=True, text=True, encoding='utf-8', cwd=folder)
            self.assertEqual(incomplete.returncode, 2, incomplete.stderr)
            self.assertFalse(json.loads(incomplete.stdout)['internal_modules']['visual-translation.md'])


if __name__ == '__main__':
    unittest.main()
