# R1-2 글자 수 표시 보고

- 작업: 요청 내용 칸 아래 오른쪽에 글자 수 `현재 / 200` 표시를 구현했고(입력마다 갱신), DESIGN 규칙 C1·C2를 320·375·768·1280px에서 쟀다. R1-2는 verification pending으로 둔다.
- 업데이트 파일: src/index.html, src/style.css, DESIGN.md(Token roles, Rule coverage C1·C2 행, Proposed changes), ROADMAP.md(R1-2, 다음 작업), ISSUES.md(ISSUE-001), TASK.md(2026-11-15-r1-2), evidence/r1-2/ 캡처 4장.
- 이슈: C1 spot check가 어긋남. 상자 기준 간격은 4px인데 캡처에서 보이는 간격(칸 아래 테두리 → 첫 글자 픽셀)은 8px(ISSUES.md#issue-001).
- 해결: 없음
- 남은 문제: C1 미통과(4 sizes x 3 states, rendered, spot check differs: check 4 / observed 8), 규칙의 4px가 상자 간격인지 보이는 간격인지 결정 필요; 글자 수 모양(14px, `--muted` 색)은 내가 고른 값이라 미승인; 다크 모드·확대·칸 크기 조절 뒤는 미측정; 전문 검토(접근성 등)는 실행 안 함; R1 사용자 화면 확인 대기.
- 다음 작업: C1 뜻 결정 → check 또는 CSS 맞춘 뒤 C1 재측정 → R1-2 완료 판정 → R1 사용자 화면 확인.

design check results:
- C1 gap (상자 기준 top 차 = 4) | 12/12 | 4 sizes x 3 states, light | rendered | 320x800 200자 캡처: check 4 / observed 8 (differs)
- C1 right edge (right 차 = 0) | 12/12 | 4 sizes x 3 states, light | rendered | 320x800·1280x800 200자 캡처: check 0 / observed 0
- C2 overflow (scrollWidth ≤ 화면 너비) | 12/12 | 4 sizes x 3 states, light | rendered | 320x800 200자: check 320 ≤ 320 / observed 캡처 잉크 열 16–303, scrollTo(200,0) 뒤 scrollX 0
- AC-002 문구 (`0 / 200`, `199 / 200`, `200 / 200`) | 12/12 | 4 sizes x 3 states, light | rendered | 320x800 200자 캡처에서 `200 / 200` 보임
- 라벨→요청 내용 칸 간격 (구조 변경 전후) | 4 → 4 | 1 size x 1 state, light | rendered | not spot-checked

설명:

- 세 상태는 빈 칸, 199자, 200자다. 측정은 모두 `node tools/measure.mjs`로 했고 페이지가 자기 CSS를 불러왔다(linkedCss loaded true, 주입 없음).
- C1은 상자 기준으로 12곳 모두 4px·오른쪽 차 0이지만(4 sizes x 3 states, rendered, spot check differs: check 4 / observed 8), 보이는 글자까지의 간격은 8px이다. 글자 수 줄의 위 여백과 글꼴 자체의 위 여백 때문이다. `--space-*` 토큰만 쓴다는 규칙 안에서는 보이는 간격을 4px로 줄일 수 없다(음수 여백이 필요). 그래서 C1을 통과로 적지 않았다.
- C2는 12곳 모두 가로 넘침이 없다(4 sizes x 3 states, rendered, spot check agrees).
- 글자 수 표시가 라벨 안에 들어가 읽히지 않도록, 요청 내용 칸을 `<label for>` 구조로 바꾸고 `aria-describedby`로 연결했다. 보이는 배치는 그대로다(라벨→칸 간격 4 → 4).
- 질문: C1의 "상자 아래 4px"는 (a) 상자끼리의 간격인가요, (b) 보이는 글자까지의 간격인가요? (a)면 C1 check와 spot check 방법을 상자 기준으로 고쳐 다시 재고, (b)면 토큰 규칙 예외나 C1 값 변경을 정해 주셔야 합니다.
- 커밋하지 않았다.

report-check: ok 2,136 chars e9ce3222
