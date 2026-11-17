# Visual rules and authority

Authority / version: PRODUCT.md rev 2 (DEC-002, RULE-002), 승인 2026-11-10.
Approved scope: 요청 화면(src/index.html), 라이트 모드, 너비 320·375·768·1280px.
Visual rules: 간격은 `src/style.css`의 `--space-*` 토큰만 쓴다. 아래 표의 규칙.
Proposed changes: none.
Not applicable / pending: 다크 모드는 승인 범위 밖. C1의 "4px"가 요소 상자 간격인지 보이는 간격(칸 테두리 → 글자)인지 소유자 결정 대기 (2026-11-17 측정: 상자 4 / 보이는 9).
Execution proof: TASK.md 항목 링크.

## Rule coverage

One row per measurable rule; a ROADMAP design Check names these rows. A rule with no
check is unmeasured, never passed. Result links the latest TASK entry; no copied log.
If the project uses JOEDESIGN's DESIGN template, keep one DESIGN.md and its Rule
Coverage table as this table (add Result if absent); never keep two rule tables.

| Rule | Check | Spot check | Layouts | Sizes | States | Unmeasured | Result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C1 글자 수 위치: 요청 내용 칸 상자 아래 4px(`--space-1`), 오른쪽 끝이 칸 오른쪽 끝과 같음 | `tools/measure.mjs --inject src/style.css` (도구가 링크 CSS를 막아 같은 CSS 주입): `#body-count` top − `#body` bottom = 4, 두 요소 right 차이 = 0 (getBoundingClientRect) | 320x800 200자: 간격 check 4 / observed 9 (칸 테두리 마지막 행 303 → 숫자 잉크 첫 행 313, 캡처 픽셀) — differs; 오른쪽 check 0 / observed 0 (숫자 잉크 끝 열 303 = 칸 오른쪽 테두리 열 303) | 요청 화면 | 320, 375, 768, 1280 (높이 800) | 빈 칸, 199자, 200자 | "4px"가 요소 상자 간격인지 보이는 간격인지 미확정이라 간격 결과는 미인정; 링크 CSS 그대로 로드한 화면; 칸 세로 크기 조절 후; 다른 글꼴 환경 | 간격 12/12 at 4 (spot check differs, 미인정), 오른쪽 12/12 at 0 — TASK.md#2026-11-17-r1-2-measure |
| C2 넘침 없음: 문서 가로 스크롤 없음(scrollWidth ≤ 화면 너비) | `tools/measure.mjs --inject src/style.css`: `documentElement.scrollWidth` ≤ `innerWidth` | 320x800 200자 캡처: check scrollWidth 320 / observed 가장 오른쪽 내용 x=303, 마지막 열 319 빈칸 | 요청 화면 | 320, 375, 768, 1280 (높이 800) | 빈 칸, 199자, 200자 (한글); 320에서 띄어쓰기 없는 영문 200자 추가 | 링크 CSS 그대로 로드한 화면; 칸 세로 크기 조절 후; 다른 글꼴 환경 | 12/12 — TASK.md#2026-11-17-r1-2-measure |
