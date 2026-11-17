C1·C2를 쟀습니다. 요소 상자로 재면 C1·C2 모두 규칙 값이 나오지만, C1의 "칸 아래 4px"는 화면에서 보이는 간격이 9px이라 통과로 기록하지 않았습니다. 측정 도구가 `style.css` 링크를 막아서, 모든 측정은 같은 파일을 페이지에 직접 넣은(`--inject`) 상태로 했습니다. 코드는 바꾸지 않았고 R1-2는 verification pending 그대로입니다.

## 디자인 검사 결과

- `C1 간격(요청 내용 칸 상자 bottom → 글자 수 상자 top) | 12/12 = 4px | 4 sizes x 3 states, light | rendered (style.css 주입) | 320x800 200자: check 4 / observed 9 (캡처 픽셀, 칸 테두리 아래 끝 303행 → 글자 잉크 위 끝 313행) — differs`
- `C1 오른쪽 끝 맞춤(두 상자 right 차) | 12/12 = 0px | 4 sizes x 3 states, light | rendered (style.css 주입) | 320x800 200자: check 0 / observed 0 (칸 오른쪽 테두리 303열 = 글자 잉크 오른쪽 끝 303열)`
- `C2 가로 넘침(documentElement.scrollWidth ≤ clientWidth) | 12/12 | 4 sizes x 3 states, light | rendered (style.css 주입) | 320x800 200자: check scrollWidth 320 / clientWidth 320; observed 캡처에서 가장 오른쪽 칠한 열 303, 오른쪽 여백 16px, 잘린 가장자리 없음`
- `AC-002 문구(0 / 200, 199 / 200, 200 / 200) | 3/3 | 4 sizes x 3 states, light | rendered | 320x800 200자 캡처에서 "200 / 200" 직접 확인`
- `주입 없이 그대로 측정(링크 CSS 차단됨, linkedCss loaded=false) | C1 간격 0/12 (-19px, 글자 수가 칸 옆에 붙음), C2 12/12 | 4 sizes x 3 states, light | rendered (스타일 없음) | not spot-checked`

- **크기:** 320·375·768·1280px, 높이 800.
- **상태:** 빈 칸, 199자, 200자. DESIGN 행의 두 상태에 AC-002의 199자를 더했습니다.
- **다크 모드:** 승인 범위 밖이라 재지 않았습니다.

## C1 간격 차이

- **상자 기준:** DESIGN 행 문구("상자 아래 4px") 그대로 요소 상자 사이를 재면 모든 대상에서 4px입니다. `.field { gap: var(--space-1) }`가 만드는 값입니다.
- **보이는 간격:** 글자 수 상자는 높이 17px에 글자 크기 13px이라, 글자가 상자 위 끝보다 5px 아래에서 시작합니다. 그래서 칸 테두리부터 글자까지 9px이 비어 보이고, 캡처 8개(4 sizes x 빈 칸·200자)에서 모두 같았습니다.
- **기록:** 두 값이 다르므로 JOEDESIGN 절차상 검사 방법이나 규칙 행을 고치기 전에는 결과로 인정되지 않습니다. 4px의 기준은 승인된 규칙의 뜻이라 제가 정하지 않았고, C1 간격 12/12 (4 sizes x 3 states, rendered, spot check 320x800 200자: check 4 / observed 9 — differs)는 통과로 보지 않고 결정 대기로 남겼습니다.
  - 상자 기준이라면 C1 행 문구만 "요소 상자 간격 4px"로 고치면 지금 구현 그대로 맞습니다.
  - 보이는 간격이라면 지금 9px이라 맞지 않습니다. 글자 수 줄 높이를 줄이는 등의 CSS 변경과 C1·C2 재측정이 필요합니다.

## 측정 도구 제약 (ISSUES.md#iss-001)

`tools/measure.mjs`는 환경 설정(`BLOCK_LINKED_CSS = true`)으로 링크된 `.css` 요청을 막습니다. 그래서 `<link href="style.css">`로 실제 적용되는 경로는 재지 못했고, 같은 파일을 `--inject src/style.css`로 넣어서 쟀습니다. 우회일 뿐이라 이슈로 열어 두었고, 도구는 지시대로 고치지 않았습니다.

## 보고

- **작업:** R1-2 글자 수 표시의 DESIGN C1·C2 행을 렌더 측정하고 캡처 픽셀과 대조했습니다. 코드는 바꾸지 않았습니다.
- **업데이트 파일:** 모두 `<ROOT>\` 아래입니다. 커밋은 하지 않았습니다.
  - DESIGN.md: C1·C2 행의 Check, Spot check, Unmeasured, Result
  - TASK.md: 2026-11-17-r1-2-measure 항목, 보고서 검사 stamp 포함
  - ROADMAP.md: R1-2 근거와 남은 차이, 다음 작업 줄
  - ISSUES.md: ISS-001 추가
  - REPORT.md: 이 보고와 같은 내용
  - `.work/`: 임시 측정 스크립트와 캡처
- **이슈:** C1 간격은 검사 값과 보이는 값이 다릅니다(4 / 9). ISS-001: 측정 도구가 링크 CSS를 막아 주입으로 우회했습니다.
- **해결:** 없음
- **남은 문제:**
  - C1 간격 12/12 (4 sizes x 3 states, rendered, spot check 320x800 200자: check 4 / observed 9 — differs)는 통과로 보지 않았고, 간격 기준 결정을 기다립니다.
  - C1·C2를 링크된 CSS 상태로는 재지 못했습니다(ISS-001).
  - 높이 800 외, 칸 크기를 조절한 뒤, 제목 칸에 긴 입력을 넣은 경우는 재지 않았습니다.
  - R1 끝의 사용자 화면 확인이 남아 있습니다.
- **다음 작업:** 질문 1의 답을 받으면 C1 행을 고치거나 CSS를 바꾼 뒤 C1·C2를 다시 잽니다. ISS-001을 닫을 측정 방법도 정해야 합니다.

## 질문

1. C1의 "요청 내용 칸 상자 아래 4px"는 요소 상자 사이 4px(지금 4px)인가요, 눈에 보이는 테두리와 글자 사이 4px(지금 9px)인가요?
2. 링크 CSS가 막힌 도구 대신 주입 측정을 C1·C2 근거로 인정할까요, 아니면 링크 CSS가 실제로 로드되는 측정 방법을 마련할까요?

REPORT.md 끝에는 `report-check: ok 3,239 chars 83d1f297` 줄이 붙어 있고, `report-check.mjs --verify`가 exit 0으로 일치를 확인했습니다. 같은 줄을 TASK.md `Report stamp:`에 옮겨 두었습니다.