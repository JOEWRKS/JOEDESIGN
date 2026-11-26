# JOEDESIGN 업데이트 내역

## 2.0.2 — ATELIER 실사용 마찰: 색·모션 관측, report-check R3·R5, 출처 관측 범위, 전문 스킬, Playwright 없는 수집기, 규칙 행 병합 (2026-11-26, T045)

- 게시: 사용자 승인("추천대로 게시", 2026-11-26, 부모 세션이 직접 받음; 하위 세션이 대신 내린 결정 6건 중 허용 오차만 "그리고"로 바꾸고 나머지 확정) 뒤 태그 v2.0.2, GitHub Release, 개인 설치 갱신(영수증 evals/v2.0.2-tests-20261126/install-receipt-202.md). 릴리스 노트 [release-notes-v2.0.2.md](evals/v2.0.2-tests-20261126/release-notes-v2.0.2.md).

출처: ATELIER(쇼핑몰) 실사용 중 기록한 `TOOL-FRICTION.md`의 JOEDESIGN 줄 7개(2026-11-23~25)와 `Library/tool-friction-review.md` 묶음 H·I다. 범위는 사용자가 2026-11-26에 확정했다(부모 세션이 전달). 준비 보고: [report.md](evals/v2.0.2-tests-20261126/report.md).

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

## 2.0.1 — 2.0.0 시험 결함 수정: doctor 경로·영수증 상대 경로·템플릿 정렬·문서 (2026-11-20, T044)

- 게시: 사용자 승인("세 도구 게시", 2026-11-20, 부모 세션이 직접 받음) 뒤 태그 v2.0.1, GitHub Release, 개인 설치 갱신(영수증 evals/v2-tests-20261119/install-receipt-201.md). 릴리스 노트 [release-notes-v2.0.1.md](evals/v2-tests-20261119/release-notes-v2.0.1.md).

출처: 2.0.0 시험 두 건([QUICKSTART 실행 시험](evals/v2-tests-20261119/docs-joedesign-report.md), [세 도구 연동 시험](evals/v2-tests-20261119/integration-report.md)). 사용자 승인 "세 도구 2.0.1 시작"(부모 세션이 받음). 준비 보고: [report-201.md](evals/v2-tests-20261119/report-201.md).

### 바뀐 것

- `doctor` 기본 탐색 경로가 `CODEX_HOME`을 따른다(T1): `$CODEX_HOME/skills`, 없으면 `~/.codex/skills`. `~/.agents/skills`와 패키지 형제 폴더는 그대로. `--skills-root`는 여전히 기본 경로를 **대체**하며 반복 지정할 수 있다. 이 사실을 `--help`, QUICKSTART 2절, INSTALL 표에 적었다(D2). "추가" 옵션은 만들지 않았다.
- `verify-design` 영수증(`joedesign.conformance.v1`)의 evidence 경로: `--project` 안의 파일은 프로젝트 기준 `/` 상대 경로로 쓴다(연동 D5). 프로젝트 밖(격리된 실행 폴더)은 절대 경로로 남는다. 이 경우 소비자 쪽에서 evidence root를 따로 허용해야 한다. 2.0.0의 절대 경로 영수증도 계속 읽힌다. schema 이름은 그대로다.
- `retrieve`에 객체가 아닌 requirements를 주면 `string indices…` 대신 `INVALID_INTENT: … {"id", "kind": "content|action|state", "description"}`로 `NOT_READY`(종료 코드 1)가 난다. `validate_intent`의 "list of objects" 오류에도 requirements·constraints·targets의 행 모양을 붙였다(연동 D7). `templates/DESIGN_INTENT.json`에 requirement 1행과 target 1행 예시를 넣었다.
- 스킬 본문 한 문장(`templates/DESIGN.md` Report Form): rendered 측정 전에 페이지의 링크 스타일시트가 실제로 로드됐는지(`document.styleSheets` 길이와 포함 여부) 확인한다. 없으면 그 측정은 `rendered`가 아니다(연동 D9). `references/conformance.md` 영수증 절에 상대 경로 한 문장.
- 문서: 공개 저장소라 로그인이 필요 없다(D1, QUICKSTART·README·INSTALL, SECURITY.md 공개 전제 한 줄). INSTALL에 백업·해시 비교 PowerShell 블록을 넣고 QUICKSTART가 그 자리를 가리킨다(D3). 업데이트는 `main` 복제본이 전제이고, 태그·detached 복제본은 `git fetch --tags; git checkout v2.0.1`을 쓴다(D4). 3절에 DESIGN.md·참고 화면이 없을 때 할 일 한 줄(D5).
- 버전: `skills/joedesign/VERSION` 2.0.1, README·QUICKSTART·INSTALL 표기.
- **연동 D3은 절차로 해결했다**(사용자 결정 "3번 절차로", 부모 세션이 전달. JOENESS review-gate.md에도 같은 문장이 들어간다). DESIGN `Result` 열 갱신이 authority 기준선을 stale로 만드는 문제다. JOENESS `assets/DESIGN.md:13`과 `assets/AGENTS.md:24-25`는 Result 갱신을 요구하고, JOEDESIGN `references/conformance.md:89-90`은 DESIGN 바이트를 고정한다. `references/conformance.md` authority 설명에 한 문장을 넣었다. JOENESS 연결 프로젝트에서 과업 완료 뒤 Result 칸 갱신으로 기준선이 stale이 되는 것은 정상이고, 다음 과업의 검수가 기준선을 새로 세운다. 같은 과업을 다시 검수하려면 Result 칸을 갱신 전 바이트로 되돌린 뒤 돌리고 다시 갱신한다. 코드(`conformance.py`의 authority 해시 범위)는 바꾸지 않았다.
- **연동 D8은 템플릿 정렬로 고쳤다**(사용자 "전부 고친 다음에 게시", 부모 세션이 전달. 행동 시험 없음). JOENESS 1.4.2는 JOENESS 파일이 먼저 있으면 그 `## Rule coverage` 표(8열, Result 포함)를 DESIGN 규칙 표로 정했다(JOENESS `assets/DESIGN.md:10-19`). 그래서 `templates/DESIGN.md`를 그 모양에 맞췄다.
  - 표 제목은 `## Rule Coverage`에서 `## Rule coverage`로 바꿨다. 앵커 `#rule-coverage`는 같다.
  - 표에 `Result` 열을 더해 JOENESS와 같은 8열이 됐다. 설명에 "Result links the latest TASK entry; no copied log"를 넣었다.
  - 머리줄은 JOENESS의 `Authority / version:`·`Approved scope:` 두 줄을 먼저 두고, 그 아래에 `**Status:**`·`**Revision:**`·`**Product Authority:**`를 남겼다. 맨 위 `**Reporting:**` 안내 줄(1.2.1)은 자리를 그대로 뒀다.
  - Report Form은 DESIGN.md에 둔다. `references/conformance.md`에 "JOENESS AGENTS 블록에도 같은 보고 규칙이 있고, DESIGN.md의 Report Form이 원본"이라는 한 문장을 넣었다.
  - `SKILL.md` 본문은 바꾸지 않았다. SKILL.md 109줄의 열 나열(rule → … → unmeasured)은 최소 기록이라 Result 열을 적지 않는다.

### 확인된 것

- 고치기 전 실패를 먼저 확인했다. 새 테스트 4개(doctor `CODEX_HOME`, 상대 evidence, 읽을 수 있는 retrieve 오류, 템플릿 행 모양)가 2.0.0 코드에서 실패했다. T1은 `CODEX_HOME=<빈 폴더>`로 `doctor`를 돌려 재현했다. 실제 홈의 `~/.codex/skills`·`~/.agents/skills`가 AVAILABLE로 나왔다.
- 고친 뒤 node 44/44, python 147 OK(건너뜀 2), part19 회귀 274개 R1~R6 수가 1.3.3·1.3.4와 같고 R7 바뀐 파일은 0이다. `harness_cli.py version`은 2.0.1이다.
- 영향 진단(`inspect-impact`)은 상대 경로 영수증과 2.0.0식 절대 경로 영수증 둘 다에서 재사용 후보 4/4를 낸다(새 테스트).
- JOENESS `review-gate.mjs`는 **읽기만** 해서 확인했다(실행 안 함). evidence 경로가 절대 경로이거나 안전한 상대 경로(`/` 구분, `..`·`\`·`:` 없음)이면 `--root` 기준으로 풀고 root 또는 `--evidence-root` 안에 있는지 본다(`pathFor`, 25–30줄). 새 상대 경로는 이 조건을 만족한다.
- INSTALL 백업 블록을 scratch 폴더(`CODEX_HOME`·`USERPROFILE`을 프로세스 안에서만 바꿈)에서 실행했다. 31개 파일이 일치하면 출력이 없고, 백업 `VERSION`을 바꾸면 그 한 파일이 양쪽 표시로 나온다.

### 확인되지 않은 것

- **행동 시험 0회.** Report Form 스타일시트 확인 문장, D3 절차 문장, D8 템플릿 정렬이 에이전트 측정 행동을 바꾸는지 시험하지 않았다. 문서 변경(D1~D5)도 다시 따라 해 보는 시험은 하지 않았다.
- JOENESS `review-gate.mjs`가 새 상대 경로 영수증을 실제로 통과시키는지는 실행해 보지 않았다(코드 읽기만 함).
- `git fetch --tags; git checkout v2.0.1`은 태그가 아직 없어 실행하지 않았다.
- macOS·Linux에서 `CODEX_HOME` 동작.

### 알려진 충돌

- 없음. 연동 D3과 D8은 2.0.1에서 고쳤다(위 "바뀐 것").

### 세션이 대신 내린 결정

- 과업 번호는 T044로 새로 땄다(2.0.0까지는 T043).
- 프로젝트 밖 evidence는 절대 경로로 남겼다. `..` 상대 경로는 review-gate의 `safeRelative`가 거부하고, `verify-design`에 `--evidence-root`를 새로 다는 것은 행동 범위를 넓히는 일이라 하지 않았다.
- `retrieve`의 requirements가 빈 목록이면 지금처럼 허용한다(검색 전용 명령). 행 모양만 검사한다.
- D9 문장은 `references/conformance.md`가 아니라 `templates/DESIGN.md` Report Form 측정 모드 문단에 넣었다. 그 문단이 `rendered (injected css)` 어휘를 정하는 곳이라서다.
- 연동 D11(전문 리뷰 미실행)·D13(빈 상태 문구 소유)은 이번 과업 범위 밖이라 손대지 않았다.

## 2.0.0 — 저장소 위생·보안 검토·빠른 시작 (2026-11-19, T043)

- 범위(사용자 승인): A 저장소 위생, B 보안 검토 문서, C 빠른 시작·README 축약, 버전 2.0.0. **스킬 동작은 1.3.4와 같다**: `skills/joedesign`에서 바뀐 파일은 `VERSION` 하나.
- A 위생: 아무도 참조하지 않는 `docs/superpowers` 4개 삭제(plans 2026-09-29·2026-10-06, specs HANDOFF·TOOL_RESEARCH). `fixtures/contract-cases/evidence/v02-operational-validation-v1/`(52파일, 약 18.8MB)을 `evals/archive/2026-11-19-unreferenced/`로 이동.
  사용자 이름이 든 홈 경로를 `~`로 가림: 15개 파일(이동한 기록 8, RACI 초안 9줄, evals 6). 남은 38개는 테스트가 해시를 고정한 20개, 회귀 입력 1개, 같은 폴더 기록이 해시를 적어 둔 17개라 그대로 둠. 이력은 다시 쓰지 않음.
- B [SECURITY.md](SECURITY.md): 비밀값 0(트리·이력), 매니페스트·CI 없음, 남은 식별자와 이유, 스크립트 신뢰 경계, 알리는 방법.
- C [docs/QUICKSTART.md](docs/QUICKSTART.md)(Codex·Claude Code 설치, 확인, 검수 요청, `report-check.mjs` 도장·`--verify`, 업데이트, 제거). README 버전 설명 두 줄을 한 문장과 이 파일 링크로 바꾸고 절반으로 줄임. docs/INSTALL.md 버전 표기 2.0.0.
- 게이트([evals/v2-release-20261119/report.md](evals/v2-release-20261119/report.md)): `git diff --stat v1.3.4 -- skills/joedesign` = `VERSION` 1개, node 44/44, python 142 OK(건너뜀 2), part19 회귀 274개 R1~R6 수 동일·R7 바뀜 0.
- 게시: 사용자 승인("게시 ㄱㄱ", 2026-11-19, 부모 세션이 직접 받음) 뒤 태그 v2.0.0, GitHub Release, 개인 설치 갱신(영수증 evals/v2-release-20261119/install-receipt.md). 스킬 폴더에서 설치본이 바뀐 파일은 `VERSION` 하나.

## 1.3.4 — R7 허용 문장 경로 보정: 페이지 이름·낱말 형태 부정·절 단위 (2026-11-18, T043)

- 게시: 사용자 승인("게시", 2026-11-18, 부모 세션이 직접 받음) 뒤 VERSION 1.3.4, 태그 v1.3.4, GitHub Release, 개인 설치 갱신(영수증 evals/check-coverage-20261104/part19/install-receipt.md).
- 출처: 18부 반사실 검사([part18/behavior-ab/report.md](evals/check-coverage-20261104/part18/behavior-ab/report.md))에서 괄호 없는 `rendered`를 목록 밖 문장으로 넘기는 허용 경로가 올바른 보고 3/4를 떨어뜨림.
- `report-check.mjs` R7 허용 경로: (a) 허용 절이 그 줄의 검사 이름(`C1`) **또는 페이지 이름**(검사 칸의 괄호 속·쉼표 뒤, 예 `요청 화면`)을 들면 통과. 다른 줄의 페이지만 들고 이 줄의 페이지는 들지 않은 절은 이 줄을 넘기지 못함.
  (b) 부정어를 낱말 형태로 읽음(`못해`·`막아`·`막혀` 등). `마지막`의 `막`, 템플릿 어휘 `not spot-checked`의 `not`은 부정이 아님. (c) 문장을 쉼표·세미콜론·빗금에서 절로 나눠 절 단위로 판정(괄호는 절 안에 둠).
  `rendered: 요청 화면 own css, 확인 화면 injected css`가 요청 화면 줄을 넘김. 지적 문구 끝 "naming this check or its page". `--verify` 의미 같음.
- references/conformance.md R7 설명과 templates/DESIGN.md 측정 모드 문단에 "검사 이름 또는 페이지" 한 절씩.
- 확인된 것([part19/report.md](evals/check-coverage-20261104/part19/report.md)): 18부 실물 반사실 A(괄호만 지움) R7 3/4 보고 → 0/4. 274개 보고 R1~R6 수·R7 결과 1.3.3과 동일, 18·16·14·15부 보고 86건 R7 동일, 18부 도장 `--verify` 4/4.
  node 44/44(report-check 27 → 30), python 142 OK.
- 확인되지 않은 것: 행동 효과(실행 0회). 페이지 이름 추출은 검사 칸 형식(괄호·쉼표)에 기댐.
- 행동 시험(2026-11-18, [part20/behavior-ab/report.md](evals/check-coverage-20261104/part20/behavior-ab/report.md), 실행 4 + 채점 1): 장면 M-L(18부 장면 M + TASK.md에 괄호 없는 `rendered` 예전 보고)에서 올바른 보고 4/4, 1.3.4 R7 오탐 0/4, 거짓 `rendered` 0, `--verify` 4/4(사전 기준 통과). 그러나 4/4가 `rendered (own css)`를 써서 문장 허용 경로는 행동으로 여전히 시험되지 않음(sentence 0/4); 같은 보고에 v1.3.3도 R7 0/4.

## 1.3.3 — R7 탐지 범위 확장: 줄마다 판정, `--inject` 문장 (2026-11-18, T043)

- 게시: 사용자 승인("게시(보정 포함)", 2026-11-18, 부모 세션이 직접 받음) 뒤 VERSION 1.3.3, 태그 v1.3.3, GitHub Release, 개인 설치 갱신(영수증 evals/check-coverage-20261104/part17/install-receipt.md).
- 출처: 16부 행동 A/B([part16/behavior-ab/report.md](evals/check-coverage-20261104/part16/behavior-ab/report.md))에서 1.3.0 팔의 거짓 `rendered` 4건 중 1.3.2 R7이 2건만 잡음.
  놓친 형태: r05(일부 줄만 `rendered (style.css 주입)`, 다른 줄은 `rendered`뿐), r08(본문이 "같은 파일을 `--inject`로 넣어 측정"이라고만 적음).
- `report-check.mjs` R7: (a) 주입 언급 판정을 문장 단위로 바꿈. 부정이 아닌 주입 낱말(주입, inject(ed/ing/ion), `--inject`)과 CSS 낱말(css, 스타일, style, stylesheet)이 같은 문장에 있으면 거리 제한 없이,
  `--inject`는 혼자서도(코드 블록 안 명령 포함), `style.css를 넣어 쟀다`처럼 CSS를 넣어/넣고로 넣은 문장도 주입 언급이다. CSS 없는 "넣어"(200자를 넣어)와 테스트 데이터 주입은 아니다.
  (b) 주입을 말하는 보고에서 넷째 칸이 `rendered`뿐인 줄은 줄마다 지적(1.3.2는 주입 표시 줄이 하나도 없을 때 첫 줄만). 페이지가 자기 CSS를 읽은 줄은 `rendered (own css)`로 적거나,
  목록 밖 문장이 그 줄의 검사 이름 첫 낱말(`C1` 등)과 함께 자기 CSS를 읽었다고 말하면(own css, 자기 CSS, 링크 CSS를 읽었다 …, 부정 없음) 통과. `rendered (<what differed>)` 줄은 1.3.2처럼 받는다.
  `--verify` 종료 코드 의미는 같다.
- templates/DESIGN.md 측정 모드 문단과 conformance.md R7 설명에 한 줄씩.
- 확인된 것([part17/report.md](evals/check-coverage-20261104/part17/report.md)): node 41/41(report-check 23 → 27), python 142 OK. 16부 A 4/4 R7(1.3.2 2/4), 16부 B 4·14부 B 16·15부 `text ok` 42건 새 R7 0,
  기존 evals 보고 274개 R1~R6 지적 수 1.3.2와 같음, R7 0 → 0.
- 확인되지 않은 것: 행동 효과(행동 시험 0회). 274개 중 주입을 말하는 보고가 2개뿐이라 정당한 섞임의 실물 오탐 검사는 테스트 문장에 기댄다.
- 행동 시험(2026-11-18, [part18/behavior-ab/report.md](evals/check-coverage-20261104/part18/behavior-ab/report.md), 실행 4 + 채점 1): 정당한 섞임 장면(index 자기 CSS, confirm 주입)에서 올바른 보고 4/4, R7 오탐 0/4, 거짓 `rendered` 0, `--verify` 4/4. 허용 경로는 4/4가 `rendered (own css)`; 반사실(괄호를 지운 실물)에서는 문장 허용 경로가 올바른 보고 3/4를 떨어뜨림(검사 이름 요구, `마지막`의 `막`·`not spot-checked`의 `not` 부분 일치).

## 1.3.2 — 보고 배치 R6 확장: 여섯 줄 앞 요약·여섯 줄과 목록 사이 문단 (2026-11-15, T043)

- 게시: 사용자 승인("둘 다 게시", 2026-11-15, 부모 세션이 직접 받음) 뒤 VERSION 1.3.2, 태그 v1.3.2, GitHub Release, 개인 설치 갱신(영수증 evals/check-coverage-20261104/part15/install-receipt.md).
- 출처: 1.3.1 행동 A/B([part14/behavior-ab/report.md](evals/check-coverage-20261104/part14/behavior-ab/report.md))에서 1.3.0 팔의 순서 실패 9건 중 8건이
  "여섯 줄 앞 요약 문단" 또는 "여섯 줄과 결과 목록 사이 문단"이었고, 1.3.1 R6(결과 줄만 봄)는 이 둘을 잡지 못했다.
- `report-check.mjs`: 여섯 줄 이름이 4개 이상인 보고에서 R6a(여섯 줄 첫 줄 앞의 산문 줄. 맨 앞 한 줄 제목은 허용: 80자 이하, 문장부호 `.?!。` 없음, `다`로 끝나지 않음.
  `#` 제목·구분선·인용부호만인 줄·코드 블록·도장 줄은 제외)와 R6b(마지막으로 시작한 여섯 줄 항목의 끝과 `design check results:` 줄, 그 줄이 없으면 첫 결과 줄 사이의 산문 문단.
  항목 바로 아래 빈 줄 없는 줄과 들여쓴 하위 항목, 40자 이하 이름표 줄, 결과 줄 바로 위 `:`로 끝나는 줄, R5 기록 줄은 제외)를 더했다. 지적은 기존처럼 종료 코드 1이며 `--verify`의 의미는 같다.
- templates/DESIGN.md Report Form 순서 문단에 한 줄: 여섯 줄 앞에 요약 문단, 여섯 줄과 결과 목록 사이에 문단을 두지 않는다(요약·질문은 설명 문단으로).
- 확인된 것([part15/report.md](evals/check-coverage-20261104/part15/report.md)): node 37/37(report-check 20 → 23), python 142 OK. 1.3.1 행동 A/B 보고 32건에서 1.3.1 팔 16건은 모두 그대로 ok,
  1.3.0 팔의 순서 실패 9건은 9건 모두 R6/R6a/R6b로 지적, 채점자가 순서 준수로 본 23건에는 R6 계열 지적 0. 기존 evals 보고 274개의 R1~R5 지적 수는 같다.
- 확인되지 않은 것: 행동 효과(행동 시험 0회). 1.3.1 이전 규칙으로 쓰인 기존 보고는 새로 지적을 받는다(274개 중 106개 파일. 도장 보고 118개 중 `--verify` 결과 줄이 바뀐 것 72개, 그중 `text ok` → 지적 있음 45개).
  빈 줄 없이 마지막 항목 바로 아래 붙인 문단은 그 항목의 이어지는 줄로 보아 잡지 않는다.
- 행동 시험(2026-11-17, 실행 8 + 채점 1, [part16/behavior-ab/report.md](evals/check-coverage-20261104/part16/behavior-ab/report.md)): 과제 자료가 CSS 주입을 말하지 않는 장면 2'에서 넷째 칸 정확 표기 1.3.2 4/4 vs 1.3.0 0/4(사전 기준 충족),
  거짓 `rendered` 0 vs 4, 두 팔 모두 `loaded:false`를 알아채고 주입해 다시 잼(4/4). R7은 1.3.0의 거짓 표기 4건 중 2건만 잡음(일부 줄 표시, `--inject`만 쓴 문장은 못 잡음).

## 1.3.1 — 보고 배치 규칙과 주입 CSS 측정 표시 (2026-11-15, T043)

- 게시: 사용자 승인("게시", 2026-11-15, 부모 세션이 직접 받음) 뒤 VERSION 1.3.1, 태그 v1.3.1, GitHub Release, 개인 설치 갱신(영수증 evals/check-coverage-20261104/part14/install-receipt.md).
- 출처: JOEFLOW 1.7.0 세 도구 통합 시험(2026-11-12)의 JOEDESIGN 이슈 2건.
- 보고 배치(b3efe2f): templates/DESIGN.md `## Report Form`의 한 문단만 순서를 정한다. JOENESS 여섯 줄 → `design check results:`와 목록 →
  `## Display before/after`(있을 때) → 설명 문단 → 도장 줄(항상 마지막). SKILL.md 6단계·conformance.md는 그 절을 가리킨다.
  `report-check.mjs` R6: 결과 줄이 여섯 줄의 첫 줄보다 위에 있으면 지적. 여섯 줄 사이에 넣은 목록(1.3.0 보고 다수)은 허용.
- 측정 모드(c4f6779): 결과 줄 넷째 칸은 `code`, `rendered`, `rendered (injected css)`(미리보기가 연결 CSS를 못 읽어 같은 CSS를 주입해 잼),
  그 밖의 차이는 `rendered (<what differed>)`. SKILL.md·conformance.md·DESIGN.md 템플릿에 정의와 예시. R7: 본문이 CSS 주입을 말하는데
  주입 표시가 붙은 rendered 줄이 하나도 없으면 지적.
- 확인된 것([part14/report.md](evals/check-coverage-20261104/part14/report.md)): 기존 evals 보고 274개 규칙별 지적 수와 도장 보고 118개
  `--verify` 결과가 1.3.0과 같다(R6·R7 0). 통합 시험 원본은 R7 1건(의도한 탐지), 고친 예시는 ok. node 34/34, python 142 OK.
- 확인되지 않은 것: 새 문구에 대한 에이전트 행동(행동 시험 0회), JOENESS 쪽 소비. SKILL.md가 1.3.0보다 554바이트 늘었다.
- 행동 시험(2026-11-15, 실행 32 + 채점 2, [part14/behavior-ab/report.md](evals/check-coverage-20261104/part14/behavior-ab/report.md)): 보고 순서 준수 1.3.1 16/16 vs 1.3.0 7/16,
  주입 측정 넷째 칸 `rendered (injected css)` 8/8 vs 6/8(1.3.0도 과제 자료만으로 대부분 같은 표기), R7 지적 0 vs 2, 오탐·퇴행 없음.

## 1.3.0 — 재배치는 전후 표시 대조표로 판정 (2026-11-11, T043)

- 1.2.1에 더한 것: SKILL.md "Decide the scope" 문단에 "기존 요소를 옮기거나 겹치거나 숨기거나 합치면 먼저 DESIGN.md와 보고에 `## Display before/after`를
  요소마다 `before: element | content shown | route` / `after: ...` 두 줄(사라지면 `hidden`)로 적고, 두 줄이 다르면 제품 결정 대기, 같으면 디자인 결정".
  templates/DESIGN.md Report Form에 같은 규칙 한 문단(인계 세션용), conformance.md에 R5 설명. `scripts/report-check.mjs` R5: 옮김·겹침·숨김·병합 완료 문장이 있는데
  before/after 줄도 `display unchanged`도 없으면, 또는 쌍이 다른데 `product decision pending` 줄이 없으면 지적한다. 스키마·CLI·도장은 그대로이고, 테스트는 11개에서 16개가 됐다.
- 뺀 문장(문구 총량 유지: SKILL.md 14,216바이트에서 14,212바이트): (1) 인계 문단 "The handoff tells that session to read DESIGN.md's Report Form section and report in that form."
  (12부에서 재지 않음. 효과는 DESIGN.md 맨 위 줄이 냄) (2) "The script reads the form of the sentences, not whether a number is true."(스크립트 주석·conformance.md에 같은 말)
  (3) "Review-only never gains write authority. The user need not prepare machine files or choose between a core and harness."(작업 종류 표와 중복, 재지 않음).
- 확인된 것([README 13부](evals/check-coverage-20261104/README.md), Opus 89회, 1.2.1 대조군):
  - 재배치 효과: 표시가 바뀐 재배치의 제품 결정 대기 8/8 vs 1/8, 요소별 전후 대조 12/12 vs 0/12. 위치만 바꾼 과제의 오탐은 0(4/4 vs 4/4).
  - 기존 항목: 기능 추가 6건은 같거나 높았다(p3 5/6 vs 3/6). 인계 24건은 l 11 vs 10, w 11 vs 9, r4 12 vs 10, g 3 vs 2, h 8 vs 7, t·c 같음. 회귀 6건은 같았다.
    state.json 읽기는 21/24 vs 13/24.
  - R5 오탐: 기존 보고 306건에서 R1~R4 결과 변화 0, 재배치 보고 21/21 감지, 그 밖 285건 중 16건.
  - 40턴(새 고정물 L-J2, 9부 G와 같은 채점기로 재채점): h2 33 vs 27(9부 기준 30), 8개 전부 29 vs 20(기준 21), 함정 h4·h6·h8 40/40,
    주 세션 35턴 report-check 실행·도장 일치 35/35, 라이브 대조 24행 일치.
- 확인되지 않은 것·남은 것:
  (1) 전후 줄의 내용 칸을 추상적으로 적으면("현재 수, 색, 좌표") 실제 글자가 바뀌어도 쌍이 같아진다. 스크립트는 막지 못한다(한 턴 f03-K, 40턴 턴 4).
  (2) 40턴에서 h1(38 vs 39)과 인계 h3·h7(각 4 vs 5)이 각 1턴 낮다. 원인은 전후 대조와 무관한 보고 누락이지만, 측정된 차이로 남긴다.
  (3) 셀당 n=3~4, 장면별 채점기 1명, 40턴은 세션 1개다. K 보고의 Display 줄이 팔을 드러낼 수 있다.
  (4) 대국 화면은 엔진 파일 없이 가짜 엔진으로 쟀다.
  (5) JOENESS 쪽 도장 소비는 여전히 별도 과제다.
- 게시: 사용자 승인("1.3.0 게시") 뒤 VERSION 1.3.0, 태그 v1.3.0, GitHub Release, 개인 설치 갱신(영수증 evals/check-coverage-20261104/part13/install-receipt.md).
- 사고: 40턴 첫 시도에서 코디네이터가 백로그에 없는 턴 6 메시지를 보내 무효 처리했고(사용자 결정 "처음부터 다시"), 기록은 part13/longterm-J-void1/에 남겼다.

## 1.2.1 — 인계 세션이 Report Form을 읽게 하는 안내 줄 (2026-11-10, T043)

- 1.2.0에 더한 것(문서만, 스크립트·스키마·계약·CLI 그대로): templates/DESIGN.md 제목 바로 아래에 "보고는 `## Report Form` 절을 그대로 따른다" 한 줄,
  SKILL.md 인계 문단에 "인계 때 그 세션에 DESIGN.md의 Report Form 절을 읽고 그 형식으로 보고하라고 알린다" 한 문장.
- 확인된 것(한 턴 20회 + 블라인드 채점 2, 1.2.0 대조군, [README 12부](evals/check-coverage-20261104/README.md)): 스킬 없는 인계 세션이 Report Form 절을 읽은 비율이 1.2.1 4/4,
  1.2.0 2/4였다(1.2.0의 두 건은 11부와 같이 grep만 함). 결과 목록 형식은 3/4 vs 2/4, 수정 줄 `fixed`/`changed`는 4/4 vs 2/4였다. 해결 줄·`design checks: none ran` 같은
  기존 규율에서 퇴행은 없었다. 회귀 14/14, 11/11, 142 OK.
- 제외한 것: 같은 시험에서 확인한 재배치 경계 문구(SKILL.md 두 문장, operation.md 한 문장, "기존 기능의 이동·겹침·숨김이 보이는 내용이나 경로를 바꾸면 제품 결정 대기")는
  효과가 없어(표시가 바뀌는 재배치의 대기 기록 2/4 vs 2/4) 사용자 결정("재배치 문구 빼고 게시")으로 넣지 않았다. 상단 바 과제에서 그 문구를 받은 두 세션도 표시를 바꾸고 "위치만
  바꿈"으로 분류했다. 바꾸기 전과 후의 표시를 대조하는 절차가 다음 과제다.
- 확인되지 않은 것: (1) 재배치가 표시를 바꿀 때의 경계(위 제외 항목). (2) SKILL.md 인계 지시 문장은 측정하지 않았다(프롬프트를 같게 둠). (3) 인계 세션의 요약 문장 범위(g·h 2/4)는
  스크립트가 없어 문구로 막히지 않는다. (4) 셀당 n=2, 고정물 1개, 채점기 장면별 1명이며, 40턴 재측정은 없다. (5) JOENESS 도장 소비는 별도 과제다. (6) 게시한 SKILL.md는 시험본과
  재배치 두 문장만 다르다. 인계 시험은 스킬을 읽지 않으므로 그 차이와 무관하며, 재배치 시험의 1.2.1 팔 결과는 게시본에 해당하지 않는다.
- 게시: 사용자 승인("재배치 문구 빼고 게시") 뒤 VERSION 1.2.1, 태그 v1.2.1, GitHub Release, 개인 설치 갱신(영수증 evals/check-coverage-20261104/part12/install-receipt.md).
  정정: 태그 v1.2.1은 06573af, GitHub Release 게시됨. 사고 기록(edfc9e7에 섞인 미완성 R5 코드와 되돌림)은 evals/check-coverage-20261104/part12/incidents.txt.

## 1.2.0 — JOEFLOW 입력 명시·인계용 Report Form·JOENESS 도장 소비 제안 (2026-11-09, T043)

- 1.1.0에 더한 것(문서만, 스크립트·스키마·계약·CLI 그대로): SKILL.md "Decide the scope"에 Product source의 실체를 적은 문단
  (`product-definition/<slug>/state.json`·`MASTER_PLANNING_SPEC.md`·`approval_status.py`를 먼저 읽고 승인 revision을 Product
  Authority로 적기, 승인된 정의에 없는 사용자 가시 동작은 `product decision pending`(제품 결정 대기)으로 기록해 JOEFLOW 구현
  재진입(DISCOVER/CLOSE, `RELAYED_USER_INTENT`, `NEW_PRODUCT`)으로 돌려보내기, 사용자가 직접 요청한 동작은 지정한 대로 만들되
  제품 기록은 대기); operation.md 같은 두 문장; templates/DESIGN.md에 주석이 아닌 본문 절 `## Report Form`(결과 목록 한 줄 형식,
  `fixed`/`changed`, `changed`는 남은 문제, `design checks: none ran`)과 SKILL.md 인계 문단의 연결; conformance.md에 ROADMAP Check
  칸 예시 한 줄과 "장부(JOENESS TASK)가 보고를 보관하면 도장 줄도 함께"; JOENESS 측 제안서
  [docs/proposals/2026-11-09-joeness-report-stamp.md](docs/proposals/2026-11-09-joeness-report-stamp.md)(TASK 도장 줄·완료 전
  `--verify`·`changed`→남은 문제, Check 칸 예시). JOENESS 저장소는 고치지 않음.
- 확인된 것(한 턴 블라인드 24회 + 채점 3, [README 11부](evals/check-coverage-20261104/README.md)): 제품 기능 추가 과제에서 state.json·
  기획서 읽기 I 6/6 vs H(1.1.0) 0/4, 승인 rev 명시 6/6 vs 1/4, 정의에 없는 조작(접기 버튼)을 제품 결정 대기로 기록 3/3 vs 1/2; 스킬 없는
  인계 세션의 결과 목록 형식 4/6 vs 0/4, `fixed`/`changed` 4/6 vs 0/4, `changed`가 해결 줄에 없음 5/6 vs 1/4; 라이브 대조 7건 일치;
  회귀 4건 8부 기준표 전부 충족·도장 4/4. 회귀 14/14, 11/11, 142 OK.
- 확인되지 않은 것: (1) 기존 기능 재배치가 표시 내용을 바꿀 때(복기 상단 바)의 경계 — I 3건 모두 "제품 결정 아님"으로 처리, 문구가
  정해 주지 않음; (2) 인계 세션 2/6은 목록을 쓰지 않음(1건은 DESIGN.md를 grep만 해 Report Form 절을 못 봄, 1건은 보고도 안 따름), 인계에는 스크립트·도장이 없음; (3) JOENESS의 도장
  소비는 제안서뿐, 실제 연결·검증 없음; (4) 40턴 재측정 없음, 고정물 1개, 셀당 n=2~3, 장면별 채점기 1명.
- 게시: 사용자 승인("게시 진행") 뒤 VERSION 1.2.0, 태그 v1.2.0, GitHub Release, 개인 설치 갱신(영수증 evals/check-coverage-20261104/part11/install-receipt.md).

## 1.1.0 — 보고 결과 형식·보고 검사 스크립트·도장 (2026-11-09, T043)

- 1.0.0에 더한 것: DESIGN 규칙 검사 표(Spot check 열 포함), 보고의 결과 목록 한 줄 형식
  `check | result | sizes x states, mode | rendered or code | spot check`, 수정 줄의 `fixed`/`changed`,
  보내기 전 `scripts/report-check.mjs`(R1~R4)와 `ok` 도장(`report-check: ok <chars> chars <sha8>`,
  `--verify`), 검사 없는 턴의 `design checks: none ran`. 문서 5개·스크립트 1개·테스트 1개. 코어·스키마·
  계약·CLI 동작은 1.0.0 그대로.
- 확인된 것: 한 턴 블라인드 비교 7회(A~G, 총 132회), 40턴 롱텀 2회(A·B, B·G), 10턴 1회(H). 40턴에서 통과
  주장 범위 G 30/40 vs B 12/40, 10턴에서 도장 일치 8/8·보낸 글 지적 0/8. 아래 "검사 범위 표 보강" 절과
  [evals/check-coverage-20261104](evals/check-coverage-20261104/README.md).
- 확인되지 않은 것: (1) H안의 40턴 후반, (2) 스킬 없는 인계 세션의 보고 형식(G 1/5, H 1/2), (3) JOEFLOW
  제품 정의 참조(40턴 0회), (4) 도장은 들키게 할 뿐 막지 못하며 JOENESS가 아직 받지 않음, (5) 고정물 1개·
  가짜 엔진·E2E 미실행·채점기 변동. 다음 과제(I안): JOEFLOW 입력 명시, 인계용 DESIGN.md에 보고 형식 동반,
  JOENESS의 도장 소비.
- 개인 설치 갱신은 별도 영수증(evals/check-coverage-20261104/longterm-H/install-receipt.md).

## 검사 범위 표 보강 (2026-11-04, T043)

- DESIGN 템플릿에 토큰 역할 표(Role | Parts | Token/value | Status)와 규칙별 검사 범위 표
  (Rule | Check | Layouts | Sizes | States | Unmeasured) 추가. SKILL.md 2·3·6단계,
  conformance·operation·visual-translation에 같은 계약을 한 곳씩 연결.
- 검사 행이 없는 규칙은 미측정이며 통과가 아니다. "0 violations"는 적힌 행에만 해당하고,
  보고는 실행한 행과 미측정 행을 적는다. 스킬 없는 세션에 인계할 때 표가 DESIGN.md로 이동.
- 단일 턴 48회 블라인드 A/B: 요구하지 않은 장면 32회에서 규칙→검사 범위 연결 B 16/16 vs
  A 4/16, 행 단위 상태 B 13/16 vs A 0/16, 퇴행 없음. 40턴 롱텀 세션 비교(80패킷)에서는 우위
  없음: 재측정·승인 구분·완료 압박 저항 동등, 통과 주장 범위는 B 17/40 vs A 31/40, B의 검사 표
  한 행이 실측과 4px 어긋난 채 PASS로 유지됨.
- 롱텀에서 나온 두 빈틈에 대한 문구 추가(2026-11-05): 보고의 통과 숫자마다 같은 문장에 검사·
  배치/크기·상태·코드/렌더 범위(SKILL 6단계), 검사 결과를 쓰기 전 한 대상에서 규칙이 말하는 양을
  직접 관찰해 대조하고 안 했으면 행에 "not spot-checked"(SKILL 3단계·conformance·템플릿).
- 추가 문구 한 턴 24회 블라인드 비교(추가 전 vs 후): 브라우저 없는 16회에서 통과 주장 범위
  5/8 vs 0/8, 코드·렌더 구분 8/8 vs 2/8, 대조 여부 표기 7/8 vs 0/8, 대조 없는 '해결' 회피 8/8 vs
  4/8. 브라우저 8회에서 실제 표본 대조 4/4 vs 0/4, 통과 주장 범위 4/4 vs 2/4. 퇴행 없음.
  남은 빈틈: 브라우저 시험에서 모든 행에 대조 여부를 적은 경우 0/4, '해결' 절 한정 1/4. 롱텀
  재측정은 하지 않음. [기록·한계](evals/check-coverage-20261104/README.md).
- 표본 대조 열 추가(2026-11-06): Rule Coverage 표에 Spot check 열(모든 행에 대상과 두 값, 또는
  "not spot-checked", 빈 칸은 대조 안 함, 한 행의 대조는 다른 행을 덮지 않음). 대조하지 않은 행의
  결과는 "not spot-checked"를 붙여 인용하고 해결·검증·완료로 적지 않는다(SKILL 3·6단계,
  conformance, 템플릿).
- 한 턴 20회 블라인드 확인(열 추가 전 C vs 후 D, 대조 문구 없는 B 포함): 검사가 규칙과 다른 양을
  재는 결함을 심은 과제에서 결함을 밝힌 시험 B 0/4, C 3/4, D 4/4. 모든 행에 대조 여부 표기는
  브라우저 두 장면 합 C 0/8 vs D 8/8, 대조 없는 '해결' 회피 2/8 vs 5/8. 남은 빈틈: 보고 문장의
  통과 범위는 나아지지 않음(C 6/8 vs D 3/8), 결함을 밝힌 시험도 고치지는 않고 사용자 결정으로
  남김. 롱텀 재측정 없음.
- 보고 결과 줄 형식 고정(2026-11-06): 보고의 디자인 검사 결과를 한 목록에 검사마다 한 줄,
  `check | result | sizes x states, mode | rendered or code | spot check` 형식으로 적는다. 곁검사·
  전후 비교·검사로 주장하는 수정도 한 줄씩. 목록 밖에서는 통과·건수를 범위와 함께 쓸 때만 쓴다
  (SKILL 6단계, conformance).
- 한 턴 12회 + 앞선 12회 재채점(형식 고정 전 D vs 후 E): E 12회 모두 결과 목록을 썼고 곁가지
  결과의 범위 누락이 사라졌다. 브라우저를 쓴 두 장면 합으로 통과 문장 범위 2/8 vs 5/8, 코드·렌더
  구분 0/8 vs 4/8(같은 묶음 재채점에서 이 판정이 12건 중 5건 바뀌어 방향만 읽음). 남은 빈틈: 맨 위
  요약 문장의 범위(결함 심은 과제 E 3/4 미달), 대조 없는 '해결' 회피는 그대로(9/12 vs 8/12).
- 수정 줄 단어 고정과 요약 괄호(2026-11-07): 결함은 그것이 보였던 대상에서 한 번 직접 관찰한 뒤에만
  고친 것으로 친다. 결과 목록의 수정 줄은 그 관찰이 있으면 `fixed`, 없으면 `changed`이고 `changed`는
  이슈를 열어 둔다. 목록 밖의 검사 결과에는 그 줄에서 복사한 괄호(크기 x 상태, 렌더·코드, 대조
  결과)를 붙인다(SKILL 5·6단계, conformance).
- 한 턴 12회 + 앞선 12회 재채점(E vs F): 대조하지 않은 검사로 '없앴다·닫았다'고 적은 보고가 E
  브라우저 장면 4/4에서 F 0/12로 사라졌다(보고 원문 기준, '고침' 2건은 캡처로 따로 확인). 남은 빈틈:
  맨 위 요약 문장의 범위는 그대로(결함 심은 과제 F 2/4 미달), 오프라인 장면의 통과 문장 범위도
  나아지지 않음(3/4 vs 2/4). 블라인드 채점의 '해결 회피'는 같은 묶음 판정이 채점기마다 달라 근거로
  쓰지 않음.
- 보고 검사 스크립트(2026-11-07): `scripts/report-check.mjs`(Node, 의존성 없음)가 보고 문안을 읽어
  결과 목록 유무·수정 줄 단어·목록 밖 검사 결과의 범위(크기×상태, 렌더/코드, 대조 결과)를 검사하고
  지적 줄과 종료 코드 1을 낸다. 보내기 전에 돌려 `ok`가 나올 때까지 문안을 고친다(SKILL 6단계,
  conformance). 글의 형식만 보고 숫자가 참인지는 판단하지 않는다. `tests/report-check.tests.mjs` 8건.
- 한 턴 12회 + 앞선 12회 재채점(F vs G): 12회 모두 스크립트를 돌렸고 맨 위 문장에 범위 없이 "통과"를
  쓴 보고는 F 3/12 → G 0/12, 지적을 받은 4건은 고쳐서 통과. 블라인드 통과 문장 범위·코드·렌더 구분
  F 7/12·7/12 → G 12/12·12/12. 대조 없는 '해결' 표기는 G도 0/12. 스크립트는 기존 보고 44건으로 다듬었고
  표현을 바꾸면 빠져나갈 수 있다. 롱텀 재측정 없음.
- 40턴 롱텀 재측정(2026-11-07~08, G 1세션 + B 재채점, 채점기 10): 통과 주장 범위 G 30/40 vs B 12/40(A 31/40),
  8개 전부 G 21/40 vs B 11/40(A 21/40), 함정 턴 전부 통과, 라이브 대조 20행 일치. 빈틈: 스크립트가 보낸
  보고가 아닌 뼈대 파일에만 돌아감(41/41), 검사 없는 턴은 스크립트·목록 생략(8/35), `changed`가 JOENESS
  해결 줄에 3회, JOEFLOW state 참조 0회. [기록](evals/check-coverage-20261104/longterm-G/).
- 보고 도장(2026-11-09, H안): `report-check.mjs`가 `ok`에 글자 수·SHA-256 앞 8자리를 찍고 보고가 그 줄로 끝남,
  `--verify`로 대조. 검사 없는 턴은 `design checks: none ran` 한 줄, R4(`changed` 수정이 해결 줄에 나오면 지적).
  SKILL.md 6단계·conformance.md 문구, 단위 테스트 11건. 10턴 1세션 + G 재채점: 도장 일치 8/8, 스크립트 8/8,
  보낸 글 지적 0/8(G 2/8), 블라인드 8개 전부 8/8(G 6/8). [기록](evals/check-coverage-20261104/longterm-H/).
- 문서 5개·스크립트 1개·테스트 1개 변경(2026-11-06은 문서 4개). 스키마·계약 유지. 버전은 2026-11-09에
  1.1.0으로 올림(위 절). 회귀 14/14, 11/11, 142 OK.

## README 영어 기본화 (2026-10-13, T042)

- 영어 설명 상단 배치 및 English·한국어 이동 링크 추가.
- 기존 한국어 본문·앵커·실행 명령 원문 보존. 영어 요청·보고 예시 번역.
- 기능·인계·지원 조건·한계 동일 유지. 한국어 전용 상세 링크의 언어 표시.
- README 및 현행 기록만 변경. 버전·기존 태그·개인 설치·실행 패키지 유지.

## 사용자 안내 문체 정비 (2026-10-13, T041)

- 대상: README·설치/복구·검증 안내. 보고서 구조·명사형 종결로 정비.
- README: 핵심 요약·설계 목적·주요 기능·사용 방법·도구 간 연결·한계 구성 적용.
- 도구 간 역할표 통일 및 설치 안내의 README 링크 앵커 갱신.
- 보존: 명령·프롬프트 예시, 지원 범위·검증 수치, 과거 기록, 실행 패키지,
  개인 설치, 기존 1.0.0 버전·태그. 코드·기능 변경 없음.

## 1.0.0 — 개인 설치 갱신·확인 (2026-10-13, T040)

- 사용자 승인으로 개인 설치도 0.3.0-dev에서 1.0.0으로 맞췄다. 검색 경로 밖에
  44개 파일을 백업하고 전체 해시 일치를 확인한 뒤 VERSION·발견 메타데이터만
  교체했다. 실행 코드와 기존 캐시를 포함한 나머지 42개 파일은 보존했다.
- 실제 설치 경로에서 version1.0.0·doctor 정상 종료와 전문 스킬의 실제 경로·해시를
  확인했다. host verifier는 UNAVAILABLE이며 자동 인증·전문 검수 수행을 뜻하지 않는다.
- 태그·GitHub Release는 세 실제 설치본 교차검증 후 Manager가 발행한다.
  [설치 영수증·백업·검증 한계](evals/v1-personal-install-20261013/README.md).
  아래 T039의 미설치 기록은 당시 상태다.

## 1.0.0 — JOE 도구군 사용 안내·패키지 버전 정리 (2026-10-13)

- JOEDESIGN의 역할을 “어떻게 보이고 사용될지 만들고 확인한다.”로 통일했다.
  README를 소개·사용 상황·시작·결과·도구 연결·지원 범위 6개 절로 정리하고,
  실제 설치 명령과 복사할 요청문, JOEFLOW/JOENESS의 전달 자료를 함께 안내한다.
- VERSION을 0.3.0-dev에서 1.0.0으로 올리고 발견 화면의 설명을 맞췄다.
  스킬 ID, 운영 코어, 실행 로직, JSON schema/contract와 F05 지원 범위는 유지한다.
- 설치·업데이트·구형 두 패키지 이전·백업/복구 및 검증 이력은 docs로 분리했다.
  기존 설치를 조용히 덮어쓰거나 Git 갱신을 개인 설치 갱신으로 취급하지 않는다.
- 이번 승격은 지원 범위의 패키지 정리다. 미확인 동적 의존성·CSS 정밀 분석,
  전문 판단·사용자 수락의 자동화를 주장하지 않는다. 과거 증거는 원래 버전에
  남긴다. 개인 설치·태그·GitHub Release는 별도 단계다.
  [1.0.0의 실제 검증·통합 기록](evals/v1-release-candidate-20261013/README.md).
- 후보7069f34의 저장소 검사와 Manager의 세 새 설치본 교차검토를 통과했다.
  일반 브랜치 푸시와 main 통합 대상으로 확정했으며, 원시 검증 로그·자료의
  줄바꿈과 공백은 Git 속성으로 보존한다. 개인 설치는 0.3.0-dev로 유지한다.

## 0.3.0-dev — F05 제한 영향 진단·검토된 증거 재사용 (2026-10-13)

- DESIGN 끝에 무관한 주석·절을 추가했을 때 기존 간격 검사를 무조건 다시
  촬영하던 문제에 대응했다. 원문 보존과 독립 의미 검토, 이전/현재 기준·검사·
  타깃·런타임·실제 제공 바이트·빌드·관찰 해시를 대조하는 `inspect-impact`를
  단일 코어의 내부 실행기에 추가했다. 별도 공개 스킬이나 CSS 분석기는 없다.
- 진단은 재사용 후보만 생산한다. JOENESS가 별도로 고정한 전환 검토를 소비해야
  기존 기하 검사를 재사용한다. 이전 receipt·캡처는 고치지 않으며 실패·반려·
  기준 완화·필수 검사 삭제·핀 누락·런타임 변경·미확인 의존성은 우회하지 않는다.
  전문 디자인 검토와 정확한 사용자 수락은 새로 충족해야 할 별도 조건이다.
- Python142·기존 Node14 회귀 통과. 실제 Edge 관찰 P01/P02에서 각4개 기하
  검사를 새 측정·PNG 없이 재사용하는 생산·소비 연결을 검증했다. 양쪽 격리본
  연결14개 기대 충족. Windows CRLF 절 추가를 차단한 초기 실패도 보존했다.
- 단일 정적 화면의 검토된 추가에 한정한다. 현재 응답 수집과 수동 검토 비용은
  남으며 총 시간 절감·동적 제품의 의존성 완전성·일반 시각 품질을 주장하지 않는다.
  버전은 `0.3.0-dev` 유지, 새 릴리스 태그가 아니다.
  [범위·실제 증거·검증과 설치 상태](evals/f05-impact-20261013/COMPLETION.md).

## 0.3.0-dev — main 통합 (2026-10-10)

사용자가 검증된 현재 작업을 커밋·푸시하고 main에 병합하도록 승인했다.
단일 운영 코어, 디자인 준수 생산자와 JOENESS 소비 연결, 실제 행동 검증을
함께 반영한다. 아래 각 단계의 변경 이유·실패·검증 한계는 그대로 보존한다.
이 통합은 새 릴리스 태그나 사용자 시각 수용을 의미하지 않는다.
실사용 피드백에서 재현되는 문제를 기준으로 후속 보강한다.

## 0.3.0-dev — 격리된 실제 에이전트 행동 검증 (2026-10-10)

- 제공 원본을 사용하는 신규 제작·중요 확장·국소 수정 3개 과제를 별도
  에이전트로 수행했다. 실제 전문 역할 검토와 독립 Critic, 브라우저 관찰을
  연결해 신규54·수정32·확장249개 필수 검사가 통과했다.
- 기준의 적용 대상 누락과 여러 페이지를 거치는 검사 입력 누락을 독립
  검토에서 보완했다. 시험 앱의 페이지 이동 시 예약 초기화를 발견·수정하고
  새 빌드에서 다시 검증했다. 이전108개 PASS는 새 빌드에서 모두 미확인으로
  차단됐다. 실패·수정·컨텍스트 이력은 보존했다.
- 이번 단계는 검증 자료와 오래된 상태 안내의 정리다. 코어 패키지28개 파일은
  변경하지 않았으며 설치·커밋·푸시·릴리스도 하지 않았다. 조정 담당자의
  기준 검토가 포함된 제한된 시험이며 일반적인 자율 준수나 사용자 수락을
  입증하지 않는다. [결과와 근거](evals/behavior-forward-20261010/README.md).

## 0.3.0-dev — 디자인 준수 판정과 JOENESS 소비 연결 후보 (2026-10-10)

- 후속 진행 지시로 이 PC의 단일 코어 설치를 전환했다. 기존 개인/프로젝트
  코어·Harness 59파일을 백업하고 새28파일 일치/의존성 검사를 확인했다.
  운영용51항목은 독립 범위검토를 받았으며 입력을174개에서 가족별15/16개로
  줄였다. 브라우저 응답과 파일 일치, 무관 변경 유지, 가족별·공유 변경 무효화를
  검증했다. 새 설치본으로 실제 GEO를 읽어51개 통과를 확인했다.
  소스 커밋·푸시·릴리스 및 전체 디자인 수락과는 별개다.
- 실제 CUA 연결에서 Windows 경로 표기 때문에 프레임 해시 조회가 실패한
  결함을 재현·수정했다. 원문 경로 키로 해시를 조회하고 파일 변조 거부는
  유지한다. 최종 Python130/Node14 및 설치본 실제 관찰 재검증 통과.

- 단일 운영 코어와 기존 검수·확장 흐름 안에 DESIGN 규칙 → 적용 대상 → 필수
  검사 → 실제 관찰의 결속을 추가했다. 별도 진행 원장이나 두 번째 스킬은 없다.
- 기준 파일은 소비 측에서 독립적으로 고정한 SHA256과 대조한다. 규칙·필수
  대상 삭제, 기준 완화, 승인 원본 변경을 기존 성공 판정으로 처리하지 않는다.
- 실제 브라우저 사각형의 연속 간격·요소 간 거리·자식 전체 영역의 내부 여백을
  측정한다. margin/padding/gap 중첩, 제어 높이, 줄바꿈과 자동 여백의 결과를
  검사하며 숫자는 각 프로젝트 기준에서 받는다. 반복 역할의 일관성도 검사한다.
- 필수 측정이 빠지거나 실패하면 일반 전문 검토가 모두 PASS여도 관련 단계와
  확장을 차단한다. 전문·독립 Critic 판정은 현재 기준·입력·캡처에 결속하며,
  기하 측정으로 전체 시각 품질이나 사용자 수락을 대신하지 않는다.
- `run`에 `design_validation` 입력을 요구하고 `verify-design` 명령을 추가했다.
  `DESIGN_CONFORMANCE-*.json` 결과를 JOENESS 소비자가 직접 읽을 수 있다.
  기준 pin·검사별 입력 fingerprint·캡처 시점 해시로 누락·낡거나 바뀐 근거를 검사한다.
- JOENESS는 이 결과의 수신·유효성·관련 완료 상태 통제를 소유한다. 실제 두
  소스 CLI를 연결해 실패 차단과 정상 복구를 검사했다. 설치본/프로젝트 활성화,
  파일 직접 수정·자연어 완료 우회 차단과 인증된 승인 권한은 별도다.
- [검증·연결 계약·남은 한계](evals/design-conformance-20261010/README.md).
- 추가로 GEO 실제 소스 사본의 9개 화면 조건/51개 간격 검사와 오류 주입을
  연결 검증했다. 텍스트 래퍼를 잘못 측정한 첫 실패를 보존하고 실제 텍스트
  경계로 바로잡았으며, 의미에 맞는 측정 대상 검토 지침을 보강했다.
  동일 대상 ID의 화면 폭·상태·경로 변경에도 과거 관찰을 거부하는 회귀를 추가했다.
  당시 Python129/과거 Node14 통과. 이 초기 사본 검증에서 남았던 입력 범위 축소·
  독립 기준 검토·운영 연결은 이후 위 후속 작업으로 완료했다.
  [초기 사본 검증 기록](evals/design-conformance-20261010/geo-validation.md)과
  [최종 운영 상태](evals/design-conformance-20261010/operational.md)를 구분한다.

## 0.3.0-dev — 단일 운영 코어 통합 후보 (2026-10-09)

사용자 지시: 하나의 운영지침 아래 여러 단계를 역할에 맞게 수행한다.
이 항목은 저장소 작업 브랜치의 새 통합 후보이며, 아래 main 반영 완료본과 구분한다.

- 외부 진입점을 `joedesign` 하나로 통합했다. 별도 `joedesign-harness` 스킬과
  호출 메타데이터를 제거하고 실행기·계약·템플릿을 같은 패키지로 이동했다.
- 최상위 SKILL.md가 작업 분류, 참조, 시각 번역, 대표 화면, 전문 검수, 확장,
  통합 관찰과 보고를 관리한다. 하나의 조정 담당자 A가 단계 전환을 책임진다.
- 과거 코어의 시각 해석·타이포·색상·공간·반응형·원본 비교 원칙은 내부
  `visual-translation.md`로 분리했다. 전문 역할은 배정받은 범위만 수행하며
  전체 운영을 다시 시작하거나 별도 방법론으로 전환하지 않는다.
- 실행기는 모든 역할에 동일한 운영 코어를 전달한다. J는 복사된 패키지 내부에서
  해석하며 전역에 남아 있는 구 코어를 불러오지 않는다. 외부 `skills.J` 재정의는
  거부하고 J의 작업에는 내부 시각 모듈을 함께 전달한다. 지침 변경 시 재개는 무효다.
- `doctor`와 실제 실행의 역할 탐색을 통일하고 `version` 명령과 단일 VERSION을
  추가했다. 버전은 `0.3.0-dev`이며 출시 태그나 품질 인증을 의미하지 않는다.
- 신규 설치 단위는 `skills/joedesign/` 폴더 전체다. CLI·수집기 경로를
  `joedesign/scripts/`로 바꾸고 기존 실행 설정의 외부 `skills.J`는 제거해야 한다.
  실제 설치 갱신 시 이전 `joedesign-harness` 설치본을 보존용 위치로 옮겨 발견
  경로에 두 진입점이 남지 않게 해야 한다. 이번 작업에서 기존 설치본은 변경하지 않았다.
- v0.2와 기존 Harness 패키지·원본 Node 테스트를 바이트 그대로 별도 보존했다.
  기존 Node 검사는 보존본의 과거 증거만 검사하며 새 통합본의 품질 증거로 사용하지 않는다.
  새 패키지 복사·역할 전달·실행 검사는 통합본을 대상으로 분리한다.
- 검증 범위와 결과는 [통합 검증 기록](evals/unified-core-20261009/README.md)에
  기록한다. 실제 에이전트의 새 지침 준수와 실프로젝트 시각 품질은 별도 검증 대상이다.

## 2026-10-09 — 실행 연동 및 디자인 작업 절차 보강

구성 버전: **JOEDESIGN 코어 v0.2 + Design Harness v0.1**. 이번 보강에 별도
버전 번호나 릴리스 태그를 부여하지 않으며 Git 커밋으로 소스를 식별한다.
사용자가 보강본의 커밋·푸시와 메인 병합을 요청했다. 기존 main은 초기 명세
단계였으므로 이번 통합에는 작업 브랜치에 누적된 코어 v0.2와 Harness 이력도
포함된다. 아래 날짜별 증거는 각각 당시 소스에 대한 기록이다.

### 디자인 작업의 핵심 절차

- 신규 방향, 중요한 확장·재설계, 승인된 관계를 보존하는 국소 수정을 구분한다.
  IA·화면 종류·콘텐츠 규모·과업 우선순위·주요 구도가 바뀌면 다시 판정한다.
  기존 색상·폰트를 유지했다는 이유로 구조 변경을 국소 수정으로 취급하지 않는다.
- 승인 범위에 충분한 원본은 재사용한다. 신규·중요 변경의 참조 결정이 미해결이면
  OMD에서 자료를 찾고 원본을 관찰해 Primary 하나와 역할이 다른 Secondary 최대
  둘을 정한다. 다른 검색 도구나 스킬의 기본 방식이 사용자 지정 방법을 대체하지 않는다.
- Product의 의미·필수 노출·중요도·상태를 시각 역할로 번역하고 root DESIGN.md에
  필요한 결정을 기록한다. 기능마다 새 색상·크기·간격을 만들지 않고 기존 역할을
  재사용한다. 승인된 값과 제안 값, 구현 허용과 시각 승인도 구분한다.
- 가장 큰 구도 위험을 드러내는 대표 화면을 먼저 제작하고 필요한 넓은 화면·좁은
  화면·상호작용 상태를 관찰한다. 낮은 충실도의 시안도 정보 위계는 검토해야 한다.
- 실제 전문 스킬을 적용한 R → C1 → 필요 시 C2와 독립 Critic 검토를 거친 뒤
  다른 화면으로 확장한다. 역할 이름만 붙인 일반 검토는 전문 스킬 사용의 증거가 아니다.
- 기능·정보 보존, 원본의 시각 관계 일치, 전체 화면의 디자인 적절성을 따로 판단한다.
  상품과 핵심 과업을 보조 메뉴·필터가 압도하는지, 밀도와 그룹 구성이 타당한지
  검토한다. 토큰 일치·빌드 성공·넘침 없음만으로 시각 품질을 통과시키지 않는다.
- 구조적 실패는 구도를 다시 설계한다. 미해결 필수 검수는 의존하는 확장을 막으며,
  확장 후에는 변경된 빌드에서 대표 화면을 포함한 전체 대상을 다시 관찰한다.
  직접 도구를 쓰거나 Git이 없는 프로젝트에도 같은 작업 순서를 적용한다.

### 로컬 실행기 및 검수 연동

- `harness_cli.py run`으로 기존 계약, 별도 Codex 프로세스, 브라우저 수집,
  R/C1/조건부 C2, 새 컨텍스트 Critic, 제한된 수정과 재개를 연결했다.
- 제작 실행에 `work_kind`와 `proof_target_ids`가 필요하다. 대표 대상은 한 화면
  계열에 계약된 모든 상태·화면 크기를 포함해야 하며, 누락·중복·잘못된 범위는
  쓰기 실행 전에 거부한다. 국소 수정 경로에 다른 화면 계열을 끼워 넣을 수 없다.
- 대표 대상의 구현·캡처·검수를 먼저 수행한다. 필수 FAIL/UNVERIFIED를 기술 항목의
  PASS로 상쇄하지 않으며, 검수 완료 후에만 확장 실행을 시작한다. 확장 검수는 새
  빌드의 모든 대상을 확인하고 보고서에 단계·검토 대상·미검토 대상을 남긴다.
- 모든 역할에 Harness 진입 지침과 담당 전문 스킬을 전달한다. 지침·계약·소스·
  캡처 식별자를 검사해 변경된 입력으로 과거 결과를 그대로 재사용하지 않는다.
- 완료 단계는 재개 시 반복하지 않는다. 확장 실패 뒤 대표 검수는 재사용하되
  증거가 변조·변경되면 거부한다. 중복 실행, 부분 수정 뒤 무분별한 재실행,
  구조 실패와 반복 미해결을 처리하는 중단 규칙을 유지한다.
- `--review-only`는 기존 구현을 새로 관찰·검토하며 쓰기 권한을 얻지 않는다.
  제작용 두 필드 없이도 전체 대상을 검토할 수 있다.
- 브라우저 수집은 실제 화면 크기·상태 조작·assertion·키보드 포커스·PNG와
  메타데이터를 기록한다. 연속 모션 품질 인증은 제공하지 않는다.

### 실행 병목과 관찰 오류 수정

- Codex 이미지 인자 뒤에 `--`를 넣어 stdin의 `-`가 이미지로 잘못 해석되는
  문제를 수정하고 동일 해시 이미지의 중복 첨부를 제거했다.
- 해시가 맞는 실제 수집 JSON과 계약 관련 소스를 검토 입력에 직접 전달해
  반복 읽기를 줄였다. 전문 스킬 원문·도구 접근·미관찰 항목의 UNVERIFIED 규칙은 유지한다.
- 잠긴 원본 인용과 현재 캡처 증거를 구분해 허용한다. 존재하지 않는 증거나
  현재 관찰 없이 원본만 인용한 PASS는 차단한다.
- 키보드 조작과 활성 요소·포커스 표시 관찰을 보완했다. 시간 초과 때는 시작한
  프로세스 트리를 종료하고 실패 기록을 보존해 해당 단계부터 재개할 수 있다.
  간헐적인 모델 응답 지연까지 해결됐다는 의미는 아니다.

### 검증 결과와 적용 시 주의

- 최신 자동 검사: **Python 112개 + Node 14개 = 126개 통과**, 생략 없음.
  범위·실행 순서·불확실성·재개·지침 변경의 회귀 검사와 합성 페이지의 실제
  Edge 캡처 검사를 포함한다. [최신 검증 기록](evals/design-workflow-20261009/README.md).
- 10월 6일 합성 사례에서 실제 Codex R 5회, C1 4회, Critic 1회의 검수를 완료했다.
  상태는 `REVIEW_COMPLETE_UNCERTIFIED`, `approved=false`였다. 이전 실패와
  시간 초과·재개 기록을 보존했다. 이는 10월 9일 새 작업 절차의 실제 모델 준수
  증거가 아니다. [병목 보강 기록](evals/harness-bottleneck-20261006/README.md),
  [선행 실패·수정 기록](evals/harness-execution-20261006/README.md).
- 기존 제작용 실행 설정은 `work_kind`와 `proof_target_ids`를 명시해야 한다.
  예전 실행 기록을 새 정책의 성공 증거로 바꾸지 않는다.
  [실행 설정·마이그레이션](skills/joedesign-harness/references/execution.md).
- 코어 `skills/joedesign/`의 바이트, 역사적 증거, 기존 개인 설치본과 제품 프로젝트는
  이번 보강에서 변경하지 않았다. Git 업데이트만으로 설치본이 갱신되지는 않는다.
- 최신 절차에 대한 실제 모델 준수, 실프로젝트 디자인 품질, 전문 검수의 판단 정확도,
  연속 모션 품질과 사용자 수용은 별도 검증 대상이다. 로컬 실행기는 자신의 실행
  순서만 통제하며 외부 에이전트의 임의 편집이나 역할의 실제 준수를 인증하지 않는다.
  인증된 호스트 receipt와 자동 최종 APPROVED는 제공하지 않는다.
- 채택되지 않은 관계 진단·의존성 검사 실험은 복원하지 않았다.
  [기존 채택 판단](evals/harness-v0.1/retention-decision.md)을 유지한다.

### 메인에 함께 포함되는 기존 기반

코어 v0.2는 Product 의미와 승인된 시각 원본의 관계를 구현으로 번역하는 역할을
유지한다. 별도 Harness v0.1은 참조 검색·선택, 계약·상태·증거 연결, RACI 경로,
재작업 및 승인 정책을 제공한다. 메인 병합은 이 이력과 최신 보강을 통합하는
소스 관리 작업이며, 과거 후보 기록이나 제한된 검증을 제품 출시 인증으로 바꾸지 않는다.
기존 설계·검증 기록은 [README](README.md)에서 각 근거로 연결한다.
