판 위 추천 고리를 진한 초록 #17692A로 바꿨고, 이제 판과 뚜렷이 구분됩니다. 실제 화면에서 고리와 판의 대비는 4.6:1로, 그래픽 대비 기준(3:1)을 넘습니다.

- **작업:**
  - 원래 고리 색은 `--lime-dark` #2F9C3A였습니다. 나무 판(#FFD98A→#F5BD5C)과의 대비가 2.07–2.62:1로 기준 3:1에 못 미쳐 구분이 잘 안 됐습니다.
  - 새 토큰 `--rec-ring` #17692A를 만들었습니다. 나무 판과의 대비는 3.99–5.03:1입니다. 색은 지시가 "더 진한 초록"이라 제가 골랐습니다.
  - 이 색은 추천 점선 고리 세 종류(1순위 표식, 다른 추천 후보, 가이드 추천)에만 적용했습니다. 카드 라벨, 갈래 비율 글자, 불러오기 막대는 기존 초록 그대로입니다. 고리 안 연두 채움과 굵기도 바꾸지 않았습니다.
  - 다시 흐려지지 않게 `work/design/system-check.mjs`에 R11 검사를 넣었습니다. 고리 색이 토큰과 같고 판과 3:1 이상인지 봅니다.
- **업데이트 파일:**
  - `src/style.css`
  - `work/design/system-check.mjs`
  - `DESIGN.md`: 토큰 표에 추천 고리 행, 화면 규칙과 검사 표에 R11
  - `TASK.md`: ds6 항목
  - `ROADMAP.md`: DS4 추가, 현재·다음 줄
  - 증거: `work/design/shots/ds5-1440x900-rec-ring.png`, `ds5-390x844-rec-ring.png`, `ds5-spot.txt`
  - 커밋은 하지 않았습니다.
- **이슈:** 다른 추천 후보 고리와 가이드 추천 고리는 측정한 화면 상태에 나타나지 않아 재지 못했습니다. 같은 색 토큰을 씁니다.
- **해결:** 추천 고리와 판의 대비 부족. 캡처 픽셀에서 고리 색 (23,105,42)를 그 자리 판과 비교해 직접 확인했습니다.
- **남은 문제:**
  - 새 색이 괜찮은지 봐 주세요. 캡처는 `work/design/shots/ds5-1440x900-rec-ring.png`입니다.
  - E2E는 아직 실행하지 못했습니다.
  - 지난 턴들의 확인 요청이 남아 있습니다.
    - 어느 그림자를 줄일지 (내 수 카드 그림자는 5px이고, 10px인 것은 판입니다)
    - 복기 바
    - 간격 값
    - 휴대폰 44px 버튼 때문에 판이 작아진 것
    - 글자 대비 부족 3곳(A11Y-05)
- **다음 작업:** 위 확인 사항에 답해 주시면 해당 항목을 마치겠습니다.

결과 목록 (preview 빌드, 엔진 대역, 기본 2크기; JOEDESIGN `report-check.mjs` 결과 ok):

- fix 추천 고리 대비 | fixed | 2 sizes x 1 state, light | rendered | 1440x900 candidates: 2.07–2.62 before(계산) / observed 4.60 after, capture; 390x844: observed 4.56 after
- R11 추천 고리 | 4/4 | 2 sizes x 6 states, light | rendered | 1440x900 candidates: check #17692A / observed (23,105,42)
- system-check 회귀 | 이전과 같음(R8 227/237, R8B 0/120 기존 미달) | 2 sizes x 6 states, light | rendered | not spot-checked
