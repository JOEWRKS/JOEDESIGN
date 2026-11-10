- 작업: 복기 모드 상단 바를 만들었다. 복기 중에만 판 위(데스크톱 옆 배치에서는 판과 오른쪽 칸 위 전체 폭)에 흰 바 한 줄이 나오고, 왼쪽에 큰 숫자로 현재 수와 "/ 총 N수", 오른쪽에 기존 "◀ 이전 수", "다음 수 ▶", "종료 판으로" 버튼이 있다. 버튼은 새로 만든 것이 아니라 기존 버튼을 같은 id·같은 동작 그대로 옮겼다(복기 시작 시 "다음 수"로 초점, 종료 판으로 누르면 "대국 복기"로 초점 그대로). 바 높이만큼 판 크기 계산에서 빼서 한 화면을 유지했고, 바와 판 사이는 2차 턴 간격 규칙(SP-2)을 따른다. 말풍선 칸 복기 패널의 "복기 중 · n수 색 좌표", "종료된 대국: 결과 · 총 N수" 문구는 지시 범위 밖이라 그대로 두었다. 검사 스크립트에 종료·복기 상태를 넣으려고 가짜 엔진이 흑 9수째 승리로 대국을 끝내게 고쳤다.
- 업데이트 파일: src/main.ts, src/style.css, DESIGN.md(복기 상단 바 절, Display before/after, Rule Coverage DS-RB 행, Open Decisions), ISSUES.md(DS-03 closed), TASK.md(2026-11-10 복기 상단 바), ROADMAP.md(현재/다음 줄, DS1), work/design/spacing-check.mjs, stub-engine.mjs, 캡처 work/design/shots/spacing-*-replay*.png와 replay-before/.
- 이슈: 복기 상태를 처음 검사에 넣자, 바 추가 전 코드에서 이미 작은 휴대폰(489x866, 375x667, 360x640) 복기 화면의 해설 카드 아래쪽이 버튼 줄 밑으로 잘려 있었다(DS-03). 버튼이 바로 빠지며 줄었고, 높이 760 이하 휴대폰 복기 중 말풍선 칸 최소 높이를 160→170px로 올려 없앴다. 그 대가로 그 화면의 판이 조금 작아진다. 현재 수가 대결줄 "복기 n/N수", 새 바, 패널 "복기 중 · n수" 세 곳에 보인다. 엔진 파일이 없어 실제 엔진 대국과 복기 E2E는 못 돌렸다(ENV-06).
- 해결: DS-03 작은 휴대폰 복기 카드 잘림 — 아래 결과 목록의 fix 줄이 fixed(375x667 픽셀 직접 관찰).
- 남은 문제: 복기 상단 바는 제품 정의(JOEFLOW rev 20)에 없는 표시 영역이라 product decision pending(제품 결정 대기) — 지시대로 구현했고 정의 반영은 JOEFLOW 재진입에서 한다. 복기 상단 바의 사용자 시각 확인 전. 현재 수 세 곳 표시 중 무엇을 뺄지 사용자 결정(빼면 숨김 변경). 복기 E2E(tests/e2e/replay.spec.ts)와 두 자리 이상 긴 수의 바 폭은 실제 엔진으로 미확인. 3차 턴 그림자 대상 질문(판 10px인지 내 수 카드인지)은 아직 답이 없어 열려 있다. 1·2차 턴의 열린 항목(v1·간격 규칙 확인, DS-01, ENV-05, ENV-06)도 그대로다.
- 다음 작업: 복기 화면을 보고 바 위치·모양과 현재 수 중복 표시를 정해 준다. 엔진 파일 받기를 허락하면 복기 E2E와 spacing-check를 실제 엔진으로 다시 돌린다.

## Display before/after

- before: 이전 수·다음 수·종료 판으로 버튼 | 같은 라벨·동작 | 대국 화면 → 종료 → 대국 복기 (위치: 말풍선 칸 복기 패널)
- after: 이전 수·다음 수·종료 판으로 버튼 | 같은 라벨·동작 | 대국 화면 → 종료 → 대국 복기 (위치: 판 위 복기 상단 바)
- before: 현재 수 번호·총 수 | 현재 수 번호, 총 수 | 대국 화면 → 종료 → 대국 복기 (위치: 대결줄, 복기 패널)
- after: 현재 수 번호·총 수 | 현재 수 번호, 총 수 | 대국 화면 → 종료 → 대국 복기 (위치: 대결줄, 복기 패널, 복기 상단 바)

두 쌍 모두 표시 내용과 경로가 같아 위치 변경은 디자인 결정이다. 다만 복기 상단 바라는 새 표시 영역 자체는 제품 정의 rev 20에 없으므로, 사용자 지시대로 만들고 제품 기록은 product decision pending(JOEFLOW 재진입 대상)으로 남긴다.

design-check results:
- DS-SP spacing SP-1/SP-2 | 294/294 pairs | 12 sizes x 8 states (setup, tutorial, candidates, preview, undone, finished, replay-start, replay; stub engine), light | rendered | 390x844 candidates bubble to chips: check 10 / observed 10 (pixel, turn 2 capture; not re-observed this turn)
- DS-RB replay bar to board | 24/24 pairs at or above --stack | 12 sizes x 2 states (replay-start, replay), light | rendered | 390x844 replay: check 10 / observed 10 (pixel x=200, bar 111-118 to board 129); 1440x900 replay: check 17 / observed 17 (pixel x=500, 131-138 to 156)
- DS-SP-O overflow | 96/96 states | 12 sizes x 8 states, light | rendered | not spot-checked
- before/after on pre-bar code, same script | 264/270 pairs, overflow 90/96 | 12 sizes x 8 states, light | rendered | 375x667 replay capture: bubble bottom border absent before
- fix DS-03 small-phone replay card clipped | fixed | 375x667 replay, light | rendered | 375x667: bubble bottom border missing before / border+shadow rows 516-524 then button row 540 after, pixel x=30 capture
- tsc and unit tests | tsc ok, vitest 87 passed 1 skipped | code | code | not spot-checked
report-check: ok 3,227 chars 410f9bb4
