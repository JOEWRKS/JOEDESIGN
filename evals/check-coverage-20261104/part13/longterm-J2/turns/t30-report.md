- 작업: 버튼 눌림 효과를 하나로 맞췄다. 먼저 버튼 13종을 마우스로 누른 채 재는 검사를 만들어 보니, 보조 버튼(아이콘 "새 게임", 새 게임 확인의 "새로 시작", 알약, 고르기 등)은 누르면 3px 내려가고 그림자 1px이 남는데, 주 버튼(종료 뒤 "새 게임!", 게임 시작, 추천 고르기, 두기)과 되돌리기만 5px 내려가고 2px이 남았다. 게다가 휴대폰에서는 주 버튼 그림자가 6px인데 5+2로 1px 더 내려갔고, 노랑·연두 주 버튼은 누르는 동안 안쪽 음영이 사라져 납작해 보였다. 이제 모든 버튼이 "그림자 길이 − 1px만큼 내려가고 1px이 남는다(그림자 아래 끝은 제자리)"로 같고, 쉬는 때 있던 안쪽 음영은 눌러도 남는다. 이 검사를 npm run design:check에 press로 넣었다.
- 업데이트 파일: src/style.css, work/design/press-check.mjs(새 파일), work/design/design-check.mjs, DESIGN.md(규칙 4, Rule Coverage DS-PR 행), TASK.md(2026-11-10 버튼 눌림 효과 통일), ROADMAP.md(현재 줄), 캡처 work/design/shots/press-390x844-rest.png, press-390x844-down.png.
- 이슈: "새 게임 버튼"이 세 개(위쪽 아이콘, 종료 뒤 큰 "새 게임!", 확인 창의 "새로 시작")라 셋 다 쟀고, 실제로 달랐던 것은 큰 "새 게임!"과 다른 주 버튼들이었다. 휴대폰의 노랑 주 버튼은 원래 쉬는 때 안쪽 음영이 없어서(데스크톱에는 있음) 그대로 두었다. 키보드 Enter나 실제 손가락 터치로 누르는 것은 마우스로 흉내 내 쟀다. 엔진 파일이 없어 가짜 엔진으로 쟀다(ENV-06).
- 해결: 없음(사용자 지시 변경이며, 전후 측정은 아래 결과 목록에 있다)
- 남은 문제: 통일한 눌림 효과의 사용자 확인 전. 휴대폰 노랑 주 버튼의 안쪽 음영 유무(데스크톱과 다름). 이전 턴의 열린 항목(말풍선 밖 11·11.5px, 휴대폰 가로 확인, DS-08, 도움말 카드·새 게임 확인 창, 390x844 E2E 기본 실행 밖, 범위 밖 간격 값 확인, 예전 승인 기록 출처, 스위치 파랑 확인, 검사 없는 규칙 4개와 일부만 재는 3개, design:check 실패 2개의 원인 DS-06·DS-05·DS-01, 로고·판 크기 확인, DS-04 줄바꿈, 동작 감소 확인, 그림자 역할 값 확인, DS-07, 다크 모드 product decision pending과 색 확인, 구름, CO2, board 빈 파일, 카드 캡션·추천 고리 확인, style.css 추가 분리, --all 실행 시점, 복기 상단 바 product decision pending, 현재 수 세 곳 표시, 그림자 대상 질문, 태블릿·데스크톱 44px, v1 확인, ENV-05, ENV-06)은 그대로다.
- 다음 작업: 버튼을 눌러 보고 느낌을 확인해 준다. 휴대폰 노랑 버튼에도 데스크톱처럼 안쪽 음영을 넣을지 정해 준다.

display unchanged: no element moved, hidden, overlapped or merged; only the pressed state of the main buttons changed.

design-check results:
- DS-PR press effect | 169/169 buttons, remaining shadow 1px everywhere | 13 sizes x up to 13 buttons (stub engine), light | rendered | 390x844 finished "새 게임!": check 5px move + 1px / observed top border rows 10-13 rest vs 15-18 pressed, bottom edge row 75 in both, capture pixels
- before/after DS-PR | 17/26 before (main buttons 5+2, phone overshoot 1px, inset lost), 169/169 after | 2 sizes before, 13 sizes after | rendered | 390x844 rest/pressed captures after; before values from the check only
report-check: ok 2,158 chars 470315ed
