턴 37 보고 — 토큰 이름을 영어로 통일했습니다. 코드의 CSS 변수 이름은 원래부터 모두 영어였고, 한글이 섞여 있던 곳은 DESIGN.md의 토큰 표였습니다. 화면은 바뀌지 않았습니다.

- 한글이 섞여 있던 곳(DESIGN 토큰 표):
  - 토큰 칸에 이름 없이 한글 설명과 값만 있던 행: 해설 문장, 비활성, 상태 글자, 돌, 그리고 "각 값"으로만 적힌 행들
  - 영어 이름이 토큰 칸이 아니라 역할 칸에 들어가 있던 행: --space-block 등 간격 토큰, --topbar-h
  - 코드에는 이름이 있는데 표에 안 적힌 것: --sky-3, --cloud-1/2, --gap, --pad
- 작업:
  - 모든 토큰 행의 토큰 칸에 영어 이름을 먼저 적었습니다. 변수가 없는 행은 "— (CSS 변수 없음)"으로 표시했습니다.
  - 표 위에 이름 규칙을 한 줄 적었습니다: 이름은 영어 소문자·하이픈, 한국어는 역할·부품 설명에만.
  - 이름이 없던 값 중 여러 곳에서 쓰이는 것을 토큰으로 만들었습니다. 값은 그대로입니다.
    - --coord: 판 좌표 글자
    - --stone-black / --stone-white: 판·로고·선택 표시의 돌 그라데이션 5곳
    - --font-display: Jua, 37곳
    - --font-body: 문장 글꼴
- 화면이 같은지 확인:
  - 3크기 × 3상태에서 판 돌·좌표까지 포함해 모든 요소의 계산된 글자색·배경·글꼴을 바꾸기 전후로 비교했고, 차이가 없습니다.
  - 처음엔 --font-display에 Pretendard를 대체 글꼴로 넣었습니다. 그러면 Jua에 없는 글자를 그리는 글꼴이 바뀌어서, 원래대로 'Jua', sans-serif로 되돌렸습니다.
  - design:check(밝은·다크): 간격·복기 바·눌림 검사는 통과했고, 실패는 기존 대비 미달(R8·R8B, A11Y-05)뿐입니다. tsc 통과.
- 업데이트 파일: src/tokens.css, src/style.css, DESIGN.md(토큰 표), TASK.md(ds30), ROADMAP.md(현재 줄). 커밋은 하지 않았습니다.
- 남은 문제:
  - 한 곳에서만 쓰이는 값(주 버튼 그라데이션, 판 바닥 그림자 등)과 글자 크기·모서리 값은 변수 없이 그대로 두었습니다. 이것들도 토큰으로 만들지 정해 주세요.
  - 앞서 남은 결정(A11Y-05, A11Y-08, LAYOUT-07, DS1 승인)도 그대로입니다.

결과 목록 (preview 빌드, 엔진 대역; JOEDESIGN report-check.mjs 결과 ok):
- 바꾸기 전후 계산 스타일(글자색·배경·글꼴) | 차이 0 (9 targets) | 3 sizes x 3 states, light | rendered | not spot-checked
- design:check --both | R5 210/210·T1 51/51, spacing·replay·press PASS, R8·R8B 기존 미달 | 2 sizes x 6 states, light+dark | rendered | not spot-checked
