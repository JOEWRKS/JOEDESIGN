결론: 출시 전 기준으로는 아직 아니다. DESIGN의 번호 규칙 14개 중 실제 렌더 화면에서 재서 확인된 것은 9개, 일부만 확인된 것 3개, 확인되지 않은 것 4개다. 지금 실패 중인 검사도 3개다. 모든 대국 화면은 가짜 엔진으로 띄운 화면이라 실제 엔진·실기기에서 본 것은 하나도 없다. 이번 턴에 npm run design:check -- --all(13크기)을 새로 돌려 아래 표를 채웠다. 표의 숫자 범위는 맨 아래 결과 목록 줄과 같다.

| DESIGN 규칙 | 실제 화면 확인 | 확인 방법 | 빠진 부분 |
| --- | --- | --- | --- |
| 1 한 화면, 스크롤 없음 | 확인 | spacing 넘침, tokens DS-O | 실제 엔진의 긴 문구, 실기기 주소창 |
| 2 위계 | 미확인 | 1차 턴에 캡처 2장을 사람 눈으로 본 것뿐 | 대국 화면 위계 판단 없음 |
| 3 핵심 정보만 | 미확인 | 검사 없음 | 전부 |
| 4 카툰 입체 표현 | 일부 | shadow, press, tokens 외곽선 | 흐린 그림자는 판만 쓴다는 조건 |
| 5 판 위 표식(점선·반투명 돌) | 미확인 | 맡은 E2E를 엔진 파일이 없어 못 돌림 | 전부 |
| 6 색만으로 구별하지 않기 | 미확인 | 검사 없음 | 전부 |
| 7 글꼴 역할 | 일부 | tokens(시작 화면 2요소) | 대국 화면 숫자·버튼 글꼴 |
| 8 크기 전환 | 일부 | tokens(역할 9개의 데스크톱/휴대폰 값) | 대국 화면 역할 |
| 8-1 휴대폰 가로 | 확인(844x390) | 13크기 실행에 포함 | 740x360 복기 잘림(DS-08), 동작 감소 흔들림(TEST-10) |
| 9 조작 크기 하한 | 확인 | spacing touch, tokens DS-H | 데스크톱·태블릿 44px 여부 미정 |
| 10 동작 감소 | 확인(실패 1) | motion | 844x390 흔들림(TEST-10) |
| SP-1 블록 사이 간격 | 확인 | spacing, 픽셀 스폿 | 실제 엔진 문구 |
| SP-2 칸 사이 간격 | 확인 | spacing(복기 바 포함) | 같음 |
| SP-3 같은 역할 같은 그림자 | 확인 | shadow 주 버튼 묶음 | 없음 |

번호 없는 규칙:

| DESIGN 규칙 | 실제 화면 확인 | 확인 방법 | 빠진 부분 |
| --- | --- | --- | --- |
| 토큰 역할 표 | 일부 | tokens(시작 화면 위주) | 대국 화면 역할 대부분 |
| 그림자 역할 | 확인 | shadow | 판 안 돌·표식 |
| 추천 고리 색 | 확인 | ring | 없음 |
| 판 위 표식 대비 | 실패 | board-marks: 금수 ✕(DS-06) | 고쳐야 함 |
| 글자·조작 대비(라이트·다크) | 실패 | contrast: 좌표 글자·첫 안내(DS-05), 수 세기 분홍(DS-01), '이유 더 보기' 조작 경계(DS-09, 새로 찾음) | 고쳐야 함 |
| 다크 모드 | 일부 | contrast·board-marks만 다크로 잰다 | 다른 검사는 라이트만 |
| 말풍선 글자 12px | 확인 | bubble-text | 말풍선 밖 11px 글자는 규칙 밖 |
| 눌림 효과 | 확인 | press | 키보드·실제 터치 |
| 복기 상단 바 | 확인 | spacing 복기 상태 | 복기 E2E 미실행 |
| 도움말 카드 | 확인 | shadow·넘침 | 없음 |
| 이유 더 보기 | 일부 | spacing 펼친 상태 | 버튼이 보이는 조건 자체, 다시 접기 |
| 판 격자선 진하기 | 일부 | 손으로 2크기 측정 | 검사에 없음 |

출시를 막는 것 네 가지:
(1) 실패 중인 검사 3개(금수 ✕ DS-06, 대비 DS-05·DS-01·DS-09, 동작 감소 흔들림 TEST-10).
(2) 확인 안 된 규칙 4개(2·3·5·6).
(3) 실제 엔진 화면·E2E·실기기 확인 0(엔진 파일 없음, ENV-06).
(4) 사용자 승인: DESIGN은 DRAFT이고 승인된 것은 간격 규칙뿐이다. product decision pending(다크 모드, 복기 상단 바, 이유 더 보기)도 남아 있다.

- 작업: DESIGN.md 규칙 전부를 검사·캡처 기록과 대조해 위 표로 정리했다. 최신 상태로 채우려고 디자인 검사 전체를 13크기로 다시 돌렸다. 새로 찾은 문제 두 가지는 ISSUES에 올렸다.
- 업데이트 파일: ISSUES.md(DS-09, TEST-10 open), TASK.md(2026-11-10 출시 전 점검), ROADMAP.md(현재·다음 줄).
- 이슈: 새로 찾은 문제는 두 가지다. '이유 더 보기' 글자 버튼에 테두리가 없어 대비 검사가 조작 경계 미달로 잡는다(DS-09). 이것이 검사 기준을 고칠 일인지, 버튼 모양을 바꿀 일인지 정해야 한다. 그리고 동작 감소 검사가 844x390에서 다시 흔들렸다(TEST-10).
- 해결: 없음
- 남은 문제: 위 "출시를 막는 것" 네 가지와 ROADMAP 다음 작업 줄의 나머지 열린 항목.
- 다음 작업: 막는 것 중 먼저 할 것을 정해 준다. 고치기만 하면 되는 것은 금수 ✕와 대비 결함(DS-06·DS-05·DS-01·DS-09)이다. 엔진 파일 받기를 허락하면 (3)을 시작할 수 있다.

design-check results:
- design:check --all | 7/10 PASS; FAIL board-marks, contrast, motion | 13 sizes x up to 14 states, light and dark (stub engine) | rendered | not spot-checked this turn
- spacing, overflow, touch | 560/560 pairs, 177/177 states clean, 636/636 buttons | 13 sizes x 13-14 states, light | rendered | not spot-checked this turn
- tokens and DS-O | 230/230, 26/26 | 13 sizes x intro and help | rendered | not spot-checked this turn
- shadow, ring, bubble-text, press | 65/65, 13/13, 391/391, 169/169 | 13 sizes | rendered | not spot-checked this turn
- board-marks | 26/52, forbidden mark fails (DS-06) | 13 sizes x 1 state x light and dark | rendered | not spot-checked this turn
- contrast | 26/182 states clean; DS-05, DS-01, reason-toggle boundary 1.00:1 (DS-09) | 13 sizes x 7 states x light and dark | rendered | not spot-checked
- motion | 25/26, 844x390 reduce pixels changed with 0 running animations (TEST-10) | 13 sizes x 2 states x reduce and control | rendered | not spot-checked
report-check: ok 3,625 chars 7e0a0bf4
