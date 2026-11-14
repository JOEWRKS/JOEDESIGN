- 작업: R1-2 글자 수 표시의 DESIGN 규칙 C1·C2를 `tools/measure.mjs`로 4개 너비(320·375·768·1280, 높이 800) x 2개 상태(빈 칸, 200자)에서 재고, 각 규칙을 320x800 캡처의 픽셀과 직접 대조했다. 미리보기가 연결 CSS를 못 읽어(`linkedCss` loaded=false, 주입 없이 재면 간격 -19px의 스타일 빠진 화면) `--inject src/style.css`로 같은 CSS를 주입해 쟀다. 코드는 고치지 않았다.
- 업데이트 파일: DESIGN.md(C1·C2 행의 Check·Spot check·Unmeasured·Result), ROADMAP.md(R1-2 근거 칸, 다음 작업 줄), TASK.md(2026-11-15-r1-2-c1c2 항목), evidence/(캡처 2장, 픽셀 판독 스크립트 png-edges.mjs), REPORT.md.
- 이슈: C1 위 간격은 요소 상자로는 4px이지만 캡처에서 칸 테두리 마지막 줄(y303)부터 글자 첫 줄(y313)까지 보이는 간격은 9px이다(320x800 200자, 1280x800 빈 칸 같음). 차이는 13px 글자의 줄 높이 위쪽 여백이다. 규칙의 "4px"가 상자 간격(`--space-1` 토큰)인지 보이는 간격인지 정해져 있지 않아, 검사 결과를 C1 간격 판정으로 쓸 수 없다.
- 해결: 없음
- 남은 문제: C1 위 간격 판정 대기(아래 질문). C1 오른쪽 끝과 C2는 주입 CSS 렌더 기준이며, 연결 CSS가 실제로 로드된 화면은 이 환경에서 잴 수 없어 미측정이다. 199자·칸 크기 조절 뒤·실제 기기 글꼴도 미측정. R1-2는 verification pending 유지, 사용자 화면 확인은 별도.
- 다음 작업: 제품 책임자가 C1 기준을 정하면 C1 재측정(보이는 간격 4px이 기준이면 CSS 수정이 필요하고, 그건 이 보고 범위 밖이다). 연결 CSS 렌더를 잴 수 있는 미리보기가 생기면 C1·C2 재측정.

디자인 검사 결과:

- `C1 오른쪽 끝(count.right − textarea.right = 0) | 8/8 | 4 sizes x 2 states, light, injected css | rendered | 320x800 200자 캡처: check 0 / observed 0 (테두리 x303, 글자 x303)`
- `C1 위 간격(count.top − textarea.bottom = 4px) | 8/8 상자 기준 4px | 4 sizes x 2 states, light, injected css | rendered | 320x800 200자 캡처: check 4 / observed 9 (테두리 y303 → 글자 y313), 다름`
- `C2 넘침 없음(scrollWidth ≤ 화면 너비) | 8/8 | 4 sizes x 2 states, light, injected css | rendered | 320x800 200자 캡처: check scrollWidth 320 ≤ 320 / observed 가장 오른쪽 픽셀 x303 < 320, 글자 잘림 없음`
- `AC-002 문구 | 3/3 (0 / 200, 199 / 200, 200 / 200) | 1 size x 3 states, light, injected css | rendered | not spot-checked`

질문(제품 책임자):
1. C1의 "칸 상자 아래 4px"은 글자 수 요소 상자와 칸 사이 간격(지금 4px)인가, 눈에 보이는 테두리와 글자 사이 간격(지금 9px)인가?

report-check: ok 1,759 chars ae0bf6fe
