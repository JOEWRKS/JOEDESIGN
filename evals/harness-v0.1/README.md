# Design Harness v0.1 — implementation evidence

Current disposition (2026-09-30): the existing installed Harness is retained.
The repository source now matches that runtime baseline, including the later visual
production/motion-quality correction. See [the adoption decision](retention-decision.md).
The record below describes the original implementation candidate and its evidence
at that time; it does not establish rendered-design superiority.

Baseline: 893e0181f77e1af87cf9a651f291b6929e5109b0.
Branch: codex/joedesign-harness-v01. Existing v0.2 core hashes: baseline-package.json.
Original v0.2 regression was 14/14 before changes. Its package-wide discovery assertion
now allows the authorized second skill; all core/history/evidence checks are preserved.

This candidate implements artifact IO, OMD metadata retrieval, product/reference
translation contracts, scope/craft guards, state/evidence policies, structural repair,
critic input isolation and exact approval policy. CLI commands are actual executable code.
Seven templates and a self-contained skill are included. No personal install or merge.

The test host is synthetic. It validates policy branches, not host integration.
No authenticated host receipt backend or browser collector is bundled. Local-only
reports remain UNVERIFIED; there is no unsafe `--trust-local` option. Fresh visual
Critic/calibration, exact user acceptance and comparative visual quality are unverified.
Therefore the full handoff's implementation-complete/production-ready claim is withheld
pending those integration and fresh behavior requirements.

## Reported failure and regressions

User report: OMD used for IT/data layout and interaction references but BIO/02
content/constraints were not translated; surface type/panels/lines were copied;
static PPT-like results were polished repeatedly. This is user-provided evidence,
not a new independent inspection of the prior BIO implementation.

Synthetic regression cases test missing content grounding, missing interaction axis,
motion claimed from stills, structural failure blocking craft immediately and two
failed local repairs forcing rework. Existing BIO files and outputs are untouched.
Presence checks cannot determine whether a rationale is meaningful; actual structural
render review and user evaluation remain required.

F1/F2/F3/F10/F11: test_harness_contracts.py.
F4/F5/F6/F7/F8/F9/F12: test_harness_evidence.py.
CLI copy/init/refusal: test_harness_cli.py and test_harness_package.py.
State/repair/critic bundle: test_harness_pipeline.py.

## Actual OMD input

Source: https://github.com/kwakseongjae/oh-my-design
Pinned commit: bb0d89ca8dcddf0bf1019d8fe8d25dcfaa567c70.
Read-only samples: web/references/linear.app/DESIGN.md,
web/references/vercel/DESIGN.md, web/references/stripe/DESIGN.md.
They are cached outside this repository; no corpus/vendor runtime is included.
Metadata retrieval does not mean these references fit BIO/02 or have been visually
inspected in this task. They are integration inputs, not adopted visual directions.

## Verification

See verification.md for final commands/results and concrete remaining boundaries.
Use `python -X utf8` with the external skill-creator quick validator on Windows;
its default-encoding run failed with cp949 decoding before validation. The package
itself uses explicit UTF-8. Preserve that failure in the report, not as product failure.

## Implementation rulings

- Native worktree API targets the unrelated JOENESS checkout; Git isolated this repository.
- Current user authority allows the new harness; historical v0.2 scope stays historical.
- Executable Python contracts and seven templates replace duplicate handwritten JSON
  Schemas; otherwise schema/validator drift would create two inconsistent validators.
- Existing authenticated host capabilities were not available to the Python CLI.
  The injected HostVerifier boundary stays unavailable by default; no authentication claim.
- CLI entrypoints are consolidated in one script rather than seven forwarding scripts.
- No model quality A/B or live visual claim follows from tests, package discovery or real metadata parsing.
