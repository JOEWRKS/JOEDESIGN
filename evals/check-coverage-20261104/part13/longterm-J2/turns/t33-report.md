- 작업: 판 격자선을 연하게 했다. 선 색은 그대로 두고 진하기만 낮췄다(투명도 .55 → .4, tokens.css의 --grid-line-opacity 토큰으로). 캡처에서 선과 나무 바탕의 대비가 약 1.75:1에서 1.5:1로 줄었다. 별점(화점)과 판 가장자리 좌표 글자는 "격자선"이 아니라서 그대로 두었다. 값은 지시에 없어 내가 골랐다. 선이 너무 흐려지면 판이 안 읽히므로 확대 캡처를 직접 보고 선이 여전히 또렷한지 확인했다. 재현용 측정 도구 work/design/grid-check.mjs를 남겼다.
- 업데이트 파일: src/tokens.css, src/style.css, DESIGN.md(토큰 표 판 격자선 행), TASK.md(2026-11-10 판 격자선 연하게), ROADMAP.md(현재·다음 줄), work/design/grid-check.mjs(새 파일), 비교 캡처 work/design/shots/grid-390x844-before-after.png.
- 이슈: 격자선 진하기를 재는 측정은 이번엔 손으로 돌린 것이고 npm run design:check에는 넣지 않았다(어느 정도가 "적당히 연한지" 기준이 없어 실패 조건을 정할 수 없다). 판 위 표식 검사 실패는 이전부터 열린 금수 ✕ 대비(DS-06)다. 엔진 파일이 없어 가짜 엔진으로 쟀다(ENV-06).
- 해결: 없음(사용자 지시 변경이며, 전후 측정은 아래 결과 목록에 있다)
- 남은 문제: 격자선 진하기의 사용자 확인 전. 별점도 같이 연하게 할지 미정. ROADMAP 다음 작업 줄의 나머지 열린 항목은 그대로다.
- 다음 작업: 판을 보고 진하기가 괜찮은지 알려 준다. 더 연하게 하거나 별점도 맞출지 정해 준다.

display unchanged: no element moved, hidden, overlapped or merged; only the grid line opacity changed.

design-check results:
- grid line contrast before/after | 1440x900 1.73:1 before / 1.48:1 after; 390x844 1.75:1 before / 1.51:1 after | 2 sizes x 1 state (candidates; stub engine), light | rendered | 390x844 zoom before/after: lines lighter and still visible, observed
- DS-SP spacing and overflow | 83/83 pairs, 26/26 states clean | 2 sizes x 13 states | rendered | not spot-checked this turn
- DS-RING | 2/2 | 2 sizes x 1 state | rendered | not spot-checked this turn
- DS-BM | 4/8, only the known forbidden-mark failure (DS-06) | 2 sizes x 1 state x light and dark | rendered | not spot-checked this turn
report-check: ok 1,570 chars 927913f0
