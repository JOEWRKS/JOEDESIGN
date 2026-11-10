- 작업: 디자인 검사를 한 명령으로 묶었다. npm run design:check 하나가 빌드하고, preview 서버를 띄우고, 검사 7개(토큰·간격·그림자·추천 고리·판 위 표식·렌더 대비·코드 대비)를 차례로 돌린 뒤 요약 표를 찍고, 하나라도 실패하면 종료 코드 1로 끝난다. 끝나면 서버도 내린다. 옵션: -- --all(12크기), -- --sizes 768x1024처럼 크기 지정, -- --only spacing,shadow처럼 일부만, CSS 정리 전후 비교용 -- --save-baseline / -- --baseline. 각 검사의 전체 출력은 .cache/design-check/에 남는다. 개별 스크립트 파일은 지우지 않고 이 명령이 불러 쓰는 부품으로 남겼다(따로 돌릴 수도 있다). 묶으면서 두 가지를 고쳤다: 토큰 검사의 기대값이 그림자 통일 전 값이라 실패하던 것을 지금 값으로 맞췄고, 계산 스타일 비교가 애니메이션·계산 타이밍 때문에 가끔 달라지던 것을 고정했다.
- 업데이트 파일: package.json(design:check), work/design/design-check.mjs(새 파일), work/design/ds-v1-check.mjs, work/design/css-equivalence.mjs, README.md(한 줄), DESIGN.md(Rule Coverage 실행 방법), TASK.md(2026-11-10 디자인 검사 한 명령), ROADMAP.md(현재 줄, DS1 완료 기준에 명령 추가).
- 이슈: 지금 돌리면 7개 중 5개 통과, 2개 실패다(2 sizes x 1~13 states, rendered, not spot-checked — 줄별 결과는 아래 목록). 실패는 새 문제가 아니라 이미 열려 있는 문제가 그대로 잡힌 것이다: 판 위 표식 검사는 금수 ✕ 대비(DS-06), 렌더 대비 검사는 판 좌표 글자·첫 안내 단계(DS-05)와 라이트 수 세기 분홍(DS-01). 그래서 이 문제들이 고쳐지기 전까지 명령은 계속 실패로 끝난다. 코드 대비 검사(색 쌍 계산)는 참고용이라 실패해도 종료 코드에 넣지 않았다. 엔진 파일이 없어 대국 상태는 가짜 엔진으로 잰다(ENV-06).
- 해결: 없음
- 남은 문제: design:check 실패 2개(DS-06, DS-05·DS-01 고치기 전까지). 이전 턴의 열린 항목(그림자 역할 값 확인, DS-07, 다크 모드 product decision pending과 색 확인, 구름, DS-04, CO2, board 빈 파일, 카드 캡션·알림 여백·추천 고리 확인, style.css 추가 분리, --all 실행 시점, 복기 상단 바 product decision pending, 현재 수 세 곳 표시, 그림자 대상 질문, 태블릿·데스크톱 44px, v1·간격 규칙 확인, ENV-05, ENV-06)은 그대로다.
- 다음 작업: 실패 2개의 원인인 금수 ✕와 좌표 글자·첫 안내 색을 고칠지 정해 준다. 고친 뒤 design:check를 다시 돌리고 캡처로 직접 확인한다.

design-check results:
- design:check tokens | PASS, DS-T 36/36, DS-H 0 below, DS-O 4/4 | 2 sizes x intro (DS-O also help), light | rendered | not spot-checked this turn
- design:check spacing | PASS, 83/83 pairs, overflow 26/26, touch 88/88 | 2 sizes x 13 states (stub engine), light | rendered | not spot-checked this turn
- design:check shadow | PASS, 10/10 role groups | 2 sizes x 8 states, light | rendered | not spot-checked this turn
- design:check ring | PASS, 2/2 | 2 sizes x 1 state, light | rendered | not spot-checked this turn
- design:check board-marks | FAIL, 4/8 (forbidden mark, DS-06) | 2 sizes x 1 state x light and dark | rendered | not spot-checked this turn
- design:check contrast | FAIL, known DS-05 and DS-01 items only | 2 sizes x 7 states x light and dark | rendered | not spot-checked this turn
- design:check contrast-code | info, 14/15 pairs | 15 token pairs | code | not spot-checked
- design:check css-equivalence twice against a saved baseline | 2249/2249 identical both runs | 4 sizes x 5 states, light | rendered | not spot-checked
report-check: ok 2,575 chars cb4ec702
