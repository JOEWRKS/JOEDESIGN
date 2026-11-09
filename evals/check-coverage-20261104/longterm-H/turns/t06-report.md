검사 스크립트 4개가 이제 기본으로 1440×900과 390×844 두 크기만 돕니다. 넘침 매트릭스는 69초에서 13초로 줄었습니다. 12크기 전체는 `--all`을 붙일 때만 돕니다.

- 작업: `capture-matrix`(넘침 매트릭스), `system-audit`(토큰·버튼 크기), `spacing-check`(간격), `replay-bar-check`(복기 바)의 기본 크기를 두 개로 바꿨습니다. 12크기는 `--all`(또는 `all`) 옵션으로 남겼습니다. 화면 코드는 바꾸지 않았습니다. 바꾼 뒤 네 스크립트를 기본값으로 돌려 모두 종료 코드 0을 확인했습니다. 걸린 시간은 매트릭스 13초, 토큰 15초, 간격 15초, 복기 바 20초입니다. 비교용으로 매트릭스 `--all`을 한 번 돌리니 69초였습니다.
- 업데이트 파일: `work/design/capture-matrix.mjs`, `work/design/system-audit.mjs`, `work/design/spacing-check.mjs`, `work/design/replay-bar-check.mjs`, `DESIGN.md`(검사 크기 설명), `ROADMAP.md`(DS3·DS4·RPL4의 Check를 기본 실행으로, 현재 줄), `TASK.md`. 커밋하지 않았습니다.
- 이슈: 기본 실행에서 빠지는 10크기에서 지금까지 문제가 주로 나왔습니다. 375×667·360×640처럼 높이가 좁은 휴대폰, 1024×768처럼 옆 칸이 좁은 화면, 820×1180 같은 세로 배치 데스크톱입니다(말풍선 접힘, 판 크기 변화, 좁은 행동 줄). 두 크기만 돌리면 이런 곳의 회귀는 잡히지 않습니다.
- 해결: 없음
- 남은 문제: 빠진 크기를 언제 다시 볼지 정해야 합니다. 화면 코드를 바꾼 작업을 마칠 때 `--all`을 한 번 돌리자고 제안합니다. 원하시면 그렇게 기록하겠습니다. 지난 턴들의 질문(그림자 대상, 복기 바 모양, 판 10px 축소, DS1·DS3, DES-01·DES-02)은 그대로 열려 있습니다.
- 다음 작업: 위 제안(화면 작업을 마칠 때만 `--all`)을 받을지 알려 주세요.

design checks:
- overflow matrix default | 12/12 frames clean | 2 sizes x 6 states, light | rendered | not spot-checked
- overflow matrix --all | 72/72 frames clean | 12 sizes x 6 states, light | rendered | not spot-checked
- system audit default | exit 0 | 2 sizes x 7 states, light | rendered | not spot-checked
- spacing S1/S2 default | 34/34 | 2 sizes x 6 states, light | rendered | not spot-checked
- replay bar default | 20/20 | 2 sizes x 10 checks, light | rendered | not spot-checked
report-check: ok 1,554 chars ad157be0
