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
| C1 글자 수 위치: 요청 내용 칸 상자 아래 4px(`--space-1`), 오른쪽 끝이 칸 오른쪽 끝과 같음 | `tools/measure.mjs --inject src/style.css`: `#body-count` 상자 top − `#body` 상자 bottom = 4, 두 상자 right 차 = 0 | 320x800 200자: 간격 check 4 / observed 9(캡처 픽셀, 칸 테두리 아래 끝~글자 잉크 위 끝) — differs; 오른쪽 check 0 / observed 0 | 요청 화면 | 320, 375, 768, 1280 (높이 800) | 빈 칸, 199자, 200자 | 링크된 style.css 로드 경로(도구가 차단, 주입으로 대체); 높이 800 외; 칸 크기 조절 후 | 상자 기준 12/12, 간격 spot check differs → 미통과, 규칙 뜻 결정 대기 (TASK.md#2026-11-17-r1-2-measure) |
| C2 넘침 없음: 문서 가로 스크롤 없음(scrollWidth ≤ 화면 너비) | `tools/measure.mjs --inject src/style.css`: `documentElement.scrollWidth ≤ clientWidth` | 320x800 200자: check scrollWidth 320 / clientWidth 320; observed 캡처 가장 오른쪽 칠한 열 303, 오른쪽 여백 16px, 잘린 가장자리 없음 — agrees | 요청 화면 | 320, 375, 768, 1280 (높이 800) | 빈 칸, 199자, 200자 | 링크된 style.css 로드 경로(도구가 차단, 주입으로 대체); 높이 800 외; 제목 칸 긴 입력 | 12/12, spot-checked; 링크 경로 미측정 (TASK.md#2026-11-17-r1-2-measure) |
