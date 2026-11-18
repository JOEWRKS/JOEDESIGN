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
| C1 글자 수 위치: 글자 수 표시가 그 칸(요청 내용, 추가 메모) 상자 아래 4px(`--space-1`), 오른쪽 끝이 칸 오른쪽 끝과 같음 | `tools/measure.mjs` getBoundingClientRect: `.char-count` top − textarea bottom = 4, right 차 = 0 (확인 화면은 `--inject src/style.css`) | 요청 화면 375x800 200자: check 세로 4 / observed 9(테두리 아래 행 303 → 글자 잉크 첫 행 313, 캡처 픽셀), 오른쪽 check 0 / observed 0 — 세로 차이 남(box 기준인지 잉크 기준인지 미정) | 요청 화면, 확인 화면 | 320, 375, 768, 1280 | 빈 칸, 200자 | 다크 모드(범위 밖), 199자, 확인 화면 자체 CSS 적용 렌더(도구가 확인 화면 연결 CSS 차단), 실제 브라우저 | 16/16 box 기준, spot check differs (TASK.md#2026-11-18-c1-c2) |
| C2 넘침 없음: 문서 가로 스크롤 없음(scrollWidth ≤ 화면 너비) | `tools/measure.mjs`: documentElement.scrollWidth ≤ innerWidth (확인 화면은 `--inject src/style.css`) | 요청 화면 320x800 200자: check scrollWidth 320 ≤ 320 / observed 캡처 오른쪽 끝 잉크 열 303, 오른쪽 16열 빈칸 | 요청 화면, 확인 화면 | 320, 375, 768, 1280 | 빈 칸, 200자 | 다크 모드(범위 밖), 199자, 확인 화면 자체 CSS 적용 렌더, 실제 브라우저 | 16/16 (TASK.md#2026-11-18-c1-c2) |
