- 작업: 도움말 창을 화면의 카드와 같은 모양으로 맞췄다. 창 자체는 추천 말풍선 카드와 같은 값(외곽선 4px·휴대폰 3px, 모서리 26px·20px, 카드 그림자 6px·5px, 안쪽 여백도 말풍선과 같게)으로, 창 안의 크림색 설명 상자 두 개("숫자(%)의 뜻", "엔진 라이선스")는 내 수 평가 카드와 같은 값(모서리 20px·16px, 카드 그림자)으로 바꿨다. 전에는 창이 대화상자용 깊은 그림자(8px)와 다른 모서리(24px)를 썼고, 설명 상자에는 그림자가 없었다. 새 게임 확인 창은 지시 범위 밖이라 대화상자 모양 그대로 두었다. 그림자 역할 검사도 도움말 창을 카드 역할로 세도록 고쳤다. 값은 기존 카드 값을 그대로 썼지만 화면 확인은 아직이다.
- 업데이트 파일: src/style.css, work/design/shadow-check.mjs, DESIGN.md(그림자 역할 두 행, 도움말 창 행), TASK.md(2026-11-10 도움말 창을 카드 스타일로), ROADMAP.md(DS1 확인 목록, 현재 줄), 비교 캡처 work/design/shots/help-390x844-before-after.png와 help-before/.
- 이슈: 안쪽 여백이 바뀌어 줄바꿈 위치가 조금 달라졌지만(예: 휴대폰 1번 항목), 12크기 모두 도움말 창이 한 화면에 들어간다(아래 목록). 대비 검사 실패는 이전부터 열린 판 좌표 글자·첫 안내·수 세기 분홍(DS-05·DS-01)뿐이다. 엔진 파일이 없어 가짜 엔진으로 쟀다(ENV-06).
- 해결: 없음(사용자 지시 변경이며, 측정은 아래 결과 목록에 있다)
- 남은 문제: 도움말 창 카드 스타일의 사용자 확인 전. 새 게임 확인 창도 카드 모양으로 맞출지 미정. 이전 턴의 열린 항목(390x844 E2E 기본 실행 밖, 범위 밖 간격 값 확인, 예전 승인 기록 출처, 스위치 파랑 확인, 검사 없는 규칙 4개와 일부만 재는 3개, 글자 하한 미강제, design:check 실패 2개의 원인 DS-06·DS-05·DS-01, 로고·판 크기 확인, DS-04 줄바꿈, 동작 감소 확인, 그림자 역할 값 확인, DS-07, 다크 모드 product decision pending과 색 확인, 구름, CO2, board 빈 파일, 카드 캡션·추천 고리 확인, style.css 추가 분리, --all 실행 시점, 복기 상단 바 product decision pending, 현재 수 세 곳 표시, 그림자 대상 질문, 태블릿·데스크톱 44px, v1 확인, ENV-05, ENV-06)은 그대로다.
- 다음 작업: 도움말 창을 열어 보고 괜찮은지 알려 준다. 새 게임 확인 창도 같은 카드 모양으로 맞출지 정해 준다.

display unchanged: no element moved, hidden, overlapped or merged; the help dialog and its note boxes changed border radius, padding and shadow only.

design-check results:
- DS-SH shadow roles with help dialog as card | 60/60 role groups uniform (help-dialog and notes 6 desktop, 5 phone) | 12 sizes x 8 states (stub engine), light | rendered | 390x844 help: note border+shadow rows 567-576 (about 3 + 5), dialog rows 742-750 (about 3 + 5), capture pixels with partial edge rows
- DS-SP-O overflow including help | 156/156 states clean | 12 sizes x 13 states, light | rendered | 390x844 help before/after captures: whole dialog inside the screen, observed
- DS-T and DS-O | DS-T 213/213, DS-O 24/24 (intro and help) | 12 sizes x 2 states, light | rendered | not spot-checked this turn
- DS-SP spacing and DS-TOUCH | 500/500 pairs, touch 440/440 | 12 sizes x 13 states, light | rendered | not spot-checked this turn
- DS-CR contrast | FAIL, only the known DS-05 and DS-01 items | 12 sizes x 7 states x light and dark | rendered | not spot-checked this turn
report-check: ok 2,403 chars a0852507
