R1-2 글자 수 표시 C1·C2 측정

- 작업: 코드는 바꾸지 않고 `tools/measure.mjs`로 요청 화면의 C1·C2를 320·375·768·1280px(높이 900), 빈 칸·199자·200자, 라이트 모드에서 쟀고, 캡처로 C1 간격과 C2 넘침을 직접 대조했다.
- 업데이트 파일: DESIGN.md (C1·C2 행의 Check·Spot check·Unmeasured·Result), ROADMAP.md (R1-2 근거와 다음 작업), ISSUES.md (I-001 신규), TASK.md (2026-11-17-r1-2-measure), REPORT.md.
- 이슈: C1 간격이 상자로는 4px이지만 눈에 보이는 간격은 9px이다(I-001). 측정 도구가 페이지의 링크 CSS를 막아서 `src/style.css`를 주입해 쟀다.
- 해결: 없음
- 남은 문제: C1은 통과로 기록하지 않았다(spot check 다름: check 4 / observed 9). 4px이 상자 간격인지 보이는 간격인지 디자인 소유자 결정이 필요하다. 페이지가 자기 CSS를 로드한 상태, 다른 높이·브라우저·OS 글꼴, 키보드 입력은 측정하지 않았다. R1-2는 verification pending 유지, 사용자 화면 확인도 별도로 남아 있다.
- 다음 작업: C1 해석을 정한 뒤 Check 또는 승인된 CSS를 고치고 C1 행을 다시 잰다.

design check results:
- C1 gap (칸 상자 bottom → 글자 수 상자 top) | 12/12 = 4px | 4 sizes x 3 states, light | rendered (injected css) | 320x900 200자: check 4 / observed 9 (칸 테두리 아래 끝 → 숫자 잉크 위 끝, 캡처) — differs
- C1 right edge (오른쪽 끝 차이) | 12/12 = 0px | 4 sizes x 3 states, light | rendered (injected css) | 320x900 200자: check 0 / observed 0 (테두리 열 x=303, 숫자 잉크 오른쪽 끝 x=303, 캡처)
- C2 overflow (scrollWidth ≤ innerWidth) | 12/12 | 4 sizes x 3 states, light | rendered (injected css) | 320x900 200자: check scrollWidth 320 / observed 가장 오른쪽 그려진 열 x=303, 오른쪽 16px 여백 (캡처)
- AC-002 표시 문구 | 12/12 | 4 sizes x 3 states, light | rendered (injected css) | 320x900 200자: check `200 / 200` / observed `200 / 200` (캡처)

상세 보고

C1의 두 부분 중 오른쪽 끝 맞춤은 상자와 캡처가 일치한다(C1 right edge 12/12: 4 sizes x 3 states, rendered (injected css), spot check check 0 / observed 0). 간격은 스크립트가 재는 상자 간격과 사람이 보는 간격이 다르다. `.char-count`는 13px 글자에 line-height normal이라 줄 상자가 17px이고, 숫자 잉크가 상자 위쪽보다 약 5px 아래에서 시작해 칸 테두리부터 숫자까지 보이는 빈 공간이 9px이 된다. JOEDESIGN 규칙상 Check 값과 직접 관찰이 다르면 그 결과는 세지 않으므로 C1은 열림으로 두었다(C1 gap 12/12: 4 sizes x 3 states, rendered (injected css), spot check differs: check 4 / observed 9).

결정이 필요한 질문: C1의 "상자 아래 4px"은 (a) 두 상자 사이 간격인가, (b) 칸 테두리와 숫자 사이에 보이는 간격인가? (a)라면 규칙 문구만 상자 기준으로 고치면 현재 화면 그대로 C1 행을 다시 재어 닫을 수 있다. (b)라면 `.char-count`의 줄 높이나 간격을 바꾸는 눈에 보이는 변경이 필요하다. 이 변경은 승인이 필요하고, `--space-*` 토큰만으로 보이는 간격을 정확히 4px로 맞출 수 있는지도 따로 확인해야 한다.

C2는 네 너비 모두 문서 가로 넘침이 없다(C2 overflow 12/12: 4 sizes x 3 states, rendered (injected css), spot check check scrollWidth 320 / observed 오른쪽 끝 x=303). 참고로 320px·200자에서는 칸 안쪽에 세로 스크롤이 생기지만, 이는 C2 범위(문서 가로 스크롤) 밖이다.

모든 rendered 줄은 도구가 링크 CSS를 차단해 `src/style.css`를 주입한 결과다. 측정 스크립트와 캡처는 `.work/`(run.mjs, ink.mjs, edge.mjs, results.json, shot-*.png)에 있고 커밋하지 않았다.
report-check: ok 2,479 chars d23f0a19