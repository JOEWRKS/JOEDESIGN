- 작업: R1-2 글자 수 표시의 DESIGN 규칙 C1(글자 수 위치)·C2(가로 넘침) 검사를 4개 너비와 2개 상태에서 돌렸다(결과는 아래 결과 목록의 각 줄). 코드는 바꾸지 않았다.
- 업데이트 파일: DESIGN.md(C1·C2 행의 Check·Spot check·Unmeasured·Result), ROADMAP.md(R1-2 근거·다음 작업 줄), TASK.md(2026-11-15-r1-2-c1-c2 항목), REPORT.md.
- 이슈: C1 spot check가 어긋난다. 검사가 재는 상자 간격은 4px인데, 320x800 200자 캡처에서 칸 아래 테두리와 글자 사이에 보이는 간격은 9px다(글자 줄높이 여백 때문). 또 미리보기는 연결 CSS를 읽지 못해(tools/README.md) 같은 CSS를 주입해서 쟀다.
- 해결: 없음.
- 남은 문제: C1은 측정 기준이 정해지지 않아 통과로 적지 않았다(R1-2 verification pending). 연결 CSS가 그대로 로드된 화면, 199자 상태의 C1·C2, 칸 크기 조절 후, 다크 모드는 측정하지 않았다.
- 다음 작업: 제품 책임자의 C1 기준 결정(아래 질문) 뒤 C1 재판정. 이후 R1 끝 사용자 화면 확인.

design check results:
- C1 상자 간격 4px | 8/8 | 4 sizes x 2 states, light | rendered (injected css) | 320x800 200자: check 4 / observed 9 (테두리~글자 잉크, 캡처)
- C1 오른쪽 끝 맞춤 | 8/8 | 4 sizes x 2 states, light | rendered (injected css) | 320x800 200자: check 0 / observed 0 (테두리 열 303, 글자 잉크 끝 열 303, 캡처)
- C2 가로 넘침 없음 | 8/8 | 4 sizes x 2 states, light | rendered (injected css) | 320x400 200자: check scrollWidth 320 / observed scrollTo(200,0) 뒤 scrollX 0
- AC-002 글자 수 문구 | 3/3 | 2 sizes x 3 states(0자 1280, 200자 1280, 199자 375), light | rendered (injected css) | not spot-checked
- 연결 CSS 그대로 측정(대조) | 측정 불가: linkedCss loaded=false, 스타일 빠진 화면에서 상자 간격 -19 | 1 size x 1 state, light | rendered (linked css blocked) | not spot-checked

상세 보고

C1은 두 부분으로 나눠 쟀다. 오른쪽 끝 맞춤은 통과(8/8, 4 sizes x 2 states, rendered (injected css), spot check 0 / 0 일치)다. 상자 간격은 검사 수치로는 8/8(4 sizes x 2 states, rendered (injected css), spot check differs: check 4 / observed 9)이지만, 사람이 보는 간격이 9px이라 규칙 "칸 상자 아래 4px"가 글자 수 표시의 상자를 뜻하는지 보이는 글자를 뜻하는지에 따라 판정이 갈린다. 규칙의 의미는 제품 책임자가 정하므로 C1은 통과로 기록하지 않았다.

C2는 통과(8/8, 4 sizes x 2 states, rendered (injected css), spot check 일치)다. 측정값은 모두 같은 CSS를 주입한 화면에서 나왔다. 실제 브라우저가 style.css를 그대로 읽는 화면은 이 환경에서 잴 수 없어 미측정이다.

질문(사용자 부재로 보고에 남김):
1. C1의 "4px"는 글자 수 표시 상자와 칸 상자 사이 간격(현재 4px)인가, 칸 테두리와 보이는 글자 사이 간격(현재 9px)인가? 후자라면 CSS 수정(예: line-height 조정)이 필요하고, 그 수정은 다시 재야 한다.
2. 연결 CSS가 로드되는 화면에서 다시 재야 R1-2를 완료로 볼지, 주입 CSS 측정으로 충분한지 정해 달라.

report-check: ok 2,057 chars a749ca05
