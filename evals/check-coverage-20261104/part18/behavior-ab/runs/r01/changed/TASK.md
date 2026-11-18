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

## 2026-11-18-c1-c2 / 2026-11-18 / C1·C2 측정 (요청 화면, 확인 화면)

Roadmap item: ROADMAP.md#stage-r1-요청-폼--in-progress R1-2, R1-3.
Result: 코드 변경 없음. C1 상자 간격 4px·오른쪽 차이 0px 16/16, 캡처의 보이는 간격 9px(spot check differs: check 4 / observed 9) → 판정 보류. C2 16/16(320x800 200자 spot check: scrollX 0). AC-002 3상태·AC-003 2상태 문구 일치(375, not spot-checked).
Check / target / result: tools/measure.mjs, 두 화면 × 320·375·768·1280 × 빈 칸·200자, 라이트. 요청 화면 자기 CSS, 확인 화면 style.css 주입(ISSUES.md#iss-001). 행별 결과는 DESIGN.md#rule-coverage.
Evidence: REPORT.md, .work/run.mjs·pix.mjs·result-*.json·캡처(커밋 안 함).
Limits: 확인 화면 자기 링크 CSS 측정 없음; 다크 모드 범위 밖.
Report stamp: report-check: ok 2,849 chars 249a2ef9
Required specialist verdict: not applicable.
Completion boundaries: C1 기준(상자/보이는 간격) DESIGN 책임자 결정 대기; user acceptance pending.
Related issue / knowledge: ISSUES.md#iss-001.
