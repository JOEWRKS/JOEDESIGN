- 작업: 다른 세션이 한 두 턴의 변경을 작업 트리와 기록으로 대조하고, DESIGN 기준 검사를 다시 돌렸다. 바뀐 것은 두 가지다. (가) 설명 카드(#current-card) 안 보조 글자 .caption을 12px→13px로 올림(엔진 상태·복기 해설 기준·예측 안내 세 줄). (나) 금수 알림·엔진 알림 줄의 안쪽 여백을 6/12px→3/10px로 줄임(값 3·10은 그 세션의 선택, 사용자 확인 전). 그 밖에 DESIGN 글자 크기 줄과 토큰 표, TASK 두 절, ROADMAP 현재 줄 링크, 임시 측정 스크립트와 캡처 두 장이 추가됐다. 커밋은 없다. 코드 수정은 하지 않았다(점검 요청이라 고칠 권한 밖). 대신 검사 쪽을 보강했다: spacing-check에 알림 상태 세 개(금수 알림은 가장 긴 실제 문구를 강제 표시, 엔진 알림은 가짜 엔진을 무응답으로 만들어 실제 재시작·멈춤)를 넣고, 잘린 그림자를 잡도록 고쳤다.
- 업데이트 파일: ISSUES.md(DS-04 open), TASK.md(2026-11-10 다른 세션 작업 점검), ROADMAP.md(현재 줄 DS-04·DS1 확인 대상), DESIGN.md(Rule Coverage DS-SP·DS-SP-O 상태 목록과 스폿), work/design/spacing-check.mjs, work/design/stub-engine.mjs, 캡처 work/design/shots/spacing-*-forbid-notice-forced.png, -engine-alert.png, -engine-stopped.png.
- 이슈: (1) 새 문제 DS-04: 375x667·360x640에서 가장 긴 금수 문구가 두 줄로 꺾여 둘째 줄에 "요" 한 글자만 남고, 그만큼 말풍선 칸이 줄어 말풍선 아래 그림자가 1px 잘린다. 보이는 간격은 기준(8px)을 지킨다. 알림 여백 축소 때문이 아니라 원래 있던 문제로 보이고, 줄인 여백이 오히려 덜 눌리게 했다(이전 여백 상태는 재지 않음). (2) 다른 세션의 측정 한계: 알림 높이 39→33px은 짧은 가짜 문구로 시작 화면에서 잰 값이었다. (3) 기록 차이: 알림 여백 3·10이 "사용자 확인 전"인데 ROADMAP DS1 확인 목록에 없어서 추가했다. 그 세션 TASK의 "#replay-result(복기 바)"는 실제로 말풍선 칸 복기 패널 안에 있다(판단에는 영향 없음). (4) 내 검사 도구 결함 두 개를 찾아 고쳤다: 잘린 그림자를 보이는 것으로 계산하던 문제(스폿 체크 check 7 / observed 8), 2차 턴 패치 때 깨진 줄 수 제한 판별 정규식. (5) 저장소 루트에 빈 파일 board가 있다. 턴 4에 내 셸 명령 실수로 생긴 것인데, 삭제 명령이 권한 거부되어 남겨 두었다.
- 해결: 없음
- 남은 문제: DS-04 open(고칠 방식 결정 필요). 카드 캡션 13px·알림 여백 3/10의 사용자 확인 전. 실제 금수 자리 상태와 실제 엔진 문구는 엔진 파일이 없어 미측정(ENV-06). 빈 파일 board 삭제 필요. 이전 턴의 열린 항목(CO2, 추천 고리 색 확인, --all 실행 시점, 복기 상단 바 product decision pending, 현재 수 세 곳 표시, 그림자 대상 질문, 태블릿·데스크톱 44px, v1·간격 규칙 확인, DS-01, ENV-05)은 그대로다.
- 다음 작업: DS-04를 고칠지와 방식(알림 문구 단어 단위 줄바꿈, 알림이 뜰 때 말풍선 칸 높이 반영 등)을 정해 준다. board 파일은 직접 지우거나 삭제를 허락해 준다.

display unchanged: no element moved, hidden, overlapped or merged this turn; no app code changed.

design-check results:
- DS-SP spacing | 500/500 pairs | 12 sizes x 13 states (adds forbid-notice-forced, engine-alert, engine-stopped; stub engine), light | rendered | 375x667 bubble to forbid notice: check 8 / observed 8 (pixel x=30, 463 to 472) after the clip fix
- DS-SP-O overflow | 154/156 states, shadow-clip at 375x667 and 360x640 forbid-notice-forced | 12 sizes x 13 states, light | rendered | 375x667 bubble shadow: check shadow-clip / observed 8 rows instead of 9 (pixel x=30, 456-463)
- fix spacing-check clipped-shadow edge | fixed | 375x667 forbid-notice-forced, light | rendered | 375x667: check 7 before / 8 after, observed 8 in capture pixels
- DS-TOUCH | 440/440 buttons | 5 phone sizes x 13 states, light | rendered | not spot-checked this turn
- DS-RING | 12/12 | 12 sizes x 1 state, light | rendered | not spot-checked this turn
- DS-T, DS-O, DS-H, DS-F | DS-T 213/213, DS-O 24/24, DS-H 0 below, DS-F min 13px | 12 sizes x intro (DS-O also help), light | rendered | not spot-checked this turn
report-check: ok 2,874 chars 15c0b699
