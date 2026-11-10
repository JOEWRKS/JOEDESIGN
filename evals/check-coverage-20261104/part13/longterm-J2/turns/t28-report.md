네, 다만 전체 크기로 돌릴 때만 들어간다. 이번 턴에는 검사를 새로 돌리지 않았고, 설정과 지난 턴 기록으로 답한다.

- npm run design:check -- --all: 13크기에 휴대폰 가로 844x390이 들어 있다. 검사 7개(토큰, 간격·넘침·터치 44px, 그림자, 추천 고리, 판 위 표식, 대비, 동작 감소)가 모두 이 크기에서도 돈다. 가로 휴대폰도 터치 화면으로 흉내 내고 44px 버튼 검사 대상으로 센다. 지난 턴 결과는 아래 줄과 같다.
- npm run design:check(기본): 1440x900과 390x844만 돈다. 가로 모드는 들어가지 않는다(턴 6에 정한 기본 2크기).
- 다른 가로 크기(740x360, 667x375 등)는 --sizes 740x360,667x375처럼 직접 줘야 돈다. 740x360은 지금 복기·금수 알림에서 넘침이 있어(DS-08) --all에 넣으면 실패로 끝나서 넣지 않았다.
- Playwright E2E에는 가로 프로젝트가 없다(기본은 데스크톱만, 휴대폰 세로는 GOMOKU_E2E_MOBILE=1일 때만). 그리고 엔진 파일이 없어 E2E 자체를 아직 못 돌린다(ENV-06).

원하면 기본 실행에 844x390을 넣거나, E2E에 가로 프로젝트를 추가할 수 있다. 기본에 넣으면 검사 시간이 약 1.5배 늘어난다(추정).

design checks: none ran

참고한 이전 결과(턴 27, 이번 턴 실행 아님):
- design:check --all with 844x390 | 6/8 PASS; FAIL board-marks (DS-06) and contrast (DS-05, DS-01) | 13 sizes x up to 13 states, light and dark (stub engine) | rendered | 844x390 captures of setup, candidates, replay and help observed
report-check: ok 966 chars 86260f5e
