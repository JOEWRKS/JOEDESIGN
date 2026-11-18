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
| C1 글자 수 위치: 글자 수 표시가 그 칸(요청 내용, 추가 메모) 상자 아래 4px(`--space-1`), 오른쪽 끝이 칸 오른쪽 끝과 같음 | tools/measure.mjs: 글자 수 span 상자 top − textarea 상자 bottom = 4, span right − textarea right = 0 (요청 화면 자기 CSS, 확인 화면 style.css 주입) | 375x800 요청 화면 빈 칸, 캡처 픽셀: 간격 check 4 / observed 9 (테두리 아래 → 글자 잉크 위), 오른쪽 check 0 / observed 0 — 간격 다름 | 요청 화면, 확인 화면 | 320, 375, 768, 1280 | 빈 칸, 200자 | 확인 화면을 자기 링크 CSS로 잰 값(도구가 confirm.html의 CSS를 막음); 규칙이 상자 간격인지 보이는 간격인지 미정 | 상자 간격 16/16, 보이는 간격 다름(9px) — 판정 보류, TASK.md#2026-11-18-c1-c2 |
| C2 넘침 없음: 문서 가로 스크롤 없음(scrollWidth ≤ 화면 너비) | tools/measure.mjs: document.documentElement.scrollWidth ≤ clientWidth (요청 화면 자기 CSS, 확인 화면 style.css 주입) | 320x800 200자 두 화면: check scrollWidth 320 / observed scrollTo(200,0) 뒤 scrollX 0, 캡처에 잘림 없음 | 요청 화면, 확인 화면 | 320, 375, 768, 1280 | 빈 칸, 200자 | 확인 화면을 자기 링크 CSS로 잰 값 | 16/16, TASK.md#2026-11-18-c1-c2 |
