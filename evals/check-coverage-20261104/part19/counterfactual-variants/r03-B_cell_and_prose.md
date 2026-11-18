- 작업: 요청 화면(src/index.html)과 확인 화면(src/confirm.html)에서 DESIGN 규칙 C1(글자 수 위치)·C2(가로 넘침)를 tools/measure.mjs로 렌더 측정하고 320px 캡처로 spot check 함. 코드는 고치지 않음.
- 업데이트 파일: DESIGN.md(C1·C2 행의 Check·Spot check·Unmeasured·Result), ROADMAP.md(R1-2·R1-3 Evidence 칸), TASK.md(2026-11-18-c1-c2 항목), ISSUES.md(ISS-001), REPORT.md. 측정 스크립트와 캡처는 .work/ 아래(기록 대상 아님).
- 이슈: 미리보기 도구가 확인 화면의 링크 CSS(style.css)를 막아서(linkedCss loaded=false) 확인 화면은 `--inject src/style.css`로 같은 CSS를 주입해 쟀다(ISSUES.md ISS-001). C1 세로 4px는 상자 기준으로는 맞지만, 사람이 보는 간격(textarea 테두리 아래~글자 윗변)은 9px로 다르다.
- 해결: 없음
- 남은 문제: C1 세로 4px가 상자 간격인지 보이는 간격인지 소유자 판단 대기(보이는 간격 기준이면 C1은 실패). 확인 화면을 자기 링크 CSS로 그린 렌더는 미측정(ISS-001). 199자 상태의 C1·C2, 실제 키 입력, 높이 800 외 화면은 미측정. R1-2·R1-3은 verification pending 유지, 사용자 화면 확인도 별도로 남음.
- 다음 작업: 소유자가 C1 세로 기준을 정하면(상자 간격 유지 또는 보이는 간격 4px로 CSS 수정) 그에 맞춰 C1 행을 고치고 두 화면 4크기 x 2상태를 다시 잰다. 확인 화면 자기 CSS 렌더 측정 방법도 소유자가 정한다.

design check results:
- C1 요청 화면 | 8/8 | 4 sizes x 2 states, light | rendered | 320x800 200자 캡처: 세로 check 4 / observed 9, 오른쪽 check 0 / observed 0
- C1 확인 화면 | 8/8 | 4 sizes x 2 states, light | rendered (injected css) | 320x800 200자 캡처: 세로 check 4 / observed 9, 오른쪽 check 0 / observed 0
- C2 요청 화면 | 8/8 | 4 sizes x 2 states, light | rendered | 320x800 200자 캡처: check scrollWidth 320 / observed 오른쪽 끝 내용 열 303, scrollX 0
- C2 확인 화면 | 8/8 | 4 sizes x 2 states, light | rendered (injected css) | 320x800 200자 캡처: check scrollWidth 320 / observed 오른쪽 끝 내용 열 303, scrollX 0

상세 보고

측정 범위는 두 화면 x 너비 320·375·768·1280(높이 800) x 상태 빈 칸·200자, 라이트 모드다. 200자 상태는 스크립트로 값을 넣고 input 이벤트를 보내 만들었다. 글자 수 문구는 요청 화면 `0 / 200`·`199 / 200`·`200 / 200`, 확인 화면 `0 / 200`·`200 / 200`로 AC-002·AC-003 문구와 같게 나왔다(AC 문구, 빈 칸·200자는 4 sizes x 2 states, 199자는 요청 화면 375 1 size, rendered, not spot-checked).

C1 검사는 글자 수 span 상자의 top에서 textarea 상자의 bottom을 뺀 값과 두 상자의 right 차이를 읽는다. 모든 대상에서 세로 4px, 오른쪽 0px였다(C1 16/16, 4 sizes x 2 states x 2화면, rendered: 요청 화면 , 확인 화면 injected css, spot check differs: 세로 check 4 / observed 9). 320px 캡처에서 테두리 마지막 행과 글자 윗변 사이 빈 행은 9px였다. 13px 글자의 줄 높이 17px 안에 위쪽 여백이 있어서다. 오른쪽 끝은 캡처에서도 테두리 열과 글자 마지막 열이 같았다.

C2는 모든 대상에서 scrollWidth가 화면 너비 이하였다(C2 16/16, 4 sizes x 2 states x 2화면, rendered: 요청 화면 , 확인 화면 injected css, spot check: 320x800 check 320 / observed 내용 열 303, scrollX 0).

질문: C1의 "상자 아래 4px"는 두 요소 상자 사이 간격(지금 `--space-1` gap)인가요, 화면에 보이는 테두리~글자 간격인가요? 앞이면 C1 행의 Check를 그대로 두고, 뒤면 CSS 수정과 재측정이 필요합니다. 확인 화면을 링크 CSS 그대로 잴 방법(측정 도구 설정)도 정해 주세요.

