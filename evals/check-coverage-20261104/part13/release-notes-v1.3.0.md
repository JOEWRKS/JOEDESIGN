## 1.3.0 — 재배치는 전후 표시 대조표로 판정 (2026-11-11, T043)

1.2.1에서 "재배치가 보이는 내용을 바꾸면 제품 결정 대기"라는 판정 문장은 효과가 없었다(에이전트가 표시를 바꾸고도 "위치만 바꿈"으로 분류). 1.3.0은 판정 문장 대신 대조표를 쓰게 한다. 스키마·계약·CLI·도장은 그대로다.

- `SKILL.md`: 기존 요소를 옮기거나 겹치거나 숨기거나 합치면 먼저 DESIGN.md와 보고에 `## Display before/after`를 요소마다 `before: element | content shown | route` / `after: ...` 두 줄로 적는다. 다르면 제품 결정 대기(JOEFLOW 재진입), 같으면 디자인 결정.
- `templates/DESIGN.md` Report Form에 같은 규칙 한 문단(인계 세션용), `references/conformance.md`에 R5 설명.
- `scripts/report-check.mjs` R5: 옮김·겹침·숨김·병합 완료 문장이 있는데 before/after 줄도 `display unchanged`도 없으면, 또는 쌍이 다른데 `product decision pending` 줄이 없으면 지적. 테스트 11→16.

**뺀 문장**(문구 총량 유지, SKILL.md 14,216→14,212바이트): 인계 문단 "The handoff tells that session to read DESIGN.md's Report Form section and report in that form."(재지 않음), "The script reads the form of the sentences, not whether a number is true."(다른 곳에 같은 말), "Review-only never gains write authority. The user need not prepare machine files or choose between a core and harness."(작업 종류 표와 중복).

**확인된 것**(Opus 89회, 1.2.1 대조군, README 13부):
- 한 턴: 표시가 바뀐 재배치의 제품 결정 대기 8/8 vs 1/8, 요소별 전후 대조 12/12 vs 0/12, 위치만 바꾼 과제 오탐 0(4/4 vs 4/4). 기능 추가·인계 24건·8부 회귀는 같거나 높음(인계 결과 목록 11 vs 10, `fixed`/`changed` 11 vs 9, 범위 3 vs 2). state.json 읽기 21/24 vs 13/24.
- R5: 기존 보고 306건에서 R1~R4 결과 변화 0, 재배치 보고 21/21 감지, 그 밖 285건 중 16건 걸림.
- 40턴(새 고정물, 9부 G와 같은 채점기로 함께 재채점): h2 33 vs 27, 8개 전부 29 vs 20, 함정 h4·h6·h8 40/40, 주 세션 35턴 report-check 실행·도장 일치 35/35, 라이브 대조 24행 일치.

**확인되지 않은 것**: (1) 전후 줄의 내용 칸을 추상적으로 적으면 실제 글자가 바뀌어도 쌍이 같아져 스크립트가 못 잡는다. (2) 40턴에서 h1(38 vs 39)과 인계 h3·h7(각 4 vs 5)이 각 1턴 낮다(전후 대조와 무관한 보고 누락). (3) 셀당 n=3~4, 장면별 채점기 1명, 40턴 세션 1개, 대국 화면은 가짜 엔진. (4) JOENESS 쪽 도장 소비는 별도.

**사고**: 1.2.1 버전 커밋에 이 작업의 미완성 R5가 섞였다가 06573af에서 되돌려졌다. 40턴 첫 시도는 코디네이터가 백로그 밖 메시지를 보내 무효 처리하고 처음부터 다시 돌렸다(`evals/check-coverage-20261104/part13/longterm-J-void1/`).
