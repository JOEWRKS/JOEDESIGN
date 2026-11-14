## 1.3.1 — 보고 배치 규칙과 주입 CSS 측정 표시 (2026-11-15, T043)

JOEFLOW 1.7.0 세 도구 통합 시험(2026-11-12)에서 나온 JOEDESIGN 결함 2건을 고쳤다. 스키마·계약·CLI·도장 형식은 그대로다.

- **보고 배치**: `templates/DESIGN.md` `## Report Form`의 한 문단이 순서를 정한다. JOENESS 여섯 줄(작업/업데이트 파일/이슈/해결/남은 문제/다음 작업) → `design check results:`와 목록(또는 `design checks: none ran`) → `## Display before/after`(있을 때) → 설명 문단 → 도장 줄(항상 마지막). 여섯 줄이 없으면 목록부터, 한 줄 제목은 여섯 줄 앞에 둘 수 있다. `SKILL.md` 6단계와 `references/conformance.md`는 그 절을 가리킨다. `scripts/report-check.mjs` R6: 결과 줄이 여섯 줄의 첫 줄보다 위에 있으면 지적(여섯 줄 사이에 넣은 목록은 허용).
- **측정 모드**: 결과 줄 넷째 칸은 `code`, `rendered`(페이지가 자기 CSS를 읽음), `rendered (injected css)`(미리보기가 연결 CSS를 읽지 못해 같은 CSS를 주입해 잼), 그 밖의 차이는 `rendered (<what differed>)`. 세 문서에 정의와 예시. R7: 본문이 CSS 주입을 말하는데 주입 표시가 붙은 rendered 줄이 하나도 없으면 지적.

**확인된 것**([14부 보고](https://github.com/JOEWRKS/JOEDESIGN/blob/main/evals/check-coverage-20261104/part14/report.md)): 도장 붙은 evals 보고 118개의 `--verify` 결과와 결과 줄이 있는 evals 보고 274개의 규칙별 지적 수가 1.3.0과 같다(R6·R7 지적 0). 통합 시험 원본 보고는 R7 1건(본문이 주입을 말하면서 행은 `rendered`라고 적은 바로 그 결함), 고친 예시는 ok. 테스트 node 34/34(report-check 16 → 20), python 142 OK.

**확인되지 않은 것**: 에이전트가 새 문구만 보고 실제로 그 순서로 쓰고 주입 측정에 표시를 붙이는지(행동 시험 0회, 유료 실행 0회). JOENESS가 이 순서를 소비하는지(JOENESS 변경 없음). R7은 본문이 주입을 말할 때만 잡는다. 여섯 줄 사이의 목록과 여섯 줄 앞 설명 문단은 규칙과 다르지만 검사하지 않는다. `SKILL.md`는 1.3.0보다 554바이트 늘어 1.2.1 총량 제한을 이번에 넘었다.

**세션이 대신 정한 것**: 규칙의 유일한 위치를 DESIGN.md Report Form으로(스킬 없는 인계 세션이 읽는 문서), 설명 문단은 목록 뒤·도장 앞, R6·R7은 경고가 아닌 지적(종료 코드 1)이되 기존 보고가 깨지지 않는 조건만, 넷째 칸 어휘는 강제하지 않음.
