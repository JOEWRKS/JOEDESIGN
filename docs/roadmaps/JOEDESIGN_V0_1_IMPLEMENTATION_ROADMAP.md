# JOEDESIGN v0.1 Implementation Roadmap

**Status:** Active execution roadmap  
**Purpose:** 대화 기억이 없어져도 현재 완료 상태, 남은 순서, gate, 금지선을 즉시 복구한다.  
**Operating model:** `docs/architecture/JOEDESIGN_OPERATING_MODEL_V1.md`  
**Current working branch:** `codex/joedesign-v0.1-color-contrast-core`  
**Phase baseline:** Reference Intelligence CLOSED at `1e66a6028399277bb9c8d575fb39ce579022d868`

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
| Color / Contrast Core | doctrine/plan 작성 | 미완료 | IN PROGRESS |
| Imagery / Focal Ownership Core | 미착수 | 미착수 | NEXT AFTER COLOR |
| Composition / Anti-template Core | 미착수 | 미착수 | PLANNED |
| Optical / Detail Polish | 미착수 | 미착수 | OPTIONAL MINIMUM |
| Implementation Bridge | candidate 별도 보존 | 미완료 | HOLD |
| Pure Core Freeze | 미완료 | 미완료 | GATE |
| BIO 5-way Competition | 미실행 | 미실행 | FINAL VALIDATION |

현재 순서:

```text
Color / Contrast
→ Imagery / Focal Ownership
→ Composition / Anti-template
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
- [x] 제한된 4px spatial vocabulary
- [x] responsive hierarchy translation
- [x] rendered Smoke C

### Typography & Scale Core

- [x] `Role before value`
- [x] semantic type roles
- [x] font size alone is not hierarchy
- [x] restrained type scale
- [x] family/weight restraint
- [x] reading measure / line-height system
- [x] Product-priority focal scale
- [x] responsive typography translation
- [x] static/semantic/rendered validation 완료

### Reference Intelligence

- [x] material adoption에서만 provenance/evidence discipline
- [x] `KNOWN / UNKNOWN`
- [x] missing source facts 발명 금지
- [x] `TAKE / DO NOT TAKE / WHY / APPLIES TO`
- [x] evidence quality ≠ aesthetic authority
- [x] multi-reference scoped contribution
- [x] conflict 자동 평균/다수결 금지
- [x] external corpus optional
- [x] DB/router/vendor dependency 없음
- [x] static contracts `40/40 PASS`
- [x] Astra semantic replay `14/14 PASS`
- [x] Smoke E PASS
- [x] Program Lead: `REFERENCE_INTELLIGENCE_CORE = CLOSED`

---

## 4. Phase 2 — Color / Contrast Core

**Status:** IN PROGRESS  
**Canonical doctrine:** `docs/specs/joedesign-color-contrast-core-v0.1.md`  
**Implementation plan:** `docs/superpowers/plans/2026-09-06-joedesign-color-contrast-core-v0.1.md`

### Required behavior

- [x] Doctrine: role before color value
- [x] Doctrine: semantic color roles
- [x] Doctrine: contrast hierarchy
- [x] Doctrine: accent ownership
- [x] Doctrine: neutral/surface-layer hierarchy
- [x] Doctrine: state color preserves Product semantics
- [x] Doctrine: color-only required cue 금지
- [x] Doctrine: WCAG 2.2 AA minimum gate where applicable
- [x] Doctrine: accessibility gate ≠ aesthetic preset
- [x] Doctrine: contextual foreground/background verification
- [x] Doctrine: responsive/theme roles preserved, values may change
- [x] Doctrine: project palette overrides JOE defaults

### Codex implementation checklist

- [ ] Color static contracts 8개 test-first 작성
- [ ] RED evidence 보존
- [ ] 최소 `SKILL.md` Color / Contrast behavior 추가
- [ ] `DESIGN.md` Color / Surface 하위 구조 최소 확장
- [ ] Color contracts `8/8 PASS`
- [ ] 전체 suite `48/48 PASS`
- [ ] fresh Astra semantic replay `14/14 PASS`
- [ ] Smoke G neutral fixture
- [ ] Smoke G desktop `1440×1000` actual observation
- [ ] Smoke G mobile `390×844` actual observation
- [ ] role map / accent owner / surface roles 검증
- [ ] applicable contrast ratios 검증
- [ ] state semantics + non-color cue 검증
- [ ] Product Truth invariant
- [ ] User Acceptance 별도 유지

### Gate

모두 통과하고 Program Lead가 승인해야:

```text
COLOR_CONTRAST_CORE = CLOSED
```

---

## 5. Phase 3 — Imagery / Focal Ownership Core

**Status:** NOT STARTED

- [ ] decoration / support / focal 역할 분리
- [ ] Product-priority focal ownership
- [ ] text ↔ image dominance
- [ ] crop / focal point / framing
- [ ] image scale / negative space
- [ ] reference imagery 관계만 차용
- [ ] 우측 이미지 패널/배경 장식 자동 문법 억제
- [ ] responsive focal recomposition
- [ ] actual render verification
- [ ] doctrine → RED contracts → minimal runtime → Smoke H

Gate: `IMAGERY_FOCAL_CORE = CLOSED`

---

## 6. Phase 4 — Composition / Anti-template Core

**Status:** NOT STARTED

- [ ] Product priority / narrative-task flow에서 composition 시작
- [ ] card는 의미 있는 containment일 때만 사용
- [ ] `hero + right image`, `3-card features`, pills, floating blobs 자동 문법 억제
- [ ] intentional asymmetry 허용
- [ ] repetition / variation 역할 구분
- [ ] 모든 section의 동일 loudness/shape 반복 금지
- [ ] reference를 generic template 평균으로 만들지 않기
- [ ] distinctiveness가 Product Truth/usability 침범 금지
- [ ] mobile composition 재구성
- [ ] doctrine → RED contracts → minimal runtime → Smoke I

Gate: `COMPOSITION_ANTI_TEMPLATE_CORE = CLOSED`

---

## 7. Phase 5 — Optical / Detail Polish Decision

독립 거대 코어로 선제 확장하지 않는다. 경쟁 전 실제 proof에서 필요성이 증명될 때만 최소화한다.

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

## 8. Phase 6 — Implementation Bridge Validation

Implementation Bridge candidate는 별도 branch에 보존되어 있다. Craft Core를 완료하기 전 더 확장하지 않는다.

**Separate branch:** `codex/joedesign-v0.1-implementation-bridge`

현재 candidate 범위:

- [x] APPROVED `DESIGN.md` derivative mapping
- [x] existing project-native token/component role 우선
- [x] unknown value 발명 금지
- [x] Google `design.md` compatibility optional
- [x] custom JOEDESIGN sections 보존
- [x] Token Mapping PASS ≠ Visual PASS

Competition 전 필수 아님:

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

## 9. Pure Core Freeze

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

## 10. BIO 5-way Competition

Pure Core freeze 전에는 실행하지 않는다.

Competitors:

- [ ] Bare Astra x-high
- [ ] Astra x-high + JOEDESIGN Pure
- [ ] Astra x-high + Impeccable only
- [ ] Astra x-high + UI UX Pro Max only
- [ ] Figma Make

Round 1:

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

## 11. v0.2 Decision

경쟁 전에 competitor mechanism을 JOEDESIGN에 복사하지 않는다.

경쟁 후에만:

- [ ] 승리/패배 메커니즘 분해
- [ ] Craft advantage와 corpus advantage 분리
- [ ] 필요한 메커니즘만 선택
- [ ] 필요 시 OmD/awesome reference-assisted A/B
- [ ] 필요 시 Google-compatible parser/lint/diff/export
- [ ] v0.2 spec

---

## 12. 항상 지켜야 할 금지선

- [ ] Product meaning을 시각 편의를 위해 변경하지 않는다.
- [ ] Visual PASS로 User Acceptance를 추론하지 않는다.
- [ ] Reference를 Project Authority로 자동 승격하지 않는다.
- [ ] Unknown source facts를 그럴듯하게 복원하지 않는다.
- [ ] JOE default taste가 APPROVED DESIGN.md를 덮지 않는다.
- [ ] 작은 수정에 전체 exploration/workflow를 강제하지 않는다.
- [ ] Google/OmD/Awesome/competitor runtime을 v0.1 dependency로 넣지 않는다.
- [ ] 필요성이 증명되지 않은 DB/router/CLI를 선제 구축하지 않는다.
- [ ] failure evidence를 삭제하거나 expected result를 실패에 맞춰 수정하지 않는다.
- [ ] actual render 없이 material Visual PASS를 선언하지 않는다.

---

## 13. Memory-loss Recovery Procedure

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

## 14. Immediate Next Action

현재 다음 작업은 하나다.

```text
Color / Contrast Core implementation + validation
```

Codex는 `docs/handoffs/JOEDESIGN_COLOR_CONTRAST_CORE_V1.md`를 최우선 실행 지시로 사용한다.
