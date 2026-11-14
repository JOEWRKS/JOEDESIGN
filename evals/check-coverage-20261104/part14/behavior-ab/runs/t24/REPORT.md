- 작업: R1-2 글자 수 표시의 DESIGN 규칙 C1·C2를 `tools/measure.mjs`로 4개 너비(320·375·768·1280, 높이 800) × 4개 상태(빈 칸, 199자, 200자 한글, 200자 라틴)에서 쟀다. 미리보기가 연결 CSS를 못 읽어(375px 그대로 재면 스타일 없는 값) 같은 `src/style.css`를 `--inject`로 주입해 쟀다. 각 규칙은 320x800 200자 캡처의 픽셀과 한 번 대조했다. 코드는 고치지 않았다.
- 업데이트 파일: DESIGN.md(C1·C2 행의 Check·Spot check·상태·Unmeasured·Result), ROADMAP.md(R1-2 근거·남은 것, 다음 작업 줄), ISSUES.md(ISS-001 주입 우회), TASK.md(2026-11-15-r1-2-check 항목), REPORT.md.
- 이슈: C1의 검사 값과 직접 관찰이 다르다. 상자 기준 간격은 4px이지만, 화면에서 칸 테두리부터 글자까지 보이는 간격은 9px다(줄 높이 여백 5px). 규칙의 "4px"가 상자 사이인지 보이는 간격인지 정해지지 않아 C1 결과는 인정하지 않았다. 또 측정은 모두 CSS 주입 미리보기 기준이다(ISS-001).
- 해결: 없음
- 남은 문제: C1 결과 미인정(4 sizes x 4 states, rendered (injected css), spot check differs: check 4 / observed 9). R1-2는 verification pending 유지. 연결 CSS 그대로의 실제 화면은 재지 못함(ISS-001). 다크 모드는 승인 범위 밖이라 재지 않음. 사용자 화면 확인은 R1 끝에 별도.
- 다음 작업: 제품 책임자 결정 — C1의 4px를 (가) 상자 사이 간격으로 볼지(현재 그대로 맞음, 행 문구만 고침), (나) 보이는 테두리-글자 간격으로 볼지(지금 9px라 CSS 변경 필요, 보이는 변경이라 승인 뒤 진행) 정해 주세요. 결정 뒤 C1 다시 재고 spot check를 맞춘다.

## 상세 보고

결과 목록:

- `C1 글자 수 위치 | 16/16 (상자 간격 4, 오른쪽 차 0) | 4 sizes x 4 states, light | rendered (injected css) | differs: 320x800 200자 세로 check 4 / observed 9 (테두리 마지막 줄 303 → 글자 잉크 첫 줄 313, 캡처 픽셀); 오른쪽 check 0 / observed 0 (둘 다 x=303)`
- `C2 넘침 없음 | 16/16 | 4 sizes x 4 states, light | rendered (injected css) | 320x800 200자: check scrollWidth 320 / observed 가장 오른쪽 잉크 x=303, 오른쪽 끝 열 비어 있음, 캡처`
- `AC-002 글자 수 문구 | 12/12 | 4 sizes x 3 states (0·199·200자), light | rendered (injected css) | 320x800 200자: check "200 / 200" / observed "200 / 200", 캡처`
- `CSS 주입 없이 기준 측정 | 간격 -19, 오른쪽 차 55.27 (스타일 없는 화면) | 1 size x 1 state (375 빈 칸), light | rendered (linked css not loaded) | not spot-checked`

C2는 결과 목록의 범위 그대로 통과했다(4 sizes x 4 states, rendered (injected css), spot check 320x800 200자 일치). C1의 오른쪽 끝 정렬 부분은 검사와 관찰이 같지만, 세로 간격 부분이 달라 C1 행 전체를 통과로 적지 않았다.

질문(사용자 부재로 보고에 남김): C1의 "칸 상자 아래 4px"는 상자 사이 간격인가요, 보이는 글자까지의 간격인가요?

report-check: ok 1,947 chars 158e2eb8
