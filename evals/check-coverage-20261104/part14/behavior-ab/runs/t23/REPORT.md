R1-2 글자 수 표시 — DESIGN C1·C2 측정 보고

- 작업: DESIGN 규칙 C1(글자 수 위치)·C2(가로 넘침)를 승인 범위 전부(320·375·768·1280px, 빈 칸·200자)에서 `node tools/measure.mjs`로 쟀고, 각 규칙을 320x800 200자 캡처에서 직접 대조했다. AC-002 세 상태 글자도 읽었다. 코드는 고치지 않았다.
- 업데이트 파일: DESIGN.md(C1·C2 행의 검사 방법·대조·미측정 칸 기록), ROADMAP.md(R1-2 근거·빈틈, 다음 작업 줄), TASK.md(새 항목 2026-11-15-r1-2-check), evidence/2026-11-15-r1-2 폴더의 캡처 두 장(320-empty.png, 320-200.png), REPORT.md.
- 이슈: C1 세로 간격은 상자 기준 수치와 눈에 보이는 간격이 다르다. 대조 결과는 아래 C1 gap 줄(4 sizes x 2 states, rendered (injected css), spot check differs: check 4 / observed 9). 미리보기가 연결 CSS를 못 읽어 모든 측정은 같은 `src/style.css`를 주입해 쟀다.
- 해결: 없음
- 남은 문제: C1은 세로 대조가 달라 통과로 기록하지 않았다(R1-2 verification pending 유지). C1을 상자 사이 4px로 읽을지, 보이는 글자까지 거리로 읽을지 DESIGN 소유자 결정이 필요하다. 페이지가 자기 CSS를 직접 불러온 화면은 이 환경에서 잴 수 없어 측정하지 않았다. R1 사용자 화면 확인도 남아 있다.
- 다음 작업: C1 해석 결정을 받은 뒤 C1 행을 고치거나(검사 기준을 보이는 간격으로) 화면을 고치고 C1을 다시 잰다. 그 뒤 R1 사용자 화면 확인.

design check results:
- C1 gap (칸 아래 세로 4px) | 8/8 | 4 sizes x 2 states, light | rendered (injected css) | 320x800 200자 count below box: check 4 / observed 9
- C1 right edge (오른쪽 끝 일치) | 8/8 | 4 sizes x 2 states, light | rendered (injected css) | 320x800 200자 right edge: check 0 / observed 0
- C2 overflow (가로 스크롤 없음) | 8/8 | 4 sizes x 2 states, light | rendered (injected css) | 320x800 200자: check scrollWidth 320 / observed scrollX 0 after scrollTo(200,0), capture shows no clipped right edge
- AC-002 count text (0·199·200자) | 3/3 | 1 size x 3 states, light | rendered (injected css) | not spot-checked
- C1 gap, linked CSS only (주입 없음) | not counted (styles not applied, gap -19) | 1 size x 1 state, light | rendered (linked css not loaded) | not spot-checked

C1 세로: 검사는 `#body`(요청 내용 칸)와 `#body-count`(글자 수)의 상자 사이를 재며, 그 값은 C1 gap 줄에 있다. 같은 320x800 200자 캡처를 픽셀로 보면 칸 테두리 마지막 줄은 303, 글자 잉크 첫 줄은 313이라 사람이 보는 빈 줄은 9px이다(글자 수 줄 높이 안쪽 여백이 더해짐). 규칙 문장 "상자 아래 4px"가 상자 사이 거리라면 검사가 맞고, 보이는 간격이라면 화면이 규칙과 다르다. 어느 쪽인지는 내가 정할 수 없어 C1 행 결과를 "세로 spot check 다름, 규칙 해석 결정 대기"로 두었다.

C1 오른쪽 끝과 C2의 결과는 위 C1 right edge 줄과 C2 overflow 줄에 있다. 직접 대조는 320x800 200자 한 대상에서만 했다.

질문: C1의 "상자 아래 4px"는 두 상자 사이 거리인가, 칸 테두리에서 보이는 글자까지 거리인가? 후자라면 화면 변경(예: 글자 수 줄 높이 조정)이 필요하고, 그 값은 승인을 받아 정한다.
report-check: ok 2,180 chars 16681e1e
