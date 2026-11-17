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
Result: 화면 코드 변경 없음. DESIGN.md#rule-coverage C1·C2 행 측정·spot check.
Check / target / result: `tools/measure.mjs --inject src/style.css`(도구가 `<link>` CSS 차단), 320·375·768·1280 x 빈 칸·199자·200자, 높이 800, light, rendered. C2 12/12 (4 sizes x 3 states, rendered, spot check 320x800 200자: check 320 / observed scrollX 0). C1 상자 12/12이나 spot check 세로 다름 (check 4 / observed 9, 캡처 픽셀) → 미통과. AC-002 세 문구 DOM 확인.
Evidence: 결과 줄과 판독은 DESIGN.md C1·C2 행; 보조 스크립트·캡처는 `.work/`(임시, 기록 외).
Limits: `<link>` CSS 로드, 다른 높이, 포커스·글꼴 확대, 긴 영문 입력 미측정.
Report stamp: report-check: ok 2,279 chars 476545fd
Completion boundaries: C1 기준 해석(상자 vs 보이는 글자) 소유자 결정 대기; user acceptance pending.
