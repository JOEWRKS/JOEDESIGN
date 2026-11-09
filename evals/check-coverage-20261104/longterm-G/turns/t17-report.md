이제 `npm run design:check` 한 번으로 디자인 검사 전체가 돕니다. 다만 아직 고치지 않은 글자 대비 문제(A11Y-05) 때문에 지금은 항상 실패로 끝납니다.

- **작업:**
  - 진입 스크립트 `work/design/design-check.mjs`를 새로 만들고, `package.json`에 `design:check` 명령을 넣었습니다.
  - 한 번 실행하면 이 순서로 돕니다.
    1. 빌드
    2. 출하 빌드로 preview 서버 띄우기
    3. 세 검사 실행: 화면 규칙(R1~R12), 간격, 복기 바
    4. 요약 표 출력
    5. 서버 종료
  - 하나라도 실패하면 종료 코드 1로 끝납니다. 이를 위해 `system-check`도 실패 규칙이 있으면 1을 내도록 고쳤습니다.
  - 붙일 수 있는 옵션: `-- --all`(12크기), `-- --dark`(다크 모드), `-- --both`(밝은+다크), `-- --no-build`(빌드 생략). 포트는 `GOMOKU_DEV_PORT`로 정합니다.
  - 세 검사 파일은 지우지 않고 진입 스크립트가 부르는 부품으로 남겼습니다. 따로 돌릴 수도 있습니다. 세 파일을 한 파일로 다시 쓰기를 원하시면 말씀해 주세요.
  - 픽셀 대조 스크립트 두 개(`system-spot.mjs`, `spacing-spot.mjs`)는 캡처 파일을 남기는 증거용이라 묶지 않았습니다.
- **실행 결과** (`npm run design:check -- --both`, 기본 2크기):
  - spacing-check와 replay-check는 밝은·다크 모두 통과했습니다.
  - system-check는 R8(글자 대비)과 R8B(판 좌표 대비)만 실패했습니다. 둘 다 이미 열려 있는 A11Y-05입니다.
  - `--no-build`로 한 번 돌리는 데 18초 걸렸고, 끝난 뒤 5299 포트는 비어 있었습니다.
- **업데이트 파일:**
  - `package.json`
  - `work/design/design-check.mjs`(새 파일)
  - `work/design/system-check.mjs`
  - `DESIGN.md`(검사 명령), `TASK.md`(ds15), `ROADMAP.md`(현재 줄)
  - 커밋은 하지 않았습니다.
- **이슈:** A11Y-05가 열려 있는 동안 `design:check`는 늘 실패로 끝납니다.
- **해결:** 없음.
- **남은 문제:**
  - A11Y-05 대비 색을 정해 주시면 고치겠습니다. 그러면 `design:check`가 통과로 끝납니다.
  - 앞 턴들의 확인 요청과 LAYOUT-07, A11Y-08 결정도 남아 있습니다.
  - E2E는 아직 실행하지 못했습니다.

결과 목록 (preview 빌드, 엔진 대역; JOEDESIGN `report-check.mjs` 결과 ok):

- design:check system-check | FAIL(R8 227/237·R8B 0/120 밝은, R8 235/237·R8B 0/120 다크, 기존 A11Y-05) | 2 sizes x 6 states, light+dark | rendered | not spot-checked
- design:check spacing-check | PASS | 2 sizes x 4 states, light+dark | rendered | not spot-checked
- design:check replay-check | PASS | 2 sizes x 4 states, light+dark | rendered | not spot-checked
