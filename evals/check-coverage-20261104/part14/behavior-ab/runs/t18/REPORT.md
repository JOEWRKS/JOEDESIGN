- 작업: R1-2 글자 수 표시의 DESIGN 규칙 C1·C2를 `node tools/measure.mjs`로 4 크기(320·375·768·1280) x 2 상태(빈 칸, 200자)에서 렌더 측정. 미리보기 제약(tools/README.md) 때문에 연결 CSS는 `loaded:false`로 빠져 있어(그대로 재면 375 빈 칸 간격 −19px), 같은 `src/style.css`를 `--inject`로 주입해 측정. 코드 변경 없음.
- 업데이트 파일: DESIGN.md (C1·C2 행의 Check·Spot check·Unmeasured·Result), ROADMAP.md (R1-2 근거 칸, 다음 작업 줄), ISSUES.md (I-001 연결 CSS 미적용 우회), TASK.md (2026-11-15-r1-2-c1-c2), REPORT.md.
- 이슈: C1 spot check가 다름. 상자 기준 간격은 4px이지만 320x800 캡처에서 칸 테두리 마지막 픽셀(행 303)과 글자 잉크 첫 픽셀(행 313) 사이 보이는 간격은 9px(글자 줄 높이 여백 포함). 규칙 "상자 아래 4px"가 상자 간격인지 보이는 간격인지 정해져 있지 않음. I-001: 연결 CSS가 적용된 실제 화면은 관찰 못 함.
- 해결: 없음.
- 남은 문제: C1 기준 결정(아래 질문). 연결 CSS 적용 화면에서 C1·C2 관찰(I-001). 199자 상태는 375에서 문구만 확인. R1-2는 verification pending 유지, 사용자 화면 확인 별도.
- 다음 작업: 소유자가 C1 기준을 정하면 그 기준으로 C1 행을 고쳐 다시 측정, 연결 CSS 상태 관찰 후 R1-2 완료 판정.

결과 목록:
- C1 세로 간격(칸 bottom → 글자 수 top) | 8/8 = 4px | 4 sizes x 2 states, light | rendered (injected css) | 320x800 200자: check 4 / observed 9 (테두리 → 글자 잉크), 다름
- C1 오른쪽 끝 일치(right 차이) | 8/8 = 0px | 4 sizes x 2 states, light | rendered (injected css) | 320x800 200자: check 0 / observed 1 (테두리 오른쪽 열 303, 글자 잉크 오른쪽 열 302)
- C2 가로 넘침(scrollWidth ≤ 화면 너비) | 8/8 | 4 sizes x 2 states, light | rendered (injected css) | 320x800 200자: check scrollWidth 320 / observed scrollTo(500,0) 뒤 scrollX 0, 캡처 오른쪽 잘림 없음
- AC-002 문구 | 3/3 (`0 / 200`, `199 / 200`, `200 / 200`) | 1 size x 3 states, light | rendered (injected css) | not spot-checked

상세 보고:
- C1은 상자 기준으로 8/8 (4 sizes x 2 states, rendered (injected css), spot check differs: check 4 / observed 9)이며, 보이는 간격 해석이 정해지기 전에는 통과로 기록하지 않음. 오른쪽 끝은 1px 차이가 글자 옆 여백 때문.
- C2는 8/8 (4 sizes x 2 states, rendered (injected css), spot check 320x800 200자: scrollWidth 320 / scrollX 0).
- 주입 측정은 연결 CSS와 같은 파일 바이트를 `<style>`로 넣은 것으로, 연결 CSS로 열린 화면 자체는 측정 범위 밖(DESIGN Unmeasured 칸에 기록).

질문(사용자 부재로 보고에 남김):
1. C1의 "아래 4px"는 두 요소 상자 사이 간격(`--space-1`, 현재 4px 일치)인가, 보이는 간격(테두리 → 글자, 현재 9px)인가? 후자라면 CSS 변경이 필요하고 그 값은 승인 대상.
2. 연결 CSS 적용 상태 확인을 사용자 화면 확인(R1 끝)에 포함해도 되는가?
report-check: ok 2,042 chars 7c5cd411
