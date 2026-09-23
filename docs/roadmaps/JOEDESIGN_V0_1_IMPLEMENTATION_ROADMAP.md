# JOEDESIGN v0.1 Implementation Roadmap

> **v0.2 branch resume point (2026-09-24):** The body below is preserved v0.1
> phase history, not current execution authority. Current work is the
> [Visual Translation candidate](../specs/joedesign-v0.2-visual-translation.md);
> see [its evidence packet](../../fixtures/contract-cases/evidence/visual-translation-v02/README.md).
> Baseline is `2a815ee49d8f7ca6a7c1e483df315eda1fa709d7`; v0.1-test stays unchanged.
> TrackE is CLOSED, specialist value NOT TESTED, TEST B platform-blocked. Do not
> resume comparison or TrackC BIO. Next decision is Program Review of v0.2;
> real-project validation remains PENDING until new approved material/assets arrive.

**Status:** `v0.1-test` — frozen working MVP for evaluation
**Purpose:** 대화 기억이 없어져도 현재 완료 상태, 다음 gate, 금지선을 즉시 복구한다.  
**Operating model:** `docs/architecture/JOEDESIGN_OPERATING_MODEL_V1.md`

---

## 1. 최종 목표

JOEDESIGN v0.1은 다음 다섯 층을 가진 작고 독립적인 AI 디자인 코어를 완성한 뒤 동일 과제 경쟁으로 검증한다.

```text
1. Process / Authority Core
2. Craft Core
3. Reference Intelligence
4. Implementation Bridge
5. Competition Proof
```

경쟁 전에는 competitor methodology를 흡수하지 않는다.

---

## 2. 현재 상태

| 영역 | 상태 |
|---|---|
| Process / Authority Core | CLOSED |
| Hierarchy / Flow / Spatial Core | CLOSED |
| Typography / Scale Core | CLOSED |
| Reference Intelligence | CLOSED |
| Color / Contrast Core | CLOSED |
| Imagery / Focal Ownership Core | CLOSED |
| Composition / Anti-template Core | CLOSED |
| Composition validation supplement | ACCEPTED by Program Lead — original Composition package scope |
| Optical / Detail Polish | DEFERRED — no demonstrated need before competition |
| Implementation Bridge | CLOSED by Program Lead — existing contracts and Smoke F scope only |
| Pure Core Freeze | PASS — Program Lead approved exact source `7f890c60ed3837efc1693aeeba33759f12c85383` |
| Test snapshot | `v0.1-test` — unchanged frozen package on `codex/joedesign-v0.1-test` |
| BIO 5-way Competition | JOEDESIGN arm ready for handoff; TrackE execution pending common-input/runtime preflight and authorization |

현재 순서:

```text
Frozen v0.1-test snapshot
→ TrackE comparison handoff; TrackC lead chat retains BIO product/evaluation management
→ common-input/runtime preflight and separately authorized comparison
→ evaluation and BIO adoption decision
→ v0.2 decision
```

---

## 3. CLOSED Core evidence

### Process / Authority

- [x] one public entrypoint: `JOEDESIGN`
- [x] Product Definition / JOEDESIGN / JOEFLOW / User authority separation
- [x] `UNDERSTAND → EXPLORE → PROVE → REFINE → VERIFY → ACCEPT/PERSIST`
- [x] `Technical PASS ≠ Product PASS ≠ Visual PASS ≠ User Acceptance`
- [x] root `DESIGN.md` lifecycle and target-medium proof

### Hierarchy / Spatial

- [x] `Hierarchy before decoration`
- [x] visual entry / second / third destination
- [x] Semantic Visual Block Tree
- [x] spacing belongs to relationship/boundary
- [x] restricted spatial vocabulary `160 / 48 / 24 / 16 / 8 / 4`
- [x] responsive hierarchy translation

### Typography / Scale

- [x] role before value
- [x] semantic type roles
- [x] multi-axis hierarchy
- [x] restrained scale / family / weight / measure / line-height
- [x] responsive type translation

### Reference Intelligence

- [x] `KNOWN / UNKNOWN`
- [x] `TAKE / DO NOT TAKE / WHY / APPLIES TO`
- [x] evidence quality ≠ aesthetic authority
- [x] conflict stays explicit
- [x] external corpus optional; no DB/router dependency
- [x] Smoke E PASS
- [x] Program Lead: `REFERENCE_INTELLIGENCE_CORE = CLOSED`

### Color / Contrast

- [x] semantic color roles
- [x] contrast hierarchy / accent ownership
- [x] neutral surface hierarchy
- [x] state semantics + non-color cues
- [x] contextual WCAG minimum gate
- [x] Smoke G PASS
- [x] Program Lead: `COLOR_CONTRAST_CORE = CLOSED`

Canonical evidence HEAD: `7417ef037062f27272c3d3527713475b7d97c6f3`.

### Imagery / Focal Ownership

- [x] `FOCAL / SUPPORT / DECORATIVE`
- [x] intentional focal ownership / sequence
- [x] text-image dominance
- [x] focal region / crop intent
- [x] scale / negative space
- [x] responsive recrop/reposition/recomposition
- [x] Smoke H H1–H9 PASS
- [x] Program Lead: `IMAGERY_FOCAL_CORE = CLOSED`

Canonical evidence HEAD: `ad22a9a761eb89ec03ace3fd94625f6a6db6927e`.

### Composition / Anti-template

- [x] structure before pattern
- [x] Product priority + task/narrative flow before layout recipe
- [x] semantic containment before cards/panels
- [x] common AI/SaaS motifs are challenge triggers, not blanket bans
- [x] repetition = equivalence; variation = meaningful role/priority change
- [x] intentional asymmetry allowed when hierarchy remains clear
- [x] specificity over novelty
- [x] Product Truth / usability / accessibility remain boundaries
- [x] mobile recomposes rather than shrinking desktop coordinates
- [x] static `64/64 PASS`
- [x] Composition contracts `8/8 PASS`
- [x] fresh Astra semantic `14/14 PASS`
- [x] Smoke I I1–I9 PASS
- [x] Product / APPROVED DESIGN invariant
- [x] User Acceptance remains `NOT_GRANTED`
- [x] Program Lead: `COMPOSITION_ANTI_TEMPLATE_CORE = CLOSED`

Canonical Composition evidence HEAD: `2b75ca76d6fcadb8aedbc7c7f1390b3bc760ec28`.

Program Lead accepted the validation supplement from `6a499807826ca41a68616a0faa5d1f4007b60596`. Portable evidence: [Composition supplement](../../fixtures/contract-cases/evidence/astra-smoke-v1/composition-validation-supplement-v1/proof.md). It covers the original Composition package (`SKILL.md` SHA-256 `2440962d1be29e8274722efa86d8271327206ecdef9e9566bd30fc226002cc04`) and one Fieldlight Rentals countercase, not a new Bridge-package run. Earlier Smoke I remains a detailed-guidance bounded repair; neither case proves general autonomy or comparative superiority.

---

## 4. Optical / Detail Polish Gate

Decision:

```text
OPTICAL_CORE = DEFERRED; no demonstrated need before competition
```

Authority: `docs/decisions/JOEDESIGN_OPTICAL_GATE_V1.md`

Reason:

- preceding actual-render smokes do not show a recurring independent optical failure;
- Smoke I candidate-01 alignment failure was resolved through existing Composition rules;
- current Spatial, Typography, Color, Imagery, and Composition cores already cover the relevant bounded corrections.

Reopen only if competition or real-project evidence shows a recurring gap not covered by existing Craft Core.

---

## 5. CLOSED — Implementation Bridge (historical validation)

Program Lead: **Implementation Bridge v0.1 CLOSED — existing contracts and Smoke F scope only**. Evidence-repair baseline: `4ae644128a71f514ea10564400d6dc70e70ae0fa`. [Recovered execution proof](../../fixtures/contract-cases/evidence/astra-smoke-v1/bridge-evidence-repair-v1/proof.md), [Smoke F reuse/correction](../../fixtures/contract-cases/evidence/astra-smoke-v1/bridge-evidence-repair-v1/smoke-f-reuse.json).

Actual runtime identity, separate log/response hashes, fixed input readback and JSON response equality are verified. Encrypted request/correction plaintext and independent expected-answer/prior-response exclusion remain UNVERIFIED; earlier non-provision reports are HISTORICALLY_REPORTED only. Shared unrestricted filesystem is not OS isolation.

Smoke F HTML before/after is not byte-identical: before equals after plus one terminal LF. Separate hashes and original proof are preserved in the correction record. `status.attention.icon` remains intentionally unresolved; no future icon-specific claim is verified.

Everything below in this section describes the completed historical integration/validation. **Do not execute these transplant or validation steps again.** The original handoff remains a historical document; the frozen version is in Section 6 and the next handoff is in Section 7.

### Existing candidate

Historical candidate branch:

`codex/joedesign-v0.1-implementation-bridge`

Historical candidate implementation HEAD:

`f51a9f70b39d49bb023a3ffc080fe7a05227b9e8`

Canonical candidate spec:

`docs/specs/joedesign-implementation-bridge-v0.1.md`

Candidate scope:

- APPROVED `DESIGN.md` is authority; Bridge is derivative
- existing project-native token/component roles first
- unknown values remain unresolved
- Google `design.md` compatibility is optional interoperability
- custom JOEDESIGN sections preserved
- material mapping diff concept
- `Token Mapping PASS ≠ Visual PASS`
- no Google/vendor runtime dependency

### Critical integration rule

The historical Bridge branch predates Color, Imagery, and Composition cores.

**Never replace the current `SKILL.md`, `DESIGN.md` template, contract test, or evidence files with the old branch version.**

Instead:

```text
current Composition CLOSED core
→ inspect historical Bridge delta
→ transplant only Bridge-specific behavior/contracts/docs
→ preserve every newer Craft section and current evidence history
```

### Historical validation order (completed; not active instructions)

Because Bridge changes shipped skill bytes:

```text
current baseline 64/64
→ Bridge contracts RED or candidate-delta compatibility check
→ bounded Bridge transplant
→ Bridge 8/8
→ fresh Astra semantic 14/14
→ full 72/72
→ Smoke F
→ final 72/72
```

If Smoke F causes any later `skills/joedesign/**` change:

```text
fresh semantic again
→ full 72/72 again
→ rerun affected Smoke F
```

### Smoke F target

Neutral fictional project only.

Prove:

```text
APPROVED DESIGN.md
→ semantic project-native mapping
→ implementation
→ actual browser render
```

Required observables:

- [x] approved authority preserved
- [x] existing project-native role reused where equivalent
- [x] unnecessary token renaming/rearchitecture avoided
- [x] missing values remain unresolved rather than invented
- [x] custom JOEDESIGN sections survive interchange/handoff
- [x] material mapping change has bounded before/after evidence, with the terminal-LF reporting correction above
- [x] actual target render observed historically, not rerendered in this consolidation
- [x] Token Mapping PASS remains separate from Visual PASS and User Acceptance

Gate:

```text
IMPLEMENTATION_BRIDGE_V0_1 = CLOSED
```

Competition-before tooling that remains optional / not required:

- parser
- standalone lint CLI
- semantic diff engine
- CSS/Tailwind/DTCG exporter

Do not build these unless the bounded Bridge contract cannot be proven without them.

---

## 6. CLOSED — Pure Core Freeze / v0.1-test

Program Lead approved `JOEDESIGN_PURE_CORE_FROZEN = PASS` and `JOEDESIGN_ARM_READY_FOR_COMPETITION = PASS`. The user requested that this version be committed and pushed as a test version on 2026-09-07. These are current program decisions, not deductions from test counts.

| Identity | Value |
| --- | --- |
| Test version | `v0.1-test` |
| Test branch | `codex/joedesign-v0.1-test` |
| Frozen core / evidence source | `7f890c60ed3837efc1693aeeba33759f12c85383` |
| Source tree | `0945d2b7dafc671bd7afdd3b5b5daaf2678f8b6c` |
| Shipped package | Unchanged three-file `skills/joedesign/`; hashes in [README](../../README.md) |

This is a working MVP for practical evaluation, not a production release. Freeze means a fixed comparison baseline, not absence of possible improvements. Pin the exact test commit for each run; do not substitute a later branch head. The source commit above remains an immutable source of the same package. No Git tag or GitHub Release is created by this document designation.

[Historical freeze review evidence](../../fixtures/contract-cases/evidence/astra-smoke-v1/pure-core-freeze-v1/README.md) preserves the original pre-approval snapshot, commands, outputs, package identities and limitations. Its former pending statuses are historical; this section is the current phase-status authority. Do not rewrite historical evidence to simulate a new test or approval.

Evidence retained at its original scope:

- package/public boundary: one public entrypoint, zero competitor/runtime dependency, vendor payload, DB bundle or automatic router;
- inherited eight-file suite: baseline/final 72 PASS / 0 FAIL in the freeze record; this documents wording/package and stored-response checks, not 72 independent design jobs or a new run for this documentation publication;
- stored semantic responses: recovered Bridge execution 14/14 with verified native identity/log/input/output linkage; independent encrypted-message input exclusion and OS isolation remain UNVERIFIED;
- historical renders: each Smoke keeps its source package, fixture, state and viewport; the Composition countercase is not a fresh Bridge-package run;
- Product authority, APPROVED project DESIGN, User Acceptance separation, prior failures and the Smoke F terminal-LF correction remain preserved.

Actual design quality, density/scroll tradeoffs and work/document overhead should be assessed in the planned comparison rather than by adding speculative rules. User Acceptance, generalization, comparative superiority and readiness of all five arms remain unverified. Optical stays DEFERRED. Publishing `v0.1-test` does not run the comparison or resume BIO production.

---

## 7. BIO 5-way Competition

Comparison execution belongs to the **new TrackE agent**, not the TrackC BIO implementation agent. JOEDESIGN's frozen arm is ready for handoff; all-arm readiness, common inputs and execution authorization remain separate. This test-version publication neither accesses BIO inputs nor runs the comparison.

| Owner | Responsibility |
| --- | --- |
| JOEDESIGN lead / TrackB | Preserve the frozen candidate; review concrete defects, not speculative feature expansion |
| TrackC implementation agent | BIO production implementation; remains paused pending its own resumption decision |
| Existing TrackC lead chat | BIO brief, product priorities, evaluation criteria and adoption decisions |
| New TrackE agent | Comparison execution, separate participant contexts, evidence collection and anonymization; no autonomous winner selection |

Historical references to "TrackC handoff" must not be interpreted as assigning comparison execution to the BIO implementation agent. This role clarification does not alter Product or Visual authority.

Competitors:

1. Bare Astra x-high
2. Astra x-high + JOEDESIGN Pure
3. Astra x-high + Impeccable only
4. Astra x-high + UI UX Pro Max only
5. Figma Make

Round 1 target:

- BIO Opening Hero desktop `1440×900`
- mobile `390×844`
- first structural transition
- motion/interaction concept
- visual rationale
- actual visible render/prototype
- fresh isolated context per arm
- anonymous A–E output

Blind score:

```text
First impression 25
BIO brand/science fit 20
Composition/hierarchy 20
Originality/anti-template 15
Typography/detail 10
Mobile 10
```

`awesome-design-md` and oh-my-design are not main competitors. Reference-assisted A/B can happen after the main competition.

---

## 8. v0.2 Decision

Only after competition:

- decompose win/loss mechanisms
- separate Craft advantage from corpus advantage
- selectively adopt useful mechanisms
- optionally run OmD / awesome reference-assisted A/B
- revisit Google-compatible parser/lint/diff/export only if evidence justifies it

---

## 9. Hard boundaries

- Product meaning is never changed for visual convenience.
- Visual PASS never grants User Acceptance.
- Reference never auto-promotes to Project Authority.
- Unknown source facts remain unknown.
- JOE default taste never overrides APPROVED `DESIGN.md`.
- Common patterns are not blanket-banned.
- Anti-template is not a novelty score.
- No competitor/vendor runtime in v0.1 Pure Core.
- No speculative DB/router/CLI/asset/template infrastructure.
- Preserve failure evidence; never rewrite expected results to match a failure.
- No material Visual PASS without actual render observation.

---

## 10. Memory-loss recovery

Read in this order:

```text
1. AGENTS.md
2. docs/roadmaps/JOEDESIGN_V0_1_IMPLEMENTATION_ROADMAP.md
3. docs/architecture/JOEDESIGN_OPERATING_MODEL_V1.md
4. fixtures/contract-cases/evidence/astra-smoke-v1/pure-core-freeze-v1/README.md
5. current branch HEAD + diff + latest review evidence
```

Resume from the frozen test snapshot and TrackE handoff boundary. Previous phase handoffs and review packets preserve history, not permission to repeat CLOSED implementation or old transplant steps. Current Freeze approval is in Section 6. TrackC implementation and TrackE comparison execution are separate. Optical stays DEFERRED; User Acceptance and comparative superiority remain unverified.

---

## 11. Immediate Next Action

```text
Register the exact v0.1-test commit and package hashes with TrackE
→ existing TrackC lead chat confirms BIO product brief/evaluation inputs
→ TrackE checks all-arm runtime/common-input readiness
→ execute the comparison only within separate authorization; do not resume TrackC BIO production here
```
