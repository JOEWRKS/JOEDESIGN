- **작업:** 메인 화면 세로 줄(카드·후보 줄·복기 칸 → 버튼 줄 → 되돌림 안내 → 안내 줄, 시작 화면 카드→버튼)의 간격 규칙 S1을 정하고 `src/style.css`를 맞췄습니다. 규칙은 "보이는 간격", 즉 위 요소의 그림자 끝에서 아래 요소 위끝까지를 `--stack`으로 같게 하는 것입니다. 값은 12px, 폭 700px 이하 10px, 높이 700px 이하 8px입니다. 원인은 상자 간격은 같아도 버튼(7px)·말풍선(8px) 그림자가 그 간격을 먹어서, 사람 눈에는 1px부터 22px까지 제각각으로 보였던 것입니다. 그래서 그림자 깊이를 토큰(`--drop-bubble`·`--drop-card`·`--drop-cta`)으로 만들고, 각 요소 아래 여백에 자기 그림자 깊이를 더했습니다. 대국 화면에서 말풍선 칸과 버튼 칸 사이는 남는 높이를 받는 자리라 `--stack` 이상이면 됩니다. 재발을 막는 검사 `work/design/stack-gap-check.mjs`(`npm run check:spacing`)를 추가했습니다. 7개 크기와 8개 상태에서 보이는 간격을 재고, 위반이 있으면 종료 코드 1을 냅니다. 페이지 스크롤도 함께 봅니다.
- **업데이트 파일:** `src/style.css`, `package.json`(check:spacing), `DESIGN.md`(S1 규칙, 간격·그림자 토큰, Rule Coverage), `TASK.md`, `ROADMAP.md`, `ISSUES.md`(LAYOUT-06). 새 파일 `work/design/stack-gap-check.mjs`, `fake-engine.mjs`, `png-column.mjs`, 캡처 `work/design/stack/`. 커밋은 하지 않았습니다.
- **이슈:** (1) LAYOUT-06: 375x667·360x640 화면에서 복기를 시작하면 말풍선이 말풍선 칸에 잘려 해설이 가려집니다. 적용 전부터 있던 문제인데, 간격이 늘면서 잘리는 양이 23px에서 34px로 늘었습니다. 검사에 남은 실패 2쌍이 이것입니다. (2) 함께 바뀐 것: 휴대폰의 `두기`·비활성 버튼 그림자를 7px에서 6px로 맞췄고, 금수 알림·엔진 알림의 아래 여백 8px를 칸 간격으로 대신했습니다. 알림 두 상태는 재지 못했습니다. (3) 엔진 파일이 없고(ENV-05로 dev 서버 글꼴도 막혀 있음) test 빌드 + 가짜 엔진 + `vite preview`(5199)로 측정했습니다.
- **해결:** S1 간격 맞춤 수정, 휴대폰 주 버튼 그림자 통일
- **남은 문제:** S1 값(12/10/8px)의 사용자 확인. LAYOUT-06. 알림·제한 안내 상태와 세로형 태블릿 크기는 아직 재지 않았습니다. 실제 엔진 화면과 E2E는 돌리지 못했습니다. 지난 턴의 v1 승인과 proposed 규칙 채택 질문도 아직 열려 있습니다.
- **다음 작업:** ① S1 간격 값을 이대로 둘지 정해 주세요. ② LAYOUT-06은 복기 중 판을 줄일지, 복기 칸이나 말풍선 내용을 접을지 정해 주세요. 접는 쪽은 보이는 내용이 바뀌어서 제품 결정입니다. ③ 지난 턴 질문(v1 승인, proposed 규칙, 엔진 파일 42MB 받기)도 아직 답을 기다립니다.

**디자인 검사 결과** (`check | result | sizes x states, mode | rendered or code | spot check`)

- S1 세로 쌓기 간격(적용 전) | 44/142쌍 | 7 sizes x 8 states, light | rendered | 1440x900 route 버튼 줄→안내 줄: check 1 / observed 1px; 360x640 candidates 말풍선→후보: check 2 / observed 2px
- S1 세로 쌓기 간격(적용 후) | 140/142쌍, 실패 2쌍은 375x667·360x640 replay 말풍선 잘림(LAYOUT-06) | 7 sizes x 8 states, light | rendered | 1440x900 route 버튼 줄→안내 줄: check 12 / observed 12px; 360x640 candidates 말풍선→후보: check 8 / observed 8px
- S1 간격 맞춤 수정 | fixed | 7 sizes x 8 states, light | rendered | 1440x900 route 버튼 줄→안내 줄: 1 before / 12 after, 캡처 픽셀; 360x640 candidates 말풍선→후보: 2 before / 8 after, 캡처 픽셀
- 휴대폰 주 버튼 그림자 통일 | fixed | 2 sizes x 7 states, light | rendered | 390x844 route 두기 버튼 아래 남색 줄: 7 before(11px) / 6 after(10px), 캡처 픽셀
- L1 페이지 스크롤(곁 검사) | 0/56 스크롤 | 7 sizes x 8 states, light | rendered | 375x667 undone 캡처: check 스크롤 없음 / observed 안내 줄 스위치가 667px 안에 보임
- E1 입체 외곽선·그림자(재실행) | 303/303 | 4 sizes x 7 states, light | rendered | 360x640 candidates 말풍선 아래: check 3+6 / observed 9px
- T1·T2·C2·L3·S2(재실행) | 적용 전과 같은 수치(대비 미달 24/400, 44px 미만 16종) | 4 sizes x 7 states, light | rendered | not spot-checked

**상세 보고:** `src/style.css` git blob이 `fe3d5ef3`에서 `2368f017`로 바뀌었습니다. 판 크기와 화면 배치 순서는 그대로입니다. TS 코드를 바꾸지 않아 tsc·단위 검사는 돌리지 않았고, E2E와 12크기 capture-matrix는 실제 엔진이 있어야 해서 돌리지 않았습니다. 기술 검사 결과는 사용자 시각 수락이 아닙니다.
report-check: ok 2,979 chars b862476d
