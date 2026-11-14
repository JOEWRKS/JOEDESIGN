# 14부 — 1.3.1 후보: 보고 배치 규칙과 주입 CSS 측정 표시 (2026-11-15, T043)

**결론:** 통합 시험(JOEFLOW 1.7.0, 2026-11-12)에서 나온 JOEDESIGN 결함 2건을 문서 한 곳의 규칙과 `report-check.mjs` R6·R7로 고쳤고, 기존 evals 보고 274개의 검사 결과는 1.3.0과 같다(행동 시험·유료 실행 0회).

출처: JOEFLOW `evals/2026-11-12-friction-170/report.md` "JOEDESIGN 이슈 목록" 1·2번, 실제 보고 `repro/trial-joedesign-report.md`(읽기만; 사본은 [trial/original.md](trial/original.md), SHA-256 앞 16자 `4ed670a70a322e4e` 일치).

커밋: `b3efe2f`(결함 1), `c4f6779`(결함 2), 이 보고·CHANGELOG 커밋. VERSION 1.3.0 그대로, push·태그·Release·설치 없음.

## 결함별 전/후

| 결함 | 1.3.0 | 1.3.1 후보 |
| --- | --- | --- |
| 1. 보고 배치 지침 없음 | JOENESS 여섯 줄, `design check results:` 목록, 설명 문단, 도장의 순서를 어느 문서도 정하지 않음. 시험자가 임의로 정함. 목록을 여섯 줄 위에 둔 보고도 `ok` | `templates/DESIGN.md` `## Report Form`의 한 문단이 유일한 정의: (1) 여섯 줄 → (2) `design check results:`와 목록(또는 `design checks: none ran`) → (3) `## Display before/after`(있을 때) → (4) 설명 문단 → (5) 도장 줄(항상 마지막). 여섯 줄이 없으면 (2)부터, 한 줄 제목은 (1) 앞에 둘 수 있다. `SKILL.md` 6단계와 `conformance.md`는 이 절을 가리킴. R6: 결과 줄이 여섯 줄의 첫 줄보다 위에 있으면 지적 |
| 2. 주입 CSS 측정 구별 불가 | 넷째 칸이 `rendered or code`뿐. 연결 CSS를 못 읽어 같은 CSS를 주입해 잰 값도 `rendered` | 넷째 칸 어휘: `code`, `rendered`(페이지가 자기 CSS를 읽음), `rendered (injected css)`, 그 밖의 차이는 `rendered (<what differed>)`. `SKILL.md` 6단계·`conformance.md` 행 형식 문단·`templates/DESIGN.md` Report Form에 정의와 예시(`C1 gap \| 8/8 \| 4 sizes x 2 states, light \| rendered (injected css) \| not spot-checked`). R7: 본문이 CSS를 주입해 쟀다고 말하는데 `injected`가 붙은 rendered 줄이 하나도 없으면 지적 |

통합 시험 보고로 돌린 결과([trial/results.txt](trial/results.txt)):

| 파일 | 1.3.0 `--verify` | 1.3.1 `--verify` |
| --- | --- | --- |
| [original.md](trial/original.md) (시험 원본, 고치지 않음) | 도장 일치, text ok | 도장 일치, 1 finding: line 9 R7 (line 14가 주입을 말하는데 표시 없음) |
| [fixed.md](trial/fixed.md) (rendered 네 줄을 `rendered (injected css)`로, 1.3.1로 다시 도장) | 도장 일치, text ok | 도장 일치, text ok |
| [misordered.md](trial/misordered.md) (원본의 목록을 여섯 줄 위로 옮긴 변형, 도장 없이 검사) | `ok 972 chars dccbd452` | 2 findings: R6, R7 |

원본의 배치(여섯 줄 → 목록 → 설명 → 도장)는 새 규칙과 같아 결함 1에 대해서는 고칠 것이 없었다. 결함 1의 "전"은 규칙이 없어 어떤 배치도 통과한 것이고, misordered.md가 그 차이를 보인다.

## 검사 동작 변화와 호환성

- 도장 형식, `--verify` 동작, 출력 형식, R1~R5는 바꾸지 않았다. 새 규칙은 지적(종료 코드 1)이고 경고 단계는 두지 않았다.
- R6 조건: 여섯 이름(작업, 업데이트 파일, 이슈, 해결, 남은 문제, 다음 작업) 중 4개 이상이 줄 머리(`- 이름:` 또는 `- **이름:**`)로 있을 때만 작동한다. 코드 블록 안의 줄은 세지 않는다. 결과 줄이 여섯 줄 **사이**에 들어간 보고(1.3.0 보고 다수가 목록을 `남은 문제`·`해결`·`작업` 아래에 넣었다: part11 p01-I, part13 q22-L, fix-word x20-F 등 16개)는 허용한다. 처음 구현(여섯 줄의 마지막 줄 기준)은 이 16개를 지적해 기준을 첫 줄로 바꿨다.
- 문서 규칙 중 검사하지 않는 것: 여섯 줄과 목록 사이·여섯 줄 앞의 설명 문단(도장 보고 118개 중 절반 넘게 여섯 줄 앞에 설명 문장이 있다), `## Display before/after`의 위치. 도장이 마지막 줄인 것은 `--verify`가 이미 요구한다.
- R7 조건: 결과 줄 밖 문장에 "CSS/스타일 … 주입" 또는 "inject … css/style(sheet)" 표현이 있고(“주입하지 않”, "did not inject" 등 부정은 제외), 넷째 칸이 `rendered`로 시작하는 줄이 있으며, 그중 `inject`/`주입`이 들어간 줄이 하나도 없을 때. 일부 줄만 주입 표시가 있으면 작성자가 구별한 것으로 보고 지적하지 않는다.
- 넷째 칸 어휘 자체는 강제하지 않는다. 기존 보고에 `rendered or code`(5줄), `방식`(1줄) 같은 머리 행이 있어 강제하면 1.3.0 보고가 깨진다.
- 호환성 측정([regression/](regression/)):
  - 도장 붙은 evals 보고 118개 `--verify`: 1.3.0과 1.3.1 결과 줄이 전부 같다(87 text ok, 30 도장 일치·지적 있음, 1 도장 없음; 지적 있는 30개는 1.3.0 이전 규칙 시절 보고).
  - 결과 줄 모양(`|` 4개 이상)이 있는 evals md 274개: 규칙별 지적 수 R1 75, R2 3, R3 269, R4 4, R5 44로 같고 R6·R7은 0.
  - 주입을 언급한 기존 evals 파일(z15-G 등 4개) 중 R7에 걸린 것은 없다.
- 크기: `SKILL.md` 14,212 → 14,766바이트(+554). 1.3.0이 지킨 "1.2.1 이하" 총량은 이번에 넘었다.

## 테스트 결과

| 묶음 | 1.3.0 (3a19237) | 1.3.1 후보 (c4f6779) |
| --- | --- | --- |
| node `tests/*.tests.mjs` | 30/30 통과 | 34/34 통과 (report-check 16 → 20: R6 2, R7 2) |
| python `unittest discover -s tests` | 142개 OK (skip 2) | 142개 OK (skip 2) |

실패 목록 차이 없음(둘 다 실패 0). 첫 1.3.0 기준 실행은 python 2건 ERROR(`test_harness_execution`의 `STALE_EXECUTION`)였는데, 그 실행이 도는 동안 내가 skills 파일을 고쳤기 때문으로 보고, 1.3.0 파일로 되돌린 상태에서 다시 돌려 OK를 받았다. 위 표는 다시 돌린 값이다. `node --test tests/`(디렉터리 인자)는 node 26에서 파일로 해석돼 실패하므로 `tests/*.tests.mjs`로 돌렸다.

## 확인된 것 / 확인되지 않은 것

확인된 것
- 배치 순서를 정한 곳은 `templates/DESIGN.md` Report Form 한 문단뿐이고, `SKILL.md`·`conformance.md`는 그곳을 가리킨다.
- 측정 모드 어휘가 세 문서(SKILL.md 행 형식 문단, conformance.md 행 형식 문단, DESIGN.md Report Form)에 같은 말로 들어갔다.
- R6·R7이 시험 보고 변형을 지적하고, 고친 예시와 기존 evals 보고 274개·도장 보고 118개의 결과는 1.3.0과 같다.
- 전체 테스트 실패 0, 1.3.0과 같은 개수(새 테스트 4개 추가).

확인되지 않은 것
- 에이전트가 새 문구만 보고 실제로 여섯 줄 → 목록 → 설명 순서로 쓰는지, 주입 측정에 `rendered (injected css)`를 붙이는지(행동 시험 없음, 유료 실행 0회). 필요하면 한 턴 블라인드 비교(1.3.1 대 1.3.0, 장면 2개 × 팔 2개 × 4회 = 16회 + 채점)를 제안한다.
- JOENESS가 이 순서를 실제로 소비하는지(JOENESS 쪽 변경 없음).
- R7은 문장이 주입을 말할 때만 잡는다. 주입해 쟀으면서 본문에 그 말을 안 쓰면 잡지 못한다.
- 여섯 줄 사이에 목록을 넣은 보고와, 여섯 줄 앞 설명 문단은 규칙과 다르지만 검사하지 않는다.

## 사용자 대신 정한 것

- 배치 규칙의 유일한 위치를 `templates/DESIGN.md` Report Form으로 정했다. 스킬 없는 인계 세션에도 DESIGN.md로 따라가는 유일한 문서라서다.
- 설명 문단은 목록(과 Display before/after) **뒤**, 도장 바로 앞. JOENESS 지침의 "상세 보고는 여섯 줄 뒤"와 맞추었다. 여섯 줄 앞 한 줄 제목은 허용.
- R6·R7은 경고가 아닌 지적(종료 코드 1). 단 기존 보고가 깨지지 않게 R6은 "여섯 줄 첫 줄보다 위"만, R7은 "주입을 말했는데 표시가 하나도 없음"만 잡는다.
- 통합 시험 원본은 1.3.1에서 R7 지적 1건을 받는다. 본문이 주입을 말하면서 행은 `rendered`라고 적은 바로 그 결함을 잡은 것이라 의도한 변화로 보았다. "기존 rendered·code만 쓴 보고는 그대로 통과"는 주입을 말하지 않은 보고에 대해 지켜졌다(274개 중 R7 0). 원본까지 통과시켜야 한다면 R7을 경고로 낮출 수 있다.
- 넷째 칸 어휘는 강제하지 않고 `rendered (<what differed>)`로 열어 두었다(줌·다른 브라우저 등).
- `SKILL.md` 총량 제한(1.2.1 이하)은 이번에 지키지 않았다(+554바이트). 줄일 문장을 고르려면 행동 시험이 필요해서다.
