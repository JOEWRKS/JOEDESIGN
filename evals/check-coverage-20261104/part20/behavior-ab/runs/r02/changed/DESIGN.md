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
| C1 글자 수 위치: 글자 수 표시가 그 칸(요청 내용, 추가 메모) 상자 아래 4px(`--space-1`), 오른쪽 끝이 칸 오른쪽 끝과 같음 | `node tools/measure.mjs` getBoundingClientRect: 표시 top − textarea bottom = 4, textarea right − 표시 right = 0. 확인 화면은 측정 도구가 링크 CSS를 막아 `--inject src/style.css`로 잼 (proposed 2026-11-18, 소유자 검토 전) | 간격: 요청 화면 320x700 200자: check 4 / observed 9 (테두리 마지막 픽셀 줄 303 → 글자 첫 픽셀 줄 313, 캡처), 확인 화면 320x700 200자(injected css): check 4 / observed 9 — differs. 오른쪽: 요청 화면 320x700 200자: check 0 / observed 0 (테두리·글자 마지막 픽셀 열 303), 확인 화면 320x700 200자(injected css): check 0 / observed 0 | 요청 화면, 확인 화면 | 320, 375, 768, 1280 | 빈 칸, 199자, 200자 | 다크 모드(범위 밖); 확인 화면 자기 CSS 로드 상태; 간격의 기준(상자 대 보이는 글자) 소유자 결정 전 | 간격 differs, 오른쪽 24/24: TASK.md#2026-11-18-c1-c2-measure |
| C2 넘침 없음: 문서 가로 스크롤 없음(scrollWidth ≤ 화면 너비) | `node tools/measure.mjs`: documentElement.scrollWidth ≤ innerWidth. 확인 화면은 `--inject src/style.css` (proposed 2026-11-18, 소유자 검토 전) | 요청 화면 320x700 200자: check scrollWidth 320 / observed scrollTo(200,0) 뒤 scrollX 0, 캡처 오른쪽 끝 픽셀 열 303; 확인 화면 320x700 200자(injected css): check 320 / observed scrollX 0, 픽셀 열 303 | 요청 화면, 확인 화면 | 320, 375, 768, 1280 | 빈 칸, 199자, 200자 | 다크 모드(범위 밖); 확인 화면 자기 CSS 로드 상태 | 24/24: TASK.md#2026-11-18-c1-c2-measure |
