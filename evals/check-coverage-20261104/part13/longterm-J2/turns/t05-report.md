- 작업: 휴대폰(폭 700 이하)에서 판 밖 모든 버튼을 높이·폭 44px 이상으로 맞췄다. 먼저 쟀더니 휴대폰 5크기 × 10상태에서 보이는 버튼 355개 중 110개만 44px 이상이었다. 작았던 것은 상단 아이콘 42×42, 승률 가이드 스위치 38, 첫 안내 버튼 36, 후보 알약 36~40, 복기·새 게임 확인·도움말 버튼 38, 시작 화면 고르기 40, 예비 착수 중 되돌리기 폭 38이다. src/style.css 끝에 휴대폰 블록 하나를 더해, 여러 곳(작은 높이·말풍선 칸 접기·첫 안내·도움말)에서 높이를 줄이던 규칙을 한 번에 덮어썼다. 늘어난 높이만큼 버튼 칸과 복기 바 높이 계산값도 올려 한 화면을 유지했다. 판 교차점은 대상에서 뺐다(촘촘한 판 칸까지 44px는 아님). 재발 방지로 spacing-check.mjs에 버튼 크기 검사를 넣었고(--expect면 44px 미만이 하나라도 있을 때 종료 코드 1), 새 게임 확인 창과 도움말 상태도 검사 범위에 넣었다. DESIGN.md 규칙 9를 사용자 지시로 바꿨다.
- 업데이트 파일: src/style.css, DESIGN.md(토큰 표 조작 높이, 규칙 9, Rule Coverage DS-TOUCH 행, Open Decisions), TASK.md(2026-11-10 휴대폰 버튼 44px), ROADMAP.md(현재/다음 줄, DS1), work/design/spacing-check.mjs, work/design/ds-v1-check.mjs(휴대폰 기준 44), 캡처 work/design/shots/spacing-*.png와 touch-before/.
- 이슈: 버튼이 커진 만큼 휴대폰 세로 화면의 판이 조금 작아졌다(489x866 439→433px, 375x667 290→284px, 360x640 263→257px). 내용이 접히거나 숨겨진 블록은 없었다(변경 전후 휴대폰 상태의 블록 목록 동일, 캡처 비교). 1920x1080에서 간이 분석 줄이 변경 전 실행에만 나타나 간격 쌍 수가 374에서 371로 달라졌는데, 데스크톱이라 이번 휴대폰 규칙과 무관한 실행 차이다. 엔진 파일이 없어 가짜 엔진으로 쟀다(ENV-06).
- 해결: 없음(결함 수정이 아니라 사용자 지시 변경이며, 전후 측정은 아래 결과 목록에 있다)
- 남은 문제: 휴대폰 44px 버튼의 사용자 화면 확인 전. 폭 700 초과 태블릿·데스크톱(pill 42px 등)을 44로 맞출지는 미정. 실제 엔진 상태와 E2E 미실행(ENV-06). 4차 턴 복기 상단 바 product decision pending과 현재 수 세 곳 표시, 3차 턴 그림자 대상 질문, v1·간격 규칙 확인, DS-01, ENV-05도 그대로 열려 있다.
- 다음 작업: 휴대폰에서 버튼 크기와 작아진 판을 확인해 준다. 태블릿·데스크톱도 44px로 맞출지 알려 주면 같은 검사에 기준을 넓혀 적용한다.

display unchanged: no element moved, hidden, overlapped or merged; button heights and widths grew and the board shrank on phones.

design-check results:
- DS-TOUCH phone buttons >= 44px | 355/355 | 5 phone sizes x 10 states (setup, tutorial, candidates, preview, reset-confirm, undone, finished, replay-start, replay, help; stub engine), light | rendered | 375x667 chip: check 44 / observed 44 (pixel x=40, rows 473-516); 375x667 guide toggle: check 44 / observed 44 (pixel x=295, rows 608-651)
- before/after DS-TOUCH | 110/355 before, 355/355 after | 5 phone sizes x 10 states, light | rendered | 375x667 chip: 36 before / 44 after; toggle: 38 before / 44 after (pixel captures)
- DS-SP spacing | 371/371 pairs | 12 sizes x 10 states, light | rendered | not spot-checked this turn
- DS-SP-O overflow | 120/120 states | 12 sizes x 10 states, light | rendered | not spot-checked
- DS-T token roles | 213/213 | 12 sizes x 1 state (intro), light | rendered | not spot-checked this turn
- DS-H control floor (phone 44) | 0 below floor | 12 sizes x 1 state (intro), light | rendered | not spot-checked this turn
- DS-O one screen | 24/24 | 12 sizes x 2 states (intro, help), light | rendered | not spot-checked this turn
report-check: ok 2,648 chars 65c237c5
