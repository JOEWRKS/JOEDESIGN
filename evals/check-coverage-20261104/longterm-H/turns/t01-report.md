DESIGN.md 맨 위에 디자인 시스템 v1을 DRAFT로 작성했습니다. `src/style.css` 값에서 토큰 60행(색 31·글꼴 11·간격/모서리/테두리 9·그림자/움직임 9)과 화면 규칙 12개를 정리했습니다. 실제 렌더 측정에서 규칙에 어긋나는 곳 2개(글자 대비, 동작 감소)를 찾았습니다. 화면 코드는 바꾸지 않았고, 승인은 아직 받지 않았습니다.

- 작업: JOEDESIGN 절차로 출하된 `src/style.css`를 읽고 프로덕션 빌드를 브라우저에서 렌더해 값을 재고, DESIGN.md 맨 위에 "디자인 시스템 v1 (DRAFT Rev 1)"을 썼습니다. 들어간 것은 출처·승인 범위, 토큰 역할 표(모든 값 measured), 화면 규칙 12개(한 화면, 배치, 위계, 색은 토큰에서만, 표면 재질, 글꼴, 최소 글자, 누르는 크기, 대비, 판 위 표식, 말풍선 간격, 동작 감소), 규칙 점검 범위 표, 열린 결정입니다. 옛 v0.1~v0.3은 "이력"으로 내리고 내용은 그대로 두었습니다. 측정 스크립트 2개를 추가했습니다.
- 업데이트 파일: `DESIGN.md`, `ISSUES.md`(DES-01·DES-02 추가), `ROADMAP.md`(P7 DS1·DS2 추가, 현재·다음 줄 다시 씀), `TASK.md`(2026-11-09 항목), 새 파일 `work/design/system-audit.mjs`, `work/design/system-spot.mjs`, `work/design/system-audit-v1.log`, `work/design/system-spot-v1.log`. 커밋하지 않았습니다.
- 이슈: DES-01 — 단색 바탕 위 글자 2곳의 대비가 기준에 못 미칩니다(수 세기 `#move-count` 2.65:1, 첫 안내 단계 `#tut-step` 1.99:1). DES-02 — 동작 감소 설정을 켜도 판 위 고리가 계속 돕니다. 환경 문제도 2개 있습니다. 이 폴더의 `node_modules`가 폴더 밖을 가리켜서 `npx vite` dev 서버가 글꼴 파일을 403으로 거절합니다. 그래서 `vite build` 뒤 `vite preview`를 같은 5099 포트에 띄워 쟀습니다. 또 엔진 파일 `public/engine/rapfi*`가 없어서, 대국 화면은 가짜 엔진 Worker로 만들었습니다(후보·승률 값은 가짜).
- 해결: 없음
- 남은 문제: v1의 사용자 승인. DES-01·DES-02(고칠지와 기준을 정해 주셔야 함). 규칙 2(배치)·3(위계)·10(판 위 표식)은 점검 수단이 없어 측정하지 못했습니다. 종료·복기·내 수 검토·AI 차례·새 게임 확인·엔진 실패·가이드 끔 상태도 재지 못했습니다. 실제 엔진이 필요한 E2E와 `capture-matrix.mjs`는 실행하지 못했습니다.
- 다음 작업: 아래 질문에 답해 주시면 v1을 확정하고, 정하신 대로 DES-01·DES-02를 고친 뒤 같은 점검을 다시 돌리겠습니다.

design checks:
- color tokens | 11518/11518 | 12 sizes x 6 states, light | rendered | 1440x900 candidates .who.on fill: check rgb(255,210,63) / observed pixel #FFD23F
- shadow material | 1108/1108 | 12 sizes x 6 states, light | rendered | 1440x900 setup #main-action: check shadow 7px / observed 7 ink rows below the 4px border
- font family | 3195/3195 | 12 sizes x 6 states, light | rendered | 1440x900 setup #main-action: check computed Jua / observed capture differs from sans-serif capture, Jua shapes in crop
- text min 11px | 1533/1533 | 12 sizes x 6 states, light | rendered | 1440x900 candidates .coach-note: check 12px / observed ink height 11px
- control height | 564/564 | 12 sizes x 6 states, light | rendered | 1440x900 setup #main-action: check 76px / observed 83px = 76 + 7 shadow
- text contrast | 1191/1251 | 12 sizes x 6 states, light | rendered | 1440x900 tutorial #tut-step: check 1.99 / observed 1.99 from pixels
- one screen | 72/72 frames no scroll | 12 sizes x 6 states, light | rendered | 390x844 candidates: check scrollHeight 844 / observed full-page capture 390x844
- hud spacing | box 12/10/8, visible 4 or 7 | 12 sizes x 2 states, light | rendered | 1440x900 candidates bubble to pills: check 4 / observed 4
- reduced motion | 0/2 still | 2 sizes x 1 state, light | rendered | 1440x900 preview ring J10: check spin / observed captures differ

상세 보고:
- 모든 토큰은 출하 코드에서 읽은 measured 값이고 approved가 아닙니다. CSS 변수가 없는 색 17개는 `ink-text` 같은 이름을 제가 붙였습니다. 정의만 되고 쓰이지 않는 `--danger`도 있습니다.
- 정해 주실 것: (1) 글자 대비 기준 4.5:1을 채택할지 (2) 동작 감소 처리를 넣을지 (3) 말풍선 아래 보이는 틈 4px와 내 수 카드 아래 7px를 맞출지 (4) 변수 없는 색을 CSS 변수로 올리고 `--danger`를 지울지 (5) 엔진 파일을 외부 사이트에서 내려받아도 되는지. 받아도 되면 실제 엔진으로 E2E와 판 위 표식 규칙을 다시 재겠습니다.
- 간격은 2~24px 사이 12단계가 쓰이고 있어 8의 배수 체계가 아닙니다. 그대로 기록만 했습니다.
report-check: ok 3,239 chars fcc21109
