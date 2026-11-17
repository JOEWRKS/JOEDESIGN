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

## 2026-11-17-r1-2-measure / 2026-11-17 / 글자 수 표시 C1·C2 측정

Roadmap item: ROADMAP.md#stage-r1-요청-폼--in-progress R1-2.
Result: 코드 변경 없음. DESIGN.md#rule-coverage C1·C2 행 측정, 320·375·768·1280 x 빈 칸·199자·200자, 라이트.
Check / target / result: C1 12/12, C2 12/12, AC-002 글자 12/12 — rendered (injected css): 측정 도구가 linked CSS를 막아(loaded=false) src/style.css를 주입.
Spot check: C1 320 200자 캡처 세로 check 4 / observed 9(불일치), 오른쪽 0/0; C2 320 200자 check 320≤320 / observed 마지막 열 어두운 픽셀 0.
Evidence: 임시 .work/run-c1c2.mjs, .work/c1c2-result.json, .work/shot-*.png (커밋 대상 아님).
Limits: linked CSS 실제 로드, 칸 크기 조절, 글꼴 확대, 다른 높이 미측정.
Report stamp: report-check: ok 2,556 chars 98b07a3e
Completion boundaries: C1 기준 결정 대기로 verification pending; user acceptance pending.
