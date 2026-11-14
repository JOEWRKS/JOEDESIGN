- 작업: R1-2 글자 수 표시의 DESIGN 규칙 C1·C2를 `tools/measure.mjs`로 측정(코드 변경 없음). 미리보기가 링크된 `style.css`를 읽지 못해(`linkedCss` loaded false) 모든 측정은 `--inject src/style.css`로 같은 CSS를 주입해 했다.
- 업데이트 파일: DESIGN.md(C1·C2 행의 Check·Spot check·Unmeasured·Result), TASK.md(2026-11-15-r1-2-measure 항목), ROADMAP.md(R1-2 근거·남은 점), evidence/2026-11-15-r1-2/(320px 캡처 두 장), REPORT.md.
- 이슈: C1 간격의 표본 대조가 어긋남. 검사는 두 상자 사이를 재고, 캡처에서 보이는 칸 테두리와 글자 사이는 그보다 넓다(아래 결과 목록 C1 gap 줄).
- 해결: 없음
- 남은 문제: C1 간격을 상자 기준으로 볼지 보이는 글자 기준으로 볼지 소유자 결정 필요, 그 전까지 C1 간격의 판정은 결과 목록 C1 gap 줄에 맡김. 링크된 CSS를 페이지가 스스로 읽은 상태는 측정 못 함. 199자 상태는 글자 수 문구만 확인, C1·C2 위치·넘침은 미측정. R1-2는 verification pending 유지, 사용자 화면 확인 별도.
- 다음 작업: C1 간격 기준 결정을 받은 뒤 C1 행을 고치거나(상자 기준) CSS 조정안을 승인받아(잉크 기준) 다시 측정.

design check results:
- C1 gap (칸 상자 아래 → 글자 수 상자 위) | 8/8 at 4px | 4 sizes x 2 states (빈 칸, 200자), light | rendered (injected css) | 320x800 200자: check 4 / observed 9 (캡처의 칸 아래 테두리 → 글자 잉크 위), differs
- C1 right edge (오른쪽 끝 차이) | 8/8 at 0px | 4 sizes x 2 states (빈 칸, 200자), light | rendered (injected css) | 320x800 200자: check 0 / observed 0 (캡처의 칸 테두리 열 303, 글자 잉크 오른쪽 열 303)
- C2 overflow (scrollWidth ≤ 화면 너비) | 8/8 | 4 sizes x 2 states (빈 칸, 200자), light | rendered (injected css) | 320x800 200자: check scrollWidth 320 / observed 캡처의 가장 오른쪽 보이는 픽셀 x=303, 잘린 가장자리 없음
- AC-002 글자 수 문구 | 3/3 (`0 / 200`, `199 / 200`, `200 / 200`) | 1 size x 3 states (320), light; 빈 칸·200자는 4 sizes에서도 같은 문구 | rendered (injected css) | 320x800 200자: 캡처에 `200 / 200` 보임

측정한 값: 네 크기 모두에서 글자 수 상자 위는 칸 상자 아래보다 4px 아래, 오른쪽 끝은 칸과 같은 x(320에서 304, 375에서 359, 768에서 648, 1280에서 904)였다. 다만 C1 gap 줄은 표본 대조가 어긋나므로 C1 간격은 통과로 기록하지 않았다(4 sizes x 2 states, rendered (injected css), spot check differs: check 4 / observed 9). 차이 5px은 13px 글자의 줄 높이 위쪽 여백이다. C1 오른쪽 끝과 C2 넘침은 각 줄의 범위와 표본 대조 그대로다.

질문(소유자): C1의 "상자 아래 4px"는 (a) 글자 수 요소 상자와 칸 상자 사이(지금 값과 일치)인가, (b) 보이는 칸 테두리와 글자 사이(지금 9px, 맞추려면 CSS 변경과 승인 필요)인가? 답에 따라 C1 행의 Check 또는 화면을 고친다.

report-check: ok 1,956 chars e5b24a0a
