- 작업: 메인 화면 간격을 먼저 쟀다. 칸 안 gap 값은 같았지만 블록마다 아래 입체 그림자 길이(8·7·5·4·3px)가 달라 그림자가 간격을 먹어서, 눈에 보이는 간격이 버튼 줄→안내 줄 1~2px, 말풍선→알약 4px, 평가 카드→말풍선 7px, 되돌리기 안내→안내 줄 8px로 섞여 있었다. 그래서 규칙을 "상자 간격"이 아니라 "보이는 간격" 기준으로 정했다. SP-1 말풍선 칸·버튼 칸 안 블록 사이 보이는 간격 = --stack(12px, 휴대폰 10px, 높이 700 이하 8px — 기존 HUD 간격 값 그대로). SP-2 판→첫 블록, 말풍선 칸→버튼 칸은 --stack 이상. SP-3 같은 역할 버튼은 상태가 바뀌어도 같은 그림자 단계. 코드는 src/style.css 끝에 블록 하나를 더했다(칸 gap = --stack, 블록마다 그림자 길이만큼 margin-bottom = --drop, 세로 배치 판 아래 --board-drop). 휴대폰에서 7px로 남아 있던 보조·두기·비활성 주 버튼 그림자는 6px로 맞췄다. 재발 방지용 검사 스크립트 work/design/spacing-check.mjs를 추가했다(12크기 × 5상태의 블록 쌍 간격과 넘침을 재고, --expect를 주면 하나라도 어긋날 때 종료 코드 1).
- 업데이트 파일: src/style.css, DESIGN.md(간격 규칙 절, 토큰 표, Rule Coverage DS-SP 행), ISSUES.md(DS-02 closed), TASK.md(2026-11-10 간격 규칙), ROADMAP.md(현재/다음 줄, DS1), 새 파일 work/design/spacing-check.mjs, stub-engine.mjs(검사 전용 가짜 엔진, 제품 빌드에 안 들어감), pixel-runs.mjs, 캡처 work/design/shots/spacing-*.png와 spacing-before/.
- 이슈: 엔진 파일이 여전히 없어(ENV-06) 대국 상태는 가짜 엔진 Worker로 들어가 쟀다. 승률·문구는 가짜라 배치 근거로만 쓴다. 세로 배치에서 판 그림자 자리를 확보하느라 판 폭이 크기에 따라 최대 10px 작아졌다(820x1180 664→654, 375x667 297→290 등). 1440x900 말풍선→알약 스폿은 검사 12px, 픽셀 12.6px로 경계 행 반투명만큼 차이가 난다.
- 해결: DS-02 블록 사이 간격 불일치 — 아래 결과 목록의 fix 줄 두 개가 fixed(390x844, 1440x900 픽셀 직접 관찰).
- 남은 문제: 간격 값(12/10/8)과 "보이는 간격" 기준의 사용자 확인 전. 종료·복기·자세히 보기·금수/엔진 알림 상태 간격은 못 쟀다. 실제 엔진 상태 검사와 E2E는 미실행(ENV-06). 넘침 줄은 not spot-checked. 1차 턴의 열린 결정(조작 높이 하한, 분홍 대비 DS-01, v1 승인)은 그대로다.
- 다음 작업: 화면에서 새 간격을 확인해 값 승인 여부를 알려 준다. 엔진 파일 받기를 허락하면 spacing-check를 실제 엔진으로, 종료·복기 상태까지 넓혀 다시 돌린다.

display unchanged: no element moved, hidden, overlapped or merged; only gaps and the board width in stacked layouts changed.

design-check results:
- DS-SP spacing SP-1/SP-2 | 165/165 pairs | 12 sizes x 5 states (setup, tutorial, candidates, preview, undone; stub engine), light | rendered | 390x844 candidates bubble to chips: check 10 / observed 10 (pixel x=40, 581 to 592); 1440x900 bubble to chips: check 12 / observed 12.6 (edge row 366 is 42% ink)
- DS-SP-O overflow after spacing change | 60/60 states | 12 sizes x 5 states, light | rendered | not spot-checked
- before/after DS-SP-O overflow on HEAD style.css | 60/60 states | 12 sizes x 5 states, light | rendered | not spot-checked
- fix DS-02 button row to guide line | fixed | 390x844 candidates, 1440x900 candidates, light | rendered | 390x844: 2 before / 10 after, pixel x=260 capture; 1440x900: 1 before / 12 after, pixel x=1210 capture
- fix DS-02 bubble to chips | fixed | 390x844 candidates, light | rendered | 390x844: 4 before / 10 after, pixel x=40 capture
- DS-T token roles rerun | 213/213 | 12 sizes x 1 state (intro), light | rendered | not spot-checked this turn
- DS-O one screen rerun | 24/24 | 12 sizes x 2 states (intro, help), light | rendered | not spot-checked this turn
report-check: ok 2,798 chars 7883d41f
