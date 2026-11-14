R1-2 글자 수 표시 — 구현과 C1·C2 측정

- 작업: 요청 내용 칸 아래 오른쪽에 `현재 / 200` 글자 수를 넣고 입력할 때마다 갱신하게 했고(DEC-002), DESIGN 규칙 C1·C2를 4 크기 x 3 상태로 쟀다.
- 업데이트 파일: src/index.html, src/style.css, src/char-count.js(새), DESIGN.md, ROADMAP.md, TASK.md, REPORT.md.
- 이슈: C1의 세로 간격은 상자 기준으로 재면 4px이지만, 화면에서 칸 테두리부터 글자까지 보이는 간격은 9px이라 두 읽기가 다르다(아래 C1 줄). 규칙의 "상자 아래 4px"가 어느 쪽인지 정해지지 않았다.
- 해결: 없음.
- 남은 문제: C1은 spot check가 달라 통과로 적지 않았고 R1-2는 verification pending이다. 글자 수의 글꼴 14px·색 `--muted`는 내가 고른 제안이라 승인 대기다. 실제 키 입력·한글 IME 입력은 관찰하지 않았다.
- 다음 작업: 소유자가 C1 세로 간격 기준을 정하면 그에 맞춰 C1을 다시 재고(필요하면 CSS 조정), 글꼴·색 제안 승인 뒤 R1-2 완료 처리, R1 끝 사용자 화면 확인.

design check results:
- C1 오른쪽 끝 맞춤 | 12/12 | 4 sizes x 3 states, light | rendered | 320x800 200자 캡처: check 0 / observed 0 (글자 잉크 x=303, 칸 테두리 x=303)
- C1 세로 간격 4px | 12/12 | 4 sizes x 3 states, light | rendered | 320x800 200자 캡처: check 4 / observed 9 (테두리 아래 줄 y=303, 글자 잉크 첫 줄 y=313), spot check differs
- C2 가로 넘침 | 12/12 | 4 sizes x 3 states, light | rendered | 320x800 200자 캡처: check scrollWidth 320 / observed 가장 오른쪽 잉크 x=303
- AC-002 글자 수 문자열 | 12/12 | 4 sizes x 3 states, light | rendered | not spot-checked
- 기존 요소 위치 비교 | 보내기 버튼만 22px 아래, 나머지 같음 | 2 sizes x 1 state, light | rendered | not spot-checked

## Display before/after

- before: 보내기 버튼 | "보내기" | 요청 화면 폼 맨 아래
- after: 보내기 버튼 | "보내기" | 요청 화면 폼 맨 아래
- before: 요청 내용 이름표 | "요청 내용" | 요청 화면, 칸 위
- after: 요청 내용 이름표 | "요청 내용" | 요청 화면, 칸 위

두 쌍 모두 보이는 내용과 경로가 같아 디자인 결정으로 적었다. 보내기 버튼은 글자 수 줄(18px)과 간격(4px)만큼 22px 아래에 그려진다(320px에서 y=320 → 342).

측정은 `node tools/measure.mjs`로 320·375·768·1280px, 빈 칸·199자·200자에서 했고 페이지가 자기 `style.css`를 불러왔다(linkedCss loaded=true). 상태는 스크립트로 값을 넣고 input 이벤트를 보내 만들었다. C2는 12개 모두 넘침이 없었다 (4 sizes x 3 states, rendered, spot check 320x800: check 320 / observed 303). C1은 상자 사이 간격이 12개 모두 4px였지만 (4 sizes x 3 states, rendered; spot check differs: check 4 / observed 9), 사람이 보는 간격은 글자 줄 높이 위쪽 여백 때문에 9px이다. 같은 폼의 이름표와 칸 사이 4px도 상자 기준이라 C1을 상자 기준으로 읽는 것이 기존 방식과 맞을 수 있으나, 그 판단은 규칙 소유자 몫이라 통과로 적지 않았다.

질문:
1. C1 "상자 아래 4px"는 글자 수 상자 위 끝까지(지금 4px)인가, 보이는 글자까지(지금 9px)인가? 보이는 글자 기준이면 줄 높이·여백을 조정해 다시 재겠다.
2. 글자 수 글꼴 14px·색 `--muted`(칸 이름표와 같은 값)를 승인하는가?
report-check: ok 2,159 chars b70068a8
