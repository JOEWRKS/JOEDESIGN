# Work results

## 2026-11-14-r1-1 / 2026-11-14 / 요청 폼 기본 화면

Roadmap item: ROADMAP.md#stage-r1-요청-폼--in-progress R1-1.
Result: 제목·요청 내용 칸과 보내기 버튼.
Changed files: src/index.html, src/style.css.
Check / target / result: 375px 화면 관찰, 세 요소 보임.
Evidence: 없음(관찰).
Limits: 다른 크기 미관찰.
Report stamp: none ran.
Required specialist verdict: not applicable.
Completion boundaries: implementation done; user acceptance pending.
Related issue / knowledge: none.
Record handoff gap: none.

## 2026-11-14-r1-2 / 2026-11-14 / 글자 수 표시 구현

Roadmap item: ROADMAP.md#stage-r1-요청-폼--in-progress R1-2.
Result: 요청 내용 칸 아래 오른쪽에 `현재 / 200` 표시, 입력마다 갱신.
Changed files: src/index.html (표시와 갱신 스크립트), src/style.css (.char-count).
Check / target / result: 코드 읽기만. C1·C2 측정 안 함.
Evidence: 없음.
Limits: 렌더 측정 없음.
Report stamp: none ran.
Required specialist verdict: not applicable.
Completion boundaries: implementation done; visual check pending; user acceptance pending.
Related issue / knowledge: none.
Record handoff gap: none.

## 2026-11-17-r1-2-measure / 2026-11-17 / R1-2 C1·C2 측정

Roadmap item: ROADMAP.md#stage-r1-요청-폼--in-progress R1-2.
Result: C2 12/12 (4 sizes x 3 states, rendered (injected css), spot-checked). C1 상자 값 12/12이나 spot check 다름(320x900 200자: check 4 / observed 9) → 통과 아님, ISSUES.md#i-001. AC-002 표시 `0 / 200`·`199 / 200`·`200 / 200` 맞음. 코드 변경 없음.
Changed files: DESIGN.md (C1·C2 행), ROADMAP.md (R1-2 근거·다음 작업), ISSUES.md (I-001).
Check / target / result: `tools/measure.mjs --inject src/style.css`, 320·375·768·1280 x 900, 빈 칸·199자·200자, light; 결과 목록은 REPORT.md.
Evidence: .work/results.json, .work/shot-*.png (로컬 임시, 커밋 안 됨).
Limits: 도구가 링크 CSS를 막아 style.css를 주입해 측정; 페이지 자체 CSS 로드, 다른 높이·브라우저, 키보드 입력 미측정.
Report stamp: report-check: ok 2,479 chars d23f0a19 (REPORT.md)
Completion boundaries: C1 해석 결정 대기; user acceptance pending.
