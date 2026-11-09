대국 화면의 카드·버튼·안내 줄 간격을 한 규칙(S1~S5)으로 맞췄고, 어긋나면 실패하는 검사 스크립트를 넣었습니다. 바꾼 뒤 검사는 224곳 모두 통과했고, 바꾸기 전에는 224곳 중 98곳만 맞았습니다. 간격 값은 제가 골랐으니 화면을 보시고 확인해 주세요. E2E 테스트는 이 폴더에 브라우저가 설치돼 있지 않아 돌리지 못했습니다.

- **작업:**
  - **원인:** 떨어지는 그림자(3–10px)가 틈을 먹고, 크기마다 CSS 간격도 달랐습니다. 같은 역할의 틈이 1–12px로 제각각이었습니다(예: 판→말풍선 6·9px, 말풍선→후보 알약 2·4px, 버튼 줄→안내 줄 1·2px).
  - **규칙:** 간격은 눈에 보이는 가장자리, 즉 그림자 끝부터 잽니다. 값은 데스크톱 / 휴대폰 순서입니다.

    | 규칙 | 범위 | 데스크톱 / 휴대폰 |
    | --- | --- | --- |
    | S1 | 세로로 쌓이는 블록 사이 | 16 / 12px |
    | S2 | 버튼 줄 안 | 12 / 10px |
    | S3 | 후보 알약 사이 | 12 / 10px |
    | S4 | 버튼 줄 → 안내 줄 | 8 / 6px |
    | S5 | 남는 높이는 카드 묶음과 버튼 줄 사이 한 곳에만, S1 이상 | 16 / 12px 이상 |

  - **코드:** `src/style.css` 끝에 간격 규칙 블록을 넣었습니다. 표면마다 그림자 높이 `--lift`를 두고 그만큼 아래 여백을 더하는 방식입니다. 휴대폰의 두기 버튼과 비활성 버튼 그림자가 7px로 남아 있던 것도 다른 버튼과 같은 6px로 맞췄습니다. DOM과 문구는 그대로입니다.
  - **검사:**
    - `work/design/spacing-check.mjs`: 12크기 × 4상태에서 S1~S5와 잘림을 재고, 하나라도 어긋나면 종료 코드 1로 끝납니다.
    - `work/design/spacing-spot.mjs`: 같은 자리를 캡처 픽셀로 직접 재서 검사값과 비교합니다.
  - 측정 환경은 지난 턴과 같습니다(preview 빌드, 5299 포트, 엔진 대역).

- **업데이트 파일:**
  - `src/style.css`
  - `DESIGN.md`: 간격 토큰 행과 "대국 화면 간격 규칙 (S1~S5)" 절, 규칙 검사 표에 S1~S5·S-clip 행 추가
  - `TASK.md`: 2026-11-07 ds2 항목
  - `ROADMAP.md`: P7에 DS2 추가, 현재·다음 줄 다시 씀
  - `ISSUES.md`: ENV-06에 E2E 브라우저 없음 추가
  - `work/design/spacing-check.mjs`, `work/design/spacing-spot.mjs`
  - 증거: `work/design/shots/ds2-spot.txt`, `ds2-1440x900-candidates.png`, `ds2-390x844-route.png`, `ds2-360x640-candidates.png`
  - 커밋은 하지 않았습니다.

- **이슈:**
  - E2E는 `.browsers/`에 Playwright 브라우저가 없어 시작하지 못했습니다(ENV-06). 설치하려면 내려받기 허가가 필요해서 하지 않았습니다.
  - 글자 대비 부족 3곳(A11Y-05)은 지난 턴 그대로 열려 있습니다.

- **해결:** 휴대폰 두기·비활성 버튼 그림자 7→6px 불일치. 실패했던 390×844 first 화면의 캡처에서 바로잡힌 것을 직접 확인했습니다(아래 fix 줄).

- **남은 문제:**
  - 간격 값(16/12, 12/10, 8/6px)을 확인해 주셔야 합니다.
  - E2E 미실행.
  - 복기·종료·금수 알림·엔진 알림·제한 안내·자세히 보기 상태와 시작 화면의 간격은 재지 않았습니다.
  - 1440×900에서 후보 알약과 주 버튼 사이가 약 300px 빈 것은 S5 규칙대로 남는 높이가 모인 자리입니다. 이 구성을 어떻게 볼지는 판단해 주세요.

- **다음 작업:** 간격 값을 확인해 주시면 DS2 확인이 끝납니다. 브라우저 설치를 허가해 주시면 E2E를 돌리겠습니다. 대비 3곳은 결정해 주시면 고치겠습니다.

결과 목록 (preview 빌드, 엔진 대역; JOEDESIGN `report-check.mjs` 결과 ok):

- spacing S1~S5 전 | 98/224 (허용 ±1px) | 12 sizes x 4 states, light | rendered | not spot-checked
- spacing S1~S5 후 | 224/224 (허용 ±0.5px) | 12 sizes x 4 states, light | rendered | 1440x900 candidates 말풍선→알약: check 16 / observed 16; 390x844 route 판→말풍선: check 12 / observed 12; 390x844 route 취소→주 버튼: check 10 / observed 10; 1440x900 알약 사이: check 12 / observed 12; 1440x900 버튼→안내 줄: check 8 / observed 8; 360x640 남는 틈: check 15 / observed 15
- clip 곁 검사 | 156/156 | 12 sizes x 4 states, light | rendered | not spot-checked
- 보이는 정보·판 크기 전후 비교 | 36/36 같음 | 12 sizes x 3 states, light | rendered | not spot-checked
- system-check 회귀 | ds1과 같음(R8 1323/1383, R8B 0/720 기존 미달) | 12 sizes x 6 states, light | rendered | not spot-checked
- fix 휴대폰 두기·비활성 버튼 그림자 7→6px | fixed | 5 sizes x 3 states, light | rendered | 390x844 first 버튼 그림자→안내 줄: spacing-check 5 before / observed 6 after, capture

`tsc` 통과, 단위 테스트 87 통과·1 건너뜀입니다.
