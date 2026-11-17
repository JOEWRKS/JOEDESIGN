# Visual rules and authority

Authority / version: PRODUCT.md rev 2 (DEC-002, RULE-002), 승인 2026-11-10.
Approved scope: 요청 화면(src/index.html), 라이트 모드, 너비 320·375·768·1280px.
Visual rules: 간격은 `src/style.css`의 `--space-*` 토큰만 쓴다. 아래 표의 규칙.
Proposed changes: none.
Not applicable / pending: 다크 모드는 승인 범위 밖.
Execution proof: TASK.md 항목 링크 (최신: TASK.md#2026-11-17-r1-2-measure).

## Rule coverage

One row per measurable rule; a ROADMAP design Check names these rows. A rule with no
check is unmeasured, never passed. Result links the latest TASK entry; no copied log.
If the project uses JOEDESIGN's DESIGN template, keep one DESIGN.md and its Rule
Coverage table as this table (add Result if absent); never keep two rule tables.

| Rule | Check | Spot check | Layouts | Sizes | States | Unmeasured | Result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C1 글자 수 위치: 요청 내용 칸 상자 아래 4px(`--space-1`), 오른쪽 끝이 칸 오른쪽 끝과 같음 | rendered: `tools/measure.mjs --inject src/style.css`, `#body` 아래 끝 → `#body-count` 위 끝(요소 상자), 두 요소 오른쪽 끝 차이 | 320x800 200자: 간격 check 4 / observed 9(캡처, 칸 테두리 마지막 줄 → 숫자 잉크 첫 줄) 다름; 오른쪽 끝 check 0 / observed 0(테두리 열 = 숫자 잉크 끝 열) | 요청 화면 | 320, 375, 768, 1280 | 빈 칸, 199자, 200자(한글·영문) | 다크 모드(범위 밖); 링크된 CSS 대신 주입 CSS로 측정; 간격 규칙이 요소 상자인지 보이는 간격인지 미정 | 간격 상자 4px 16/16, 보이는 간격 9px로 spot check 다름 → 미판정(소유자 결정 대기); 오른쪽 끝 16/16. [TASK](TASK.md#2026-11-17-r1-2-measure) |
| C2 넘침 없음: 문서 가로 스크롤 없음(scrollWidth ≤ 화면 너비) | rendered: `tools/measure.mjs --inject src/style.css`, `documentElement`·`body` scrollWidth ≤ innerWidth | 320x800 200자: check 320 ≤ 320 / observed 캡처 오른쪽 끝 열 잉크 0px, 글자 수 잉크 끝 x=303, scrollTo(200,0) 뒤 scrollX 0 | 요청 화면 | 320, 375, 768, 1280 | 빈 칸, 199자, 200자(한글·영문) | 다크 모드(범위 밖); 링크된 CSS 대신 주입 CSS로 측정 | 16/16 (4 sizes x 4 states, rendered, spot check 320x800 일치). [TASK](TASK.md#2026-11-17-r1-2-measure) |
