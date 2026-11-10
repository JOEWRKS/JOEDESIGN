- **작업:** 복기 모드에만 나오는 상단 바를 판 위 전체 폭에 넣었습니다. 바에는 "N수 / 총 M수"와 기존 `◀ 이전 수`·`다음 수 ▶`·`종료 판으로` 버튼이 있습니다. 버튼은 같은 id로 바에 옮겨서 동작·포커스·E2E 선택자가 그대로입니다. 바 아래 간격은 지난 턴 간격 규칙(`--stack`)을 따르고, 판은 바 높이만큼 작아집니다. 복기 버튼이 빠지면서 복기 칸은 상황 글 두 줄만 남았습니다. 키 작은 휴대폰에서 복기 말풍선이 잘리던 문제(LAYOUT-06)는 복기 중 판을 조금 더 줄이는 방법으로 함께 고쳤습니다. 간격 검사 스크립트에 복기 바 아래 간격, 바 안 넘침, 복기 진행 중 상태를 추가했습니다.
- **업데이트 파일:** `src/main.ts`, `src/style.css`, `work/design/stack-gap-check.mjs`, `DESIGN.md`(R1 규칙, Display before/after, Rule Coverage), `TASK.md`, `ROADMAP.md`(P8 RP1), `ISSUES.md`(LAYOUT-06). 커밋은 하지 않았습니다.
- **이슈:** (1) 승인된 기획서(JOEFLOW rev 20)에는 복기 상단 바가 없어서 product decision pending입니다. 요청하신 대로 만들었고, 기획 갱신은 JOEFLOW 재진입으로 따로 해야 합니다. (2) 요청에 없던 부분은 제가 정했습니다: 바 위치(판 위 전체 폭), 수 표시 형식, 복기 칸 상황 글 유지, 키 작은 화면에서 판 축소(360x640에서 판 약 180px). (3) 엔진 파일이 없어 E2E `replay.spec.ts`는 돌리지 못했습니다. 측정은 test 빌드와 가짜 엔진, 기록 없는 고정 국면으로 했고, 그래서 복기는 0수와 9수 두 칸만 확인했습니다.
- **해결:** LAYOUT-06 복기 말풍선 잘림 수정
- **남은 문제:** 복기 상단 바의 제품 결정(JOEFLOW 반영)과 배치·표시 형식 사용자 확인. LAYOUT-06 판 축소 방법 사용자 확인(이슈는 그때까지 열어 둡니다). 실제 엔진 E2E. 앞 턴 질문(내 수 카드 그림자 대상, S1 값, v1 승인, proposed 규칙, 엔진 파일 받기)도 열려 있습니다.
- **다음 작업:** 복기 화면을 써 보시고 ① 바 위치·표시 형식이 괜찮은지, ② 키 작은 화면에서 복기 중 판이 작아지는 것을 받아들일지, ③ 이 바를 기획서(JOEFLOW)에 올릴지 알려 주세요.

## Display before/after

- before: 복기 이전 수·다음 수·종료 판으로 버튼 | `◀ 이전 수`·`다음 수 ▶`·`종료 판으로` | 대국 종료 → `대국 복기` → 말풍선 칸의 복기 칸 안
- after: 복기 이전 수·다음 수·종료 판으로 버튼 | `◀ 이전 수`·`다음 수 ▶`·`종료 판으로` | 대국 종료 → `대국 복기` → 판 위 복기 상단 바
- before: 복기 상단 바 | hidden | 없음
- after: 복기 상단 바 | `N수 / 총 M수` + 위 버튼 3개 | 대국 종료 → `대국 복기` → 판 위

두 쌍 모두 달라서 product decision pending입니다.

**디자인 검사 결과** (`check | result | sizes x states, mode | rendered or code | spot check`)

- S1·R1 세로 쌓기 간격과 복기 바 | 177/177쌍 | 7 sizes x 9 states, light | rendered | 1440x900 replay-mid 바→복기 칸: check 12 / observed 12px; 360x640 replay-mid 바→판: check 8 / observed 8px, 캡처 픽셀
- 페이지 스크롤·복기 바 넘침(곁 검사) | 0/63 | 7 sizes x 9 states, light | rendered | 360x640 replay 캡처: check 넘침 없음 / observed `종료 판으로`가 바 오른쪽 외곽선 안에 보임
- LAYOUT-06 복기 말풍선 잘림 수정 | fixed | 2 sizes x 2 states, light | rendered | 360x640 replay: 말풍선 아래 외곽선 before 잘려 안 보임 / after 보임, 캡처
- 복기 흐름(진입 포커스·버튼 위치·수 표시·종료 판으로 복귀) | 2/2 크기 정상 | 2 sizes x 1 state, light | rendered | not spot-checked

**상세 보고:** `npx tsc --noEmit`이 통과했고, `npx vitest run`은 87개 통과·1개 건너뜀입니다. `src/style.css` git blob은 `f22135df`입니다. 기술 검사 결과는 사용자 시각 수락이 아닙니다.
report-check: ok 2,378 chars 7d0edfe2
