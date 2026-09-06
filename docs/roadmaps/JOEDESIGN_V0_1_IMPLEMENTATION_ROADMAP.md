# JOEDESIGN v0.1 Implementation Roadmap

**Status:** Active execution roadmap  
**Purpose:** 다음 세션/에이전트가 이전 대화를 잃어도 JOEDESIGN의 현재 상태, 남은 순서, 완료 조건을 즉시 복구할 수 있게 한다.  
**Operating model:** `docs/architecture/JOEDESIGN_OPERATING_MODEL_V1.md`  
**Current working branch:** `codex/joedesign-v0.1-implementation-bridge`  
**Roadmap baseline HEAD:** `f51a9f70b39d49bb023a3ffc080fe7a05227b9e8`

---

## 1. 목표

JOEDESIGN v0.1의 목표는 다음 다섯 층을 갖춘 **작고 독립적인 AI 디자인 코어**를 완성하고 동일 과제 경쟁으로 검증하는 것이다.

```text
1. Process / Authority Core
2. Craft Core
3. Reference Intelligence
4. Implementation Bridge
5. Competition Proof
```

완료 전까지 새로운 vendor runtime, giant rule DB, reference DB bundle, router, 별도 public skill을 추가하지 않는다.

---

## 2. 현재 상태 한눈 요약

| 영역 | 구현 | 검증 | 상태 |
|---|---:|---:|---|
| Process / Authority Core | 완료 | 완료 | CLOSED |
| Visual Hierarchy / Flow / Spatial Core | 완료 | 완료 | CLOSED |
| Typography & Scale Core | 완료 | 완료 | CLOSED |
| Reference Intelligence | 완료 후보 | 미완료 | VALIDATION NEXT |
| Implementation Bridge | 완료 후보 | 미완료 | HOLD AFTER REFERENCE |
| Color / Contrast Core | 미착수 | 미착수 | NEXT CRAFT |
| Imagery / Focal Ownership Core | 미착수 | 미착수 | PLANNED |
| Composition / Anti-template Core | 미착수 | 미착수 | PLANNED |
| Optical / Detail Polish | 미착수 | 미착수 | OPTIONAL MINIMUM |
| Pure Core Freeze | 미완료 | 미완료 | GATE |
| BIO 5-way Competition | 미실행 | 미실행 | FINAL VALIDATION |

현재 우선순위:

```text
Reference validation
→ Color / Contrast
→ Imagery / Focal Ownership
→ Composition / Anti-template
→ 최소 Optical Polish 판단
→ Implementation Bridge validation
→ Pure Core freeze
→ BIO competition
```

---

## 3. 완료된 기반

### A. Process / Authority Core — CLOSED

- [x] 단일 public entrypoint `JOEDESIGN`
- [x] Product Definition / JOEDESIGN / JOEFLOW / User 역할 분리
- [x] `UNDERSTAND → EXPLORE → PROVE → REFINE → VERIFY → ACCEPT/PERSIST`
- [x] 방향 미정 시 2–3 materially distinct alternatives
- [x] 승인 방향/local refinement에서 불필요한 fanout 금지
- [x] Product ambiguity bounded re-entry
- [x] `Technical PASS ≠ Product PASS ≠ Visual PASS ≠ User Acceptance`
- [x] Project root `DESIGN.md` lifecycle
- [x] 실제 target-medium proof 우선

### B. Hierarchy / Spatial Core — CLOSED

- [x] `Hierarchy before decoration`
- [x] Visual entry point / second / third destination / visual flow
- [x] Semantic Visual Block Tree
- [x] Spacing belongs to relationship/boundary
- [x] Structural hierarchy와 binding hierarchy 분리
- [x] JOE spatial roles `160 / 48 / 24 / 16 / 8 / 4`
- [x] 제한된 4px spatial vocabulary
- [x] Responsive hierarchy translation
- [x] Smoke C rendered evidence

### C. Typography & Scale Core — CLOSED

- [x] `Role before value`
- [x] Semantic type roles
- [x] Font size alone is not hierarchy
- [x] Restrained type scale
- [x] Family/weight restraint
- [x] Reading measure / line-height system
- [x] Product-priority focal scale
- [x] Responsive typography translation
- [x] Contract suite `32/32 PASS`
- [x] Astra semantic replay `14/14 PASS`
- [x] Smoke A/B/C/D PASS

Canonical typography readiness evidence is historical evidence; later skill-byte changes require fresh branch-level evidence before competition readiness.

---

## 4. Phase 1 — Reference Intelligence Validation

**Implementation status:** candidate implemented  
**Canonical spec:** `docs/specs/joedesign-reference-intelligence-core-v0.1.md`

### Required behavior

- [x] Material adoption에서만 provenance/evidence 확인
- [x] `KNOWN` / `UNKNOWN` 분리
- [x] Missing reference facts 발명 금지
- [x] `TAKE / DO NOT TAKE / WHY / APPLIES TO`
- [x] Evidence quality와 aesthetic authority 분리
- [x] 여러 reference의 scoped contribution 허용
- [x] 충돌 reference 자동 평균/다수결 금지
- [x] External corpus는 optional source
- [x] Reference DB / router / vendor dependency 금지

### Validation checklist

- [ ] Reference static contracts 8/8 PASS
- [ ] 전체 contract suite fresh PASS
- [ ] Fresh Astra semantic replay 14/14 PASS
- [ ] Smoke E: material reference adoption
- [ ] Smoke E에서 Product Truth 불변 확인
- [ ] Smoke E에서 unknown 미발명 확인
- [ ] Smoke E에서 conflicting references 분리 확인
- [ ] Smoke E에서 actual render observation 확인
- [ ] User acceptance 별도 유지 확인

### Gate

모두 통과해야:

`REFERENCE_INTELLIGENCE_CORE = CLOSED`

실패 시 expected answer를 runtime 결과에 맞추지 않는다. 원인을 수정한 뒤 fresh evidence를 만든다.

---

## 5. Phase 2 — Color / Contrast Core

**Status:** NOT STARTED  
**Priority:** 다음 Craft 축

### 설계 목표

- [ ] Semantic color roles 정의
- [ ] Functional color와 expressive color 분리
- [ ] Foreground / background contrast hierarchy
- [ ] Accent ownership: 한 화면에서 무엇이 색을 소유하는가
- [ ] Neutral system / surface hierarchy
- [ ] State colors와 Product semantics 보존
- [ ] Color만으로 hierarchy/state 전달하지 않기
- [ ] Accessibility contrast와 art direction 균형
- [ ] Project palette override가 JOE default보다 우선
- [ ] Responsive/different-background context에서 contrast 재검증

### 구현 방식

- [ ] Doctrine 먼저 작성/commit
- [ ] Failing contracts 먼저 추가
- [ ] 최소 `SKILL.md` behavior 추가
- [ ] 필요 시 `DESIGN.md` template 최소 확장
- [ ] Fresh static suite
- [ ] Fresh Astra replay
- [ ] Smoke G: color/contrast-specific rendered proof

### Gate

`COLOR_CONTRAST_CORE = CLOSED`

---

## 6. Phase 3 — Imagery / Focal Ownership Core

**Status:** NOT STARTED

### 설계 목표

- [ ] Image/artwork의 역할을 decoration / support / focal로 구분
- [ ] Product-priority focal ownership
- [ ] Text ↔ image dominance 관계
- [ ] Crop / focal point / framing
- [ ] Image scale과 negative space
- [ ] Reference imagery의 관계만 차용하고 asset/brand identity 복제 금지
- [ ] 반복적인 우측 이미지 패널/배경 장식 남발 방지
- [ ] Desktop/mobile에서 focal ownership 재구성
- [ ] Actual target render에서 crop/ownership 검증

### 구현/검증

- [ ] Doctrine
- [ ] Contracts RED → minimal runtime
- [ ] Fresh suite
- [ ] Fresh Astra replay
- [ ] Smoke H rendered proof

### Gate

`IMAGERY_FOCAL_CORE = CLOSED`

---

## 7. Phase 4 — Composition / Anti-template Core

**Status:** NOT STARTED

### 설계 목표

Generic AI/SaaS 구조를 자동 기본값으로 선택하는 경향을 억제하면서 프로젝트 목적에 맞는 구조적 다양성을 만든다.

- [ ] Composition은 Product priority와 narrative/task flow에서 시작
- [ ] Card는 의미 있는 containment일 때만 사용
- [ ] `hero + right image`, `3-card features`, pills, floating blobs 등 자동 문법 억제
- [ ] Intentional asymmetry 허용
- [ ] Repetition과 variation의 구조적 역할 구분
- [ ] 섹션마다 같은 loudness/shape 반복 금지
- [ ] Reference 관계를 generic template으로 평준화하지 않기
- [ ] Distinctiveness가 usability/Product Truth를 침범하지 않기
- [ ] Mobile은 desktop composition 축소가 아니라 재구성

### 구현/검증

- [ ] Doctrine
- [ ] Contracts RED → minimal runtime
- [ ] Fresh suite
- [ ] Fresh Astra replay
- [ ] Smoke I: generic-template defect → project-specific composition

### Gate

`COMPOSITION_ANTI_TEMPLATE_CORE = CLOSED`

---

## 8. Phase 5 — Optical / Detail Polish Decision

**Status:** OPTIONAL MINIMUM

이 단계는 독립 거대 코어로 확장하지 않는다. 앞 단계의 실제 경쟁 proof에서 필요성이 확인될 때만 최소화하여 추가한다.

검토 후보:

- [ ] Optical alignment
- [ ] Icon/text balance
- [ ] Border/elevation restraint
- [ ] Radius consistency
- [ ] Micro-spacing exception discipline
- [ ] Fine typography optical correction

### Gate

다음 중 하나로 명시한다.

- [ ] `OPTICAL_CORE = MINIMUM CLOSED`
- [ ] `OPTICAL_CORE = DEFERRED; no demonstrated need before competition`

---

## 9. Phase 6 — Implementation Bridge Validation

**Implementation status:** candidate implemented  
**Canonical spec:** `docs/specs/joedesign-implementation-bridge-v0.1.md`

### 현재 구현된 계약

- [x] Bridge는 `APPROVED DESIGN.md`의 derivative layer
- [x] Exact approved values와 rationale 분리
- [x] Existing project-native token/component role 우선
- [x] Unknown value 발명 금지
- [x] Google `design.md` structured-token compatibility는 optional
- [x] Custom JOEDESIGN sections 보존
- [x] Material token mapping diff 개념
- [x] `Token Mapping PASS ≠ Visual PASS`
- [x] Google CLI/package dependency 없음

### 아직 하지 않는 것

- [ ] 실제 parser 구현 — v0.1 competition 전 필수 아님
- [ ] standalone lint CLI — 필수 아님
- [ ] semantic diff engine — 필수 아님
- [ ] CSS/Tailwind/DTCG exporter — 필수 아님

이 항목들은 competition 또는 실제 project handoff에서 필요성이 증명된 뒤 v0.2 후보로 올린다.

### Validation checklist

- [ ] Bridge static contracts 8/8 PASS
- [ ] 전체 contract suite fresh PASS
- [ ] Fresh Astra semantic replay 14/14 PASS
- [ ] Smoke F: `APPROVED DESIGN.md → project-native token mapping → render`
- [ ] Existing token architecture 보존 확인
- [ ] Missing values unresolved 유지 확인
- [ ] Custom DESIGN.md sections 보존 확인
- [ ] Material mapping change diff evidence 확인
- [ ] Actual render observation 확인

### Gate

`IMPLEMENTATION_BRIDGE_V0_1 = CLOSED`

---

## 10. Phase 7 — Pure Core Freeze

모든 Craft/Reference/Bridge gate를 닫은 뒤 feature development를 중지한다.

- [ ] Public entrypoint = 1
- [ ] Competitor runtime dependency = 0
- [ ] Vendor payload = 0
- [ ] Reference DB bundle = 0
- [ ] Automatic router = 0
- [ ] BIO exposure during core building = 0
- [ ] 모든 canonical doctrine/operating model 상호 모순 없음
- [ ] 전체 contract suite fresh PASS
- [ ] Fresh Astra replay PASS
- [ ] Required rendered smokes PASS
- [ ] Skill/template SHA 기록
- [ ] Freeze commit 기록

Gate:

`JOEDESIGN_PURE_CORE_FROZEN = PASS`

---

## 11. Phase 8 — BIO 5-way Competition

Pure Core freeze 전에는 실행하지 않는다.

### Competitors

- [ ] Bare Astra x-high
- [ ] Astra x-high + JOEDESIGN Pure
- [ ] Astra x-high + Impeccable only
- [ ] Astra x-high + UI UX Pro Max only
- [ ] Figma Make

`awesome-design-md`와 oh-my-design은 별도 competitor로 추가하지 않는다. Reference-assistance A/B가 필요하면 competition 이후 별도 실험으로 수행한다.

### Round 1 target

- [ ] BIO Opening Hero desktop `1440×900`
- [ ] BIO Opening Hero mobile `390×844`
- [ ] First structural transition
- [ ] Motion/interaction concept
- [ ] Visual rationale
- [ ] Actual visible render/prototype
- [ ] Fresh isolated context per arm
- [ ] Anonymous A–E output

### Blind score

- [ ] First impression — 25
- [ ] BIO brand/science fit — 20
- [ ] Composition/hierarchy — 20
- [ ] Originality/anti-template — 15
- [ ] Typography/detail — 10
- [ ] Mobile — 10

### Round 2

- [ ] Top 2–3 select
- [ ] Same vertical slice implementation
- [ ] Quality + implementation fidelity 비교
- [ ] 승리 메커니즘 분해

---

## 12. Phase 9 — v0.2 Decision

경쟁 전에 competitor mechanism을 JOEDESIGN에 복사하지 않는다.

경쟁 후:

- [ ] 우승/패배 원인 분해
- [ ] Craft mechanism과 corpus advantage 분리
- [ ] JOEDESIGN에 필요한 메커니즘만 선택
- [ ] 필요 시 OmD/awesome reference-assisted A/B
- [ ] 필요 시 Google-compatible parser/lint/diff/export 검토
- [ ] v0.2 spec 작성

---

## 13. 항상 지켜야 할 금지선

- [ ] Product meaning을 시각 편의를 위해 변경하지 않는다.
- [ ] Visual PASS로 User Acceptance를 추론하지 않는다.
- [ ] Reference를 Project Authority로 자동 승격하지 않는다.
- [ ] Unknown source facts를 그럴듯하게 복원하지 않는다.
- [ ] JOE default taste가 APPROVED DESIGN.md를 덮지 않는다.
- [ ] 작은 수정에 전체 exploration/workflow를 강제하지 않는다.
- [ ] Google/OmD/Awesome/competitor runtime을 v0.1 dependency로 넣지 않는다.
- [ ] 기능 필요성이 증명되지 않은 DB/router/CLI를 선제 구축하지 않는다.
- [ ] 기존 failure evidence를 삭제하거나 expected result를 실패 결과에 맞춰 수정하지 않는다.
- [ ] 실제 render 관찰 없이 material Visual PASS를 선언하지 않는다.

---

## 14. Memory-loss Recovery Procedure

새 세션/새 에이전트는 구현 전에 아래 순서로 읽는다.

```text
1. AGENTS.md
2. docs/roadmaps/JOEDESIGN_V0_1_IMPLEMENTATION_ROADMAP.md
3. docs/architecture/JOEDESIGN_OPERATING_MODEL_V1.md
4. 현재 Phase의 canonical spec
5. 현재 branch HEAD / diff / latest review evidence
```

그 후 이 문서에서 **가장 위에 남아 있는 unchecked Phase gate**부터 이어간다.

체크박스만 보고 PASS를 추론하지 않는다. 완료 표시는 반드시 해당 branch의 fresh test/runtime/render evidence와 함께 갱신한다.

---

## 15. Immediate Next Action

현재 다음 작업은 하나다.

```text
Reference Intelligence fresh validation
```

Reference gate가 닫히기 전에는 Color Core 구현을 시작하지 않는다.  
Implementation Bridge는 이미 candidate가 존재하지만 Reference/Craft 흐름을 가로막지 않도록 검증만 후순위에 둔다.
