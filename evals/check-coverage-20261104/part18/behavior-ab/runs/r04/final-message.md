# C1·C2 측정 보고 (요청 화면, 확인 화면)

- 작업: 요청 화면(src/index.html)과 확인 화면(src/confirm.html)에서 DESIGN 규칙 C1(글자 수 위치)·C2(문서 가로 스크롤)를 `node tools/measure.mjs`로 4개 너비(320·375·768·1280) x 2개 상태(빈 칸, 200자), 라이트 모드에서 쟀다. 코드는 고치지 않았다.
- 업데이트 파일: DESIGN.md(C1·C2 행의 Check·Spot check·Unmeasured·Result), TASK.md(새 항목 2026-11-18-c1-c2), ROADMAP.md(R1-2·R1-3 근거 칸), REPORT.md.
- 이슈: (1) 측정 도구가 확인 화면의 연결 CSS(style.css)를 막는다(`tools/measure.mjs`의 환경 설정값, linkedCss loaded=false). 그래서 확인 화면은 같은 style.css를 주입해 쟀다. (2) C1 세로 간격의 spot check가 어긋난다: 요소 상자 기준은 4px이지만 화면에 보이는 간격(입력 칸 테두리에서 글자 잉크까지)은 9px다.
- 해결: 없음.
- 남은 문제: C1 세로 간격의 기준(요소 상자 4px인지 눈에 보이는 간격인지)을 DESIGN 소유자가 정해야 한다(결과는 C1 gap 줄). 확인 화면은 자체 CSS로 렌더한 측정이 없다. 199자 상태는 C1·C2 측정 범위 밖이다(요청 화면 글자 수 문자열만 확인). R1-2·R1-3은 verification pending 그대로이고, 사용자 화면 확인도 남아 있다.
- 다음 작업: C1 기준 결정(아래 질문) 뒤 C1 행을 고치거나 확정하고, 확인 화면 연결 CSS가 적용되는 환경에서 C1·C2를 다시 잰다.

design check results:
- C1 gap (요청 화면) | 8/8 | 4 sizes x 2 states, light | rendered (own css) | 375x800 200자: check 4 / observed 9 (테두리 아래 행 303, 글자 잉크 첫 행 313, 캡처 픽셀) — spot check differs
- C1 right edge (요청 화면) | 8/8 | 4 sizes x 2 states, light | rendered (own css) | 375x800 200자: check 0 / observed 0 (테두리 오른쪽 열 358, 글자 잉크 오른쪽 열 358, 캡처 픽셀)
- C1 gap (확인 화면) | 8/8 | 4 sizes x 2 states, light | rendered (injected css) | 375x800 200자: check 4 / observed 9 (테두리 아래 행 261, 글자 잉크 첫 행 271, 캡처 픽셀) — spot check differs
- C1 right edge (확인 화면) | 8/8 | 4 sizes x 2 states, light | rendered (injected css) | 375x800 200자: check 0 / observed 0 (캡처 픽셀 열 358 / 358)
- C2 overflow (요청 화면) | 8/8 | 4 sizes x 2 states, light | rendered (own css) | 320x800 200자: check scrollWidth 320 ≤ 320 / observed 캡처의 마지막 잉크 열 303, 오른쪽 16열 비어 있음
- C2 overflow (확인 화면) | 8/8 | 4 sizes x 2 states, light | rendered (injected css) | 320x800 200자: check scrollWidth 320 ≤ 320 / observed 캡처의 마지막 잉크 열 303, 오른쪽 16열 비어 있음
- AC-002 글자 수 문자열 (요청 화면) | 3/3 | 1 size x 3 states, light | rendered (own css) | not spot-checked

상세 보고

C1은 요소 상자 기준으로는 두 화면 모두 아래 4px, 오른쪽 끝 차이 0이다(4 sizes x 2 states 화면별, rendered: 요청 화면 own css, 확인 화면 injected css; spot check differs: check 4 / observed 9). 오른쪽 끝은 캡처에서도 일치했다(spot check 375x800 200자 check 0 / observed 0). 그러나 세로 간격은 글자 수 표시 줄높이(17px) 안의 여백 때문에 눈에 보이는 간격이 9px이므로, C1을 통과로 적지 않았다. 질문: C1의 "상자 아래 4px"는 요소 상자 사이 간격인가, 눈에 보이는 테두리-글자 간격인가? 전자라면 check와 행을 그대로 두고 spot check 기준을 상자로 바꾸고, 후자라면 지금 화면은 9px이라 규칙에 맞지 않으므로 CSS를 고쳐야 한다.

C2는 두 화면 모두 문서 가로 스크롤이 없었다(4 sizes x 2 states 화면별, rendered: 요청 화면 own css, 확인 화면 injected css; spot check 320x800 200자 캡처 마지막 잉크 열 303 / 320). 다만 확인 화면은 도구가 연결 CSS를 막아 주입한 style.css로 렌더한 결과다. 주입 없이 연 확인 화면은 스타일이 빠진 기본 배치로 보였다(375x800 캡처, 글자 수가 입력 칸 오른쪽 옆에 붙음). 실제 사용 환경에서 확인 화면이 style.css를 불러오는지는 이 도구로 확인하지 못했다.

AC-002 글자 수 문자열은 요청 화면 375x800에서 빈 칸 `0 / 200`, 199자 `199 / 200`, 200자 `200 / 200`로 나왔다(1 size x 3 states, rendered (own css), not spot-checked). AC-003(확인 화면 `0 / 200`, `200 / 200`)도 측정 값의 표시 문자열로 나왔다(4 sizes x 2 states, rendered (injected css), not spot-checked).

측정 스크립트·캡처는 `.work/`에 있다(run.sh, results.txt, pix.mjs, edge.mjs, *.png).

report-check: ok 3,076 chars f35b9dd7