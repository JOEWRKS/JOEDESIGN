# Single operating core — 2026-10-09

The user requested one JOEDESIGN operating core governing multiple stages and
specialist responsibilities. Baseline: `0efacd8e6db52235b07b9d5b570a8aa0ca9d6a1a`.
This supersedes the former frozen-current-core/two-public-skills layout. Preserve
its original bytes and test source in `fixtures/package-history/pre-unification-20261009/`.
Do not rebind historical v0.2 behavior evidence to the new package.

## Expectations fixed before implementation

1. Exactly one public skill under skills/: joedesign. A copy of that folder contains
   its operating rules, role guidance, templates and executable controller without
   needing a sibling Harness skill or repository documents.
2. One coordinator owns scope, assignments, stage transitions and integrated results.
   Role workers follow their bounded assignments; they do not restart orchestration
   or use specialist defaults to override the chosen method.
3. Preserve the visual translation/craft principles and the proof-before-expansion,
   source inspection, R/C1/conditional C2, independent critique and acceptance limits.
   Local repairs remain scoped; read-only reviews never acquire write authority.
4. Runtime roles receive the same operating core; J resolves inside this package,
   never to a separately installed old core. An override cannot install a competing
   operating authority. Relevant visual modules are delivered to J assignments.
5. Source/module changes invalidate cached runs. Missing external specialists remain
   unresolved. Copied CLI preflight/doctor and execution use the same core source.
6. Historical packages, saved behavior evidence and installations remain unchanged.
   Current packaging/runtime checks and historical v0.2 evidence checks are reported
   separately. Existing runs require a new candidate after this source migration.

Validation: Python regression including a copied-package production fixture,
Node historical v0.2 regression, skill validator and package/history/install hashes.
Synthetic review results do not establish live specialist compliance or design quality.
No installation, new commit/push or release is part of this implementation step.

## Implemented

- One public `skills/joedesign/SKILL.md` operating entry, one coordinator A, bounded
  specialist assignments and one self-contained package. Internal harness scripts,
  contracts and templates moved into that package; the second skill was removed.
- Former visual interpretation/craft guidance is an internal visual-translation
  module. Scope and stage orchestration belong to the entrypoint, not a second
  public core. Source access, scoped approval and proof/review gates remain required.
- Every runtime role receives the packaged core first. J resolves locally and gets
  visual modules, rather than invoking an independently installed old core. An
  external J override fails before role execution. Missing internal modules block.
- Doctor and execution share source resolution. One VERSION (`0.3.0-dev`) and the
  `version` command identify the unified candidate. README/CHANGELOG document the
  old-to-new paths, settings migration and installation distinction.
- Original package and Node source bytes remain archived; existing evidence is
  unchanged. Historical tests point at that exact archive, never the changed skill.

## Verification results

- Python: **117 PASS**, zero skips/failures (`python-tests.txt`), including the real
  Edge click/focus/capture fixture using the already available browser runtime.
- Historical Node v0.2 evidence regression: **14 PASS**, zero skips/failures
  (`node-history-tests.txt`). These are not 14 new unified-skill behavior tests.
- New regression coverage checks copied-package production through proof and
  expansion, one core per role, J-module delivery, source-change invalidation,
  conflicting core override rejection, missing module failure, and doctor resolution
  with an old core present. The production roles/captures in that test are synthetic.
- First focused run: 28 PASS / 1 FAIL (`focused-first.txt`). The new assertion
  mistakenly required J's visual modules for the read-only Technical implementer
  review, whose assigned role needs only the operating core. The assertion now
  distinguishes that review from the actual J implementation task; source delivery
  was not changed to satisfy an irrelevant role requirement. Final full suite passes.
- Skill validator passed. `integrity.json` records all 25 unified package file
  hashes, 26 preserved original package/test files, unchanged existing evidence,
  46 unchanged installed files, and resolving package links/anchors.

No new live model exercise, actual project design change or human visual acceptance
was performed. The tests show local packaging and orchestration behavior, not
specialist obedience or visual quality. Existing installed skills remain old until
an explicit installation update; the repository has one public source entrypoint.
Working branch: `codex/joedesign-unified-core`; no new commit/push/main integration.
