- 작업: 검사 스크립트가 기본으로 1440x900과 390x844 두 크기만 돌게 바꿨다. 크기 목록을 work/design/sizes.mjs 한 곳으로 모으고 spacing-check.mjs, ds-v1-check.mjs, capture-matrix.mjs가 이를 쓰게 했다. 12크기 전체는 지우지 않고 --all 인자(또는 GOMOKU_ALL_SIZES=1)를 줄 때만 돈다. 출력 줄에 어떤 크기로 돌았는지 찍힌다. 같은 빌드에서 시간을 재 보니 spacing-check는 62초→13초, ds-v1-check는 16초→3초로 줄었다. 앱 코드는 바꾸지 않았다.
- 업데이트 파일: work/design/sizes.mjs(새 파일), work/design/spacing-check.mjs, ds-v1-check.mjs, capture-matrix.mjs, DESIGN.md(Rule Coverage 위 검사 크기 설명), TASK.md(2026-11-10 검사 크기 기본값), ROADMAP.md(현재 줄 링크).
- 이슈: 기본 실행에서는 나머지 10크기(1920x1080, 1366x768, 1280x720, 1024x768, 820x1180, 768x1024, 489x866, 430x932, 375x667, 360x640)를 재지 않는다. 오늘 찾은 문제 중 작은 휴대폰 복기 카드 잘림(DS-03), 휴대폰 버튼 36~40px, 1280x720 시작 화면 간격은 모두 이 10크기에서만 드러났다. 그래서 --all을 지우지 않고 남겨 두었다. DESIGN의 "한 화면, 스크롤 없음" 규칙은 모든 지원 크기가 대상이라, 기본 실행만으로는 그 규칙이 2크기에서만 확인된다.
- 해결: 없음
- 남은 문제: 기본 실행의 10크기 unmeasured. 화면을 바꾼 뒤 출시 전이나 하루 한 번처럼 --all을 언제 돌릴지 사용자가 정하면 DESIGN에 적는다. 이전 턴의 열린 항목(복기 상단 바 product decision pending, 현재 수 세 곳 표시, 그림자 대상 질문, 태블릿·데스크톱 44px, v1·간격 규칙 확인, DS-01, ENV-05, ENV-06)은 그대로다.
- 다음 작업: --all을 돌릴 때를 정해 준다(예: 커밋 전, 출시 전). 정하지 않으면 지금처럼 기본은 2크기, 필요할 때 --all.

design-check results:
- DS-SP spacing, default sizes | 62/62 pairs, 13s | 2 sizes (1440x900, 390x844) x 10 states, light | rendered | 390x844 candidates bubble to chips: check 10 / observed 10 (pixel x=40, rows 567-575 to 586)
- DS-SP-O overflow, default sizes | 20/20 states | 2 sizes x 10 states, light | rendered | not spot-checked
- DS-TOUCH, default sizes | 71/71 buttons | 1 phone size (390x844) x 10 states, light | rendered | not spot-checked this turn
- DS-T and DS-O, default sizes | DS-T 36/36, DS-O 4/4, 3s | 2 sizes x intro (DS-O also help), light | rendered | not spot-checked this turn
- DS-SP spacing, --all | 371/371 pairs, overflow 120/120, touch 355/355, 62s | 12 sizes x 10 states, light | rendered | not spot-checked this turn
- DS-T and DS-O, --all | DS-T 213/213, DS-O 24/24, 16s | 12 sizes x intro (DS-O also help), light | rendered | not spot-checked this turn
report-check: ok 2,030 chars ef6f67fb
