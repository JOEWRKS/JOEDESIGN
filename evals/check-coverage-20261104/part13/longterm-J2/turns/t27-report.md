- 작업: 휴대폰 가로 모드를 대응했다. 변경 전 844x390에서는 시작 화면의 "게임 시작!" 버튼이 화면 밖으로 밀려나 누를 수 없었고, 도움말 창도 잘렸다. 높이 500 이하인 가로 화면에서는 이제 판이 왼쪽에 화면 높이만큼 들어가고, 오른쪽 칸에 말풍선과 버튼이 온다. 대결줄은 48px, 주 버튼은 60px로 두고, 판 밖 버튼은 휴대폰 규칙대로 44px 이상으로 맞췄다(touch 528/528, 13 sizes x 13 states, rendered, not spot-checked this turn). 오른쪽 칸이 낮아서 말풍선 글자와 안쪽 여백은 세로 휴대폰 값을 쓴다. 시작 화면은 왼쪽에 제목과 시작 버튼, 오른쪽에 돌 색·강도 고르기를 둔다. 복기 상단 바는 두 칸 위 전체 폭에 둔다. 도움말은 세 단(설명 목록, 숫자의 뜻과 다시 보기 버튼, 엔진 라이선스)으로 한 화면에 넣었다. 복기·종료처럼 안내 줄의 두 요소가 이미 숨은 때는 빈 줄이 높이를 차지하지 않게 했다. 검사도 고쳤다: 844x390을 전체 크기 목록에 넣었고, 가로 휴대폰도 터치·44px 검사 대상으로 셌으며, 옆 칸끼리는 간격 검사를 하지 않게 했다. 값은 지시에 없어 내가 골랐다.
- 업데이트 파일: src/style.css, work/design/sizes.mjs, work/design/spacing-check.mjs, ds-v1-check.mjs, 다른 검사 스크립트 6개(휴대폰 판정), DESIGN.md(규칙 8-1, Rule Coverage 행), ISSUES.md(DS-08 open), TASK.md(2026-11-10 휴대폰 가로 모드), ROADMAP.md(현재 줄, DS1 확인 목록), 캡처 work/design/shots/spacing-844x390-*.png.
- 이슈: 키가 더 작은 가로 휴대폰 740x360에서는 복기와 금수 알림 상태에서 오른쪽 칸이 모자라 해설 카드 아래가 잘린다(DS-08). 같은 방식으로 더 줄이려면 복기 패널 일부를 접어야 하는데, 그건 보이는 내용을 숨기는 것이라 정하지 않고 남겼다. 667x375에서는 같은 넘침이 없었다(2 sizes x 13 states, rendered, not spot-checked). 가로 모드 디자인 검사에서 실패한 2개는 이전부터 열린 금수 ✕와 좌표 글자·첫 안내·수 세기 분홍 대비(DS-06, DS-05·DS-01)다. 엔진 파일이 없어 가짜 엔진으로 쟀고(ENV-06), 실제 기기의 주소창 높이는 반영하지 못했다.
- 해결: 없음(새 화면 대응이며, 측정은 아래 결과 목록에 있다)
- 남은 문제: 휴대폰 가로 배치의 사용자 확인 전. DS-08 open. 이전 턴의 열린 항목(도움말 카드·새 게임 확인 창, 390x844 E2E 기본 실행 밖, 범위 밖 간격 값 확인, 예전 승인 기록 출처, 스위치 파랑 확인, 검사 없는 규칙 4개와 일부만 재는 3개, 글자 하한 미강제, design:check 실패 2개의 원인 DS-06·DS-05·DS-01, 로고·판 크기 확인, DS-04 줄바꿈, 동작 감소 확인, 그림자 역할 값 확인, DS-07, 다크 모드 product decision pending과 색 확인, 구름, CO2, board 빈 파일, 카드 캡션·추천 고리 확인, style.css 추가 분리, --all 실행 시점, 복기 상단 바 product decision pending, 현재 수 세 곳 표시, 그림자 대상 질문, 태블릿·데스크톱 44px, v1 확인, ENV-05, ENV-06)은 그대로다.
- 다음 작업: 휴대폰을 가로로 돌려 확인해 준다. 키 360 가로 휴대폰의 복기 잘림은 복기 패널의 "종료된 대국" 줄을 접을지, 복기 바를 더 줄일지 정해 준다.

display unchanged: no visible element moved, hidden, overlapped or merged in portrait or desktop; in landscape the existing regions take a side-by-side layout and an empty guide row (both items already hidden) takes no height.

design-check results:
- design:check --all with 844x390 added | 6/8 PASS; FAIL board-marks (DS-06) and contrast (DS-05, DS-01) | 13 sizes x up to 13 states, light and dark (stub engine) | rendered | not spot-checked this turn
- DS-SP spacing, overflow, touch at 13 sizes | 533/533 pairs, 169/169 states clean, 528/528 buttons | 13 sizes x 13 states, light | rendered | 844x390 setup, candidates, replay and help captures: start button on screen, board left, cards and buttons right, help in three columns, observed
- DS-T and DS-O | 230/230, 26/26 | 13 sizes x intro and help | rendered | not spot-checked this turn
- before/after 844x390 | before: start button off screen, help clipped (DS-O 1/4 with 740x360); after: overflow 0 | 1 size x 13 states | rendered | 844x390 setup capture: start button visible after
- landscape 740x360 and 667x375 | 667x375 0 overflow; 740x360 4 overflow (replay-start, replay, help over replay, forced forbid notice) | 2 sizes x 13 states | rendered | not spot-checked
- DS-SH, DS-RING, DS-MO | 65/65, 13/13, 26/26 | 13 sizes | rendered | not spot-checked this turn
report-check: ok 3,170 chars 26717f5e
