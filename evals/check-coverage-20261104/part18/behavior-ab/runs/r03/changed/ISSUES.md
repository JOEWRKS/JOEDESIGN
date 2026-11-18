# Open problems and workarounds

Active issues: ISS-001.

## ISS-001 / 2026-11-18 / 미리보기가 확인 화면의 링크 CSS를 막음

Cause: tools/measure.mjs가 confirm.html의 *.css 요청을 막는다(BLOCK_LINKED_CSS, 환경 설정값, 수정 금지). linkedCss loaded=false.
Workaround: `--inject src/style.css`로 같은 CSS를 넣어 측정. 실제 브라우저에서 링크 CSS로 그린 화면과 같다는 관찰은 없다.
Risk: 확인 화면의 C1·C2 결과는 주입 CSS 기준이며 자기 CSS 렌더는 미측정.
Closure: 확인 화면을 자기 링크 CSS로 렌더해 C1·C2 재측정(측정 환경 변경은 소유자 결정).
