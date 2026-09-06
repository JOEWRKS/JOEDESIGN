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
| Optical / Detail Polish | DEFERRED — no demonstrated need before competition |
| Implementation Bridge | ACTIVE NEXT |
| Pure Core Freeze | PENDING |
| BIO 5-way Competition | PENDING |

현재 순서:

```text
Implementation Bridge validation
→ Pure Core freeze
→ BIO 5-way competition
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

## 5. ACTIVE — Implementation Bridge Validation

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

### Required validation order

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

- [ ] approved authority preserved
- [ ] existing project-native role reused where equivalent
- [ ] unnecessary token renaming/rearchitecture avoided
- [ ] missing values remain unresolved rather than invented
- [ ] custom JOEDESIGN sections survive interchange/handoff
- [ ] material mapping change has bounded before/after evidence
- [ ] actual target render observed
- [ ] Token Mapping PASS remains separate from Visual PASS and User Acceptance

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

## 6. Pure Core Freeze

After Bridge closes:

- [ ] public entrypoint = 1
- [ ] competitor runtime dependency = 0
- [ ] vendor payload = 0
- [ ] reference/template/asset DB bundle = 0
- [ ] automatic router = 0
- [ ] BIO exposure during core building = 0
- [ ] canonical doctrines and operating model have no material contradiction
- [ ] current full contract suite PASS
- [ ] current fresh Astra replay PASS
- [ ] required rendered smokes PASS
- [ ] current skill/template SHA recorded
- [ ] freeze commit recorded

Gate:

```text
JOEDESIGN_PURE_CORE_FROZEN = PASS
```

---

## 7. BIO 5-way Competition

Run only after Pure Core Freeze.

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
4. current phase handoff/spec
5. current branch HEAD + diff + latest review evidence
```

Then continue from the first open gate in this roadmap.

---

## 11. Immediate Next Action

```text
Implementation Bridge candidate transplant + validation on top of Composition CLOSED core
```
