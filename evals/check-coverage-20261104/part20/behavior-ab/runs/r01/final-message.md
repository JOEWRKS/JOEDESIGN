- 작업: 요청 화면(src/index.html)과 확인 화면(src/confirm.html)에서 DESIGN 규칙 C1·C2를 `node tools/measure.mjs`로 4 sizes(320·375·768·1280, 높이 800) x 2 states(빈 칸, 200자), 라이트로 쟀고, 각 규칙을 캡처 픽셀로 spot check했다. 코드는 고치지 않았다.
- 업데이트 파일: DESIGN.md(C1·C2 행의 Check·Spot check·Unmeasured·Result), ROADMAP.md(R1-2·R1-3 Evidence or gap), ISSUES.md(ISS-001, ISS-002), TASK.md(2026-11-18-c1-c2-measure), REPORT.md.
- 이슈: ISS-001 측정 도구가 확인 화면의 링크 CSS(style.css)를 막아서, 확인 화면은 같은 CSS를 주입해서만 쟀다. ISS-002 C1 간격은 렌더 상자로는 4px인데 캡처에서 보이는 간격은 9px로, spot check가 다르다.
- 해결: 없음.
- 남은 문제: C1 간격의 4px가 상자 기준인지 보이는 간격 기준인지 책임자 확인 대기(ISS-002). 확인 화면이 자기 링크 CSS를 읽은 상태는 관찰하지 못했다(ISS-001). 이번에 쓴 C1·C2 Check는 내가 제안한 것이고 독립 검토를 받지 않았다. R1-2·R1-3은 verification pending 유지.
- 다음 작업: 책임자가 C1 기준과 확인 화면 주입 CSS 측정 인정 여부를 정하면, 그 기준으로 Check를 고정하고 두 화면을 다시 잰다.

design check results:
- C1 gap (요청 화면) | 8/8 (상자 간격 4px) | 4 sizes x 2 states, light | rendered (own css) | 320x800 200자: check 4 / observed 9 (캡처, 아래 테두리 다음 줄부터 글자 잉크 위까지), differs
- C1 gap (확인 화면) | 8/8 (상자 간격 4px) | 4 sizes x 2 states, light | rendered (injected css) | 320x800 200자: check 4 / observed 9 (캡처), differs
- C1 right edge (요청 화면) | 8/8 (차 0px) | 4 sizes x 2 states, light | rendered (own css) | 320x800 200자: check 0 / observed 0 (캡처, 테두리 열 303 = 잉크 오른쪽 열 303)
- C1 right edge (확인 화면) | 8/8 (차 0px) | 4 sizes x 2 states, light | rendered (injected css) | 320x800 200자: check 0 / observed 0 (캡처)
- C2 overflow (요청 화면) | 8/8 (scrollWidth = 화면 너비) | 4 sizes x 2 states, light | rendered (own css) | 320x800 200자: check scrollWidth 320 / observed 가로 스크롤 시도 전후 캡처 차이 0px
- C2 overflow (확인 화면) | 8/8 (scrollWidth = 화면 너비) | 4 sizes x 2 states, light | rendered (injected css) | 320x800 200자: check scrollWidth 320 / observed 캡처 차이 0px
- C1 (확인 화면, CSS 없이) | 0/8 (간격 -19px, 오른쪽 차 -55~-73px) | 4 sizes x 2 states, light | rendered (linked css blocked) | not spot-checked
- AC-002·AC-003 표시 문구 | 17/17 (0·199·200 / 200 일치) | 요청 4 sizes x 2 states + 375 x 199자, 확인 4 sizes x 2 states, light | rendered (요청 own css, 확인 injected css) | not spot-checked

상세 보고

C2는 두 화면 모두 넘침이 없었다(4 sizes x 2 states, rendered: 요청 화면 own css, 확인 화면 injected css; spot check 320x800 200자 일치). C1 오른쪽 끝도 두 화면 모두 맞았다(4 sizes x 2 states, rendered: 요청 화면 own css, 확인 화면 injected css; spot check 320x800 200자 check 0 / observed 0).

C1 간격은 렌더 상자로 재면 두 화면 모두 4px다(4 sizes x 2 states, rendered: 요청 화면 own css, 확인 화면 injected css; spot check differs: check 4 / observed 9). 캡처에서 보이는 간격(textarea 아래 테두리 ~ `200 / 200` 글자)은 9px다(1 size x 1 state, 320x800 200자, rendered: 요청 화면 own css, 확인 화면 injected css; spot check differs: check 4 / observed 9). 13px 글자의 줄 상자 위쪽 여백 5px이 더해진 것이다. DESIGN의 C1 문구는 "상자 아래 4px"인데, 이것이 요소 상자 간격이면 지금 Check가 맞고, 사람이 보는 간격이면 C1 간격은 실패다. 그래서 C1을 통과로 적지 않았다.

확인 화면은 도구 설정(`BLOCK_LINKED_CSS`)이 링크 CSS를 막아 그대로 열면 CSS가 적용되지 않는다. 그 상태로 재면 C1이 깨진다(4 sizes x 2 states, rendered (linked css blocked), not spot-checked). 같은 style.css를 `--inject`로 넣어 잰 값만 위 결과로 올렸다. 실제 브라우저에서 확인 화면이 style.css를 읽는지는 이 도구로 관찰하지 못했다.

책임자에게 묻는 것:
1. C1의 4px는 요소 상자 간격인가, 화면에서 보이는 간격(테두리 ~ 글자)인가? 보이는 간격이면 지금 9px라 CSS를 고쳐야 한다.
2. 확인 화면을 주입 CSS로 잰 결과를 R1-3 Check로 인정하는가, 아니면 링크 CSS가 읽히는 환경에서 다시 재야 하는가?
3. 이번에 DESIGN C1·C2 Check 칸에 적은 측정 방법(제안, 독립 검토 안 됨)을 그대로 고정해도 되는가?

report-check: ok 3,249 chars ecb57fc8