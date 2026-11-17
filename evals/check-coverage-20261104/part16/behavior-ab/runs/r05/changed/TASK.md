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

Roadmap item: ROADMAP.md#stage-r1-요청-폼--in-progress R1-2 (verification pending 유지).
Result: 코드 변경 없음. C1·C2를 4 sizes(320·375·768·1280, 높이 800) x 3 states(빈 칸·199자·200자), light, `--inject src/style.css`로 렌더 측정.
Check / target / result: C1 상자 간격 12/12=4px, 오른쪽 차 12/12=0; C2 12/12; AC-002 문구 3/3. 결과 줄과 spot check는 REPORT.md.
Spot check: C1 간격 differs(320x800 200자 check 4 / observed 9) → C1 미통과; C1 오른쪽·C2 agrees.
Limits: 링크된 CSS는 도구가 차단(ISSUES.md#iss-001); 다크 모드·높이 800 외 미측정.
Report stamp: report-check: ok 3,239 chars 83d1f297 (REPORT.md)
Completion boundaries: C1 규칙 뜻 사용자 결정 대기; user acceptance pending.
