# Open problems and workarounds

Active issues: ISS-001.

## ISS-001

- 문제: `tools/measure.mjs`가 링크된 CSS를 막는다(`BLOCK_LINKED_CSS = true`, 출력 `linkedCss loaded=false`). 그대로 재면 스타일 없는 화면이 측정된다(C1 간격 -19px).
- 우회: `--inject src/style.css`로 같은 CSS를 넣어 측정. 우회일 뿐 해결 아님.
- 위험: `<link href="style.css">`가 실제로 적용되는지는 측정되지 않음.
- 닫는 조건: `linkedCss loaded=true` 상태(또는 사용자가 인정한 다른 방법)에서 C1·C2 행을 다시 재서 같은 결과.
- 기록: TASK.md#2026-11-17-r1-2-measure.
