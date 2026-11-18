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
| C1 글자 수 위치: 글자 수 표시가 그 칸(요청 내용, 추가 메모) 상자 아래 4px(`--space-1`), 오른쪽 끝이 칸 오른쪽 끝과 같음 | `node tools/measure.mjs` 렌더 상자: 글자 수 top − 칸 bottom(간격), 칸 right − 글자 수 right(오른쪽 끝) | gap: 요청 화면 375 빈 칸: check 4 / observed 9 (칸 테두리 아래~글자 잉크 위, 캡처) — 어긋남; right edge: 요청 화면 375 빈 칸: check 0 / observed 0 (캡처) | 요청 화면, 확인 화면 | 320, 375, 768, 1280 | 빈 칸, 199자, 200자 | 확인 화면 자기 CSS 로드 상태(도구가 막아 style.css 주입으로 잼, ISSUES#iss-002) | not passed: gap 스폿 체크 어긋남(ISSUES#iss-001), TASK.md#2026-11-18-c1-c2-measure |
| C2 넘침 없음: 문서 가로 스크롤 없음(scrollWidth ≤ 화면 너비) | `node tools/measure.mjs`: documentElement.scrollWidth ≤ innerWidth | 요청 화면 320 200자: check 320 / observed 오른쪽 끝 칠해진 열 x=303, 화면 320 안 (캡처) | 요청 화면, 확인 화면 | 320, 375, 768, 1280 | 빈 칸, 199자, 200자 | 확인 화면 자기 CSS 로드 상태(ISSUES#iss-002) | 24/24 (4 sizes x 3 states x 2 화면, 확인 화면은 rendered (injected css); spot check: check 320 / observed 303 안), TASK.md#2026-11-18-c1-c2-measure |
