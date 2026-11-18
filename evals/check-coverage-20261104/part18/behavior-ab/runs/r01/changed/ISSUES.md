# Open problems and workarounds

Active issues: ISS-001.

## ISS-001

Opened: 2026-11-18. Status: open (workaround).
Problem: tools/measure.mjs가 confirm.html의 링크 CSS(style.css)를 막는다(linkedCss loaded=false). 막힌 채 재면 C1 값이 무의미(간격 -19px).
Workaround: 같은 src/style.css를 `--inject`로 넣어 확인 화면 C1·C2를 잼(TASK.md#2026-11-18-c1-c2).
Risk: 실제 링크 CSS로 읽은 렌더와 다를 수 있음(측정 안 됨).
Closure: 확인 화면을 자기 링크 CSS가 읽힌 상태(loaded=true)로 C1·C2 다시 측정.
