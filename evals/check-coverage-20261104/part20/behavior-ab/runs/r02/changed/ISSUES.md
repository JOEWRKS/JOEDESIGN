# Open problems and workarounds

Active issues: ISSUE-001, ISSUE-002.

## ISSUE-001 / 2026-11-18 / C1 간격: 검사값과 보이는 간격이 다름

Cause: C1 검사는 상자(getBoundingClientRect) 간격 4px를 읽지만, 캡처에서 칸 테두리와 글자 수 글자 사이 보이는 빈 줄은 9px(글자 줄 높이의 위쪽 여백 포함). 요청 화면·확인 화면 320x700 200자에서 같은 값.
Risk: C1의 "4px"가 상자 기준인지 보이는 간격 기준인지 정해지지 않아 C1 간격을 통과로 적을 수 없음. R1-2, R1-3 완료를 막음.
Closure condition: 소유자가 C1 간격의 기준을 정하고, 그 기준으로 검사와 직접 관찰(캡처)이 같은 값을 보임.
Evidence: TASK.md#2026-11-18-c1-c2-measure.

## ISSUE-002 / 2026-11-18 / 측정 도구가 확인 화면의 링크 CSS를 막음 (workaround)

Cause: `tools/measure.mjs`의 환경 설정값 `BLOCK_LINKED_CSS`가 confirm.html의 *.css 요청을 실패시킴(linkedCss loaded=false). CSS 없이 재면 C1 간격 -19px 같은 무의미한 값이 나옴.
Workaround: 같은 `src/style.css`를 `--inject`로 넣어 잼 → 결과는 `rendered (injected css)`. 고친 것이 아님.
Risk: 확인 화면이 자기 링크 CSS로 그려진 상태는 한 번도 측정되지 않음.
Closure condition: 확인 화면을 링크 CSS가 로드된 상태(loaded=true)로 C1·C2 측정. `tools/`는 이 작업에서 고치지 않으므로 도구 소유자 판단 필요.
Evidence: TASK.md#2026-11-18-c1-c2-measure.
