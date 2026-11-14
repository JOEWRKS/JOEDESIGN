- 작업: R1-2 글자 수 표시 구현. 요청 내용 칸 아래 오른쪽에 `현재 / 200`을 보여 주고 입력할 때마다 갱신(PRODUCT.md DEC-002). 그다음 DESIGN 규칙 C1·C2를 4개 너비(320·375·768·1280) x 3개 상태(빈 칸·199자·200자)에서 `node tools/measure.mjs`로 렌더링 측정. AC-002 표시도 확인: 빈 칸 `0 / 200`, 199자 `199 / 200`, 200자 `200 / 200`, 4개 너비 모두 일치(4 sizes x 3 states, rendered, not spot-checked).
- 업데이트 파일: src/index.html(요청 내용 칸을 `div.field` + `label for="body"`로 바꾸고 `#body-count`와 갱신 스크립트 추가, 화면 문구·순서는 그대로), src/style.css(`.counter` 한 줄), DESIGN.md(C1·C2 행의 Check·Spot check·Result, 제안 값, 판단 대기 항목), ROADMAP.md(R1-2 verification pending, 다음 작업 줄), TASK.md(2026-11-15-r1-2 항목).
- 이슈: C1 세로 간격의 spot check가 측정값과 다름. 상자 사이 간격은 4px지만, 칸 테두리에서 보이는 글자까지는 9px(320 200자 캡처, 줄 높이 안의 여백 때문).
- 해결: 없음
- 남은 문제: (1) C1 "4px"가 상자 사이 간격(`--space-1`)인지 보이는 글자까지 간격(지금 9px)인지 소유자 판단 필요. 판단 전까지 C1은 미결이고 R1-2는 verification pending. 보이는 글자까지 4px로 맞추려면 `--space-*`에 없는 값이나 음수 여백이 필요해 간격 토큰 규칙과 부딪힘. (2) 글꼴 14px·색 `--muted`는 내가 고른 값(요청 내용 이름표와 같은 값)이고 아직 승인되지 않음. (3) 측정 안 한 범위: 다크 모드(승인 범위 밖), 다른 창 높이, 다른 글꼴·확대, 공백 없는 긴 문자열, 사용자가 칸 크기를 바꾼 상태. (4) R1 끝 사용자 화면 확인.
- 다음 작업: C1 기준 판단을 받으면 C1 행을 고치거나 확정하고 다시 측정. 그 뒤 사용자 화면 확인.

결과 목록:

- C1 세로(글자 수 상자 top − 칸 bottom = 4) | 12/12 | 4 sizes x 3 states, light | rendered | 320 200자: check 4 / observed 9 (테두리 아래 첫 글자 잉크까지, capture) — differs
- C1 오른쪽 끝(칸 right − 글자 수 right = 0) | 12/12 | 4 sizes x 3 states, light | rendered | 320 200자: check 0 / observed 0 (글자 잉크 끝 x=303 = 칸 테두리 x=303, capture)
- C2 가로 넘침(scrollWidth ≤ innerWidth) | 12/12 | 4 sizes x 3 states, light | rendered | 320 200자: check 320 ≤ 320 / observed 가장 오른쪽 잉크 x=303 of 320 (capture)
- AC-002 표시 문구 | 12/12 | 4 sizes x 3 states, light | rendered | not spot-checked

질문(소유자): C1의 "상자 아래 4px"는 두 상자 사이 간격인가, 눈에 보이는 글자까지의 간격인가? 앞의 뜻이면 C1 Check 칸 기준을 상자 간격으로 확정하고, 뒤의 뜻이면 간격 토큰 규칙의 예외 승인이 필요합니다.

측정 환경: 헤드리스 Chrome, `--height 800`, 연결된 style.css 적용됨(`linkedCss loaded: true`). 200자 상태는 '가' 200자를 넣고 `input` 이벤트를 보내 만들었고, 실제 키보드 입력은 하지 않음. 커밋 안 함.

report-check: ok 1,968 chars b88d065a
