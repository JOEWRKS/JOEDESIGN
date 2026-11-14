- 작업: R1-2 글자 수 표시의 DESIGN 규칙 C1·C2를 `tools/measure.mjs`로 4개 너비(320·375·768·1280) x 2개 상태(빈 칸·200자)에서 측정했다. 미리보기가 연결 CSS를 못 읽어(`linkedCss loaded:false`) `--inject src/style.css`로 같은 CSS를 주입해 쟀다. 320x420 200자 캡처로 두 행 모두 표본 대조했다. 화면 코드는 고치지 않았다.
- 업데이트 파일: DESIGN.md (C1·C2 행의 Check·Spot check·Unmeasured·Result), ROADMAP.md (R1-2 근거·다음 작업), TASK.md (2026-11-15-r1-2-check), evidence/2026-11-15-r1-2-320x420-200.png, REPORT.md
- 이슈: C1 아래 간격은 상자 기준으로는 4px이지만 화면에 보이는 간격은 9px다(칸 테두리 끝 y304, 글자 잉크 시작 y313; 글자 줄 높이의 위쪽 여백 때문). 규칙이 어느 쪽을 뜻하는지 정해져 있지 않다.
- 해결: 없음
- 남은 문제: C1은 표본 대조가 측정과 달라 통과로 기록하지 않았다(소유자 판단 대기). 연결 CSS를 페이지가 직접 읽은 화면, 199자 상태의 배치, 칸 크기 조절, 이 기기 system-ui 외 글꼴은 측정하지 않았다. R1-2는 verification pending 유지, 사용자 화면 확인 별도.
- 다음 작업: 소유자 질문 — C1 "칸 상자 아래 4px"가 (a) 요소 상자 사이 4px(현재 4px로 충족)인지, (b) 보이는 간격 4px(현재 9px, `.char-count`의 line-height 조정 필요)인지 정해 주세요. 답에 따라 C1 행의 Check를 고치거나 화면을 고친 뒤 C1·C2를 다시 잰다.

design check results:
- C1 아래 간격(상자) | 8/8 | 4 sizes x 2 states, light | rendered (injected css) | spot check differs: 320x420 200자 check 4 / observed 9
- C1 오른쪽 끝 | 8/8 | 4 sizes x 2 states, light | rendered (injected css) | 320x420 200자 check 0 / observed 0 (테두리·글자 잉크 끝 모두 x303)
- C2 넘침 | 8/8 | 4 sizes x 2 states, light | rendered (injected css) | 320x420 200자 check scrollWidth 320 / observed 가장 오른쪽 잉크 x303, 가로 스크롤바 없음
- AC-002 글자 | 3/3 | 1 size x 3 states, light | rendered (injected css) | not spot-checked

C2는 통과다(4 sizes x 2 states, rendered (injected css), spot check 일치). C1 오른쪽 끝도 측정과 관찰이 일치한다(4 sizes x 2 states, rendered (injected css), spot check 일치). C1 아래 간격은 상자 측정 8/8(4 sizes x 2 states, rendered (injected css), spot check differs: check 4 / observed 9)이라 규칙 통과로 적지 않았다. 주입 없이 페이지 그대로 재면 스타일이 빠져 글자 수가 칸 위로 겹쳐 측정되므로(375px에서 간격 -19), 위 결과는 모두 주입 CSS 기준이다.

참고: 첫 캡처를 작업 루트 밖 임시 폴더에 저장했다가 프로젝트 안 evidence/로 다시 찍고 바깥 사본은 지웠다(같은 바이트 확인). 커밋하지 않았다.

report-check: ok 1,879 chars 3a9a7536
