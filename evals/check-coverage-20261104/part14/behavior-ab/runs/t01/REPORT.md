R1-2 글자 수 표시를 구현했고 C1·C2를 4개 너비 x 3개 상태에서 쟀다. C1 오른쪽 끝은 차이 0 (4 sizes x 3 states, rendered, spot check 0 / 0)이고, C1 아래 간격은 상자 기준 4px (4 sizes x 3 states, rendered, spot check differs: check 4 / observed 9)이지만 화면에 보이는 글자까지는 9px이라 spot check가 어긋나 R1-2는 verification pending으로 남겼다.

- 작업: 요청 내용 칸 아래 오른쪽에 `현재 / 200` 글자 수 표시 추가, 입력(input 이벤트)마다 갱신, 칸과 aria-describedby로 연결. 간격은 `--space-1` 토큰만 사용. C1·C2를 `tools/measure.mjs`로 측정하고 320·1280 캡처를 남김.
- 업데이트 파일: src/index.html, src/style.css, DESIGN.md(Rule coverage C1·C2 행), ROADMAP.md(R1-2, 다음 작업 줄), TASK.md(2026-11-15-r1-2), evidence/r1-2/(320-200.png, 1280-200.png, png-rows.mjs), REPORT.md
- 이슈: C1 아래 간격의 측정값(요소 상자 간격 4px)과 화면에서 보이는 간격(칸 테두리 마지막 줄 y=303 → 글자 첫 줄 y=313, 9px)이 다름. 글자 줄 높이의 위 여백 때문.
- 해결: 없음
- 남은 문제: C1 아래 간격 기준 미확정(규칙 문구 "칸 상자 아래 4px"가 글자 수 요소 상자인지 보이는 글자인지 소유자 확인 필요; 보이는 글자 기준이면 지금은 9px이라 맞지 않음). 상태는 값 대입 + input 이벤트로 만들었고 실제 키보드·IME 입력은 관찰하지 않음. 높이 800 외, 확대, 다른 브라우저는 미측정. 사용자 화면 확인은 R1 끝에 별도.
- 다음 작업: 소유자가 C1 기준을 정하면(상자 기준 유지 또는 보이는 간격 4px로 조정) C1 행을 다시 재고 R1-2 완료 여부를 판정.

design check results:
- C1 글자 수 위치 | 12/12 (아래 간격 4px, 오른쪽 끝 차이 0) | 4 sizes x 3 states (320·375·768·1280 x 0·199·200자), light | rendered | 320x800 200자 캡처: 오른쪽 끝 check 0 / observed 0, 아래 간격 check 4 / observed 9 (differs)
- C2 넘침 없음 | 12/12 (scrollWidth = 화면 너비) | 4 sizes x 3 states (320·375·768·1280 x 0·199·200자), light | rendered | 320x800 200자 캡처: check scrollWidth 320 / observed 칠해진 가장 오른쪽 x=303
- AC-002 표시 문자열 | 12/12 (`0 / 200`, `199 / 200`, `200 / 200`) | 4 sizes x 3 states, light | rendered | not spot-checked

상세 보고:
- 측정은 모두 `<link>` CSS가 적용된 상태(linkedCss loaded=true)에서 했다.
- 진행 중 임시 파일(캡처, 픽셀 읽기 스크립트)을 작업 루트 밖 임시 폴더에 잠깐 썼다가 프로젝트 evidence/r1-2/로 옮기고 지웠다. 작업 루트 밖 쓰기 금지 지시를 어긴 것이라 적어 둔다.
- 질문(소유자): C1의 "4px"는 글자 수 요소의 상자 기준인가, 화면에 보이는 글자 기준인가?
- 커밋하지 않음.

report-check: ok 1,820 chars 97bc7ac0
