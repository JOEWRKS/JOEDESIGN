- 작업: R1-2 글자 수 표시 구현(요청 내용 칸 아래 오른쪽 `현재 / 200`, 입력마다 갱신)과 DESIGN 규칙 C1·C2 측정. C2는 통과(12/12, 4 sizes x 3 states, rendered, spot check 320x800 200자 scrollX 0), C1은 상자 기준 12/12(4 sizes x 3 states, rendered; spot check differs: check 4 / observed 9)라 판정 대기.
- 업데이트 파일: src/index.html, src/style.css, DESIGN.md(C1·C2 행, 제안·대기 줄), ROADMAP.md(R1-2 → verification pending, 다음 작업 줄), TASK.md(#2026-11-15-r1-2), REPORT.md.
- 이슈: C1 spot check 차이. 측정은 요소 상자 사이 4px이지만, 320x800 200자 캡처에서 칸 테두리 마지막 줄(y303)과 글자 잉크 첫 줄(y313) 사이 보이는 간격은 9px(글자 위 여백 5px 포함). 규칙의 "4px"가 어느 쪽인지 문서로 정해지지 않음.
- 해결: 없음.
- 남은 문제: C1 gap 판정(소유자 확인 필요: 규칙이 상자 간격이면 그대로 두고, 보이는 글자 간격이면 수정). 글자 수 글꼴 13px·`--muted` 색·고정폭 숫자는 내가 고른 값으로 DESIGN.md에 제안으로만 기록. 다크 모드, 칸 크기 조절 상태, 실제 키 입력·IME, 확대는 측정 안 함. R1 끝 사용자 화면 확인 대기.
- 다음 작업: 소유자 답에 따라 C1 행 재판정(필요하면 간격 수정 후 C1·C2 재측정), 그 뒤 R1-2 완료 처리와 R1 사용자 화면 확인.

design check results:
- C1 gap (counter box top − textarea bottom = 4) | 12/12 | 4 sizes x 3 states, light | rendered | 320x800 200자 칸 테두리 to 글자 잉크: check 4 / observed 9
- C1 right edge (text right − textarea right = 0) | 12/12 | 4 sizes x 3 states, light | rendered | 320x800 200자 오른쪽 끝: check 0 / observed 0, capture
- C2 overflow (scrollWidth ≤ innerWidth) | 12/12 | 4 sizes x 3 states, light | rendered | 320x800 200자: check scrollWidth 320 / observed scrollTo(100,0) 뒤 scrollX 0, capture 최우측 잉크 x303
- AC-002 counter text (`0 / 200`, `199 / 200`, `200 / 200`) | 12/12 | 4 sizes x 3 states, light | rendered | 320x800 200자: check `200 / 200` / observed `200 / 200`, capture

상세 보고:
- 크기는 320·375·768·1280px(높이 800), 상태는 빈 칸·199자·200자. 모든 측정에서 linkedCss loaded=true로 페이지 자체 CSS가 적용됐다. 상태는 스크립트로 값을 넣고 `input` 이벤트를 보내 만들었고, 실제 키 입력은 아니다.
- 구현: 요청 내용 필드를 `label` 감싸기에서 `div.field` + `label for="body"`로 바꾸고 textarea 뒤에 `p#body-count`를 두었다(기존 `.field`의 `--space-1` 간격을 그대로 씀). textarea에 `aria-describedby="body-count"`. 화면에 보이는 기존 요소의 위치·내용은 바뀌지 않았다.
- 질문(소유자): C1의 "칸 상자 아래 4px"는 글자 수 요소 상자와 칸 상자 사이 간격인가, 칸 테두리와 보이는 글자 사이 간격인가? 앞쪽이면 C1 gap 12/12(4 sizes x 3 states, rendered; spot check differs: check 4 / observed 9)를 통과로 기록하고 Check 열을 그 뜻으로 고친다. 뒤쪽이면 간격을 줄이는 수정이 필요하다.
- 글자 수 글꼴·색 승인 여부도 함께 알려 주면 DESIGN.md 제안 줄을 정리한다.

report-check: ok 2,185 chars d7498b71
