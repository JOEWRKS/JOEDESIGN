# JOEDESIGN v0.1 Implementation Roadmap

**Status:** Active execution roadmap  
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
| Pure Core Freeze | REVIEW PREPARATION — not declared |
| BIO 5-way Competition | NOT AUTHORIZED by this task; readiness not declared |

현재 순서:

```text
Pure Core Freeze review preparation (documents/evidence only)
→ Program Lead final Freeze / readiness judgment
→ TrackC handoff only after that judgment and authorization
→ competition only when separately authorized
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

Everything below in this section describes the completed historical integration/validation. **Do not execute these transplant or validation steps again.** The original handoff remains a historical document; the active task is Section 6.

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

## 6. ACTIVE — Pure Core Freeze review preparation

Review baseline: `4ae644128a71f514ea10564400d6dc70e70ae0fa`, tree `77197aa9894de7c3691c28adf70df20b9fbf6fca`. Composition supplement source: `6a499807826ca41a68616a0faa5d1f4007b60596`.

Active resume/evidence pointer: [Pure Core Freeze review record](../../fixtures/contract-cases/evidence/astra-smoke-v1/pure-core-freeze-v1/README.md). This documents source identities, package hashes, approval pointers, versioned reuse, actual suite outputs, preserved failures and current limitations. The final result HEAD/tree belongs in the delivery report, not recursively inside its own commit.

Preparation checks are evidence/document checks, not a Freeze declaration:

- package/public checks: one public entrypoint; zero competitor/runtime dependency, vendor payload, DB bundle or automatic router; fixed three-file shipped package;
- existing eight-file suite: baseline and final 72 PASS / 0 FAIL, with command/exit/full output in the review record;
- saved semantic responses: recovered Bridge execution 14/14, no new model invocation; actual identity/log/input/output linkage is separate from unverified encrypted-message exclusion;
- actual-screen evidence: reuse each historical Smoke only for its recorded source package, fixture, state and viewport; Composition supplement uses its original Composition package, not Bridge;
- no shipped skill/test/scenario/response/Smoke-source changes; no new BIO access or work;
- preserve Product authority, APPROVED DESIGN invariants and User Acceptance NOT_GRANTED.

The operating model remains the role/authority map; its original expansion-candidate list is not today's phase schedule. Closed Craft/Reference/Bridge and deferred Optical status are governed here. No role, philosophy, doctrine or skill behavior is changed by this update.

**Pure Core Freeze and competition readiness remain undeclared. Program Lead alone makes the final judgment.** Preparation READY means ready for that review only.

---

## 7. BIO 5-way Competition

Future TrackC scope, not active execution instructions: run only after Program Lead's final judgment and separate authorization. This preparation neither accesses BIO inputs nor runs competition.

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

Resume the current review-preparation gate only. Previous phase handoffs/specs preserve history and authority, not permission to repeat CLOSED implementation or old transplant steps. Optical stays DEFERRED. A preparation READY report does not grant Freeze, competition readiness or User Acceptance.

---

## 11. Immediate Next Action

```text
Complete Pure Core Freeze review packet
→ Program Lead final judgment
→ TrackC handoff only after that judgment and authorization
```
