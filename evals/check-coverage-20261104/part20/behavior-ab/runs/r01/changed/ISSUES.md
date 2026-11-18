# Open problems and workarounds

Active issues: ISS-001, ISS-002.

## ISS-001 / 2026-11-18 / 확인 화면 링크 CSS를 측정 도구가 막음 (workaround)

Cause: `tools/measure.mjs`의 환경 설정 `BLOCK_LINKED_CSS = /confirm\.html$/`가 확인 화면의 `style.css` 요청을 실패시킨다. CSS 없이 재면 C1이 0/8(간격 -19px, 오른쪽 차 -55~-73px)로 나온다.
Workaround: `--inject src/style.css`로 같은 CSS를 넣어 잼. 결과 줄은 `rendered (injected css)`.
Risk: 확인 화면이 실제로 자기 링크 CSS를 읽은 상태는 관찰되지 않았다.
Closure condition: 확인 화면을 링크 CSS가 읽히는 상태(linkedCss loaded=true)로 렌더해 C1·C2를 다시 재고 spot check가 맞음. 또는 책임자가 주입 CSS 측정을 R1-3 Check로 인정.
Links: TASK.md#2026-11-18-c1-c2-measure.

## ISS-002 / 2026-11-18 / C1 간격 spot check 불일치 (규칙 뜻 확인 대기)

Cause: C1 Check(렌더 상자 간격)는 4px, 캡처에서 보이는 간격(textarea 아래 테두리 ~ 글자 수 글자 잉크 위)은 9px. 차이는 13px 글자의 줄 높이 안 위쪽 여백(상자 top 308, 잉크 top 313, 요청 화면 320x800 200자).
Risk: 규칙이 "보이는 간격 4px"를 뜻하면 C1 간격은 실패, "상자 간격 4px"를 뜻하면 Check가 맞다. 어느 쪽인지 정해지기 전에는 C1을 통과로 적지 않는다.
Closure condition: 책임자가 C1의 4px가 상자 기준인지 보이는 간격 기준인지 정하고, 그 기준으로 Check·spot check가 맞음.
Links: DESIGN.md#rule-coverage C1, TASK.md#2026-11-18-c1-c2-measure.
