# JOEDESIGN

## Design Harness v0.1 implementation candidate

The separate [joedesign-harness skill](skills/joedesign-harness/SKILL.md) implements
OMD corpus retrieval, grounded design contracts, scoped transitions, structural
rework and evidence/approval policy. The original joedesign v0.2 package is unchanged.
See [usage and trust boundaries](skills/joedesign-harness/references/operation.md)
and [verification/limitations](evals/harness-v0.1/README.md).

Run `python skills/joedesign-harness/scripts/harness_cli.py --help`.
Tests: `python -m unittest discover -s tests -v` and
`node --test tests/joedesign-v02.tests.mjs`.
No global install is performed. Copy the harness folder project-locally beside the
existing joedesign skill when adopting this candidate. A trusted host evidence adapter
is not bundled; local-only use cannot issue final APPROVED. Design quality improvement
and operational readiness remain unverified.

## Preserved v0.2 documentation

> JOEDESIGN으로 디자인해.

JOEDESIGN preserves product meaning while translating approved visual material and
selected reference relationships into project-specific composition and implementation
decisions, then diagnoses differences between the original and actual output.

## v0.2 Visual Translation — implementation candidate

Primary: implement/refine an approved visual target using its original material and
real assets. Conditional: propose an unapproved direction when a reference-based
decision is unresolved. Sufficient inputs need only the implementation delta, not
compulsory alternatives or a rewritten design brief. A supplied image is not approval.

This is a candidate for Program Review, not a production release, user acceptance,
design-quality guarantee or evidence of specialist superiority.

- Branch: codex/joedesign-v0.2-visual-translation.
- Pinned v0.1 baseline: 2a815ee49d8f7ca6a7c1e483df315eda1fa709d7;
  preserved branch codex/joedesign-v0.1-test.
- [Change spec / contract mapping](docs/specs/joedesign-v0.2-visual-translation.md).
- [Current role map](docs/architecture/JOEDESIGN_OPERATING_MODEL_V1.md).
- [Evidence, hashes, instruction sizes and limits](fixtures/contract-cases/evidence/visual-translation-v02/README.md).

## Project-local use

Copy only skills/joedesign into your project's .agents/skills/joedesign, preserving
the three files and relative paths. No installer or global behavior overlay is needed.
This repository's spec, AGENTS, tests, operational reports and diagnostic history are
not candidate runtime input. This task does not perform a personal install.

In a fresh project session invoke $joedesign or ask “JOEDESIGN으로 디자인해.”
Point to Product authority, original visual material/assets and the exact request.
Identify what is actually approved, including version/surface/state, versus ordinary
references. The skill reads existing decisions and keeps a single root DESIGN.md;
the compact template is needed only for creating/materially updating those decisions.

Source observation → project preserve/change → implementation decision → observable
result difference. This connection supplements the originals; a controller must not
replace them with a taste paragraph. Native project tokens/components remain useful.
The implementer still observes its actual render. Build/token success is not visual
conformance, and visual conformance is not user acceptance.

## Verification and history

Current command: node --test tests/joedesign-v02.tests.mjs

The suite checks the three-file package, a temporary project-local copy, historical
bytes, frozen inputs and linkage/review of fresh functional responses. It does not
call a model and does not turn textual decisions into rendered proof. The evidence
packet records actual executions separately, including failures and limitations.

The pre-change original suite was run: 72 PASS / 0 FAIL. Its exact test sources now
live under fixtures/contract-cases/history/v01-test-sources/; their relative imports
are intentionally unmodified. To rerun that historical suite, use a separate checkout
of the pinned v0.1 commit and the original command in the evidence packet. Do not run
those archived tests against v0.2 or relabel v0.1 semantic/Smoke evidence as v0.2.

TrackE is CLOSED. JOEDESIGN and UI UX Pro Max specialist value remains NOT TESTED;
TEST B was platform-blocked, not a method failure. No diagnostic rerun is authorized.
Real-project visual validation with newly approved designs and actual assets is
PENDING; none were supplied here. No BIO production, comparison, personal install,
main merge, release tag or new runtime dependency is part of this candidate.
