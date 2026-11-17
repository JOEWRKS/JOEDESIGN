# Visual rules and authority

Authority / version: PRODUCT.md rev 2 (DEC-002, RULE-002), 승인 2026-11-10.
Approved scope: 요청 화면(src/index.html), 라이트 모드, 너비 320·375·768·1280px.
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
| C1 글자 수 위치: 요청 내용 칸 상자 아래 4px(`--space-1`), 오른쪽 끝이 칸 오른쪽 끝과 같음 | `node tools/measure.mjs --inject src/style.css`, getBoundingClientRect: 아래 간격 = #body-count.top − #body.bottom, 오른쪽 차 = #body-count.right − #body.right | 320x800 200자 캡처: 오른쪽 차 check 0 / observed 0(칸 테두리 마지막 열 303, 글자 잉크 마지막 열 303); 아래 간격 check 4 / observed 9(테두리 마지막 행 303, 글자 잉크 첫 행 313) — 다름, 규칙 해석(상자 기준 vs 보이는 글자 기준) 소유자 결정 대기 | 요청 화면 | 320, 375, 768, 1280 (높이 800) | 빈 칸, 199자, 200자 | link로 불러온 CSS 렌더(도구가 막아 주입으로 대신), 포커스·칸 크기 조절·확대 상태, 800 외 높이 | TASK.md#2026-11-17-r1-2-measure |
| C2 넘침 없음: 문서 가로 스크롤 없음(scrollWidth ≤ 화면 너비) | `node tools/measure.mjs --inject src/style.css`, document.documentElement.scrollWidth ≤ clientWidth | 320x800 200자 캡처: check scrollWidth 320 / observed 가장 오른쪽 잉크 열 303(화면 320 안) | 요청 화면 | 320, 375, 768, 1280 (높이 800) | 빈 칸, 199자, 200자 | link로 불러온 CSS 렌더(도구가 막아 주입으로 대신), 포커스·칸 크기 조절·확대 상태 | TASK.md#2026-11-17-r1-2-measure |
