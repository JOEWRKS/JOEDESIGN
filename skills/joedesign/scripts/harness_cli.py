#!/usr/bin/env python3
"""Run from a project or copied skill; no installation/dependencies required."""
import argparse
import json
import sys
from pathlib import Path
from harness.io import read_artifact, write_artifact, write_artifacts_transaction, digest, file_hash
from harness.references import build_index, retrieve
from harness.contracts import guard_change
from harness.evidence import assess, snapshot, raci_plan
from harness.pipeline import ARTIFACTS, init_bundle, load_bundle, transition, current_stage, make_role_bundle, validate_handoff, repair_disposition


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('version', help='Identify the single JOEDESIGN package')
    p = sub.add_parser('verify-design', help='Evaluate pinned rule coverage and actual observations; no acceptance')
    p.add_argument('--baseline', type=Path, required=True)
    p.add_argument('--baseline-sha256', required=True)
    p.add_argument('--project', type=Path, required=True)
    p.add_argument('--observation', type=Path, action='append', default=[])
    p.add_argument('--reviews', type=Path)
    p.add_argument('--output', type=Path)
    p = sub.add_parser('doctor'); p.add_argument('--skills-root', type=Path, action='append')
    p = sub.add_parser('init'); p.add_argument('root', type=Path); p.add_argument('--intent', type=Path, required=True)
    p = sub.add_parser('index'); p.add_argument('corpus', type=Path); p.add_argument('--output', type=Path)
    p = sub.add_parser('retrieve'); p.add_argument('index', type=Path); p.add_argument('--intent', type=Path, required=True); p.add_argument('--limit', type=int, default=10); p.add_argument('--output', type=Path)
    p = sub.add_parser('run', help='Execute bounded production/review; does not authenticate approval')
    p.add_argument('root', type=Path); p.add_argument('--project', type=Path, required=True)
    p.add_argument('--runtime', type=Path, required=True); p.add_argument('--resume', action='store_true')
    p.add_argument('--check-only', action='store_true', help='Validate execution inputs without launching roles')
    p.add_argument('--review-only', action='store_true', help='Capture/review current source without implementation or repair')
    for name in ('check', 'handoff', 'advance', 'bundle', 'bind', 'guard', 'repair', 'raci'):
        p = sub.add_parser(name); p.add_argument('root', type=Path)
        if name == 'advance': p.add_argument('stage')
        if name == 'bundle': p.add_argument('role', choices=['synthesis', 'craft', 'critic', 'expand'])
        if name in ('handoff', 'bundle'): p.add_argument('--output', type=Path)
        if name == 'handoff': p.add_argument('--validate', type=Path)
        if name == 'guard': p.add_argument('--change', type=Path, required=True)
        if name == 'raci': p.add_argument('--claim-id', required=True)
        if name == 'bind': p.add_argument('--run-id', required=True); p.add_argument('--build-id', required=True); p.add_argument('--context-id', required=True)
    args = parser.parse_args(argv)
    code = 0
    package = Path(__file__).resolve().parents[1]
    if args.command == 'verify-design':
        from harness.conformance import load_baseline, evaluate
        baseline = load_baseline(args.baseline, args.baseline_sha256, args.project)
        result = evaluate(baseline, args.baseline_sha256, args.project, args.observation, args.reviews)
        code = 0 if result['eligible'] else 2
    elif args.command == 'version':
        result = {'name': 'joedesign', 'version': (package / 'VERSION').read_text().strip(),
                  'operating_core': str(package / 'SKILL.md')}
    elif args.command == 'doctor':
        from harness.execution import skill_sources, VISUAL_MODULE_NAMES
        settings = {'skills_roots': args.skills_root} if args.skills_root else {}
        sources = skill_sources(settings)
        dependencies = {}
        for role, name in (('J', 'joedesign'), ('I', 'impeccable'), ('U', 'ui-ux-pro-max'),
                           ('V', 'web-design-guidelines'), ('R', 'react-best-practices'),
                           ('M', 'optimize-web-animations')):
            found = sources.get(role)
            dependencies[name] = {'status': 'AVAILABLE' if found else 'UNAVAILABLE',
                                  'path': str(found) if found else None,
                                  'sha256': file_hash(found) if found else None}
        modules = {name: (package / 'references' / name).is_file() for name in VISUAL_MODULE_NAMES}
        ready = all(modules.values()) and all(dependencies[n]['status'] == 'AVAILABLE' for n in
                    ('joedesign', 'impeccable', 'ui-ux-pro-max', 'web-design-guidelines'))
        result = {'dependencies': dependencies, 'ready_for_synthesis': ready,
                  'internal_modules': modules,
                  'version': (package / 'VERSION').read_text().strip(),
                  'operating_core': str(package / 'SKILL.md'),
                  'host_verifier': 'UNAVAILABLE', 'automatic_certification': False,
                  'note': 'Availability and file identity do not prove skill invocation or behavior.'}
        code = 0 if ready else 2
    elif args.command == 'run':
        from harness.execution import Execution
        execution = Execution(args.root, args.project, read_artifact(args.runtime))
        if args.check_only:
            if not args.review_only:
                execution.production_targets()
            result = {'execution': 'INPUTS_READY', 'approved': False, 'host_verifier': 'UNAVAILABLE',
                      'specialists': {r: str(p) for r, p in execution.skills.items()}}
        else:
            result = execution.run(resume=args.resume, review_only=args.review_only)
            code = 0 if result['execution'] == 'REVIEW_COMPLETE_UNCERTIFIED' else 2
    elif args.command == 'init':
        init_bundle(args.root, read_artifact(args.intent)); result = {'initialized': str(args.root), 'artifacts': list(ARTIFACTS.values())}
    elif args.command == 'index': result = build_index(args.corpus)
    elif args.command == 'retrieve': result = retrieve(read_artifact(args.index), read_artifact(args.intent), args.limit)
    else:
        bundle = load_bundle(args.root)
        if args.command in ('check', 'handoff'):
            result = assess(bundle)
            if args.command == 'handoff' and args.validate:
                validate_handoff(bundle, read_artifact(args.validate))
            code = 0 if result['approved'] else 2
        elif args.command == 'advance':
            result = transition(bundle, args.stage)
            write_artifact(args.root / ARTIFACTS['evidence'], result, overwrite=True)
        elif args.command == 'bundle': result = make_role_bundle(bundle, args.role)
        elif args.command == 'raci': result = raci_plan(bundle, args.claim_id)
        elif args.command == 'guard':
            result = {'issues': guard_change(bundle['intent'], bundle['contract'], read_artifact(args.change))}
            code = 2 if result['issues'] else 0
        elif args.command == 'repair':
            result = {'disposition': assess(bundle)['disposition']}
            code = 0 if result['disposition'] == 'CONTINUE' else 2
        elif args.command == 'bind':
            # Binding records identity, never authenticity. Existing observations
            # remain preserved and become stale against this new snapshot.
            bundle['matrix']['bindings'] = {k: digest(bundle[k]) for k in ('intent', 'lock', 'contract')}
            bundle['evidence']['run'] = {k: bundle['intent'][k] for k in ('candidate_id', 'revision', 'scope_id')} | {
                'run_id': args.run_id, 'build_id': args.build_id, 'implementation_context': args.context_id,
                'snapshot': snapshot(bundle)}
            write_artifacts_transaction({args.root / ARTIFACTS['matrix']: bundle['matrix'],
                                         args.root / ARTIFACTS['evidence']: bundle['evidence']})
            result = {'bound': bundle['evidence']['run'], 'trust': 'LOCAL_UNAUTHENTICATED'}
    if getattr(args, 'output', None):
        write_artifact(args.output, result)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return code


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
    try:
        sys.exit(main())
    except (ValueError, OSError, KeyError, TypeError) as error:
        print(json.dumps({'error': str(error), 'status': 'NOT_READY'}, ensure_ascii=False), file=sys.stderr)
        sys.exit(1)
