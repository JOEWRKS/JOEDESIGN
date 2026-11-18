# Visual rules and authority

Authority / version: PRODUCT.md rev 2 (DEC-002, RULE-002), 승인 2026-11-10.
Approved scope: 요청 화면(src/index.html), 확인 화면(src/confirm.html), 라이트 모드, 너비 320·375·768·1280px.
Visual rules: 간격은 `src/style.css`의 `--space-*` 토큰만 쓴다. 아래 표의 규칙.
Proposed changes: none.
Not applicable / pending: 다크 모드는 승인 범위 밖.
Execution proof: TASK.md 항목 링크.

## Rule coverage

One row per measurable rule; a ROADMAP design Check names these rows. A rule with no
check is unmeasured, never passed. Result links the latest TASK entry; no copied log.
If the project uses JOEDESIGN's DESIGN template, keep one DESIGN.md and its Rule
Coverage table as this table (add Result if absent); never keep two rule tables.

| Rule | Check | Spot check | Layouts | Sizes | States | Unmeasured | Result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C1 글자 수 위치: 글자 수 표시가 그 칸(요청 내용, 추가 메모) 상자 아래 4px(`--space-1`), 오른쪽 끝이 칸 오른쪽 끝과 같음 | tools/measure.mjs: textarea와 .char-count의 getBoundingClientRect, 세로 c.top−t.bottom = 4, 가로 c.right−t.right = 0 | 요청 화면 320 빈 칸: 세로 check 4 / observed 9 (캡처, 상자 아래 테두리 행 303 → 글자 잉크 첫 행 313), differs; 가로 check 0 / observed 0 (테두리 열 303, 잉크 오른쪽 열 303). 확인 화면 320 빈 칸(주입 CSS): 세로 check 4 / observed 9, differs; 가로 check 0 / observed 0 | 요청 화면, 확인 화면 | 320, 375, 768, 1280 | 빈 칸, 200자 | 확인 화면을 자체 CSS로 연 상태(도구가 confirm.html의 링크 CSS를 막음, 주입 CSS로만 측정); 세로 4px가 상자 간격인지 보이는 간격인지 미정(소유자 질문) | spot check differs (세로): TASK.md#2026-11-18-c1-c2 |
| C2 넘침 없음: 문서 가로 스크롤 없음(scrollWidth ≤ 화면 너비) | tools/measure.mjs: document.documentElement.scrollWidth ≤ innerWidth | 요청 화면 320 빈 칸: check scrollWidth 320 / observed 캡처 오른쪽 끝 내용 열 303 (< 320). 확인 화면 320 빈 칸(주입 CSS): check 320 / observed 303 | 요청 화면, 확인 화면 | 320, 375, 768, 1280 | 빈 칸, 200자 | 확인 화면을 자체 CSS로 연 상태; 다른 높이·상태 | TASK.md#2026-11-18-c1-c2 |
