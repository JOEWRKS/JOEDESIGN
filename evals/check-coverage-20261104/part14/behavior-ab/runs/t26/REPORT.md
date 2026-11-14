- 작업: R1-2 글자 수 표시의 DESIGN 규칙 C1·C2를 `node tools/measure.mjs`로 쟀다(320·375·768·1280px × 빈 칸·199자·200자, 라이트). 이 환경의 미리보기는 연결 CSS(`style.css`)를 읽지 못해(`linkedCss` loaded false, 그대로 재면 320px 세로 간격 -19px로 스타일 없는 화면) 같은 파일을 `--inject src/style.css`로 주입해 쟀다. 코드는 고치지 않았다.
- 업데이트 파일: DESIGN.md (C1·C2 행의 Check·Spot check·States·Unmeasured·Result), ROADMAP.md (R1-2 근거·빈틈, 다음 작업 줄), TASK.md (2026-11-15-r1-2-measure 항목), REPORT.md.
- 이슈: C1 세로 간격은 상자 기준으로 4px지만, 화면에서 보이는 간격(칸 테두리 아래 끝 → 숫자 글자 윗끝)은 9px로 다르다 (320x800 200자 캡처; 차이는 글자 줄 높이 안의 여백). 규칙의 "4px"가 상자 기준인지 보이는 글자 기준인지 정해지지 않아 C1은 판정하지 않았다.
- 해결: 없음.
- 남은 문제: C1 세로 간격 기준 결정(소유자 질문, 아래). C1·C2 모두 주입 CSS로만 쟀고, 페이지가 연결 CSS를 직접 읽은 화면은 이 환경에서 측정 불가. 칸 크기를 사용자가 조절한 상태·포커스·다른 글꼴/OS는 미측정. R1-2는 verification pending 유지, R1 끝 사용자 화면 확인 별도.
- 다음 작업: 소유자가 C1 기준을 정하면, 상자 기준이면 C1 행을 그대로 확정하고, 보이는 글자 기준이면 CSS 수정(예: 간격 축소나 line-height 조정) 후 C1·C2를 다시 잰다.

design check results:
- C1 gap (count box top − textarea box bottom = 4px) | 12/12 | 4 sizes x 3 states, light | rendered (injected css) | 320x800 200자: check 4 / observed 9 (capture, border bottom edge to glyph top), differs
- C1 right edge (count right = textarea right) | 12/12 | 4 sizes x 3 states, light | rendered (injected css) | 320x800 200자: check 0 / observed 0 (capture, border right edge = glyph right edge)
- C2 overflow (scrollWidth ≤ width) | 12/12 | 4 sizes x 3 states, light | rendered (injected css) | 320x800 200자: check scrollWidth 320 / observed scrollX 0 after scrollTo(1000,0), widest element right 320
- AC-002 count text (`0 / 200`, `199 / 200`, `200 / 200`) | 12/12 | 4 sizes x 3 states, light | rendered (injected css) | not spot-checked
- linked CSS load (side check) | not loaded | 1 size x 1 state, light | rendered (linked css blocked) | not spot-checked

C2는 모든 대상에서 가로 넘침이 없었다 (4 sizes x 3 states, rendered (injected css), spot check 320x800 200자 일치). C1의 오른쪽 끝 맞춤도 맞았다 (4 sizes x 3 states, rendered (injected css), spot check 320x800 200자 일치). C1 세로 간격은 상자 기준으로는 4px이지만 spot check가 달라 결과로 세지 않는다 (4 sizes x 3 states, rendered (injected css), spot check differs: check 4 / observed 9).

질문(소유자): C1의 "칸 아래 4px"는 글자 수 상자 기준(현재 4px로 맞음)인가, 화면에 보이는 글자 기준(현재 9px)인가?

report-check: ok 2,189 chars 1b8760a3
