다크 모드를 넣었습니다. 시스템 설정을 따라가고, `src/tokens.css`의 다크 블록에서 색 토큰만 바꿉니다. 밝은 모드 화면은 바꾸기 전과 똑같습니다.

- **작업:**
  - **준비:** 색 토큰만 바꿔서 다크가 되려면 `src/style.css`에 직접 박혀 있던 색부터 토큰으로 올려야 했습니다. 그래서 다음을 토큰으로 바꿨습니다. 밝은 모드 값은 모두 원래 그대로입니다.
    - 글자색 7종: 해설, 안내, 경고, 실패 등
    - 표면색: 비활성, 스위치, 추천/경고 알약, 하늘 아래쪽, 구름
  - **글자 토큰 분리:** 지금까지 외곽선 색 `--ink`가 글자에도 쓰였습니다. 화면·흰 표면 위 글자는 새 `--text`로 분리했습니다. 노랑·연두·하늘·분홍 같은 밝은 칩 위 글자는 다크에서도 진한 색으로 남도록 고정했습니다. 포커스 고리는 `--focus` 토큰을 씁니다.
  - **다크 값:** `@media (prefers-color-scheme: dark)` 블록에서 토큰만 바꿉니다. 배경은 밤하늘 남보라, 표면은 어두운 남보라, 글자는 밝게, 포커스 고리는 노랑입니다. 판(나무·좌표·돌)과 밝은 칩은 그대로 둡니다. 구체적인 색은 지시에 없어서 제가 골랐습니다.
  - **검사:** system-check, spacing-check, replay-check에 `--dark` 옵션을 넣어 다크 모드로도 돌 수 있게 했습니다.
- **업데이트 파일:**
  - `src/tokens.css`, `src/style.css`
  - `work/design/sizes.mjs`, `work/design/system-check.mjs`, `work/design/spacing-check.mjs`, `work/design/replay-check.mjs`
  - `DESIGN.md` (다크 모드 토큰 표), `TASK.md` (ds11), `ROADMAP.md` (DS7), `ISSUES.md` (A11Y-05에 다크 결과 추가)
  - 다크 캡처: `work/design/shots/ds7-*-dark-*.png`
  - 커밋은 하지 않았습니다.
- **이슈:**
  - 다크 배경에서는 남색 외곽선과 아래로 떨어지는 그림자의 대비가 낮아, 입체감이 밝은 모드보다 약하게 보입니다.
  - 기존 대비 미달 두 곳(첫 안내 단계 글자, 판 좌표)은 다크에서도 그대로입니다. 대결줄 수 표시는 다크에서는 기준을 넘습니다.
- **해결:** 없음.
- **남은 문제:**
  - 다크 색이 괜찮은지 봐 주세요. 캡처는 `work/design/shots/ds7-1440x900-dark-candidates.png`, `ds7-390x844-dark-intro.png`입니다.
  - 다크 캡처를 픽셀 단위로 대조하지 않았습니다. 지금 대조 스크립트는 밝은 모드 색 기준입니다.
  - 복기 화면과 도움말은 다크에서 검사만 했고 캡처는 눈으로 보지 않았습니다.
  - E2E는 아직 돌리지 못했습니다(이 폴더에 테스트용 브라우저가 없음).
  - 앞 턴들의 확인 요청과 LAYOUT-07(작은 휴대폰에서 금수 안내가 뜨면 후보 알약이 잘림) 수정 여부도 그대로 남아 있습니다.
- **다음 작업:** 다크 색을 확인해 주시고, LAYOUT-07을 고칠지 정해 주세요.

결과 목록 (preview 빌드, 엔진 대역; JOEDESIGN `report-check.mjs` 결과 ok):

- 밝은 모드 전후 계산 스타일 비교 | 차이 0 (9 targets) | 3 sizes x 3 states, light | rendered | not spot-checked
- system-check 밝은 모드 | 이전과 같음(R8 227/237, R8B 0/120 기존 미달) | 2 sizes x 6 states, light | rendered | not spot-checked
- system-check 다크 | R1 12/12, T1 51/51, R7 94/94, R8 235/237, R8B 0/120 | 2 sizes x 6 states, dark | rendered | not spot-checked
- spacing-check 다크 | 38/38, clip 26/26 | 2 sizes x 4 states, dark | rendered | not spot-checked
- replay-check 다크 | 8/8 | 2 sizes x 4 states, dark | rendered | not spot-checked

`tsc`는 통과했습니다.
