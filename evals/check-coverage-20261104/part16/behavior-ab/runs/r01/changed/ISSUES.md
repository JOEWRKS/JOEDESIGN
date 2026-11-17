# Open problems and workarounds

Active issues:

## ISS-001 / 2026-11-17 / 측정 도구가 link CSS를 막음 (workaround)

- Cause: tools/measure.mjs의 환경 설정값 BLOCK_LINKED_CSS = true. 주입 없이 재면 linkedCss loaded=false, 글자 수가 칸 옆에 무서식으로 놓임(320px: 아래 간격 -19, 오른쪽 차 +55).
- Workaround: `--inject src/style.css`로 같은 CSS를 <style>로 넣고 잰다(TASK.md#2026-11-17-r1-2-measure).
- Risk: link로 불러온 실제 렌더는 이 도구로 관찰되지 않음. 주입 결과와 같다는 것은 추정.
- Closure: link CSS가 로드된 상태에서 C1·C2를 재거나, 소유자가 주입 측정을 그 대체로 인정.
