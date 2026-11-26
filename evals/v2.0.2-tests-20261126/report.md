# JOEDESIGN 2.0.2 후보 준비 (2026-11-26, T045)

**결론:** ATELIER 실사용(2026-11-23~25) 마찰 중 사용자가 2026-11-26에 확정한 일곱 항목(묶음 H·I, 그 뒤 JOEDESIGN 줄 다섯)을 모두 구현하고 문서화했다. 커밋은 브랜치 `v2.0.2`에 로컬로만 했다(push·태그·Release·설치 없음). node 60/60(5번 결정 반영 뒤), python 150 OK(건너뜀 2). report-check 회귀 274개는 v2.0.1과 지적이 같고 바뀐 파일은 0이다. 행동 시험은 0회다.

입력: `ATELIER/TOOL-FRICTION.md` JOEDESIGN 줄 7개(2026-11-23~25), `ATELIER/Library/tool-friction-review.md` 묶음 H·I. ATELIER는 읽기만 했다. 캡처 1장과 보고 두 건을 복사해 fixture로 썼다(아래).

## 항목별 처리

| # | 항목 | 처리 | 확인 |
|---|---|---|---|
| 1 | H 색·모션의 직접 관측 | SKILL.md 새 절 "Direct observation of colour and motion". 어느 픽셀(획 중앙 행), 배율(DPR 2 원본 또는 2x 줌), 허용 오차(채널 ±8 그리고 대비 ±0.2, 2026-11-26 사용자 결정), 기록 형식 `median M, range a–b, n px`을 정했다. `scripts/sample-pixels.mjs`(Node만, zlib로 PNG 해독)를 넣었다. reduced-motion은 에뮬레이션이 기본이다. 안 되면 "페이지 자체 reduce 규칙을 조건 없이 주입"을 대체 관측으로 인정하고 `rendered (reduce injected)`로 적는다. DESIGN Report Form에 두 문장 | ATELIER 캡처 `scr002-360x640-soldout-chips-M-L.png`(fixtures/sample-pixels/): M 칩 획 행 `median #8E8E8E, range 118–158, n 12 px`, 범위는 ATELIER 기록(118–158)과 같다. `#8A8A8A` within, 수정 전 색 `#9A9A9A` outside. CDP 캡처(DPR 2)한 `#8A8A8A` 칩: `median #8A8A8A, range 138–179, n 30 px`, diff 0. 테스트 8개(그리고 판정 1개 포함) |
| 2 | I report-check R5 | 쌍의 줄 끝이 `decided in rev N DEC-xxx`(리비전과 결정·레코드 ID)이면 정의가 정한 변화로 인정한다. `rev19 DEC-061에서 결정`, 쌍 줄 자체의 `product decision pending`도 인정한다. 지적 문구에 그 형식을 넣었다. SKILL.md 한 구절, DESIGN Report Form 한 문장과 예시 | ATELIER Stage 1 보고 재구성 fixture: 표지 없음 → R5(2.0.1·2.0.2 둘 다), `— decided in JOEFLOW rev19 DEC-061` → 2.0.1 R5, 2.0.2 ok. `decided in JOEFLOW`(리비전·ID 없음) → 여전히 R5. 테스트 4개 |
| 3 | 출처 관측 범위 | DESIGN 템플릿 Visual Sources에 출처 표를 넣고 `Observation scope (per state)` 열을 필수로 했다(관측 상태 → 결정, 미관측 상태 → 유도 근거). SKILL.md 1단계에 일부만 관측됐을 때 진행 방법(관측분과 명시한 유도로 진행, 미관측은 증거 경계에, 반하는 관측이 나오면 재개) | 문서. 행동 시험 0회 |
| 4 | report-check R3 | `AC:`로 시작하는 줄(`AC-004:`, `AC-004, AC-007:`, `수용 기준:`)과 AC 제목(`## AC …`, `## 수용 기준`, `acceptance`) 아래 같은 수준 다음 제목까지는 R3이 읽지 않는다. 기술 검사 낱말 확장: typecheck, `validate-*`, pytest, 통합 테스트 등. 둘 다 디자인 검사 낱말이 있으면 다시 읽는다. 지적 문구에 `AC:` 안내를 넣었다. SKILL.md 6단계·Report Form 한 문장 | ATELIER Stage 3 보고 재구성 fixture: 접두어 없는 AC 문장 → R3(2.0.1·2.0.2 둘 다, 2.0.2 문구에 `AC:` 안내), `AC:` 접두 → 2.0.2 ok, `## AC observation` 절 → 2.0.2 ok, 실제 보낸 글은 둘 다 ok. 테스트 4개 |
| 5 | 전문 스킬 | SKILL.md "Specialist skills" 문단: 설치 위치 네 곳, 다른 설치본의 SKILL.md를 하위 에이전트가 읽어 적용(경로·SHA-256 기록), 어디에도 없으면 `not run`. 3단계: 규칙 행은 덮는 크기마다 전 화면 캡처 1장 이상. `doctor` 기본 탐색에 `~/.claude/skills` 추가, 없는 전문 스킬은 `missing_specialists`로 안내 | 테스트 1개(가짜 홈 `.claude/skills` 발견, `missing_specialists` 문구). doctor 전후(아래) |
| 6 | Playwright 없는 수집기 | `scripts/capture-cdp.mjs`: 설치된 Chrome/Edge를 DevTools 프로토콜로 헤드리스 구동한다(`executable` → `CHROME_PATH` → 일반 설치 경로, 포트 0, 새 임시 프로필, Node 22+). capture.mjs 요청·결과 계약을 그대로 받고(`capture.mjs`가 Playwright를 못 찾으면 넘김), 직접 모드는 크기·DPR·전 화면·reduced motion(emulate/inject)을 지원한다. 로컬 루프백·file:만 연다. ATELIER `scripts/design-checks/cdp.mjs`가 씨앗이다. SKILL.md 실행 지원 문단, doctor `collector` 블록, INSTALL·QUICKSTART | 픽스처 페이지와 ATELIER 빌드 클라이언트(`client/dist`, 정적 서버, 읽기만)에 실행했다. 캡처 보관: `collector/`. 실제 브라우저 테스트 1개(대체 경로, Tab·Enter, 단언, reduce inject 1규칙, 실패 단언) |
| 7 | 규칙 표 증가 | SKILL.md 3단계·템플릿 Rule coverage 주석: 규칙당 한 행, 개정이 넓힌 화면·상태는 그 행 목록에 개정 표시와 함께 더한다, 기준이 바뀌면 Rule 칸 수정, 재실행은 "바뀐 파일이 그리는 화면을 가진 모든 행". conformance.md 새 절 "Rule rows across revisions"에 ATELIER 예시(T1 세 행을 한 행으로) | ATELIER 42행 중 T1·C1·S1·M1·M2가 Rev 2/3/4로 15행, 합치면 5행, 표 32행(아래 계산). 문서. 행동 시험 0회 |

## 명령과 출력

모두 저장소 루트에서 실행했다(Windows, Node 26.3.0, Python 3.14, Chrome 158).

| 명령 | 결과 | 기록 |
|---|---|---|
| `node --test tests/*.tests.mjs` | 60/60, 2026-11-26 5번 결정 반영 뒤 재실행(2.0.1의 44 + report-check 8 + sample-pixels 8). [node-tests.txt](node-tests.txt)는 결정 전 59/59 실행 기록이다 | [node-tests.txt](node-tests.txt) |
| `python -B -m unittest discover -s tests` | 150 OK, 건너뜀 2(2.0.1의 147 + doctor 2 + CDP 수집 1. 건너뜀은 기존 2개: Playwright 수집 시험, 브라우저 렌더 conformance 시험. 둘 다 환경 변수로 켜는 시험) | [python-tests.txt](python-tests.txt) |
| `node evals/v2.0.2-tests-20261126/regress.mjs` | 274개: v2.0.1 `{"R3":269,"R5":44,"R1":75,"R6a":103,"R4":4,"R2":3,"R6b":7}`, 후보 같음, 바뀐 파일 0. fixture 8개: v2.0.1 R5 3·R3 3 → 후보 R5 2·R3 1 | [regress-274.txt](regress-274.txt), [regress-changes.tsv](regress-changes.tsv) |
| `sh evals/v2.0.2-tests-20261126/collector/run.sh` | 아래 수집기 절 | [collector/run-output.txt](collector/run-output.txt) |
| `python -B skills/joedesign/scripts/harness_cli.py doctor` 전(10671e5)·후 | 아래 doctor 절 | [doctor/](doctor/) |

part19 회귀(`evals/check-coverage-20261104/part19/regress.mjs`)는 돌리지 않았다. 그 스크립트는 자기 출력 파일을 덮어쓰고 v1.3.3과 비교한다. 대신 같은 274개 목록으로 v2.0.1 태그와 비교하는 `regress.mjs`를 이 폴더에 두었다.

## sample-pixels (항목 1)

```text
$ node skills/joedesign/scripts/sample-pixels.mjs fixtures/sample-pixels/scr002-360x640-soldout-chips-M-L.png --region 0,0,78,44 --expect '#8A8A8A'
median #8E8E8E, range 118–158, n 12 px (row 22, bg #FFFFFF, contrast 3.28)
expect #8A8A8A: channel diff 4 / contrast diff 0.18 -> within (±8 and ±0.2)
$ ... --expect '#9A9A9A'
expect #9A9A9A: channel diff 12 / contrast diff 0.46 -> outside (±8 and ±0.2)   (종료 코드 1)
```

- 캡처는 160×44 RGB, 1x(ATELIER가 DPR 2 렌더를 내장 브라우저 zoom으로 1x 재표본한 것)다. 획 행은 22행 하나이고 그 행 잉크 픽셀 12개의 범위가 ATELIER가 .NET으로 읽은 118–158과 같다. 중앙값은 짝수 개라 가운데 두 값(140, 143)의 평균을 반올림해 142(#8E)다. ATELIER는 141을 적었다(가운데 값 고르는 방식 차이로 보이며 확인하지 않았다).
- 기본 문턱은 배경과 채널 차 40 초과다. 칩 테두리 `#E5E5E5`(차 26)는 배경으로 남아 영역 없이 전체 이미지를 줘도 22행을 고른다(테스트).
- 칩 L 영역(82,0,78,44)은 `median #8F8F8F, range 121–198, n 8 px`이다. `#8A8A8A`는 diff 5 / 0.22로, 대비가 0.2를 넘어 outside다("그리고" 판정. 결정 전 "또는"에서는 within). `#9A9A9A`는 outside(diff 11 / 0.42)다. 테스트는 칩 M만 단언한다.
- [collector/run-output.txt](collector/run-output.txt)의 sample-pixels 줄은 결정 전 실행이라 `(±8 or ±0.2)` 문구가 남아 있다. 그 두 판독(diff 0 / 0.00)은 "그리고"에서도 within이다.

## 수집기 (항목 6)

서버 두 개를 띄우고 [run.sh](collector/run.sh)를 실행했다. 8731은 `fixtures/capture-cdp/`, 8732는 ATELIER `client/dist`다. ATELIER 폴더에는 아무것도 쓰지 않았고, 실행 뒤 `git status`가 깨끗했다. 이 저장소에는 Playwright 패키지가 없어 `capture.mjs`가 `capture-cdp.mjs`로 넘겼다.

| 실행 | 결과 | 파일 |
|---|---|---|
| 직접 모드, 픽스처, 1024x768·360x640, DPR 2 | 2048×3408, 720×3408 PNG. 스타일시트 1개 로드, 애니메이션 `rise 0.6s`, reduce false | `collector/fixture/fixture-*@2x-full.png`, `fixture-summary.json` |
| `--reduce-motion emulate` | `matchMedia(reduce)` true, 애니메이션 none | `fixture-reduce-emulate-*` |
| `--reduce-motion inject` | 주입 규칙 2, 읽지 못한 시트 0, 애니메이션 none, `matchMedia(reduce)` false(조건 없이 주입했으므로) | `fixture-reduce-inject-*` |
| `capture.mjs < request.json`(Playwright 없음 → CDP) | 오류 0. 360x640: Tab·Enter 뒤 focus `BUTTON#chip-s` `:focus-visible`, `#state` "S 선택됨". 1024x768: `reduced_motion: "injected"`, 규칙 2 | `collector/request-out/`(관측 JSON의 절대 경로는 `<repo>`로 가림) |
| 직접 모드, ATELIER `client/dist`, 1024x768·360x640 | 자체 스타일시트 2개 로드(Pretendard, `index-*.css`). API 서버가 없어 카탈로그는 "상품을 불러올 수 없습니다" 오류 상태 | `collector/atelier-dist/` |
| sample-pixels, 픽스처 DPR 2 캡처의 칩 M(200,236,128,76) | 두 크기 모두 `median #8A8A8A, range 138–179, n 30 px`, diff 0 | run-output.txt |
| `--url https://example.com/` | 거부: `Collector only operates an explicitly configured local preview`(종료 코드 2) | run-output.txt |

ATELIER 빌드 클라이언트는 편집 없이 정적으로만 띄울 수 있었다. 그래서 상품·주문 API가 필요한 화면(카탈로그 목록, 상세, 장바구니)은 찍지 못했다. 서버(`server/`)는 데이터 파일을 쓸 수 있어 실행하지 않았다.

## doctor 전후 (항목 5·6)

홈 경로는 `~`, 이 워크트리는 `<repo>`로 가렸다([before.json](doctor/before.json), [after.json](doctor/after.json), [after-empty-skills-root.json](doctor/after-empty-skills-root.json)).

- 전(10671e5, 2.0.1): 종료 0, 전문 스킬 5개 AVAILABLE(`~/.agents/skills/impeccable`, 나머지 `~/.codex/skills`).
- 후: 종료 0. 바뀐 것은 `version` 2.0.2, `joedesign` SKILL.md 해시, 새 `collector` 블록(`route: "cdp"`, `cdp_browser` Chrome 일반 설치 경로(`<ProgramFiles>`로 가림), `playwright: null`, `chrome_path_env: "UNSET"`)이다.
- 후, `--skills-root <빈 폴더>`: 종료 2, `ready_for_synthesis: false`, `missing_specialists`에 다섯 이름과 하위 에이전트 대체 경로 문장.
- 이 기계에서는 `~/.claude/skills`에 전문 스킬이 없어 새 기본 경로가 결과를 바꾸지 않았다. 발견은 가짜 홈 테스트로만 확인했다.

## 규칙 표 병합 계산 (항목 7)

ATELIER `DESIGN.md` Rule coverage 표를 읽어 첫 칸의 규칙 ID로 묶었다(읽기만).

- 42행. ID가 같은 규칙이 개정별로 여러 행인 것은 T1, C1, S1, M1, M2이고 각각 Rev 2·Rev 3·Rev 4 세 행으로 15행이다.
- 합치면 5행, 표는 42 − 10 = 32행이 된다. C1F(Rev 5)는 다른 규칙이라 따로 둔다.
- T1 세 행의 Layouts·States·Spot check·Unmeasured를 이어 붙인 한 행을 conformance.md 예시로 실었다. T1 Rev 2 행의 Result 칸에 "the first Rev 5 build failed dots"가 있어, Rev 5 변경이 Rev 2 행을 깬 사례를 확인했다.

## SKILL.md 문구 변경 요약

전체 diff: [skill-md.diff](skill-md.diff)(v2.0.1 대비). 크기 14,766B → 18,390B(+3,624B), 허용 오차 결정 반영 뒤 18,452B. skill-md.diff는 결정 전 diff이고, 그 뒤 색 관측 절의 "or"가 "and"로 바뀌었다(아래 "사용자 확인이 필요한 것" 5번).

| 위치 | 2.0.1 | 2.0.2 | 항목 |
|---|---|---|---|
| "One owner, bounded roles" 표 아래 | 없음 | **Specialist skills** 문단: 네 설치 위치, `doctor`가 목록, 다른 폴더의 SKILL.md를 하위 에이전트가 읽어 그 주장에만 적용하고 경로·SHA-256 기록, 어디에도 없으면 `not run` | 5 |
| "Decide the scope" 표시 전후 문단 | 다른 쌍은 대기, 같은 쌍은 디자인 결정 | + 정의가 이미 정한 다른 쌍은 after 줄 끝 `decided in rev N DEC-xxx`, 대기 아님 | 2 |
| 1단계 Establish the source | 소스가 없으면 의존 작업 미해결 | + 일부 상태만 관측된 경우: 출처 표 관측 범위 열에 상태별 기록(관측 → 결정, 미관측 → 유도 근거, 관측으로 적지 않음), 관측분과 유도로 진행, 미관측은 증거 경계, 반하는 관측이 나오면 재개 | 3 |
| 3단계 Rule coverage | 행마다 spot check | + 규칙당 한 행(개정 확장은 목록에, 기준 변경은 Rule 칸 수정), 바뀐 파일이 그리는 화면을 가진 모든 행 재실행, 크기마다 전 화면 캡처 1장 이상 | 7, 5 |
| 6단계 보고 | 목록 밖 통과 문장엔 괄호 | + AC 결과는 디자인 검사가 아님: `AC:` 줄 또는 AC 제목 아래, 괄호 규칙 밖 | 4 |
| 새 절 "Direct observation of colour and motion" | 없음 | 획 중앙 행, DPR 2 또는 2x 줌, `sample-pixels.mjs` 명령, `median M, range a–b, n px` 기록과 예, ±8/±0.2, reduced-motion 에뮬레이션 → 안 되면 reduce 규칙 주입 `rendered (reduce injected)`, 규칙 읽기만은 `code` | 1 |
| "Execution support" | Playwright 수집기만 암시 | + capture.mjs가 Playwright 없으면 capture-cdp.mjs로, 직접 모드 명령, 설치 없음, doctor가 경로 보고 | 6 |

템플릿(`templates/DESIGN.md`)은 출처 표와 관측 범위 열, Rule coverage 주석의 병합·재실행·전 화면 캡처·병합 예, Report Form의 `rendered (reduce injected)`·색 기록 형식·AC 줄·`decided in` 예를 바꿨다. `references/conformance.md`는 report-check 설명 한 문단과 새 절 "Rule rows across revisions"를 바꿨다.

## Fixture 출처

- `fixtures/sample-pixels/scr002-360x640-soldout-chips-M-L.png`: ATELIER `work/captures/2026-11-24/`의 같은 파일을 그대로 복사했다(1,977B).
- `fixtures/report-check-202/stage3-*.md`: ATELIER `work/reports/2026-11-24-stage3.md`, 도장 줄은 뺐다. `stage3-sent.md`는 실제로 보낸 글이다. 초안 문장은 TOOL-FRICTION.md 2026-11-24 R3 줄을 보고 **재구성**했다. ATELIER에 초안이 남아 있지 않다. 원래 문장 "... carried over pass on screen as written (table in ...)"은 보낸 글의 우회 괄호를 원래 표현으로 되돌린 것이다.
- `fixtures/report-check-202/stage1-*.md`: ATELIER `work/reports/2026-11-24-stage1-finish.md`. 보낸 글은 쌍을 빼고 산문으로 적었다. `## Display before/after` 쌍과 "merged …" 문장은 마찰 줄과 보낸 산문으로 **재구성**했다.
- 재구성한 fixture는 "같은 문장이 2.0.1에서 지적되고 2.0.2에서 어떻게 되는가"만 보인다. 사용자가 실제로 쓴 초안 바이트와 같다는 증거는 아니다.

## 확인되지 않은 것

- **행동 시험 0회.** 새 문구(관측 절차, 관측 범위 열, 전문 스킬 대체 경로, 규칙 병합, AC 접두어)가 에이전트 행동을 바꾸는지 시험하지 않았다.
- ATELIER의 API가 필요한 화면을 CDP로 찍는 것. 정적 빌드의 오류 상태 화면만 찍었다.
- macOS·Linux의 브라우저 자동 탐색 경로(코드만 있고 실행 안 함), Edge 단독 환경(이 기계는 Chrome을 먼저 찾음).
- 16비트·인터레이스 PNG: 의도적으로 거부한다. 다시 저장하라는 안내만 하고 해독하지 않는다.
- `capture-cdp.mjs`의 `fill`·`hover`·`scroll` 동작은 코드만 있다. 실제 브라우저로는 `press`, 단언, reduce, 전 화면만 시험했다. `click`은 직접 시험하지 않았다(Enter로 눌렀다).
- R5 대기 표기가 보고 전체 단위인 점(아래 "남은 약점")은 그대로 뒀다.

## 남은 약점 (범위 밖, 기록만)

- R5의 `product decision pending`은 보고 어디에 있든 모든 다른 쌍을 통과시킨다. ATELIER Stage 3 보고의 `decided in JOEFLOW rev20 SCR-004` 쌍은 2.0.1에서도 통과했다. 그 쌍 때문이 아니라 남은 문제 줄의 "제품 결정 대기 2건" 때문이다. 2.0.2는 쌍 줄 단위 표기(`decided in …`, 줄 안의 pending)를 더했지만, 전체 단위 인정은 274개 회귀를 바꾸지 않으려고 남겼다.
- AC 문장을 접두어 없이 쓰면 여전히 R3이다. 문장 내용(AC-ID + "sentence passes")으로 자동 판별하는 방법은 오탐 위험이 있어 넣지 않았다. 지적 문구가 `AC:`를 안내한다.

## 사용자 확인이 필요한 것

사용자 결정(2026-11-26, 부모 세션에 "추천대로 게시"): 아래 6건 중 1·2·3·4·6은 그대로 확정했고 5번만 바꿨다. 바꾼 5번은 결정 뒤 커밋 하나로 반영했다.

1. **R5가 인정하는 ID 범위 — 확정.** `DEC-061`만이 아니라 `[A-Z]{2,6}-숫자` 레코드 ID(예 `SCR-004`)도 받는다. ATELIER Stage 3이 `decided in JOEFLOW rev20 SCR-004`를 썼다.
2. **쌍 줄 안의 `product decision pending`도 인정 — 확정.** after 줄 끝에 대기를 적는 형식(ATELIER slice-proof)을 기록으로 본다.
3. **doctor 기본 탐색에 `~/.claude/skills` 추가 — 확정.** 러너(`run`)의 전문 스킬 해석도 같은 함수라 함께 바뀐다(마지막 순위).
4. **SKILL.md +3.6KB — 확정.** 일곱 항목 문구를 줄이지 않고 둔다.
5. **허용 오차 의미 — 바뀜.** 처음 안은 "채널 ±8 **또는** 대비 ±0.2"였다. 결정은 "채널 ±8 **그리고** 대비 ±0.2"로, 둘 다 맞아야 within(agree)이다. 이유는 "또는"이면 명도가 같은 색상 변화(회색 ↔ 푸른 회색)가 통과하기 때문이다. 반영한 곳:
   - `sample-pixels.mjs`의 판정과 출력 `-> within (±8 and ±0.2)`, SKILL.md 색 관측 절, 템플릿 Report Form 한 문장.
   - 테스트 1개를 더했다. M 칩(4 / 0.18)은 within이다. 채널만 넘는 경우(푸른 회색 `[138,138,156]` 대 `#8A8A8A`)와 대비만 넘는 경우(`#282828` 대 `#202020`)는 outside다.
   - 결과가 바뀐 판독이 하나 있다. 칩 L(8 px, diff 5 / 0.22)은 "또는"에서 within이었고 이제 outside다. ATELIER가 근거로 쓴 칩 M은 그대로 within이다.
6. **CDP 수집기의 `mobile` 에뮬레이션 끔 — 확정.** capture.mjs(Playwright)와 같게 데스크톱 뷰포트 크기만 바꾼다.

## 쓴 경로

이 워크트리 안만 썼다(커밋된 파일). scratchpad에는 doctor 원본 출력과 가림 스크립트를 두었다. ATELIER는 읽기와 `client/dist` 정적 제공만 했다. `~/.codex/skills`, 작업 폴더의 `.local`·`.claude/skills`, 주 체크아웃에는 쓰지 않았다. doctor가 실제 홈의 전문 스킬 SKILL.md를 읽어 해시를 냈다. 2.0.1과 같은 읽기 동작이다. 헤드리스 Chrome은 실행마다 OS 임시 폴더에 프로필을 만들고 끝나면 지운다.
