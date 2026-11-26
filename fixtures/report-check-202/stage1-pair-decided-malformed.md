Stage 1 3차 — rev19 반영, 재측정, AC-001~003 관측 (TASK T009)

- 작업: rev19 반영(계정 진입 비회원 메뉴 '로그인 / 주문 조회', 사이즈 표 있음/품절, 배송 안내 '5만원 이상 무료 배송, 미만 3,000원', 프레임 버튼 없음 확인, 품절 칩 #8A8A8A 토큰 행), DESIGN Rule coverage 8행을 5 크기 × 5 경로에서 재측정, AC-001·AC-002 전 문장을 1024×768·360×640에서 관측, AC-003은 검증 명령과 업로드 경로 부재로 관측. 관측 중 실패 4건과 계정 버튼 스타일 1건을 바운디드 수정하고 그 대상만 재관측.
- 업데이트 파일: `client/src/ui/AccountEntry.tsx`(새), `client/src/ui/TopBar.tsx`, `client/src/routes/ProductPage.tsx`, `client/src/routes/CatalogPage.tsx`, `client/src/hooks/useCatalogUrlState.ts`, `client/src/ui/ProductCard.tsx`, `client/src/ui/RotationStage.tsx`, `client/src/styles/app.css`, `client/src/styles/tokens.css`, `scripts/design-checks/checks.js`·`run-all.js`(새)·`README.md`, `work/captures/2026-11-24/`(캡처 32장), `work/reports/2026-11-24-stage1-ac.md`, `DESIGN.md`(토큰 행 color-soldout, Rule coverage 8행, Display before/after, Open Decisions), `TASK.md`(T009), `ROADMAP.md`(Stage 1 줄, 다음 작업), `TOOL-FRICTION.md`(2줄), 이 보고.
- 이슈: 빠른 연속 필터 변경이 앞 변경을 되돌림, 커서 아래에 그려진 카드의 호버 미리보기가 시작되지 않음, 상세에서 뒤로 오면 스크롤이 548로 돌아옴(812 기대), 세로로 시작한 터치가 회전으로 넘어감, 계정 버튼에 브라우저 기본 버튼 스타일.
- 해결: 위 5건(각각 fixed, 아래 목록의 직접 관측), 품절 칩 #8A8A8A 렌더 관측으로 C1 fixed.
- 남은 문제: AC-003 재고 차감·복구 문장 미관측(Stage 2 주문 API 필요, Stage 2로 넘길지 소유자 결정), 계정 메뉴 모양 확인 필요(승인된 증명 구성 밖의 새 요소), M2 행 not spot-checked, R/C1 전문 리뷰·독립 비평 미실행, 실기기 터치 미관측.
- 다음 작업: 위 두 결정(AC-003 재고 문장, 계정 메뉴 모양)에 대한 사용자 답, 그 뒤 Stage 1 완료 판정과 세 도구 마찰 검토.

design check results:
- B1 first screen SCR-001 | 4/4 pass (360 default 628, no-result 248; 390 default 658, no-result 248) | 2 sizes x 2 states, light | rendered (own css) | 360x640 card 4 first dot bottom: check 614 / observed 613 (capture pixel rows 598–613)
- B2 first screen SCR-002 | 8/8 pass (360 default/variant/all sold out 620, size hint 640, added 620; 390 650 x3) | 2 sizes x 5 states, light | rendered (own css) | 360x640 담기 bottom: check 620 / observed 619–620 (capture pixel rows 564–619)
- M1 no layout shift | 0 changed in every run | 5 sizes x 5 states (hover, long-press, drag, reveal, account menu), light | rendered (own css) | 360x640 account menu box: check 57.5–163.5 / observed 58–163, tabs and cards unmoved (two captures)
- M2 motion budget | pass: input 200 (menu 200), reveal 600 | 5 sizes x 1 state, light | rendered (own css) | not spot-checked
- M2 reduced motion | pass: reveal 0s | 5 sizes x 1 state, light | rendered (reduce rules injected without media) | not spot-checked
- T1 tap targets | pass: min 44x44 in every group incl. account menu items (158x44), pills 56 | 5 sizes x 3 states, light | rendered (own css) | 360x640 menu items: check 44 / observed 44 (item centres 88 to 132, capture)
- C1 contrast | pass: ink 18.88, muted 5.07 (4.72 under highlight), sale 6.54, pill 18.88, sold-out chip 3.45, menu item 18.88 | 5 sizes x 3 states, light | rendered (own css) | 360x640 sold-out chip M: check 138 (3.45) / observed strike-row pixel median 141, range 118–158 (capture)
- S1 spacing roles | pass: grid 16, section 32/48, stage to info 8 stacked (360, 390, 768) and 24 side by side (1024, 1440) | 5 sizes x 1 state, light | rendered (own css) | 360x640 grid column gap: check 16 / observed 15–16 (image edges 172 to 187/188, capture pixels)
- R1 rotation | pass: 80px = 10 frames, unchanged after release, arrows ±1, vertical-first touch leaves the frame | 5 sizes x 1 state, light | rendered (own css) | 1024x768 real mouse drag of about 79px: check 10/30 / observed rail marker at index 9 = 10/30 (capture)
- frame buttons absent (DEC-062) | 0/15 present | 5 sizes x 3 states (default, sold-out variant, all sold out), light | rendered (own css) | not spot-checked
- C1 sold-out chip #9A9A9A to #8A8A8A | fixed | 1 size x 1 state (sold-out), light | rendered (own css) | 360x640 chip M: check 138 / observed strike-row median 141 (#9A9A9A would read 154), capture `scr002-360x640-soldout-chips-M-L.png`
- account button browser default style | fixed | 2 sizes x 1 state (default), light | rendered (own css) | 1024x768 and 360x640 account button: grey fill and border before / plain icon after (captures `fix-account-button-*`)
- catalog quick successive changes | fixed | 1 size x 1 state (default), light | rendered (own css) | 1024x768 전체 then colour in one tick: `?tab=드레스` before / three changes in one tick give `?size=M` with 전체 pressed after
- hover preview on a card drawn under the pointer | fixed | 1 size x 1 state (hover), light | rendered (own css) | 1024x768 card 1 after no-result to grid: cover in 10 samples before / frames 01 to 07 after, leave gives cover
- catalog scroll on back from 상세 | fixed | 1 size x 1 state (default), light | rendered (own css) | 360x640 back from `/p/rib-knit-top`: 548 before (812 expected) / 812 and 500 after (capture `fix-scroll-restore-360-after-back-500.jpg`)
- touch axis lock on the rotation stage | fixed | 1 size x 1 state (default), light | rendered (synthetic touch pointer events) | 360x640 vertical-first then horizontal gesture: 7 frames turned before / 0 after

AC observation is in `work/reports/2026-11-24-stage1-ac.md`: every AC-001 and AC-002 sentence passes at 1024x768 and 360x640, four of them after the fixes listed above (2 sizes x 21 sentences, rendered (own css), spot check: one capture or DOM reading per sentence in that table); touch gestures there are synthetic pointer events, so native vertical page scroll on a touch device is not observed. AC-003 schema, frame paths and the absence of an upload path pass (10 products x 1 state, code: `npm run validate-products` 720 frames, 754 asset paths, and a route search showing GET routes only; not spot-checked); the stock deduction and restore sentence is 미관측, Stage 2.

## Display before/after

- before: account entry | link to `/account` (account icon) | top bar, all routes
- after: account entry | guest menu '로그인' / '주문 조회' under the account icon | top bar, all routes — decided in JOEFLOW

The account entry was replaced by the guest menu (merged the login and order lookup links under one icon); the menu's look is the 확인 필요 item below.

Technical checks: `npm test` 70 passed, `npm run typecheck` 0 errors, `npm run validate-products` passed.

확인 필요 (user-visible choices this session made that neither rev19 nor the task settles): the account menu's look and closing behaviour (popover under the icon, 160px wide, `shadow-hover`, 200ms opacity fade, closes on Esc, outside tap or item choice, '로그인' carries the return location); whether the AC-003 stock sentence moves to Stage 2's completion check. Stage 1 stays in progress until those answers; the scroll restore, axis lock and preview start implement behaviour the definition already specifies (FLOW-001, SCR-002, SCR-001).
