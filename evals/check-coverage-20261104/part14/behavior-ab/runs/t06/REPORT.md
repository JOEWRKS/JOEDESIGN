- 작업: R1-2 글자 수 표시 구현(요청 내용 칸 아래 오른쪽 `현재 / 200`, 입력마다 갱신)과 DESIGN 규칙 C1·C2 측정. C2 통과 12/12 (4 sizes x 3 states, rendered, spot check agrees). C1은 상자 기준 12/12 (4 sizes x 3 states, rendered, spot check differs: check 4 / observed 9)라 통과로 기록하지 않음.
- 업데이트 파일: src/index.html, src/style.css, DESIGN.md(C1·C2 행), ROADMAP.md(R1-2 verification pending), ISSUES.md(ISS-001), TASK.md(2026-11-15-r1-2).
- 이슈: ISS-001 — C1 간격이 상자로는 4px인데 캡처에서 보이는 간격(칸 테두리 → 글자 잉크)은 9px. 글꼴 위쪽 여백 때문이며, `--space-*` 토큰만으로는 보이는 4px를 만들 수 없음.
- 해결: 없음.
- 남은 문제: ISS-001 C1 기준 결정 대기(4px가 상자 간격인지 보이는 간격인지). R1-2는 verification pending. 글자 수 글자 크기 14px·색 `--muted`는 내가 고른 값이라 승인 전. R1 사용자 화면 확인 대기. 측정하지 않은 범위: 칸 높이를 끌어 늘린 상태, 포커스 상태, 브라우저 글자 크기 확대, 높이 800 외.
- 다음 작업: C1 기준을 정해 주시면 DESIGN.md C1 행을 고치고 재측정. 질문: (1) C1의 4px는 글자 수 상자 위 끝 기준인가요, 보이는 글자 기준인가요? (2) 글자 수 14px·회색(`--muted`)으로 괜찮은가요?

design check results:
- C1 gap (상자 top − 칸 bottom = 4) | 12/12 | 4 sizes x 3 states, light | rendered | 320x800 200자: check 4 / observed 9 (capture, 칸 테두리 행 303 → 잉크 첫 행 313)
- C1 right edge (상자 right 차 = 0) | 12/12 | 4 sizes x 3 states, light | rendered | 320x800 200자: check 0 / observed 0 (capture, 잉크 오른쪽 열 303 = 칸 테두리 열 303)
- C2 no horizontal overflow (scrollWidth ≤ innerWidth) | 12/12 | 4 sizes x 3 states, light | rendered | 320x800 200자: check 320 ≤ 320 / observed scrollTo(200,0) 뒤 scrollX 0, capture 오른쪽 흰 여백 16px
- AC-002 counter text (`0 / 200`, `199 / 200`, `200 / 200`) | 12/12 | 4 sizes x 3 states, light | rendered | not spot-checked

크기는 320·375·768·1280px(높이 800), 상태는 빈 칸·199자·200자이며, 측정 중 `style.css`는 페이지가 직접 불러왔습니다(linkedCss loaded). 오른쪽 끝 맞춤은 보이는 글자 기준으로도 맞고(12/12, 4 sizes x 3 states, rendered, spot check agrees: check 0 / observed 0), 세로 간격만 상자와 보이는 값이 다릅니다. 표시 위치를 바꾸거나 숨긴 기존 요소는 없습니다(요청 내용 라벨은 `<label for>`로 바꿨을 뿐 보이는 변화 없음). 커밋하지 않았습니다.

report-check: ok 1,829 chars 8d312bbe
