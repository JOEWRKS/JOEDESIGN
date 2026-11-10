- 작업: 시스템 설정(prefers-color-scheme)을 따르는 다크 모드를 넣었다. 다크 규칙은 src/tokens.css의 색 토큰 값 바꾸기 한 곳뿐이고, 화면별 다크 규칙은 없다. 다만 그대로 토큰만 바꾸면 안 되는 곳이 있어서 먼저 준비 작업을 했다. 지금까지 --ink 하나가 글자와 외곽선·그림자를 같이 맡고 있어서, 다크에서 글자를 밝히면 외곽선도 밝아지고 노랑 버튼 위 글자는 안 보이게 된다. 그래서 역할을 나눴다: 글자 --ink, 외곽선·입체 그림자 --line, 판 안 돌·표식 외곽선 --board-line, 노랑·연두·하늘·분홍 채움과 판 위 글자 --on-fill. 판 밖에 박혀 있던 원시 색 13종도 역할 토큰으로 바꿨다. 이 준비 단계는 라이트 화면을 하나도 바꾸지 않는다(계산 스타일 비교로 확인). 다크 값은 밤하늘 바탕, 짙은 남보라 카드, 밝은 글자다. 짙은 외곽선은 밤하늘에서 거의 안 보여(1.3:1) 외곽선과 입체 그림자를 밝은 라벤더로 바꿨다. 판, 추천 고리, 노랑·연두 버튼은 두 모드에서 같다. 다크 색 값은 지시에 없어 내가 골랐다. 라이트·다크 대비를 실제 화면에서 재는 검사 work/design/contrast-check.mjs를 새로 만들었다.
- 업데이트 파일: src/tokens.css, src/style.css, DESIGN.md(다크 모드 절, Rule Coverage DS-CR 행), ISSUES.md(DS-05 open), TASK.md(2026-11-10 다크 모드), ROADMAP.md(현재 줄 DS-05·DS1 확인 대상), work/design/contrast-check.mjs(새 파일), 캡처 work/design/shots/contrast-light-*.png, contrast-dark-*.png.
- 이슈: (1) 다크 모드는 제품 정의(JOEFLOW rev 20)에 없는 기능이다. 예전 v0.1 기록도 테마 전환을 범위 밖으로 적었다. 그래서 product decision pending으로 남겼다. (2) 다크에서 새로 생긴 대비 미달은 결과 배너 1건이었고(밝은 외곽선 때문에 1.42:1) 판 외곽선 토큰으로 바꿔 없앴다. (3) 새 대비 검사로 두 모드 공통의 기존 문제를 찾았다(DS-05): 판 좌표 글자 3.11:1, 첫 안내 "1 / 3" 표시 1.99:1. 라이트의 수 세기 분홍 글자(DS-01)도 같은 검사에서 다시 잡혔다. (4) 하늘의 흰 반투명 구름이 밤하늘에서는 회색 원처럼 보인다. 지울지 바꿀지는 사용자가 볼 부분이다. (5) 계산 스타일 비교 첫 실행에서 예비 착수 화면 7건이 계산 타이밍 때문에 달랐고 다시 돌리니 같았다. 엔진 파일이 없어 가짜 엔진으로 쟀다(ENV-06).
- 해결: 없음(새 기능 추가이며, 측정은 아래 결과 목록에 있다)
- 남은 문제: 다크 모드 product decision pending과 다크 색의 사용자 시각 확인 전. DS-05 open(좌표 글자·첫 안내 단계 대비). 구름 처리. 다크에서 알림 상태와 판 위 표식 글자는 대비 검사 밖. 이전 턴의 열린 항목(DS-04, DS-01, CO2, board 빈 파일, 카드 캡션·알림 여백·추천 고리 확인, style.css 추가 분리, --all 실행 시점, 복기 상단 바 product decision pending, 현재 수 세 곳 표시, 그림자 대상 질문, 태블릿·데스크톱 44px, v1·간격 규칙 확인, ENV-05, ENV-06)은 그대로다.
- 다음 작업: 시스템을 다크로 두고 화면을 보거나 work/design/shots/contrast-dark-*.png를 보고 색과 구름을 판단해 준다. DS-05 좌표 글자·첫 안내 색을 바꿀지도 정해 준다.

display unchanged: no element moved, hidden, overlapped or merged; light computed styles identical, dark mode changes colors only.

design-check results:
- DS-EQ light computed styles before/after | 2249/2249 identical | 4 sizes x 5 states, light | rendered | not spot-checked
- DS-CR contrast, light and dark | 4/28 states clean; failures: board coordinate labels 3.11:1 and tut-step 1.99:1 in both modes, move-count 2.65:1 in light; no dark-only failure | 2 sizes x 7 states x 2 schemes (stub engine) | rendered | dark 1440x900 card text: check pass / observed pixel ratio 10.19:1 (rgb(221,215,245) on rgb(43,37,80))
- fix dark result banner outline | fixed | 2 sizes x finished state, dark | rendered | 1440x900 dark finished: lavender outline 1.42:1 before (check) / navy outline pixels rgb(42,32,71) at x=420 rows 357-361, 382-389 after, capture
- DS-SP spacing | 83/83 pairs, overflow 26/26, touch 88/88 | 2 sizes x 13 states, light | rendered | not spot-checked this turn
- DS-RING | 2/2 | 2 sizes x 1 state, light | rendered | not spot-checked this turn
- tsc | passed | code | code | not spot-checked
report-check: ok 2,953 chars 8cfd56dd
