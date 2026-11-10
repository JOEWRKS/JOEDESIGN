- 작업: 판 밖 요소의 입체 그림자 깊이를 역할 다섯 가지로 묶어 통일했다. 먼저 역할별로 실제 그림자 길이를 재는 검사 work/design/shadow-check.mjs를 만들어 12크기에서 쟀더니, 60개 역할 묶음 중 29개만 값이 하나였다. 카드는 말풍선 8, 첫 안내 7, 내 수 평가·복기 패널·복기 바 5로 제각각이었고, 보조 버튼도 아이콘(휴대폰 3)·취소 5·승률 가이드 스위치 3이 달랐으며, 대결줄 4와 카드 라벨 3도 달랐다. 정한 값(tokens.css의 그림자 토큰): 카드 6px(휴대폰 5px), 대화상자 8px, 주 버튼 7px(휴대폰 6px), 보조 버튼 4px, 라벨·칩 3px. 주 버튼과 대화상자는 원래 같아서 값은 그대로다. 블록 사이 간격 규칙이 그림자 길이를 아래 여백으로 쓰므로 그 여백도 같은 토큰에 묶어 보이는 간격이 그대로 유지되게 했다. 누른 버튼이 내려앉는 거리도 보조 버튼 그림자에 맞췄다. 판 위 돌·표식은 대상에서 뺐다. 값은 지시에 없어 내가 골랐다.
- 업데이트 파일: src/tokens.css, src/style.css, DESIGN.md(토큰 표 그림자 행, Rule Coverage DS-SH 행), TASK.md(2026-11-10 그림자 깊이 역할별 통일), ROADMAP.md(현재 줄), work/design/shadow-check.mjs(새 파일), 캡처 work/design/shots/spacing-*.png와 shadow-before/.
- 이슈: 눈에 띄는 변화는 말풍선 그림자가 8→6px(휴대폰 6→5)로 얕아지고, 내 수 평가·복기 패널·복기 바는 5→6px로 깊어진 것이다. 작은 휴대폰 금수 알림 상태의 말풍선 그림자 1px 잘림(DS-04)은 그대로 남아 있다. style.css 끝에 덮어쓰는 블록을 하나 더 붙였으므로 앞쪽 개별 그림자 값은 이제 쓰이지 않는 채 남아 있다(정리는 style.css 분리 결정과 같이). 엔진 파일이 없어 가짜 엔진으로 쟀다(ENV-06).
- 해결: 없음(사용자 지시 변경이며, 전후 측정은 아래 결과 목록에 있다)
- 남은 문제: 그림자 역할 값(카드 6/5 등)의 사용자 확인 전. 이전 턴의 열린 항목(DS-07 태블릿 말풍선 재현 안 됨, DS-06, 다크 모드 product decision pending과 색 확인, 구름, DS-05, DS-04, DS-01, CO2, board 빈 파일, 카드 캡션·알림 여백·추천 고리 확인, style.css 추가 분리, --all 실행 시점, 복기 상단 바 product decision pending, 현재 수 세 곳 표시, 그림자 대상 질문, 태블릿·데스크톱 44px, v1·간격 규칙 확인, ENV-05, ENV-06)은 그대로다. 3차 턴 그림자 대상 질문은 이번 통일로 내 수 카드가 6px가 되어 다시 볼 필요가 있다.
- 다음 작업: 화면에서 카드 그림자 6px(휴대폰 5px)가 괜찮은지 알려 준다. 값만 바꾸면 tokens.css 한 곳에서 바뀌고 shadow-check와 spacing-check로 다시 잰다.

display unchanged: no element moved, hidden, overlapped or merged; only shadow depths and the matching bottom margins changed.

design-check results:
- DS-SH shadow roles | 60/60 role groups uniform | 12 sizes x 8 states (stub engine), light | rendered | 1440x900 candidates bubble: check 6 / observed 6 (pixel x=1000, rows 356-365 = border 4 + shadow 6); review card: check 6 / observed 6 (rows 127-135 = 3 + 6)
- before/after DS-SH | 29/60 before, 60/60 after | 12 sizes x 8 states, light | rendered | 1440x900 bubble shadow 8 before / 6 after, review card 5 before / 6 after, capture pixels
- DS-SP spacing | 500/500 pairs, touch 440/440 | 12 sizes x 13 states, light | rendered | 1440x900 review card to bubble: check 12 / observed 12 (pixel x=1000, 135 to 148)
- DS-SP-O overflow | 154/156 states, the 2 known DS-04 shadow-clips at 375x667 and 360x640 | 12 sizes x 13 states, light | rendered | not spot-checked this turn
- DS-EQ changed properties before/after | box-shadow 72, margin-bottom 40, --drop text, opacity 2 (logo animation timing) | 4 sizes x 5 states, light | rendered | not spot-checked
- DS-CR dark | 2/14 states clean, only the known DS-05 items | 2 sizes x 7 states, dark | rendered | not spot-checked this turn
- tsc | passed | code | code | not spot-checked
report-check: ok 2,805 chars b869ce2a
