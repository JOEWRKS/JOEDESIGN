# JOEDESIGN 2.0.2 — ATELIER 실사용 마찰: 색·모션 관측, report-check R3·R5, 출처 관측 범위, 전문 스킬, Playwright 없는 수집기, 규칙 행 병합 (2026-11-26)

출처: ATELIER(쇼핑몰) 실사용 중 기록한 `TOOL-FRICTION.md`의 JOEDESIGN 줄 7개(2026-11-23~25)와 `Library/tool-friction-review.md` 묶음 H·I다. 범위는 사용자가 2026-11-26에 확정했다(부모 세션이 전달). 준비 보고: [report.md](report.md).

### 바뀐 것

- **색·모션의 직접 관측(H).** SKILL.md에 새 절 "Direct observation of colour and motion"을 넣었다.
  - 색 규칙은 캡처 픽셀로 관측한다. 요소 안 획 중앙 행을 DPR 2 원본 또는 2x 줌에서 읽는다.
  - 기록 형식은 `median M, range a–b, n px`다. 채널 ±8 **그리고** 대비 ±0.2 안이어야 검사와 일치로 본다(2026-11-26 사용자 결정. "또는"이면 명도가 같은 색상 변화가 통과한다).
  - 새 스크립트 `scripts/sample-pixels.mjs`(Node만, 의존성 없는 PNG 해독)가 이 값을 낸다.
  - reduced-motion은 에뮬레이션으로 관측한다(그 줄은 그냥 `rendered`). 안 되면 페이지 자체 reduce 규칙을 조건 없이 주입한 렌더를 대체 관측으로 인정하고 `rendered (reduce injected)`로 적는다.
  - DESIGN Report Form에 두 문장을 더했다.
- **report-check R5(I).** before/after 쌍이 달라도 줄 끝이 `decided in rev N DEC-xxx`(리비전과 결정·레코드 ID)면 정의가 정한 변화로 인정한다. 한국어 `rev19 DEC-061에서 결정`도 받는다. 쌍 줄 안에 쓴 `product decision pending`도 기록으로 본다. 지적 문구가 이 형식을 안내한다. SKILL.md 한 구절, 템플릿 한 문장과 예시를 더했다.
- **report-check R3(항목 4).** 다음은 디자인 검사 결과로 읽지 않는다. 단, 디자인 검사 낱말이 들어 있으면 다시 읽는다.
  - `AC:`로 시작하는 줄과 AC 제목 아래 절(같은 수준 다음 제목까지).
  - 기술 검사 낱말을 더 넓혔다(typecheck, `validate-*`, pytest, 통합 테스트 등).
  - SKILL.md 6단계와 Report Form에 AC 줄 문장을 넣었다.
- **출처 관측 범위(항목 3).** 템플릿 Visual Sources에 출처 표를 넣고 `Observation scope (per state)` 열을 필수로 했다(관측 상태 → 결정, 미관측 상태 → 유도 근거). SKILL.md 1단계에는 일부 상태만 관측됐을 때 기록하고 진행하는 방법을 적었다.
- **전문 스킬(항목 5).**
  - SKILL.md에 설치 위치 네 곳을 적었다: 패키지 형제, `$CODEX_HOME/skills` 또는 `~/.codex/skills`, `~/.agents/skills`, `~/.claude/skills`.
  - 이 에이전트가 못 불러오는 스킬은 하위 에이전트가 그 SKILL.md를 읽어 적용하고, 경로와 해시를 기록한다. 어디에도 없으면 `not run`이다.
  - 규칙 행은 덮는 크기마다 전 화면 캡처가 1장 이상 있어야 센다.
  - `doctor`는 `~/.claude/skills`도 찾는다(마지막 순위, 러너의 해석도 같은 함수다). 없는 전문 스킬은 `missing_specialists`로 안내한다.
- **Playwright 없는 수집기(항목 6).** 새 스크립트 `scripts/capture-cdp.mjs`를 넣었다.
  - 설치된 Chrome/Edge를 DevTools 프로토콜로 헤드리스 구동한다. 브라우저는 `CHROME_PATH`, 없으면 일반 설치 경로에서 찾는다. 포트 0과 임시 프로필을 쓰고 Node 22 이상이 필요하다.
  - `capture.mjs`의 요청·결과 계약을 그대로 받는다. `capture.mjs`는 Playwright 패키지를 못 찾으면 이 스크립트로 넘긴다.
  - 직접 모드는 크기, DPR, 전 화면 캡처, `--reduce-motion emulate|inject`를 지원한다. `capture.mjs`도 probe의 `reduced_motion: "inject"`를 받는다.
  - `doctor`에 `collector` 블록(`route` playwright/cdp/none)을 넣었다.
  - ATELIER `scripts/design-checks/cdp.mjs`가 씨앗이다.
- **규칙 표 증가(항목 7).** SKILL.md 3단계와 템플릿 Rule coverage 주석을 바꿨다.
  - 규칙당 한 행만 둔다. 개정이 넓힌 화면·상태는 그 행 목록에 개정 표시와 함께 더하고, 기준이 바뀌면 Rule 칸을 고친다.
  - 재실행 범위는 "바뀐 파일이 그리는 화면을 가진 모든 행"이다.
  - `references/conformance.md`에 새 절 "Rule rows across revisions"를 넣었다. ATELIER 42행 중 개정별 15행을 5행으로 합치는 예와 T1 병합 행을 실었다.
- 버전: `skills/joedesign/VERSION` 2.0.2. README, QUICKSTART(캡처·색 관측 소절 추가), INSTALL 표기도 바꿨다.

### 확인된 것

- node 60/60, python 150 OK(건너뜀 2). 새 테스트는 report-check 8, sample-pixels 8(채널만·대비만 넘는 경우 outside 포함), doctor 2, CDP 수집 1이다. CDP 수집 테스트는 실제 Chrome으로 돌렸다.
- report-check 회귀: 274개 보고의 지적이 v2.0.1과 같고 바뀐 파일은 0이다. ATELIER에서 만든 fixture 8개 중 바뀐 것은 의도한 3개다(`AC:` 접두, AC 절, `decided in rev19 DEC-061`).
- sample-pixels는 ATELIER 캡처(품절 칩 M)에서 `median #8E8E8E, range 118–158, n 12 px`를 낸다. 범위는 ATELIER의 .NET 판독과 같다. `#8A8A8A`는 within, 수정 전 `#9A9A9A`는 outside다.
- 수집기는 픽스처 페이지에서 확인했다. DPR 2 전 화면, reduce emulate·inject, Playwright 없는 `capture.mjs` 대체 경로의 Tab·Enter와 단언을 돌렸다. ATELIER `client/dist`(정적, 읽기만)에서는 1024·360 전 화면을 찍었다. CDP로 찍은 `#8A8A8A` 칩은 sample-pixels로 `median #8A8A8A`(diff 0)였다. 캡처는 `evals/v2.0.2-tests-20261126/collector/`에 보관했다.
- doctor 전후: 바뀐 것은 version, 핵심 해시, `collector` 블록이다. 빈 `--skills-root`에서는 `missing_specialists`가 나오고 종료 코드는 2다.

### 확인되지 않은 것

- **행동 시험 0회.** 새 문구가 에이전트 행동을 바꾸는지 시험하지 않았다.
- ATELIER의 API가 필요한 화면은 찍지 못했다. 정적 빌드는 카탈로그 오류 상태만 보인다.
- macOS·Linux 브라우저 자동 탐색과 Edge 단독 환경은 실행하지 않았다. CDP `fill`·`hover`·`scroll`·`click`도 실제 브라우저로 시험하지 않았다.
- R3·R5 fixture의 초안 문장은 ATELIER에 원본이 없어 마찰 줄에서 재구성했다.

### 세션이 대신 내린 결정 (2026-11-26 사용자 결정: 아래 허용 오차만 바꾸고 나머지 확정)

- 과업 번호는 T045다.
- R5가 받는 ID는 `DEC-`만이 아니라 `[A-Z]{2,6}-숫자`다. ATELIER가 `SCR-004`를 썼다.
- 쌍 줄 안의 대기 표기도 인정한다.
- `~/.claude/skills`를 기본 탐색 마지막에 더했다.
- 허용 오차: 처음 안은 채널 **또는** 대비였다. 사용자 결정으로 **그리고**(둘 다)로 바꿨다. 이 바뀜으로 ATELIER 칩 L 판독(diff 5 / 0.22)은 outside가 됐다.
- CDP 수집기는 `mobile`·터치 에뮬레이션을 끈다(Playwright 경로와 같게).
- SKILL.md는 14,766B에서 18,452B로 커졌고(허용 오차 결정 반영 포함) 줄이지 않았다.
- part19 회귀 스크립트는 자기 출력을 덮어써서 돌리지 않았다. 같은 274개로 v2.0.1과 비교하는 스크립트를 따로 두었다.
- R5의 보고 전체 단위 대기 인정은 회귀를 바꾸지 않으려고 그대로 뒀다.


설치: 백업 → 바뀐 파일 교체 → 설치 트리가 저장소 `skills/joedesign`(v2.0.2)과 바이트 단위로 같은지 확인 → `harness_cli.py version`·`doctor`(영수증 [install-receipt-202.md](install-receipt-202.md)).
