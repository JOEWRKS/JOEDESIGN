# JOEDESIGN Reference Intelligence Validation Handoff v1

**Status:** EXECUTION HANDOFF  
**Repository:** `JOEWRKS/JOEDESIGN`  
**Branch:** `codex/joedesign-v0.1-reference-intelligence-validation`  
**Starting HEAD:** `fb8c843629416c3f706c8d9cd72eb9c1f60889d0`  
**Purpose:** Reference Intelligence Core를 독립 검증하고 `REFERENCE_INTELLIGENCE_CORE = CLOSED` 여부를 판정한다.

## 1. Authority

먼저 읽는다.

1. `docs/architecture/JOEDESIGN_OPERATING_MODEL_V1.md`
2. `docs/specs/joedesign-reference-intelligence-core-v0.1.md`
3. `docs/specs/joedesign-v0.1.md`
4. `docs/specs/joedesign-craft-core-v0.1.md`
5. `docs/specs/joedesign-typography-scale-core-v0.1.md`
6. `AGENTS.md`

Implementation Bridge는 이 검증 범위가 아니다. 이 branch에는 Bridge runtime 변경을 가져오지 않는다.

## 2. Scope

이번 작업은 **validation only**다.

금지:

- 새 Reference 기능 추가
- doctrine 확장
- expected answer를 runtime 결과에 맞춰 수정
- BIO 사용
- oh-my-design / awesome-design-md corpus bundle
- crawler / vector DB / router / vendor dependency 추가
- `skills/joedesign/**` 수정
- main merge
- 개인 설치 변경

실패가 발생하면 원인을 기록하고 `READY`를 선언하지 않는다.

## 3. Static contracts

실행:

```bash
node --test \
  tests/joedesign-contract.tests.mjs \
  tests/joedesign-craft-core.tests.mjs \
  tests/joedesign-typography-scale-core.tests.mjs \
  tests/joedesign-reference-intelligence-core.tests.mjs
```

기대:

```text
40 tests
40 PASS
0 FAIL
```

구성:

- Process / Authority: 16
- Spatial Craft: 8
- Typography & Scale: 8
- Reference Intelligence: 8

실제 개수와 결과를 증거에 기록한다. 기대와 다르면 그대로 FAIL 처리한다.

## 4. Fresh Astra semantic replay

현재 shipped `skills/joedesign/**` bytes에 대해 fresh replay를 실행한다.

Runtime:

```text
gpt-6-astra
reasoning: xhigh
```

기존 `fixtures/contract-cases/decisions.json` 14개 scenario를 그대로 사용한다.

필수:

```text
14 / 14 PASS
```

`observed.json`에는 최소 다음 provenance를 갱신한다.

- source implementation commit
- complete shipped-skill SHA-256
- cases SHA-256
- runtime model / effort / thread
- rollout SHA-256
- 14 responses

이전 Typography/Case14 evidence는 history로 보존한다.

## 5. Smoke E — Material Reference Adoption

BIO가 아닌 neutral fixture를 새로 만든다.

### 5.1 Product Truth

가상의 `Research Briefing Portal` 한 화면을 사용한다.

고정 Product Truth:

- 한 개의 primary briefing title
- 한 개의 required primary action
- 세 개의 research summary records
- source / date metadata는 각 record에 필수
- desktop / mobile에서 동일 정보와 action 유지
- record 의미와 순서는 바꾸지 않음

### 5.2 Existing Project Visual Authority

fixture `DESIGN.md`에는 다음만 APPROVED로 둔다.

```text
- calm editorial hierarchy
- one clear primary focal point
- restrained surfaces
- dense dashboard/card-wall composition 금지
```

정확한 font family, mobile spacing, motion timing은 정의하지 않는다.

### 5.3 Reference A — strong evidence

제공된 reference brief에는 다음만 명시한다.

KNOWN:

- editorial asymmetry
- large headline relative to body
- generous image/text negative space
- low-chrome surface treatment

UNKNOWN:

- exact mobile spacing
- exact font family
- exact motion timing

TAKE 후보:

- headline/body dominance relationship
- low-chrome editorial grouping

DO NOT TAKE:

- source brand identity
- exact copy
- unsupported token values

### 5.4 Reference B — supported evidence, material conflict

KNOWN:

- dense modular card grid
- compact metadata grouping
- repeated boxed containers

UNKNOWN:

- responsive order
- exact spacing tokens

Reference B의 `dense modular card grid`는 APPROVED Project DESIGN.md와 material conflict다.

단, `compact metadata grouping`은 record 내부의 bounded relationship으로 별도 채택 가능하다.

### 5.5 Required JOEDESIGN behavior

Smoke E에서 반드시 확인한다.

1. `SOURCE / EVIDENCE QUALITY / KNOWN / UNKNOWN / TAKE / DO NOT TAKE / WHY / APPLIES TO`를 material adoption 범위에서만 사용한다.
2. Reference A의 unknown font/mobile/motion 값을 source truth처럼 발명하지 않는다.
3. Reference A의 editorial hierarchy는 현재 프로젝트에 번역할 수 있다.
4. Reference B의 dense card-grid는 승인 authority와 충돌한다고 명시하고 전체 composition으로 채택하지 않는다.
5. Reference B의 compact metadata grouping은 충돌하지 않는 bounded relationship으로만 채택 가능하다.
6. 두 reference를 평균내어 중간 형태의 generic card/editorial hybrid를 자동 생성하지 않는다.
7. Product Truth와 record content/order/action을 바꾸지 않는다.
8. 필요한 missing mobile/layout 값은 `project-specific JOEDESIGN decision`으로 명시하며 reference fact로 위장하지 않는다.
9. desktop과 mobile 실제 target render를 관찰한다.
10. Visual PASS와 User Acceptance를 분리한다.

## 6. Smoke E evidence

경로:

`fixtures/contract-cases/evidence/astra-smoke-v1/smoke-e/`

최소 산출물:

```text
PRODUCT.md
DESIGN.md
reference-a.md
reference-b.md
before-desktop.png
after-desktop.png
before-mobile.png
after-mobile.png
reference-adoption-manifest.json
```

`reference-adoption-manifest.json` 최소 필드:

- sourceImplementation
- target viewports
- Product Truth invariants
- Project DESIGN.md authority
- Reference A: evidence / known / unknown / take / doNotTake / appliesTo
- Reference B: evidence / known / unknown / conflict / bounded take / doNotTake / appliesTo
- project-specific decisions introduced because source facts were unknown
- changed files
- before/after observations
- actual rendered observations
- user acceptance boundary

## 7. Smoke E PASS conditions

모두 충족해야 PASS:

- Product Truth invariant
- APPROVED DESIGN.md preserved
- unknown reference facts remain unknown
- no copied brand identity or unsupported exact values
- conflicting references not silently blended
- bounded compatible relationship can be adopted independently
- actual desktop render observed
- actual mobile render observed
- material visual claims use expected → observed → verdict
- user acceptance not inferred

## 8. Final gate

최종 재실행:

```bash
node --test \
  tests/joedesign-contract.tests.mjs \
  tests/joedesign-craft-core.tests.mjs \
  tests/joedesign-typography-scale-core.tests.mjs \
  tests/joedesign-reference-intelligence-core.tests.mjs
```

READY 조건:

```text
Static contracts: 40/40 PASS
Semantic replay: 14/14 PASS
Smoke E: PASS
Public entrypoint: 1
Competitor/runtime dependency: 0
BIO exposure: 0
skills/joedesign/** changed during validation: NO
```

모두 충족 시에만:

`JOEDESIGN_REFERENCE_INTELLIGENCE_CORE_READY_FOR_PROGRAM_REVIEW`

Program Lead 검토 후에만 roadmap의 Phase 1을 `CLOSED`로 갱신한다.

## 9. Report format

```text
JOEDESIGN_REFERENCE_INTELLIGENCE_CORE_READY_FOR_PROGRAM_REVIEW

Repository:
Branch:
HEAD:
Tree:

Static contracts:
Semantic replay:
Runtime:
Thread:

Smoke E:
- Product Truth invariant:
- unknown preservation:
- conflict handling:
- bounded adoption:
- desktop observation:
- mobile observation:
- user acceptance boundary:

Skill SHA-256:
DESIGN template SHA-256:

Public entrypoint count:
Competitor dependency count:
BIO exposure count:

Known failures:
Unverified:
```
