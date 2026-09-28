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
    def test_core_package_bytes_stay_frozen(self):
        frozen = json.loads((ROOT / 'evals/harness-v0.1/baseline-package.json').read_text(encoding='utf-8-sig'))
        for entry in frozen:
            self.assertEqual(hashlib.sha256((ROOT / entry['path']).read_bytes()).hexdigest(), entry['sha256'])

    def test_discoverable_self_contained_harness_copy_runs_cli(self):
        source = ROOT / 'skills/joedesign-harness'
        self.assertTrue((source / 'SKILL.md').is_file(), 'Public skill missing')
        with tempfile.TemporaryDirectory() as folder:
            dest = Path(folder) / 'joedesign-harness'
            shutil.copytree(source, dest, ignore=shutil.ignore_patterns('__pycache__'))
            for relative in ['SKILL.md', 'references/operation.md']:
                p = dest / relative
                content = p.read_text(encoding='utf-8')
                for link in re.findall(r'\]\(([^)]+)\)', content):
                    if '://' not in link:
                        target = (p.parent / link.split('#')[0]).resolve()
                        self.assertTrue(target.is_relative_to(dest.resolve()))
                        self.assertTrue(target.is_file(), link)
            result = subprocess.run([sys.executable, str(dest / 'scripts/harness_cli.py'), '--help'],
                                    capture_output=True, text=True, encoding='utf-8', cwd=folder)
            self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == '__main__':
    unittest.main()
