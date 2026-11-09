메인 화면의 카드·안내 줄·버튼 사이 간격을 하나의 규칙으로 맞추고, 다시 어긋나면 실패하는 검사 스크립트를 추가했습니다. 바꾸기 전 실제로 보이는 틈은 1~9px로 제각각이었습니다. 지금은 측정한 모든 화면에서 화면 크기별 한 값(12 / 10 / 8px)입니다(spacing 198/198, 12 sizes x 6 states, rendered, spot check 1440x900 review card to bubble: check 12 / observed 12).

- 작업: 간격 규칙을 정했습니다. 세로로 쌓인 덩어리 사이(카드, 안내 줄, 후보 알약 줄, 행동 줄, 발밑 줄, 세로 배치의 판 → 첫 말풍선)와 행동 줄 버튼 사이의 보이는 틈을 `--stack` 하나로 둡니다. 값은 기본 12px, 폭 700px 이하 10px, 높이 700px 이하 8px입니다. 보이는 틈은 그림자 끝부터 잽니다. 그림자가 있는 덩어리는 `--drop` 변수 하나로 그림자 깊이와 아래 여백을 함께 정하게 해서 둘이 따로 놀지 않게 했습니다. `src/style.css` 끝에 한 덩어리로 추가했고, 판·버튼의 모양과 색은 그대로입니다.
- 업데이트 파일: `src/style.css`, `DESIGN.md`(규칙 11, 간격 토큰, 점검 표), `TASK.md`, `ROADMAP.md`(DS3 추가, 현재·다음 줄), 새 검사 `work/design/spacing-check.mjs`, `work/design/capture-matrix.mjs`(가짜 엔진 옵션), 측정 로그 `work/design/spacing-before.log`·`spacing-after.log`·`matrix-spacing.log`·`system-audit-v1-spacing.log`·`folds-before.txt`·`folds-after.txt`. 커밋하지 않았습니다.
- 이슈: 판 크기가 화면 높이로 정해지는 세로 배치에서는 늘어난 간격만큼 판이 작아집니다(820×1180 판 계산 664px → 측정 647px). 휴대폰 390×844처럼 폭으로 정해지는 화면은 그대로입니다. 그 밖의 바뀐 점: 좁은 행동 줄 버튼 사이 8 → 10px, 휴대폰의 작은 주 버튼·꺼진 주 버튼 그림자 7 → 6px. 엔진 파일이 없는 것은 여전해서 가짜 엔진으로 쟀습니다.
- 해결: 쌓임 간격 불일치. 1440×900 수순 화면의 행동 줄 → 발밑 줄 틈이 검사 1px에서 12px로 바뀌었고, 캡처 픽셀로도 12px를 확인했습니다.
- 남은 문제: 간격 값(12/10/8)과 적용 범위의 사용자 확인(DS3). 재지 못한 상태는 종료·복기·내 수 검토·AI 차례·금수 안내·엔진 경고와 실제 엔진 화면입니다. E2E는 실제 엔진이 필요해 돌리지 못했습니다. 지난 턴의 DES-01(대비)·DES-02(동작 감소)와 v1 승인은 아직 열려 있습니다.
- 다음 작업: 값과 범위가 괜찮은지 알려 주세요. 앞으로 화면을 고칠 때마다 `GOMOKU_DEV_PORT=<포트> node work/design/spacing-check.mjs all`을 돌려 종료 코드 0을 확인합니다(엔진 파일이 없으면 `--stub`을 붙입니다).

design checks:
- spacing S1/S2 before | 85/198 | 12 sizes x 6 states, light | rendered | not spot-checked
- spacing S1/S2 after | 198/198 | 12 sizes x 6 states, light | rendered | 1440x900 candidates review card to bubble: check 12 / observed 12
- fix turn-actions to foot gap | fixed | 12 sizes x 6 states, light | rendered | 1440x900 route turn-actions to foot: check 1 before / 12 after, pixel 12 after
- fix board to first card gap | fixed | 4 phone sizes x 5 states, light | rendered | 390x844 candidates board to bubble: check 9 before / 10 after, pixel 10 after
- fix bubble to pills gap | fixed | 12 sizes x 1 state, light | rendered | 390x844 candidates bubble to pills: check 4 before / 10 after, pixel 10 after
- overflow and clipping | 72/72 frames clean | 12 sizes x 6 states, light | rendered | not spot-checked
- page scroll | 72/72 frames no scroll | 12 sizes x 6 states, light | rendered | not spot-checked
- color, shadow, font, text, control rules | 0 violations | 12 sizes x 6 states, light | rendered | not spot-checked
- hud folding before/after | 72/72 frames identical | 12 sizes x 6 states, light | rendered | not spot-checked

상세 보고:
- 새 검사는 그림자를 포함해 눈에 보이는 가장자리 사이를 잽니다. 기대값과 1px 넘게 다르면 종료 코드 1로 끝납니다. `--spot`은 캡처 픽셀로 남색 가장자리 사이 줄 수를 세어 검사 값 옆에 적고, `--folds`는 말풍선 영역에서 접힌 항목을 보여 줍니다. 안내 글자 줄(`#undo-notice`)처럼 남색 테두리가 없는 덩어리는 픽셀 확인이 안 되고 검사 값만 있습니다.
- 그림자가 이제 아래 여백 안에 그려지므로, 말풍선 영역 아래 안쪽 여백을 10px에서 2px로 줄였습니다. 그래서 늘어난 간격 때문에 접히는 안내는 생기지 않았습니다(접힘 비교 72장 동일).
report-check: ok 3,055 chars d04c0650
