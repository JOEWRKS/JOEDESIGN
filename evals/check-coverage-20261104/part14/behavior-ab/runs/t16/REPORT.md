R1-2 글자 수 표시 구현과 DESIGN C1·C2 측정 보고

- 작업: 요청 내용 칸 아래 오른쪽에 `현재 / 200` 글자 수를 넣고 입력마다 갱신하도록 구현(DEC-002). DESIGN C1·C2와 AC-002를 4개 너비 x 3개 상태에서 측정하고, 행마다 320x700 캡처로 spot check.
- 업데이트 파일: src/index.html, src/style.css, checks/r1-2-char-count.mjs(새 측정 스크립트), DESIGN.md(Token roles 표, Rule coverage C1·C2 행), ROADMAP.md(R1-2 → verification pending), TASK.md(2026-11-15-r1-2 항목).
- 이슈: C1 "칸 상자 아래 4px"의 기준이 불분명. 글자 수 요소의 상자는 칸 아래 4px이지만, 사람이 보는 글자 잉크는 칸 테두리 아래 8px(줄 높이 여백 포함).
- 해결: 없음(이번 턴은 새 구현이라 고친 결함 없음).
- 남은 문제: C1은 spot check가 다르게 나와 통과로 기록하지 않음(간격 check 4 / observed 8) → 제품 책임자 확인 대기. 글자 수 세는 방식은 내가 고름(`value.length`, `maxlength`와 같은 기준; 이모지는 2자로 셈) → 확인 대기. AC-002는 not spot-checked. 다크 모드·글꼴 확대·칸 높이 조절·Chrome 외 브라우저·실제 키 입력은 미측정. R1 사용자 화면 확인은 별도로 남음.
- 다음 작업: C1 기준 답을 받으면 (a) 상자 기준이면 C1 행 Check 유지·Result 갱신, (b) 보이는 글자 기준이면 줄 높이·간격 조정안을 내고 C1·C2 재측정. 그 뒤 R1 사용자 화면 확인.

design check results:
- C1 position (상자 간격 4px, 글자 오른쪽 끝 0px) | 12/12 | 4 sizes x 3 states, light | rendered | 320x700 200자: 간격 check 4 / observed 8 (differs); 오른쪽 끝 check 0 / observed 0
- C2 overflow (scrollWidth ≤ 화면 너비) | 12/12 | 4 sizes x 3 states, light | rendered | 320x700 200자: check scrollWidth 320 / observed 가장 오른쪽 잉크 x=303 of 320, 가로 스크롤바 없음
- AC-002 표시 문구 (`0 / 200`, `199 / 200`, `200 / 200`) | 12/12 | 4 sizes x 3 states, light | rendered | not spot-checked

## Display before/after
before: 보내기 버튼 | "보내기" | 폼 제출
after: 보내기 버튼 | "보내기" | 폼 제출
(글자 수 줄이 들어온 만큼 버튼이 아래로 내려갈 뿐 내용·경로는 같음.)

측정 범위: 너비 320, 375, 768, 1280 x 상태 빈 칸·199자·200자, 라이트 모드, `tools/measure.mjs`로 페이지가 자기 `style.css`를 실제로 불러온 상태(linkedCss loaded 12/12)에서 잼. 상태는 칸 값을 넣고 `input` 이벤트를 보내 만들었고, 실제 키보드 입력은 아님.

C1은 상자 기준 숫자가 12/12 (4 sizes x 3 states, rendered, spot check differs: 간격 check 4 / observed 8)이라 DESIGN 행에 "해석 확인 대기"로 적었음. 보이는 글자를 4px로 맞추려면 `--space-*` 토큰 밖 값(음수 여백이나 줄 높이 1 미만)이 필요해 토큰 규칙과 부딪히므로 지금은 바꾸지 않았음. C2는 12/12 (4 sizes x 3 states, rendered, spot check 320x700: check 320 / observed 잉크 x=303 of 320).

질문(제품 책임자):
1. C1의 "칸 상자 아래 4px"는 글자 수 요소 상자 기준(현재 그대로 맞음)인가, 보이는 글자 기준(현재 8px)인가?
2. 글자 수를 `maxlength`와 같은 방식으로 세도 되는가(이모지 1개 = 2자)?
3. 글자 수 글자 모양(14px, 이름표와 같은 회색, 오른쪽 정렬)은 이름표에 맞춰 내가 고른 것. 그대로 둘까?

report-check: ok 2,186 chars fa55ddaa
