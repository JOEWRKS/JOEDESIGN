토큰을 새 파일 `src/tokens.css`로 분리했고, 화면은 분리 전과 같습니다. `src/style.css`는 517줄에서 508줄로 줄었습니다.

- **작업:**
  - `src/tokens.css`(22줄)로 옮긴 것: 색 변수 전부, 간격 토큰(`--space-block` / `--space-row` / `--space-tight`, `--board-lift`), 복기 바 토큰(`--rb-h` / `--rb-lift` / `--rb-total`), 그리고 각각의 휴대폰 값.
  - 휴대폰 복기 바 높이는 style.css에서 46px로 정한 뒤 56px로 다시 덮어쓰던 두 줄이었습니다. 실제로 적용되던 56px 한 줄로 합쳤습니다.
  - `src/main.ts`가 tokens.css를 style.css보다 먼저 불러옵니다.
  - 표면별 그림자 높이(`--lift`)와 무대 배치 변수(`--top`, `--cta`, `--hud-min` 등)는 쓰이는 규칙 바로 옆에 있어야 읽기 쉬워서 style.css에 남겼습니다. 이것도 옮기길 원하시면 말씀해 주세요.
- **화면이 그대로인지 확인한 방법:** 분리 전후로 1440×900·390×844·360×640 × 시작 화면·첫 수·복기 화면의 계산된 스타일과 위치를 요소 약 9,800개 전부 비교했습니다. 판·로고 안 요소는 비교에서 뺐습니다.
  - 다른 곳은 복기 카드 라벨 너비 3건뿐입니다. 대역 AI가 매번 다른 좌표에 두어서 생기는 차이로, 분리 전에 두 번 찍어 비교했을 때도 같은 곳에서 나왔습니다.
  - 디자인 검사, `tsc`, 단위 테스트 결과도 분리 전과 같습니다(아래 목록).
- **업데이트 파일:**
  - 코드: `src/tokens.css`(새 파일), `src/style.css`, `src/main.ts`
  - 기록: `DESIGN.md`(토큰 역할 표 설명에 파일 위치 추가), `TASK.md`(ds10 항목), `ROADMAP.md`(현재 줄)
  - 커밋은 하지 않았습니다.
- **이슈:** 없음.
- **해결:** 없음.
- **남은 문제:**
  - E2E는 아직 돌리지 못했습니다.
  - 지난 턴에 찾은 LAYOUT-07(작은 휴대폰에서 금수 안내가 뜨면 후보 알약이 잘림)을 고칠지 정해 주셔야 합니다.
  - 앞 턴들의 확인 요청도 그대로 남아 있습니다: 그림자 대상, 복기 바, 간격 값, 판 크기 변화, 추천 고리 색, 캡션·안내 줄 값, 대비 미달 3곳(A11Y-05).
- **다음 작업:** LAYOUT-07 수정 여부를 알려 주세요.

결과 목록 (preview 빌드, 엔진 대역; JOEDESIGN `report-check.mjs` 결과 ok):

- 분리 전후 계산 스타일 비교 | 9 targets 같음(대역 좌표 잡음 3건 제외) | 3 sizes x 3 states, light | rendered | not spot-checked
- system-check | R1 12/12, T1 51/51, R11 4/4, R8 227/237·R8B 0/120 기존 미달 | 2 sizes x 6 states, light | rendered | not spot-checked
- spacing-check | 실패 줄 없음, clip 26/26 | 2 sizes x 4 states, light | rendered | not spot-checked
- replay-check | 8/8 | 2 sizes x 4 states, light | rendered | not spot-checked

`tsc` 통과, 단위 테스트는 87 통과·1 건너뜀입니다.
