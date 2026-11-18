- 작업: 요청 화면(src/index.html)과 확인 화면(src/confirm.html)에서 DESIGN 규칙 C1·C2를 `node tools/measure.mjs`로 쟀다. 범위는 4 sizes(320·375·768·1280) x 3 states(빈 칸, 199자, 200자), 라이트 모드. 각 행은 캡처 픽셀로 스폿 체크했다. 코드는 고치지 않았다.
- 업데이트 파일: DESIGN.md(C1·C2 행의 Check·Spot check·Unmeasured·Result), ROADMAP.md(R1-2·R1-3 근거 칸), TASK.md(2026-11-18-c1-c2-measure 항목), ISSUES.md(ISS-001, ISS-002), REPORT.md(이 보고).
- 이슈: ISS-001 C1 간격의 측정값과 눈에 보이는 간격이 다르다. 상자 간격은 4px인데 칸 테두리 아래에서 글자 잉크 위까지는 9px다. ISS-002 측정 도구가 확인 화면의 style.css 로드를 막아서, 확인 화면은 같은 style.css를 주입해서 쟀다(우회).
- 해결: 없음.
- 남은 문제: C1 간격은 스폿 체크가 어긋나 통과로 치지 않는다. 규칙의 4px가 상자 간격인지 보이는 간격인지 제품 책임자가 정해야 한다. 확인 화면이 자기 CSS를 불러온 상태는 재지 못했다. 다크 모드는 승인 범위 밖이라 재지 않았다. R1-2와 R1-3은 verification pending을 유지한다.
- 다음 작업: C1 4px의 뜻을 정한다. 보이는 간격이라면 .char-count의 line-height나 간격을 고친 뒤 두 화면을 4 sizes x 3 states로 다시 잰다. 상자 간격이라면 DESIGN C1 행의 문구와 스폿 체크 기준을 고친다.

design check results:
- C1 gap (요청 화면) | 12/12 (상자 간격 4px) | 4 sizes x 3 states, light | rendered (own css) | 375 빈 칸: check 4 / observed 9
- C1 gap (확인 화면) | 12/12 (상자 간격 4px) | 4 sizes x 3 states, light | rendered (injected css) | 375 빈 칸: check 4 / observed 9
- C1 right edge (요청 화면) | 12/12 (차 0px) | 4 sizes x 3 states, light | rendered (own css) | 375 빈 칸: check 0 / observed 0
- C1 right edge (확인 화면) | 12/12 (차 0px) | 4 sizes x 3 states, light | rendered (injected css) | 375 빈 칸: check 0 / observed 0
- C2 overflow (요청 화면) | 12/12 (scrollWidth = 화면 너비) | 4 sizes x 3 states, light | rendered (own css) | 320 200자: check 320 / observed 오른쪽 끝 칠해진 열 x=303, 화면 320 안
- C2 overflow (확인 화면) | 12/12 (scrollWidth = 화면 너비) | 4 sizes x 3 states, light | rendered (injected css) | 320 200자: check 320 / observed 오른쪽 끝 칠해진 열 x=303, 화면 320 안
- 글자 수 문구 AC-002 (요청 화면) | 12/12 (`0 / 200`, `199 / 200`, `200 / 200`) | 4 sizes x 3 states, light | rendered (own css) | not spot-checked
- 글자 수 문구 AC-003 (확인 화면) | 12/12 (`0 / 200`, `199 / 200`, `200 / 200`) | 4 sizes x 3 states, light | rendered (injected css) | not spot-checked

C1 간격의 차이는 이렇게 생긴다. 요청 화면 375에서 칸 테두리의 마지막 줄은 y=303이고, 글자 수 상자는 4px 아래 y=308에서 시작한다. 그런데 13px 글자의 줄 상자가 17px 높이라서 글자 잉크는 y=313부터 보인다. 그래서 사람이 보는 간격은 9px다. C1 gap 줄은 상자끼리의 거리만 재므로, 규칙이 보이는 간격을 뜻한다면 두 화면 모두 C1을 어긴다.

확인 화면은 측정 도구가 confirm.html의 CSS 요청을 막는다(tools/measure.mjs의 환경 설정값). 그래서 확인 화면의 결과는 모두 같은 src/style.css를 주입한 값이다. 요청 화면은 자기 CSS를 불러온 상태(linkedCss loaded=true)에서 쟀다.

C1 right edge와 C2 overflow 줄은 스폿 체크 값이 측정값과 같았다(각 줄의 다섯째 칸). C1 행 전체의 판정은 C1 gap 줄의 스폿 체크 값에 맡기고 DESIGN 결과에는 not passed로 적었다.

질문: C1의 "상자 아래 4px"는 글자 수 상자와 칸 상자 사이의 거리인가, 아니면 눈에 보이는 글자까지의 거리인가? 답에 따라 CSS를 고칠지, DESIGN 행 문구를 고칠지가 정해진다.

report-check: ok 2,609 chars a71eca97
