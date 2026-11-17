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
| C1 글자 수 위치: 요청 내용 칸 상자 아래 4px(`--space-1`), 오른쪽 끝이 칸 오른쪽 끝과 같음 | `tools/measure.mjs` 렌더(링크 CSS 차단 → `src/style.css` 주입): `#body-count` 상자 top − `#body` 상자 bottom = 4, right 차이 = 0 | 320x700 200자: 간격 check 4 / observed 9 (테두리 아래 끝 y303 → 글자 잉크 첫 줄 y313, 캡처 픽셀), 오른쪽 끝 check 0 / observed 0 (잉크 오른쪽 x303 = 칸 테두리 x303) — 간격 다름: 4px가 상자 기준인지 보이는 글자 기준인지 소유자 판단 대기 | 요청 화면 | 320, 375, 768, 1280 | 빈 칸, 199자, 200자 | 페이지 자체 CSS 로드(주입으로만 렌더), 다크 모드(범위 밖), 칸 크기 조절 후 | 상자 12/12, 간격 spot check 다름 → not passed ([TASK](TASK.md#2026-11-17-r1-2-measure)) |
| C2 넘침 없음: 문서 가로 스크롤 없음(scrollWidth ≤ 화면 너비) | `tools/measure.mjs` 렌더(`src/style.css` 주입): `documentElement.scrollWidth` ≤ `innerWidth` | 320x700 200자: check scrollWidth 320 ≤ 320 / observed `scrollTo(200,0)` 후 scrollX 0, 캡처 x305–319 전 높이 빈 칸(가장 오른쪽 잉크 x303) | 요청 화면 | 320, 375, 768, 1280 | 빈 칸, 199자, 200자 | 페이지 자체 CSS 로드(주입으로만 렌더), 다크 모드(범위 밖) | 12/12 ([TASK](TASK.md#2026-11-17-r1-2-measure)) |
