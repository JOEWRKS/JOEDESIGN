R1-2 글자 수 표시를 구현했습니다. C1은 상자 측정과 직접 관찰이 어긋나 통과로 적지 않았고(4 sizes x 3 states, rendered; spot check differs: check 4 / observed 7), C2는 넘침이 없습니다(4 sizes x 3 states, rendered; spot-checked 320x800 200자). R1-2는 verification pending입니다.

- 작업: 요청 내용 칸 아래 오른쪽에 `현재 / 200` 표시(`#body-count`)를 추가하고, 입력할 때마다 갱신하게 했습니다. 표시는 14px·`--muted` 색·줄높이 1이고, 칸과의 간격은 `.field`의 `--space-1` 간격을 그대로 씁니다. 칸 묶음은 `<label>` 감싸기에서 `<div>` + `<label for>`로 바꿨고, 칸에 `aria-describedby`로 표시를 연결했습니다. 그다음 DESIGN 규칙 C1·C2를 `tools/measure.mjs`로 4개 너비 x 3개 상태에서 재고, 320x800 200자 캡처의 픽셀로 직접 대조했습니다.
- 업데이트 파일: src/index.html, src/style.css, DESIGN.md(C1·C2 행의 Check·Spot check·Unmeasured·Result), ROADMAP.md(R1-2 → verification pending, 다음 작업 줄), TASK.md(2026-11-15-r1-2).
- 이슈: C1 "칸 상자 아래 4px"의 기준이 정해지지 않았습니다. 요소 상자 사이는 4px인데, 화면에서 칸 테두리부터 숫자 글자까지 보이는 간격은 7px입니다(320x800 200자 캡처). 글자의 위아래 여백 때문이며, 토큰 규칙(`--space-*`만 사용) 안에서는 보이는 간격을 4px로 줄일 수 없습니다.
- 해결: 없음(이번 턴은 신규 구현, 고친 결함 없음).
- 남은 문제: (1) C1은 not passed. 아래 간격 기준을 소유자가 정해야 합니다: 요소 상자 4px이면 C1 행 문구에 "상자 기준"을 적고 다시 판정하고, 보이는 간격 4px이면 토큰 밖 값이나 규칙 변경이 필요합니다. 오른쪽 끝 맞춤은 상자와 캡처 모두 0px 차이입니다. (2) 글자 수는 `value.length`로 셉니다. `maxlength`와 같은 단위라 표시가 200을 넘지 않지만, 이모지 같은 일부 문자는 2자로 셉니다. PRODUCT.md는 세는 방식을 정하지 않았으므로 소유자 확인 전까지 R1-2는 열어 둡니다. (3) 포커스·오류 상태, 사용자가 칸 크기를 바꾼 상태, 확대는 재지 않았습니다. (4) R1 끝 사용자 화면 확인은 별도로 남아 있습니다.
- 다음 작업: 위 두 질문에 대한 소유자 답을 받아 C1 행을 고치거나 재판정하고, R1-2를 complete로 올릴지 결정합니다.

결과 목록:

- `C1 글자 수 위치(상자 측정) | 12/12 (아래 간격 4, 오른쪽 차 0) | 4 sizes x 3 states (빈 칸·199자·200자), light | rendered | differs: 320x800 200자 아래 간격 check 4 / observed 7, 오른쪽 끝 check 0 / observed 0 (캡처 픽셀)`
- `C2 가로 넘침 없음 | 12/12 (scrollWidth = 화면 너비) | 4 sizes x 3 states (빈 칸·199자·200자), light | rendered | 320x800 200자: check scrollWidth 320 / observed scrollTo(200,0) 뒤 scrollX 0, 캡처 오른쪽 내용 끝 304px`
- `AC-002 표시 문구 | 12/12 ("0 / 200", "199 / 200", "200 / 200") | 4 sizes x 3 states, light | rendered | 320x800 200자: check "200 / 200" / observed 캡처에 "200 / 200"`
- `입력 갱신(편집 입력) | 2/2 (insertText 5자 → "5 / 200", delete → "4 / 200") | 1 size x 2 states, light | rendered | not spot-checked`

질문(사용자 부재로 여기에 적습니다):
1. C1의 "아래 4px"는 요소 상자 사이 간격인가요, 눈에 보이는 간격인가요?
2. 글자 수를 `maxlength`와 같은 방식(이모지 2자)으로 세도 되나요?

report-check: ok 2,214 chars afb1822d
