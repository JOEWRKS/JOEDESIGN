# R1-2 글자 수 표시: C1·C2 측정 결과

C2와 C1의 오른쪽 끝은 측정값과 캡처 대조가 일치합니다. C1의 아래 간격은 검사 기준(상자 사이 4px)과 눈에 보이는 간격(9px)이 달라 대조 불일치이고, 이 부분은 규칙 해석을 정해 주셔야 끝납니다. 그래서 R1-2는 그대로 verification pending입니다.

디자인 검사 결과 (모두 `node tools/measure.mjs --inject src/style.css`, 너비 320·375·768·1280, 높이 800, 라이트):

- C1 오른쪽 끝 (#body-count.right − #body.right = 0) | 12/12 | 4 sizes x 3 states(빈 칸, 199자, 200자), light | rendered | 320x800 200자 캡처: check 0 / observed 0 (칸 테두리 마지막 열 303, 글자 잉크 마지막 열 303)
- C1 아래 간격 (#body-count.top − #body.bottom = 4px) | 12/12 | 4 sizes x 3 states, light | rendered | 320x800 200자 캡처: check 4 / observed 9 (칸 테두리 마지막 행 303, 글자 잉크 첫 행 313), 1280x800 200자도 같음; 대조 불일치
- C2 가로 넘침 (scrollWidth ≤ clientWidth) | 12/12 | 4 sizes x 3 states, light | rendered | 320x800 200자 캡처: check scrollWidth 320 / observed 가장 오른쪽 잉크 열 303 (화면 320 안, 캡처는 화면 영역만 담음)
- AC-002 표시 문구 (`0 / 200`, `199 / 200`, `200 / 200`) | 12/12 | 4 sizes x 3 states, light | rendered | 320x800 캡처에서 `200 / 200` 직접 확인
- 주입 없이 잰 비교 (link CSS 상태) | 아래 간격 -19, 오른쪽 차 +55 (서식 없음) | 320 x 3 states, light | rendered | not spot-checked; 도구가 link CSS를 막아(linkedCss loaded=false) 글자 수가 칸 옆에 무서식으로 놓임

- 작업: DESIGN C1·C2 행에 측정 방법을 정하고, 요청 화면을 4개 너비 x 3개 상태로 렌더 측정했습니다. 각 행을 320px 캡처의 픽셀 가장자리와 대조했습니다. 코드는 바꾸지 않았습니다.
- 업데이트 파일: DESIGN.md (C1·C2 행의 Check, Spot check, 범위, 미측정, Result), ROADMAP.md (R1-2 근거와 다음 작업 줄), TASK.md (2026-11-17-r1-2-measure 항목), ISSUES.md (ISS-001), REPORT.md. 측정 스크립트와 캡처는 .work/ 아래에 있습니다.
- 이슈: (1) C1 아래 간격: 규칙 문구 "상자 아래 4px"를 상자 기준으로 재면 4px이지만, 사람이 보는 테두리와 글자 사이 빈 줄은 9px입니다(13px 글자의 줄 높이 여백 때문). (2) ISS-001: `tools/measure.mjs`의 환경 설정이 link로 불러오는 style.css를 막아서, 모든 측정은 같은 CSS를 주입해 잰 값입니다. 실제 link 로드 렌더는 관찰하지 못했습니다.
- 해결: 없음
- 남은 문제: C1 아래 간격 기준 결정 대기, link CSS 실제 렌더 미관찰(ISS-001), 포커스·칸 크기 조절·확대 상태와 800 외 높이는 미측정, 사용자 화면 확인 대기. R1-2는 verification pending 유지.
- 다음 작업: 아래 질문에 답해 주시면 C1 행 문구나 CSS를 맞추고 다시 재겠습니다.

질문:
1. C1의 "4px"는 상자 사이 간격(지금 4px)인가요, 눈에 보이는 테두리와 글자 사이 간격(지금 9px)인가요? 보이는 간격이 기준이면 `.char-count`의 줄 높이나 여백을 바꿔야 하고, 그건 화면이 달라지는 변경이라 승인 뒤 하겠습니다.
2. link CSS가 막힌 도구 대신 주입 측정을 C1·C2 근거로 인정하실지, 아니면 link 로드 렌더를 따로 확인할 방법을 마련할지 정해 주세요.

report-check: ok 2,133 chars b5c19543
