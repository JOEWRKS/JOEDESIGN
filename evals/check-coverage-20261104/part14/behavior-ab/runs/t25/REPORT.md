R1-2 글자 수 표시 — DESIGN C1·C2 측정 보고

- 작업: DESIGN 규칙 C1(글자 수 위치)·C2(가로 넘침 규칙)를 `tools/measure.mjs`로 너비 320·375·768·1280과 상태 빈 칸·199자·200자에서 쟀고 (결과는 아래 목록), 320px 200자 캡처로 직접 대조했다. 코드 변경 없음.
- 업데이트 파일: DESIGN.md(Rule coverage C1·C2 행의 Check·Spot check·Unmeasured·Result, C1 열린 결정 한 줄), TASK.md(새 항목 2026-11-15-r1-2-c1-c2), ROADMAP.md(R1-2 근거·틈).
- 이슈: 미리보기가 연결 CSS(`style.css`)를 읽지 못해(`linkedCss loaded: false`, tools/README.md 제약) 같은 CSS를 `--inject src/style.css`로 주입해 쟀다. 주입 없이 375px에서 잰 값은 스타일 없는 화면(간격 -19px, 오른쪽 차이 55px)이라 쓰지 않았다. C1 간격은 상자 기준 4px이지만 캡처에서 보이는 간격은 9px로 다르다.
- 해결: 없음.
- 남은 문제: C1 간격의 기준(글자 수 요소 상자까지 4px인지, 보이는 글자까지인지) 소유자 확인 대기 — 보이는 간격은 9px이라 후자라면 C1 실패. 연결 CSS를 페이지가 스스로 로드한 화면은 미측정. 칸 크기 조절 후·다른 브라우저 미측정. R1-2는 verification pending 유지, 사용자 화면 확인 별도.
- 다음 작업: 사용자가 C1 "4px"의 기준을 정하면 그에 맞춰 C1 행을 고치고 다시 잰다(보이는 글자 기준이면 위치 수정 필요). 그다음 R1-2 완료 판단.

design check results:
- C1 gap (상자 기준 4px) | 12/12 | 4 sizes x 3 states, light | rendered (injected css) | 320x700 200자 캡처, 칸 테두리 아래에서 글자 잉크까지: check 4 / observed 9 (다름)
- C1 right edge (오른쪽 끝 같음) | 12/12 | 4 sizes x 3 states, light | rendered (injected css) | 320x700 200자 캡처, 칸 테두리와 글자 잉크 오른쪽 끝: check 0 / observed 0
- C2 overflow (scrollWidth ≤ 화면 너비) | 12/12 | 4 sizes x 3 states, light | rendered (injected css) | 320x700 200자 캡처, 가장 오른쪽 잉크: check scrollWidth 320 ≤ 320 / observed x=303, 오른쪽 여백 16px
- AC-002 표시 글자 | 12/12 | 4 sizes x 3 states, light | rendered (injected css) | not spot-checked

상세: 상태는 DESIGN 행의 빈 칸·200자에 AC-002의 199자를 더했다. C1 오른쪽 끝 12/12 (4 sizes x 3 states, rendered (injected css); spot check 같음: check 0 / observed 0)과 C2 12/12 (4 sizes x 3 states, rendered (injected css); spot check 같음: check 320 ≤ 320 / observed x=303)은 측정 범위 안에서 규칙대로다. C1 간격 12/12 (4 sizes x 3 states, rendered (injected css); spot check differs: check 4 / observed 9)는 요소 상자 사이가 `--space-1` 4px라는 뜻일 뿐이고, 글자 줄 높이의 위쪽 여백 때문에 눈에 보이는 간격은 9px다. RULE-002의 "붙어 보여야"를 어느 쪽으로 판단할지는 내가 정하지 않았다.

질문: C1의 "4px"는 글자 수 요소 상자까지인가, 눈에 보이는 글자까지인가?

report-check: ok 2,001 chars 96546d24
