- 작업: 디자인 토큰을 새 파일 src/tokens.css(36줄)로 분리했다. 옮긴 것은 색 변수 20개, 추천 고리 --rec-ring, 간격 토큰 --stack·--board-drop·--drop과 그 크기별 값(옆 배치·휴대폰·높이 700 이하)이다. 원래 순서를 지켜 옮겼고 src/style.css 맨 위에서 @import로 불러온다. 판 크기 계산에만 쓰는 배치 변수(--top, --cta, --hud-min, --rbar 등)와 변수 없이 박힌 원시 색 값은 토큰이 아니어서 style.css에 남겼다. 화면은 바뀌지 않아야 하는 정리라서, 분리 전후의 계산 스타일을 통째로 비교하는 검사 work/design/css-equivalence.mjs를 새로 만들어 확인했다. 토큰 목록을 세는 token-inventory.mjs도 두 파일을 함께 읽게 고쳤다.
- 업데이트 파일: src/tokens.css(새 파일), src/style.css, DESIGN.md(토큰 파일 위치 설명, Rule Coverage DS-EQ 행), TASK.md(2026-11-10 토큰을 tokens.css로 분리), ROADMAP.md(현재 줄 링크), work/design/css-equivalence.mjs(새 파일), work/design/token-inventory.mjs.
- 이슈: style.css는 526줄에서 515줄로 11줄만 줄었다. 길이 대부분은 토큰이 아니라 화면 요소별 규칙(판, 말풍선, 버튼, 복기, 도움말 등)과 그동안 뒤에 덧붙인 덮어쓰기 블록이다. 더 줄이려면 요소별 파일로 나누거나 덮어쓰기 블록을 원래 규칙에 합치는 정리가 따로 필요하다. 원시 색 값 57종을 토큰으로 바꾸는 일(1차 턴 Open Decisions)도 아직 안 했다. 엔진 파일이 없어 가짜 엔진으로 쟀다(ENV-06).
- 해결: 없음(화면 변화 없는 정리이며, 전후 비교는 아래 결과 목록에 있다)
- 남은 문제: style.css를 더 줄일지(요소별 분리, 덮어쓰기 블록 합치기)와 원시 색 토큰화는 사용자 결정 전. 이전 턴의 열린 항목(DS-04, CO2, board 빈 파일, 카드 캡션·알림 여백·추천 고리 확인, --all 실행 시점, 복기 상단 바 product decision pending, 현재 수 세 곳 표시, 그림자 대상 질문, 태블릿·데스크톱 44px, v1·간격 규칙 확인, DS-01, ENV-05, ENV-06)은 그대로다.
- 다음 작업: style.css를 요소별 파일로 더 나눌지 정해 준다. 나누면 같은 css-equivalence 검사로 화면이 그대로인지 확인한다.

display unchanged: no element moved, hidden, overlapped or merged; computed styles identical before and after.

design-check results:
- DS-EQ computed styles before/after split | 2249/2249 identical | 4 sizes (1440x900, 820x1180, 390x844, 360x640) x 5 states (setup, tutorial, candidates, preview, help; stub engine), light | rendered | 390x844 candidates bubble to chips: dump identical / observed 10px in capture pixels (x=40, 575 to 586)
- DS-EQ stability, two dumps before the split | 2249/2249 identical | 4 sizes x 5 states, light | rendered | not spot-checked
- DS-SP spacing | 83/83 pairs, overflow 26/26, touch 88/88 | 2 sizes (1440x900, 390x844) x 13 states, light | rendered | 390x844 candidates bubble to chips: check 10 / observed 10 (pixel x=40)
- DS-RING | 2/2 | 2 sizes x 1 state, light | rendered | not spot-checked this turn
- DS-T, DS-O | DS-T 36/36, DS-O 4/4 | 2 sizes x intro (DS-O also help), light | rendered | not spot-checked this turn
- tsc | passed | code | code | not spot-checked
report-check: ok 2,304 chars f41c0ef1
