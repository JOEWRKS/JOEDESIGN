요약: C2는 측정 범위 안에서 맞고(4 sizes x 3 states, rendered (injected css), spot check 일치), C1은 대조가 달라 통과로 보지 않습니다. 칸 테두리에서 글자 수까지 상자 간격은 4px이지만, 화면에 보이는 글자까지는 9px입니다. 코드는 바꾸지 않았습니다.

측정 방법: 이 미리보기는 연결된 `style.css`를 읽지 못해(`linkedCss loaded: false`, tools/README.md) 그대로 재면 스타일 없는 값이 나옵니다(주입 없이 잰 C1 위 간격 -19px, 버림). 그래서 모든 측정은 `--inject src/style.css`로 같은 CSS를 넣고 했습니다.

결과 목록
- C1 위 간격(상자) | 12/12 = 4px | 4 sizes(320·375·768·1280, 높이 800) x 3 states(빈 칸·199자·200자), light | rendered (injected css) | 320x800 200자 캡처: check 4 / observed 9 (칸 테두리 아래 끝 → 글자 잉크 위 끝), 다름
- C1 오른쪽 끝 | 12/12 = 0px 차 | 4 sizes x 3 states, light | rendered (injected css) | 320x800 200자 캡처: check 0 / observed 0 (테두리 오른쪽 열 x=303 = 잉크 오른쪽 열 x=303)
- C2 가로 넘침 | 12/12 (scrollWidth ≤ 화면 너비) | 4 sizes x 3 states, light | rendered (injected css) | 320x800 200자 캡처: check scrollWidth 320 / clientWidth 320, observed 가장 오른쪽 잉크 x=303, 오른쪽 16px 비어 있음
- AC-002 표시 글자 | 12/12 (`0 / 200`, `199 / 200`, `200 / 200`) | 4 sizes x 3 states, light | rendered (injected css) | not spot-checked

- 작업: DESIGN 규칙 C1·C2를 4개 화면 너비와 3개 상태에서 렌더 측정했습니다(CSS 주입). C2 넘침 측정은 결과 목록의 C2 줄을 보세요. C1 위 간격은 상자 기준 측정값과 캡처에서 보이는 간격이 다릅니다(상자 4 / 글자 9). 글자 줄 높이 17px 안의 위 여백 때문입니다.
- 업데이트 파일: DESIGN.md(C1·C2 행의 Check·Spot check·Unmeasured·Result), TASK.md(2026-11-15-r1-2-measure 새 항목), ROADMAP.md(R1-2 근거 칸과 다음 작업 줄). 코드 변경은 없습니다.
- 이슈: C1 규칙의 "4px"가 무엇을 재는지 정해지지 않았습니다. 상자 사이 간격(`--space-1`)인지, 화면에 보이는 칸 테두리와 글자 사이 간격인지 문구로는 정할 수 없습니다. RULE-002는 "시각적으로 붙어 보여야" 한다고만 합니다.
- 해결: 없음
- 남은 문제: C1 미판정(재는 양 결정 대기), R1-2는 verification pending 유지. 측정하지 않은 것: 실제 연결 CSS가 로드된 브라우저, 높이 800 외의 화면, 칸 크기를 조절한 뒤, 다크 모드(승인 범위 밖). AC-002 표시 글자는 대조하지 않았습니다. 측정 출력과 캡처는 세션 임시 폴더에 있어 보존되지 않습니다. 사용자 화면 확인도 남아 있습니다.
- 다음 작업: 질문입니다. C1의 4px를 (가) 상자 간격으로 볼까요, (나) 보이는 글자 간격으로 볼까요? (가)면 DESIGN C1 행에 상자 기준임을 적고 C1을 다시 판정하면 됩니다. (나)면 글자 수 표시의 줄 높이나 간격을 고쳐야 하는데, 이는 보이는 변화이므로 승인이 필요하고, 고친 뒤 C1·C2를 다시 잽니다.

report-check: ok 1,916 chars a5faa257
