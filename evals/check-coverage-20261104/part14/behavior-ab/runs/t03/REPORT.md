- 작업: R1-2 글자 수 표시 구현(요청 내용 칸 아래 오른쪽 `현재 / 200`, 입력마다 갱신)과 DESIGN 규칙 C1·C2 측정. C1 간격은 상자 기준 4px이나 화면에서 보이는 간격은 7px이라 R1-2는 verification pending.
- 업데이트 파일: src/index.html, src/style.css, DESIGN.md(Token roles, Rule coverage C1·C2 행), ROADMAP.md(R1-2 verification pending, 다음 작업 줄), ISSUES.md(I-001), TASK.md(2026-11-15-r1-2)
- 이슈: I-001 — C1 "칸 상자 아래 4px"를 상자로 재면 4, 320x800 200자 캡처에서 칸 테두리와 글자 잉크 사이 보이는 간격은 7px(C1 간격 8/8 (4 sizes x 2 states, rendered; spot check differs: check 4 / observed 7))
- 해결: 없음
- 남은 문제: I-001 C1 기준 결정 대기(상자 간격인지 보이는 간격인지; 보이는 간격이면 `--space-*` 토큰만으로는 4px를 맞출 수 없음). 다크 모드·확대·세로 크기 조절·실제 키보드 입력의 200자 차단은 미측정. R1 사용자 화면 확인 대기.
- 다음 작업: C1 기준을 정해 주시면 그 기준으로 C1 행 재측정, 일치하면 R1-2 complete, 이후 R1 사용자 화면 확인.

design check results:
- C1 gap (글자 수 top − 칸 bottom = 4) | 8/8 | 4 sizes x 2 states, light | rendered | 320x800 200자 capture: check 4 / observed 7 (테두리 마지막 행 y=303, 잉크 첫 행 y=311), differs
- C1 right edge (글자 수 right = 칸 right) | 8/8 | 4 sizes x 2 states, light | rendered | 320x800 200자 capture: check 0 / observed 0 (둘 다 x=303)
- C2 overflow (scrollWidth ≤ 화면 너비) | 8/8 | 4 sizes x 2 states, light | rendered | 320x800 200자 capture: check scrollWidth 320 / observed 가장 오른쪽 칠해진 열 x=303
- AC-002 text (0·199·200자 → `0 / 200`·`199 / 200`·`200 / 200`) | 12/12 | 4 sizes x 3 states, light | rendered | 320x800 200자 capture: check "200 / 200" / observed "200 / 200"

측정은 `node tools/measure.mjs`로 320·375·768·1280 너비(높이 800)에서 했고, 매 실행에서 linkedCss `style.css`가 loaded=true였습니다(페이지 자체 CSS). 상태는 스크립트로 값을 넣고 `input` 이벤트를 보낸 것이며, 199자 상태는 C1·C2 행 범위 밖이라 C1·C2 결과 수에는 넣지 않았습니다.

C1 간격: 측정 상자끼리는 4px(C1 간격 8/8 (4 sizes x 2 states, rendered; spot check differs: check 4 / observed 7))이지만, 글자 줄 상자 위쪽에 글꼴 여백 3px가 있어 사람이 보는 간격은 7px입니다. 규칙이 어느 쪽을 뜻하는지 정해 주세요. 상자 기준이면 지금 그대로 통과로 기록하고, 보이는 간격 기준이면 음수 여백 같은 토큰 밖 값이 필요해 규칙(토큰만 사용)과 충돌하므로 그 예외 승인도 필요합니다.

구현 메모: 요청 내용 칸 묶음을 `<label>` 감싸기에서 `<div>` + `<label for>`로 바꿨습니다(보이는 배치는 같음, 글자 수가 칸 이름에 섞이지 않게). 글자 수는 `aria-describedby`로 칸에 연결했고 글자 크기 14px, 색 `--muted`, 줄 높이 1입니다. 글자 수는 `maxlength`와 같은 기준(value.length)이라 이모지는 2자로 셉니다.

report-check: ok 2,094 chars 92b10110
