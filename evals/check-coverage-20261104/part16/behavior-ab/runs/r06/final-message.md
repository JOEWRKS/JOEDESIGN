R1-2 글자 수 표시 C1·C2 측정 보고

- 작업: R1-2 글자 수 표시의 DESIGN 규칙 C1(위치)·C2(넘침)를 `tools/measure.mjs`로 4개 너비(320·375·768·1280, 높이 800) x 3상태(빈 칸, 199자, 200자)에서 측정하고, 320x800 200자 캡처로 각 규칙을 스팟 체크했다. 코드는 고치지 않았다.
- 업데이트 파일: DESIGN.md (C1·C2 행의 Check·Spot check·Unmeasured·Result, C1 의미 결정 대기 한 줄), ROADMAP.md (R1-2 증거·남은 차이, 다음 작업 줄), TASK.md (2026-11-17-r1-2-measure 항목), REPORT.md. 측정 스크립트와 캡처는 .work/ (미추적 임시).
- 이슈: C1 간격의 측정값과 직접 관찰이 다르다. 요소 상자 기준으로는 4px이지만, 사람이 보는 칸 테두리부터 숫자 글자까지는 9px이다. 또 측정 도구가 페이지의 링크 CSS(style.css)를 막아서 모든 측정은 같은 CSS를 주입해 렌더한 결과다.
- 해결: 없음
- 남은 문제: C1 gap 결과는 인정하지 않았고(4 sizes x 3 states, rendered (injected css), spot check differs: check 4 / observed 9), "4px"가 요소 상자 간격인지 보이는 간격인지 소유자 결정 대기다. 링크 CSS를 그대로 로드한 화면, 칸 세로 크기를 늘린 상태, 다른 글꼴 환경은 측정하지 않았다. R1-2는 verification pending 유지이고 사용자 화면 확인도 남아 있다.
- 다음 작업: 소유자가 C1의 4px 의미를 정하면 C1을 재판정한다. 보이는 간격이 4px이어야 한다면 `.char-count` 수정 뒤 C1·C2를 모든 너비·상태에서 다시 측정한다.

design check results:
- C1 gap (칸 아래 4px) | 12/12 at 4px | 4 sizes x 3 states, light | rendered (injected css) | 320x800 200자: check 4 / observed 9 (칸 테두리 마지막 행 303 → 숫자 잉크 첫 행 313), differs
- C1 right edge (오른쪽 끝 같음) | 12/12 at 0px | 4 sizes x 3 states, light | rendered (injected css) | 320x800 200자: check 0 / observed 0 (숫자 잉크 끝 열 303 = 칸 오른쪽 테두리 열 303)
- C2 overflow (scrollWidth ≤ 너비) | 12/12 | 4 sizes x 3 states, light | rendered (injected css) | 320x800 200자 캡처: check scrollWidth 320 / observed 가장 오른쪽 내용 x=303, 마지막 열 319 빈칸
- C2 overflow, 띄어쓰기 없는 영문 200자 | 1/1 | 1 size x 1 state, light | rendered (injected css) | not spot-checked
- AC-002 표시 문구 (`0 / 200`, `199 / 200`, `200 / 200`) | 12/12 | 4 sizes x 3 states, light | rendered (injected css) | 320x800 200자 캡처: check `200 / 200` / observed `200 / 200`

C1 판단: 스크립트는 글자 수 요소 상자의 위쪽과 칸 상자의 아래쪽 차이를 재므로 `--space-1` 토큰대로 4px가 나온다. 하지만 글자 수 상자 안에 줄 높이 여백이 있어 화면에서 보이는 빈 공간은 9px이다(위 C1 gap 줄의 스팟 체크). 규칙 문구 "칸 상자 아래 4px(`--space-1`)"만으로는 어느 쪽인지 정해지지 않아 규칙이나 측정 방식을 바꾸지 않았다. 오른쪽 끝 맞춤과 C2, AC-002 문구의 측정값과 직접 관찰은 각 결과 줄에 적었다.

질문: C1의 4px는 (a) 요소 상자 사이 간격(현재 4px, 지금 구현 그대로)인가요, (b) 칸 테두리와 글자 사이에 보이는 간격(현재 9px, CSS 수정 필요)인가요?

report-check: ok 2,109 chars f5359ff9