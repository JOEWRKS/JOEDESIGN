- 작업: 시스템의 동작 줄이기 설정(prefers-reduced-motion: reduce)을 켜면 화면의 움직임이 모두 멈추게 했다. 판 위 착수 예정 고리와 가이드 대체 추천 고리의 회전, 로고 별 반짝임과 돌 떨어짐, 승리 배너 등장, 계산 중 점 튀기기, 스위치·엔진 막대 전환이 대상이다. 멈춘 고리는 같은 자리에 점선 그대로 보인다. 설정을 끈 사람에게는 이전과 똑같이 움직인다. 이 동작은 예전 DESIGN v0.1에 "동작 감소 설정에서 장식 전환을 제거한다"로 적혀 있었지만 구현이 없었다(CSS에 관련 규칙 0건). 확인용 검사 work/design/motion-check.mjs를 만들어 npm run design:check에 motion으로 넣었다.
- 업데이트 파일: src/style.css, DESIGN.md(화면 규칙 10, Rule Coverage DS-MO 행, 실행 방법), TASK.md(2026-11-10 동작 감소 설정 대응), ROADMAP.md(현재 줄), work/design/motion-check.mjs(새 파일), work/design/design-check.mjs, 캡처 work/design/shots/motion-reduce-1440x900-preview-ring.png.
- 이슈: 승리 배너·첫 안내·계산 중 점 상태는 같은 전역 규칙으로 꺼지지만 하나하나 따로 재지는 않았다(시작 화면과 예비 착수 상태만 측정). design:check 전체는 8개 중 6개 통과(2 sizes x up to 13 states, rendered, not spot-checked this turn)로, 실패 2개는 이전부터 열린 금수 ✕(DS-06)와 좌표 글자·첫 안내·수 세기 분홍 대비(DS-05·DS-01)다. 엔진 파일이 없어 가짜 엔진으로 쟀다(ENV-06).
- 해결: 없음(새 대응 추가이며, 측정은 아래 결과 목록에 있다)
- 남은 문제: 동작 감소 화면의 사용자 확인 전. 이전 턴의 열린 항목(design:check 실패 2개의 원인 DS-06·DS-05·DS-01, 그림자 역할 값 확인, DS-07, 다크 모드 product decision pending과 색 확인, 구름, DS-04, CO2, board 빈 파일, 카드 캡션·알림 여백·추천 고리 확인, style.css 추가 분리, --all 실행 시점, 복기 상단 바 product decision pending, 현재 수 세 곳 표시, 그림자 대상 질문, 태블릿·데스크톱 44px, v1·간격 규칙 확인, ENV-05, ENV-06)은 그대로다.
- 다음 작업: 기기의 동작 줄이기를 켜고 화면을 확인해 준다. 계산 중 점처럼 상태를 알리는 움직임은 남기길 원하면 알려 준다(지금은 함께 멈춤).

display unchanged: no element moved, hidden, overlapped or merged; only motion stops when the system asks for reduced motion.

design-check results:
- DS-MO reduced motion | 4/4 | 2 sizes (1440x900, 390x844) x 2 states (setup, preview) x reduce and no-preference control (stub engine) | rendered | 1440x900 reduce preview ring: check 0 running animations and identical captures / observed computed animation none, dashed ring still drawn in capture
- DS-MO control, no-preference | animations running: setup 7, preview 2 (spin); ring captures differ | 2 sizes x 2 states | rendered | not spot-checked
- design:check default | 6/8 PASS; FAIL board-marks (DS-06) and contrast (DS-05, DS-01) | 2 sizes x up to 13 states, light and dark | rendered | not spot-checked this turn
report-check: ok 2,130 chars deab96b7
