- 작업: R1-2 글자 수 표시 구현. 요청 내용 칸 아래 오른쪽에 `현재 / 200`을 보여 주고 입력할 때마다 갱신(DEC-002). DESIGN 규칙 C1·C2를 4개 크기 x 3개 상태에서 렌더 측정하고 각 행을 직접 관찰과 대조함.
- 업데이트 파일: src/index.html(요청 내용 칸을 `div.field` + `label for`로 바꾸고 글자 수 `span#body-count`, `aria-describedby`, 갱신 스크립트 추가), src/style.css(`.counter` 한 줄: 오른쪽 정렬, 13px, `--muted` 색, 새 간격 값 없음), DESIGN.md(Rule coverage C1·C2 행의 Check·Spot check·States·Unmeasured·Result), ROADMAP.md(R1-2 complete, 다음 작업 줄), TASK.md(2026-11-15-r1-2 항목), evidence/r1-2/(캡처 3장).
- 이슈: 없음.
- 해결: 없음(고친 결함 없음, 새 구현).
- 남은 문제: 측정하지 않은 것은 칸 세로 크기를 늘린 뒤, 실제 키보드 입력(값 설정 + input 이벤트로 상태를 만듦), 다크 모드(승인 범위 밖). C1은 상자 기준 규칙이라 사람이 보는 글자 잉크와 칸 테두리 사이는 9px(320x800 캡처, 잉크 위 행 313)로 4px보다 넓어 보임. 이 차이를 규칙으로 고칠지는 디자인 승인자 판단. 사용자 화면 확인(R1 끝)은 아직 안 함.
- 다음 작업: R1 끝 사용자 화면 확인. 확인할 질문: 글자 수 글자 크기·색(13px, `--muted`)을 그대로 둘지, C1을 글자 잉크 기준으로 바꿀지.

결과 목록:

- C1 글자 수 위치 | 12/12 (간격 4px, 오른쪽 차이 0) | 4 sizes x 3 states (320·375·768·1280 x 빈 칸·199자·200자), light | rendered | 320x800 200자: check 4px·오른쪽 차이 0 / observed 캡처 픽셀 칸 아래 테두리 행 303, 글자 수 상자 위 행 308(빈 행 4), 오른쪽 열 303·303
- C2 넘침 없음 | 12/12 (scrollWidth = 화면 너비) | 4 sizes x 3 states (320·375·768·1280 x 빈 칸·199자·200자), light | rendered | 320x800 200자: check scrollWidth 320 ≤ 320 / observed scrollTo(200,0) 뒤 scrollX 0, 캡처 오른쪽 여백 x 304–319에 칠해진 픽셀 없음
- AC-002 표시 글자 | 12/12 (`0 / 200`, `199 / 200`, `200 / 200`) | 4 sizes x 3 states, light | rendered | 320x800 200자: check `200 / 200` / observed 캡처에 `200 / 200`

R1-2는 ROADMAP Check인 C1·C2 행과 AC-002 세 상태를 현재 입력에서 돌려 complete로 기록함(C1 12/12, 4 sizes x 3 states, rendered, spot check 일치; C2 12/12, 4 sizes x 3 states, rendered, spot check 일치). 사용자 화면 확인은 별도로 남음.

report-check: ok 1,661 chars 43b1181d
