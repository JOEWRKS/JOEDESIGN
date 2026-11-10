- **작업:** 출하된 `src/style.css` 값으로 DESIGN.md를 디자인 시스템 v1 DRAFT로 다시 썼습니다. 토큰 역할 표(색·글꼴·간격·외곽선·모서리·그림자·움직임), 화면 규칙 L1~B1, Rule Coverage, Report Form, 열린 결정이 들어 있고, 이전 시각 기록은 같은 파일 `이력` 절에 그대로 남겼습니다. 값은 코드에서 읽고 렌더에서 잰 measured 값이고, 토큰 이름은 proposed이며 사용자 승인은 아직 없습니다. 앱 코드와 CSS는 바꾸지 않았습니다. 측정은 Playwright 실제 Chrome으로 4크기(1440x900, 1366x768, 390x844, 360x640)와 7상태(intro, setup, tutorial, candidates, route, help, finished)에서 했습니다.
- **업데이트 파일:** `DESIGN.md`, `TASK.md`(2026-11-10 항목), `ROADMAP.md`(현재·다음 줄 다시 씀, P7 DS1 verification pending 추가), `ISSUES.md`(ENV-05). 새 스크립트 `work/design/ds-v1-audit.mjs`, `ds-v1-spot.mjs`, `ds-v1-inventory.mjs`, 캡처 `work/design/ds-v1/`. 커밋은 하지 않았습니다.
- **이슈:** (1) 엔진 파일(`public/engine/rapfi*`)이 없어 실제 엔진으로 대국 화면을 띄울 수 없었습니다. 외부에서 약 42MB를 받아야 해서 받지 않았고, test 빌드에 고정 응답을 주는 가짜 엔진을 넣어 화면 상태만 만들었습니다. (2) ENV-05: 이 폴더의 `npx vite` dev 서버가 글꼴 파일을 403으로 막아 Jua·Pretendard 대신 대체 글꼴로 그립니다(`node_modules`가 폴더 밖과 연결돼 있기 때문). 그래서 `vite build` 후 `vite preview`로 5199 포트에서 쟀습니다. (3) 출하 화면이 proposed 기준에 못 미치는 곳: 수 세기 분홍 글자 대비 2.65:1, 안내 단계 라벨 1.99:1, 44px보다 작은 컨트롤 16종(예비 착수 때 되돌리기 폭 38px 등), 동작 감소 설정 처리 없음. (4) 같은 역할인데 값이 다른 곳: 휴대폰 주 버튼 그림자 6px와 7px, 거의 같은 오류 색 두 개와 덮개 색 두 개, `--danger` 정의만 있고 안 쓰임, 이름 없이 박힌 색 57종. 말풍선 그림자 때문에 바로 아래 칸과 보이는 간격이 4px(360x640에서는 2px)밖에 안 됩니다.
- **해결:** 없음
- **남은 문제:** v1 DRAFT 사용자 승인. proposed 규칙(C1 색 토큰화, C2 대비, L3 44px, M1 동작 감소) 채택 여부. 아직 안 잰 행: H1 위계, L2 배치 전환, B1 판 표식. 실제 엔진 화면 측정. 그라데이션 배경 위 글자 대비. 독립 검토자의 규칙 범위 검토. ENV-05 dev 서버 글꼴 문제.
- **다음 작업:** 아래 질문에 답해 주시면 반영하겠습니다. ① v1 토큰·화면 규칙을 이대로 승인할지, 고칠 곳이 있는지. ② proposed 규칙 넷 중 채택할 것(채택하면 CSS 수정은 다음 작업이 됩니다). ③ 실제 엔진 화면을 재기 위해 엔진 파일(gomocalc.com, 약 42MB) 받는 것을 허락할지. ④ ENV-05를 고칠 때 Vite 설정(`server.fs.allow`)을 바꿀지, 지금처럼 build+preview로 잴지.

**디자인 검사 결과** (`check | result | sizes x states, mode | rendered or code | spot check`)

- L1 한 화면 스크롤 | 28/28 스크롤 없음 | 4 sizes x 7 states, light | rendered | 360x640 candidates: check 스크롤 없음 / observed 맨 아래 스위치가 640px 안에 보임
- E1 입체 외곽선·단단한 그림자 | 303/303 부품 ink·x0·blur0 | 4 sizes x 7 states, light | rendered | 1440x900 candidates 말풍선 아래: check 4+8 / observed 12px; 360x640: check 3+6 / observed 9px
- S1 HUD 세로 간격 | 11/11 쌍이 상자 12·10·8px, 보이는 간격 7·4·2px | 4 sizes x 7 states, light | rendered | 1440x900 candidates 말풍선→후보: check 4 / observed 4; 360x640: check 2 / observed 2
- S2 휴대폰 좌우 여백 | 14/14 대상 12px | 2 sizes x 7 states, light | rendered | 390x844 candidates 말풍선: check 12/12 / observed 12/12
- T1 글꼴 로드·외부 요청 | 28/28 Jua·Pretendard loaded, 외부 호스트 요청 0 | 4 sizes x 7 states, light | rendered | 1440x900 route: check loaded / observed `J10에 두기`가 Jua 글리프로 보임
- T2 최소 글자 | 판 밖 최소 11px, 판 안 최소 8px | 4 sizes x 7 states, light | rendered | not spot-checked
- C1 색 토큰 사용 | :root 밖 리터럴 색 57종, `--danger` 사용 0 | code | code | not spot-checked
- C2 글자 대비 AA(proposed) | 400건 중 24건 미달(수 세기 20건, 안내 단계 라벨 4건), 그라데이션 배경 102건 미측정 | 4 sizes x 7 states, light | rendered | 1440x900 candidates 수 세기: check 2.65 / observed 픽셀 2.65
- L3 누르는 크기 44px(proposed) | 44px 미만 16종, 28/28 대상에 1개 이상 | 4 sizes x 7 states, light | rendered | 1440x900 route 되돌리기: check 폭 38 / observed 38px
- M1 동작 감소(proposed) | `prefers-reduced-motion` 0곳, 무한 애니메이션 7곳 | code | code | not spot-checked

**상세 보고:** 측정 기준은 `src/style.css` git blob `fe3d5ef3`입니다. 가짜 엔진은 화면 상태를 만드는 데만 썼고, 엔진 결과나 속도는 재지 않았습니다. 코드를 바꾸지 않아 tsc·단위·E2E는 돌리지 않았습니다. 기술 측정 결과는 사용자 시각 수락이 아닙니다.
report-check: ok 3,381 chars 34daef99
