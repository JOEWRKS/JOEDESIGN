import tempfile
import unittest
from pathlib import Path
from harness_support import module, intent


class ReferenceTests(unittest.TestCase):
    def setUp(self):
        self.api = module(self, 'references')
        self.io = module(self, 'io')

    def test_actual_omd_frontmatter_preserves_unknown_quality(self):
        with tempfile.TemporaryDirectory() as folder:
            p = Path(folder) / 'linear.app'
            p.mkdir()
            (p / 'DESIGN.md').write_text('---\nid: linear.app\nname: Linear\ncategory: productivity\nverification_v2:\n  schema: 2\n---\n# Data comparison\n', encoding='utf-8')
            result = self.api.build_index(Path(folder))
            item = result['references'][0]
            self.assertEqual(item['id'], 'linear.app')
            self.assertEqual(item['quality'], 'UNKNOWN')
            self.assertEqual(item['inspection'], 'VISUAL_UNINSPECTED')
            self.assertEqual(len(item['sha256']), 64)

    def test_duplicate_reference_ids_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            for name in ['one', 'two']:
                p = Path(folder) / name
                p.mkdir()
                (p / 'DESIGN.md').write_text('---\nid: same\n---\n', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'duplicate'):
                self.api.build_index(Path(folder))

    def test_retrieval_is_shortlist_not_visual_fit_or_approval(self):
        with tempfile.TemporaryDirectory() as folder:
            p = Path(folder) / 'DESIGN.md'
            p.write_text('---\nid: data\n---\nData comparison', encoding='utf-8')
            result = self.api.retrieve(self.api.build_index(Path(folder)), intent())
            self.assertEqual([x['id'] for x in result['candidates']], ['data'])
            self.assertEqual(result['candidates'][0]['fit'], 'UNVERIFIED')
            self.assertEqual(result['candidates'][0]['unresolved_requirements'], ['compare', 'metrics'])

    def test_unicode_json_and_markdown_roundtrip_no_duplicate_keys(self):
        with tempfile.TemporaryDirectory() as folder:
            for suffix in ['.json', '.md']:
                p = Path(folder) / ('artifact' + suffix)
                self.io.write_artifact(p, {'label': '한글'}, overwrite=False)
                self.assertEqual(self.io.read_artifact(p), {'label': '한글'})
                with self.assertRaises(FileExistsError):
                    self.io.write_artifact(p, {'label': 'changed'}, overwrite=False)
            p.write_text('```json\n{"id":1,"id":2}\n```', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'duplicate'):
                self.io.read_artifact(p)

    def test_unknown_corpus_and_empty_query_are_not_success(self):
        with tempfile.TemporaryDirectory() as folder:
            with self.assertRaisesRegex(ValueError, 'reference'):
                self.api.build_index(Path(folder))
        with self.assertRaises(ValueError):
            self.api.retrieve({'references': []}, {'search_terms': []})


if __name__ == '__main__':
    unittest.main()
