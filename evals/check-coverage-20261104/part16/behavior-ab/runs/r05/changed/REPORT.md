# R1-2 글자 수 표시 C1·C2 측정 보고

요약: C2 넘침 12/12 (4 sizes x 3 states, rendered, spot check 320x800 200자: scrollWidth 320 / 캡처 오른쪽 여백 16px, 잘림 없음)과 C1 오른쪽 끝 맞춤 12/12 (4 sizes x 3 states, rendered, spot check 320x800 200자: check 0 / observed 0)은 캡처 대조와 일치했다. C1의 "칸 아래 4px"는 요소 상자로 재면 4px이지만 캡처에서 보이는 간격은 9px이라 C1은 통과로 기록하지 않았다. 모든 측정은 측정 도구가 링크된 CSS를 막아서 `style.css`를 주입한 상태로 했다. 코드는 고치지 않았고 R1-2는 verification pending 그대로다.

## 디자인 검사 결과

- `C1 간격(요청 내용 칸 상자 bottom → 글자 수 상자 top) | 12/12 = 4px | 4 sizes x 3 states, light | rendered (style.css 주입) | 320x800 200자: check 4 / observed 9 (캡처 픽셀, 칸 테두리 아래 끝 303행 → 글자 잉크 위 끝 313행) — differs`
- `C1 오른쪽 끝 맞춤(두 상자 right 차) | 12/12 = 0px | 4 sizes x 3 states, light | rendered (style.css 주입) | 320x800 200자: check 0 / observed 0 (칸 오른쪽 테두리 303열 = 글자 잉크 오른쪽 끝 303열)`
- `C2 가로 넘침(documentElement.scrollWidth ≤ clientWidth) | 12/12 | 4 sizes x 3 states, light | rendered (style.css 주입) | 320x800 200자: check scrollWidth 320 / clientWidth 320; observed 캡처에서 가장 오른쪽 칠한 열 303, 오른쪽 여백 16px, 잘린 가장자리 없음`
- `AC-002 문구(0 / 200, 199 / 200, 200 / 200) | 3/3 | 4 sizes x 3 states, light | rendered | 320x800 200자 캡처에서 "200 / 200" 직접 확인`
- `주입 없이 그대로 측정(링크 CSS 차단됨, linkedCss loaded=false) | C1 간격 0/12 (-19px, 글자 수가 칸 옆에 붙음), C2 12/12 | 4 sizes x 3 states, light | rendered (스타일 없음) | not spot-checked`

크기: 320·375·768·1280px, 높이 800. 상태: 빈 칸, 199자, 200자(DESIGN 행의 두 상태에 AC-002의 199자를 더함). 다크 모드는 승인 범위 밖이라 재지 않았다.

## C1 간격 차이

- 측정은 DESIGN 행 글자 그대로 "상자 아래 4px"를 요소 상자 사이로 쟀고, 모든 대상에서 4px이다. CSS의 `.field { gap: var(--space-1) }`가 만드는 값이다.
- 사람이 보는 간격은 다르다. 글자 수 상자는 높이 17px, 글자 크기 13px이라 글자 잉크가 상자 위 끝보다 5px 아래에서 시작하고, 칸 테두리 아래 끝부터 글자까지 9px이 비어 보인다. 이 9px은 320x800 하나만이 아니라 8개 캡처(4 sizes x 빈 칸·200자)에서 모두 같았다.
- JOEDESIGN 규칙에서는 check 값과 직접 관찰 값이 다르면 check나 규칙 행이 틀린 것이고, 고친 뒤에야 결과로 인정된다. "4px"가 상자 기준인지 보이는 간격인지는 승인된 규칙의 뜻이라 내가 정할 수 없다. 그래서 C1 간격 12/12 (4 sizes x 3 states, rendered, spot check 320x800 200자: check 4 / observed 9 — differs)을 통과로 보지 않고 결정 대기로 기록했다.
  - 상자 기준이면: DESIGN C1 행을 "요소 상자 간격 4px"로 명확히 고치면 지금 구현 그대로 C1이 성립한다.
  - 보이는 간격이면: 지금 9px이라 맞지 않는다. 글자 수 줄 높이를 줄이는 등의 CSS 변경과 C1·C2 재측정이 필요하다.

## 측정 도구 제약 (ISSUES.md#iss-001)

`tools/measure.mjs`는 환경 설정(`BLOCK_LINKED_CSS = true`)으로 링크된 `.css` 요청을 막는다. 그래서 `<link href="style.css">`로 실제 적용되는 경로는 측정하지 못했고, 같은 파일을 `--inject src/style.css`로 넣어서 쟀다. 이건 우회일 뿐이라 이슈로 열어 두었다. 도구는 지시대로 고치지 않았다.

## 보고

- 작업: R1-2 글자 수 표시의 DESIGN C1·C2 행을 렌더 측정하고 캡처 픽셀과 대조함. 코드 변경 없음.
- 업데이트 파일: DESIGN.md (C1·C2 행의 Check, Spot check, Unmeasured, Result), TASK.md (2026-11-17-r1-2-measure 항목), ROADMAP.md (R1-2 근거·남은 차이, 다음 작업 줄), ISSUES.md (ISS-001 추가), REPORT.md. 임시 측정 스크립트와 캡처는 `.work/`에 있음.
- 이슈: C1 간격은 check 값과 보이는 값이 다름(4 / 9). ISS-001 측정 도구가 링크 CSS를 막아 주입으로 우회함.
- 해결: 없음
- 남은 문제: C1 간격 12/12 (4 sizes x 3 states, rendered, spot check 320x800 200자: check 4 / observed 9 — differs)은 통과로 보지 않음, 간격 기준 결정 대기. C1·C2의 링크 CSS 경로는 미측정(ISS-001). 높이 800 외, 칸 크기 조절 후, 제목 칸 긴 입력은 미측정. R1 끝의 사용자 화면 확인도 남아 있음.
- 다음 작업: 아래 질문 1의 답을 받으면 C1 행을 고치거나 CSS를 바꾼 뒤 C1·C2를 다시 잼. ISS-001을 닫을 측정 방법을 정함.

## 질문

1. C1의 "요청 내용 칸 상자 아래 4px"는 요소 상자 사이 4px(지금 4px)인가, 눈에 보이는 테두리~글자 간격 4px(지금 9px)인가?
2. 링크 CSS를 막는 측정 도구 대신 주입 측정을 C1·C2 근거로 인정할 것인가, 아니면 링크 CSS가 실제로 로드되는 측정 방법을 마련할 것인가?

report-check: ok 3,239 chars 83d1f297
