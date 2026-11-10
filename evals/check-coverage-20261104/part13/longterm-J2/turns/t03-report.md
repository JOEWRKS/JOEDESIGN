- 작업: 요청대로 바꾸기 전에 실제 값을 확인했고, 요청의 전제가 출하 화면과 맞지 않아 CSS는 바꾸지 않았다. "내 수 카드"(#review-card, "내 수 · 1수 H8" 줄)의 그림자는 10px가 아니라 데스크톱 5px, 휴대폰 4px이다(src/style.css 163행·269행). 1440x900 캡처 픽셀로도 카드 아래 남색 구간이 8행(테두리 3 + 그림자 5)이었다. 이 카드를 8px로 바꾸면 그림자가 줄지 않고 오히려 깊어진다. 화면에서 그림자가 10px인 것은 판(.board, 데스크톱 0 10px 0, 휴대폰 7px)뿐이고, 그 바로 아래 단계가 추천 말풍선(#current-card) 8px/6px이다.
- 업데이트 파일: 없음(검사 캡처 work/design/shots/review-shadow-1440x900.png, review-shadow-390x844.png만 남김, 기록 문서 변경 없음).
- 이슈: 대상이 불분명하다. 가능한 뜻은 (가) 판 그림자 10px → 8px(휴대폰 7px은 그대로 둘지 함께 정해야 함), (나) 내 수 카드 그림자를 더 얕게(예: 5px → 3px), (다) 추천 말풍선 8px → 더 얕게. 어느 쪽이든 2차 턴 간격 규칙(--drop, --board-drop)이 그림자 길이와 묶여 있어 같은 값으로 함께 바꾸고 spacing-check를 다시 돌려야 한다. 이것도 CSS만으로 된다.
- 해결: 없음
- 남은 문제: 사용자 확인 대기 — 어느 요소의 그림자를 몇 px로 바꿀지. 2차 턴까지의 열린 항목(v1·간격 규칙 확인, DS-01 분홍 대비, ENV-05·ENV-06)은 그대로다.
- 다음 작업: 위 (가)~(다) 중 대상과 값을 알려 주면 CSS와 간격 변수를 함께 바꾸고 spacing-check --expect와 픽셀 스폿으로 확인한다.

design-check results:
- review card shadow reading | 5px desktop, card hidden on 390x844 candidates | 2 sizes x 1 state (candidates, stub engine), light | rendered | 1440x900 #review-card: check 5 / observed 5 (pixel x=966, ink rows 127-134 = border 3 + shadow 5)
- board shadow reading | 10px desktop, 7px phone | 2 sizes x 1 state (candidates, stub engine), light | rendered | 1440x900 .board: check 10 / observed 10 (pixel x=300, ink rows 866-880 = border 5 + shadow 10)
report-check: ok 1,389 chars a93085b3
