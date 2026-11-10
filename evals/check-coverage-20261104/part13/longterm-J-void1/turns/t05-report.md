- **작업:** 휴대폰(폭 700px 이하)에서 판 교차점과 문장 안 링크를 뺀 모든 버튼을 44×44px 이상으로 키웠습니다. 대상은 아이콘 버튼, 첫 안내·도움말·새 게임 확인·복기의 작은 버튼, 후보 알약, 승률 가이드 스위치, 고르기·글자 버튼, 예비 착수 때 38px 폭이던 되돌리기입니다. 버튼 칸이 높아지면서 키 작은 화면에서 후보 줄 그림자가 6px 잘리는 것이 보여서, 판 크기 계산에 실제 버튼 칸 높이를 넣어 판을 그만큼 줄였습니다. 검사 스크립트(`npm run check:spacing`)에 휴대폰 44px 검사와 말풍선 칸 잘림 검사를 추가했고, 도움말·새 게임 확인 창 상태도 넣었습니다. CSS만 바꿨습니다.
- **업데이트 파일:** `src/style.css`, `work/design/stack-gap-check.mjs`, `DESIGN.md`(L3 휴대폰 규칙, 토큰, Rule Coverage), `TASK.md`, `ROADMAP.md`. 커밋은 하지 않았습니다.
- **이슈:** (1) 판이 360x640 기준 몇 px 더 작아졌습니다. 버튼을 키우고도 한 화면에 들어가게 하는 대가입니다. (2) 데스크톱은 요청 범위 밖이라 그대로입니다. 작은 버튼 42px, 예비 착수 때 되돌리기 폭 38px, 브랜드 링크 28px가 남아 있습니다. (3) 측정은 이번에도 test 빌드와 가짜 엔진으로 했고, E2E는 엔진 파일이 없어 돌리지 못했습니다.
- **해결:** L3 휴대폰 버튼 44px 수정, 말풍선 칸 잘림 수정(`--cta` 보정)
- **남은 문제:** 실제 휴대폰에서 눌러 보는 확인. 데스크톱 44px 적용 여부. 앞 턴 질문(복기 바 제품 결정, LAYOUT-06 판 축소, 내 수 카드 그림자 대상, S1 값, v1 승인, 나머지 proposed 규칙, 엔진 파일 받기)도 열려 있습니다.
- **다음 작업:** 휴대폰에서 버튼 크기와 줄어든 판을 확인해 주세요. 데스크톱도 44px로 맞출지 알려 주시면 이어서 하겠습니다.

**디자인 검사 결과** (`check | result | sizes x states, mode | rendered or code | spot check`)

- L3 휴대폰 누르는 크기(적용 전) | 44px 미만 176건(20종) | 3 sizes x 11 states, light | rendered | 360x640 route 안내 줄 스위치: check 높이 38 / observed 38px; 새 게임 아이콘: check 42 / observed 42px, 캡처 픽셀
- L3 휴대폰 누르는 크기(적용 후) | 44px 미만 0건 | 3 sizes x 11 states, light | rendered | 360x640 route 안내 줄 스위치: check 44 / observed 44px; 새 게임 아이콘: check 44 / observed 44px, 캡처 픽셀
- L3 휴대폰 버튼 44px 수정 | fixed | 3 sizes x 11 states, light | rendered | 360x640 route 스위치 38 before / 44 after, 아이콘 42 before / 44 after, 캡처 픽셀
- 말풍선 칸 잘림 clipped(중간 빌드, 보정 전) | 6건(후보 줄 +6px) | 7 sizes x 11 states, light | rendered | 360x640 candidates 후보 알약 아래 남색 줄: check +6 잘림 / observed 1px만 보임(정상 7px)
- 말풍선 칸 잘림 수정(`--cta` 보정) | fixed | 7 sizes x 11 states, light | rendered | 360x640 candidates 후보 알약 아래 남색 줄: 1px before / 7px after, 캡처 픽셀
- S1·R1 세로 쌓기 간격(재실행) | 221/221쌍 | 7 sizes x 11 states, light | rendered | not spot-checked
- 페이지 스크롤·복기 바 넘침 | 0 | 7 sizes x 11 states, light | rendered | not spot-checked

**상세 보고:** `src/style.css` git blob은 `7667e322`입니다. 적용 전 수치는 같은 소스에서 이번 휴대폰 블록만 뺀 빌드로 쟀습니다. TS 코드를 바꾸지 않아 tsc·단위 검사는 돌리지 않았습니다. 기술 검사 결과는 사용자 시각 수락이 아닙니다.
report-check: ok 2,212 chars 409d8d1f
