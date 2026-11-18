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
| C1 글자 수 위치: 글자 수 표시가 그 칸(요청 내용, 추가 메모) 상자 아래 4px(`--space-1`), 오른쪽 끝이 칸 오른쪽 끝과 같음 | `tools/measure.mjs` 렌더 상자: 글자 수 top − textarea bottom = 4px, textarea right − 글자 수 right = 0px (2026-11-18 제안, 독립 검토 안 됨) | 요청 화면 320x800 200자 — 간격: check 4 / observed 9 (캡처 픽셀, 테두리 아래 ~ 글자 잉크 위), 다름; 오른쪽 끝: check 0 / observed 0 (캡처). 확인 화면 320x800 200자(주입 CSS)도 같은 값 | 요청 화면, 확인 화면 | 320, 375, 768, 1280 | 빈 칸, 200자 | 확인 화면이 자기 링크 CSS를 읽은 상태(도구가 막음, 주입 CSS로 잼); 높이 800 외 | 간격 spot check 다름 → 규칙 뜻(상자/보이는 간격) 책임자 확인 대기. TASK.md#2026-11-18-c1-c2-measure |
| C2 넘침 없음: 문서 가로 스크롤 없음(scrollWidth ≤ 화면 너비) | `tools/measure.mjs` 렌더: documentElement.scrollWidth ≤ innerWidth (2026-11-18 제안, 독립 검토 안 됨) | 요청 화면 320x800 200자: check scrollWidth 320 / observed 가로 스크롤 시도 전후 캡처 차이 0px, 가장 오른쪽 잉크 열 303. 확인 화면 320x800 200자(주입 CSS)도 같음 | 요청 화면, 확인 화면 | 320, 375, 768, 1280 | 빈 칸, 200자 | 확인 화면이 자기 링크 CSS를 읽은 상태; 높이 800 외 | 16/16, spot check 일치(확인 화면은 주입 CSS). TASK.md#2026-11-18-c1-c2-measure |
