# Project roadmap

Project scope: 요청 폼 1차 출시.
Product authority: PRODUCT.md.
Product revision / approval: rev 2, approved (PRODUCT.md, read 2026-11-15).
Current stage: R1 요청 폼 — in progress.
Next eligible work: R1-2 글자 수 표시 — C1 간격 해석 결정(ISSUES.md#i-001) 후 C1 재측정; C2·AC-002는 측정됨.
Status words: not started / in progress / verification pending / on hold / complete / removed from scope.

## Stage R1 요청 폼 — in progress

Goal: 제목·요청 내용을 보내는 폼.
Entry condition: none.
Completion condition: R1-1, R1-2 complete; 사용자 화면 확인 별도.

| ID | Required outcome | Status | Check / completion criterion | Evidence or gap |
| --- | --- | --- | --- | --- |
| R1-1 | 제목·요청 내용 입력과 보내기 버튼 | complete | 화면 관찰 | TASK.md#2026-11-14-r1-1 |
| R1-2 | 요청 내용 아래 글자 수 `현재 / 200` (DEC-002, RULE-002, AC-002) | verification pending | DESIGN.md#rule-coverage C1, C2 rows on current inputs, Spot check per row; AC-002 세 상태 | TASK.md#2026-11-17-r1-2-measure: C2 12/12 (4 sizes x 3 states, rendered (injected css), spot-checked), AC-002 세 상태 표시 맞음; C1 상자 4px이나 보이는 간격 9px로 다름 → 열림 (ISSUES.md#i-001); 페이지 자체 CSS 로드 상태 미측정 |

Scope decisions: none.
User acceptance: R1 끝에 사용자 화면 확인 필요.
Optional/later: 다크 모드.
