# JOEDESIGN v0.1 — Product Specification

**Status:** IMPLEMENTATION BASELINE  
**Product:** JOEDESIGN  
**Repository:** `JOEWRKS/JOEDESIGN`  
**Target runtime:** GPT-6 Astra / xhigh  
**Primary use:** Web/UI visual design, design direction, visual proof, refinement, responsive translation, visual conformance  
**Public mental model:** `JOEDESIGN으로 디자인해.`

## Cross-system authority

JOEDESIGN follows the shared cross-system contract at:

- Repository: `JOEWRKS/joewrks-work-harness`
- Commit: `5e7497bd104527d5e6dbfc36011f0f5ee3668ff5`
- Path: `docs/contracts/JOEWRKS_CROSS_SYSTEM_AUTHORITY_V1.md`

The shared contract defines only cross-system ownership, handoff, re-entry, verification, and progression boundaries. It does not import historical JOENESS runtime behavior, skills, vendors, or workflow into JOEDESIGN.

---

# 1. Product Raison d’être

> **JOEDESIGN은 프로젝트의 승인된 제품 의미, 현재 구현, 레퍼런스와 기존 시각 맥락을 이해하고, 강한 시각 방향을 실제 결과로 탐색·비교·정제·검증하여 프로젝트의 지속 가능한 visual truth로 정착시키는 AI 디자인 시스템이다.**

JOEDESIGN의 목적은 AI가 그럴듯한 UI를 한 번 생성하는 것이 아니다.

해결해야 하는 문제:

- generic AI/SaaS template으로 회귀
- 제품 의미와 시각 표현의 괴리
- 레퍼런스의 표면적 복제
- 디자인 방향 없이 곧바로 production coding
- 구현 결과가 스스로 acceptance 기준이 되는 문제
- 기술적 PASS를 visual PASS로 오인
- rejection 후 근본 방향 대신 CSS polish만 반복
- desktop의 단순 축소로 mobile 처리
- 작은 피드백에도 전체 화면을 재생성
- 장기 프로젝트에서 visual authority 유실

핵심 제품 가치:

**Context Fidelity + Direction Quality + Visual Exploration + Target-Medium Proof + Precise Refinement + Visual Authority Preservation**

---

# 2. JOEFLOW / Product Definition Boundary

### Product Definition owns

- 제품 의미
- 기능 존재 여부
- 정책 / 권한
- IA
- flow / route
- state semantics
- data meaning
- failure / recovery meaning
- functional acceptance

### JOEFLOW owns

- lifecycle state
- authority pointer
- gate
- handoff
- re-entry
- progression / promotion

### JOEDESIGN owns

- visual direction
- composition
- hierarchy
- typography
- color / surface
- imagery / artwork
- spacing / density
- visual component grammar
- motion expression
- responsive visual translation
- visual proof
- visual refinement
- visual conformance
- project `DESIGN.md`

Canonical rule:

> **JOEDESIGN may visually interpret approved product truth but may not silently create, remove, or alter material product meaning.**

JOEFLOW is not a runtime dependency of JOEDESIGN. In a JOEFLOW-managed project, handoff and re-entry pass through JOEFLOW. Otherwise JOEDESIGN consumes the current user instruction and project-local product/UX authority directly.

---

# 3. Public Surface

Public entrypoint is exactly one concept:

```text
JOEDESIGN
```

Do not create separate public commands or concepts such as:

- `$visual-check`
- `$design-router`
- `$direction`
- `$proof`
- `$review`
- `$refine`

Those responsibilities remain internal.

---

# 4. Internal Mental Model

Internal behavior may be understood as:

```text
UNDERSTAND
    ↓
EXPLORE   ← only when needed
    ↓
PROVE
    ↓
REFINE
    ↓
VERIFY
    ↓
ACCEPT / PERSIST
```

This is not a mandatory waterfall. Perform only applicable responsibilities.

---

# 5. Context Intake

Before material design work, inspect only the context necessary for the current scope, prioritizing:

1. current user request
2. Product Definition / product authority
3. cross-system handoff when present
4. project root `DESIGN.md`
5. accepted visual evidence
6. rejected visual evidence
7. relevant current implementation
8. user-provided references/assets
9. named target surface/state/viewport

Rules:

- Do not ask the user for facts available from current evidence.
- Do not promote current implementation appearance to visual authority automatically.
- Rejected visual output is negative evidence, not positive authority.
- Tool/reference output is advisory evidence.
- Do not hide product ambiguity behind a visual decision.

---

# 6. Project Visual Authority — DESIGN.md

A project uses at most one root `DESIGN.md` as durable visual authority.

Lifecycle:

```text
ABSENT
→ DRAFT Rev 1
→ explicit user approval
→ APPROVED Rev 1
```

Material revision:

```text
APPROVED Rev N
→ DRAFT Rev N+1
→ proof
→ explicit user approval
→ APPROVED Rev N+1
```

A new DRAFT never automatically supersedes the current APPROVED revision.

`DESIGN.md` must not duplicate Product Definition.

Required structure:

```text
Status / Revision
Product Authority Pointer

Visual North Star
Experience / Brand Character
Durable Visual Principles

Typography
Color / Surface
Composition / Spatial Hierarchy
Imagery / Artwork
Component / Control Grammar
Motion / Interaction Expression
Responsive Translation
Accessibility / Legibility

Project-specific Anti-patterns
Reference Relationships
Approved Visual Evidence
Open Visual Decisions
```

Do not invent exact tokens, families, values, or rules merely to fill sections. Empty/non-applicable sections are acceptable.

---

# 7. Direction Exploration

Direction exploration is required when:

- visual direction is absent
- material direction is unresolved
- the user asks for alternatives
- a material redesign is requested
- the same direction has been materially rejected repeatedly

Default unresolved-direction behavior:

```text
2–3 materially different directions
```

Differences should be meaningful, not color swaps. They may vary in:

- composition
- hierarchy
- image dominance
- typographic character
- spatial rhythm
- density
- geometry
- contrast
- motion character
- visual metaphor

All candidates must preserve the same Product Truth.

Do not force alternatives when:

- an APPROVED `DESIGN.md` already defines the direction
- there is an approved exact visual target
- the user requests refinement of a specific approved direction
- the task is a concrete visual defect

---

# 8. Reference Handling

References are relationship evidence, not recipes.

When a reference materially informs a decision, capture as needed:

```text
TAKE
DO NOT TAKE
WHY
APPLIES TO
```

A reference never becomes project authority by itself.

---

# 9. Visual Proof Before Expansion

Do not expand a material visual direction into broad production before the smallest useful proof exists.

Examples:

- Hero keyframe
- one transition
- one complex component/state
- desktop/mobile pair

## Target-medium-first

Proof should be produced as close as practical to the final target medium.

For web work, prefer:

```text
bounded implementation
→ actual browser render
→ critique / refine
```

Image-generation mockups are supplementary for art direction, composition probes, or when the target runtime is unavailable. A mockup alone cannot prove production fidelity.

---

# 10. User Choice and Approval

Materially different design directions are not automatically promoted by internal scoring.

JOEDESIGN should expose meaningful candidates, explain their differences, and obtain user choice/acceptance where required.

`ㄱㄱ`, `진행`, `구현` may authorize continuation within current scope, but they do not automatically constitute material visual acceptance when explicit acceptance is still required.

Only accepted results may become durable visual authority.

---

# 11. Refinement vs Redesign

### Refinement

Preserves the current direction while improving details such as:

- spacing
- type hierarchy
- scale
- crop
- alignment
- balance
- color tuning
- detail craft

### Redesign

Replaces or materially changes the current direction, composition, or visual system.

A local refinement request must not silently trigger a broad redesign. Conversely, a direction-level problem must not be handled indefinitely through numeric polish alone.

---

# 12. Exact-target Refinement

Local feedback should produce local work.

Expected behavior:

```text
exact surface/state
→ inspect current actual render
→ identify affected relationship
→ bounded change
→ rerender same target
```

Forbidden default behavior:

```text
local feedback
→ regenerate entire page
```

Broaden scope only when the user or evidence requires a real redesign.

---

# 13. Rejection Handling

After the same visual direction is materially rejected twice, do not default to a third local polish pass.

Return to direction-level diagnosis:

- composition problem?
- visual metaphor problem?
- artwork ownership problem?
- reference interpretation problem?
- hierarchy problem?
- product truth misunderstanding?

Then re-enter EXPLORE / PROVE only for the affected scope.

---

# 14. Responsive Translation

Mobile is not scaled desktop.

Preserve intent across targets by evaluating:

- hierarchy
- artwork ownership
- focal point
- information order
- negative space
- control reachability
- crop
- viewport height/aspect
- transition continuity

JOEDESIGN may recompose visual presentation, crop, order, and density.

Product Definition re-entry is required if the change alters:

- feature existence
- policy
- material content
- behavior
- navigation meaning

---

# 15. Motion

Product Definition owns semantic states/transitions.

JOEDESIGN owns their visual expression:

- timing
- easing
- spatial continuity
- visual feedback
- transformation
- motion restraint
- interaction feel

Material/signature motion should be proven in a bounded prototype before broad integration. Consider reduced-motion when applicable.

---

# 16. Actual-output Review

Do not expose a separate public `$visual-check`. Visual conformance is an internal JOEDESIGN responsibility.

Core logic:

```text
Expected observable
→ Actual observed fact
→ PASS / FAIL / UNVERIFIED
```

For each material claim, capture as applicable:

- authority/source
- target artifact/version
- surface
- state
- viewport/dimensions
- expected observable
- actual observation
- verdict

No observation means no PASS.

The following do not prove visual appearance by themselves:

- build success
- DOM existence
- code inspection only
- test pass
- screenshot file existing on disk
- plausibility language

Visual conformance requires actual rendered-output evidence appropriate to the claim.

---

# 17. PASS Separation

Always preserve:

```text
Technical PASS
≠ Product PASS
≠ Visual PASS
≠ User Acceptance
```

JOEDESIGN visual PASS does not create user acceptance.

In JOEFLOW-managed projects, JOEDESIGN verdicts become progression evidence rather than progression authority.

---

# 18. Product Ambiguity Re-entry

JOEDESIGN must not resolve material product ambiguity by itself.

JOEFLOW-managed project:

```text
JOEDESIGN
→ affected product ambiguity
→ JOEFLOW bounded re-entry
→ Product Definition
→ resolution
→ JOEDESIGN resume
```

Standalone project:

```text
JOEDESIGN
→ current Product authority / user
```

Re-enter only the affected scope. Do not restart the entire design lifecycle unnecessarily.

---

# 19. External Design Capability Policy — v0.1

v0.1 must remain a pure JOEDESIGN Core so that the planned design competition can measure its unique value.

Do not bundle or depend on:

- Impeccable
- UI UX Pro Max
- Figma Make methodology
- Apple Design
- Hallmark
- Refero orchestration
- oh-my-design
- Watermelon
- Componentry
- Cult UI

Good ideas learned from external products may be implemented as independent principles, but not as hidden runtime/vendor dependencies.

Only mechanisms with demonstrated unique benefit in the later competition or real project evidence become v0.2 integration candidates.

---

# 20. General Tool Policy

JOEDESIGN may use normal Astra capabilities needed by the authorized task, such as:

- browser/rendering tools
- image generation
- repository/code tools
- existing project runtime
- user-provided Figma artifacts when relevant

During benchmark runs, the Competition Controller must freeze allowed capabilities consistently across comparable arms.

JOEDESIGN must not silently call competitor-specific design-intelligence systems during the pure-core comparison.

---

# 21. Non-goals

v0.1 does not build:

- PM system
- ticket system
- multi-agent orchestrator
- lifecycle control plane
- vendor router
- capability marketplace
- component zoo
- universal visual aesthetic
- giant design database
- separate visual-verification skill
- mandatory seven-stage workflow
- general-purpose evaluation platform
- JOENESS runtime revival

---

# 22. Repository Architecture

Current repository:

```text
JOEWRKS/JOEDESIGN
```

Recommended minimal tree:

```text
JOEDESIGN/
├─ README.md
├─ AGENTS.md
├─ skills/
│  └─ joedesign/
│     ├─ SKILL.md
│     ├─ agents/
│     │  └─ openai.yaml
│     └─ templates/
│        └─ DESIGN.md
├─ docs/
│  ├─ specs/
│  │  └─ joedesign-v0.1.md
│  └─ handoff/
├─ tests/
│  └─ joedesign-contract.tests.mjs
└─ fixtures/
   └─ contract-cases/
```

Do not add more subsystems until a real requirement proves they are necessary.

---

# 23. Minimum Contract Tests

Deterministically lock at least these behaviors:

1. single public entrypoint
2. Product Truth cannot be overridden by visual authority
3. `DESIGN.md` lifecycle
4. unresolved direction → meaningful alternatives
5. approved direction → no unnecessary alternative fanout
6. reference relationship handling
7. target-medium proof
8. exact-target refinement
9. refinement vs redesign separation
10. repeated rejection → direction reconsideration
11. responsive translation
12. product ambiguity → correct re-entry
13. actual-output PASS / FAIL / UNVERIFIED
14. technical PASS ≠ visual PASS
15. visual PASS ≠ user acceptance
16. external competitor runtime/vendor dependencies absent

---

# 24. Runtime Semantic Smoke

Static wording/contract tests alone cannot establish readiness.

Use fresh GPT-6 Astra / xhigh sessions for at least two semantic smokes.

## Smoke A — unresolved direction

Use a neutral non-BIO fixture where Product Truth is defined and visual direction is not.

Expected behavior:

- inspect current product truth
- identify unresolved visual direction
- produce 2–3 materially distinct options
- preserve product semantics
- create/propose bounded proof before broad expansion
- do not auto-promote a candidate to approved authority

## Smoke B — approved refinement

Use a neutral fixture with APPROVED `DESIGN.md` and an existing rendered target.

Request a narrow Hero typography-hierarchy refinement.

Expected behavior:

- no unnecessary alternatives
- no broad redesign
- exact-target change only
- reobserve the same rendered target
- preserve visual-verdict vs user-acceptance boundary

Do not use BIO source, screenshots, assets, or competition brief in these smokes.

---

# 25. Distribution

A large installer framework is not required for v0.1 competition readiness.

Provide the smallest practical project-local and/or explicit personal skill installation method.

Installer automation is a separate follow-up only if actual usage proves it to be a blocker.

---

# 26. Competition Readiness Gate

Declare:

```text
JOEDESIGN_MVP_READY_FOR_COMPETITION
```

only when all of the following have current evidence:

- independent repository exists
- exactly one public JOEDESIGN entrypoint
- external design-competitor dependency count = 0
- `DESIGN.md` lifecycle implemented
- Product/Visual authority separation implemented
- conditional alternatives implemented
- bounded proof implemented
- target-medium-first behavior implemented
- exact-target refinement implemented
- responsive translation implemented
- actual rendered visual review implemented
- user-acceptance boundary implemented
- cross-system re-entry implemented
- deterministic contract suite PASS
- fresh Astra semantic Smoke A PASS
- fresh Astra semantic Smoke B PASS
- no BIO benchmark exposure during smokes
- documentation matches actual behavior

---

# 27. Stop Rule

Once the competition-readiness gate is satisfied, stop v0.1 feature development.

Do not add features before the competition merely because they appear useful.

New features require evidence from:

- the 5-way design competition, or
- a real project failure/gap.

---

# 28. v0.1 Success Definition

> 사용자가 승인된 Product Truth와 프로젝트 맥락을 제공하고 `JOEDESIGN으로 디자인해`라고 요청했을 때, Astra가 generic한 단일 시안을 곧바로 production으로 확대하지 않고, 필요한 경우 의미 있는 방향을 탐색하고, 실제 target에 가까운 proof를 만들고, 사용자의 선택을 보존하며, 정확한 target만 반복적으로 refine하고, desktop/mobile 결과를 실제로 관찰하여 visual truth를 `DESIGN.md`에 지속 가능하게 유지할 수 있다.

This is the product completion line for JOEDESIGN v0.1.
