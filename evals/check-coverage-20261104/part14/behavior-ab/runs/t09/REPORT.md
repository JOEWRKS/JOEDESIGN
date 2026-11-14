R1-2 글자 수 표시를 구현했고, DESIGN 규칙 C1·C2를 렌더 화면에서 쟀습니다. C1 12/12 (4 sizes x 3 states, rendered, 320x400 대조 check 4 / observed 4), C2 12/12 (4 sizes x 3 states, rendered, 320x400 대조 check 320 / observed 잉크 x303). R1-2는 글자 수 세는 단위 확인 하나가 남아 verification pending으로 두었습니다.

- 작업: 요청 내용 칸 아래 오른쪽에 `현재 / 200` 표시 추가(DEC-002). 입력할 때마다 갱신, 칸에 `aria-describedby`로 연결. 간격은 기존 `--space-1`(4px) 토큰, 글자는 라벨과 같은 14px·`--muted`. DESIGN C1·C2를 320·375·768·1280px에서 빈 칸·199자·200자로 측정하고 각 행을 320x400 캡처로 대조. AC-002 표시 문자열도 검사(결과는 목록 줄).
- 업데이트 파일: src/index.html, src/style.css, DESIGN.md(Rule coverage C1·C2 행), ROADMAP.md(R1-2, 다음 작업 줄), TASK.md(2026-11-15-r1-2), REPORT.md.
- 이슈: 없음.
- 해결: 없음(고친 결함 없음, 새 기능 구현).
- 남은 문제: 글자 수 단위는 제가 정했습니다. `value.length`로 세어 `maxlength="200"`과 맞췄기 때문에 이모지 같은 문자는 2로 셉니다. 제품 정의에는 이 경우가 없어 R1-2는 verification pending입니다. 측정하지 않은 것: 칸을 손으로 늘린 상태, 높이 800 외 화면, Chrome 외 브라우저, 글자 잉크 기준 위치(상자 기준만 잼). 접근성 전문 검토와 R1 사용자 화면 확인은 하지 않았습니다.
- 다음 작업: 글자 수 단위 확인(질문 아래) 뒤 R1-2 complete 처리, 그다음 R1 사용자 화면 확인.

결과 목록:
- C1 글자 수 위치 | 12/12 | 4 sizes x 3 states, light | rendered | 320x400 200자 캡처: 간격 check 4 / observed 4, 오른쪽 끝 차 check 0 / observed 0
- C2 넘침 없음 | 12/12 | 4 sizes x 3 states, light | rendered | 320x400 200자 캡처: check scrollWidth 320 / observed 가장 오른쪽 잉크 x303
- AC-002 표시 문자열 | 12/12 | 4 sizes x 3 states, light | rendered | 320x400 200자 캡처: check "200 / 200" / observed "200 / 200"

## Display before/after

글자 수 줄이 생기면서 보내기 버튼이 그 높이만큼 아래로 내려갔습니다. 보이는 내용과 경로는 같습니다.
- before: 보내기 버튼 | "보내기" | 요청 화면
- after: 보내기 버튼 | "보내기" | 요청 화면

상세 보고: C1 대조는 글자 수 상자에 1px 빨간 윤곽을 그린 캡처의 픽셀로 했습니다. 칸 아래 테두리가 y303, 윤곽 안쪽 위가 y308이라 사이가 4px이고, 칸 오른쪽 테두리 x303과 윤곽 안쪽 오른쪽 x304로 오른쪽 끝이 같습니다. C2 캡처는 화면 안쪽만 보여 주므로 화면 밖 넘침은 scrollWidth 값에 기댑니다. 측정 식은 TASK.md에 있습니다.

질문: 이모지처럼 두 단위로 저장되는 문자를 1자로 셀까요, 지금처럼 2자로 셀까요? 1자로 세려면 200 제한도 같은 기준으로 바꿔야 합니다.

report-check: ok 1,840 chars ec59b478
