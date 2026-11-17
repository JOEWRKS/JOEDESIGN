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
Result: 코드 변경 없음. C1·C2와 AC-002 문구를 측정, DESIGN.md#rule-coverage C1·C2 행 갱신.
Check / target / result: `tools/measure.mjs --inject src/style.css`, 320·375·768·1280 x 빈 칸·199자·200자, light, rendered (injected css). C1 간격 12/12 at 4 (spot check differs: 4 / 9), C1 오른쪽 12/12 at 0, C2 12/12, AC-002 12/12 — 스팟 체크는 DESIGN 행 참조.
Evidence: 결과 줄과 질문은 REPORT.md; 측정 스크립트·캡처는 .work/ (미추적 임시).
Limits: 도구가 링크 CSS를 막아 주입 CSS로만 측정; 칸 세로 크기 조절·다른 글꼴 미측정.
Report stamp: report-check: ok 2,109 chars f5359ff9
Completion boundaries: C1 간격 결과 미인정(4px 의미 소유자 결정 대기); R1-2 verification pending; user acceptance pending.
Related issue / knowledge: DESIGN.md Not applicable / pending 줄.
Record handoff gap: none.
