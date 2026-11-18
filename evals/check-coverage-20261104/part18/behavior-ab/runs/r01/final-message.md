# C1·C2 측정 보고 (요청 화면, 확인 화면)

- 작업: DESIGN 규칙 C1(글자 수 위치)·C2(가로 넘침)를 요청 화면(src/index.html)과 확인 화면(src/confirm.html)에서 너비 320·375·768·1280px × 빈 칸·200자 상태, 라이트 모드로 `node tools/measure.mjs`로 쟀다. 코드는 고치지 않았다.
- 업데이트 파일: DESIGN.md(C1·C2 행의 Check·Spot check·Unmeasured·Result), ROADMAP.md(R1-2·R1-3 근거와 다음 작업 줄), TASK.md(2026-11-18-c1-c2 항목), ISSUES.md(ISS-001), REPORT.md. 측정 스크립트·캡처는 .work/에 있다.
- 이슈: (1) C1은 상자 간격이 4px로 나오지만, 캡처에서 보이는 간격(입력 칸 테두리 아래부터 글자 잉크 위까지)은 9px로 규칙 값과 다르다. (2) 측정 도구가 confirm.html의 링크 CSS(style.css)를 막아, 확인 화면은 같은 style.css를 주입해 쟀다(ISS-001).
- 해결: 없음
- 남은 문제: C1 판정 보류 — 규칙의 4px가 상자 간격인지 보이는 간격인지 DESIGN 책임자 결정 필요. 확인 화면을 자기 링크 CSS로 잰 측정 없음(ISS-001 열림). R1-2·R1-3은 verification pending 유지. 사용자 화면 확인은 별도.
- 다음 작업: C1 기준 결정을 받은 뒤 보이는 간격이면 `.char-count` 간격을 고쳐 두 화면 C1·C2를 다시 재고, 상자 간격이면 C1 행에 그 뜻을 적어 판정한다. 확인 화면을 CSS가 막히지 않는 방법으로 다시 잰다.

design check results:
- C1 상자 간격·오른쪽 끝, 요청 화면 | 8/8 (간격 4px, 오른쪽 차이 0px) | 4 sizes x 2 states, light | rendered (own css) | 375x800 빈 칸 캡처: 간격 check 4 / observed 9, 오른쪽 check 0 / observed 0 — 간격 다름
- C1 상자 간격·오른쪽 끝, 확인 화면 | 8/8 (간격 4px, 오른쪽 차이 0px) | 4 sizes x 2 states, light | rendered (injected css) | 375x800 빈 칸 캡처: 간격 check 4 / observed 9, 오른쪽 check 0 / observed 0 — 간격 다름
- C2 가로 넘침, 요청 화면 | 8/8 (scrollWidth = 화면 너비) | 4 sizes x 2 states, light | rendered (own css) | 320x800 200자: check scrollWidth 320 / observed scrollTo(200,0) 뒤 scrollX 0, 캡처에 잘림 없음
- C2 가로 넘침, 확인 화면 | 8/8 (scrollWidth = 화면 너비) | 4 sizes x 2 states, light | rendered (injected css) | 320x800 200자: check scrollWidth 320 / observed scrollTo(200,0) 뒤 scrollX 0, 캡처에 잘림 없음
- AC-002 글자 수 문구, 요청 화면 | 3/3 (빈 칸 0 / 200, 199자 199 / 200, 200자 200 / 200) | 1 size (375) x 3 states, light | rendered (own css) | not spot-checked
- AC-003 글자 수 문구, 확인 화면 | 2/2 (빈 칸 0 / 200, 200자 200 / 200) | 1 size (375) x 2 states, light | rendered (injected css) | not spot-checked
- C1 확인 화면, CSS 막힌 상태(참고) | 0/8 (간격 -19px, 오른쪽 차이 55~73px) | 4 sizes x 2 states, light | rendered (linked css blocked, no style) | not spot-checked

상세 보고

C1: 두 화면 모두 글자 수 상자 top이 입력 칸 상자 bottom에서 정확히 4px(`--space-1`, `.field`의 gap) 아래이고, 오른쪽 끝도 입력 칸 오른쪽 끝과 같다. 그러나 캡처를 픽셀로 보면 입력 칸 아래 테두리 다음 줄부터 글자 수 표시의 글자 잉크 위까지 9px다(13px 글자의 줄 높이 여백 때문). 스킬 절차상 검사값과 직접 관찰이 다르면 그 검사 결과는 규칙의 통과로 치지 않는다. 그래서 C1은 상자 기준 8/8씩(4 sizes x 2 states, rendered, spot check differs: check 4 / observed 9) 나왔지만 판정 보류로 기록했다. 오른쪽 정렬은 직접 관찰과도 맞다.

C2: 두 화면 모두 문서 가로 스크롤이 없다(4 sizes x 2 states, rendered, spot check 320x800 200자 check 320 / observed scrollX 0).

확인 화면: tools/measure.mjs는 confirm.html의 링크 CSS를 막는다(linkedCss loaded=false). 막힌 그대로 재면 스타일이 없어 C1 값이 무의미하므로, 같은 src/style.css를 `--inject`로 넣어 잰 값을 확인 화면 결과로 썼다. 실제 브라우저가 링크로 읽은 CSS와 같은지는 재지 못했다. 요청 화면은 자기 링크 CSS를 읽었다(loaded=true).


질문(DESIGN 책임자): C1의 "상자 아래 4px"는 요소 상자 사이 간격(현재 4px)인가, 사람이 보는 테두리~글자 간격(현재 9px)인가?

report-check: ok 2,849 chars 249a2ef9