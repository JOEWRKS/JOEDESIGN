# C1·C2 측정 보고 (요청 화면, 확인 화면)

- 작업: DESIGN 규칙 C1(글자 수 위치)·C2(가로 넘침 규칙)를 `node tools/measure.mjs`로 요청 화면(src/index.html)·확인 화면(src/confirm.html)에서 DESIGN.md 행의 크기·상태 그대로 쟀다. 크기·상태·측정 방식과 결과는 아래 목록의 각 줄에 있다. 소스는 고치지 않았다.
- 업데이트 파일: DESIGN.md(C1·C2 행의 Check·Spot check·Unmeasured·Result), TASK.md(2026-11-18-c1-c2 항목), ROADMAP.md(R1-2·R1-3 Evidence 칸, 현재/다음 줄), ISSUES.md(측정 우회 1건), REPORT.md. 임시 스크립트·캡처는 .work/ 아래.
- 이슈: (1) 측정 도구가 confirm.html의 링크 CSS(style.css)를 막는다(`linkedCss` loaded=false, 16회 모두). 그래서 확인 화면은 같은 src/style.css를 주입해서만 쟀다. (2) C1 세로 간격은 상자 기준 4px지만 화면에 보이는 간격(입력 칸 아래 테두리 → 글자)은 9px라서 spot check가 어긋난다.
- 해결: 없음
- 남은 문제: C1 세로 4px의 뜻 결정 대기(아래 질문). 확인 화면을 자체 CSS 로드로 연 상태는 측정하지 못함(ISSUES.md 측정 우회). R1-2의 AC-002 199자 상태는 이번에 재지 않음. R1-2·R1-3은 verification pending 유지, 사용자 화면 확인 별도.
- 다음 작업: 소유자가 C1 세로 기준을 정하면 그 기준으로 C1 행을 고쳐 다시 잰다. 확인 화면을 자체 CSS로 여는 측정 방법(도구 설정은 환경 소유)이 생기면 C1·C2를 확인 화면에서 다시 잰다. 그 뒤 AC-002·AC-003 상태 확인.

design check results:
- C1 세로 간격, 요청 화면 | 8/8 (상자 간격 4px) | 4 sizes x 2 states, light | rendered (own css) | 320 빈 칸: check 4 / observed 9, differs
- C1 오른쪽 끝, 요청 화면 | 8/8 (차 0px) | 4 sizes x 2 states, light | rendered (own css) | 320 빈 칸: check 0 / observed 0
- C2 넘침, 요청 화면 | 8/8 (scrollWidth = 화면 너비) | 4 sizes x 2 states, light | rendered (own css) | 320 빈 칸: check scrollWidth 320 / observed 캡처 오른쪽 끝 내용 열 303
- C1 세로 간격, 확인 화면 | 8/8 (상자 간격 4px) | 4 sizes x 2 states, light | rendered (injected css) | 320 빈 칸: check 4 / observed 9, differs
- C1 오른쪽 끝, 확인 화면 | 8/8 (차 0px) | 4 sizes x 2 states, light | rendered (injected css) | 320 빈 칸: check 0 / observed 0
- C2 넘침, 확인 화면 | 8/8 (scrollWidth = 화면 너비) | 4 sizes x 2 states, light | rendered (injected css) | 320 빈 칸: check scrollWidth 320 / observed 303
- 확인 화면 자체 CSS 로드 | 0/8 로드됨, CSS 없는 화면에서 C1 0/8 (세로 −19px, 오른쪽 차 55~73px) | 4 sizes x 2 states, light | rendered (linked css blocked by tool) | not spot-checked

C1은 두 화면 모두 통과로 볼 수 없다(4 sizes x 2 states, rendered (own css) 요청 화면 / rendered (injected css) 확인 화면, spot check differs: check 4 / observed 9). 오른쪽 끝은 맞지만(8/8 두 화면, 4 sizes x 2 states, rendered (own css) 요청 화면 / rendered (injected css) 확인 화면, spot check 0 / 0), 세로 간격은 검사가 재는 상자 간격 4px와 화면에서 보이는 간격 9px가 다르다(spot check differs: check 4 / observed 9). 글자 수 줄의 상자(높이 17px)가 13px 글자보다 크고 글자 위 여백이 있어서 생기는 차이다. JOEDESIGN 규칙상 두 값이 다르면 검사나 규칙 행을 먼저 고쳐야 결과로 센다.

C2는 두 화면 모두 넘침이 없다(8/8 각각, 4 sizes x 2 states, 요청 화면 rendered (own css) / 확인 화면 rendered (injected css), spot check 320 빈 칸: check 320 / observed 303). 다만 확인 화면은 주입 CSS로 잰 것이라, 페이지가 자기 style.css를 불러온 상태의 결과는 아직 없다. 글자 수 문구는 빈 칸 `0 / 200`, 200자 `200 / 200`으로 읽혔다(4 sizes x 2 states, rendered (own css) 요청 화면 / rendered (injected css) 확인 화면, not spot-checked).

질문(소유자): C1의 "상자 아래 4px"는 (가) 글자 수 요소 상자와 입력 칸 상자 사이(지금 4px, 4 sizes x 2 states, rendered (own css) / rendered (injected css), spot check differs: check 4 / observed 9), (나) 화면에 보이는 입력 칸 테두리와 글자 사이(320 빈 칸 캡처에서 9px, 4px 기준이면 맞지 않음) 중 어느 쪽인가? (가)면 C1 행에 "요소 상자 기준"을 적고 spot check를 상자 기준으로 다시 하면 되고, (나)면 화면 수정이 필요하다(제품 정의 RULE-002 "시각적으로 붙어 보여야" 범위 안의 디자인 수정).
report-check: ok 3,088 chars d0781c76
