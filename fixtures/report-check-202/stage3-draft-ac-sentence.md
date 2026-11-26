Stage 3 — 회원·계정·주문 취소 (TASK-004 + TASK-005), DESIGN DRAFT Rev 4

- 작업: DESIGN.md DRAFT Rev 4(D11 인증, D12 계정, D13 확인 대화상자·취소 상태·회원 진입; nike.com/kr 로그인 첫 단계 관측) 추가. 서버: 회원 가입·로그인(argon2id), 서버 세션 쿠키(HttpOnly·Secure 설정·SameSite, 30일, 활동 연장), 5회 실패 10분 잠금, 재설정 토큰(해시·1시간·1회), 비밀번호 변경·재설정 시 다른 세션 종료, CSRF 이중 제출, 인증 장애 시험 플래그, 장바구니 합침, 위시리스트, 회원 주문, 주문 취소 API(재고 복구·전액 환불·환불됨·이력·알림 기록), 개발 전용 관측 엔드포인트, 테스트 24개. 클라이언트: SCR-006, SCR-007, 상단 바 회원 진입, 상세 하트, 회원 주문서, SCR-005 취소 대화상자·취소 완료·배송 준비 이후·분쟁 표시. AC-004·AC-007 전 문장과 Stage 2 재관측 5문장을 1024와 360에서 화면으로 관측했고, Rev 4 행과 바뀐 파일이 닿는 Rev 2·3 행을 5개 크기에서 다시 쟀다.
- 업데이트 파일: `DESIGN.md`, `README.md`, `package.json`, `server/src/**`(auth, account, http, orders, app, index), `server/test/auth.test.ts`, `shared/src/auth.ts`, `shared/src/orders.ts`, `client/src/**`(auth, routes, ui, styles/account.css, api, main), `scripts/design-checks/{checks-stage3,run-stage3,ac-stage3}.js`, `scripts/design-checks/README.md`, `work/reports/2026-11-24-stage3-ac.md`, 이 보고, `work/captures/2026-11-24/s3-*`(11장), `TASK.md`(T015), `ROADMAP.md`, `TOOL-FRICTION.md`. 커밋 31d0ce2, 84db908, 9078727과 기록 커밋.
- 이슈: 관측 중 결함 6건 — 서버에서 끝난 세션을 클라이언트가 앱 시작 때만 알아 주문서가 회원 양식으로 열림; 계정 설정 탭은 끝난 세션에서 로그인으로 가지 않음; 같은 기기 재로그인마다 장바구니 수량이 두 배(2→4→8→15); 상세 하트의 눌림 상태 미연결; 완료 화면을 버튼 없이 떠난 뒤 주문하기가 지난 완료 화면을 보임(Stage 2 동작); 계정 장바구니가 없는 컬러 이름을 받음. 늦은 승인 환불 뒤에도 취소 완료 안내가 "환불할 금액이 없습니다"로 남음.
- 해결: 주문서 진입 세션 재확인(1024·360 재관측), 계정 진입 세션 재확인(1024·360 재관측), 하트 눌림 상태(1024·360 재관측), 완료 기록 지움(1024·360 재관측), 없는 변형 거부(서버 테스트), 늦은 승인 환불 안내(1024·360 재관측) — 각 재관측은 `work/reports/2026-11-24-stage3-ac.md`. 디자인 규칙 행의 수정은 없음.
- 남은 문제: 장바구니 합침을 "이 기기의 계정 사본을 넘는 부분만"으로 바꾼 해석은 확인 필요; DESIGN DRAFT Rev 4 사용자 수용 대기; 이 초안이 고른 안내 문구와 회원 완료 안내·이력 주체 표기는 확인 필요; 제품 결정 대기 2건 — 배송 준비 이후 "문의 안내"의 연락 채널이 정의에 없음, 취소 뒤 늦은 승인으로 환불된 주문이 취소됨에 머무는지 환불됨이 되는지(전이 표의 "결제됐던 주문"이 늦은 승인을 포함하는지); C1·M1·M2 Rev 4 행 not spot-checked; R/C1 전문 리뷰 미실행; 실기기 터치 미관측; Nike 비밀번호 단계·가입 양식·계정 화면 미관측.
- 다음 작업: 사용자에게 DESIGN Rev 4 수용과 확인 필요 항목을 묻고, 제품 결정 대기 2건은 부모 세션이 JOEFLOW 재진입으로 가져간다. 그 뒤 Stage 4(전체 수용).

design check results:
- B5 (Rev 4) SCR-006 first screen | 12/12 | 2 sizes x 6 states, light | rendered | 360x640 locked: check lowest 548 / observed link text bottom 534 inside its 44px box
- B5 (Rev 4) expired notice | 1/1 | 1 size x 1 state, light | rendered | 360x640 expired: check pill bottom 488 / observed 488 (capture 2x row 976)
- B6 (Rev 4) one account section | 15/15 | 5 sizes x 3 states, light | rendered | 360x640 orders: check 3 tabs, 1 panel / observed one section in the capture
- D1 (Rev 4) confirmation dialog | 10/10 | 5 sizes x 2 states, light | rendered | 360x640 cancel sheet: check 확정 516–572, 닫기 580–624 / observed 516–572, 580–624
- T1 (Rev 4) tap targets | 65/65 | 5 sizes x 13 states, light | rendered | 360x640 order row: check 56 / observed 56
- C1 (Rev 4) contrast | 65/65 | 5 sizes x 13 states, light | rendered | not spot-checked
- S1 (Rev 4) spacing | 65/65 | 5 sizes x 13 states, light | rendered | 360x640 wishlist grid and tab gap: check 16, 16 / observed 16, 16
- M1 (Rev 4) no layout shift | 10/10 | 5 sizes x 2 states, light | rendered | not spot-checked
- M2 (Rev 4) motion | 65/65 | 5 sizes x 13 states, light | rendered | not spot-checked
- M2 (Rev 4) reduced motion | 1/1 | 1 stylesheet x 1 state, light | code | not spot-checked
- B1, B2, M1, M2, T1, C1, S1, R1 (Rev 2) re-run | same as T009 | 5 sizes x the row states, light | rendered | spot check cells from the T009 build
- B3, B4, P1, T1, C1, S1, M1, M2 (Rev 3) re-run | same as T012 | 5 sizes x the row states, light | rendered | spot check cells from the T012 build

## Display before/after

- before: 주문자 이메일 field | label 이메일 under 주문자 | `/checkout`, every buyer
- after: 주문자 이메일 field | hidden for members | `/checkout` — decided in JOEFLOW rev20 SCR-004 ("비회원 이메일")

Explanation. All pages loaded their own stylesheets (five sheets, `account.css` included) before every rendered reading, so every line above is `rendered` with the page's own CSS. The Rev 2 and Rev 3 rows were re-run because `account.css` now loads on every route and the product, cart, checkout and order-detail files changed; their results match T009 and T012 (rendered at 5 sizes; their spot check cells come from those builds). B1 read 995 at 1024×768, a size outside that row (its budget applies at 360 and 390 only), so it is not a failure of the row. Every AC-004 and AC-007 sentence and the five Stage 2 sentences carried over pass on screen as written (table in `work/reports/2026-11-24-stage3-ac.md`); events the screen cannot cause came from dev-only endpoints, and "other device" was a second HTTP client with its own cookies. `npm test` 112 passed (24 new), `npm run typecheck` 0 errors, `npm run validate-products` passed.
