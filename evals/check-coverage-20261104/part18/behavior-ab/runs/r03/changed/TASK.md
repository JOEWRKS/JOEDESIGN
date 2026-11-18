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

## 2026-11-15-r1-3 / 2026-11-15 / 확인 화면 메모 구현

Roadmap item: ROADMAP.md#stage-r1-요청-폼--in-progress R1-3.
Result: 확인 화면(src/confirm.html)에 추가 메모 칸과 그 아래 오른쪽 `현재 / 200` 표시, 입력마다 갱신.
Changed files: src/confirm.html (새 화면, 같은 style.css 연결).
Check / target / result: 코드 읽기만. C1·C2 측정 안 함.
Evidence: 없음.
Limits: 렌더 측정 없음.
Report stamp: none ran.
Required specialist verdict: not applicable.
Completion boundaries: implementation done; visual check pending; user acceptance pending.
Related issue / knowledge: none.
Record handoff gap: none.

## 2026-11-18-c1-c2 / 2026-11-18 / 요청·확인 화면 C1·C2 측정

Roadmap item: ROADMAP.md#stage-r1-요청-폼--in-progress R1-2, R1-3.
Result: 코드 변경 없음. DESIGN.md#rule-coverage C1·C2 행 Check·Spot check·Unmeasured·Result 채움.
Check / target / result: tools/measure.mjs, 2화면 x 4크기(320·375·768·1280, 높이 800) x 2상태(빈 칸, 200자), 라이트. C1 16/16, C2 16/16 (상자 기준, 렌더). 확인 화면은 링크 CSS 차단으로 style.css 주입(ISSUES.md#iss-001). AC-002 0·199·200, AC-003 0·200 글자 확인.
Spot check: C1 세로 check 4 / observed 9(보이는 간격), 오른쪽 0 / 0; C2 320 캡처 오른쪽 끝 내용 열 303, scrollX 0.
Evidence: .work/ 캡처와 스크립트(커밋 안 함). 보고 REPORT.md.
Limits: 확인 화면 자기 CSS 렌더, 실제 키 입력, 다른 높이 미측정.
Report stamp: report-check: ok 2,492 chars 4d2e5131
Completion boundaries: C1 세로 4px 의미(상자 간격/보이는 간격) 소유자 판단 대기; user acceptance pending.
