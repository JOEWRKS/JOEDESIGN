- 작업: 지난 턴 표에서 확인되지 않았던 것 중 위험한 3개를 골라 지금 실제 화면에서 확인했다. 고른 것은 규칙 5 판 위 표식, 규칙 6 색만으로 구별하지 않기, 규칙 2 위계다. 판 위 표식은 사용자가 직접 정한 표현이고 틀리면 판을 잘못 읽게 만든다. 색만으로 구별하지 않기는 접근성 문제다. 위계는 사용자 시각 원칙이다. 실제 엔진 확인이 더 위험하지만 엔진 파일 받기 허락이 필요해 지금은 못 한다. 규칙 3(핵심 정보만)은 기계로 잴 기준이 없어 뺐다. 세 규칙을 재는 검사 work/design/rules-check.mjs를 만들어 npm run design:check에 rules로 넣었다. 13크기에서 두 상태(H8을 실제 3-3 금수로 만든 추천 화면, 예비 착수 화면)로 돌렸고, 세 규칙 모두 위반을 찾지 못했다(아래 목록). 390x844 캡처도 직접 봤다. 상대 예상 수순 1·3은 반투명 흰 돌, 내 수순 2·4는 점선, 착수 예정 자리는 노란 점선, H8은 분홍 점선 ✕, 실제 돌은 불투명이었다. 표식마다 숫자·✕·번호가 함께 있었다.
- 업데이트 파일: work/design/rules-check.mjs(새 파일), work/design/design-check.mjs, DESIGN.md(Rule Coverage DS-R5·DS-R6·DS-R2 행), TASK.md(2026-11-10 미확인 규칙 중 위험한 3개 확인), ROADMAP.md(현재 줄), 캡처 work/design/shots/rules-390x844-marks.png.
- 이슈: 위계는 "판이 가장 크고, 판 밖에서 가장 큰 글자가 좌표·승률이고, 가장 큰 버튼이 주 버튼"이라는 크기 순서만 잰 대리 측정이다. 밝기·색으로 정해지는 위계와 사람의 전체 판단을 대신하지 못한다. 숫자 없는 작은 후보 고리는 모양(점선 고리)으로 구별되므로 규칙 6 검사에서 뺐다. 엔진 파일이 없어 가짜 엔진의 짧은 수순으로 쟀다(ENV-06). 필승 고리, 복기 중 표식, 실제 엔진 수순은 확인하지 못했다.
- 해결: 없음(확인 작업이며 고친 것은 없다)
- 남은 문제: 규칙 3 미확인. 위계의 사람 판단. 지난 턴의 "출시를 막는 것" 중 실패 검사 3개(DS-06, DS-05·DS-01·DS-09, TEST-10), 실제 엔진·E2E·실기기 0, 사용자 승인은 그대로다.
- 다음 작업: 엔진 파일 받기를 허락해 주면 다음으로 위험한 실제 엔진 화면 확인을 시작한다. 그 전에는 실패 중인 대비 결함(DS-06·DS-05·DS-01·DS-09)부터 고칠 수 있다.


design-check results:
- DS-R5 board marks | 286/286 | 13 sizes x 2 states (recommend with a 3-3 point, preview; stub engine), light | rendered | 390x844 capture: foe route 1,3 translucent stones, own route 2,4 dashed, preview ring dashed, H8 dashed ✕, real stones opaque, observed
- DS-R6 not color alone | 208/208 | 13 sizes x 2 states, light | rendered | 390x844 capture: every mark carries a number, ✕ or route number, observed
- DS-R2 hierarchy proxy | 39/39 | 13 sizes x 1 state (recommend), light | rendered | 390x844 recommend capture from turn 35: board, then coordinate and 62%, then yellow button, observed
report-check: ok 1,886 chars 6507c19e
