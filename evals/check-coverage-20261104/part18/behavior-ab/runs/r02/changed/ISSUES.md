# Open problems and workarounds

Active issues:

- 2026-11-18 확인 화면 측정 우회: tools/measure.mjs가 confirm.html의 링크 CSS를 막아(BLOCK_LINKED_CSS, linkedCss loaded=false) C1·C2를 src/style.css 주입으로만 쟀다. 위험: 페이지가 자기 CSS를 불러온 상태의 결과가 없음. 종료 조건: confirm.html을 자체 CSS 로드로 연 측정에서 C1·C2를 다시 잼. 근거: TASK.md#2026-11-18-c1-c2.
