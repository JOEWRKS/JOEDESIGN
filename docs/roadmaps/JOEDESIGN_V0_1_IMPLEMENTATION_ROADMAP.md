# JOEDESIGN v0.1 Implementation Roadmap

**Status:** Active execution roadmap  
**Purpose:** 대화 기억이 없어져도 현재 완료 상태, 남은 순서, gate, 금지선을 즉시 복구한다.  
**Operating model:** `docs/architecture/JOEDESIGN_OPERATING_MODEL_V1.md`  
**Current working branch:** `codex/joedesign-v0.1-composition-anti-template-core`  
**Current phase baseline:** Imagery / Focal Ownership Core CLOSED at `ad22a9a761eb89ec03ace3fd94625f6a6db6927e`

---

## 1. 최종 목표

JOEDESIGN v0.1은 다음 다섯 층을 가진 작고 독립적인 AI 디자인 코어를 완성하고 동일 과제 경쟁으로 검증한다.

```text
1. Process / Authority Core
2. Craft Core
3. Reference Intelligence
4. Implementation Bridge
5. Competition Proof
```

경쟁 전에는 competitor methodology를 흡수하지 않는다. Vendor runtime, giant rule DB, reference DB bundle, automatic router, 별도 public skill을 추가하지 않는다.

---

## 2. 현재 상태

| 영역 | 구현 | 검증 | 상태 |
|---|---:|---:|---|
| Process / Authority Core | 완료 | 완료 | CLOSED |
| Visual Hierarchy / Flow / Spatial Core | 완료 | 완료 | CLOSED |
| Typography & Scale Core | 완료 | 완료 | CLOSED |
| Reference Intelligence | 완료 | 완료 | CLOSED |
| Color / Contrast Core | 완료 | 완료 | CLOSED |
| Imagery / Focal Ownership Core | 완료 | 완료 | CLOSED |
| Composition / Anti-template Core | doctrine/plan 작성 | 미완료 | IN PROGRESS |
| Optical / Detail Polish | 미착수 | 미착수 | OPTIONAL MINIMUM |
| Implementation Bridge | candidate 별도 보존 | 미완료 | HOLD |
| Pure Core Freeze | 미완료 | 미완료 | GATE |
| BIO 5-way Competition | 미실행 | 미실행 | FINAL VALIDATION |

현재 순서:

```text
Composition / Anti-template
→ Optical 최소 필요성 판단
→ Implementation Bridge validation
→ Pure Core freeze
→ BIO competition
```

---

## 3. CLOSED 영역

### Process / Authority Core

- [x] public entrypoint = `JOEDESIGN` 하나
- [x] Product Definition / JOEDESIGN / JOEFLOW / User 역할 분리
- [x] `UNDERSTAND → EXPLORE → PROVE → REFINE → VERIFY → ACCEPT/PERSIST`
- [x] material direction 미정 시 2–3 materially distinct alternatives
- [x] 승인 방향/local refinement에서 불필요한 fanout 금지
- [x] Product ambiguity bounded re-entry
- [x] `Technical PASS ≠ Product PASS ≠ Visual PASS ≠ User Acceptance`
- [x] Project root `DESIGN.md` lifecycle
- [x] actual target-medium proof 우선

### Hierarchy / Spatial Core

- [x] `Hierarchy before decoration`
- [x] visual entry point / second / third destination / visual flow
- [x] Semantic Visual Block Tree
- [x] spacing belongs to relationship/boundary
- [x] structural hierarchy / binding hierarchy 분리
- [x] JOE spatial roles `160 / 48 / 24 / 16 / 8 / 4`
- [x] responsive hierarchy translation
- [x] rendered Smoke C

### Typography & Scale Core

- [x] role before value
- [x] semantic type roles
- [x] font size alone is not hierarchy
- [x] restrained type scale / family / weight / measure / line-height
- [x] responsive type translation
- [x] static + semantic + rendered validation

### Reference Intelligence

- [x] material adoption discipline
- [x] `KNOWN / UNKNOWN`
- [x] `TAKE / DO NOT TAKE / WHY / APPLIES TO`
- [x] evidence quality ≠ aesthetic authority
- [x] multi-reference conflict stays explicit
- [x] external corpus optional; DB/router/vendor dependency 없음
- [x] static `40/40 PASS`
- [x] Astra semantic `14/14 PASS`
- [x] Smoke E PASS
- [x] Program Lead: `REFERENCE_INTELLIGENCE_CORE = CLOSED`

### Color / Contrast Core

- [x] role before color value
- [x] semantic color roles / contrast hierarchy / accent ownership
- [x] neutral surface hierarchy
- [x] state semantics + non-color cues
- [x] WCAG AA minimum gate where applicable
- [x] contextual foreground/background observation
- [x] responsive/theme role preservation
- [x] static `48/48 PASS`
- [x] fresh Astra semantic `14/14 PASS`
- [x] Smoke G PASS
- [x] Program Lead: `COLOR_CONTRAST_CORE = CLOSED`

Canonical Color evidence HEAD: `7417ef037062f27272c3d3527713475b7d97c6f3`.

### Imagery / Focal Ownership Core

- [x] role before asset treatment
- [x] `FOCAL / SUPPORT / DECORATIVE`
- [x] informative imagery preserves Product meaning
- [x] intentional focal ownership / sequence
- [x] deliberate text-image dominance
- [x] focal region / crop intent
- [x] scale / negative space express image priority
- [x] reference imagery relationship ≠ copied asset
- [x] responsive recrop/reposition/recomposition
- [x] actual render required for crop/focal PASS
- [x] static `56/56 PASS`
- [x] Imagery contracts `8/8 PASS`
- [x] fresh Astra semantic `14/14 PASS`
- [x] Smoke H H1–H9 PASS — desktop `1440×1000`, mobile viewport `390×844`
- [x] Product / APPROVED DESIGN invariant
- [x] User Acceptance remains separate
- [x] Program Lead: `IMAGERY_FOCAL_CORE = CLOSED`

Canonical Imagery evidence HEAD: `ad22a9a761eb89ec03ace3fd94625f6a6db6927e`.

---

## 4. Phase 4 — Composition / Anti-template Core

**Status:** IN PROGRESS  
**Canonical doctrine:** `docs/specs/joedesign-composition-anti-template-core-v0.1.md`  
**Implementation plan:** `docs/superpowers/plans/2026-09-06-joedesign-composition-anti-template-core-v0.1.md`  
**Execution handoff:** `docs/handoffs/JOEDESIGN_COMPOSITION_ANTI_TEMPLATE_CORE_V1.md`

### Required behavior

- [x] Doctrine: structure before pattern
- [x] Doctrine: Product priority + task/narrative flow precede layout recipe
- [x] Doctrine: semantic containment before cards/panels
- [x] Doctrine: familiar AI/SaaS motifs are challenge triggers, not blanket bans
- [x] Doctrine: repetition expresses equivalence
- [x] Doctrine: variation expresses meaningful role/priority change
- [x] Doctrine: intentional asymmetry allowed when hierarchy remains clear
- [x] Doctrine: specificity over novelty
- [x] Doctrine: Product Truth/usability/accessibility remain boundaries
- [x] Doctrine: references contribute relationships, not complete page grammar
- [x] Doctrine: mobile recomposes rather than shrinking desktop coordinates
- [x] Doctrine: actual target render required for material composition PASS

### Codex implementation checklist

- [ ] isolated worktree / baseline `56/56`
- [ ] Composition contracts 8개 test-first 작성
- [ ] RED evidence 보존
- [ ] 최소 `SKILL.md` composition behavior 추가
- [ ] `DESIGN.md` Composition block 최소 확장
- [ ] Composition contracts `8/8 PASS`
- [ ] fresh Astra semantic replay `14/14 PASS`
- [ ] 전체 suite `64/64 PASS`
- [ ] Smoke I neutral fixture
- [ ] pre-edit structural map
- [ ] desktop `1440×1000` actual before/after observation
- [ ] mobile viewport `390×844` actual before/after observation
- [ ] Product first/second/third destinations 보존
- [ ] semantic containment / card justification 확인
- [ ] generic motif 자동 기본값 억제 확인
- [ ] repetition / variation structural meaning 확인
- [ ] mobile recomposition 확인
- [ ] Product / APPROVED DESIGN invariant
- [ ] User Acceptance separate
- [ ] final `64/64 PASS`

### Required execution order

```text
baseline 56/56
→ RED
→ minimal implementation
→ Composition 8/8
→ fresh semantic 14/14
→ full 64/64
→ Smoke I
→ final 64/64
```

If Smoke I changes shipped `skills/joedesign/**` bytes:

```text
fresh semantic again
→ full 64/64 again
→ rerun affected Smoke I evidence
```

### Gate

Program Lead approval after all evidence:

```text
COMPOSITION_ANTI_TEMPLATE_CORE = CLOSED
```

---

## 5. Phase 5 — Optical / Detail Polish Decision

**Status:** OPTIONAL MINIMUM

독립 거대 코어로 선제 확장하지 않는다. Composition까지의 actual proof와 경쟁 준비 상태에서 명확한 반복 결함이 확인될 때만 최소화한다.

검토 후보:

- [ ] optical alignment
- [ ] icon/text balance
- [ ] border/elevation restraint
- [ ] radius consistency
- [ ] micro-spacing exception discipline
- [ ] fine typography optical correction

Gate는 둘 중 하나:

```text
OPTICAL_CORE = MINIMUM CLOSED
```

또는

```text
OPTICAL_CORE = DEFERRED; no demonstrated need before competition
```

---

## 6. Phase 6 — Implementation Bridge Validation

Implementation Bridge candidate는 별도 branch에 보존되어 있다. Craft Core를 완료하기 전 더 확장하지 않는다.

**Separate branch:** `codex/joedesign-v0.1-implementation-bridge`

현재 candidate 범위:

- [x] APPROVED `DESIGN.md` derivative mapping
- [x] existing project-native token/component role 우선
- [x] unknown value 발명 금지
- [x] Google `design.md` compatibility optional
- [x] custom JOEDESIGN sections 보존
- [x] Token Mapping PASS ≠ Visual PASS

Competition 전 필수 구현 아님:

- [ ] parser
- [ ] standalone lint CLI
- [ ] semantic diff engine
- [ ] CSS/Tailwind/DTCG exporter

Validation gate:

- [ ] Bridge static contracts 8/8
- [ ] full suite fresh PASS
- [ ] fresh Astra replay
- [ ] Smoke F actual mapping/render proof

Gate: `IMPLEMENTATION_BRIDGE_V0_1 = CLOSED`

---

## 7. Pure Core Freeze

- [ ] public entrypoint = 1
- [ ] competitor runtime dependency = 0
- [ ] vendor payload = 0
- [ ] reference DB bundle = 0
- [ ] automatic router = 0
- [ ] BIO exposure during core building = 0
- [ ] canonical doctrine/operating model 상호 모순 없음
- [ ] current full contract suite PASS
- [ ] current Astra replay PASS
- [ ] required rendered smokes PASS
- [ ] skill/template SHA 기록
- [ ] freeze commit 기록

Gate: `JOEDESIGN_PURE_CORE_FROZEN = PASS`

---

## 8. BIO 5-way Competition

Pure Core freeze 전에는 실행하지 않는다.

Competitors:

- [ ] Bare Astra x-high
- [ ] Astra x-high + JOEDESIGN Pure
- [ ] Astra x-high + Impeccable only
- [ ] Astra x-high + UI UX Pro Max only
- [ ] Figma Make

Round 1 target:

- [ ] BIO Opening Hero desktop `1440×900`
- [ ] mobile `390×844`
- [ ] first structural transition
- [ ] motion/interaction concept
- [ ] visual rationale
- [ ] actual visible render/prototype
- [ ] fresh isolated context per arm
- [ ] anonymous A–E

Blind score:

```text
First impression 25
BIO brand/science fit 20
Composition/hierarchy 20
Originality/anti-template 15
Typography/detail 10
Mobile 10
```

`awesome-design-md`와 oh-my-design은 competitor로 추가하지 않는다. 필요하면 competition 이후 reference-assisted A/B로 분리한다.

---

## 9. v0.2 Decision

경쟁 전에 competitor mechanism을 JOEDESIGN에 복사하지 않는다.

경쟁 후에만:

- [ ] 승리/패배 메커니즘 분해
- [ ] Craft advantage와 corpus advantage 분리
- [ ] 필요한 메커니즘만 선택
- [ ] 필요 시 OmD/awesome reference-assisted A/B
- [ ] 필요 시 Google-compatible parser/lint/diff/export
- [ ] v0.2 spec

---

## 10. 항상 지켜야 할 금지선

- [ ] Product meaning을 시각 편의를 위해 변경하지 않는다.
- [ ] Visual PASS로 User Acceptance를 추론하지 않는다.
- [ ] Reference를 Project Authority로 자동 승격하지 않는다.
- [ ] Unknown source facts를 그럴듯하게 복원하지 않는다.
- [ ] JOE default taste가 APPROVED DESIGN.md를 덮지 않는다.
- [ ] 작은 수정에 전체 exploration/workflow를 강제하지 않는다.
- [ ] common pattern 자체를 blanket-ban하지 않는다.
- [ ] anti-template을 novelty score로 바꾸지 않는다.
- [ ] Google/OmD/Awesome/competitor runtime을 v0.1 dependency로 넣지 않는다.
- [ ] 필요성이 증명되지 않은 DB/router/CLI/asset/template system을 선제 구축하지 않는다.
- [ ] failure evidence를 삭제하거나 expected result를 실패에 맞춰 수정하지 않는다.
- [ ] actual render 없이 material Visual PASS를 선언하지 않는다.

---

## 11. Memory-loss Recovery Procedure

새 세션/새 에이전트는 구현 전에 다음 순서로 읽는다.

```text
1. AGENTS.md
2. docs/roadmaps/JOEDESIGN_V0_1_IMPLEMENTATION_ROADMAP.md
3. docs/architecture/JOEDESIGN_OPERATING_MODEL_V1.md
4. 현재 Phase canonical doctrine
5. 현재 Phase implementation plan / handoff
6. branch HEAD / diff / latest review evidence
```

그 후 이 문서에서 가장 위에 남은 미완료 Phase gate부터 이어간다.

체크박스만으로 PASS를 추론하지 않는다. 완료 표시는 fresh test/runtime/render evidence와 Program Lead 판정으로 갱신한다.

---

## 12. Immediate Next Action

현재 다음 작업은 하나다.

```text
Composition / Anti-template Core implementation + validation
```

Codex는 `docs/handoffs/JOEDESIGN_COMPOSITION_ANTI_TEMPLATE_CORE_V1.md`를 최우선 실행 지시로 사용한다.
