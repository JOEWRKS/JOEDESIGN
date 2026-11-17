# Open problems and workarounds

Active issues: I-001.

## I-001

Opened: 2026-11-17. Item: ROADMAP R1-2, DESIGN.md#rule-coverage C1.
Problem: C1 "칸 상자 아래 4px"를 상자로 재면 4px이지만, 칸 테두리 아래 끝에서 글자 수 숫자 위 끝까지 눈에 보이는 빈 간격은 9px (320x900 200자 캡처; 네 너비·세 상태 모두 같은 상자 값).
Cause: `.char-count`(13px, line-height normal)의 줄 상자가 17px이라 숫자 잉크가 상자 top보다 약 5px 아래에서 시작한다.
Risk: 규칙이 보이는 간격을 뜻한다면 C1은 실패이고, 상자 간격을 뜻한다면 Check는 맞고 규칙 문구가 불명확하다.
Closure condition: 디자인 소유자가 C1의 4px이 상자 간격인지 보이는 간격인지 정하고, 그에 맞게 Check(또는 승인된 CSS)를 고친 뒤 C1 행을 다시 재어 spot check가 일치할 것.
Workaround: none.
