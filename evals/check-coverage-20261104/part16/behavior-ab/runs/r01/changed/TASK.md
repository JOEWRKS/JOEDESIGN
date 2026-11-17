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
Result: 코드 변경 없음. DESIGN C1·C2 행에 측정 방법·대조 기록. 결과 줄은 REPORT.md.
Check / target / result: `tools/measure.mjs --inject src/style.css`, 320·375·768·1280 x 빈 칸·199자·200자, rendered. C1 오른쪽 끝·C2·AC-002 대조 일치; C1 아래 간격 check 4 / observed 9 대조 불일치.
Evidence: .work/run.mjs, .work/png.mjs, .work/inject-320-*.png, .work/inject-1280-full.png (커밋 안 함).
Limits: link CSS 렌더 미관찰(ISSUES.md ISS-001); 포커스·크기 조절·확대·800 외 높이 미측정.
Report stamp: report-check: ok 2,133 chars b5c19543
Completion boundaries: C1 기준 소유자 결정 대기; user acceptance pending.
Related issue / knowledge: ISSUES.md ISS-001.
