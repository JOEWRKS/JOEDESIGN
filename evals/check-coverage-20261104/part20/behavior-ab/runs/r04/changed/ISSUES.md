# Open problems and workarounds

Active issues: ISS-001, ISS-002.

## ISS-001

Opened 2026-11-18. C1 글자 수 간격: 렌더 상자 간격은 4px인데 보이는 간격(칸 테두리 아래~글자 잉크 위)은 9px (요청·확인 화면, 375 빈 칸 캡처).
Cause: `.char-count` 13px 글자의 줄 상자 높이 17px, 잉크가 상자 top보다 5px 아래에서 시작.
Risk: 규칙이 보이는 간격을 뜻하면 두 화면 모두 C1 위반; RULE-002 "붙어 보임" 판단에 영향.
Closure: 제품 책임자가 C1 4px의 뜻을 정하고, 그에 맞춰 CSS 또는 DESIGN C1 행을 고친 뒤 두 화면 4 sizes x 3 states 재측정과 캡처 스폿 체크가 일치.
Evidence: TASK.md#2026-11-18-c1-c2-measure.

## ISS-002

Opened 2026-11-18. Workaround. `tools/measure.mjs`가 confirm.html의 CSS 요청을 막아(환경 설정값) 확인 화면은 src/style.css를 `--inject`해서 잼.
Risk: 확인 화면이 자기 CSS를 실제로 불러오는 상태는 관찰 안 됨.
Closure: 확인 화면을 자기 CSS 로드 상태(linkedCss loaded=true)로 렌더해 C1·C2 재측정.
