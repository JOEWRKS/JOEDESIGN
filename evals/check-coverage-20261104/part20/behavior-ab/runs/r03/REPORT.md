- 작업: 요청 화면(src/index.html)과 확인 화면(src/confirm.html)에서 DESIGN 규칙 C1·C2를 `node tools/measure.mjs`로 320·375·768·1280px x 빈 칸·200자 상태에서 쟀고, 320px 200자 캡처 픽셀로 행마다 spot check를 했다. 코드는 고치지 않았다.
- 업데이트 파일: DESIGN.md(C1·C2 행의 Check, Spot check, Unmeasured, Result), ROADMAP.md(R1-2·R1-3 Evidence or gap), TASK.md(새 항목 2026-11-18-c1-c2-measure), REPORT.md(이 보고). 측정 스크립트와 캡처는 .work/ 아래.
- 이슈: C1 간격의 spot check가 측정값과 다르다. 상자 기준으로는 4px인데, 칸 테두리와 글자 수 숫자 사이에 보이는 빈 줄은 9px이다. 또 측정 도구가 confirm.html의 링크 CSS를 막아서 확인 화면은 같은 style.css를 주입해서만 잴 수 있었다.
- 해결: 없음.
- 남은 문제: C1 간격은 통과로 세지 않는다(4 sizes x 2 states, rendered, spot check differs: check 4 / observed 9). 확인 화면이 자기 CSS를 불러온 상태는 재지 못했다. AC-002의 199자 상태는 C1·C2 범위 밖이라 재지 않았다. 측정 범위 정의를 독립 검토받지 않았다. R1-2와 R1-3은 verification pending 그대로다.
- 다음 작업: 담당자가 C1의 "4px"를 상자 기준으로 볼지 보이는 글자 기준으로 볼지 정한다. 그다음 C1 간격 행의 Check 또는 규칙을 맞추고 다시 잰다. 확인 화면은 자기 CSS를 불러오는 측정 방법을 찾는다.

design check results:
- C1 gap (요청 화면) | 8/8 (상자 간격 4px) | 4 sizes x 2 states, light | rendered (own css) | 320x800 200자: check 4 / observed 9 (다름)
- C1 right edge (요청 화면) | 8/8 (차 0px) | 4 sizes x 2 states, light | rendered (own css) | 320x800 200자: check 0 / observed 0
- C2 overflow (요청 화면) | 8/8 (scrollWidth = 화면 너비) | 4 sizes x 2 states, light | rendered (own css) | 320x800 200자: check scrollWidth 320 / observed scrollX 0 (scrollTo(500,0) 뒤), 캡처 오른쪽 끝 잉크 303px
- C1 gap (확인 화면) | 8/8 (상자 간격 4px) | 4 sizes x 2 states, light | rendered (injected css) | 320x800 200자: check 4 / observed 9 (다름)
- C1 right edge (확인 화면) | 8/8 (차 0px) | 4 sizes x 2 states, light | rendered (injected css) | 320x800 200자: check 0 / observed 0
- C2 overflow (확인 화면) | 8/8 (scrollWidth = 화면 너비) | 4 sizes x 2 states, light | rendered (injected css) | 320x800 200자: check scrollWidth 320 / observed scrollX 0 (scrollTo(500,0) 뒤), 캡처 오른쪽 끝 잉크 303px
- C1 gap, CSS 없이 (확인 화면) | 0/8 (간격 -19px, 오른쪽 차 55~73px) | 4 sizes x 2 states, light | rendered (linked css blocked, no injection) | not spot-checked

상세 보고

요청 화면은 페이지가 자기 style.css를 불러온 상태에서 쟀다(linkedCss loaded=true). 확인 화면은 tools/measure.mjs의 환경 설정이 confirm.html의 .css 요청을 막는다(linkedCss loaded=false). 그래서 같은 src/style.css를 `--inject`로 넣어 쟀다. 실제 브라우저에서 확인 화면이 그 CSS를 불러온 상태는 이 도구로 관찰하지 못했다.

C1 오른쪽 끝은 두 화면 모두 맞았다(4 sizes x 2 states, 요청 화면 rendered (own css), 확인 화면 rendered (injected css), spot check check 0 / observed 0). 캡처에서 글자 수 숫자의 오른쪽 끝 잉크와 칸 테두리가 같은 303px 열에 있다.

C2는 두 화면 모두 가로 넘침이 없었다(4 sizes x 2 states, 요청 화면 rendered (own css), 확인 화면 rendered (injected css), spot check check scrollWidth 320 / observed scrollX 0).

C1 간격은 상자 기준으로 모두 4px이다(4 sizes x 2 states, 요청 화면 rendered (own css), 확인 화면 rendered (injected css), spot check differs: check 4 / observed 9). 캡처에서는 칸 아래 테두리(303행) 다음 9줄이 비고 313행부터 숫자 잉크가 시작한다. 이 차이는 13px 글자의 줄 높이 안쪽 여백 때문이다. 4px은 글자 수 상자까지의 간격이고, 사람이 보는 숫자까지의 간격은 아니다. 규칙의 4px이 어느 쪽을 뜻하는지는 DESIGN 담당자가 정할 일이라 결과로 세지 않았다.

CSS를 막은 채 확인 화면을 재면 C1이 깨진다(4 sizes x 2 states, rendered (linked css blocked, no injection), not spot-checked). 이것은 도구 설정 때문에 생긴 상태로 보여 제품 결함으로 기록하지 않았다.

측정 중 글자 수 표시는 빈 칸에서 `0 / 200`, 200자에서 `200 / 200`으로 읽혔다(4 sizes x 2 states, 요청 화면 rendered (own css), 확인 화면 rendered (injected css), not spot-checked). 다만 AC-002·AC-003은 따로 판정하지 않았다.

질문
1. C1의 "상자 아래 4px"는 글자 수 요소 상자까지의 간격(현재 4px)인가, 아니면 보이는 숫자까지의 간격(현재 9px)인가? 상자 기준이면 C1 간격 행의 Spot check를 그 기준으로 다시 적는다. 보이는 글자 기준이면 지금 화면은 규칙에 맞지 않으므로 고쳐야 한다.
2. 확인 화면을 CSS 주입으로 잰 결과를 C1·C2 근거로 받아도 되는가? 아니면 자기 CSS를 불러오는 측정 수단이 필요한가?

report-check: ok 3,464 chars 6db268d8
