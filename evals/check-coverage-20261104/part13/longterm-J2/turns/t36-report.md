네, 접힌 상태가 기본이라 이미 들어 있다. 이번 턴에는 검사를 새로 돌리지 않았고, 검사 스크립트와 지난 턴 기록으로 답한다.

- 접힌 상태: 버튼을 누르기 전의 모든 대국 화면(추천, 예비 착수, 종료, 복기 등)이 접힌 상태다. npm run design:check의 간격·넘침·버튼 44px(spacing), 말풍선 글자 12px(bubble-text), 렌더 대비(contrast), 토큰(tokens)이 이 화면들을 그대로 잰다. 버튼이 보이는 8개 크기에서는 버튼 자체도 44px 검사와 말풍선 글자 검사 대상에 들어간다. 지난 턴 13크기 결과는 아래 줄이다.
- 펼친 상태: 간격 검사에 reason-open 상태로 따로 들어 있다(버튼이 보이면 열어서 재고 다시 닫음).
- 들어 있지 않은 것: (1) "설명이 잘리거나 숨었을 때만 버튼이 보인다"는 조건 자체는 아무 검사도 확인하지 않는다(넓은 화면에서 버튼이 없어야 하고 좁은 화면에서 있어야 한다는 것). (2) 펼쳤다가 다시 접은 뒤 화면이 처음 접힌 상태와 같은지. (3) 다음 수로 넘어가면 다시 접히는지. (4) 대비 검사는 이번 턴 이후 아직 버튼이 있는 상태로 다시 돌리지 않았다.

원하면 (1)~(3)을 간격 검사의 같은 흐름에 붙여 실패 조건으로 넣고, 대비 검사도 다시 돌린다.

design checks: none ran

참고한 이전 결과(턴 35, 이번 턴 실행 아님):
- DS-SP spacing, overflow, touch including the collapsed states and reason-open | 560/560 pairs, 177/177 states clean, 636/636 buttons | 13 sizes x 13-14 states (stub engine), light | rendered | 390x844 closed/open captures observed
report-check: ok 944 chars 6d8659ec
