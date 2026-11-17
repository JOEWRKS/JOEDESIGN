# R1-2 글자 수 표시 C1·C2 측정 보고

- 작업: DESIGN.md 규칙 C1·C2를 `tools/measure.mjs`로 320·375·768·1280px x 빈 칸·199자·200자(라이트)에서 재고, 320px 캡처로 행마다 spot check 함. 코드는 바꾸지 않음.
- 업데이트 파일: DESIGN.md(C1·C2 행의 Check·Spot check·States·Unmeasured·Result, C1 기준 미정 항목), ROADMAP.md(R1-2 근거·다음 작업 줄), TASK.md(새 항목 2026-11-17-r1-2-measure), REPORT.md.
- 이슈: C1 세로 간격은 측정값과 눈에 보이는 값이 다름(C1 세로 간격 12/12 (4 sizes x 3 states, rendered (injected css), spot check differs: check 4 / observed 9)). 또 측정 도구가 페이지의 linked CSS를 막아서(loaded=false) src/style.css를 주입해 렌더함.
- 해결: 없음.
- 남은 문제: C1은 "4px"가 글자 수 상자 기준인지 보이는 글자 기준인지 정해지지 않아 통과로 기록하지 않음. R1-2는 verification pending 유지. linked CSS를 실제로 읽은 렌더, 칸 크기 조절 뒤 모습, 글꼴 확대는 측정하지 않음. 사용자 화면 확인 대기.
- 다음 작업: C1 기준을 정해 주시면(아래 질문) 그 기준으로 C1 행을 고치고 다시 잰다. 보이는 글자 기준이면 CSS 수정이 필요하다.

design check results:
- C1 세로 간격(상자 top − 칸 bottom = 4px) | 12/12 | 4 sizes x 3 states, light | rendered (injected css) | 320x800 200자: check 4 / observed 9
- C1 오른쪽 끝 맞춤(right 차 0) | 12/12 | 4 sizes x 3 states, light | rendered (injected css) | 320x800 200자: check 0 / observed 0
- C2 가로 넘침(scrollWidth ≤ 화면 너비) | 12/12 | 4 sizes x 3 states, light | rendered (injected css) | 320x800 200자: check scrollWidth 320 ≤ 320 / observed 가장 오른쪽 칠해진 열 303, 마지막 열 어두운 픽셀 0
- AC-002 글자 수 문구(0·199·200 / 200) | 12/12 | 4 sizes x 3 states, light | rendered (injected css) | 320x800 200자: check "200 / 200" / observed 캡처에 "200 / 200"

C1 세로 간격 12/12 (4 sizes x 3 states, rendered (injected css), spot check differs: check 4 / observed 9). 측정은 글자 수 표시의 상자(`.char-count`)와 칸 상자 사이 거리를 읽고, 이 값은 `.field`의 `gap: var(--space-1)`이라 모든 크기에서 정확히 4px다. 그런데 320px 캡처를 픽셀로 보면 칸 아래 테두리(303행)와 글자 맨 윗줄(313행) 사이에 빈 행이 9개다. 글자 줄 높이 안의 위쪽 여백 때문이다. 규칙 문장("상자 아래 4px")만으로는 어느 쪽을 뜻하는지 정할 수 없어서, C1 결과는 위 목록의 줄에 맡기고 규칙 기준이 정해질 때까지 열어 둔다.

C1 오른쪽 끝 맞춤 12/12 (4 sizes x 3 states, rendered (injected css), spot check: check 0 / observed 0). 캡처에서 칸 오른쪽 테두리와 마지막 글자 "0"의 오른쪽 끝이 같은 303열이다.

C2 가로 넘침 12/12 (4 sizes x 3 states, rendered (injected css), spot check: check scrollWidth 320 ≤ 320 / observed 가장 오른쪽 칠해진 열 303). 320px 200자에서도 문서가 화면보다 넓어지지 않는다.

측정 방식: `tools/measure.mjs`는 페이지의 `<link rel=stylesheet>`를 막는 설정이라(모든 실행에서 loaded=false), 같은 src/style.css를 `--inject`로 넣어 렌더했다. 그래서 모든 결과는 rendered (injected css)다. 보조 스크립트와 캡처는 .work/ 아래에 있고(run-c1c2.mjs, c1c2-result.json, shot-*.png) 커밋 대상이 아니다. 아무것도 커밋하지 않았다.

질문: C1의 "4px"는 어느 쪽 기준인가요? (가) 글자 수 상자 기준이면 지금 상태 그대로 C1이 맞고, 행 문구를 "상자 기준"으로 분명히 고치면 된다. (나) 눈에 보이는 글자 기준이면 지금 9px라서 CSS를 고쳐야 한다(예: `.char-count`의 line-height를 줄이는 방법). 고치면 C1·C2를 다시 잰다.

report-check: ok 2,556 chars 98b07a3e