- 작업: R1-2 글자 수 표시의 DESIGN 규칙 C1·C2를 `node tools/measure.mjs`로 쟀습니다. 미리보기가 링크된 `style.css`를 막기 때문에(`linkedCss loaded: false`) 같은 파일을 `--inject src/style.css`로 주입해서 쟀습니다. 주입하지 않고 잰 값은 스타일이 빠진 화면 값이라(320에서 간격 -19, 오른쪽 차 55.27) 쓰지 않았습니다. 코드는 바꾸지 않았습니다.
- 업데이트 파일: DESIGN.md(C1·C2 행의 Check·Spot check·Unmeasured·Result), ROADMAP.md(R1-2 근거·빈틈, 다음 작업 줄), TASK.md(새 항목 2026-11-15-r1-2-measure).
- 이슈: C1 세로 간격의 스폿 체크 값이 다릅니다. 상자 기준 측정값은 4px인데, 320x600 200자 캡처에서 보이는 간격은 9px입니다(칸 아래 테두리 마지막 픽셀 303행, 숫자 잉크 첫 행 313행). 차이는 13px 글자의 줄 높이 안쪽 여백에서 생깁니다. 규칙 문구 "칸 상자 아래 4px(`--space-1`)"만으로는 상자 사이 간격인지 눈에 보이는 간격인지 정해지지 않아서 C1을 통과로 적지 않았습니다.
- 해결: 없음
- 남은 문제: C1 미통과입니다(4 sizes x 3 states, rendered (injected css), spot check differs: check 4 / observed 9). 규칙의 뜻은 소유자가 정해야 합니다. R1-2는 verification pending으로 유지했습니다. 측정은 모두 CSS를 주입한 화면에서 했고, 링크 CSS로 정상 로드된 화면은 재지 못했습니다. 다크 모드는 승인 범위 밖이고, 사용자 화면 확인도 아직 남아 있습니다.
- 다음 작업: 소유자 답을 받은 뒤 C1을 다시 판정합니다. 상자 기준이면 지금 결과의 스폿 체크 기준을 바꿔 다시 확인하고, 보이는 간격 기준이면 `.char-count` 줄 높이나 간격을 고친 뒤 C1·C2를 다시 잽니다.

질문(소유자): C1의 "4px"는 글자 수 요소 상자와 칸 상자 사이의 간격(지금 4px)인가요, 아니면 눈에 보이는 칸 테두리와 숫자 사이의 간격(지금 9px)인가요?

결과 목록:
- C1 세로 간격 | 12/12 상자 기준 4px | 4 sizes x 3 states, light | rendered (injected css) | 320x600 200자: check 4 / observed 9 (다름)
- C1 오른쪽 끝 | 12/12 차 0 | 4 sizes x 3 states, light | rendered (injected css) | 320x600 200자: check 0 / observed 0 (테두리·잉크 x 303)
- C2 넘침 없음 | 12/12 scrollWidth = 화면 너비 | 4 sizes x 3 states, light | rendered (injected css) | 320x600 200자: check scrollWidth 320 / observed 맨 오른쪽 잉크 x 303, 304–319 빈 칸
- AC-002 표시 문구 | 3/3 (`0 / 200`, `199 / 200`, `200 / 200`) | 4 sizes x 3 states, light | rendered (injected css) | not spot-checked

크기: 320, 375, 768, 1280. 상태: 빈 칸, 199자, 200자.

report-check: ok 1,733 chars e7ff3109
