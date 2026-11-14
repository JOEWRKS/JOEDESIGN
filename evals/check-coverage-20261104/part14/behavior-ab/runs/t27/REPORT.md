- 작업: R1-2 글자 수 표시의 DESIGN 규칙 C1·C2를 `tools/measure.mjs`로 쟀다. 미리보기가 연결 CSS(`style.css`)를 읽지 못해(출력 `linkedCss loaded: false` 확인) 같은 파일을 `--inject src/style.css`로 주입해 쟀다. 화면 코드는 고치지 않았다.
- 업데이트 파일: DESIGN.md (C1·C2 행 갱신, 주입 측정 메모), ROADMAP.md (R1-2 근거 칸, 다음 작업 줄), TASK.md (새 항목 2026-11-15-r1-2-check), 대조용 캡처 파일 320-200.png (폴더 evidence/2026-11-15-r1-2).
- 이슈: C1 간격은 상자 기준으로는 4px이지만, 캡처에서 칸 테두리 아래 끝부터 글자 윗 끝까지 보이는 간격은 9px이다(글자 줄 높이의 위쪽 여백). 규칙 "상자 아래 4px"가 어느 쪽을 뜻하는지 정해지지 않아 C1은 통과로 기록하지 않았다.
- 해결: 없음
- 남은 문제: C1 간격의 판정 기준을 제품·디자인 소유자가 정해야 한다. 상자 사이로 보면 현재 구현을 그대로 둘 수 있고, 보이는 글자까지로 보면 `.char-count` 간격을 고쳐야 한다(결과는 아래 C1 gap 줄). R1-2는 verification pending 유지. 199자 상태는 C1·C2 측정 범위 밖이다(표시 글자는 아래 AC-002 줄). 모든 측정은 CSS 주입 화면이며, 페이지가 자기 CSS를 스스로 로드한 화면은 이 환경에서 잴 수 없다. 사용자 화면 확인은 별도.
- 다음 작업: 소유자에게 질문 — C1의 4px를 "글자 수 표시 상자 위 끝"까지로 볼지 "보이는 글자 위 끝"까지로 볼지. 답에 따라 C1 행의 Check를 고치거나 `.char-count` 간격을 고친 뒤 C1·C2 재측정.

design check results:
- C1 gap (box) | 8/8 at 4px | 4 sizes x 2 states, light | rendered (injected css) | 320x800 200자 capture: check 4 / observed 9 (differs)
- C1 right edge | 8/8 at 0px | 4 sizes x 2 states, light | rendered (injected css) | 320x800 200자 capture: check 0 / observed 0
- C2 overflow | 8/8 | 4 sizes x 2 states, light | rendered (injected css) | 320x800 200자: scrollWidth 320 / capture content right edge 303px, scrollTo(50,0) gives scrollX 0
- AC-002 text | 3/3 | 1 size x 3 states, light | rendered (injected css) | not spot-checked

크기는 320·375·768·1280px, 상태는 빈 칸과 200자다. C2는 문서 가로 스크롤이 없다(4 sizes x 2 states, rendered (injected css), spot check match at 320x800 200자). C1의 오른쪽 끝 맞춤은 맞다(4 sizes x 2 states, rendered (injected css), spot check match: check 0 / observed 0). C1 간격은 상자 기준 값과 보이는 간격이 다르므로(4 sizes x 2 states, rendered (injected css), spot check differs: check 4 / observed 9) 이 행은 통과로 세지 않았다.
report-check: ok 1,841 chars 3c567d6d
