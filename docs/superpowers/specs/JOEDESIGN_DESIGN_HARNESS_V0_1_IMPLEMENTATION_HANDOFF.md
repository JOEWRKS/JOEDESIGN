# JOEDESIGN Design Harness v0.1 — Implementation Handoff

**Project:** JOEWRKS / JOEDESIGN  
**Document type:** Implementation specification + execution checklist + agent instruction  
**Status:** READY FOR IMPLEMENTATION PLANNING / NOT YET IMPLEMENTED  
**Date:** 2026-09-28  
**Primary goal:** AI가 웹 디자인을 자율 생성할 때 발생하는 **낮은 시각 품질, generic AI/PPT/dashboard 수렴, responsive/state 결함, reference drift, 과확장 및 허위 완료 보고**를 줄인다.

---

# 0. 한 줄 정의

`JOEDESIGN Design Harness v0.1`은 하나의 거대한 디자인 프롬프트가 아니다.

> **JOEFLOW/Product Intent → Oh My Design reference retrieval → Reference Lock → JOEDESIGN synthesis → 실제 웹 구현 → Impeccable craft pass → Browser evidence → Independent critic → User approval**

을 순서대로 강제하고, 각 단계의 입력·출력·권한·STOP 조건을 통제하는 **디자인 전용 Controller**다.

---

# 1. 왜 만드는가

현재 문제는 단순히 "검증을 덜 했다"가 아니다.

반복해서 확인된 실패는 다음과 같다.

- AI가 디자인을 자유롭게 만들면 PPT / dashboard / generic SaaS / giant background image 쪽으로 수렴한다.
- 큰 composition뿐 아니라 spacing, typography, alignment, component state, dark/light surface ownership 같은 세부 craft 오류도 자주 발생한다.
- Desktop 구조를 Mobile에 축소·전파한다.
- 국소 수정이 다른 surface에 전파된다.
- 여러 reference/plugin/skill의 결과를 섞으면서 현재 visual authority가 불명확해진다.
- 기술 PASS가 시각 PASS처럼 취급된다.
- 구현자가 자기 결과를 직접 PASS 판정하면서 confirmation bias가 생긴다.
- 실제로 확인하지 않은 route/state까지 완료했다고 일반화하는 문제가 발생한다.

따라서 목표는 Astra에게 더 많은 추상 디자인 이론을 외우게 하는 것이 아니다.

목표는:

1. **좋은 디자인 근거를 먼저 제한적으로 선택하고**
2. **선택된 근거의 역할을 잠그고**
3. **그 근거를 프로젝트에 맞게 합성하고**
4. **실제 동작하는 웹으로만 증명하고**
5. **독립 검수와 사용자 승인 없이는 완료하지 못하게 하는 것**

이다.

---

# 2. 핵심 설계 원칙

## 2.1 Global harness는 얇게, Design harness는 강하게

JOENESS/Astra global runtime 전체를 다시 무겁게 만들지 않는다.

이 Controller는 **material visual design / redesign / visual implementation** 작업에만 활성화한다.

일반 코드 수정, backend, 비시각 refactor에는 적용하지 않는다.

## 2.2 JOEDESIGN v0.2는 동결한다

기존 검증된 JOEDESIGN v0.2의 역할:

- approved visual target interpretation
- visual authority semantics
- project-specific translation
- bounded correction
- responsive/state preservation
- original-versus-result gap diagnosis
- user acceptance 분리

이 역할은 유지한다.

`skills/joedesign/`를 v0.1 Harness 구현 때문에 재작성하지 않는다.

## 2.3 Oh My Design은 corpus다

Oh My Design을 fork하거나 별도 대형 DB로 다시 만들지 않는다.

역할:

> **실제 디자인 시스템/reference corpus**

Harness가 맡는 역할:

> **Intent 기반 retrieval + selection + role assignment + provenance lock**

즉:

```text
Oh My Design = corpus
Harness = retriever / selector / orchestrator
JOEDESIGN = project-specific synthesizer
```

## 2.4 Reference는 평균내지 않는다

금지:

```text
Apple typography
+ Linear layout
+ Stripe cards
+ Toss color
+ biotech image
= 새 디자인
```

허용:

```text
Primary A
  owns: composition, type rhythm, imagery dominance

Secondary B
  owns: interaction/state treatment only

Secondary C
  owns: mobile recomposition only
```

**동일 디자인 축을 두 reference가 동시에 소유하지 못한다.**

## 2.5 Static concept art는 웹 디자인 proof가 아니다

웹 작업에서 다음만 존재하면 material visual implementation 완료로 볼 수 없다.

- ImageGen PNG
- static mockup
- generated concept art
- screenshot-like image

웹 디자인 proof는 실제 target runtime에서 최소 다음을 포함해야 한다.

- HTML/React/component
- CSS/layout
- responsive
- required interaction/state
- browser render
- exact viewport/state evidence

## 2.6 Impeccable은 Authority가 아니라 Craft Specialist다

Impeccable은 다음을 다듬는다.

- typography
- spacing
- alignment
- component polish
- motion craft
- responsive craft
- interaction detail
- anti-slop detail

Impeccable이 다음을 바꾸면 안 된다.

- Product meaning
- Primary composition
- Reference ownership
- visual direction
- surface role
- information architecture

이 경계를 넘으면 자동 수정하지 않고 Harness가 `SCOPE_ESCALATION_REQUIRED`로 중단한다.

## 2.7 Critic은 또 다른 디자이너가 아니다

Independent critic의 역할:

> 디자인을 새로 만드는 것이 아니라 **잠긴 디자인 의도와 실제 결과 사이의 결함을 찾는 것**

Critic은 새 디자인 방향을 제시하지 않는다.

Critic 결과:

- `PASS`
- `FAIL`
- `UNVERIFIED`

만 사용한다.

숫자 점수는 v0.1에서 사용하지 않는다.

---

# 3. v0.1 목표 / 비목표

## 목표

- JOEFLOW/Product Definition 결과에서 Design Intent를 추출한다.
- Oh My Design corpus에서 관련 reference 후보를 찾는다.
- Primary 1개 + Secondary 최대 2개의 역할을 잠근다.
- JOEDESIGN v0.2가 프로젝트-specific Design Contract를 생성하도록 한다.
- 실제 웹 구현 전 Reference Lock과 Design Contract를 강제한다.
- Impeccable을 craft-only 역할로 제한한다.
- route/surface/viewport/state matrix를 사전에 만든다.
- 실제 Browser evidence가 없으면 Visual PASS를 막는다.
- fresh-context critic을 지원한다.
- User Acceptance를 모든 내부 PASS와 분리한다.
- false-completion 및 scope creep를 구조적으로 차단한다.

## 비목표

v0.1에서는 다음을 만들지 않는다.

- 자체 vector DB
- embedding service
- 자체 design model
- Oh My Design fork
- 별도 GUI
- cloud service
- critic ensemble
- multi-agent voting
- 자동 미감 점수 시스템
- global JOENESS integration
- JOEFLOW 자체 수정
- 이미지 생성 기반 디자인 엔진
- 모든 프로젝트용 강제 lifecycle
- 기존 JOEDESIGN v0.2 재설계

---

# 4. 추천 파일 구조

```text
JOEDESIGN/
├─ skills/
│  ├─ joedesign/                      # 기존 v0.2, 변경 금지
│  │
│  └─ joedesign-harness/
│     ├─ SKILL.md                     # public controller entrypoint
│     ├─ agents/
│     │  └─ openai.yaml
│     ├─ references/
│     │  ├─ pipeline.md
│     │  ├─ authority.md
│     │  ├─ reference-selection.md
│     │  ├─ gates.md
│     │  ├─ impeccable-boundary.md
│     │  └─ critic.md
│     ├─ templates/
│     │  ├─ DESIGN_INTENT.json
│     │  ├─ REFERENCE_CANDIDATES.json
│     │  ├─ REFERENCE_LOCK.md
│     │  ├─ DESIGN_CONTRACT.md
│     │  ├─ STATE_MATRIX.md
│     │  ├─ CRITIQUE.md
│     │  └─ EVIDENCE_MANIFEST.json
│     ├─ schemas/
│     │  ├─ design-intent.schema.json
│     │  ├─ reference-candidates.schema.json
│     │  ├─ reference-lock.schema.json
│     │  ├─ design-contract.schema.json
│     │  ├─ state-matrix.schema.json
│     │  ├─ critique.schema.json
│     │  └─ evidence-manifest.schema.json
│     └─ scripts/
│        ├─ build_omd_index.py
│        ├─ retrieve_references.py
│        ├─ validate_reference_lock.py
│        ├─ validate_design_contract.py
│        ├─ validate_state_matrix.py
│        ├─ build_evidence_manifest.py
│        └─ validate_handoff.py
│
├─ tests/
│  ├─ test_joedesign_harness_contract.py
│  ├─ test_design_intent.py
│  ├─ test_omd_retrieval.py
│  ├─ test_reference_lock.py
│  ├─ test_design_contract.py
│  ├─ test_state_matrix.py
│  ├─ test_critic_contract.py
│  └─ test_handoff.py
│
└─ evals/
   └─ harness-v0.1/
      ├─ README.md
      ├─ control/
      ├─ candidate/
      └─ fixtures/
```

경로는 현재 repository 구조에 맞춰 조정 가능하지만 책임 분리는 유지한다.

---

# 5. Runtime artifact 구조

각 디자인 작업에서 프로젝트 안에 아래 artifact를 생성한다.

```text
.design-harness/
├─ DESIGN_INTENT.json
├─ REFERENCE_CANDIDATES.json
├─ REFERENCE_LOCK.md
├─ DESIGN_CONTRACT.md
├─ STATE_MATRIX.md
├─ CRITIQUE.md
└─ EVIDENCE_MANIFEST.json
```

## Authority 주의

`.design-harness/*`는 작업용 execution artifact다.

최종 visual authority가 아니다.

최종 승인된 durable visual truth는 기존 원칙대로 project root `DESIGN.md`에만 승격한다.

사용자 승인 전 `.design-harness/DESIGN_CONTRACT.md`를 `APPROVED` authority로 취급하지 않는다.

---

# 6. 단계별 Contract

## 6.1 DESIGN_INTENT

입력:

- JOEFLOW artifact
- Product Definition
- user brief
- root DESIGN.md
- current implementation
- current assets
- explicit user constraints

출력:

`DESIGN_INTENT.json`

최소 필드:

```json
{
  "surface": {
    "name": "",
    "type": "",
    "routes": [],
    "platform": "web"
  },
  "product": {
    "primary_goal": "",
    "primary_user": "",
    "information_density": "",
    "required_content": [],
    "required_actions": []
  },
  "visual": {
    "tone": [],
    "brand_traits": [],
    "avoid": []
  },
  "interaction": {
    "required_states": [],
    "required_behaviors": [],
    "motion_character": ""
  },
  "responsive": {
    "target_viewports": [],
    "mobile_contract": ""
  },
  "authority": {
    "product_sources": [],
    "visual_sources": [],
    "approved_sources": [],
    "rejected_directions": []
  }
}
```

금지:

- reference 검색 전 구체 색상/레이아웃을 임의 확정
- "healthcare니까 blue" 같은 category shortcut
- Product 의미를 visual simplification을 위해 제거

## 6.2 OMD Reference Retrieval

입력:

`DESIGN_INTENT.json`

출력:

`REFERENCE_CANDIDATES.json`

v0.1 retrieval 절차:

```text
local OMD catalog
→ metadata normalization
→ hard filters
→ lexical/metadata relevance
→ top 8~12 candidates
→ agent inspection 3~5
→ final lock candidates
```

v0.1에서는 embedding/vector DB를 사용하지 않는다.

### 검색 차원

- product/surface type
- content density
- visual tone
- typography character
- composition
- image/media ownership
- component grammar
- interaction character
- responsive character
- surface/background model
- known avoid patterns
- reference quality / freshness

### 후보 우선순위

기본 우선:

```text
Verified > Partial > Legacy
```

단, 이것은 aesthetic ranking이 아니다.

Legacy/Partial reference를 선택할 수 있으나:

- 선택 이유를 기록
- missing facts를 `UNKNOWN` 처리
- 없는 interaction/motion 값을 추론하지 않음

### provenance

각 retrieval run은 최소 다음을 기록한다.

- corpus root
- retrieval timestamp
- catalog fingerprint 또는 Git commit 가능 시 commit
- reference ID/path
- quality status
- inspected candidate count

## 6.3 REFERENCE_LOCK

최종 선택:

```text
Primary: 정확히 1개
Secondary Interaction: 0~1
Secondary Responsive/Component: 0~1
```

Primary는 material redesign에서 필수다.

### Template

```markdown
# Reference Lock

## Primary
SOURCE:
QUALITY:
PROVENANCE:

OWNS:
- composition
- typography rhythm
- imagery/media dominance
- section rhythm

TAKE:
- ...

DO NOT TAKE:
- brand identity
- copy
- product semantics
- unrelated navigation
- ...

APPLIES TO:
- ...

UNKNOWN:
- ...

## Secondary — Interaction
SOURCE:
OWNS:
- selected-state / hover / transition only

TAKE:
- ...

DO NOT TAKE:
- palette
- typography
- page composition

## Secondary — Responsive
SOURCE:
OWNS:
- mobile recomposition only
```

### Hard Rule

동일 축에 둘 이상의 owner가 있으면 validator FAIL.

예:

```text
Primary owns composition
Secondary also owns composition
→ REFERENCE_LOCK_CONFLICT
```

## 6.4 DESIGN_CONTRACT

JOEDESIGN v0.2가 생성한다.

입력:

- DESIGN_INTENT
- REFERENCE_LOCK
- Product authority
- root DESIGN.md
- current implementation
- real assets

출력:

`DESIGN_CONTRACT.md`

최소 항목:

```markdown
# Design Contract

## Scope
## Product invariants
## Visual thesis
## Primary composition
## Visual flow
## Typography roles
## Spatial rhythm
## Imagery/media ownership
## Surface roles
## Component grammar
## Interaction states
## Motion character
## Responsive composition
## Forbidden patterns
## Allowed implementation freedom
## Exact proof targets
## Unknowns
```

각 material decision에는 가능하면 source를 표시한다.

```text
SOURCE:
- PRODUCT
- APPROVED_PROJECT_AUTHORITY
- PRIMARY_REFERENCE
- SECONDARY_REFERENCE
- JOEDESIGN_PROJECT_PROPOSAL
```

`JOEDESIGN_PROJECT_PROPOSAL`은 승인된 source truth처럼 표현하면 안 된다.

---

# 7. Surface Contract

Material web 작업 전 대상 surface를 분류한다.

기본 family:

```text
Narrative
Evidence
Utility
Detail
Interactive Workspace
```

필요하면 프로젝트-specific type 추가 가능.

각 surface에 최소 다음을 정의한다.

```text
surface role
background ownership
foreground semantics
interaction density
scroll behavior
responsive model
content priority
shared selector allowance
```

### Hard Rule

서로 다른 surface family를 동일 global style override로 묶는 경우 사전 blast-radius evidence 필요.

다음과 같은 변경은 기본적으로 경고/STOP 대상:

```css
.text-* global recolor
.bg-* global transparency
!important theme remap
broad selector override across Narrative + Utility + Detail
```

---

# 8. Scope / Blast Radius Guard

한 execution slice는 기본적으로 다음 중 하나다.

```text
one route
one section
one component family
one coherent state family
```

다음 조건이면 자동 확장 금지:

- 새로운 route family를 건드려야 함
- Product flow 변경 필요
- 승인된 다른 surface composition 변경 필요
- global selector 변경으로 여러 route 영향
- 기존 rejected grammar 재활성화 필요

상태:

`SCOPE_EXPANSION_REQUIRED`

로 중단하고 사용자/상위 controller 판단을 요구한다.

---

# 9. State Machine

```text
INTENT_READY
    ↓
REFERENCES_FOUND
    ↓
REFERENCE_LOCKED
    ↓
CONTRACT_READY
    ↓
IMPLEMENTED
    ↓
CRAFTED
    ↓
PROOF_COMPLETE
    ↓
CRITIC_REVIEWED
    ↓
USER_REVIEW
    ↓
APPROVED
```

## Gate Rules

```text
DESIGN_INTENT invalid
→ REFERENCES_FOUND 금지

Primary reference 없음
→ material CONTRACT_READY 금지

REFERENCE_LOCK conflict
→ implementation 금지

Design Contract 없음
→ material code generation 금지

Static PNG only
→ IMPLEMENTED 인정 금지 (web task)

State Matrix incomplete
→ PROOF_COMPLETE 금지

Required browser state 미관찰
→ 해당 claim UNVERIFIED

Critic FAIL
→ VISUAL_INTERNAL_PASS 금지

Critic unavailable
→ CRITIC_UNVERIFIED
→ 사용자에게 proof를 보여주는 것은 가능
→ "Visual Internal PASS" 주장은 금지

User exact acceptance 없음
→ APPROVED 금지
```

---

# 10. Actual Web Implementation Contract

웹 작업에서 구현자는 실제 product runtime을 수정/구현한다.

필수:

- real component
- real data/model
- real responsive layout
- real required interaction
- real state transitions
- actual browser render

금지:

- product data를 디자인 편의를 위해 fork
- static image만 만들어 production design 완료 주장
- mockup에만 존재하는 interaction
- user-approved scope 밖의 broad redesign
- reference screenshot 자체를 그대로 복제

---

# 11. Impeccable Craft Pass

## 위치

```text
Reference Lock
→ JOEDESIGN Contract
→ Implementation
→ Impeccable Craft Pass
```

## 허용

- spacing refinement
- local alignment
- hierarchy clarity
- typography craft
- touch target
- focus/hover clarity
- responsive local polish
- motion craft
- component micro polish
- anti-slop cleanup

## 금지

- new composition
- new visual direction
- primary reference 교체
- surface role 변경
- Product semantics 변경
- information architecture 변경
- material layout ownership 변경

경계 초과:

`CRAFT_SCOPE_VIOLATION`

자동 적용 금지.

---

# 12. STATE_MATRIX

Browser proof 전에 생성한다.

예:

```markdown
| Route/Surface | Viewport | State | Required | Observed | Evidence | Result |
|---|---|---|---|---|---|---|
| /pipeline | 1440×900 | opening | YES | YES | ...png | PASS |
| /pipeline | 390×844 | opening | YES | YES | ...png | PASS |
| Evidence | 1440×900 | BX-201 selected | YES | NO | - | UNVERIFIED |
```

### Required dimensions

각 프로젝트/contract가 정의한다.

무조건 1440×900 / 390×844를 재사용하지 않는다.

### Out of scope

검사하지 않는 state도 사전에 기록한다.

`OUT_OF_SCOPE`

사후에 누락된 state를 조용히 지우지 않는다.

---

# 13. Browser Evidence Gate

각 required row에 대해 가능한 범위에서 기록한다.

- route
- surface
- viewport
- state
- screenshot
- console error
- page error
- failed request
- horizontal overflow
- broken asset
- interaction result
- focus behavior
- reduced motion if applicable

Visual claim은 실제 render observation 없이는 PASS 불가.

```text
Technical PASS ≠ Responsive PASS
Responsive PASS ≠ Visual PASS
Visual Internal PASS ≠ User Acceptance
```

---

# 14. Independent Critic

## 목적

confirmation bias 차단.

## 원칙

가능하면 fresh context / separate agent를 사용한다.

Critic에 전달:

- DESIGN_INTENT
- REFERENCE_LOCK
- DESIGN_CONTRACT
- actual screenshots
- state/interaction evidence

기본적으로 전달하지 않음:

- implementer의 자기 평가
- 이전 PASS 문구
- 긴 chain-of-thought
- 결과를 정당화하는 서술

필요할 때만 code를 보조 evidence로 제공한다.

## 출력

```markdown
# Critique

## Claim 1
Expected:
Observed:
Evidence:
Verdict: PASS | FAIL | UNVERIFIED

## Claim 2
...
```

Critic은 새 디자인을 제안하지 않는다.

FAIL은 "어디가 contract/reference와 달라졌는지"를 특정한다.

---

# 15. Repair Loop

Critic FAIL:

```text
FAIL
→ exact target diagnosis
→ bounded repair
→ rerender
→ critic recheck
```

동일 material direction에서 최대 2회.

2회 이후에도 material FAIL이면:

```text
LOCAL_POLISH_STOP
MATERIAL_REWORK_REQUIRED
```

로 synthesis/reference 단계로 돌아간다.

무한 CSS tweak 금지.

---

# 16. User Acceptance

내부 모든 상태와 분리한다.

사용자에게 제출할 때:

```text
Technical:
Responsive:
Accessibility:
Craft:
Visual Internal:
Critic:
User Acceptance: PENDING
```

사용자의 exact output 승인 후에만:

`USER VISUAL ACCEPTANCE: APPROVED`

로 변경한다.

`진행`, `ㄱㄱ`, 구현 허가 등은 exact visual acceptance로 자동 해석하지 않는다.

---

# 17. Evidence Manifest

최종 visual proof package에 최소:

```json
{
  "run": {},
  "authority": {},
  "references": [],
  "targets": [],
  "screenshots": [],
  "interactions": [],
  "technical": {},
  "critic": {},
  "unverified": []
}
```

을 기록한다.

전체 PASS라는 문구를 사용할 수 있는 조건:

- STATE_MATRIX required rows 모두 evidence 존재
- 해당 category의 required gates 모두 PASS
- 미검증 row 없음 또는 명시적으로 OUT_OF_SCOPE
- User Acceptance는 별도

---

# 18. 구현 체크리스트

## P0 — Baseline / Spec Lock

- [ ] 현재 JOEDESIGN repository clean baseline 확인
- [ ] 기존 `skills/joedesign/` SHA/hash 기록
- [ ] v0.2 package가 Harness 구현 중 변경되지 않도록 regression check 추가
- [ ] `docs/superpowers/specs/...design-harness-v0.1-design.md` 작성
- [ ] Scope / Non-goal 고정
- [ ] public entrypoint 이름 `joedesign-harness` 확정
- [ ] root JOEDESIGN과 Harness authority 관계 명시
- [ ] OMD / Impeccable / Critic 역할 경계 문서화
- [ ] user acceptance semantics 문서화
- [ ] spec self-review
- [ ] spec commit

**PASS:** 구현자가 "무엇을 만들고 무엇을 만들지 않는지" 추가 판단 없이 이해 가능.

## P1 — Skill Skeleton / Artifact Contracts

- [ ] `skills/joedesign-harness/SKILL.md`
- [ ] `agents/openai.yaml`
- [ ] references 파일 생성
- [ ] templates 파일 생성
- [ ] schemas 파일 생성
- [ ] artifact directory naming 고정
- [ ] runtime state naming 고정
- [ ] invalid transition test 작성
- [ ] package validation test 작성
- [ ] `python -m unittest discover -s tests -v`
- [ ] commit

**PASS:** skill package가 독립 discovery 가능하고 기존 JOEDESIGN을 수정하지 않음.

## P2 — DESIGN_INTENT Adapter

- [ ] Product/JOEFLOW input pointer contract 정의
- [ ] existing DESIGN.md read-only authority 처리
- [ ] approved/rejected direction extraction 규칙
- [ ] required states 추출
- [ ] avoid-pattern 추출
- [ ] surface family 분류
- [ ] responsive target contract
- [ ] `DESIGN_INTENT.json` validator
- [ ] missing product meaning → `NEEDS_PRODUCT_INPUT`
- [ ] aesthetic guess를 Product truth로 쓰지 않는 fixture
- [ ] tests
- [ ] commit

**PASS:** reference 검색에 필요한 의미는 충분하지만 아직 layout/color를 임의 확정하지 않음.

## P3 — Oh My Design Index

- [ ] OMD local catalog root 입력 방식 정의
- [ ] OMD corpus 전체를 repository에 vendor하지 않음
- [ ] metadata normalization
- [ ] quality status 수집
- [ ] provenance / catalog fingerprint 수집
- [ ] duplicate reference ID 처리
- [ ] unavailable fields를 UNKNOWN으로 처리
- [ ] index cache output을 project authority로 취급하지 않음
- [ ] no vector DB
- [ ] no embedding dependency
- [ ] tests with small fixture corpus
- [ ] commit

**PASS:** 작은 fixture와 실제 local corpus 모두에서 재현 가능한 index 생성.

## P4 — Reference Retrieval / Lock

- [ ] Design Intent → hard filters
- [ ] top candidate limit 8~12
- [ ] inspection candidate limit 3~5
- [ ] Primary 1개 필수
- [ ] Secondary max 2
- [ ] role ownership 필드
- [ ] TAKE / DO NOT TAKE / APPLIES TO / UNKNOWN 필수
- [ ] same-axis ownership conflict validator
- [ ] quality status 기록
- [ ] Legacy/Partial missing fact 추론 금지
- [ ] reference averaging 금지 fixture
- [ ] no-primary → STOP fixture
- [ ] conflicting owners → FAIL fixture
- [ ] tests
- [ ] commit

**PASS:** Reference Lock만 읽어도 각 reference의 책임이 명확함.

## P5 — JOEDESIGN Synthesis Adapter

- [ ] existing v0.2 invocation contract 정의
- [ ] DESIGN_INTENT 전달
- [ ] REFERENCE_LOCK 전달
- [ ] Product authority 전달
- [ ] existing DESIGN.md 전달
- [ ] project assets/current implementation pointer 전달
- [ ] `DESIGN_CONTRACT.md` template
- [ ] source attribution 필드
- [ ] Product invariant 보존 validator
- [ ] forbidden pattern 기록
- [ ] proof target 기록
- [ ] unknowns 보존
- [ ] approved source와 project proposal 분리
- [ ] tests
- [ ] commit

**PASS:** Design Contract가 Reference Lock을 대체/변조하지 않고 project-specific implementation decision으로 번역.

## P6 — Scope / Blast Radius Guard

- [ ] execution slice type 정의
- [ ] affected routes list
- [ ] affected surface families list
- [ ] shared selector impact check contract
- [ ] broad `.text-*` / `.bg-*` / `!important` override warning
- [ ] index/detail selector sharing 경고
- [ ] desktop-only geometry 재사용 경고
- [ ] new route family 영향 → STOP
- [ ] global CSS cross-family fixture
- [ ] rejected grammar reactivation fixture
- [ ] tests
- [ ] commit

**PASS:** 한 surface 수정이 다른 page family를 조용히 깨는 경로를 사전에 표면화.

## P7 — Impeccable Adapter

- [ ] Impeccable available/unavailable detection
- [ ] craft-only prompt contract
- [ ] Design Contract 전달
- [ ] forbidden authority changes 명시
- [ ] proposed change classification
- [ ] local craft change 허용
- [ ] material composition change → `CRAFT_SCOPE_VIOLATION`
- [ ] Product mutation → FAIL
- [ ] reference ownership mutation → FAIL
- [ ] tests
- [ ] commit

**PASS:** Impeccable이 polish는 가능하지만 art direction을 탈취하지 못함.

## P8 — State Matrix / Browser Evidence

- [ ] STATE_MATRIX template
- [ ] required/out-of-scope semantics
- [ ] exact viewport contract
- [ ] opening/below-fold/state 분리
- [ ] hover/focus/selection/dialog/filter/loading/error 지원
- [ ] browser evidence manifest
- [ ] screenshot path binding
- [ ] console/overflow/broken asset 기록
- [ ] interaction observation 기록
- [ ] Desktop only → Responsive UNVERIFIED fixture
- [ ] static screenshot only → Interaction UNVERIFIED fixture
- [ ] missing required row → PROOF_COMPLETE 차단
- [ ] tests
- [ ] commit

**PASS:** 에이전트가 실제로 본 state와 보지 않은 state가 기계적으로 분리됨.

## P9 — Independent Critic

- [ ] critic input bundle 생성
- [ ] implementer self-evaluation 제외
- [ ] critic role = diagnosis only
- [ ] PASS/FAIL/UNVERIFIED only
- [ ] no score
- [ ] no new design direction
- [ ] evidence binding 필수
- [ ] fresh context invocation path
- [ ] critic unavailable → `CRITIC_UNVERIFIED`
- [ ] FAIL → user-review 내부 PASS 차단
- [ ] tests
- [ ] commit

**PASS:** 동일 agent의 자기합리화가 최종 visual internal verdict를 단독 소유하지 못함.

## P10 — Repair Loop / User Gate / Handoff

- [ ] FAIL bounded repair contract
- [ ] max 2 local material correction
- [ ] third attempt → `MATERIAL_REWORK_REQUIRED`
- [ ] root DESIGN.md promotion은 user approval 이후만
- [ ] `ㄱㄱ` != visual acceptance fixture
- [ ] exact user approval record contract
- [ ] evidence manifest validation
- [ ] summary cannot exceed evidence scope validator
- [ ] final handoff states
- [ ] tests
- [ ] commit

**PASS:** 완료 문구가 실제 evidence 범위를 넘어갈 수 없음.

---

# 19. 필수 실패 Fixture

## F1 — Reference 없음

```text
Material redesign requested
Primary reference = none
```

Expected:

`REFERENCE_INSUFFICIENT`

구현 금지.

## F2 — Reference ownership 충돌

```text
Primary owns composition
Secondary owns composition
```

Expected:

`REFERENCE_LOCK_CONFLICT`

## F3 — Impeccable scope 침범

Craft pass가:

```text
typography polish
→ 전체 hero composition 변경
```

시도.

Expected:

`CRAFT_SCOPE_VIOLATION`

## F4 — Desktop만 확인

Desktop screenshot 존재.
Mobile 없음.

Expected:

```text
Desktop Visual = eligible
Responsive = UNVERIFIED
Overall Responsive PASS = BLOCKED
```

## F5 — Static PNG only

웹 interaction 작업인데 정적 PNG만 존재.

Expected:

`INTERACTION_UNVERIFIED`

## F6 — Missing state matrix row

required `selected` state 미관찰.

Expected:

`PROOF_COMPLETE = BLOCKED`

## F7 — Critic FAIL

Critic material FAIL.

Expected:

`VISUAL_INTERNAL_PASS = BLOCKED`

## F8 — Critic unavailable

Expected:

`CRITIC_UNVERIFIED`

사용자에게 proof를 보여줄 수는 있으나 Internal PASS 금지.

## F9 — 가짜 승인

사용자:

`ㄱㄱ`

Expected:

`USER ACCEPTANCE = PENDING`

## F10 — CSS blast radius

한 Utility surface 수정이 Narrative/Detail에도 적용.

Expected:

`SCOPE_EXPANSION_REQUIRED`

## F11 — rejected grammar 재사용

과거 rejected direction을 새 design contract가 primary grammar로 재사용.

Expected:

`AUTHORITY_CONFLICT`

## F12 — 기술 PASS를 시각 PASS로 승격

tests/build/console/overflow PASS지만 screenshot 없음.

Expected:

`VISUAL = UNVERIFIED`

---

# 20. Verification Checklist

모든 구현 단계 완료 전:

- [ ] `python -m unittest discover -s tests -v`
- [ ] JOEDESIGN 기존 test regression 0
- [ ] package quick validation PASS
- [ ] Python compile PASS
- [ ] test fixtures deterministic
- [ ] no OMD corpus copied into repo
- [ ] no new mandatory external runtime
- [ ] no JOEFLOW modification
- [ ] no existing JOEDESIGN v0.2 behavior regression
- [ ] docs/spec/skill behavior 일치
- [ ] status names 일관성
- [ ] no stale template references
- [ ] no duplicate active public skill name

---

# 21. Eval Plan

## Control

`JOEDESIGN v0.2`

## Candidate

`JOEDESIGN Design Harness v0.1`

## Runtime

동일:

```text
gpt-6-astra / xhigh
same repo
same baseline
same Product authority
same brief
same target runtime
```

## Eval Case A

BIO02 Portfolio Evidence.

이유:

- 기존 실패 이력 존재
- data/state/interaction 포함
- PPT/dashboard 수렴 위험
- desktop/mobile 모두 중요
- reference grounding 효과 확인 가능

## Eval Case B

성격이 다른 별도 surface.

추천:

- marketing/narrative web surface

또는

- utility/product UI surface

BIO에만 overfit하지 않는지 확인한다.

---

# 22. Eval Metrics

숫자 미감 점수보다 실패율을 본다.

기록:

- 첫 proof 사용자 승인 여부
- material rejection 수
- local correction 수
- generic AI/PPT/dashboard rejection 수
- component visual defect 수
- responsive defect 수
- state defect 수
- reference drift 수
- scope expansion 수
- 사용자가 먼저 발견한 결함 수
- false completion claim 수
- 총 tool/model calls
- 총 token/time cost

## Success Condition

Harness v0.1은 다음 중 하나만 좋아져도 성공이 아니다.

```text
검증 문서가 더 많아짐
PASS 수가 늘어남
agent가 더 자신 있게 보고함
```

성공은 실제로:

```text
visual rejection 감소
regression 감소
user-found defects 감소
reference drift 감소
false completion 감소
```

가 보여야 한다.

---

# 23. v0.1 Stop Conditions

다음이면 기능 확장을 중단한다.

- OMD retrieval이 실제 design failure를 줄이지 못함
- Reference Lock이 agent output에 실질적 차이를 만들지 못함
- Impeccable 추가가 방향 drift만 증가시킴
- Critic이 implementer와 동일한 self-validation만 반복
- Harness가 token/latency만 크게 늘리고 rejection이 감소하지 않음

이 경우 v0.2로 규칙을 더 추가하지 않는다.

원인을 분석하고 해당 모듈을 제거하거나 프로젝트를 닫는다.

---

# 24. 커밋 권장 단위

```text
docs: specify JOEDESIGN design harness v0.1
feat: add design harness contracts
feat: add OMD reference retrieval
feat: add reference lock validation
feat: connect JOEDESIGN synthesis
feat: add design blast-radius guard
feat: bound Impeccable craft pass
feat: add visual state evidence gate
feat: add independent visual critic
feat: add design harness closure gates
test: add design harness falsification suite
```

각 commit 전 해당 task test를 실행한다.

---

# 25. 최종 구현 완료 조건

다음이 모두 충족되어야 v0.1 implementation complete로 부른다.

- [ ] Public `joedesign-harness` skill discovery
- [ ] 기존 `joedesign` v0.2 package unchanged
- [ ] DESIGN_INTENT contract PASS
- [ ] OMD retrieval PASS
- [ ] Reference Lock conflict detection PASS
- [ ] Design Contract validation PASS
- [ ] Scope/blast-radius guard PASS
- [ ] Impeccable boundary PASS
- [ ] State Matrix gate PASS
- [ ] Browser Evidence gate PASS
- [ ] Critic PASS/FAIL/UNVERIFIED contract PASS
- [ ] User Acceptance gate PASS
- [ ] F1~F12 falsification cases PASS
- [ ] 기존 JOEDESIGN regression suite PASS
- [ ] eval package ready
- [ ] Control/Candidate 아직 미실행이면 production-ready 주장 금지

Implementation completion과 production validation을 분리한다.

```text
IMPLEMENTATION_COMPLETE
≠
OPERATIONALLY_VALIDATED
≠
PRODUCTION_READY
```

---

# 26. 구현 에이전트용 지시문

아래 지시를 그대로 사용한다.

---

## AGENT INSTRUCTION — JOEDESIGN Design Harness v0.1

너는 `JOEWRKS/JOEDESIGN` repository에서 **JOEDESIGN Design Harness v0.1**을 구현한다.

### 최우선 목표

AI에게 디자인 이론을 더 많이 주입하는 것이 아니다.

다음 pipeline을 강제해 **디자인 실패율을 줄이는 것**이 목표다.

```text
Product/JOEFLOW Intent
→ Oh My Design reference retrieval
→ Reference Lock
→ JOEDESIGN project synthesis
→ Actual interactive web implementation
→ Impeccable craft pass
→ Browser/state evidence
→ Independent critic
→ User acceptance
```

### 기존 authority

기존 `skills/joedesign/` v0.2는 검증된 dependency다.

**수정하지 마.**

Harness는 그 위의 orchestration/controller layer다.

### 구현 원칙

1. 새 public entrypoint: `joedesign-harness`
2. 기존 JOEDESIGN v0.2: unchanged.
3. Oh My Design: corpus로만 사용. fork/vendor 금지. v0.1 vector DB/embedding 금지.
4. Reference: Primary 1개 필수. Secondary 최대 2개. 각 reference는 bounded ownership을 갖는다. 동일 디자인 축 다중 owner 금지.
5. JOEDESIGN: Design Intent + Reference Lock + Product authority를 project-specific Design Contract로 번역한다.
6. Impeccable: craft-only. visual direction authority가 아니다.
7. 웹 디자인: static concept art만으로 완료 금지. 실제 component/state/responsive/browser proof 필요.
8. Critic: fresh-context visual diagnosis. 새 디자인을 만들지 않는다. PASS / FAIL / UNVERIFIED만 사용.
9. Browser: 실제 observed state만 PASS 가능.
10. User: exact visual approval 전까지 항상 `USER VISUAL ACCEPTANCE: PENDING`.

### 과확장 금지

v0.1에서 만들지 마:

- GUI
- cloud service
- vector DB
- embeddings
- OMD fork
- custom design model
- critic voting/ensemble
- automatic aesthetic score
- JOEFLOW rewrite
- JOENESS global integration
- existing JOEDESIGN rewrite

### 구현 방식

- TDD
- task 단위 commit
- 기존 repository pattern 우선
- 추가 dependency 최소화
- Python stdlib 우선
- existing tests 먼저 baseline 확인
- hidden failure 발견 시 scope를 넓혀 고치지 말고 보고

### Mandatory falsification

F1~F12를 전부 자동 fixture로 구현한다.

특히 반드시 증명할 것:

```text
No reference → implementation blocked
Reference role conflict → blocked
Desktop only → responsive UNVERIFIED
Static PNG only → interaction UNVERIFIED
Missing matrix row → proof incomplete
Critic FAIL → internal visual PASS blocked
"ㄱㄱ" → user acceptance remains pending
Cross-family CSS impact → scope expansion required
Technical PASS only → visual UNVERIFIED
```

### 완료 보고 금지 조건

다음 중 하나라도 미완료면:

`JOEDESIGN_DESIGN_HARNESS_V0_1_IMPLEMENTATION_NOT_READY`

로 보고한다.

- package discovery
- F1~F12
- existing JOEDESIGN regression
- state transition validation
- artifact validation
- exact test output

### 구현 완료 상태

모든 구현/테스트가 통과하면:

`JOEDESIGN_DESIGN_HARNESS_V0_1_IMPLEMENTATION_COMPLETE`

단, 이 상태는:

`OPERATIONALLY_VALIDATED` 또는 `PRODUCTION_READY`

를 의미하지 않는다.

그 다음 별도 Control vs Candidate 평가를 수행해야 한다.

### 최종 보고 형식

```text
TRACK:
JOEDESIGN Design Harness v0.1

STATUS:

Repository:
Branch:
Baseline HEAD:
Final HEAD:

Existing JOEDESIGN v0.2:
- unchanged:
- regression:

Harness:
- public skill:
- package validation:

Modules:
- Intent Adapter:
- OMD Retriever:
- Reference Lock:
- JOEDESIGN Synthesis:
- Blast Radius Guard:
- Impeccable Adapter:
- State Matrix:
- Browser Evidence:
- Critic:
- User Gate:

Falsification:
- F1:
- F2:
...
- F12:

Tests:
Compile:
Diff check:

Dependencies added:
Files changed:

Known limitations:

Operational validation:
PENDING

Next:
Prepare Control vs Candidate evaluation.

STOP.
```

---

# 27. PM Review Focus

구현 결과를 검토할 때 특히 다음을 의심한다.

1. **Harness가 그냥 긴 prompt wrapper가 된 것은 아닌가**
2. **OMD reference를 많이 넣는 방식으로 퇴행하지 않았는가**
3. **Reference Lock이 실제로 downstream decision을 제한하는가**
4. **Impeccable이 새 authority처럼 행동하지 않는가**
5. **Critic이 implementer의 자기평가를 복사하고 있지 않은가**
6. **Browser proof가 실제 target runtime인가**
7. **미검증 state를 PASS라고 쓰는 경로가 남아 있지 않은가**
8. **기존 JOEDESIGN v0.2가 조용히 수정되지 않았는가**
9. **BIO에만 맞춘 hard-code가 들어가지 않았는가**
10. **실패율 감소보다 ceremony 양만 늘어난 것은 아닌가**

---

# 28. 최종 원칙

이 Harness의 성공 기준은 규칙의 수가 아니다.

> **AI가 처음부터 더 근거 있는 디자인을 만들고, 작은 디자인 오류와 구조 오류가 덜 발생하며, 잘못된 디자인을 스스로 PASS시키지 않고, 실제로 확인한 범위를 넘어 완료라고 말하지 않는 것.**

이 효과가 실제 A/B 평가에서 보이지 않으면 Harness를 더 복잡하게 만들지 않는다.
