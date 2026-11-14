- 작업: R1-2 글자 수 표시 구현(요청 내용 칸 아래 오른쪽 `현재 / 200`, 입력마다 갱신)과 DESIGN 규칙 C1·C2 측정. R1-2는 verification pending.
- 업데이트 파일: src/index.html, src/style.css, DESIGN.md(규칙 표 두 행, 제안 값 줄), ROADMAP.md(R1-2, Next 줄), TASK.md(2026-11-15-r1-2), REPORT.md, evidence 폴더 `2026-11-15-r1-2` (320px 캡처 두 장)
- 이슈: C1 간격의 spot check가 측정과 다름(320x700 200자: check 4 / observed 9). 측정은 상자 사이 4px이고, 캡처에서 칸 테두리부터 글자 잉크까지는 9px.
- 해결: 없음
- 남은 문제: (1) C1 간격 기준 owner 확인 필요: 규칙의 4px가 상자 간격(지금 구현, 제목·요청 내용 이름표와 칸 사이와 같은 방식)인지, 눈에 보이는 글자까지의 간격인지. (2) 글자 수 세는 단위를 제가 정함: `maxlength`와 같은 UTF-16 단위라 이모지 하나가 2로 셈. 제품 정의에 없으니 owner 확인 전까지 pending. (3) 글자 14px·`--muted` 색은 제안값(미승인). (4) 실제 키 입력·한글 IME 조합 중 표시는 관찰 안 함(측정은 스크립트로 값을 넣고 input 이벤트 발생). (5) 사용자 화면 확인은 R1 끝에 별도.
- 다음 작업: 위 (1)(2) 답을 받으면 C1 행 기준을 고치거나 확정하고 C1·C2 재측정, 그 뒤 R1-2 완료 판단.

design check results:
- C1 gap | 12/12 | 4 sizes x 3 states, light | rendered | 320x700 200자: check 4 / observed 9, spot check differs
- C1 right edge | 12/12 | 4 sizes x 3 states, light | rendered | 320x700 200자: check 0 / observed 0
- C2 overflow | 12/12 | 4 sizes x 3 states, light | rendered | 320x700 200자: check scrollWidth 320 / observed no horizontal scrollbar, rightmost ink 303px, capture
- AC-002 counter text | 12/12 | 4 sizes x 3 states, light | rendered | 320x700 200자: check "200 / 200" / observed "200 / 200" in capture

크기는 320x700, 375x700, 768x700, 1280x800, 상태는 빈 칸·199자·200자(규칙 표의 빈 칸·200자에 AC-002의 199자를 더함)이며, 매 측정에서 페이지 자체 CSS가 적용됨(`linkedCss loaded: true`). C1 간격은 12곳 모두 상자 기준 4px(4 sizes x 3 states, rendered; spot check differs: check 4 / observed 9)이므로 규칙 통과로 적지 않고 owner 답을 기다린다. 오른쪽 끝 맞춤과 넘침 없음은 측정과 캡처가 일치함(4 sizes x 3 states, rendered; spot check 320x700 200자 일치). 다크 모드는 승인 범위 밖이라 재지 않음.

구현 메모: 요청 내용 칸의 이름표를 감싸는 `label`에서 `label for="body"`로 바꾸고 글자 수 문단을 같은 `.field` 묶음에 넣어 기존 `--space-1` 간격을 그대로 씀. 칸에는 `aria-describedby`로 글자 수를 연결함. 커밋하지 않음.

report-check: ok 1,888 chars d7d89b6a
