"""Bounded, read-only DESIGN impact diagnosis. Never authorizes evidence reuse."""
import hashlib
import json
from pathlib import Path
import re

from .conformance import evaluate, input_fingerprint, input_path, load_baseline
from .io import digest, unique_pairs


def _need(ok, message):
    if not ok:
        raise ValueError(message)


def _text(value):
    return isinstance(value, str) and bool(value.strip())


def _sha(value):
    return isinstance(value, str) and re.fullmatch('[a-f0-9]{64}', value) is not None


def _unique(rows, key):
    _need(isinstance(rows, list), 'Expected list: ' + key)
    result = {}
    for row in rows:
        _need(isinstance(row, dict) and _text(row.get(key)) and row[key] not in result,
              'Missing/duplicate identity: ' + key)
        result[row[key]] = row
    return result


class Reader:
    def __init__(self, project, evidence_roots):
        self.project = Path(project).resolve(strict=True)
        self.roots = [self.project, *(Path(p).resolve(strict=True) for p in evidence_roots)]
        self.seen = {}
        self.aliases = {}

    def read(self, name, expected=None, evidence=False):
        _need(isinstance(name, str), 'Invalid path')
        if evidence and Path(name).is_absolute():
            path = Path(name).resolve(strict=True)
            _need(any(path.is_relative_to(p) for p in self.roots), 'Evidence outside allowed roots')
        else:
            path = input_path(self.project, name)
        _need(path.is_file() and path.stat().st_size <= 64 * 1024 * 1024, 'Invalid/oversize input')
        raw = path.read_bytes()
        actual = hashlib.sha256(raw).hexdigest()
        if expected is not None:
            _need(_sha(expected) and actual == expected, 'Pinned bytes changed: ' + name)
        _need(path not in self.seen or self.seen[path] == actual, 'Input changed during diagnosis')
        self.seen[path] = actual
        self.aliases[(name, evidence)] = path
        return raw

    def ref(self, value):
        _need(isinstance(value, dict) and _sha(value.get('sha256')), 'Invalid pinned reference')
        return self.read(value['path'], value['sha256'])

    def json(self, value):
        data = json.loads(self.ref(value).decode('utf-8-sig'), object_pairs_hook=unique_pairs,
                          parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)))
        _need(isinstance(data, dict), 'Expected JSON object')
        return data

    def verify(self):
        for (name, evidence), previous in self.aliases.items():
            current = (Path(name).resolve(strict=True) if evidence and Path(name).is_absolute()
                       else input_path(self.project, name))
            _need(current == previous, 'Input path changed during diagnosis')
        for path, expected in self.seen.items():
            _need(path.resolve(strict=True) == path and
                  hashlib.sha256(path.read_bytes()).hexdigest() == expected,
                  'Input changed during diagnosis: ' + str(path))


def inspect_impact(project, request_path, request_sha256, review_sha256=None, evidence_roots=()):
    """Return candidates and reasons; no mutation, pin refresh or new PASS receipt."""
    report = {'schema': 'joedesign.impact.v1', 'scope_id': None, 'reuse_authorized': False,
              'acceptance': 'NOT_GRANTED', 'trust': 'LOCAL_UNAUTHENTICATED',
              'checks': [], 'authority_delta': [], 'findings': [],
              'limits': ['Append-only reviewed DESIGN changes; no selector/CSS impact precision',
                         'Local pins/contexts do not authenticate reviewers or approval',
                         'Served dependency completeness requires actual scoped collection and review',
                         'Candidate only; existing gate remains authoritative until separately reviewed consumption']}
    reader = Reader(project, evidence_roots)
    def finding(kind, code, detail):
        report['findings'].append({'kind': kind, 'code': code, 'detail': str(detail)})
    try:
        request_path = Path(request_path).resolve(strict=True)
        request_ref = {'path': request_path.relative_to(reader.project).as_posix(), 'sha256': request_sha256}
        request = reader.json(request_ref)
        _need(request.get('schema') == 'joedesign.impact-request.v1', 'Unsupported request schema')
        report['request'] = request_ref
        for name in ('old_baseline', 'new_baseline', 'old_result', 'served', 'review', 'authority_before'):
            report[name] = request.get(name)
        transition = digest({k: v for k, v in request.items() if k != 'review'})
        report['transition_sha256'] = transition
        old, new = reader.json(request['old_baseline']), reader.json(request['new_baseline'])
        # Current source must validate normally; the old baseline is checked for exact
        # structural equivalence below, without weakening load_baseline's authority check.
        load_baseline(input_path(reader.project, request['new_baseline']['path']),
                      request['new_baseline']['sha256'], reader.project)
        report['scope_id'] = new['scope_id']
        old_checks = _unique(old['required_checks'], 'check_id')
        new_checks = _unique(new['required_checks'], 'check_id')
        report['checks'] = [dict(check_id=c['check_id'], target_id=c['target_id'],
            method=c['method'], criterion_sha256=c['criterion_sha256'],
            classification='unknown', reasons=[]) for c in new['required_checks']]
        _need(set(old_checks) == set(new_checks), 'Required coverage changed')
        context = lambda b: {k: v for k, v in b.items() if k not in ('authority', 'authorization_ref')}
        _need(digest(context(old)) == digest(context(new)), 'Baseline context/criterion/target/acceptance changed')
        old_authority, new_authority = _unique(old['authority'], 'path'), _unique(new['authority'], 'path')
        snapshots = _unique(request['authority_before'], 'path')
        _need(set(old_authority) == set(new_authority) == set(snapshots), 'Authority coverage changed')
        # No opaque authority field can be silently waived by the hash exception.
        for name, before in old_authority.items():
            _need({k: v for k, v in before.items() if k != 'sha256'} ==
                  {k: v for k, v in new_authority[name].items() if k != 'sha256'},
                  'Authority definition changed')
        if not review_sha256:
            finding('unknown', 'REVIEW_REQUIRED', 'Independent semantic-review pin missing')
            return report
        _need(request['review']['sha256'] == review_sha256, 'Independent review pin mismatch')
        review = reader.json(request['review'])
        _need(review.get('schema') == 'joedesign.impact-review.v1' and
              review.get('scope_id') == new['scope_id'] and review.get('transition_sha256') == transition,
              'Semantic review transition mismatch')
        _need(_text(review.get('implementation_context')) and _text(review.get('review_context')) and
              review['implementation_context'] != review['review_context'] and _text(review.get('scope_analysis')),
              'Substantive independent review missing')
        analyses = _unique(review.get('authority_analysis'), 'path')
        _need(set(analyses) == set(old_authority), 'Authority review incomplete')
        reviewed = _unique(review.get('checks'), 'check_id')
        _need(set(reviewed) <= set(new_checks), 'Unknown review check')
        for name, before in old_authority.items():
            snapshot = snapshots[name]['snapshot']
            _need(snapshot['sha256'] == before['sha256'], 'Old authority snapshot binding mismatch')
            a = reader.ref(snapshot)
            b = reader.read(name, new_authority[name]['sha256'])
            analysis = analyses[name]
            _need(_text(analysis.get('rationale')), 'Authority rationale missing')
            kind = analysis.get('kind')
            suffix = b[len(a):] if b.startswith(a) else b''
            if a == b:
                _need(kind == 'UNCHANGED', 'Authority review contradicts unchanged bytes')
            else:
                _need(name == 'DESIGN.md', 'Only root DESIGN.md changes supported')
                _need(b.startswith(a) and suffix, 'Existing DESIGN bytes changed; fresh review required')
                content = suffix.decode('utf-8').strip()
                if kind == 'COMMENT_APPEND':
                    _need(content.startswith('<!--') and content.endswith('-->') and
                          '-->' not in content[4:-3], 'Not one append-only comment')
                elif kind == 'UNRELATED_SECTION_APPEND':
                    _need(suffix.startswith((b'\n', b'\r\n')) and content.startswith('## '), 'Not an appended section')
                    heading = content.splitlines()[0]
                    _need(heading not in a.decode('utf-8').splitlines(), 'Appended heading duplicates existing section')
                else:
                    raise ValueError('Unsupported authority change')
            report['authority_delta'].append({'path': name, 'old_sha256': before['sha256'],
                'new_sha256': new_authority[name]['sha256'], 'kind': kind,
                'appended_sha256': hashlib.sha256(suffix).hexdigest(), 'rationale': analysis['rationale']})

        receipt = reader.json(request['old_result'])
        _need(receipt.get('schema') == 'joedesign.conformance.v1' and
              receipt.get('scope_id') == new['scope_id'] and
              receipt.get('baseline_sha256') == request['old_baseline']['sha256'] and
              receipt.get('acceptance') == 'NOT_GRANTED', 'Old result identity/acceptance mismatch')
        prior = _unique(receipt.get('results'), 'check_id')
        _need(set(prior) == set(old_checks), 'Old result incomplete/extra coverage')
        unresolved = _unique(receipt.get('unresolved'), 'check_id')
        _need(set(unresolved) <= set(old_checks), 'Unknown unresolved check')
        served = reader.json(request['served'])
        _need(served.get('schema') == 'joedesign.served-build.v1' and
              served.get('scope_id') == new['scope_id'] and
              served.get('baseline_sha256') == request['new_baseline']['sha256'], 'Served scope/baseline mismatch')
        target_map = _unique(new['targets'], 'id')
        served_map = {}
        for target in served.get('targets', []):
            tid = target['target']['id']
            _need(tid not in served_map and tid in target_map, 'Duplicate/unknown served target')
            served_map[tid] = target
        _need(set(served_map) == set(target_map), 'Served target coverage missing')

        for row in report['checks']:
            cid = row['check_id']; check = new_checks[cid]; previous = prior[cid]
            row['previous_result'] = previous
            try:
                for name in check['inputs']:
                    reader.read(name)
                fingerprint = input_fingerprint(reader.project, check['inputs'])
                row['input_fingerprint'] = fingerprint
                _need(all(previous.get(k) == check[k] for k in ('check_id', 'target_id', 'method', 'criterion_sha256')),
                      'Previous criterion identity mismatch')
                if previous.get('input_fingerprint') != fingerprint:
                    row.update(classification='rerun', reasons=['Runtime input bytes changed; no CSS precision claimed'])
                    continue
                _need(previous.get('status') == 'PASS' and cid not in unresolved,
                      'Previous failure/unverified/unresolved result retained')
                _need(check['method'] == 'geometry', 'v1 reuses geometry only; specialist claims need fresh scoped review')
                decision = reviewed.get(cid)
                _need(decision and _text(decision.get('rationale')) and
                      isinstance(decision.get('blocking_findings'), list), 'Per-check reviewed rationale missing')
                _need(decision.get('verdict') in ('UNAFFECTED', 'AFFECTED', 'UNKNOWN'), 'Invalid impact verdict')
                _need(decision.get('source_refs'), 'Per-check actual source references missing')
                for evidence in decision['source_refs']:
                    reader.ref(evidence)
                if decision['verdict'] == 'AFFECTED':
                    row.update(classification='rerun', reasons=[decision['rationale']]); continue
                _need(decision['verdict'] == 'UNAFFECTED' and not decision['blocking_findings'],
                      'Review unknown or blocking finding/rejection retained')
                target = served_map[check['target_id']]
                _need(target['target'] == target_map[check['target_id']] and _text(target.get('build_id')),
                      'Served target/build identity mismatch')
                _need(target.get('dependencies_complete') is True and target.get('limitations') == [],
                      'Conditional/late/served dependencies unverified')
                resources = _unique(target.get('resources'), 'path')
                expected_inputs = set().union(*(set(c['inputs']) for c in new_checks.values()
                                               if c['target_id'] == check['target_id']))
                _need(set(resources) == expected_inputs, 'Served dependency coverage mismatch')
                for name, resource in resources.items():
                    reader.read(name, resource['sha256'])
                    _need(resource.get('response_sha256') == resource['sha256'], 'Served response differs from current file')
                _need(isinstance(previous.get('evidence'), list) and previous['evidence'], 'Previous evidence missing')
                logs = []
                bound_paths = set()
                for proof in previous['evidence']:
                    raw = reader.read(proof['path'], proof['sha256'], evidence=True)
                    bound_paths.add(Path(proof['path']).resolve() if Path(proof['path']).is_absolute()
                                    else input_path(reader.project, proof['path']))
                    try:
                        log = json.loads(raw.decode('utf-8-sig'), object_pairs_hook=unique_pairs)
                    except (ValueError, UnicodeError):
                        continue
                    if isinstance(log, dict) and 'target' in log and 'design' in log:
                        logs.append((proof['path'], log))
                _need(len(logs) == 1, 'Missing/ambiguous previous target observation')
                log_path, log = logs[0]
                _need(isinstance(log.get('design'), dict), 'Malformed previous design observation')
                _need(log.get('target') == target['target'] and log.get('build_id') == target['build_id'] and
                      log.get('design', {}).get('baseline_sha256') == request['old_baseline']['sha256'] and
                      log.get('design', {}).get('input_fingerprints', {}).get(cid) == fingerprint,
                      'Observed target/baseline/build/input mismatch')
                _need(isinstance(log.get('frames'), list) and log['frames'], 'Rendered frame missing')
                _need(isinstance(log.get('frame_hashes'), dict), 'Rendered frame hashes missing')
                for frame in log['frames']:
                    _need(_sha(log['frame_hashes'].get(frame)), 'Rendered frame hash missing')
                    reader.read(frame, log['frame_hashes'][frame], evidence=True)
                    resolved = Path(frame).resolve() if Path(frame).is_absolute() else input_path(reader.project, frame)
                    _need(resolved in bound_paths, 'Frame not bound in old result')
                absolute_log = Path(log_path) if Path(log_path).is_absolute() else input_path(reader.project, log_path)
                evaluated = evaluate(old, request['old_baseline']['sha256'], reader.project, [absolute_log],
                                     target_ids=[check['target_id']])
                proof_row = next(r for r in evaluated['results'] if r['check_id'] == cid)
                _need(proof_row['status'] == 'PASS', 'Prior measured result not reproducible from immutable evidence')
                row.update(classification='reusable-candidate', reasons=[decision['rationale']],
                           target=target['target'], build_id=target['build_id'])
            except (ValueError, OSError, KeyError, TypeError, StopIteration) as error:
                row.update(classification='unknown', reasons=[str(error)])
    except (ValueError, OSError, KeyError, TypeError) as error:
        finding('invalid', 'IMPACT_INPUT_INVALID', error)
        for row in report['checks']:
            row.update(classification='unknown', reasons=[str(error)])
    finally:
        try:
            reader.verify()
        except (ValueError, OSError) as error:
            finding('unknown', 'CHANGED_DURING_READ', error)
            for row in report['checks']:
                row.update(classification='unknown', reasons=['Inputs changed during diagnosis'])
        report['integrity'] = [{'path': str(p), 'sha256': h} for p, h in sorted(reader.seen.items())]
        report['counts'] = {k: sum(c['classification'] == k for c in report['checks'])
                            for k in ('reusable-candidate', 'rerun', 'unknown')}
    return report
