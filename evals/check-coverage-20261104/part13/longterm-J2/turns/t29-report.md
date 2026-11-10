- 작업: 말풍선 안의 11px 글자를 12px로 올렸다. 말풍선은 추천·해설 말풍선과, CSS에서 "작은 말풍선"이라 부르는 내 수 평가 카드 두 가지로 보았다. 11px였던 규칙은 세 곳이다: 말풍선 칸이 좁을 때의 보조 줄("상대 예상 E1 · 번호는 이어질 수순 4수" 같은 줄), 자세히 보기 때의 같은 줄, 내 수 평가 카드의 기준 줄. 세 곳 모두 12px로 바꿨다. 실제 화면에서 11px로 그려지던 것은 7개 세로 크기(360x640~820x1180)의 예비 착수 화면 보조 줄이었다. 다시 안 어긋나게 말풍선 글자 크기를 재는 검사를 npm run design:check에 bubble-text로 넣었다.
- 업데이트 파일: src/style.css, work/design/bubble-text-check.mjs(새 파일), work/design/design-check.mjs, DESIGN.md(글자 크기 줄, Rule Coverage DS-BT 행), TASK.md(2026-11-10 말풍선 글자 12px 이상), ROADMAP.md(현재 줄), 비교 캡처 work/design/shots/bubble-text-390x844-before-after.png.
- 이슈: 말풍선 밖에는 아직 12px 미만 글자가 있다: 휴대폰 화면 아래 고지문 "엔진 추정 승률 · 실제 승률 아님" 11px, 휴대폰 도움말의 라이선스 설명 11.5px. 지시가 말풍선이라 그대로 두었다. 판 위 표식 숫자는 칸 크기에 따라 8~13px로 줄어드는데 이것도 범위 밖이다. 엔진 파일이 없어 가짜 엔진으로 쟀다(ENV-06).
- 해결: 없음(사용자 지시 변경이며, 전후 측정은 아래 결과 목록에 있다)
- 남은 문제: 12px 값의 사용자 확인 전. 말풍선 밖 11·11.5px 글자를 같이 올릴지 미정. 이전 턴의 열린 항목(휴대폰 가로 확인, DS-08, 도움말 카드·새 게임 확인 창, 390x844 E2E 기본 실행 밖, 범위 밖 간격 값 확인, 예전 승인 기록 출처, 스위치 파랑 확인, 검사 없는 규칙 4개와 일부만 재는 3개, 글자 하한 미강제(말풍선 밖), design:check 실패 2개의 원인 DS-06·DS-05·DS-01, 로고·판 크기 확인, DS-04 줄바꿈, 동작 감소 확인, 그림자 역할 값 확인, DS-07, 다크 모드 product decision pending과 색 확인, 구름, CO2, board 빈 파일, 카드 캡션·추천 고리 확인, style.css 추가 분리, --all 실행 시점, 복기 상단 바 product decision pending, 현재 수 세 곳 표시, 그림자 대상 질문, 태블릿·데스크톱 44px, v1 확인, ENV-05, ENV-06)은 그대로다.
- 다음 작업: 말풍선 밖의 휴대폰 고지문(11px)과 도움말 라이선스(11.5px)도 12px로 올릴지 정해 준다.

display unchanged: no element moved, hidden, overlapped or merged; only three font sizes changed.

design-check results:
- DS-BT bubble text >= 12px | 358/358, smallest 12px | 13 sizes x 5 states (stub engine), light | rendered | 390x844 preview sub-line: check 12px / observed larger glyphs in the before/after zoom capture
- before/after DS-BT | 351/358 before (7 x 11px preview sub-line), 358/358 after | 13 sizes x 5 states | rendered | 390x844 preview capture compared side by side
- DS-SP spacing, overflow, touch | 533/533 pairs, 169/169 states clean, 528/528 buttons | 13 sizes x 13 states, light | rendered | not spot-checked this turn
- DS-T and DS-O | 230/230, 26/26 | 13 sizes x intro and help | rendered | not spot-checked this turn
report-check: ok 2,165 chars 8c36724d
