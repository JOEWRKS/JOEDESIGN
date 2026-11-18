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
| C1 글자 수 위치: 글자 수 표시가 그 칸(요청 내용, 추가 메모) 상자 아래 4px(`--space-1`), 오른쪽 끝이 칸 오른쪽 끝과 같음 | `node tools/measure.mjs` 렌더 측정: getBoundingClientRect로 글자 수 top − 칸 bottom = 4, 글자 수 right − 칸 right = 0. 확인 화면은 도구가 링크 CSS를 막아 `--inject src/style.css` | 요청 화면 320x800 200자: 간격 check 4 / observed 9 (칸 테두리와 숫자 잉크 사이 빈 줄, 다름), 오른쪽 끝 check 0 / observed 0. 확인 화면 320x800 200자(injected css): 간격 check 4 / observed 9 (다름), 오른쪽 끝 check 0 / observed 0 | 요청 화면, 확인 화면 | 320, 375, 768, 1280 | 빈 칸, 200자 | 확인 화면 자체 CSS 로드(도구가 차단), 높이 800 외. 간격은 spot check가 달라 결과로 세지 않음(4px이 상자 기준인지 보이는 글자 기준인지 담당자 확인 대기) | [TASK 2026-11-18-c1-c2-measure](TASK.md#2026-11-18-c1-c2-measure--2026-11-18--c1c2-측정-요청확인-화면) |
| C2 넘침 없음: 문서 가로 스크롤 없음(scrollWidth ≤ 화면 너비) | `node tools/measure.mjs` 렌더 측정: document.documentElement.scrollWidth ≤ innerWidth. 확인 화면은 `--inject src/style.css` | 요청 화면 320x800 200자: check scrollWidth 320 / observed scrollTo(500,0) 뒤 scrollX 0, 캡처 오른쪽 끝 잉크 303px. 확인 화면 320x800 200자(injected css): check 320 / observed scrollX 0, 잉크 303px | 요청 화면, 확인 화면 | 320, 375, 768, 1280 | 빈 칸, 200자 | 확인 화면 자체 CSS 로드(도구가 차단), 높이 800 외 | [TASK 2026-11-18-c1-c2-measure](TASK.md#2026-11-18-c1-c2-measure--2026-11-18--c1c2-측정-요청확인-화면) |
