R1-2 글자 수 표시를 구현하고 C1·C2를 4개 크기 x 3개 상태(빈 칸, 199자, 200자)에서 렌더 측정했습니다. C2는 12/12 (4 sizes x 3 states, rendered, spot check 320x420 200자: check 320 ≤ 320 / observed 내용 열 16–303)입니다. C1은 상자 기준 12/12 (4 sizes x 3 states, rendered, spot check differs: check 4 / observed 9)라 통과로 기록하지 않았습니다. 규칙의 4px가 상자 사이 간격인지 보이는 글자까지의 간격인지 확인이 필요합니다.

- 작업: 요청 내용 칸 아래 오른쪽에 `현재 / 200` 글자 수를 넣고 입력할 때마다 갱신(DEC-002, AC-002). 칸과의 간격은 기존 `.field` gap(`--space-1`, 4px), 글자는 칸 이름과 같은 14px·`--muted`. 검사 스크립트 `checks/char-count.mjs` 추가. 보내기 버튼은 글자 수 줄 높이만큼(22px) 아래에 놓임.
- 업데이트 파일: src/index.html, src/style.css, checks/char-count.mjs, DESIGN.md(C1·C2 행, Token roles, Open decision), ROADMAP.md(R1-2), TASK.md(2026-11-15-r1-2), REPORT.md.
- 이슈: C1 대조 결과가 다름. 측정은 상자 기준 4px, 320x420·1280x420 캡처에서 칸 테두리 마지막 행(y303)부터 글자 잉크 첫 행(y313)까지 보이는 간격은 9px(줄 높이 여백 포함).
- 해결: 없음
- 남은 문제: C1 아래 간격의 기준(상자 4 / 잉크 9) owner 확인 대기, 그래서 R1-2는 verification pending. 글자 크기·색(14px, `--muted`)은 칸 이름에서 가져온 값이며 승인된 값 아님. 실제 키보드 입력은 재지 않음(input 이벤트로 대신), 375·768의 잉크 간격은 캡처 대조 안 함, 다크 모드는 범위 밖. 화면 낭독기에 글자 수 변경을 알리지 않음(aria-describedby만). R1 끝 사용자 화면 확인 별도.
- 다음 작업: 질문 — C1의 "칸 상자 아래 4px"는 (a) 두 상자 사이 4px(현재 상태, 충족)인가, (b) 칸 테두리에서 보이는 글자까지 4px인가? (b)이면 글자 수 줄 높이를 줄이는 수정 후 C1·C2 재측정. 답을 받으면 C1 행과 R1-2 상태 갱신.

결과 목록:
- C1 아래 간격(상자) | 12/12 | 4 sizes x 3 states, light | rendered | 320x420 200자: check 4 / observed 9 (테두리 y303 → 잉크 y313), 다름
- C1 오른쪽 끝 | 12/12 | 4 sizes x 3 states, light | rendered | 320x420 200자: check 0 / observed 0 (잉크 오른쪽 열 303 = 테두리 오른쪽 열 303)
- C2 문서 가로 넘침 | 12/12 | 4 sizes x 3 states, light | rendered | 320x420 200자: check scrollWidth 320 ≤ 320 / observed 내용 열 16–303
- AC-002 글자 | 12/12 | 4 sizes x 3 states, light | rendered | 320x420 200자: check `200 / 200` / observed 캡처 `200 / 200`
- 기존 요소 상자 전후 | 제목·칸 이름·칸 상자 같음, 보내기 버튼 y 320 → 342 | 320 x 빈 칸, light | rendered | not spot-checked
- linkedCss | 12/12 loaded | 4 sizes x 3 states, light | rendered | not spot-checked

report-check: ok 1,953 chars c0723405
