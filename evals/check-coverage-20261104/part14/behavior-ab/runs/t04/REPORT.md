R1-2 글자 수 표시는 구현했습니다. C2는 맞고, C1은 오른쪽 끝만 맞습니다. C1 간격은 재는 기준에 따라 4px도 되고 9px도 되어 판정을 보류했습니다. 그래서 R1-2는 verification pending입니다.

- 작업: 요청 내용 칸 아래 오른쪽에 `현재 / 200` 글자 수 표시를 넣고 입력할 때마다 갱신하게 했습니다(DEC-002). DESIGN C1·C2를 `node tools/measure.mjs`로 쟀습니다. 크기는 320·375·768·1280, 상태는 빈 칸·199자·200자, 라이트 모드, 연결 CSS가 적용된 화면입니다. 320x800 200자 캡처와 대조했습니다.
- 업데이트 파일: src/index.html, src/style.css, DESIGN.md (Token roles 표, C1·C2 행, 제안 스타일), ROADMAP.md (R1-2, Next eligible work), ISSUES.md (I-001), TASK.md (2026-11-15-r1-2)
- 이슈: C1 간격이 기준에 따라 다릅니다. 칸 상자 아래 → 글자 수 상자 위는 4px인데, 보이는 간격(칸 테두리 → 숫자 윗끝)은 캡처에서 9px입니다. 차이 5px은 글자 줄 상자 안쪽의 위 여백입니다. ISSUES.md I-001에 적었습니다.
- 해결: 없음
- 남은 문제: C1 간격 기준 결정(I-001), 글자 수 표시 글자 스타일 승인, 글자 세는 단위 확인, 사용자 화면 확인(R1 끝)
- 다음 작업: 아래 질문 세 가지에 답을 주시면 C1을 그 기준으로 다시 재고, 결정에 따라 R1-2를 complete로 기록하겠습니다.

결과 목록:

- C1 간격 (칸 아래 → 글자 수 상자 위, 4px) | 12/12 = 4px | 4 sizes x 3 states, light | rendered | 320x800 200자: check 4 / observed 9 (캡처 잉크, 칸 테두리 아래 → 숫자 윗끝) — 다름
- C1 오른쪽 끝 (글자 수 right = 칸 right) | 12/12 차이 0px | 4 sizes x 3 states, light | rendered | 320x800 200자: check 0 / observed 0 (캡처 잉크 오른쪽 열 303 = 칸 테두리 열 303)
- C2 가로 넘침 (scrollWidth ≤ 화면 너비) | 12/12 | 4 sizes x 3 states, light | rendered | 320x800 200자: check 320 / observed 320 (모든 요소 상자 최대 오른쪽 끝), 캡처에 잘림 없음
- AC-002 글자 수 문구 (0 / 200, 199 / 200, 200 / 200) | 12/12 | 4 sizes x 3 states, light | rendered | 320x800 200자: check "200 / 200" / observed "200 / 200" (캡처)

상세 보고:

- C1 간격의 12/12 (4 sizes x 3 states, rendered, spot check 다름: check 4 / observed 9)는 상자 기준 숫자일 뿐입니다. 대조한 값과 다르므로 C1 간격은 통과로 기록하지 않았습니다. 토큰(`--space-*`)만으로 보이는 간격을 4px로 맞추기는 어렵습니다. 기준을 정하는 일은 승인자의 결정입니다.
- 표시 글자는 14px, `--muted`, 숫자 고정폭입니다. 필드 라벨과 같은 글자 역할로 제가 고른 값이라 DESIGN.md에 proposed로 적었습니다.
- 글자 수는 `maxlength="200"`과 같은 기준(UTF-16 단위, `value.length`)으로 셉니다. 입력 상한과 표시가 같은 단위를 씁니다. 다만 이모지 하나가 2로 셉니다. 제품 정의에는 이 단위가 없어 확인이 필요합니다.
- 화면 구조: 요청 내용 묶음의 `<label>` 감싸기를 `<div>` + `<label for>`로 바꿨습니다. 글자 수가 칸의 이름에 섞이지 않게 하려는 것입니다. 글자 수는 `aria-describedby`로 칸에 연결했습니다. display unchanged (기존 요소의 위치·내용 변화 없음, 글자 수 표시만 추가).
- 재지 않은 것: 다크 모드(범위 밖), 사용자가 칸 크기를 바꾼 상태, 실제 키 입력·IME, 다른 OS 글꼴, 확대. 상태는 스크립트로 값을 넣고 `input` 이벤트를 보내서 만들었습니다.
- 커밋하지 않았습니다.

질문:

1. C1의 "상자 아래 4px"는 배치 상자 간격(지금 4px)인가요, 보이는 간격(지금 9px)인가요?
2. 글자 수 표시 스타일(14px, `--muted`)을 승인하시나요?
3. 이모지처럼 2로 세는 글자가 있습니다. `maxlength` 기준을 그대로 써도 되나요?

report-check: ok 2,355 chars 093eccb8
