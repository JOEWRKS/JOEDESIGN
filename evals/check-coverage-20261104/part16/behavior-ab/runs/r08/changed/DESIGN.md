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
| C1 글자 수 위치: 요청 내용 칸 상자 아래 4px(`--space-1`), 오른쪽 끝이 칸 오른쪽 끝과 같음 | `tools/measure.mjs --inject src/style.css`, 높이 800: `#body-count` 상자 top − `#body` 상자 bottom = 4, `#body` right − `#body-count` right = 0 | 320x800 200자 캡처: 세로 check 4 / observed 9(칸 테두리 아래 끝 y304 → 글자 잉크 위 끝 y313), 오른쪽 check 0 / observed 0(테두리 x303, 잉크 x303); 375 빈 칸·1280 200자도 세로 9, 오른쪽 0 — 세로 판독 다름 | 요청 화면 | 320, 375, 768, 1280 | 빈 칸, 199자, 200자 | `<link>`로 실제 로드된 CSS(도구가 차단, 주입으로 측정), 높이 800 외, 포커스·글꼴 확대 | spot check differs (세로): 기준 해석 결정 전 미통과 — TASK.md#2026-11-17-r1-2-measure |
| C2 넘침 없음: 문서 가로 스크롤 없음(scrollWidth ≤ 화면 너비) | 같은 도구: `documentElement.scrollWidth`·`body.scrollWidth` ≤ `innerWidth` | 320x800 200자: check scrollWidth 320 ≤ 320 / observed `scrollTo(200,0)` 뒤 scrollX 0, 캡처 오른쪽 끝 열(x316–319) 빈 칸, 콘텐츠 오른쪽 끝 x304 | 요청 화면 | 320, 375, 768, 1280 | 빈 칸, 199자, 200자 | `<link>`로 실제 로드된 CSS, 높이 800 외, 띄어쓰기 없는 긴 영문 입력 | 12/12 (4 sizes x 3 states, rendered, spot-checked 320x800 200자) — TASK.md#2026-11-17-r1-2-measure |
