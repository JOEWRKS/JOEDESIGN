- **작업:** `DESIGN.md` 맨 위에 "디자인 시스템 v1"을 만들었습니다. 상태는 DRAFT Rev 1이고 아직 승인하지 않으셨습니다. `src/style.css`는 바꾸지 않았고, 거기서 읽은 값으로 표 네 개를 만들었습니다: 색(19행), 글꼴·글자 크기(9행), 간격(6행), 그림자·테두리·모서리(8행). 모든 값의 상태는 measured(코드에서 읽고 렌더로 확인함)이고 승인값이 아닙니다. 화면 규칙은 R1~R10·R8B·T1·EXT·M1·M2를 적었고, 규칙마다 검사 방법·스폿 체크·범위·측정 안 한 부분을 담은 규칙 검사 표를 붙였습니다. 검사는 새로 만든 스크립트로 브라우저에서 실제 렌더를 쟀습니다. 문서 아래쪽 v0.1·v0.2의 옛 색 표는 비활성으로 표시했습니다.
- **업데이트 파일:**
  - `DESIGN.md`
  - `TASK.md` (2026-11-07 ds1 항목)
  - `ROADMAP.md` (P7 DS1 추가, 현재·다음 줄 다시 씀)
  - `ISSUES.md` (A11Y-05, ENV-06)
  - 새 검사 스크립트: `work/design/system-check.mjs`, `work/design/system-spot.mjs`, `work/design/engine-stub.mjs`
  - 증거: `work/design/shots/ds1-spot.txt`, `ds1-1440x900-candidates.png`, `ds1-390x844-route.png`, `ds1-font-card-title.png`
  - 커밋은 하지 않았습니다.
- **이슈:**
  - **글자 대비 부족 3곳 (A11Y-05):** 위쪽 대결줄의 수 표시(분홍 글자), 첫 안내의 단계 표시(하늘색 위 흰 글자), 판의 좌표 글자가 기준 4.5:1에 못 미칩니다. 수치는 아래 결과 목록의 R8·R8B 줄에 있습니다.
  - **환경 문제 (ENV-06):** 이 폴더의 `node_modules`가 프로젝트 밖 폴더로 연결돼 있어, 5299 dev 서버가 글꼴(Jua·Pretendard)을 403으로 거절합니다. 그래서 dev 서버 화면은 대체 글꼴로 그려집니다. 또 엔진 파일 `public/engine/rapfi*`가 없어 시작 화면 다음으로 넘어가지 못합니다.
  - 그래서 측정 방법을 두 가지 바꿨습니다. 지정된 dev 서버 대신 `vite build` 후 `vite preview`를 같은 5299 포트로 띄워 출하 빌드를 쟀습니다. 엔진은 검사 스크립트 안에서만 대역으로 바꿨기 때문에 화면의 수와 승률 숫자는 가짜입니다.
  - 엔진 파일을 외부에서 받으려면 허가가 필요해서 받지 않았습니다. 작업이 끝난 뒤 제 5299 서버는 껐습니다.
- **해결:** 없음.
- **남은 문제:**
  - v1 DRAFT 승인 여부를 정해 주셔야 합니다.
  - 대비 부족 3곳의 색을 바꿀지 정해 주셔야 합니다. 제안 값은 다음과 같습니다.
    - 수 표시: #B8325A (5.77:1, 이미 쓰는 색)
    - 단계 글자: `--ink` (7.56:1)
    - 좌표: #6B3A12 (5.50:1)
  - 그 밖의 열린 결정:
    - 하드코딩된 색을 토큰으로 올릴지, 쓰이지 않는 `--danger`를 지울지
    - 판 밖 글자 크기가 24단계인데 줄일지
    - 보조 버튼이 v0.1 목표 44px보다 낮은 36px까지 내려가는데 그대로 둘지
    - 간격이 2px 단위인데 4/8px 단계로 정리할지
  - M1(색만으로 구별하지 않기)과 M2(게임처럼 보이기)는 자동 검사가 없습니다.
  - 측정하지 않은 상태가 10개(계산 중·내 수 평가·AI 응수·자세히 보기·종료·복기·새 게임 확인·금수 안내·가이드 꺼짐·엔진 실패) 있고, 실제 엔진으로도 재지 않았습니다.
  - 화면에서 본 점: 1440×900 후보 상태에서 오른쪽 칸 가운데가 약 330px 비어 보입니다. 이 구성을 어떻게 볼지는 판단해 주셔야 합니다.
- **다음 작업:** 승인 여부와 대비 3곳 처리를 정해 주시면, 바꾼 뒤 R8·R8B를 12크기 × 6상태로 다시 돌리고 바뀐 화면 캡처에서 픽셀 대비를 직접 확인하겠습니다.

결과 목록 (preview 빌드, 엔진 대역; JOEDESIGN `report-check.mjs` 결과 ok):

- R1 한 화면 | 72/72 | 12 sizes x 6 states, light | rendered | 375x667 route: check 화면 밖 0, 문서 375x667 / observed 전체 페이지 캡처 375x667, scrollY 0
- R2 위계 | 60/60 | 12 sizes x 3 states, light (tutorial 12대상은 숫자 쪽 미측정) | rendered | 390x844 route: check 40px > 22px / observed 잉크 높이 29px > 18px
- R3 외곽선 | 800/800 | 12 sizes x 6 states, light | rendered | 1440x900 candidates 말풍선: check 4px / observed 4px
- R4 입체 그림자 | 776/776 | 12 sizes x 6 states, light | rendered | 1440x900 candidates 말풍선 아래: check 4+8 = 12px / observed 12px
- R5 글꼴 역할 | 1233/1233 | 12 sizes x 6 states, light | rendered | 1440x900 candidates 카드 제목: check Jua 폭 154.5 / observed 렌더 폭 154.6, 캡처에서 Jua 모양
- R6 최소 글자 11px | 1533/1533 | 12 sizes x 6 states, light | rendered | 390x844 route 부제: check 11px / observed 잉크 높이 10px
- R7 버튼 높이 | 564/564 | 12 sizes x 6 states, light | rendered | 390x844 route 주 버튼: check 60+7 = 67px / observed 67px
- R8 글자 대비 | 1323/1383, 미달 60 | 12 sizes x 6 states, light | rendered | 1440x900 candidates 수 표시: check 2.65 / observed 2.65
- R8B 판 좌표 대비 | 0/720 | 12 sizes x 4 states, light | rendered | spot check differs: 1440x900 candidates 열 H: check 3.11 / observed 3.79 (검사값은 하한)
- R9 배치 | 24/24 | 12 sizes x 2 states, light | rendered | 1440x900 candidates: check 40px / observed 40px
- R10 가장자리 여백 | 144/144 | 12 sizes x 6 states, light | rendered | 390x844 route: check 12px / observed 12px
- T1 토큰 렌더 | 303/303 | 12 sizes x 6 states, light | rendered | 1440x900 candidates: check FFFFFF, 6EE05A / observed 255,255,255 및 110,224,90
- EXT 외부 요청 | 12/12 | 12 sizes x 6 states, light | rendered | not spot-checked

R8 미달 60건의 내역은 다음과 같습니다.
- 수 표시: 2.65:1, 48건
- 첫 안내 단계: 1.99:1, 12건

판 좌표는 그라데이션에서 가장 어두운 곳 기준으로 3.11:1, 1440×900의 H 자리 픽셀로는 3.79:1입니다.
