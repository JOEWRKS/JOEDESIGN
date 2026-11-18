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
Result: DESIGN.md#rule-coverage C1·C2 행을 정의하고 두 화면 × 320·375·768·1280 × 빈 칸·200자, 라이트로 측정. 소스 변경 없음.
Check / target / result: C1 세로 상자 간격 8/8씩, 오른쪽 끝 8/8씩, C2 8/8씩(4 sizes x 2 states, 요청 화면 rendered (own css), 확인 화면 rendered (injected css)); C1 세로 spot check differs (320 빈 칸: check 4 / observed 9), 가로·C2 spot check 일치. 줄별 결과는 REPORT.md.
Evidence: .work/run.mjs, .work/ink.mjs, .work/*.png (로컬 임시).
Limits: 확인 화면은 도구가 링크 CSS를 막아 주입 CSS로만 측정(ISSUES.md); AC-002 199자 미측정; C1 세로 기준은 소유자 결정 대기.
Report stamp: report-check: ok 3,088 chars d0781c76
Completion boundaries: R1-2·R1-3 verification pending 유지; user acceptance pending.
