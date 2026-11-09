휴대폰 가로 모드(844×390, 667×375 등)를 지원하도록 고쳤습니다. 바꾸기 전에는 667×375에서 시작 버튼이 선택 카드에 가려져 게임을 시작할 수조차 없었습니다. 이제 가로 크기에서도 시작·대국·복기·도움말이 스크롤이나 잘림 없이 한 화면에 들어갑니다.

- **작업:**
  - **원인:** 가로로 눕힌 휴대폰은 폭이 700px를 넘어 데스크톱 크기(64px 상단 줄, 76px 버튼)가 적용됐습니다. 동시에 폭이 900px보다 좁아 판·말풍선·버튼이 세로로 쌓였는데, 높이 390px에는 다 들어갈 수 없었습니다.
  - **크기 규칙:** 높이가 500px 이하이면 휴대폰 크기 규칙(작은 상단 줄, 44px 이상 버튼, 카드 모양)을 쓰도록 바꿨습니다.
  - **옆 배치:** 가로:세로가 3:2 이상이면 판을 왼쪽에, 말풍선과 버튼을 오른쪽에 둡니다.
  - **시작 화면:** 제목을 왼쪽에, 선택 카드와 시작 버튼을 오른쪽에 두었습니다. 667×375에서 제목이 "오목 한 / 판!"으로 꺾여서 한 줄로 고쳤습니다.
  - **도움말 창:** 왼쪽에 규칙 목록, 오른쪽에 숫자 뜻·다시 보기·라이선스를 두는 두 칸으로 바꿨습니다. 처음 검사에서 라이선스 부분이 화면 밖으로 나가 이렇게 고쳤습니다.
  - **판 크기:** 844×390은 317px, 667×375는 302px입니다.
  - 배치 방식은 제가 골랐습니다. DOM은 바꾸지 않았습니다.
  - **검사:** `npm run design:check -- --all`에 844×390·667×375를 넣어 14크기로 늘렸습니다. 휴대폰·옆 배치 판정도 CSS와 같은 조건으로 맞췄습니다.
- **결과:**
  - 14크기 전체 검사에서 새 실패는 없습니다. 실패로 남은 것은 기존 대비 미달(A11Y-05)뿐입니다.
  - 다크 모드도 같은 결과입니다.
  - 740×360·932×430은 별도 탐침으로만 확인했고, 같은 배치로 나옵니다.
  - 캡처: `work/design/shots/ds15-before-*`, `ds15-after-*`, `ds15-after2-*`
- **업데이트 파일:**
  - 코드: `src/style.css`, `src/tokens.css`
  - 검사 스크립트: `work/design/sizes.mjs`, `system-check.mjs`, `spacing-check.mjs`, `replay-check.mjs`, `system-spot.mjs`, `spacing-spot.mjs`, `capture-matrix.mjs`
  - 기록: `DESIGN.md`(R9L 규칙과 검사 행, 크기 범위), `TASK.md`(ds23), `ROADMAP.md`(DS14)
  - 커밋은 하지 않았습니다.
- **이슈:** 기본 `design:check`는 여전히 두 크기(1440×900·390×844)만 봅니다. 가로 크기는 `--all`을 붙여야 검사됩니다.
- **해결:**
  - 667×375 시작 버튼 가림: 바뀐 캡처를 보고, 실제로 버튼을 눌러 게임이 시작되는 것까지 확인했습니다.
  - 가로 도움말 창이 화면 밖으로 나가던 문제: 캡처로 확인했습니다.
- **남은 문제:**
  - 가로 배치가 괜찮은지 봐 주세요.
  - 실기기에서 화면을 돌렸을 때와 주소창 때문에 높이가 줄어드는 경우는 확인하지 못했습니다.
  - 휴대폰 E2E는 기본으로 꺼져 있고, 가로용 E2E도 아직 없습니다.
  - 앞 턴들의 확인 요청과 LAYOUT-07, A11Y-08, A11Y-05 결정도 남아 있습니다.

결과 목록 (preview 빌드, 엔진 대역; JOEDESIGN `report-check.mjs` 결과 ok):

- fix 667x375 시작 버튼 가림 | fixed | 1 size x 1 state, light | rendered | 667x375 intro: 시작 버튼이 카드 아래 before / 카드 오른쪽 아래에 보이고 눌림 after, capture
- fix 가로 도움말 창 화면 밖 | fixed | 2 sizes x 1 state, light | rendered | 667x375 help: 라이선스가 화면 밖 before / 두 칸 창 전체 보임 after, capture
- design:check --all R1 | 84/84 | 14 sizes x 6 states, light | rendered | 844x390 candidates: check 화면 밖 0 / observed 캡처에서 판·말풍선·버튼 모두 보임
- design:check --all 나머지 | R7 658/658·R9 28/28·R12 848/848·R14 28/28, spacing 256/256·clip 182/182, replay 56/56, R8·R8B 기존 미달 | 14 sizes x 6 states, light | rendered | not spot-checked
- design:check --all 다크 | spacing·replay PASS, R8·R8B 기존 미달 | 14 sizes x 6 states, dark | rendered | not spot-checked

`tsc` 통과입니다.
