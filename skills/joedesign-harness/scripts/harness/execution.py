"""Run bounded production work; existing evidence policy retains certification authority."""
from contextlib import contextmanager
import copy
import json
import os
from pathlib import Path
import shutil
import subprocess
import uuid

from .contracts import validate_intent, validate_lock, validate_contract
from .evidence import RACI_ROUTES, SKILL_IDS, assess, snapshot, validate_matrix, repair_disposition
from .io import digest, file_hash, read_artifact, write_artifact
from .pipeline import ARTIFACTS, load_bundle, make_role_bundle
from .runner import CodexRunner, command, validate_result


def project_fingerprint(project):
    """Tracked + nonignored files, including dirty/untracked edits; never just HEAD."""
    result = subprocess.run(['git', '-C', str(project), 'ls-files', '-z', '--cached', '--others',
                             '--exclude-standard'], capture_output=True, check=True)
    paths = sorted(set(result.stdout.decode('utf-8').split('\0')) - {''})
    records = []
    for name in paths:
        path = project / name
        if path.is_symlink() or (path.exists() and not path.resolve().is_relative_to(project)):
            raise ValueError('Project symlinks/escaped files require an explicit isolated checkout')
        records.append({'path': name, 'sha256': file_hash(path) if path.is_file() else 'MISSING'})
    return digest(records)


@contextmanager
def run_lock(root):
    path = root / 'execution.lock'
    try:
        fd = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        raise ValueError(f'EXECUTION_LOCKED: inspect {path}; never start a second writer') from None
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as stream:
            json.dump({'pid': os.getpid()}, stream)
        yield
    finally:
        path.unlink()


def skill_sources(settings):
    names = dict(SKILL_IDS)
    names['R'] = 'react-best-practices'
    roots = [Path(__file__).resolve().parents[3], Path.home() / '.codex/skills', Path.home() / '.agents/skills']
    result = {}
    for role, name in names.items():
        explicit = settings.get('skills', {}).get(role)
        candidates = [Path(explicit)] if explicit else [root / name / 'SKILL.md' for root in roots]
        path = next((p.resolve() for p in candidates if p.is_file()), None)
        if path:
            result[role] = path
    return result


def preflight(bundle, settings, project, root):
    errors = validate_intent(bundle['intent'])
    if not errors:
        errors += validate_lock(bundle['intent'], bundle['lock'])
        errors += validate_contract(bundle['intent'], bundle['lock'], bundle['contract'])
    if not errors:
        errors += validate_matrix(bundle)
    if errors:
        raise ValueError('EXECUTION_CONTRACT_INVALID: ' + str(errors))
    if root.is_relative_to(project) or project.is_relative_to(root):
        raise ValueError('Execution artifacts and project must be separate, non-nested directories')
    if not isinstance(settings.get('request'), str) or not settings['request'].strip():
        raise ValueError('An explicit authorized bounded request is required')
    if not isinstance(settings.get('collector_command'), list) or not settings['collector_command']:
        raise ValueError('collector_command must name an existing browser collector')
    if any(not isinstance(a, str) or not a for a in settings['collector_command']):
        raise ValueError('collector_command needs nonempty string arguments')
    if not shutil.which(settings['collector_command'][0]):
        raise ValueError('COLLECTOR_UNAVAILABLE: executable not found')
    git_root = subprocess.run(['git', '-C', str(project), 'rev-parse', '--show-toplevel'],
                             capture_output=True, text=True, encoding='utf-8', check=True).stdout.strip()
    if Path(git_root).resolve() != project:
        raise ValueError('project must be the explicit Git checkout root')
    if type(settings.get('timeout_seconds', 600)) is not int or settings.get('timeout_seconds', 600) < 1:
        raise ValueError('timeout_seconds must be a positive integer')
    if type(settings.get('max_cycles', 2)) is not int or not 1 <= settings.get('max_cycles', 2) <= 20:
        raise ValueError('max_cycles must be 1..20; exhaustion remains unresolved')
    skills = skill_sources(settings)
    required = {'J'} | {r for c in bundle['matrix']['claims'] if c['required']
                        for r in RACI_ROUTES[c['category']] if r != 'implementer'}
    missing = required - set(skills)
    if missing:
        raise ValueError('SPECIALIST_UNAVAILABLE: ' + ', '.join(sorted(missing)))
    for image in settings.get('reference_images', []):
        if not Path(image).is_file():
            raise ValueError('Original reference image unavailable: ' + image)
    return skills


class Execution:
    def __init__(self, root, project, settings, runner=None):
        self.root = Path(root).resolve(strict=True)
        self.project = Path(project).resolve(strict=True)
        self.settings = settings
        self.bundle = load_bundle(self.root)
        self.skills = preflight(self.bundle, settings, self.project, self.root)
        self.runner = runner or CodexRunner(settings['codex_executable'], settings.get('timeout_seconds', 600))
        self.state_path = self.root / 'EXECUTION_STATE.json'
        self.state = None
        self.harness_skill = Path(__file__).resolve().parents[2] / 'SKILL.md'
        self.identity = digest({'snapshot': snapshot(self.bundle), 'settings': settings,
            'project': str(self.project), 'skills': {r: file_hash(p) for r, p in self.skills.items()},
            'references': {str(p): file_hash(p) for p in settings.get('reference_images', [])},
            'runtime_files': {p: file_hash(p) for p in [settings['codex_executable'],
                *settings['collector_command']] if Path(p).is_file()},
            'policy': {p.name: file_hash(p) for p in Path(__file__).parent.glob('*.py')},
            'guidance': {str(p.relative_to(self.harness_skill.parent)): file_hash(p)
                         for p in [self.harness_skill, *sorted((self.harness_skill.parent / 'references').glob('*.md'))]}})

    def production_targets(self):
        """Require a complete representative family, not one convenient viewport."""
        kind = self.settings.get('work_kind')
        if kind not in ('new_direction', 'material_extension', 'local_repair'):
            raise ValueError('WORK_KIND_REQUIRED: classify new_direction, material_extension or local_repair')
        selected = self.settings.get('proof_target_ids')
        targets = self.bundle['intent']['targets']
        known = {t['id'] for t in targets}
        if (not isinstance(selected, list) or not selected or
                any(not isinstance(t, str) for t in selected) or
                len(set(selected)) != len(selected) or not set(selected) <= known):
            raise ValueError('PROOF_SCOPE_REQUIRED: explicit unique target IDs required before production')
        families = {t['family'] for t in targets if t['id'] in selected}
        if len(families) != 1 or set(selected) != {t['id'] for t in targets if t['family'] in families}:
            raise ValueError('PROOF_FAMILY_REQUIRED: include every contracted viewport/state of one representative family')
        if kind == 'local_repair' and set(selected) != known:
            raise ValueError('LOCAL_REPAIR_SCOPE: scope the affected family or classify material extension')
        return selected

    def save(self):
        write_artifact(self.state_path, self.state, overwrite=True)

    def step(self, key, inputs, operation, writable=False):
        identity = digest(inputs)
        previous = self.state['steps'].get(key)
        if previous and previous['status'] == 'COMPLETED':
            if previous['input_hash'] != identity:
                raise ValueError('STALE_EXECUTION_INPUT: ' + key)
            file = self.root / previous['result_path']
            if file_hash(file) != previous['result_hash']:
                raise ValueError('CHANGED_EXECUTION_RESULT: ' + key)
            return read_artifact(file)
        if previous and previous['status'] == 'RUNNING':
            raise ValueError('INTERRUPTED_STEP: inspect partial work before starting a new candidate run')
        if previous and writable and previous.get('before') != previous.get('after'):
            raise ValueError('PARTIAL_WRITE_REQUIRES_INSPECTION: preserve edits and start a reviewed candidate revision')
        attempt = self.root / 'execution' / (key + '-' + uuid.uuid4().hex[:12])
        before = project_fingerprint(self.project)
        if before != self.state['project_fingerprint'] or snapshot(load_bundle(self.root)) != snapshot(self.bundle):
            raise ValueError('STALE_EXECUTION: project or contract changed between steps')
        record = {'status': 'RUNNING', 'input_hash': identity, 'directory': str(attempt), 'before': before}
        self.state['steps'][key] = record
        self.save()
        try:
            output = operation(attempt)
            after = project_fingerprint(self.project)
            if not writable and before != after:
                raise ValueError('READ_ONLY_PHASE_CHANGED_PROJECT: ' + key)
            attempt.mkdir(parents=True, exist_ok=True)
            file = attempt / 'step-result.json'
            write_artifact(file, output)
            record.update(status='COMPLETED', after=after,
                          result_path=str(file.relative_to(self.root)), result_hash=file_hash(file))
            return output
        except BaseException as error:
            record.update(status='FAILED', error=str(error))
            self.state['status'] = 'BLOCKED'
            raise
        finally:
            record['after'] = project_fingerprint(self.project)
            self.state['project_fingerprint'] = record['after'] if writable else before
            self.save()

    def role(self, key, role, task, captures=(), writable=False):
        paths = list(dict.fromkeys([self.harness_skill] + ([self.skills[role]] if role in self.skills else [])))
        images = list(self.settings.get('reference_images', []))
        for item in captures:
            if item['kind'] == 'render':
                images.append(item['path'])
            images.extend(item.get('frames', []))
        images = list(dict.fromkeys(images))
        inputs = {'role': role, 'task': task, 'images': {p: file_hash(p) for p in images},
                  'skills': {str(p): file_hash(p) for p in paths}}
        def run(folder):
            result = self.runner.run(task, folder, self.project, paths, images, writable)
            validate_result(result['result'], [c['id'] for c in task.get('claims', [])])
            if result['result']['status'] != 'COMPLETED':
                raise ValueError('ROLE_BLOCKED: ' + result['result']['summary'])
            if task.get('claims'):
                self.checked_claims(result['result'], task['claims'], captures)
            contexts = self.state.setdefault('contexts', [])
            if not result.get('context_id') or result['context_id'] in contexts:
                raise ValueError('FRESH_CONTEXT_REQUIRED')
            contexts.append(result['context_id'])
            return result
        return self.step(key, inputs, run, writable)

    def collect(self, cycle, build, target_ids):
        targets = [t for t in self.bundle['intent']['targets'] if t['id'] in target_ids]
        def collect(folder):
            folder.mkdir(parents=True)
            request = {'project': str(self.project), 'output_dir': str(folder / 'captures'),
                       'targets': targets, 'build_id': build, 'browser': self.settings.get('browser', {})}
            command(self.settings['collector_command'], self.project, folder / 'process',
                    json.dumps(request), self.settings.get('timeout_seconds', 600))
            raw = read_artifact(folder / 'process/stdout.jsonl')
            if raw.get('errors') or not isinstance(raw.get('captures'), list):
                raise ValueError('BROWSER_OBSERVATION_FAILED: ' + str(raw.get('errors')))
            items = []
            for n, row in enumerate(raw['captures']):
                target = next((t for t in targets if t['id'] == row.get('target_id')), None)
                file = Path(row.get('path', '')).resolve(strict=True)
                frames = [Path(p).resolve(strict=True) for p in row.get('frames', [])]
                if (target is None or row.get('kind') not in ('render', 'interaction', 'technical') or
                        any(not p.is_relative_to(folder.resolve()) or not p.is_file() for p in [file, *frames])):
                    raise ValueError('INVALID_COLLECTOR_OUTPUT')
                items.append(dict(row, id=f'{cycle}-capture-{n}', target=target, path=str(file),
                    frames=list(map(str, frames)), sha256=file_hash(file),
                    frame_hashes={str(p): file_hash(p) for p in frames}, receipt_id='',
                    snapshot=snapshot(self.bundle), run_id=self.state['id'], build_id=build))
            pairs = {(i['target_id'], i['kind']) for i in items}
            required = {(c['target_id'], c['kind']) for c in self.bundle['matrix']['claims']
                        if c['required'] and c['target_id'] in target_ids}
            required |= {(t['id'], k) for t in targets for k in t['required_kinds']}
            if not required <= pairs:
                raise ValueError('OBSERVATION_INCOMPLETE: ' + str(sorted(required - pairs)))
            return {'items': items, 'build_id': build}
        packet = self.step(f'{cycle}-capture', {'build': build, 'settings': self.settings, 'targets': targets}, collect)
        for item in packet['items']:
            if file_hash(item['path']) != item['sha256'] or any(file_hash(p) != h for p, h in item['frame_hashes'].items()):
                raise ValueError('CHANGED_CAPTURE: ' + item['id'])
        return packet['items']

    def checked_claims(self, result, assigned, captures):
        by_id = {i['id']: i for i in captures}
        references = {r['id'] for r in self.bundle['lock']['references']}
        for row in result['claims']:
            claim = next(c for c in assigned if c['id'] == row['claim_id'])
            if any(i not in by_id and i not in references for i in row['evidence_ids']):
                raise ValueError('UNKNOWN_REVIEW_EVIDENCE')
            if row['verdict'] == 'PASS' and not any(i in by_id and by_id[i]['target_id'] == claim['target_id'] and
                                                  by_id[i]['kind'] == claim['kind'] for i in row['evidence_ids']):
                raise ValueError('REVIEW_EVIDENCE_MISSING')
            # The shipped collector samples frames, not continuous temporal quality.
            # Do not let a prose verdict promote those samples to observed motion.
            if claim.get('translation_id') and claim['kind'] == 'interaction' and row['verdict'] == 'PASS':
                row.update(verdict='UNVERIFIED', observed=row['observed'] +
                    ' Continuous motion inspection is not provided by the frame-sampling collector.', hypothesis='')
        return result['claims']

    def reviews(self, cycle, captures, target_ids):
        claims = [c for c in self.bundle['matrix']['claims'] if c['required'] and c['target_id'] in target_ids]
        rows, escalations = [], []
        base = make_role_bundle(self.bundle, 'critic')
        # No builder summaries, previous verdicts, or critic conclusions in review input.
        base.pop('captures', None)
        base['captures'] = captures
        base['matrix']['claims'] = copy.deepcopy(claims)
        base['matrix']['targets'] = [t for t in base['matrix']['targets'] if t['id'] in target_ids]
        base['review_scope'] = target_ids
        for rank in range(3):
            groups = {}
            for claim in claims:
                route = RACI_ROUTES[claim['category']]
                if rank >= len(route):
                    continue
                if rank == 2:
                    prior = [r for r in rows if r['claim_id'] == claim['id']]
                    needed = (len(claim['reviewers']) == 3 or claim.get('escalation_reason') or
                              len({r['verdict'] for r in prior}) > 1 or
                              any(r['verdict'] != 'PASS' for r in prior))
                    if not needed:
                        continue
                    escalations.append(claim['id'])
                groups.setdefault(route[rank], []).append(claim)
            for role, assigned in groups.items():
                task = dict(base, role=role, raci_step=('R', 'C1', 'C2')[rank], claims=assigned)
                if rank == 2:
                    task['diagnosis_request'] = [r for r in rows if r['claim_id'] in {c['id'] for c in assigned}]
                result = self.role(f'{cycle}-review-{rank}-{role}', role, task, captures)
                for row in result['result']['claims']:
                    rows.append(dict(row, reviewer=role, raci_step=('R', 'C1', 'C2')[rank],
                                     context_id=result['context_id']))
        critic_task = dict(base, role='critic', claims=claims,
            instruction=base['instruction'] + ' Review all assigned claims; missing technical/interaction proof stays UNVERIFIED.')
        critic = self.role(f'{cycle}-critic', 'J', critic_task, captures)
        return rows, critic, escalations

    def run(self, resume=False, review_only=False):
        with run_lock(self.root):
            mode = 'review' if review_only else 'production'
            if not review_only:
                self.production_targets()
            now = project_fingerprint(self.project)
            if self.state_path.exists():
                if not resume:
                    raise ValueError('Execution exists; use --resume or a separate candidate directory')
                self.state = read_artifact(self.state_path)
                if self.state.get('mode', 'production') != mode:
                    raise ValueError('EXECUTION_MODE_MISMATCH: preserve the original write authority')
                if self.state['identity'] != self.identity or self.state['project_fingerprint'] != now:
                    raise ValueError('STALE_EXECUTION: inputs or project changed; prepare a new candidate revision')
                if self.state['status'] in ('REVIEW_COMPLETE_UNCERTIFIED', 'NEEDS_REPAIR'):
                    for step in self.state['steps'].values():
                        if step.get('status') == 'COMPLETED' and file_hash(self.root / step['result_path']) != step['result_hash']:
                            raise ValueError('CHANGED_EXECUTION_RESULT')
                    completed_captures = self.state['report']['captures'] + self.state.get('proof_report', {}).get('captures', [])
                    for item in completed_captures:
                        if file_hash(item['path']) != item['sha256'] or any(file_hash(p) != h for p, h in item['frame_hashes'].items()):
                            raise ValueError('CHANGED_CAPTURE')
                    return self.state['report']
            else:
                self.state = {'id': uuid.uuid4().hex, 'identity': self.identity, 'project_fingerprint': now,
                              'status': 'RUNNING', 'mode': mode, 'steps': {}, 'contexts': []}
                write_artifact(self.state_path, self.state)
            self.state['status'] = 'RUNNING'
            self.state.pop('error', None)
            self.save()
            try:
                return self.produce()
            except (ValueError, OSError, subprocess.SubprocessError) as error:
                self.state.update(status='BLOCKED', error=str(error))
                self.save()
                return {'execution': 'BLOCKED', 'error': str(error), 'approved': False,
                        'trust': 'LOCAL_UNAUTHENTICATED', 'state': str(self.state_path)}

    def produce(self):
        review_only = self.state.get('mode') == 'review'
        all_targets = [t['id'] for t in self.bundle['intent']['targets']]
        proof_targets = all_targets if review_only else self.production_targets()
        expands = set(proof_targets) != set(all_targets)
        report = self.produce_phase(proof_targets, 'review' if review_only else 'proof',
                                    'proof-' if expands else '')
        if expands and report['execution'] == 'REVIEW_COMPLETE_UNCERTIFIED':
            self.state['proof_report'] = report
            self.save()
            # This is an operational gate on local role launches, not host certification.
            report = self.produce_phase(all_targets, 'expansion', 'expansion-')
        self.state.update(status=report['execution'], report=report)
        self.save()
        return report

    def produce_phase(self, target_ids, phase, prefix):
        base = make_role_bundle(self.bundle, 'synthesis')
        base['phase'] = phase
        base['phase_targets'] = [t for t in self.bundle['intent']['targets'] if t['id'] in target_ids]
        review_only = self.state.get('mode') == 'review'
        boundary = (' Work only on phase_targets. The full contract is context, not permission to implement '
                    'other families. A proof phase must establish the representative composition before expansion. '
                    'In expansion preserve the proved relationships and recheck the integrated result. ')
        plan = None if review_only else self.role(prefix + 'synthesis', 'J', dict(base, claims=[], request=self.settings['request'],
            instruction=base['instruction'] + boundary + ' Produce a bounded implementation plan, without editing or changing the locked direction.'))
        findings, attempts = [], []
        for cycle in range(1 if review_only else self.settings.get('max_cycles', 2)):
            cycle_key = f'{prefix}{cycle}'
            task = dict(base, role='implementer' if cycle == 0 else 'repair', claims=[],
                request=self.settings['request'], contract=self.bundle['contract'],
                plan=plan['result']['summary'] if plan else '', findings=findings,
                instruction=boundary + 'Implement the authorized bounded slice using the originals and actual assets. '
                'Observe your result with available project tools. Fix the diagnosed cause; preserve protected regions. '
                'If a structural change requires a new contract or approval, return BLOCKED with that reason. '
                'Do not alter harness artifacts or manufacture evidence. Missing capabilities must be reported.')
            implementation = None if review_only else self.role(f'{cycle_key}-implement', 'J', task, writable=True)
            build = project_fingerprint(self.project) if review_only else self.state['steps'][f'{cycle_key}-implement']['after']
            captures = self.collect(cycle_key, build, target_ids)
            rows, critic, escalations = self.reviews(cycle_key, captures, target_ids)
            findings = [r for r in rows + critic['result']['claims'] if r['verdict'] != 'PASS']
            # Count unresolved claims once per cycle, not once per reviewer. Stable
            # claim identity prevents paraphrased causes from resetting the limit.
            for claim in (c for c in self.bundle['matrix']['claims'] if c['required'] and c['target_id'] in target_ids):
                failures = [r for r in findings if r['claim_id'] == claim['id']]
                attempts.append({'cause_id': claim['id'], 'outcome': 'FAIL' if failures else 'IMPROVED',
                                 'hypothesis': ' | '.join(r['hypothesis'] for r in failures)
                                 if failures and all(r['hypothesis'].strip() for r in failures) else ''})
            structural = {c['id'] for c in self.bundle['matrix']['claims'] if c['category'] == 'Structure'}
            disposition = repair_disposition(attempts, [dict(r, kind='structural' if r['claim_id'] in structural
                                                            else 'local') for r in findings])
            manifest = copy.deepcopy(self.bundle['evidence'])
            manifest['run'] = {k: self.bundle['intent'][k] for k in ('candidate_id', 'revision', 'scope_id')} | {
                'run_id': self.state['id'], 'build_id': build, 'snapshot': snapshot(self.bundle),
                'implementation_context': implementation['context_id'] if implementation else ''}
            manifest.setdefault('items', []).extend(captures)
            # Keep local reviews in execution records; do not synthesize skill_use/host receipts.
            local_bundle = dict(self.bundle, evidence=manifest)
            assessment = assess(local_bundle)
            report = {'execution': 'NEEDS_REPAIR' if findings else 'REVIEW_COMPLETE_UNCERTIFIED',
                      'phase': phase, 'target_ids': target_ids,
                      'unreviewed_target_ids': [t['id'] for t in self.bundle['intent']['targets'] if t['id'] not in target_ids],
                      'mode': self.state.get('mode', 'production'),
                      'approved': False, 'user_acceptance': 'PENDING', 'trust': 'LOCAL_UNAUTHENTICATED',
                      'cycle': cycle, 'build_id': build, 'captures': captures, 'reviews': rows,
                      'critic': critic['result'], 'escalations': escalations, 'findings': findings,
                      'repair_disposition': disposition, 'repair_attempts': copy.deepcopy(attempts),
                      'assessment': assessment, 'state': str(self.state_path)}
            report_path = self.root / f'EXECUTION_REPORT-{cycle_key}.json'
            if report_path.exists():
                if read_artifact(report_path) != report:
                    raise ValueError('CHANGED_EXECUTION_REPORT')
            else:
                write_artifact(report_path, report)
            # No policy state or exact-approval mutation. Original seven artifacts stay intact.
            if review_only or not findings or disposition != 'CONTINUE' or cycle + 1 == self.settings.get('max_cycles', 2):
                return report
        raise AssertionError('unreachable')
