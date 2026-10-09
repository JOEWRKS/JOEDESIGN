import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
from harness_support import module


class RunnerTests(unittest.TestCase):
    def setUp(self):
        self.api = module(self, 'runner')
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)

    def test_child_process_preserves_unicode_input_without_shell_expansion(self):
        text = '한글 $() `unchanged`'
        result = self.api.command([sys.executable, '-c',
            'import sys; sys.stdout.buffer.write(sys.stdin.buffer.read())'], self.root,
            self.root / 'call', text)
        self.assertEqual(result['exit_code'], 0)
        self.assertEqual((self.root / 'call/stdout.jsonl').read_text(encoding='utf-8'), text)

    def test_failure_and_timeout_keep_raw_outputs(self):
        for name, script, timeout in [('failed', 'print("before failure"); raise SystemExit(3)', 5),
                                      ('timeout', 'import time; print("started", flush=True); time.sleep(30)', .2)]:
            with self.assertRaisesRegex(ValueError, 'PROCESS_FAILED'):
                self.api.command([sys.executable, '-c', script], self.root, self.root / name, timeout=timeout)
            record = json.loads((self.root / name / 'process.json').read_text())
            self.assertNotEqual(record.get('exit_code'), 0)
            self.assertTrue((self.root / name / 'stdout.jsonl').read_bytes())

    def test_duplicate_missing_or_invented_claim_is_rejected(self):
        row = dict(claim_id='a', verdict='PASS', observed='seen', evidence_ids=['e'], cause='', hypothesis='')
        for rows in ([], [row, row], [dict(row, claim_id='other')]):
            with self.assertRaises(ValueError):
                self.api.validate_result(dict(status='COMPLETED', summary='review', claims=rows), ['a'])

    def test_missing_observation_is_not_a_valid_review(self):
        with self.assertRaises(ValueError):
            self.api.validate_result(dict(status='COMPLETED', summary='review', claims=[
                dict(claim_id='a', verdict='PASS', observed='', evidence_ids=[], cause='', hypothesis='')]), ['a'])

    def test_native_argv_separates_prompt_and_deduplicates_only_identical_images(self):
        images = [self.root / n for n in ('a.png','b.png','c.png')]
        for p, data in zip(images, (b'first',b'first',b'other')):
            p.write_bytes(data)
        result = dict(status='COMPLETED',summary='fixture',claims=[])
        seen = []
        def native(argv, project, folder, prompt, timeout):
            seen.extend(argv)
            folder.mkdir(parents=True)
            answer = json.dumps(result)
            Path(argv[argv.index('--output-last-message')+1]).write_text(answer)
            events = [{'type':'thread.started','thread_id':'fixture'},
                      {'type':'item.completed','item':{'type':'agent_message','text':answer}},
                      {'type':'turn.completed'}]
            (folder/'stdout.jsonl').write_text('\n'.join(map(json.dumps,events)))
            return {'exit_code':0}
        with patch.object(self.api, 'command', side_effect=native):
            self.api.CodexRunner(sys.executable).run({'claims':[]},self.root/'role',self.root,images=images)
        self.assertEqual(seen[-2:],['--','-'])
        self.assertEqual(seen.count('--image'),2)
        inp = json.loads((self.root/'role/input.json').read_text())
        self.assertEqual(len(inp['image_sources']),3)
        self.assertEqual(inp['image_sources'][1]['attached_as'],str(images[0].resolve()))
        self.assertEqual(inp['attachments'],[str(images[0].resolve()),str(images[2].resolve())])

    def test_review_packet_includes_bound_observations_and_scoped_source_only(self):
        from harness.io import file_hash
        project = self.root / 'project'; project.mkdir()
        (project/'AGENTS.md').write_text('Scoped authority')
        (project/'index.html').write_bytes(b'<button>Compare</button>\r\n')
        outside = self.root/'outside.txt';outside.write_text('excluded outside project')
        observation = self.root/'observation.json';observation.write_text('{"actual":"selected"}')
        changed = self.root/'changed.json';changed.write_text('{"stale":true}')
        task = {'claims':[{'id':'x'}], 'captures':[
            {'path':str(observation),'kind':'interaction','sha256':file_hash(observation)},
            {'path':str(changed),'kind':'technical','sha256':'wrong'}],
            'contract':{'translations':[{'implementation':{'component':'index.html'}},
                                        {'implementation':{'component':'../outside.txt'}}]}}
        def stop_before_native(argv, cwd, folder, prompt, timeout):
            packet = json.loads(prompt[prompt.index('{'):])
            sources = {s['path']:s for s in packet['source_context']}
            self.assertEqual(set(sources),set(map(str, [project/'AGENTS.md', project/'index.html', observation])))
            self.assertEqual(sources[str(project/'index.html')]['content'],'<button>Compare</button>\r\n')
            self.assertEqual(sources[str(observation)]['sha256'],file_hash(observation))
            raise ValueError('inspected packet')
        with patch.object(self.api,'command',side_effect=stop_before_native):
            with self.assertRaisesRegex(ValueError,'inspected packet'):
                self.api.CodexRunner(sys.executable).run(task,self.root/'context',project)


if __name__ == '__main__':
    unittest.main()
