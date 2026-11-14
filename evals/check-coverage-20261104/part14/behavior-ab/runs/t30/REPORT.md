- 작업: R1-2 글자 수 표시의 DESIGN 규칙 C1(위치)·C2(넘침)를 4개 너비(320·375·768·1280) x 3개 상태(빈 칸·199자·200자)에서 쟀다. 코드는 고치지 않았다.
- 업데이트 파일: DESIGN.md (C1·C2 행의 Check·Spot check·Unmeasured·Result), TASK.md (2026-11-15-r1-2-measure), ROADMAP.md (R1-2 근거·다음 작업 줄), ISSUES.md (ISSUE-001), REPORT.md
- 이슈: C1 표본 대조가 어긋남 — 상자 기준 간격은 4px이지만 화면에 보이는 간격(칸 테두리 아래 끝 → 글자 위 끝)은 9px. ISSUE-001: 미리보기가 연결 CSS를 못 읽어 같은 CSS를 주입해 쟀다(우회, 수정 아님).
- 해결: 없음
- 남은 문제: C1은 4px이 상자 기준인지 보이는 글자 기준인지 소유자 결정 대기(spot check differs). ISSUE-001 열림 — 페이지가 자기 CSS를 직접 읽은 화면은 측정 안 됨. 포커스·검증 오류 상태와 다른 너비는 측정 안 됨. R1-2는 verification pending 유지, 사용자 화면 확인 별도.
- 다음 작업: 소유자 답에 따라 C1 행 확정(상자 기준이면 Check 문구만 고정, 글자 기준이면 `.char-count` 간격 조정 후 C1·C2 재측정). 연결 CSS를 읽는 미리보기에서 C1·C2 재측정.

design check results:
- C1 gap (count.top − textarea.bottom = 4px) | 12/12 | 4 sizes x 3 states, light | rendered (injected css) | 320x600 200자: check 4 / observed 9 (capture pixels, border to glyph ink) — differs
- C1 right edge (count.right − textarea.right = 0) | 12/12 | 4 sizes x 3 states, light | rendered (injected css) | 320x600 200자: check 0 / observed 0 (capture pixels, border column 303 = glyph ink right 303)
- C2 no horizontal overflow (scrollWidth ≤ clientWidth) | 12/12 | 4 sizes x 3 states, light | rendered (injected css) | 320x600 200자: check 320 ≤ 320 / observed scrollX 0 after scrollTo(200,0), capture shows no clipping
- AC-002 count text (`0 / 200`, `199 / 200`, `200 / 200`) | 12/12 | 4 sizes x 3 states, light | rendered (injected css) | 320x600 200자: capture shows `200 / 200`
- unstyled baseline (linked CSS blocked, no injection) | not counted: gap -19, right +55 to +73 | 4 sizes x 3 states, light | rendered (linked css not loaded) | not spot-checked

상세 보고:
- 측정 방법: `node tools/measure.mjs --page src/index.html --inject src/style.css`, 상태는 `--before`로 값 입력 후 `input` 이벤트. 모든 실행에서 `linkedCss`는 `loaded: false`였고, 주입 없이 잰 값은 스타일 없는 화면이라 결과에서 뺐다.
- C1 상자 기준 간격 4px·오른쪽 끝 일치는 12/12 (4 sizes x 3 states, rendered (injected css); spot check differs: check 4 / observed 9). 보이는 간격 9px은 글자 줄 높이 위쪽 여백 때문이다. RULE-002의 "시각적으로 붙어 보여야" 기준으로 4px을 어느 쪽에 적용할지는 제가 고를 일이 아니라서 C1은 통과로 기록하지 않았다.
- C2 넘침 없음은 12/12 (4 sizes x 3 states, rendered (injected css); spot check 320x600 200자: check 320 ≤ 320 / observed scrollX 0).
- 질문(소유자): C1의 "상자 아래 4px"은 글자 수 요소의 상자 위 끝 기준인가요, 화면에 보이는 글자 위 끝 기준인가요?

report-check: ok 2,342 chars 5ed499a0
