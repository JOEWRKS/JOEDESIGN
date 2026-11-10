- 작업: 설명 카드(추천 말풍선)에 "이유 더 보기" 버튼을 넣었다. 버튼은 카드 오른쪽 위, "추천" 같은 라벨과 같은 줄에 둔다. 설명 문장이 줄 수 제한으로 잘리거나 좁은 화면에서 접혀 안 보일 때만 나타난다. 누르면 설명 전체가 펼쳐지고 버튼 글자가 "이유 접기"로 바뀐다. 다시 누르면 접힌다. 다음 수로 넘어가 설명이 바뀌면 다시 접힌 상태가 된다. 펼친 설명 때문에 말풍선 칸이 넘칠 때만, 펼친 동안 아래 후보 알약 줄(2·3순위)을 잠시 접어 자리를 만든다. 넘치지 않으면 그대로 둔다. 처음엔 버튼을 제목 줄에 두었는데, 휴대폰에서 버튼 높이(44px)만큼 말풍선이 커져 접힌 상태에서도 화면이 넘쳤다. 그래서 비어 있는 라벨 줄 오른쪽으로 옮겨 높이가 늘지 않게 했다. 간격 검사에 "펼친 상태"를 추가해 같이 재게 했다.
- 업데이트 파일: src/main.ts, src/style.css, work/design/spacing-check.mjs, DESIGN.md("이유 더 보기" 절, Display before/after, Rule Coverage 행), TASK.md(2026-11-10 설명 카드 '이유 더 보기' 버튼), ROADMAP.md(현재·다음 줄), 캡처 work/design/shots/reason-390x844-closed-open.png.
- 이슈: 이 버튼은 제품 정의(JOEFLOW rev 20)에 없는 새 조작이라 product decision pending으로 남겼다. 지시에 없던 부분은 내가 정했다: 버튼이 보이는 조건, 펼친 뒤 글자 "이유 접기", 설명이 바뀌면 닫힘, 넘칠 때 알약 줄 접기. 알약 줄을 잠시 숨기는 것은 보이는 내용이 바뀌는 일이라 아래 Display before/after에 적었다. 넓은 화면(1440x900 등)에서는 설명이 원래 다 보여서 버튼이 나오지 않는다. 엔진 파일이 없어 가짜 엔진의 짧은 설명으로 쟀고, E2E는 돌리지 못했다(ENV-06).
- 해결: 없음(새 기능이며, 측정은 아래 결과 목록에 있다)
- 남은 문제: 이유 더 보기의 product decision pending과 위 담당자 선택 4가지의 사용자 확인. 실제 엔진의 긴 설명과 키보드·화면 읽기 프로그램 조작은 확인 전. ROADMAP 다음 작업 줄의 나머지 열린 항목은 그대로다.
- 다음 작업: 휴대폰에서 버튼을 눌러 보고, 위 네 가지 동작이 괜찮은지 정해 준다. 넓은 화면에서도 버튼을 늘 보이게 할지도 정해 준다.

## Display before/after

- before: 후보 알약 줄(2·3순위) | 후보 좌표와 승률 | 대국 화면 → 내 차례 추천
- after: 후보 알약 줄(2·3순위) | 이유를 펼쳐 말풍선 칸이 넘칠 때만 hidden, 접으면 다시 보임 | 대국 화면 → 내 차례 추천 → 이유 더 보기

내용이 다르므로 product decision pending(이유 더 보기 기능과 같은 JOEFLOW 재진입 대상).

design-check results:
- DS-SP spacing, overflow, touch with reason-open state | 560/560 pairs, 177/177 states clean, 636/636 buttons | 13 sizes x 13-14 states (stub engine), light | rendered | 390x844 closed/open captures: button on the label row, opened sentence shown, chips kept, observed
- before/after placements during the turn | title-row button: overflow 138/177; negative margins: 156/177; label-row overlay: closed 0 overflow, open 173/177; measured chip folding: 177/177 | 13 sizes x 13-14 states | rendered | not spot-checked
- DS-T, DS-BT, DS-PR | 230/230, 391/391, 169/169 | 13 sizes | rendered | not spot-checked this turn
- tsc and unit tests | tsc ok, vitest 87 passed 1 skipped | code | code | not spot-checked
report-check: ok 2,196 chars b2ecffd4
