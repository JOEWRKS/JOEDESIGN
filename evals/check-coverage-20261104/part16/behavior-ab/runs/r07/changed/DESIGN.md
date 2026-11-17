# Visual rules and authority

Authority / version: PRODUCT.md rev 2 (DEC-002, RULE-002), 승인 2026-11-10.
Approved scope: 요청 화면(src/index.html), 라이트 모드, 너비 320·375·768·1280px.
Visual rules: 간격은 `src/style.css`의 `--space-*` 토큰만 쓴다. 아래 표의 규칙.
Proposed changes: none.
Open decision: C1의 "4px"가 글자 수 상자 기준인지 보이는 글자(잉크) 기준인지 — 제품/디자인 책임자 확인 대기(2026-11-17, 측정 상자 4px·보이는 간격 9px).
Not applicable / pending: 다크 모드는 승인 범위 밖.
Execution proof: TASK.md 항목 링크.

## Rule coverage

One row per measurable rule; a ROADMAP design Check names these rows. A rule with no
check is unmeasured, never passed. Result links the latest TASK entry; no copied log.
If the project uses JOEDESIGN's DESIGN template, keep one DESIGN.md and its Rule
Coverage table as this table (add Result if absent); never keep two rule tables.

| Rule | Check | Spot check | Layouts | Sizes | States | Unmeasured | Result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C1 글자 수 위치: 요청 내용 칸 상자 아래 4px(`--space-1`), 오른쪽 끝이 칸 오른쪽 끝과 같음 | `tools/measure.mjs` (--inject src/style.css): #body-count 상자 top − #body 상자 bottom = 4, right 차 = 0 | 320x800 200자 캡처: 세로 check 4 / observed 9(칸 테두리 아래 ~ 글자 잉크 위 빈 행), 오른쪽 check 0 / observed 0 — 세로 불일치 | 요청 화면 | 320, 375, 768, 1280 | 빈 칸, 199자, 200자 | 보이는 글자 기준 세로 간격(규칙 기준 미정), linked CSS 실제 로드, 칸 크기 조절 후, 글꼴 확대 | 12/12, spot check differs (TASK.md#2026-11-17-r1-2-measure) |
| C2 넘침 없음: 문서 가로 스크롤 없음(scrollWidth ≤ 화면 너비) | `tools/measure.mjs` (--inject src/style.css): documentElement·body scrollWidth ≤ innerWidth | 320x800 200자 캡처: check scrollWidth 320 ≤ 320 / observed 가장 오른쪽 칠해진 열 303, 마지막 열 어두운 픽셀 0 | 요청 화면 | 320, 375, 768, 1280 | 빈 칸, 199자, 200자 | linked CSS 실제 로드, 칸 크기 조절 후, 글꼴 확대 | 12/12 (TASK.md#2026-11-17-r1-2-measure) |
