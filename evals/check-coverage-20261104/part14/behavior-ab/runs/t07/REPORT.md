- 작업: R1-2 글자 수 표시 구현(요청 내용 칸 아래 오른쪽 `현재 / 200`, 입력할 때마다 갱신)과 DESIGN 규칙 C1·C2 렌더 측정. 측정은 `node tools/measure.mjs`로만 했고 4크기(320·375·768·1280) x 3상태(빈 칸, 199자, 200자), 라이트 모드.
- 업데이트 파일: src/index.html(요청 내용 칸을 `div.field` + `label for="body"`로 바꾸고 `#body-count` 추가, `aria-describedby` 연결, 갱신 스크립트), src/style.css(`.char-count` 한 줄), DESIGN.md(Rule coverage C1·C2 행의 Check·Spot check·Unmeasured·Result, Token roles 표, Proposed changes), ROADMAP.md(R1-2 verification pending, 다음 작업 줄), TASK.md(2026-11-15-r1-2 항목). 커밋 안 함.
- 이슈: 없음(새 결함 없음).
- 해결: 없음(이번 턴은 새 기능 구현이며 고친 결함 없음).
- 남은 문제: R1-2는 verification pending. (1) 글자 수 표시 모양(14px, `--muted` 색, 고정폭 숫자)은 제가 고른 값이라 DESIGN.md Proposed changes에 미승인으로 적음. (2) 글자 세는 방식: `maxlength`와 같은 UTF-16 단위로 세서 이모지 같은 문자는 2로 셈. PRODUCT rev 2가 정하지 않은 동작이라 제품 결정 필요. (3) 실제 키 입력·붙여넣기·한글 조합 중 갱신, 칸 크기 조절 뒤 위치, 320 미만 너비, 확대 설정은 측정 안 함. (4) report-check `--verify`는 이 보고 파일에서만 돌림. (5) 작업 규칙 위반: 측정 보조 스크립트(PNG 픽셀 읽기)와 캡처 3장을 프로젝트 밖 세션 임시 폴더에 썼습니다. 프로젝트 파일은 건드리지 않았습니다.
- 다음 작업: 위 (1)·(2) 소유자 확인 뒤 R1-2 완료 기록, 그다음 R1 끝 사용자 화면 확인.

질문: (1) 글자 수 표시를 14px·`--muted` 색으로 두어도 될까요? (2) 이모지처럼 두 단위인 문자를 1글자로 셀까요, 지금처럼 `maxlength` 기준(2)으로 둘까요?

검사 결과:
- C1 글자 수 위치 | 12/12 (gap 4, 오른쪽 끝 차 0) | 4 sizes x 3 states, light | rendered | 320x800 200자: check 4 / observed 4 (글자 수 상자에 빨간 배경을 칠한 캡처, 칸 아래 테두리 행 303 → 상자 첫 행 308), 오른쪽 check 0 / observed 0 (열 303 = 303)
- C2 넘침 없음 | 12/12 (scrollWidth = 화면 너비, scrollX 0) | 4 sizes x 3 states, light | rendered | 320x800 200자: check scrollWidth 320 / observed 캡처의 `200 / 200` 잉크 오른쪽 끝 열 303, 오른쪽 여백 16px
- AC-002 글자 수 문구 | 12/12 (`0 / 200`, `199 / 200`, `200 / 200`) | 4 sizes x 3 states, light | rendered | 320x800 200자: check `200 / 200` / observed 캡처에서 `200 / 200`
- 기존 요소 위치 전후 비교 | 제목·라벨·두 칸 위치 같음, 보내기 버튼만 22px 아래 | 2 sizes x 1 state, light | rendered | not spot-checked

## Display before/after

- before: 보내기 버튼 | 보내기 | 요청 화면, 폼 맨 아래
- after: 보내기 버튼 | 보내기 | 요청 화면, 폼 맨 아래

보내기 버튼은 글자 수 표시가 들어가며 아래로 밀린 것으로, 보이는 내용과 찾아가는 길은 같습니다.
report-check: ok 2,000 chars d83025a9
