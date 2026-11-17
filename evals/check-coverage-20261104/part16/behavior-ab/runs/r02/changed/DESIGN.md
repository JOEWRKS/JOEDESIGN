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
| C1 글자 수 위치: 요청 내용 칸 상자 아래 4px(`--space-1`), 오른쪽 끝이 칸 오른쪽 끝과 같음 | `tools/measure.mjs --inject src/style.css`: `#body-count` 상자 top − `#body` 상자 bottom = 4, right 차이 = 0 (getBoundingClientRect) | 320x900 200자: 간격 check 4 / observed 9 (테두리 아래 끝 → 숫자 잉크 위 끝, 캡처) — 다름; 오른쪽 끝 check 0 / observed 0 | 요청 화면 | 320, 375, 768, 1280 (높이 900) | 빈 칸, 199자, 200자 | 페이지 자체 CSS 로드(도구가 링크 CSS 차단, 주입으로 측정), 다른 높이·브라우저·OS 글꼴, 키보드 입력(스크립트 input 이벤트로 상태 생성) | 상자 12/12, 보이는 간격 9px로 규칙과 다름 → 통과 아님, 해석 결정 대기 (TASK.md#2026-11-17-r1-2-measure, ISSUES.md#i-001) |
| C2 넘침 없음: 문서 가로 스크롤 없음(scrollWidth ≤ 화면 너비) | `tools/measure.mjs --inject src/style.css`: `documentElement.scrollWidth ≤ innerWidth` | 320x900 200자: check scrollWidth 320 ≤ 320 / observed 가장 오른쪽 그려진 열 x=303 (오른쪽 16px 여백, 캡처) | 요청 화면 | 320, 375, 768, 1280 (높이 900) | 빈 칸, 199자, 200자 | 페이지 자체 CSS 로드(주입으로 측정), 다른 높이·브라우저·OS 글꼴 | 12/12 (4 sizes x 3 states, rendered (injected css), spot-checked) (TASK.md#2026-11-17-r1-2-measure) |
