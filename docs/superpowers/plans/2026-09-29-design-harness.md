# JOEDESIGN Design Harness v0.1 Implementation Plan

> **For agentic workers:** Use superpowers:executing-plans inline. Steps below are TDD checkpoints; final branch review uses a fresh reviewer.

**Goal:** Ship a usable reference-to-contract controller that rejects ungrounded
implementation and unsupported completion, including the reported BIO/02 failure.

**Architecture:** A self-contained skill invokes a Python stdlib CLI. Seven scoped
artifacts carry machine-readable JSON (one fenced JSON payload in Markdown files).
Validators compute gates; agents interpret images and implement the actual UI.
An injected host verifier is a separate trust boundary, unavailable by default.

**Tech Stack:** Python 3.11+ stdlib, existing Node regression suite.

**Spec:** ../specs/JOEDESIGN_UI_REVIEW_RACI_V0_1_DRAFT.md, original handoff alongside it.

## Global Constraints

- Design quality first; no aesthetic scoring or token minimization gate.
- Existing skills/joedesign bytes and historical evidence unchanged.
- Primary 1, Secondary at most 2; one owner per design axis.
- OMD is read-only reference input, never a runtime authority or vendored corpus.
- Missing facts are UNKNOWN/UNVERIFIED; no inferred motion from screenshots.
- Exact user approval separate from implementation permission and all internal gates.
- No BIO production changes, global install, main merge, or remote publishing.

## Review Focus

- Malformed/duplicate IDs and references to absent targets must fail closed (Tasks 1–3).
- Self-authored receipts and changed content must not authenticate execution (Task 3).
- Repeated decorative fixes must not hide a structural failure (Tasks 2, 4).
- Candidate/viewport/state mixing and omitted required rows must not pass (Task 3).
- CLI failure must preserve existing artifacts and return a nonzero exit (Tasks 1, 4).

### Task 1: Artifact IO and OMD retrieval

Files: scripts/harness/io.py, references.py, cli.py within skills/joedesign-harness;
tests/test_harness_references.py, test_harness_cli.py.
Interfaces: read_artifact(Path)->dict; build_index(Path)->dict;
retrieve(index, intent, limit=10)->dict; CLI init/index/retrieve.

- [ ] Write tests for Unicode, duplicate JSON keys, duplicate reference IDs, missing quality,
  real OMD frontmatter, structural needs versus superficial keyword matches, no overwrite.
- [ ] Run `python -m unittest discover -s tests -p 'test_harness_references.py' -v`; observe RED.
- [ ] Implement bounded metadata extraction retaining source pointer/hash/unknowns; never parse YAML as executable instructions.
- [ ] Run tests GREEN and commit.

### Task 2: Product, reference, synthesis, scope and craft gates

Files: scripts/harness/contracts.py; tests/test_harness_contracts.py.
Interfaces: validate_intent, validate_lock, validate_contract -> list of issues;
guard_change(intent, contract, change)->list of issues.

- [ ] Write F1/F2/F3/F10/F11 plus BIO structural-grounding regression tests.
- [ ] Observe RED; implement coverage of content/action IDs, constraints, concrete spatial,
  responsive and applicable motion rules, nondecorative relationships, invariants and axis ownership.
- [ ] Require early structural proof before expansion; structural FAIL immediately REWORK.
- [ ] Run task tests GREEN and commit.

### Task 3: Evidence, critic, calibration, user and scope-bound gates

Files: scripts/harness/evidence.py; tests/test_harness_evidence.py.
Interfaces: assess(bundle, host=None)->structured report; HostVerifier.resolve(id)->receipt|None.

- [ ] Write F4–F9/F12, tampered bytes, stale revision, mismatched target, missing matrix row,
  same-context critic, uncalibrated critic, false approval and scope-laundering tests.
- [ ] Observe RED; implement host receipts checked against local evidence hash/exact target,
  separate categories, fail precedence, approved calibration and exact user event requirements.
- [ ] Keep default host unavailable; do not claim writable local JSON authenticates a run.
- [ ] Run task tests GREEN and commit.

### Task 4: Stateful CLI, adapters, repair and truthful handoff

Files: scripts/harness/pipeline.py, cli.py; templates/; tests/test_harness_pipeline.py, test_harness_cli.py.
Interfaces: load_bundle(Path)->dict; transition(bundle, stage, host=None)->dict;
repair_disposition(attempts, findings)->str; commands check/advance/bundle/handoff.

- [ ] Write transition, candidate isolation, first structural failure, two failed local repairs,
  no hypothesis, historical FAIL preservation, fabricated report and CLI roundtrip tests.
- [ ] Observe RED; implement precondition gates and stage invalidation from current artifacts.
- [ ] Emit synthesis/craft/critic input bundles; critic excludes builder verdicts and rationale.
- [ ] Generate reports only from assessed fields. Preserve all attempts; never overwrite approved DESIGN.md.
- [ ] Run task tests GREEN and commit.

### Task 5: Skill package and integrated verification

Files: SKILL.md, agents/openai.yaml, references/operation.md, README.md,
evals/harness-v0.1/{README.md,verification.md}, tests/test_harness_package.py.

- [ ] Add package discovery/copy/CLI tests and byte-for-byte v0.2 regression; observe RED.
- [ ] Create concise skill using skill-creator; RACI and OMD grounding are execution guidance.
- [ ] Update only the old whole-repository one-skill inventory assertion for the authorized second package;
  preserve all original package and evidence checks.
- [ ] Exercise real pinned OMD metadata outside repo, CLI initialized project, blocked decorative-only
  contract, corrected structural contract, missing runtime/host evidence, and standalone copy.
- [ ] Run Python suite, Node v0.2 suite, compile, package validation and git diff --check.
- [ ] Fresh whole-branch review; fix important findings with RED→GREEN; record limitations and commit.

No claim that automated string/coverage checks determine aesthetic quality. A valid
contract only permits scoped proof creation; host/user/visual evidence still governs closure.
