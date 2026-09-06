# JOEDESIGN Implementation Bridge Validation v1

**Status:** ACTIVE EXECUTION HANDOFF  
**Scope:** transplant the historical bounded Bridge candidate onto the current Composition-closed Pure Craft core, then validate it.  
**Current authority baseline:** `16210004ef4bf43850a9324f574dbdf39f31688d`  
**Historical Bridge source branch:** `codex/joedesign-v0.1-implementation-bridge`  
**Historical Bridge candidate implementation HEAD:** `f51a9f70b39d49bb023a3ffc080fe7a05227b9e8`

---

## 1. Objective

Close the final pre-freeze runtime layer without regressing newer Craft work.

```text
Composition CLOSED core
→ inspect historical Bridge-only delta
→ transplant Bridge-specific doctrine/tests/runtime only
→ fresh semantic evidence
→ full 72-test gate
→ neutral Smoke F actual render
→ Program Review
```

Do not merge or overwrite the current branch with the historical Bridge branch.

---

## 2. Authority and scope

Implementation Bridge is derivative.

```text
APPROVED Project DESIGN.md
→ Implementation Bridge
→ project-native token/component/style mapping
→ implementation
→ actual runtime
→ visual verification
```

Bridge cannot create Product Truth, Project Visual Truth, or User Acceptance.

Canonical Bridge doctrine lives on the historical source branch at:

`docs/specs/joedesign-implementation-bridge-v0.1.md`

Historical static contract:

`tests/joedesign-implementation-bridge.tests.mjs`

Historical implementation plan:

`docs/superpowers/plans/2026-09-06-joedesign-implementation-bridge-v0.1.md`

---

## 3. Critical transplant rule

The historical Bridge branch predates Color, Imagery, and Composition.

Never copy these files wholesale from the old branch:

- `skills/joedesign/SKILL.md`
- `skills/joedesign/templates/DESIGN.md`
- `tests/joedesign-contract.tests.mjs`
- `fixtures/contract-cases/observed.json`
- `fixtures/contract-cases/review-evidence.json`

Instead, inspect the old branch and transplant only Bridge-specific additions into the current files.

The current closed sections must remain byte-preserving except for the exact insertion point required by Bridge:

- Process / Authority
- Spatial / Hierarchy
- Typography / Scale
- Reference Intelligence
- Color / Contrast
- Imagery / Focal Ownership
- Composition / Anti-template

---

## 4. Required Bridge behavior

The transplanted behavior must preserve these eight contracts:

1. mapping is derivative, not visual authority;
2. exact approved values may map while unknown values remain unresolved;
3. existing equivalent project-native roles are preferred;
4. structured tokens remain distinct from visual intent/rationale;
5. Google `design.md` interoperability is optional and dependency-free;
6. custom JOEDESIGN sections survive structured interoperability;
7. material mapping changes use bounded semantic diff/review;
8. mapping/lint/export success never replaces actual rendered verification.

Do not add parser, token DB, standalone CLI, exporter, Figma sync, vendor runtime, or new public skill.

---

## 5. Required execution order

Use an isolated worktree.

### A. Baseline

Run the current seven-file 64-test suite before any Bridge transplant.

Required:

```text
64 PASS / 0 FAIL
```

If the only failure is an internal-document allowlist omission caused by this handoff/spec/plan, fix only that allowlist and rerun. Do not alter shipped skill or expected semantic actions.

### B. Bridge contract compatibility / RED

Bring the historical Bridge spec and Bridge test into the current branch as new files, preserving their doctrine meaning.

Before runtime insertion, run:

```text
node --test tests/joedesign-implementation-bridge.tests.mjs
```

Expected: Bridge runtime assertions FAIL because the current Composition-closed skill does not yet contain the Bridge section. Preserve this RED evidence.

If any assertion already passes due to newer unrelated wording, keep the test semantics but do not weaken them merely to force eight RED failures. Record the actual RED breakdown.

### C. Bounded transplant

Transplant only the Bridge-specific section into current `SKILL.md` and any compact Bridge persistence/interoperability guidance required by the current template.

Do not replace current Craft sections with historical file versions.

Run Bridge contracts.

Required:

```text
8 PASS / 0 FAIL
```

### D. Fresh semantic replay

Because shipped skill bytes changed, run one fresh isolated:

```text
gpt-6-astra / xhigh
14 deterministic cases
```

Required:

```text
14 PASS / 0 FAIL
```

Expected actions stay frozen. Preserve previous observed/review evidence under history before replacing current evidence.

### E. Full suite

Run:

```text
16 process/authority
+ 8 spatial
+ 8 typography
+ 8 reference
+ 8 color
+ 8 imagery
+ 8 composition
+ 8 bridge
= 72 tests
```

Required:

```text
72 PASS / 0 FAIL
```

### F. Smoke F

Run one neutral fictional actual-browser proof.

Required target:

```text
APPROVED DESIGN.md
→ semantic project-native mapping
→ implementation
→ actual browser render
```

Required viewports:

```text
Desktop 1440×1000
Mobile 390×844
```

### G. Final gate

If Smoke F did not modify `skills/joedesign/**`, reuse the fresh semantic evidence and run final `72/72` once.

If Smoke F caused any shipped skill change:

```text
fresh semantic 14/14 again
→ full 72/72 again
→ rerun affected Smoke F proof
```

---

## 6. Smoke F fixture

Use a fictional neutral product such as **Operations Status Console**.

Product Truth must include:

- fixed status heading and summary;
- three semantic status rows;
- one primary action;
- one secondary detail link;
- no change to Product semantics during Bridge work.

APPROVED `DESIGN.md` must contain a mix of:

- exact approved values that map cleanly;
- existing project-native tokens with different names but equivalent roles;
- one intentionally unresolved value;
- at least one JOEDESIGN-specific custom section/rationale block;
- responsive intent that should remain prose rather than forced into a token schema.

Existing implementation must already have a small healthy project-native token set so the Bridge has something to reuse.

---

## 7. Smoke F observables

Record a pre-edit mapping table before implementation changes.

Required PASS observables:

```text
F1 approved authority remains unchanged
F2 exact approved values map correctly
F3 equivalent existing project-native roles are reused
F4 no unnecessary token renaming/rearchitecture
F5 intentionally missing value remains unresolved / explicitly bounded
F6 JOEDESIGN-specific custom sections/rationale are preserved
F7 material mapping diff records role + before/after + source + reason + scope
F8 desktop actual render observed
F9 mobile actual render observed
F10 Token Mapping / Technical / Visual / User Acceptance verdicts remain separate
```

If an unresolved value prevents a material visual claim, report that exact boundary as UNVERIFIED rather than inventing the value.

---

## 8. Hard boundaries

Do not:

- expose BIO;
- import competitor methodology/runtime;
- install Google `design.md` tooling;
- add parser/lint CLI/exporter infrastructure;
- overwrite newer Craft sections with the historical Bridge branch;
- rename healthy project tokens merely to match an external schema;
- invent missing design values;
- promote code tokens to Project Visual Truth;
- alter expected semantic actions;
- delete failure evidence;
- grant User Acceptance from Visual PASS.

---

## 9. Final report

All gates pass:

`JOEDESIGN_IMPLEMENTATION_BRIDGE_V0_1_READY_FOR_PROGRAM_REVIEW`

Report:

```text
Repository:
Branch:
HEAD:
Tree:
Worktree:
Static contracts: 72/72
Bridge contracts: 8/8
Semantic replay: fresh 14/14
Smoke F: F1–F10
Skill SHA-256:
DESIGN template SHA-256:
Public entrypoint count:
Competitor dependency count:
Runtime dependency count:
BIO exposure count:
Known failures:
Unverified:
```

Any unresolved required gate:

`JOEDESIGN_IMPLEMENTATION_BRIDGE_V0_1_NOT_READY`

Do not declare Pure Core Freeze or competition readiness. Program Lead owns those gates.
