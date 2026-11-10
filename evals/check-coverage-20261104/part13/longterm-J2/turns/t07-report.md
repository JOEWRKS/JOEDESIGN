- 작업: 판 위 1순위 추천 고리(점선 테두리)를 더 진한 초록 #17692a로 바꿨다. 기존 #2f9c3a는 판 나무색과 대비가 2.1~2.6:1로, 그림 요소가 구분되려면 필요한 3:1보다 낮았다. 새 색은 4.0~5.0:1이다. 새 색은 --rec-ring 토큰으로 두고 추천 고리에만 썼다. 같은 초록(--lime-dark)을 쓰는 버튼 안쪽 그림자, 엔진 막대, 승률 글자는 바꾸지 않았다. 고리 안의 연두 채움과 숫자도 그대로다. 정확한 색 값은 지시에 없어 내가 골랐다. 재발 방지로 고리 색과 판 대비를 재는 work/design/ring-check.mjs를 추가했다(--expect면 3:1 미만일 때 종료 코드 1).
- 업데이트 파일: src/style.css, DESIGN.md(토큰 표 추천 고리 행, Rule Coverage DS-RING 행), TASK.md(2026-11-10 추천 고리 진한 초록), ROADMAP.md(현재/다음 줄), work/design/ring-check.mjs(새 파일), 캡처 work/design/shots/ring-*.png, ring-before/, 확대 비교 ring-1440x900-before-after.png, ring-390x844-before-after.png.
- 이슈: 진한 초록이 다른 후보의 남색 점선과 작은 휴대폰 판에서 헷갈릴 수 있는지는 사람 눈으로 확인하지 않았다(가짜 엔진 화면에는 그런 후보가 붙어 있지 않았다). 필승 고리(노랑)와 가이드 대체 표시는 이번 범위 밖이다. 엔진 파일이 없어 가짜 엔진으로 쟀다(ENV-06).
- 해결: 없음(사용자 지시 색 변경이며, 전후 측정은 아래 결과 목록에 있다)
- 남은 문제: 새 고리 색의 사용자 화면 확인 전(값 #17692a는 담당자 선택). 이전 턴의 열린 항목(--all 실행 시점, 복기 상단 바 product decision pending, 현재 수 세 곳 표시, 그림자 대상 질문, 태블릿·데스크톱 44px, v1·간격 규칙 확인, DS-01, ENV-05, ENV-06)은 그대로다.
- 다음 작업: 확대 비교 캡처나 실제 화면에서 색을 확인해 준다. 더 진하게 또는 덜 진하게를 원하면 값만 바꾸고 ring-check로 다시 잰다.

display unchanged: no element moved, hidden, overlapped or merged; only the recommendation ring border color changed.

design-check results:
- DS-RING ring vs board contrast | 12/12 at 3.99-5.03:1 | 12 sizes x 1 state (candidates; stub engine), light | rendered | 1440x900 candidates: check rgb(23,105,42) / observed rgb(23,105,42) in capture pixels, zoom crop before/after
- before/after DS-RING | 0/12 before (2.07-2.62:1), 12/12 after | 12 sizes x 1 state, light | rendered | 1440x900 zoom crop: ring rgb(47,156,58) before / rgb(23,105,42) after, capture pixels
- DS-SP spacing | 62/62 pairs | 2 sizes (1440x900, 390x844) x 10 states, light | rendered | not spot-checked this turn
- DS-SP-O overflow | 20/20 states | 2 sizes x 10 states, light | rendered | not spot-checked
- DS-TOUCH | 71/71 buttons | 1 phone size (390x844) x 10 states, light | rendered | not spot-checked this turn
report-check: ok 2,002 chars 2595baae
