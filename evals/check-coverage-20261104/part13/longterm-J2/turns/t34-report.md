- 작업: 디자인 검사 속도를 줄였다. 바꾸기 전 같은 빌드에서 npm run design:check 기본 실행은 100초였고, 검사 10개가 하나씩 차례로 돌았다(가장 긴 간격 검사 36초). 검사를 빼거나 크기·상태를 줄이지 않고 두 가지만 바꿨다. (1) 검사 10개를 동시에 4개씩 돌린다(결과 표 순서는 그대로, --jobs N이나 --serial로 조절). (2) 가장 오래 걸리는 간격 검사 안에서 화면 크기별로 3개씩 동시에 돈다. 결과 기본 실행은 27초·29초(두 번 재봄), 12+1크기 전체(--all)는 144초다. 이 과정에서 동작 감소 검사가 한 번 흔들려 실패한 것을 봤다. 원인은 늦게 그려지는 계산 결과를 움직임으로 센 것이어서, 화면이 0.5초 잠잠해진 뒤 비교하게 고쳤다.
- 업데이트 파일: work/design/design-check.mjs, work/design/spacing-check.mjs, work/design/motion-check.mjs, README.md, DESIGN.md(Rule Coverage 실행 방법), TASK.md(2026-11-10 디자인 검사 속도), ROADMAP.md(현재 줄).
- 이슈: 동시 실행이라 컴퓨터가 바쁠 때는 시간이 더 걸릴 수 있고, 빌드(약 1초)와 서버 띄우기 시간은 그대로다. 결과는 이전과 같다(2 sizes x up to 13 states, rendered, not spot-checked this turn): 기본 8/10 통과, 실패 2개는 이전부터 열린 금수 ✕·판 좌표 글자·첫 안내·수 세기 대비(DS-06, DS-05·DS-01). 전체 실행의 간격 쌍 수가 직전 533에서 532로 다른데, 1920x1080에서 간이 분석 줄이 실행마다 나타났다 안 나타났다 하는 기존 차이다. 엔진 파일이 없어 가짜 엔진으로 잰다(ENV-06).
- 해결: 없음
- 남은 문제: 동작 감소 검사의 흔들림 수정(결과는 아래 목록의 fix 줄) — 흔들림이 없어졌다고 직접 확인하지는 못했다. 대비 실패 원인 결함(DS-06·DS-05·DS-01)과 ROADMAP 다음 작업 줄의 나머지 열린 항목은 그대로다.
- 다음 작업: 더 줄이려면 여러 검사가 각자 대국을 끝까지 두는 부분(간격·그림자·대비·말풍선 글자)을 한 번만 두고 함께 재도록 합치는 방법이 있다. 원하면 진행한다.

display unchanged: no element moved, hidden, overlapped or merged; only the check tooling changed.

design-check results:
- design:check default timing | 100s before (serial), 27s and 29s after (4 jobs) | 2 sizes, all checks | rendered | not spot-checked
- design:check default results after | 8/10 PASS; FAIL board-marks (DS-06) and contrast (DS-05, DS-01), same as before | 2 sizes x up to 13 states (stub engine) | rendered | not spot-checked this turn
- design:check --all after | 144s; tokens 230/230, spacing 532/532, overflow 169/169, touch 528/528, shadow 65/65, ring 13/13, motion 26/26, bubble-text 358/358, press 169/169 | 13 sizes x up to 13 states | rendered | not spot-checked this turn
- fix motion check flake | changed | 1440x900 reduce preview | rendered | not spot-checked (passed in the following runs only)
report-check: ok 1,992 chars ef68d158
