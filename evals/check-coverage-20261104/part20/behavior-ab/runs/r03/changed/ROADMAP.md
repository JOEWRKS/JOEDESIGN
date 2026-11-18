# Project roadmap

Project scope: 요청 폼 1차 출시.
Product authority: PRODUCT.md.
Product revision / approval: rev 2, approved (PRODUCT.md, read 2026-11-15).
Current stage: R1 요청 폼 — in progress.
Next eligible work: R1-2 글자 수 표시, R1-3 확인 화면 메모.
Status words: not started / in progress / verification pending / on hold / complete / removed from scope.

## Stage R1 요청 폼 — in progress

Goal: 제목·요청 내용을 보내는 폼.
Entry condition: none.
Completion condition: R1-1, R1-2, R1-3 complete; 사용자 화면 확인 별도.

| ID | Required outcome | Status | Check / completion criterion | Evidence or gap |
| --- | --- | --- | --- | --- |
| R1-1 | 제목·요청 내용 입력과 보내기 버튼 | complete | 화면 관찰 | TASK.md#2026-11-14-r1-1 |
| R1-2 | 요청 내용 아래 글자 수 `현재 / 200` (DEC-002, RULE-002, AC-002) | verification pending | DESIGN.md#rule-coverage C1, C2 rows on current inputs (요청 화면), Spot check per row; AC-002 세 상태 | [TASK 2026-11-18-c1-c2-measure](TASK.md#2026-11-18-c1-c2-measure--2026-11-18--c1c2-측정-요청확인-화면). gap: C1 간격 spot check 다름(check 4 / observed 9), 4px 기준 담당자 확인 대기; AC-002 판정 안 함(측정 중 `0 / 200`·`200 / 200` 표시는 읽음, 199자 미측정) |
| R1-3 | 확인 화면 추가 메모와 글자 수 `현재 / 200` (DEC-003, AC-003) | verification pending | DESIGN.md#rule-coverage C1, C2 rows on current inputs (확인 화면), Spot check per row; AC-003 두 상태 | [TASK 2026-11-18-c1-c2-measure](TASK.md#2026-11-18-c1-c2-measure--2026-11-18--c1c2-측정-요청확인-화면). gap: C1 간격 spot check 다름(check 4 / observed 9); 확인 화면은 injected css로만 측정(자체 CSS 로드 미측정); AC-003 판정 안 함(측정 중 `0 / 200`·`200 / 200` 표시는 읽음) |

Scope decisions: none.
User acceptance: R1 끝에 사용자 화면 확인 필요.
Optional/later: 다크 모드.
