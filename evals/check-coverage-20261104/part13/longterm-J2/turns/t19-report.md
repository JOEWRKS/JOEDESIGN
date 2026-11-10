- 작업: 시작 화면 로고 영역을 줄이고 휴대폰 대국 화면의 판을 키웠다. 먼저 짚을 점: 로고는 시작 화면에만 있고 휴대폰 대국 화면에는 없다(대결줄에서 숨겨짐). 그래서 로고를 줄여도 판은 커지지 않는다. 또 390x844에서는 판이 화면 폭에 막혀 있어 좌우 여백을 줄여야 커진다. 그래서 두 가지를 따로 했다. 로고: 그림을 3/4 크기로, "오목 한 판!" 제목 최대 크기를 96→72px로 줄였다. 휴대폰 판: 대결줄 높이 58→52px, 좌우 여백 12→8px, 판 크기 계산의 여유 40→32px. 처음엔 키 작은 휴대폰에도 여유를 32로 줄였는데 375x667·360x640 추천 화면에서 후보 알약 그림자가 잘리는 것을 검사가 잡아서, 높이 760 이하 휴대폰은 여유 40을 유지했다. 값은 지시에 없어 내가 골랐다.
- 업데이트 파일: src/style.css, DESIGN.md(토큰 표 화면 여백·대결줄 높이·시작 화면 로고 행), ISSUES.md(DS-04 경과), TASK.md(2026-11-10 로고 영역 줄이고 휴대폰 판 키우기), ROADMAP.md(현재 줄), work/design/motion-check.mjs, 비교 캡처 work/design/shots/logo-390x844-before-after.png, board-390x844-before-after.png, logo-board-before/.
- 이슈: 판 폭 변화는 489x866 433→447px, 430x932 406→414px, 390x844 366→374px, 375x667 284→290px, 360x640 257→263px이다. 데스크톱·태블릿 판은 그대로다. 로고 영역 높이는 1440x900 264→216px, 390x844 228→190px. 덤으로 작은 휴대폰 금수 알림 상태의 말풍선 그림자 잘림(DS-04 일부)이 없어졌다. DS-04의 "요" 한 글자 줄바꿈은 그대로다. 동작 감소 검사가 계산 숫자가 바뀌는 것을 움직임으로 잘못 세던 문제도 고쳤다. 엔진 파일이 없어 가짜 엔진으로 쟀다(ENV-06).
- 해결: 없음(사용자 지시 변경이며, 측정은 아래 결과 목록에 있다. DS-04 그림자 잘림은 결과 목록의 fix 줄 참고)
- 남은 문제: 로고·판 크기 값의 사용자 확인 전. DS-04 줄바꿈 open. 이전 턴의 열린 항목(동작 감소 확인, design:check 실패 2개의 원인 DS-06·DS-05·DS-01, 그림자 역할 값 확인, DS-07, 다크 모드 product decision pending과 색 확인, 구름, CO2, board 빈 파일, 카드 캡션·알림 여백·추천 고리 확인, style.css 추가 분리, --all 실행 시점, 복기 상단 바 product decision pending, 현재 수 세 곳 표시, 그림자 대상 질문, 태블릿·데스크톱 44px, v1·간격 규칙 확인, ENV-05, ENV-06)은 그대로다.
- 다음 작업: 휴대폰에서 판 크기와 줄어든 여백을 확인해 준다. 판을 더 키우려면 판 테두리 두께나 말풍선 칸 최소 높이를 줄이는 방법이 있는데, 말풍선 내용이 더 접힌다.

display unchanged: no element moved, hidden, overlapped or merged; the logo, top bar height, side margins and board size changed.

design-check results:
- DS-SP spacing and DS-TOUCH | 500/500 pairs, touch 440/440 | 12 sizes x 13 states (stub engine), light | rendered | not spot-checked this turn
- DS-SP-O overflow | 156/156 states clean | 12 sizes x 13 states, light | rendered | not spot-checked
- before/after board width and logo height | phone boards 433/406/366/284/257 before, 447/414/374/290/263 after; logo area 1440x900 264 before / 216 after | 12 sizes x 2 states (setup, candidates) | rendered | 390x844 side-by-side captures: board wider, logo smaller
- fix DS-04 bubble shadow clip on small phones | fixed | 375x667 forbid-notice-forced, light | rendered | 375x667: shadow rows 8 of 9 before / border 3 + shadow 5 all visible (pixel x=30, 456-463) after, capture
- regression caught during the change | 4 shadow-clips at 375x667 and 360x640 with slack 32, 0 after keeping 40 on short phones | 12 sizes x 13 states | rendered | not spot-checked
- DS-T, DS-O, DS-H | DS-T 213/213, DS-O 24/24, DS-H 0 below | 12 sizes x intro (DS-O also help) | rendered | not spot-checked this turn
- DS-SH | 60/60 | 12 sizes x 8 states | rendered | not spot-checked this turn
- DS-MO | 24/24 | 12 sizes x 2 states x reduce and control | rendered | not spot-checked this turn
report-check: ok 2,916 chars 9536bef9
