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
Result: 코드 변경 없음. C1·C2·AC-002 렌더 측정, 결과 줄은 REPORT.md.
Changed files: DESIGN.md (C1·C2 행), ROADMAP.md (R1-2 근거, 다음 작업).
Check / target / result: DESIGN.md#rule-coverage C1·C2 행, 320·375·768·1280 × 빈 칸·199자·200자, 라이트, rendered (injected css). C2 12/12, C1 상자 12/12, AC-002 문구 12/12.
Evidence: 320x700 200자 캡처 픽셀(C1 간격 check 4 / observed 9, 오른쪽 끝 0 / 0, C2 scrollX 0).
Limits: 링크 CSS 차단으로 주입 렌더만; 다크 모드·칸 크기 조절 미측정.
Report stamp: report-check: ok 2,227 chars 973052a1
Required specialist verdict: not applicable.
Completion boundaries: C1 간격 기준 소유자 판단 대기(not passed); user acceptance pending.
Related issue / knowledge: none.
Record handoff gap: none.
