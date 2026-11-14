C2는 8/8 통과(4 sizes x 2 states, rendered (injected css), spot check 320x800 200자: check 320 ≤ 320 / observed scrollX 0). C1은 상자 기준 8/8 일치(4 sizes x 2 states, rendered (injected css), spot check differs: check 4 / observed 9)라 판정을 미뤘습니다. 칸 테두리와 글자 사이 실제 보이는 간격이 9px이기 때문입니다.

- 작업: DESIGN 규칙 C1·C2를 4개 너비 × 2개 상태(빈 칸, 200자)에서 쟀습니다. 미리보기는 연결된 CSS를 못 읽기 때문에(주입 없이 재면 `linkedCss loaded:false`, 간격 −19px로 스타일이 빠진 화면) `--inject src/style.css`로 같은 CSS를 넣고 쟀습니다. 320x800 200자 캡처의 픽셀로 각 행을 대조했고, AC-002 세 상태는 375px에서 입력으로 확인했습니다(3/3, 1 size x 3 states, rendered (injected css), not spot-checked; 텍스트만 확인).
- 업데이트 파일: DESIGN.md(C1·C2 행의 Check·Spot check·Unmeasured·Result), ROADMAP.md(R1-2 근거와 다음 작업 줄), TASK.md(2026-11-15-r1-2-measure 항목). 코드는 바꾸지 않았습니다.
- 이슈: C1 "상자 아래 4px"은 요소 상자 기준으로는 맞습니다(check 4). 하지만 사람에게 보이는 간격은 칸 아래 테두리 끝에서 글자 윗 끝까지 9px입니다(observed 9, 13px 글자의 줄 높이 여백). 규칙이 둘 중 어느 쪽을 뜻하는지 정해져 있지 않습니다.
- 해결: 없음
- 남은 문제: C1은 spot check 결과가 달라 통과로 기록하지 않았습니다. R1-2는 verification pending 상태를 유지합니다. 측정은 주입한 CSS 기준이라 실제 `<link>` 로드 경로는 재지 않았습니다. 1~199자 중간 상태의 배치, 높이 800 외의 화면, 확대·글꼴 차이도 재지 않았습니다. 사용자 화면 확인은 별도로 남아 있습니다.
- 다음 작업: 질문입니다. C1의 4px은 (가) 요소 상자 간격(현재 8/8 일치, 완료 가능)과 (나) 보이는 글자까지의 간격(현재 9px, 줄 높이나 여백 조정 필요) 중 어느 쪽입니까? 답을 주시면 그 기준으로 C1을 판정하고 R1-2 완료 여부를 정하겠습니다.

결과 목록:
- C1 글자 수 위치 | 8/8 상자 기준 일치(간격 4, 오른쪽 차이 0) | 4 sizes (320, 375, 768, 1280) x 2 states (빈 칸, 200자), light | rendered (injected css) | 320x800 200자 capture: gap check 4 / observed 9 (differs), right check 0 / observed 0
- C2 넘침 없음 | 8/8 | 4 sizes (320, 375, 768, 1280) x 2 states (빈 칸, 200자), light | rendered (injected css) | 320x800 200자: check scrollWidth 320 ≤ 320 / observed scrollTo(100,0) 뒤 scrollX 0, capture rightmost pixel x=303
- AC-002 글자 수 텍스트 | 3/3 | 1 size (375) x 3 states (0, 199, 200자), light | rendered (injected css) | not spot-checked
- 주입 없는 대조 | 연결 CSS 미적용(간격 −19, 오른쪽 차이 55.3) | 1 size (320) x 1 state (빈 칸), light | rendered (linked css blocked) | not spot-checked
report-check: ok 1,967 chars 38930086
