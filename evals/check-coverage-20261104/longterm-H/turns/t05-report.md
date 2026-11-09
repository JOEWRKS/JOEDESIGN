휴대폰 화면(폭 700px 이하)에서 판 밖의 모든 버튼을 높이 44px 이상으로 키웠습니다. 보조 버튼도 포함했고, 검사에서 미달은 0건입니다(control 660/660, 12 sizes x 7 states, rendered, spot check 390x844 #tut-skip: check 44 + 4 / observed 48). 대신 화면 높이가 좁은 휴대폰에서는 판이 10px 작아졌습니다.

- 작업: 바꾸기 전 44px 기준으로 재 보니 660개 중 170개가 미달이었습니다(control 490/660, 12 sizes x 7 states, rendered, not spot-checked). 미달은 도움말·새 게임 아이콘 42, 승률 가이드 스위치 38, 첫 안내 건너뛰기·다음 36, 후보 알약 36~40, 도움말 닫기·다시 보기 38, 새 게임 확인 버튼 38, 돌·강도 선택 40px이었고, 코드상 복기 바 버튼도 34px였습니다. 모두 44px로 올렸습니다. 복기 바가 44px 버튼을 담을 수 있게 휴대폰 상단 줄을 58 → 62px로 높였습니다. 판의 교차점은 "버튼"에서 제외했습니다(고른 뒤 확정하는 절차로 보완).
- 업데이트 파일: `src/style.css`, `DESIGN.md`(규칙 2·8과 점검 행), `ROADMAP.md`(DS4, 현재·다음 줄), `TASK.md`, 검사 `work/design/system-audit.mjs`(휴대폰 44px 기준, 새 게임 확인 상태 추가), `work/design/replay-bar-check.mjs`(같은 기준), 로그 `work/design/tap-before.log`·`tap-after.log`·`replay-bar-tap.log`·`spacing-tap.log`·`matrix-tap.log`·`folds-tap-before.txt`·`folds-tap-after.txt`. 커밋하지 않았습니다.
- 이슈: 버튼과 상단 줄이 커진 만큼 판 크기 예산이 줄었습니다. 판 크기가 화면 높이로 정해지는 휴대폰에서 판이 10px 작아집니다(489×866 435 → 425, 375×667 288 → 278, 360×640 261 → 251). 390×844·430×932는 그대로입니다. 말풍선에서 접히는 안내는 늘지 않았습니다. 엔진 파일이 없어 가짜 엔진으로 쟀고, E2E와 실제 휴대폰 확인은 못 했습니다.
- 해결: 휴대폰 버튼 크기. 390×844 첫 안내의 "건너뛰기"가 36px에서 44px가 됐고, 캡처 픽셀로도 테두리 위 끝부터 그림자 끝까지 48px(44 + 그림자 4)로 확인했습니다.
- 남은 문제: 따라온 변경(상단 줄 62px, 판 10px 축소)에 대한 사용자 확인(DS4). 실제 휴대폰과 E2E. 종료 후 말풍선 영역의 "대국 복기" 시작 버튼은 이번 검사 상태에 없어 코드 값(44px)만 확인했습니다. 지난 턴들의 질문(그림자 대상, 복기 바 모양, DS1·DS3, DES-01·DES-02)은 그대로 열려 있습니다.
- 다음 작업: 판이 작아지는 게 괜찮은지 알려 주세요. 판 크기를 지키고 싶으시면 말풍선 영역이나 상단 줄에서 높이를 덜어 내는 안을 만들겠습니다.

design checks:
- control height phone 44 before | 490/660 | 12 sizes x 7 states, light | rendered | not spot-checked
- fix phone button height | fixed | 5 phone sizes x 7 states, light | rendered | 390x844 tutorial #tut-skip: check 36 before / 44 after, pixel 48 = 44 + shadow 4 after
- control height after | 660/660 | 12 sizes x 7 states, light | rendered | 390x844 tutorial #help-button: check 44 + shadow 3 / observed 47
- replay bar | 120/120 | 12 sizes x 10 checks, light | rendered | not spot-checked
- spacing S1/S2 | 198/198 | 12 sizes x 6 states, light | rendered | not spot-checked
- overflow and clipping | 72/72 frames clean | 12 sizes x 6 states, light | rendered | not spot-checked
- page scroll | 84/84 frames no scroll | 12 sizes x 7 states, light | rendered | not spot-checked
- color, shadow, font, text rules | 0 violations | 12 sizes x 7 states, light | rendered | not spot-checked
- hud folding before/after | 72/72 frames identical | 12 sizes x 6 states, light | rendered | not spot-checked
report-check: ok 2,577 chars 7f5d1b4b
