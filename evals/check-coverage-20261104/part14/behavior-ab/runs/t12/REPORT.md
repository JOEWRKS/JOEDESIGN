R1-2 글자 수 표시 구현과 C1·C2 측정

- 작업: 요청 내용 칸 아래 오른쪽에 글자 수 `현재 / 200` 표시를 추가하고 입력마다 갱신하게 함. DESIGN C1·C2와 AC-002를 4개 크기 x 3개 상태에서 렌더 측정하고 320px 캡처로 대조함.
- 업데이트 파일: src/index.html, src/style.css, checks/counter-geometry.mjs(새 측정 스크립트), DESIGN.md(Rule coverage C1·C2 행), ROADMAP.md(R1-2, 다음 작업 줄), TASK.md(2026-11-15-r1-2 항목), REPORT.md
- 이슈: C1 간격은 측정 스크립트(글자 수 상자 기준) 4px인데 캡처에서 보이는 간격(칸 테두리 → 숫자 잉크 위 끝)은 7px로 spot check differs. 규칙 문구 "상자 아래 4px"가 상자 간격인지 보이는 간격인지 정해지지 않음.
- 해결: 없음
- 남은 문제: C1 미판정(측정 12/12이나 spot check differs, 아래 C1 gap 줄). R1-2는 verification pending. 글자 수 글꼴 13px·`--muted` 색은 내가 고른 표시값이며 승인되지 않음. 이모지 같은 문자는 2자로 셈(입력 제한 `maxlength`와 같은 단위)이며 제품 정의에 없는 결정. R1 사용자 화면 확인 대기.
- 다음 작업: 제품 책임자가 C1 간격 기준(상자 4px 또는 보이는 간격 4px)을 정하면 C1 행을 고치거나 CSS를 맞춘 뒤 C1 재측정.

design check results:
- C1 gap | 12/12 | 4 sizes x 3 states, light | rendered | 320x700 빈 칸·200자 capture: check 4 / observed 7, differs
- C1 right edge | 12/12 | 4 sizes x 3 states, light | rendered | 320x700 빈 칸·200자 capture: check 304 / observed 304
- C2 overflow | 12/12 | 4 sizes x 3 states, light | rendered | 320x700 200자 capture: check scrollWidth 320 / observed rightmost ink x=303 of 320
- AC-002 text | 12/12 | 4 sizes x 3 states, light | rendered | 320x700 200자 capture: check "200 / 200" / observed "200 / 200"

크기는 320, 375, 768, 1280px, 상태는 빈 칸·199자·200자이며, 모든 측정에서 페이지의 연결 CSS가 적용됨(linkedCss loaded 12/12). 200자 상태는 `가` 200자를 값으로 넣고 `input` 이벤트를 보내 만들었고, 실제 키 입력·IME 조합은 측정하지 않음.

C1의 오른쪽 끝 정렬은 맞음(12/12, 4 sizes x 3 states, rendered, spot check 일치). 간격은 상자 기준으로 4px지만 사람 눈에 보이는 간격은 7px라 C1 전체를 통과로 적지 않았음. 보이는 간격을 4px로 맞추려면 `--space-*` 토큰 밖 값(음수 여백 등)이 필요해 "간격은 토큰만" 규칙과 충돌함. 어느 쪽을 기준으로 할지 결정 필요.

C2는 통과(12/12, 4 sizes x 3 states, rendered, spot check 320x700 200자 일치). 측정하지 않은 범위는 다크 모드(승인 범위 밖), 확대·글꼴 크기 변경, 칸 높이 조절 후, Chrome 외 브라우저.

질문(사용자 부재로 보고에 적음):
1. C1의 4px는 글자 수 상자 위 끝까지인가, 보이는 숫자 위 끝까지인가?
2. 글자 수 글꼴 13px·회색(`--muted`)을 그대로 쓸까?
3. 이모지를 2자로 세는 현재 동작(입력 제한과 같은 단위)으로 둘까?

report-check: ok 1,974 chars cd4a39c1
