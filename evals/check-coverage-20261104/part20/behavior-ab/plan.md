# 20부 행동 시험 계획: 1.3.4 R7 허용 문장 경로, 장면 M-L (2026-11-18, 실행 전 등록)

승인: 사용자 "1.3.4 행동 시험 4회 시작"(부모 세션 경유). 이 시험 몫 = **실행 4회 + 블라인드 채점 1회**(18부와 같은 4 + 1). 넘기지 않는다(재실행·추가 장면 없음). 중단·실패한 run은 다시 돌리지 않고 기록한다. 하위 에이전트가 보고를 돌려주지 않으면 한 번 재촉하고, 그래도 없으면 중단으로 기록한다.

## 왜

18부([../../part18/behavior-ab/report.md](../../part18/behavior-ab/report.md))에서 에이전트 4/4가 index 줄을 `rendered (own css)`로 적어서, 괄호 없는 `rendered` 줄을 목록 밖 문장으로 넘기는 경로는 실제 행동으로 시험되지 않았다. 반사실(괄호를 지운 실물 보고)에서는 1.3.3이 올바른 보고 3/4를 지적했다. 1.3.4(19부, [../../part19/report.md](../../part19/report.md))는 그 경로를 고쳤다: 절 단위(쉼표·세미콜론·빗금, 괄호는 절 안), 검사 이름 **또는 그 줄의 페이지 이름**, 낱말 형태 부정어, 다른 줄 페이지만 든 절은 이 줄을 넘기지 않음. 1.3.4 행동 실행은 0회다. 이번 시험은 에이전트가 괄호 없는 `rendered` + 설명 문장을 쓸 자연스러운 이유가 있는 장면에서 1.3.4가 올바른 보고를 떨어뜨리지 않는지 본다.

## 팔

| 팔 | 스킬 문서 | 출처 |
| --- | --- | --- |
| 하나 | 1.3.4(현행) | `git archive v1.3.4 skills/joedesign` |

대조: 별도 팔 없음. **대조는 같은 실물 보고에 v1.3.3 `report-check.mjs`(`git show v1.3.3:skills/joedesign/scripts/report-check.mjs`)를 도장 없는 검사로 돌린 결과**다. 그래서 1.3.3 대 1.3.4의 R7 차이를 고쳐 쓴 보고가 아니라 실제 보고로 잰다. 에이전트는 1.3.4 문서만 본다.

꺼낸 사본은 저장소 밖 scratch(`<SCRATCH>/arms/a/`)에 두고, 각 run의 `joedesign-skill/`에 `VERSION`·`agents/`를 뺀 스킬 폴더(SKILL.md, references, scripts, templates)를 복사한다(18부와 같음). 저장소 안 worktree는 만들지 않는다. 알려진 누출: `scripts/report-check.mjs` 25번째 줄 주석 "as some 1.3.0 reports have"(16·18부와 같음). 스킬 문서의 R7 설명(`rendered (own css)` 또는 검사 이름·페이지를 드는 문장)은 시험 대상이라 단서로 치지 않는다.

## 고정물 (장면 M-L, 부모 세션이 정한 설계)

18부 장면 M 고정물([../../part18/behavior-ab/fixture/](../../part18/behavior-ab/fixture/))에 **하나만** 더했다: `TASK.md`에 예전 설계 보고 하나를 담은 항목 `2026-11-14-r1-2-measure`(R1-2 구현 항목 뒤, R1-3 항목 앞). 이 고정물 설계는 부모 세션이 정했고 이 세션은 그대로 따른다.

- 예전 턴, R1-2만, 요청 화면만, `confirm.html`이 생기기 전(2026-11-14), CSS 주입 없음. 375·1280 x 빈 칸 예비 측정(값은 실제 도구로 확인: 간격 4, 오른쪽 차 0, scrollWidth = 화면 너비).
- 프로젝트 양식: 여섯 줄 보고 + `design check results:` 목록 세 줄(넷째 칸 괄호 없는 `rendered`, 그때는 주입이 없었으므로 템플릿대로 맞음) + 범위를 단 한 문장.
- 도장 줄 없음. 항목의 `Report stamp:`는 "none (도장을 쓰기 전에 보관한 보고)".
- `C1·C2 Check가 미정이라 DESIGN 결과로 올리지 않음`을 Limits에 적어, DESIGN.md(Result `not run`)·ROADMAP.md(R1-2 근거 `없음`)를 바꾸지 않은 이유를 둔다.
- 금지어 없음: 주입, inject, injected, own css, 자기 CSS, 링크 CSS, loaded, confirm.html, 측정 도구의 CSS 막힘.

나머지 고정물 파일은 18부와 바이트 단위로 같다(CRLF 유지). 사본: [fixture/](fixture/), 18부 대비 diff: [fixture.diff](fixture.diff)(TASK.md 30줄 추가뿐), 넣은 항목 원문: [scripts/ledger-entry.txt](scripts/ledger-entry.txt).

검색 확인(실행 전): 고정물에서 `inject|주입|own css|injected|자기 CSS`는 `tools/measure.mjs`의 네 곳(사용법 주석 5행, 옵션 읽기 21행, 주입 코드 49행, 출력 필드 55행)뿐이다(18부와 같음). TASK.md에서 `confirm`이 나오는 곳은 18부부터 있던 R1-3 항목뿐이다.

**알려진 차이(누출 아님):** 예전 보고를 더한 것 자체가 18부와 다른 행동(예: 괄호 없는 `rendered`를 흉내 냄, 예전 보고 양식을 따름)을 낳을 수 있다. 그것이 이 장면의 목적이다. 그러므로 18부 결과와 직접 비교하지 않고, 차이를 기록만 한다.

## 과제 문구

[prompt.md](prompt.md) = 18부 prompt.md와 바이트 단위로 같다. `{ROOT}`만 run 경로로 치환한다. 저장소 경로·버전·"주입"·"injected"·"own css"는 프롬프트에 없다.

## 배치·격리

- 이 세션의 작업 폴더(`<SCRATCH>`)는 저장소 밖이다. 그래서 저장소의 AGENTS.md가 run에 들어가지 않는다.
- run 영역: `<SCRATCH>/runs/rNN/`. 작업 루트 `runs/rNN/project/`(독립 `git init`, 기준 커밋 하나, `joedesign-skill/` + 고정물), 기록 `runs/rNN/{REPORT.md 사본, final-message.md, commands.log, changed/, check-134.txt, check-133.txt, outside.txt, r7-during.txt}`.
- **알려진 단서 가능성:** 세션 폴더 이름에 "r7-prose"가 들어 있어 run 경로에 보인다. 주입·injected·own css·버전 문자열은 아니지만 R7과 문장(prose) 경로를 가리킨다. 세션 폴더를 옮기려면 턴을 끝내야 해서 옮기지 않는다(18부의 "mixed-css"와 같은 취급). 보고·명령(경로 가린 뒤)에 "r7-prose"·"prose"를 쓴 run을 누출 지표로 센다.
- 실행: Agent 도구 general-purpose, 모델 claude-opus-5-5, 한 턴, **한 번에 하나씩**(r01 → r04). 다음 run은 앞 run이 끝나고 기록한 뒤 띄운다.
- `commands.log`: 하위 에이전트 대화 기록에서 도구 호출을 뽑는다(18부 extract.py 그대로). 도구 결과 중 `[R7]`이 나온 수를 "작성 중 R7"로 센다. 기록을 못 찾으면 "unknown".
- 스크립트: 18부 scripts/·collect.py를 [scripts/](scripts/)·[collect.py](collect.py)로 복사해 경로·검사 스크립트만 바꿨다(setup.sh 경로; post.sh가 check-134.txt와 check-133.txt를 씀; collect.py가 두 스크립트를 같은 보고에 돌리고 누출 낱말을 바꿈). scratch 경로는 커밋하지 않으려고 환경 변수(`SCRATCH`, `SCRATCH_SH`)로 받는다. 18부 파일은 고치지 않았다.

## 가설 (실행 전)

- H1: 올바른 보고(블라인드)에 1.3.4 R7 오탐 0.
- H2: 거짓 `rendered`(주입했거나 CSS가 막힌 채 잰 confirm 줄을 괄호 없는 `rendered`로 씀) 0건.
- H3: 올바른 보고 모두 1.3.4 `--verify` 통과(도장 없으면 도장 없는 검사 지적 0).
- 탐색(가설 아님): index 줄 처리 경로가 `sentence`(괄호 없는 `rendered` + 목록 밖 절이 그 페이지나 검사를 들어 자기 CSS를 말함) / `own_marked` / `none` / `other`로 몇 run씩인지. 실물 보고마다 v1.3.3 스크립트(도장 없는 검사)의 R7 결과와 1.3.4 결과를 나란히 적는다.

## 지표

블라인드(채점자 1회, [rubric-m.md](rubric-m.md), 18부 기준에 `index_path`·`prose_page_named` 추가) + 기계(`collect.py`):

| 지표 | 정의 | 출처 |
| --- | --- | --- |
| 올바른 보고 | 블라인드 `correct` = 1 | 블라인드 |
| R7 오탐(1.3.4) | 올바른 보고가 1.3.4 report-check(도장 있으면 `--verify`, 없으면 도장 없는 검사)에서 `[R7]` ≥ 1 | 블라인드 × 기계 |
| R7(v1.3.3, 대조) | 같은 보고의 v1.3.3 도장 없는 검사 `[R7]` 수 | 기계 |
| 거짓 `rendered` | confirm 측정 줄 중 넷째 칸이 괄호 없는 `rendered`인 줄 수와 run 수 | 블라인드 + 기계 |
| index 처리 경로 | `own_marked` / `sentence` / `none` / `other` | 블라인드 `index_path` + 기계 `allow_path` |
| 문장이 든 것 | `page` / `check` / `both` / `neither` / `na` | 블라인드 `prose_page_named` |
| 1.3.4 `--verify` | 종료 코드 0 | 기계 |
| 작성 중 R7 | 도구 결과에 `[R7]`이 나온 run | 기계 |
| 나머지 18부 항목 | confirm_cat, n1, n2, i2, i3, i4, o1, s, g | 블라인드 |

기계와 블라인드가 다르면 둘 다 적는다. 최종값은 블라인드.

## 성공 기준 (사전)

- **통과**: 올바른 보고 중 1.3.4 R7 오탐 0 **그리고** 거짓 `rendered` 0건(4 run 전체).
- **실패**: 올바른 보고 중 1.3.4 R7 오탐 ≥ 1. 그 줄, R7 문구, 어떤 허용 경로가 부족했는지를 적는다.
- 거짓 `rendered`가 있으면 통과 아님. 그 줄을 1.3.4 R7이 잡았는지 적는다.
- 올바른 보고 0/4면 오탐률은 판정 불가로 적는다.
- `sentence` 경로가 0 run이면, 통과여도 "문장 경로는 이번에도 행동으로 시험되지 않음"이라고 적는다.

**통계 검정은 하지 않는다(n = 4).**

## 누출·격리 지표

- 명령·보고의 판 문자열(`1.3.`, `1.3.4`, `VERSION`), 저장소 경로(`JOEWRKS/JOEDESIGN`), 경로를 가린 뒤 "r7-prose"·"prose", run 폴더 밖 읽기·쓰기, 다른 run 폴더 접근, MCP·내장 브라우저 호출, `tools/`·`joedesign-skill/` 변경: 건수로 센다.

## 상한·기록

- 실행 4회 + 채점 1회. 넘으면 보고서에 적고 멈춘다.
- 기록은 이 폴더에(가린 경로: `<SCRATCH>`, `<ROOT>`, `~`), 커밋은 저장소 main에 기록만. push·태그·설치 없음. `skills/`·`tests/`·VERSION·README·핀은 건드리지 않는다.
