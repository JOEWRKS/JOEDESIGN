- 작업: R1-2 글자 수 표시의 DESIGN 규칙 C1(위치)·C2(넘침)와 AC-002 표시 문구를 렌더 측정. 코드는 바꾸지 않음. 이 미리보기는 `<link>` CSS를 읽지 못하므로(측정 출력 `linkedCss.loaded: false`) tools/README.md대로 `--inject src/style.css`로 같은 CSS를 주입해 잼. 주입 없이 잰 값(간격 -19px, 오른쪽 차이 55~73px)은 스타일이 빠진 화면이라 결과로 쓰지 않음.
- 업데이트 파일: DESIGN.md(C1·C2 행의 Check·Spot check·States·Unmeasured·Result), ROADMAP.md(R1-2 근거·다음 작업 줄), TASK.md(2026-11-15-r1-2-check 항목), evidence/2026-11-15-r1-2/(measure-log.txt, 캡처 4장), REPORT.md.
- 이슈: 없음. 측정에서 규칙 어긋남은 나오지 않음(결과는 아래 목록).
- 해결: 없음(고친 것 없음).
- 남은 문제: 측정은 모두 주입 CSS 방식이라, 실제 `<link>`로 CSS가 로드된 화면은 관찰하지 못함(같은 파일이고 다른 스타일 시트가 없어 값이 같을 것으로 보지만 추정). 다른 글꼴, 브라우저 확대, 사용자가 칸 크기를 조절한 상태도 미측정. 그래서 R1-2는 verification pending으로 둠. 사용자 화면 확인(R1 끝)은 별도.
- 다음 작업: 질문 — 주입 CSS 측정을 R1-2 완료 근거로 인정할까요? 인정하면 R1-2를 complete로 바꾸고, 아니면 연결 CSS가 로드되는 환경에서 C1·C2를 다시 잼.

결과 목록:

- C1 글자 수 위치(간격 4px, 오른쪽 끝 일치) | 12/12 | 4 sizes (320, 375, 768, 1280) x 3 states (빈 칸, 199자, 200자), light | rendered (injected css) | 320x700 200자: check 4px·0 / observed 4px·0 (캡처에서 칸 아래 테두리 행 303, 글자 수 상자 시작 행 308, 오른쪽 끝 열 303 = 303); 1280x700 200자도 check 4px·0 / observed 4px·0
- C2 넘침 없음(scrollWidth ≤ 화면 너비) | 12/12 | 4 sizes (320, 375, 768, 1280) x 3 states (빈 칸, 199자, 200자), light | rendered (injected css) | 320x700 200자: check scrollWidth 320 / 화면 320, observed 캡처의 가장 오른쪽 내용 열 303(오른쪽 여백 16px), 잘린 요소 없음
- AC-002 표시 문구(0 / 200, 199 / 200, 200 / 200) | 12/12 | 4 sizes (320, 375, 768, 1280) x 3 states (빈 칸, 199자, 200자), light | rendered (injected css) | 320x700 200자 캡처에서 `200 / 200` 보임: check 200 / 200, observed 200 / 200

C1 스폿 체크는 글자 수 요소에 자홍 배경을 임시로 칠한 캡처에서 픽셀 행·열을 읽은 것(파일은 고치지 않음). 규칙이 말하는 것은 상자 간격이고, 글자 잉크와 칸 테두리 사이는 줄 높이 때문에 4px보다 넓게 보임.

report-check: ok 1,696 chars 3645c2f2
