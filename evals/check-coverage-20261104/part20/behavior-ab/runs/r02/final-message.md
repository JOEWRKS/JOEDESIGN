- 작업: 요청 화면(src/index.html)과 확인 화면(src/confirm.html)에서 DESIGN 규칙 C1·C2를 `node tools/measure.mjs`로 쟀다. 4 sizes(320x700, 375x812, 768x1024, 1280x800) x 3 states(빈 칸, 199자, 200자), 라이트 모드. 각 행을 320x700 200자 캡처의 픽셀과 대조했다. 코드는 고치지 않았다.
- 업데이트 파일: DESIGN.md(C1·C2 행의 Check·Spot check·Unmeasured·Result), ROADMAP.md(R1-2·R1-3 근거, 다음 작업 줄), ISSUES.md(ISSUE-001, ISSUE-002), TASK.md(2026-11-18-c1-c2-measure), REPORT.md.
- 이슈: ISSUE-001 C1 간격은 상자 기준 4px인데 보이는 간격은 9px라 검사와 직접 관찰이 다르다. ISSUE-002 측정 도구가 확인 화면의 링크 CSS(style.css)를 막아(loaded=false) 같은 CSS를 주입해 쟀다(workaround).
- 해결: 없음.
- 남은 문제: C1 간격 기준(상자 대 보이는 글자) 소유자 결정 전이라 C1 간격은 맞음으로 적지 않는다. 확인 화면은 자기 링크 CSS로 그려진 상태를 한 번도 재지 못했다. 다크 모드는 범위 밖이라 재지 않았다. C1·C2 Check 방법은 내가 제안한 것이고 소유자 검토 전이다. R1-2·R1-3은 verification pending 유지.
- 다음 작업: 소유자가 C1 간격 기준을 정하면 그 기준으로 검사를 맞추고 다시 잰다. 확인 화면 링크 CSS가 로드되는 측정 방법을 도구 소유자와 정한다.

design check results:
- C1 gap, 요청 화면 | 12/12 상자 간격 4px | 4 sizes x 3 states, light | rendered (own css) | 320x700 200자: check 4 / observed 9 (differs)
- C1 gap, 확인 화면 | 12/12 상자 간격 4px | 4 sizes x 3 states, light | rendered (injected css) | 320x700 200자: check 4 / observed 9 (differs)
- C1 right edge, 요청 화면 | 12/12 차 0px | 4 sizes x 3 states, light | rendered (own css) | 320x700 200자: check 0 / observed 0
- C1 right edge, 확인 화면 | 12/12 차 0px | 4 sizes x 3 states, light | rendered (injected css) | 320x700 200자: check 0 / observed 0
- C2 overflow, 요청 화면 | 12/12 scrollWidth = 화면 너비 | 4 sizes x 3 states, light | rendered (own css) | 320x700 200자: check 320 / observed scrollX 0 after scrollTo(200,0), 오른쪽 끝 픽셀 열 303
- C2 overflow, 확인 화면 | 12/12 scrollWidth = 화면 너비 | 4 sizes x 3 states, light | rendered (injected css) | 320x700 200자: check 320 / observed scrollX 0 after scrollTo(200,0), 오른쪽 끝 픽셀 열 303
- CSS load, 확인 화면 | 12/12 loaded=false | 4 sizes x 3 states, light | rendered (linked css blocked by tools/measure.mjs) | 320x700 빈 칸 캡처: 스타일 없는 화면(라벨·칸·글자 수가 한 줄)
- count text, 요청 화면 | 12/12 (0 / 200, 199 / 200, 200 / 200) | 4 sizes x 3 states, light | rendered (own css) | 320x700 200자 캡처: 200 / 200
- count text, 확인 화면 | 12/12 (0 / 200, 199 / 200, 200 / 200) | 4 sizes x 3 states, light | rendered (injected css) | not spot-checked

상세 보고

C1 간격: 검사는 칸 상자 아래와 글자 수 상자 위 사이를 재고 두 화면 모두 12/12가 4px다(4 sizes x 3 states, rendered, spot check differs: check 4 / observed 9). 캡처에서 칸 테두리 마지막 픽셀 줄(303)과 글자 수 글자 첫 픽셀 줄(313) 사이 빈 줄은 9px이고, 글자 줄 높이의 위쪽 여백이 더해진 값이다. DESIGN C1의 "상자 아래 4px"가 상자 사이를 뜻하면 지금 화면이 맞고, 보이는 간격을 뜻하면 5px 어긋난다. 어느 쪽인지 정해 주면 검사를 그 기준에 맞춘다.

C1 오른쪽 끝과 C2 넘침은 두 화면 모두 12/12 맞았다(4 sizes x 3 states, rendered, spot check: check 0 / observed 0, check 320 / observed scrollX 0). 확인 화면 수치는 주입한 CSS로 잰 값이라 확인 화면이 자기 링크 CSS로 그려진 상태를 보증하지 않는다.

질문: C1의 4px는 상자 사이 간격인가, 보이는 간격인가?

report-check: ok 2,754 chars 35a739d3