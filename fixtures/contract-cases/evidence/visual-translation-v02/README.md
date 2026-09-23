# v0.2 candidate evidence — bounded functional validation

Baseline `2a815ee49d8f7ca6a7c1e483df315eda1fa709d7`; separate worktree/branch.
No personal install, main integration, real-project visual validation or TrackE work.

## Chronology (append results, do not rewrite a failed attempt)

1. `01-v01-baseline.tap`: original eight-file suite, 72 PASS / 0 FAIL, exit 0.
   Actual Node default reporter output, despite the historical `.tap` filename.
   Command and immutable source hashes: `baseline-and-freeze.json`.
2. Spec, nine neutral inputs and separate qualitative expectations authored before
   candidate output or runtime edits. Hashes frozen in `baseline-and-freeze.json`.
3. `02-v01-behavior/`: PATH CLI 0.146.0 rejected Astra with HTTP 400 before model
   response. Platform failure, not skill failure. Retained input, events, stderr,
   exit 1 and invocation. No model response exists for this attempt.
4. `03-v01-behavior-native/`: same input via already installed CLI
   0.155.0-alpha.16; Astra xhigh, fresh exec, exit 0. No runtime installation/change.
   This is a pre-change functional characterization, not a Bare-vs-skill experiment.
5. `04-v02-red.txt`: new current-version evidence gates RED, 4 PASS / 10 FAIL,
   exit 1, specifically missing fresh v0.2 evidence. This is evidence-readiness RED,
   **not demonstrated behavioral failure of v0.1**. Old tests archived byte-exact.

## Pre-change decision review

All nine responses satisfy the core scoped behavior qualitatively: B01 direct
title wiring; B02 one reversible relationship-based draft with proposed values;
B03 scoped reference adoption without image dominance; B04 original source/SVG
handoff and concrete alignment; B05 crop-only with six records and pending state;
B06 bounded Product question and independent caption work; B07 PASS/FAIL/UNVERIFIED
separation; B08 approved native roles and restricted draft spatial profile; B09
one-root approved/draft boundary. B08's type independence is implicit in preserving
the approved 15px role; not an independent exhaustive type-policy test.

B09 additionally prescribes 2–3 candidates, illustrating the existing fixed
exploration instruction. This is a friction observation, not retrospectively added
to its frozen expected-answer gate. No clear material behavioral failure is claimed
for the baseline. The authorized refactor proceeds; no failure-seeking reruns.

## Method limits

Text-only functional scenarios supply fictional approval facts; no actual approved
designs/assets were supplied or fabricated, and no rendering occurred. Each batch
uses one fresh context (nine independent requests in that context), not nine
independently isolated design projects. The template is explicitly supplied in this
functional check; ordinary default load is measured separately. Native platform
instructions/automatic metadata are not a clean-room exclusion claim.

Authored candidate input contains the skill, template and neutral requests only,
not this spec, rubric, expected outputs, PM report or old failures. Raw response,
CLI event stream and native-rollout provenance have separate identities. No full
Codex home, credentials or full ambient rollout are committed. This is not a new
evaluation platform and cannot establish design quality, specialist value or the
causal effect of instruction length.

Skill guidance used: skill-creator/writing-skills for concise package and fresh
consumer checks, TDD for fixed-before-output expectations. The user's bounded
verification sequence overrides the skill's open-ended pressure-test/loophole loop;
no repeated success search or new program is introduced. Native worktree tool
targets the unrelated harness task repo, so ordinary Git created the requested
separate JOEDESIGN worktree from the pinned SHA.

## Final candidate validation (2026-09-24 KST)

6. Package implementation and four structural/history/input checks passed.
   `05-validator-default-encoding-failure.txt` preserves Python's Windows cp949
   decoding failure (exit 1); `06-validator-utf8.txt` shows the same validator
   invoked with `python -X utf8` passing (exit 0). No validator or package change
   was needed for that environment issue.
7. Read-only review identified one retained-contract omission: the first condensed
   runtime lacked explicit smallest proof before dependent integration. Restored
   that conditional sentence; removed a worked example overly similar to B04.
   No frozen expectation or response was changed. Pre-review SKILL was 10,999 bytes,
   SHA-256 `49fc833765e44f4a2831031c54d3e1e07eca9f7e0af3b2cae4734d55c4148d1a`;
   final package identities are in `instruction-size.json`. No model execution used
   the intermediate v0.2 package. `08-post-review-structural.txt`: 4 PASS, exit 0.
8. `09-v02-fresh/`: one fresh GPT-6 Astra xhigh batch, native CLI
   0.155.0-alpha.16, thread `01a0ced9-b462-7e73-9c10-0c24aecb25df`, exit 0.
   `fresh-review.json` records nine PASS decisions with exact response quotations
   for all 27 pre-fixed scoped obligations. B01 does not explicitly repeat the
   acceptance rule but grants no acceptance; B08 demonstrates a proposed 24px
   subgroup and native reuse, not exhaustive enforcement of every spacing value.
9. `10-v02-full-suite.txt`: 14 PASS / 0 FAIL, exit 0. Four package/history/input
   tests + one execution linkage test + nine recorded qualitative reviews. It is
   neither 14 live model invocations nor 14 rendered design checks.
10. Independent review confirmed runtime fixes, all nine scoped decision findings,
    frozen input hashes and execution package identity. Its integrity finding was
    fixed by checking execution-time paths/hashes/bytes against the current package,
    rather than only the review record. See `review-notes.md`.

### Exact artifact identity

Each functional attempt has an authored input, response if produced, CLI event
stream, stderr and execution record. Successful attempts additionally have compact
native provenance: actual model/effort/thread/turn, native rollout hash, matching
authored user-content hash (with documented stdin newline normalization), final
response linkage, message hash inventory and zero tool-call count. Native rollout,
CLI event stream and final response hashes are distinct. Native flush/shell-snapshot
warnings remain in stderr; the retained native files contain the matching input,
model context and final response. Full provider-request/OS isolation is not proven.

`review-evidence.json` indexes the new bounded evidence files and exact hashes.
All original v0.1 observed/review/Smoke/failure bytes are preserved, never relabeled.
Archived v0.1 tests are source records; rerun at the pinned baseline, not their
new archive location. The current command is:

```sh
node --test tests/joedesign-v02.tests.mjs
```

### Instruction size and required load

| UTF-8 file | v0.1 bytes | v0.2 bytes |
| --- | ---: | ---: |
| SKILL.md | 23,573 | 10,930 |
| templates/DESIGN.md | 3,743 | 1,583 |
| agents/openai.yaml | 207 | 243 |

Invoked default body is SKILL.md; template is conditional on creating/materially
updating durable decisions. No always-loaded references, sidecars or extra runtime
instructions were added. Existing Product/DESIGN/source/assets remain task inputs.
The functional test deliberately supplies the template too; discovery/default-prompt
loading was not tested by model. Byte/word reduction is not a quality or speed claim.

### Readiness boundary / next PM decision

Candidate implementation and bounded functional validation are ready for Program
Review after commit/push/readback. No unresolved observed contract failure remains.
Historical platform/encoding failures, readiness RED and review corrections remain
visible. Real-project visual validation is **PENDING**, not a missing rendered proof
disguised as PASS. No actual visual source/asset operation was performed.

TrackE **CLOSED**, JOEDESIGN / UI UX Pro Max specialist value **NOT TESTED**.
Program Lead decides whether to accept this candidate and separately authorize an
operational check with newly approved source material and actual assets. No personal
install, production acceptance, comparison rerun or release is implied. Stop after
the final report.
