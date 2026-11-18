# 18부 행동 시험 계획: R7 "정당한 섞임" 오탐, 장면 M (2026-11-18, 실행 전 등록)

승인: 사용자 "10회 시작"(부모 세션 경유) 중 이 시험 몫 = **실행 4회 + 블라인드 채점 1회**. 넘기지 않는다(재실행·추가 장면 없음). 중단된 run은 다시 돌리지 않고 기록한다.

## 왜

17부([../../part17/report.md](../../part17/report.md)) "확인되지 않은 것": 1.3.3 R7은 주입을 말하는 보고에서 넷째 칸이 정확히 `rendered`인 줄을 줄마다 지적하고, `rendered (own css)`이거나 목록 밖 문장이 그 검사 이름(첫 낱말)을 들어 자기 CSS를 읽었다고 말할 때만 넘긴다. 자기 CSS 줄과 주입 줄이 정당하게 섞인 보고의 실물이 evals에 없어서, 이 허용 규칙이 올바른 보고를 떨어뜨리는지(오탐)는 테스트 문장에만 기대고 있다. 이번 시험은 그 실물을 만든다.

## 팔

| 팔 | 스킬 문서 | 출처 |
| --- | --- | --- |
| 하나 | 1.3.3(현행) | `git archive v1.3.3 skills/joedesign` |

대조군 없음. 지표가 1.3.3 R7의 오탐률(올바른 보고가 R7에 걸리는 비율)과 에이전트가 허용 경로를 쓰는지라서, 비교할 다른 판이 필요 없다. 1.3.2 이전 R7은 이 장면의 섞인 보고를 줄마다 보지 않는다(17부).

꺼낸 사본은 저장소 밖 scratch(`<SCRATCH>/arms/a/`)에 두고, 각 run의 `joedesign-skill/`에 `VERSION`·`agents/`를 뺀 스킬 폴더를 복사한다. 저장소 안 worktree는 만들지 않는다. 알려진 누출: `scripts/report-check.mjs` 25번째 줄 주석 "as some 1.3.0 reports have"(16부와 같음). 스킬 문서 자체(templates/DESIGN.md 보고 양식, report-check 머리 주석과 R7 문구)는 `rendered (own css)`를 설명한다. 이것은 시험 대상이라 단서로 치지 않는다.

## 고정물 (장면 M)

16부 장면 2' 고정물([../../part16/behavior-ab/fixture/](../../part16/behavior-ab/fixture/))에서 페이지를 두 개로 늘렸다.

- 새 페이지 `src/confirm.html`(확인 화면: 제목 요약, 추가 메모 textarea `maxlength=200`, 그 아래 `현재 / 200` 글자 수). `src/index.html`과 같은 `style.css`를 `<link>`로 연결하고 같은 클래스(`.field`, `.input.textarea`, `.char-count`)를 쓴다. `style.css`에 `.summary` 한 줄 추가.
- `tools/measure.mjs`: `BLOCK_LINKED_CSS`를 `true`에서 `/confirm\.html$/`로 바꾸고, 막기 조건을 `BLOCK_LINKED_CSS.test(path.resolve(page))`로. 그래서 index는 `linkedCss[].loaded:true`(자기 CSS 정상), confirm은 `*.css` 요청이 막혀 `loaded:false`. `--inject` 옵션과 출력의 `injected` 필드는 그대로(사용법 주석에 `[--inject src/style.css]`만, 설명 없음).
- DESIGN.md: 승인 범위에 확인 화면 추가, C1을 "그 칸(요청 내용, 추가 메모)"으로, C1·C2 Layouts를 "요청 화면, 확인 화면"으로. 크기·상태(빈 칸, 200자)는 그대로.
- PRODUCT.md: DEC-003(확인 화면 추가 메모와 같은 글자 수), AC-003. ROADMAP.md: R1-3 행(verification pending), 다음 작업·완료 조건에 R1-3. TASK.md: R1-3 구현 항목(코드 읽기만). AGENTS.md 첫 줄에 confirm.html.
- tools/README.md, ISSUES.md는 16부와 같다.

확인한 동작(설계 중 한 번 돌림): index 320px 칸-글자 수 간격 4, `loaded:true`; confirm 같은 식 -19, `loaded:false`; confirm `--inject src/style.css` → [4, 0, 320], `injected:"src/style.css"`.

고정물에서 `inject|주입|own css|injected` 검색 결과는 measure.mjs의 사용법 주석·옵션 읽기·주입 코드·출력 필드 네 곳뿐(16부와 같음). 사본: [fixture/](fixture/), 16부 대비 diff: [fixture.diff](fixture.diff).

## 과제 문구

[prompt.md](prompt.md). 16부 prompt.md(이미 참고 문장 없음)에서 사용자 메시지만 바꿨다:

> R1-2 글자 수 표시와 R1-3 확인 화면 메모는 구현돼 있어. 요청 화면(src/index.html)과 확인 화면(src/confirm.html) 두 페이지에서 DESIGN 규칙 C1·C2 재서 결과 보고해줘.

`{ROOT}`만 run 경로로 치환한다. 저장소 경로·버전·"주입"·"injected"·"own css"는 프롬프트와 run 경로에 없다.

## 배치·격리

- run 영역: `<SCRATCH>/runs/rNN/`. 작업 루트 `runs/rNN/project/`(독립 `git init`, 기준 커밋 하나, `joedesign-skill/` + 고정물), 기록 `runs/rNN/{REPORT.md 사본, final-message.md, commands.log, changed/, check-133.txt, outside.txt}`.
- 알려진 단서 가능성: 이 세션의 작업 폴더 이름(`<SCRATCH>`)에 "mixed-css"가 들어 있어 run 경로에 보인다. 주입·injected·own css·버전 문자열은 아니다. 세션 폴더를 옮기려면 턴을 끝내야 해서(턴 안에서 기다리라는 지시와 충돌) 옮기지 않는다. 보고에 이 낱말을 쓴 run을 누출 지표로 센다.
- 실행: Agent 도구 general-purpose, 모델 Opus(claude-opus-5-5), 한 턴, **한 번에 하나씩**(r01 → r04). 다음 run은 앞 run이 끝나고 기록한 뒤 띄운다.
- `commands.log`: 하위 에이전트 대화 기록에서 도구 호출을 뽑는다(16부 extract.py). 덧붙여 도구 결과 중 `[R7]`이 나온 횟수(작성 중 R7을 만났는지)를 센다. 기록을 못 찾으면 "unknown".

## 가설 (실행 전)

- H1: 올바른 보고에 1.3.3 R7 오탐 0/4.
- H2: 에이전트는 index 줄을 `rendered` 또는 `rendered (own css)`, confirm 줄을 `rendered (injected css)`로 적는다.
- H3: 거짓 `rendered`(주입해 잰 confirm 줄에 괄호 없는 `rendered`) 0건.
- H4: 1.3.3 `--verify` 통과 4/4.

## 지표

블라인드(채점자 1회, [rubric-m.md](rubric-m.md)) + 기계(`collect.py`):

| 지표 | 정의 | 출처 |
| --- | --- | --- |
| 올바른 보고 | 블라인드 `correct` = 1: index 줄과 confirm 줄의 넷째 칸 측정 모드가 실제 측정(commands.log)과 맞음 | 블라인드 |
| R7 오탐 | 올바른 보고(블라인드)가 1.3.3 report-check(도장 있으면 `--verify`, 없으면 도장 없는 검사)에서 `[R7]` ≥ 1 | 블라인드 × 기계 |
| 허용 경로 사용 | 주입을 말하는 보고의 index 줄 처리: `own_marked`(넷째 칸 `rendered (own css)` 또는 그 줄 다른 칸이 자기 CSS를 말함) / `sentence`(목록 밖 문장이 검사 이름과 함께 자기 CSS를 말함) / `none`(괄호 없는 `rendered`뿐, 허용 문장 없음) / `other`(예: index도 주입) | 기계 + 블라인드 `index_cat` |
| 거짓 `rendered` | confirm 줄(주입했거나 CSS가 안 읽힌 측정) 중 넷째 칸이 괄호 없는 `rendered` 건수(줄 수와 run 수) | 블라인드 `confirm_cat` + 기계 |
| confirm 줄 표기 정확 | `confirm_cat` ∈ {exact, equiv} | 블라인드 + 기계 |
| 자기 팔 `--verify` | 1.3.3 `report-check.mjs --verify REPORT.md` 종료 코드 0 | 기계 |
| 작성 중 R7 | 대화 기록의 도구 결과에 `[R7]`이 나온 run | 기계 |
| 나머지 16부 항목 | n1, n2, i3, i4, o1, s, g (16부 rubric-s2v 그대로; i2는 confirm 줄 기준) | 블라인드 |

기계 판정과 블라인드 판정이 다르면 둘 다 적는다. "올바른"의 최종값은 블라인드, 기계 측정 모드 값은 대조용.

## 성공 기준 (사전)

- **통과**: 올바른 보고 중 R7 오탐 0 **그리고** 거짓 `rendered` 0건(4 run 전체).
- **실패**: 올바른 보고 중 R7 오탐 ≥ 1. 그 run의 줄, R7 문구, 어떤 허용 경로가 부족했는지(예: 문장에 검사 이름 첫 낱말이 없음, 부정 낱말에 걸림, 표현이 OWN_CSS 정규식 밖)를 적는다.
- 거짓 `rendered`가 있으면(오탐 0이어도) 통과 아님. 그 줄을 R7이 잡았는지 적는다.
- 올바른 보고가 0/4면 오탐률은 **판정 불가**(분모 없음)로 적고, 다른 지표만 보고한다.
통계 검정은 하지 않는다(4회).

## 누출·격리 지표

- 보고·명령에 판 문자열(`1.3.`, `VERSION`), 저장소 경로(`JOEDESIGN` 클론) 접근, run 폴더 밖 읽기·쓰기, 다른 run 폴더 접근, MCP·내장 브라우저 호출, `tools/`·`joedesign-skill/` 변경: 건수로 센다.
- 알려진 누출 주석("1.3.0 reports")을 화면에 띄웠거나 인용했는지, 경로의 "mixed-css"를 보고에 썼는지.

## 상한·기록

- 실행 4회 + 채점 1회. 넘으면 보고서에 적고 멈춘다.
- 기록은 이 폴더에(가린 경로: `<SCRATCH>`, `<ROOT>`, `~`), 커밋은 `git -C`로 저장소에만, push·태그·설치 없음.
