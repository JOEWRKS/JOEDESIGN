- 작업: 다크 모드에서 판 위 추천 고리와 금수 표시를 실제 화면으로 확인했다. 가짜 엔진으로 흑을 F8·G8·H6·H7에 두어 H8을 실제 3-3 금수로 만든 상태를 라이트·다크, 1440x900·390x844에서 찍고, 표식 색과 판 나무색의 대비를 계산값과 캡처 픽셀 두 가지로 쟀다. 이 확인용 검사 work/design/board-marks-check.mjs를 새로 만들었다. 코드는 바꾸지 않았다. 결론: 추천 고리는 잘 보이고, 금수 ✕는 잘 안 보인다. 판은 두 모드에서 같은 색이라 결과도 두 모드가 같다. 즉 금수 ✕가 흐린 것은 다크 모드 탓이 아니라 원래 있던 문제다.
- 업데이트 파일: ISSUES.md(DS-06 open), TASK.md(2026-11-10 다크 모드 추천 고리·금수 표시 확인), DESIGN.md(Rule Coverage DS-BM 행), ROADMAP.md(현재 줄), work/design/board-marks-check.mjs(새 파일), 캡처 work/design/shots/board-marks-*.png와 확대 비교 board-marks-1440x900-light-vs-dark.png.
- 이슈: 금수 ✕(분홍 #ff6f91 점선 고리와 ✕)는 판 나무색과 대비가 1.55~1.96:1로, 그림 요소 기준 3:1에 못 미친다. ✕가 작고 H8처럼 별점 위에 오면 갈색 점과 겹친다(DS-06). 흑으로 둘 때 금수 자리를 알아보기 어렵다. 엔진 파일이 없어 가짜 엔진으로 쟀다(ENV-06).
- 해결: 없음
- 남은 문제: DS-06 금수 ✕ 대비(색·굵기 결정 필요). 이전 턴의 열린 항목(다크 모드 product decision pending과 색 확인, 구름, DS-05, DS-04, DS-01, CO2, board 빈 파일, 카드 캡션·알림 여백·추천 고리 확인, style.css 추가 분리, --all 실행 시점, 복기 상단 바 product decision pending, 현재 수 세 곳 표시, 그림자 대상 질문, 태블릿·데스크톱 44px, v1·간격 규칙 확인, ENV-05, ENV-06)은 그대로다.
- 다음 작업: 금수 ✕를 더 진한 빨강 계열과 굵은 선으로 바꿀지 정해 준다(바꾸면 board-marks-check와 캡처로 확인).

design-check results:
- DS-BM recommendation ring | 4/4 at 3.99-5.03:1 | 2 sizes x 1 state (black to move with a 3-3 point; stub engine) x light and dark | rendered | dark 1440x900: check 3.99-5.03:1 / observed pixel rgb(54,93,79) 4.34:1 vs wood
- DS-BM forbidden mark | 0/4 at 1.55-1.96:1 | 2 sizes x 1 state x light and dark | rendered | dark 1440x900: check 1.55-1.96:1 / observed pixel rgb(223,112,142) 1.80:1 vs wood, zoom crop
report-check: ok 1,566 chars b5610919
