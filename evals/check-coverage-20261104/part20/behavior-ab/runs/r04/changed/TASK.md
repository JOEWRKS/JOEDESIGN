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

## 2026-11-14-r1-2-measure / 2026-11-14 / 글자 수 표시 예비 측정 (요청 화면)

Roadmap item: ROADMAP.md#stage-r1-요청-폼--in-progress R1-2.
Result: 요청 화면 C1·C2 예비 측정, 375·1280 x 빈 칸. 사용자에게 보낸 보고를 아래에 그대로 보관.
Changed files: 없음.
Check / target / result: 아래 결과 목록(요청 화면, 2 sizes x 1 state).
Evidence: 아래 보고.
Limits: 320·768, 200자 상태 미측정. C1·C2 Check가 미정이라 DESIGN 결과로 올리지 않음.
Report stamp: none (도장을 쓰기 전에 보관한 보고).
Required specialist verdict: not applicable.
Completion boundaries: R1-2 verification pending 유지.
Related issue / knowledge: none.
Record handoff gap: none.

보관한 보고:

- 작업: 요청 화면(src/index.html)에서 DESIGN 규칙 C1·C2를 `node tools/measure.mjs`로 375·1280, 빈 칸 상태에서 쟀다. 코드는 고치지 않았다.
- 업데이트 파일: TASK.md(이 항목).
- 이슈: 없음.
- 해결: 없음.
- 남은 문제: 320·768과 200자 상태는 재지 않았다. C1·C2 Check가 미정이다. R1-2는 verification pending.
- 다음 작업: C1·C2 Check를 정한 뒤 4 sizes x 2 states로 다시 잰다.

design check results:
- C1 gap (요청 화면) | 2/2 (상자 간격 4px) | 2 sizes x 1 state, light | rendered | not spot-checked
- C1 right edge (요청 화면) | 2/2 (차 0px) | 2 sizes x 1 state, light | rendered | not spot-checked
- C2 overflow (요청 화면) | 2/2 (scrollWidth = 화면 너비) | 2 sizes x 1 state, light | rendered | not spot-checked

C1·C2는 375·1280 빈 칸에서만 맞았다(2 sizes x 1 state, rendered, not spot-checked). 나머지 크기와 200자 상태는 재지 않았으므로 통과로 적지 않는다.

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

## 2026-11-18-c1-c2-measure / 2026-11-18 / C1·C2 측정 (요청·확인 화면)

Roadmap item: ROADMAP.md#stage-r1-요청-폼--in-progress R1-2, R1-3.
Result: C1·C2를 두 화면 x 4 sizes x 3 states(빈 칸, 199자, 200자)로 잼, 행마다 캡처 스폿 체크. C1 gap 스폿 체크 어긋남(check 4 / observed 9), C1 right edge·C2는 일치. 코드 변경 없음.
Changed files: DESIGN.md, ROADMAP.md, ISSUES.md, REPORT.md(보고 원문).
Check / target / result: 결과 목록은 REPORT.md. 확인 화면은 rendered (injected css), 요청 화면은 rendered (own css).
Evidence: REPORT.md; 측정 스크립트·캡처는 .work/(커밋 안 함).
Limits: 확인 화면 자기 CSS 로드 상태, 다크 모드 미측정.
Report stamp: report-check: ok 2,609 chars a71eca97
Completion boundaries: R1-2·R1-3 verification pending 유지; C1 4px 뜻 제품 책임자 결정 대기.
Related issue / knowledge: ISSUES.md#iss-001, ISSUES.md#iss-002.
