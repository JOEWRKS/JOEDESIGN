# 20부 행동 시험: 1.3.4 R7 허용 문장 경로, 장면 M-L (2026-11-18, T043)

**결론:** 사전 기준은 통과했다. 블라인드 채점에서 올바른 보고 4/4, 그중 1.3.4 R7 오탐 0/4, 거짓 `rendered` 0건, 1.3.4 `--verify` 4/4 통과. 그러나 네 run 모두 요청 화면 줄을 `rendered (own css)`로 적었다(경로 `own_marked` 4/4, `sentence` 0/4). 예전 보고(괄호 없는 `rendered`)를 작업 기록에 넣어도 에이전트는 그 형식을 따르지 않았다. 그래서 **1.3.4가 고친 문장 허용 경로는 이번에도 실제 행동으로 시험되지 않았다.** 같은 실물 보고에 v1.3.3 스크립트를 돌린 결과도 R7 0/4로 1.3.4와 같다. 이번 보고들로는 두 판의 차이가 드러나지 않는다.

사전 등록: [plan.md](plan.md)(커밋 0801ede, 첫 실행 전). 프롬프트 [prompt.md](prompt.md)(18부와 바이트 단위로 같음), 채점 기준 [rubric-m.md](rubric-m.md), 고정물 [fixture/](fixture/)와 18부 대비 diff [fixture.diff](fixture.diff)(TASK.md 항목 하나 추가, 원문 [scripts/ledger-entry.txt](scripts/ledger-entry.txt)). 원문: [runs/](runs/)(REPORT.md, final-message.md, commands.log, changed/, check-134.txt, check-133.txt, outside.txt, r7-during.txt). 블라인드 결과는 [blind-grades/](blind-grades/), 합본 [grades.json](grades.json), 배치표 [blind-map.json](blind-map.json)(채점 뒤 복사). 기계 측정은 [mech.json](mech.json)(`collect.py`). 사고 기록 [incidents.txt](incidents.txt), 기록 스크립트 [scripts/](scripts/).

팔: 1.3.4 하나(`git archive v1.3.4`, VERSION·agents/ 뺌). 대조: 같은 보고에 v1.3.3 `report-check.mjs`를 돌린 결과(별도 팔 아님). Opus 한 턴, 한 번에 하나씩 r01 → r04.

## 지표

| 항목 | 결과 | 출처 |
| --- | --- | --- |
| **올바른 보고** | **4/4** | 블라인드 |
| **R7 오탐(1.3.4)**(올바른 보고에서 `[R7]` ≥ 1) | **0/4** | 블라인드 × 기계(check-134.txt) |
| **거짓 `rendered`** | **0줄, 0/4 run** | 블라인드 = 기계 |
| 1.3.4 `--verify` 통과 | 4/4(모두 도장 있음, `stamp: match; text ok`) | 기계 |
| 1.3.4 지적(R1~R7, 도장 없는 검사) | 0/4 | 기계 |
| 요청 화면 줄 처리 경로 `own_marked` / `sentence` / `none` / `other` | **4 / 0 / 0 / 0** | 블라인드 `index_path` = 기계 `allow_path` |
| 목록 밖 자기 CSS 문장(own_sentence) | 3/4(r02 없음) | 블라인드 |
| 그 문장이 든 것(prose_page_named) | page 2(r03, r04), both 1(r01), na 1(r02) | 블라인드 |
| confirm 줄 표기 | exact 3, equiv 1(r01) | 블라인드 |
| 작성 중 R7을 만난 run | 0/4 | 기계(r7-during.txt) |
| n1 / n2 / i2 / i3 / i4 | 4/4 각각 | 블라인드 |
| o1 / s / g | 4/4 각각 | 블라인드 |

성공 기준(사전): R7 오탐 0 그리고 거짓 `rendered` 0 → **통과.** 사전 등록한 단서대로 적는다. `sentence` 경로 0 run이므로 문장 경로는 행동으로 시험되지 않았다.

## run별 넷째 칸 (블라인드 `fourth`, 결과 줄 그대로)

| run | 요청 화면 줄 | 확인 화면 줄 | 그 밖 |
| --- | --- | --- | --- |
| r01 | `rendered (own css)` ×3 | `rendered (injected css)` ×3, `rendered (linked css blocked)` ×1(CSS 없이 잰 대조 줄, 0/8) | AC 줄 하나가 두 화면을 합쳐 `rendered (요청 own css, 확인 injected css)` |
| r02 | `rendered (own css)` ×4 | `rendered (injected css)` ×4, `rendered (linked css blocked by tools/measure.mjs)` ×1(로드 확인 줄) | — |
| r03 | `rendered (own css)` ×3 | `rendered (injected css)` ×3, `rendered (linked css blocked, no injection)` ×1(대조 줄, 0/8) | — |
| r04 | `rendered (own css)` ×4 | `rendered (injected css)` ×4 | — |

괄호 없는 `rendered` 결과 줄은 네 보고 어디에도 없다. CSS가 막힌 채 잰 대조 줄은 모두 괄호 표기이고 통과 근거로 쓰이지 않았다(i4 4/4). r02는 본문 통과 문장 하나에서 두 화면을 괄호 없는 `rendered`로 묶었다(결과 줄 아님, 채점자 g = 1, R7 대상 아님).

## 1.3.3 대 1.3.4, 실물 보고별 R7 (도장 없는 검사)

| run | 괄호 없는 `rendered` 줄 | v1.3.3 R7 | 1.3.4 R7 | v1.3.3 다른 지적 | 1.3.4 `--verify` |
| --- | --- | --- | --- | --- | --- |
| r01 | 0 | 0 | 0 | 0 | 0(match) |
| r02 | 0 | 0 | 0 | 0 | 0(match) |
| r03 | 0 | 0 | 0 | 0 | 0(match) |
| r04 | 0 | 0 | 0 | 0 | 0(match) |

두 스크립트가 다를 수 있는 곳은 괄호 없는 `rendered` 줄뿐이다. 그런 줄이 0이라 이 표는 차이를 잴 수 없다. 고쳐 쓴 보고로 하는 반사실은 이번 범위가 아니라서 하지 않았다(19부 counterfactual이 이미 있음).

## 예전 보고(장면 M-L 추가분)의 영향

- 네 run 모두 첫 몇 번의 호출 안에 TASK.md 전체를 읽었다(commands.log). 예전 보고의 괄호 없는 `rendered` 결과 줄을 본 것이다.
- 그래도 새 보고는 4/4 `rendered (own css)`였다. 네 run 모두 `templates/DESIGN.md`를 읽었다(측정 모드 문단에 `rendered (own css)` 형식이 있음). r01·r03·r04는 `references/conformance.md`도 읽었다. 어느 문서가 결정했는지는 나누지 않았다.
- 새 TASK 항목에 괄호 없는 `rendered` 결과 줄을 쓴 run 0/4. r04는 TASK 항목에 "확인 화면은 rendered (injected css), 요청 화면은 rendered (own css)"라고 적었다.
- 보고에서 예전 측정(2026-11-14)을 언급한 run 0/4.
- 18부(같은 장면, 예전 보고 없음, 1.3.3 문서)도 `own_marked` 4/4였다. 예전 보고를 더했어도 이 지표는 그대로였다. 18부와 직접 비교하지는 않는다(판과 고정물이 다름).

## 누출·격리

- 판 문자열·`1.3.4`·VERSION을 명령이나 보고에 쓴 run 0/4. 저장소 경로(`JOEWRKS/JOEDESIGN`) 접근 0/4.
- 경로 단서 "r7-prose": 보고에 쓴 run 0/4. 명령에서는 r02의 하네스 저장 파일 경로 1건뿐이었다(세션 폴더 이름의 일부, 가림).
- 알려진 누출 주석("as some 1.3.0 reports have", 25번째 줄): 네 run 모두 report-check.mjs 머리를 그 줄이 들어가는 범위까지 띄웠다(r01 `head -80`, r02 파일 전체, r03·r04 `head -40`). 16·18부와 같은 시험 조건이다. 판 문자열을 옮겨 쓴 run 0/4.
- 폴더 밖 접근: r02 1건. 하네스가 따로 저장한 자기 명령 출력 파일(`~/.claude/projects/<session-project>/tool-results/…`)을 읽었다. 프로젝트·다른 run·저장소는 0/4. MCP·내장 브라우저 0/4. tools/·joedesign-skill/ 변경 0/4. 보조 파일은 모두 자기 `.work/`.
- 채점자: blind/ 밖 접근 없음, grade.json 외 파일 없음(채점자 자기 보고, blind 폴더 목록으로 확인).

## 사고 ([incidents.txt](incidents.txt))

1. r03·r04: "Write 도구가 REPORT.md를 막아 셸로 썼다"고 보고했다. 하위 에이전트 쪽 하네스 제한으로 보인다. 결과 파일은 정상이고 `--verify`도 맞다.
2. 블라인드 배치가 seed(실행 전 고정) 결과 우연히 실행 순서와 같았다(g01=r01 … g04=r04). 채점자에게 run 번호는 주지 않았다.
3. 기계 `inject_confirm`이 r01에서 False인 것은 검출 누락이다(`.work/` 스크립트 안의 `--inject`). 기계 `confirm_cat`도 r01·r02가 `other`였다. 대조 줄의 괄호 표기를 주입으로 세지 않았기 때문이다. 블라인드는 equiv·exact로 봤고 최종값은 블라인드다.
4. 기록 단계 실수(프롬프트 생성 스크립트의 백슬래시, 마스크 정규식)는 모두 첫 실행 전에 고쳤다.

## 확인된 것

- 1.3.4는 이 장면의 올바른 실물 보고 4/4를 통과시켰다. R7 오탐 0, `--verify` 4/4, R1~R7 지적 0.
- 에이전트는 두 페이지의 측정 모드를 갈라 적었다. 요청 화면은 `rendered (own css)`, 확인 화면은 `rendered (injected css)`였다. 거짓 `rendered` 0. 작성 중 R7을 만난 run 0.
- 작업 기록에 괄호 없는 `rendered` 예전 보고가 있어도 4/4가 `rendered (own css)`를 썼다. 세 run(r01, r03, r04)은 목록 밖에서도 요청 화면이 자기 CSS를 읽었다고 말했다(둘은 페이지 이름만, 하나는 검사와 페이지 함께).
- 같은 네 보고에서 v1.3.3과 1.3.4의 R7 결과는 같다(0 = 0).

## 확인되지 않은 것

- **1.3.4 문장 허용 경로의 실제 행동.** 괄호 없는 `rendered` 줄 + 설명 문장을 쓴 보고가 18부·20부 합쳐 0/8이다. 그런 보고에서 1.3.4가 오탐을 내지 않는지는 19부 반사실(고친 보고)과 테스트로만 확인됐다.
- 에이전트가 `(own css)`를 고른 이유. 템플릿 측정 모드 문단이 가장 그럴듯하지만, 문서별로 나누어 보지 않았다.
- 표본: 4회, 한 턴 Opus, 고정물 하나. 다른 모델·Codex, 검사 이름이 페이지마다 다른 보고, 예전 보고가 더 많거나 더 최근인 기록은 시험하지 않았다. 통계 검정은 하지 않았다(n = 4).
- 블라인드 배치가 실행 순서와 같았던 점이 채점에 영향을 줬는지(채점자는 run 번호를 몰랐다).

## 세션이 대신 내린 결정

1. 장면 M-L 설계(예전 보고 하나를 TASK.md에 넣음)는 부모 세션의 결정이다. 이 세션이 정한 세부: 항목 위치(R1-2 항목 뒤), 예비 측정 범위(375·1280 x 빈 칸, 값은 실제 도구로 확인), DESIGN·ROADMAP을 바꾸지 않은 이유를 Limits에 둠("C1·C2 Check가 미정이라 DESIGN 결과로 올리지 않음"), 도장 줄 대신 "도장을 쓰기 전에 보관한 보고".
2. 채점 기준에서 18부 `index_cat`(측정 모드 분류)은 그대로 두고, 브리프가 말한 `own_marked` / `sentence` / `none` / `other` 값은 새 항목 `index_path`로 넣었다. `prose_page_named`는 `page` / `check` / `both` / `neither` / `na`.
3. scratch 경로를 커밋하지 않으려고 기록 스크립트가 경로를 환경 변수(`SCRATCH`, `SCRATCH_SH`)로 받게 바꿨다. 하네스 세션 폴더 이름은 `<session-project>`로 가렸다.
4. check-134.txt에는 도장이 있으면 `--verify`, 그리고 도장 없는 검사를 함께 적었다. check-133.txt는 v1.3.3 도장 없는 검사만 적었다.
5. 행동이 문장 경로를 쓰지 않았지만 반사실이나 추가 run은 하지 않았다(상한 4 + 1, 19부에 반사실 있음).

## 쓴 횟수

실행 4회(Opus, 순차, 중단·재실행 없음) + 블라인드 채점 1회(Opus). 승인 상한 4 + 1 안이다.
