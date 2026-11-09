이제 디자인 검사는 기본으로 1440×900과 390×844 두 크기만 돌립니다. 같은 기기에서 세 검사를 합쳐 79초 걸리던 것이 17초로 줄었습니다. 12크기 전체는 `--all`을 붙이면 그대로 돌릴 수 있습니다.

- **작업:**
  - 크기 목록을 `work/design/sizes.mjs` 한 곳에 모았습니다. `system-check`, `spacing-check`, `replay-check`, `capture-matrix`가 이 목록을 씁니다.
  - 전체 12크기는 `--all` 인자나 `GOMOKU_SIZES=all`로 돌립니다. 각 검사 출력에 몇 크기를 돌렸는지 찍힙니다.
  - 실행 시간(preview 빌드, 엔진 대역):

    | 검사 | 12크기 | 2크기 |
    | --- | --- | --- |
    | system-check | 30초 | 6초 |
    | spacing-check | 22초 | 5초 |
    | replay-check | 27초 | 6초 |

  - 제품 코드는 바꾸지 않았습니다.
- **업데이트 파일:**
  - 검사: `work/design/sizes.mjs`(새 파일), `work/design/system-check.mjs`, `work/design/spacing-check.mjs`, `work/design/replay-check.mjs`, `work/design/capture-matrix.mjs`
  - 기록: `DESIGN.md`(규칙 검사 표의 공통 범위), `TASK.md`(ds5 항목), `ROADMAP.md`(DS1·DS2·DS3·RB1의 Check를 기본 2크기로 고쳐 씀, 현재 줄)
  - 커밋은 하지 않았습니다.
- **이슈:**
  - **두 크기만으로는 못 잡는 실패가 있습니다.** 이번 세션에서 실제로 다른 크기에서만 드러난 실패가 세 번 있었습니다.
    - 489×866: 카드 제목이 접혀 사라짐
    - 375×667·360×640: 후보 알약이 아래로 잘림
    - 1024×768·1280×720: 버튼 사이 간격이 8px로 어긋남
  - 이 세 실패는 1440×900·390×844에서는 나오지 않았습니다. 그래서 화면 배치를 바꾼 뒤에는 `--all`로 한 번 돌리기를 권합니다.
  - `capture-matrix.mjs`는 엔진 대역을 쓰지 않아서, 엔진 파일이 없는 이 폴더에서는 돌리지 않았습니다(ENV-06).
- **해결:** 없음.
- **남은 문제:**
  - E2E 미실행: 브라우저 바이너리가 없어서입니다.
  - 지난 턴들의 확인 요청이 그대로 남아 있습니다.
    - 어느 그림자를 줄일지: 내 수 카드 그림자는 실제로 5px이고, 10px인 것은 판입니다.
    - 복기 바 구성
    - 간격 값
    - 휴대폰 44px 버튼 때문에 판이 작아진 것
    - 글자 대비 부족 3곳(A11Y-05)
- **다음 작업:** 위 확인 사항에 답해 주시면 해당 항목을 마치겠습니다. 브라우저 설치를 허가해 주시면 E2E를 돌리겠습니다.

결과 목록 (preview 빌드, 엔진 대역; JOEDESIGN `report-check.mjs` 결과 ok):

- system-check 기본 | R1 12/12, R7 94/94, R8 227/237, R8B 0/120 등 | 2 sizes x 6 states, light | rendered | not spot-checked (두 크기의 스폿 체크는 이전 기록 재사용, 이번 변경은 검사 범위만 바꿈)
- spacing-check 기본 | 38/38, clip 26/26 | 2 sizes x 4 states, light | rendered | not spot-checked
- replay-check 기본 | 8/8 | 2 sizes x 4 states, light | rendered | not spot-checked
- --all 대조 | spacing 224/224, clip 156/156, replay 48/48 | 12 sizes x 4 states, light | rendered | not spot-checked

R8 미달 10건과 R8B 0/120은 이미 열려 있는 대비 부족(A11Y-05)이며, 이번 변경과는 관계없습니다.
