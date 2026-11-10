# 디자인 시스템 v1 — 함께 배우는 AI 오목

**Reporting:** follow the `## Report Form` section below exactly (보고는 `## Report Form` 절을 그대로 따른다).

**Status:** DRAFT — 아래 값은 출하 코드에서 읽고 렌더에서 잰 **measured** 값이다. 사용자 승인 없음.
**Revision:** 1 (2026-11-10)
**Product Authority:** [기획서](product-definition/ai-coach/MASTER_PLANNING_SPEC.md) JOEFLOW rev 20 APPROVED(Manifest `47304076…`, state.json `approval`). 화면·행동·상태·문구는 기획서가 정하고, 이 문서는 그것이 어떻게 보이는지만 정한다.
**측정 기준:** `src/style.css` git blob `2368f017`(2026-11-10 세로 쌓기 간격 S1 적용 후). 토큰 표의 첫 측정은 적용 전 blob `fe3d5ef3`이고, 적용 후 Rule Coverage 렌더 행을 다시 돌렸다. 이 파일이 바뀌면 아래 Rule Coverage 행을 다시 돌린다.

## Visual Sources and Approval Scope

| 출처 | 범위 | 승인 |
| --- | --- | --- |
| 사용자 시각 원칙 1~5(아래 [이력](#사용자-시각-원칙-2026-10-23-사용자-지시)) | 게임처럼, 분명한 위계, 스크롤 없는 한 화면, 핵심 정보만, 카툰 캐주얼 표현 | 사용자 지시(2026-10-23) |
| 시안 v0.3 카툰 게임형 [work/design/coach-v2.html](work/design/coach-v2.html) | 방향(굵은 외곽선, 떨어지는 단단한 그림자, Jua+Pretendard, 하늘 배경, 사탕 돌) | 사용자 방향 승인(2026-10-23, 시안 기준). 구현 화면의 시각 수락은 없음(ROADMAP CO2) |
| 판 표식: 점선(rev 14), 상대 예상 수 반투명 돌(rev 20, DEC-049) | 판 위 표식 모양 | 사용자 지시 |
| 출하 `src/style.css` | 아래 토큰 값 전부 | **measured** — 코드에서 읽은 값은 승인이 아니다 |

v1은 새 시각 결정이 아니라 출하된 값의 정리다. 값 이름(토큰 이름)과 역할 묶음은 이번에 붙인 **proposed** 이름이며 CSS에는 아직 없다(CSS 변수로 있는 것은 그 이름을 그대로 쓴다). DRAFT → APPROVED 승격은 사용자만 한다.

## Token Roles

같은 역할은 모든 크기에서 같은 토큰을 쓴다. 값 둘이 `/`로 붙어 있으면 `데스크톱 / 휴대폰(폭 ≤700px)`. Status는 모두 measured(출하 코드 + 2026-11-10 렌더 측정)이며, "이름 없음"은 CSS 변수가 아니라 리터럴로 박힌 값이다.

### 색

| Role | Parts | Token / value | Status |
| --- | --- | --- | --- |
| 윤곽·글자 기본 | 모든 외곽선, 단단한 그림자, 본문·제목 글자, 포커스 링, 글자 외곽선(text-stroke) | `--ink` `#2a2047` | measured |
| 보조 글자 | 꺼진 차례 표시, 알약 보조 숫자, caption, 판 수 부족 | `--ink-soft` `#6b6290` | measured |
| 설명 문장 | `#card-text`, `#review-text` | `#4a4170`(이름 없음) | measured |
| 하늘 위 안내 글자 | `.title-meta`, `.coach-note`, `.alt-title`, 도움말 링크 | `#22507a`(이름 없음) | measured |
| 배경 | body 세로 그라데이션 + 흰 구름 원 | `--sky-1` `#5fd0ff` → `--sky-2` `#9be7ff` → `#bdf0ff`, 구름 `#ffffff44`·`#ffffff55` | measured |
| 표면 | 말풍선, 버튼, 알약, 대화상자 | `--paper` `#ffffff` | measured |
| 보조 표면 | 내 수 카드, 도움말 노트 | `--cream` `#fff7e3` | measured |
| 판 | 판 그라데이션 / 격자·별점 / 좌표 글자 | `--wood-1` `#ffd98a` → `--wood-2` `#f5bd5c` / `--grid` `#a46a2c`(불투명도 .55) / `#9a5d22`(이름 없음) | measured |
| 추천·진행 | 추천 표식, `두기` 버튼(go), 스위치 켬, 로딩 막대 | `--lime` `#6ee05a`, 어두운 쪽 `--lime-dark` `#2f9c3a` | measured |
| 주 행동·선택 | 주 버튼, 현재 차례, 선택한 고르기 버튼, 착수 예정 고리, 필승 | `--sun` `#ffd23f`, 어두운 쪽 `--sun-dark` `#e09a12` | measured |
| 상대·주의 | 마지막 수 점, 상대 점선, 수 세기 글자, 금수 ✕ | `--pink` `#ff6f91` | measured |
| 상대·검토 표면 | 검토·복기 라벨, 상대 알약, 금수 알림, 패배 배너 | `--pink-soft` `#ffe1ea` | measured |
| 보조 행동 | 되돌리기, 안내 단계 라벨 | `--sky-btn` `#4cc3ff` | measured |
| 히트맵 단계 | 후보 표식 높음·중간·비슷·낮음(반투명) | `--lime`·`--mid` `#b8ec7a`·`--even` `#ffe07a`·`--low` `#ffb199` + 알파 리터럴 | measured |
| 비활성 | 비활성 주 버튼·되돌리기 표면 / 외곽선·그림자 | `#e9e5f5` / `#b9b2d6`(이름 없음) | measured |
| 오류 글자 | 제한 안내 / 엔진 실패 | `#b23a3a` / `#b0213f`(이름 없음, 거의 같은 두 값) | measured |
| 상대 강조 글자 | 상대 예상 번호, 안내 강조 | `#b8325a`(이름 없음) | measured |
| 돌 | 흑: `#8a84b5`→`#3a2f63`→`#1c1533` 방사 그라데이션 / 백: `#ffffff`→`#f3eedf`→`#d9d1bd` | 이름 없음. 상단 칩 백돌은 `#e9e4d6`로 판 돌과 다름 | measured |
| 덮개(scrim) | 새 게임 확인 / 도움말 뒤 | `#2a204799` / `#2a2047a6`(거의 같은 두 값) | measured |
| 정의만 됨 | 사용처 없음 | `--danger` `#ff6b6b` | measured(사용 0) |

### 글꼴과 글자 크기

| Role | Parts | Token / value | Status |
| --- | --- | --- | --- |
| 표시 글꼴 | 제목, 좌표·비율 숫자, 모든 버튼·라벨·알약(`.fun` 포함) | `'Jua'` 400, `@fontsource/jua` korean+latin 자체 호스팅 | measured |
| 문장 글꼴 | 설명·안내·고지 문장 | `'Pretendard Variable'`(동적 부분 집합, 자체 호스팅) → `system-ui`, 굵기 550~800 | measured |
| 숫자 | 전체 | `font-variant-numeric: tabular-nums`, 줄 높이 1.5 | measured |
| 외곽선 글자 | 로고, 브랜드, 비율 숫자, 결과 배너 | 흰·색 글자 + `-webkit-text-stroke` `--ink` 5~10px, `paint-order: stroke fill` | measured |
| 크기: 화면 상징 | 로고 / 결과 배너 | `clamp(44px, min(12vw, 9dvh), 96px)` / `clamp(40px, 14cqw, 110px)` | measured |
| 크기: 핵심 숫자 | 추천 좌표 / 비율 | 64 / 40px, 56 / 40px(단위 30 / 22px); 높이가 좁으면 34px | measured |
| 크기: 주 버튼 | `.primary` | 30 / 25px(비활성 24 / 19px) | measured |
| 크기: 카드 제목 | `#card-title`, 대화상자 제목 | 22 / 18px, 26px | measured |
| 크기: 컨트롤 | 알약·갈래 / 고르기 / 차례·스위치·작은 버튼 / 라벨 | 19 / 17·16px, 18px, 17 / 15px, 15 / 13px | measured |
| 크기: 문장 | 설명 / 내 수 설명 / 보조(hero-sub) / caption·고지 | 15 / 13px, 14 / 12px, 13 / 12px, 12 / 11px | measured |
| 최소 | 판 밖 글자 / 판 좌표·번호 | 11px(렌더 최소) / `clamp(8px, …, 14px)` | measured |

### 간격

| Role | Parts | Token / value | Status |
| --- | --- | --- | --- |
| 간격 단계 | flex/grid `gap` | 4 · 6 · 8 · 10 · 12 · 14 · 16px(8px가 17곳으로 최다) | measured |
| 위 막대 | `#app` 첫 줄 높이 / 좌우 안쪽 | 64 / 58px, 24 / 12px | measured |
| 무대 안쪽 여백 | `.stage` padding | 데스크톱 옆 배치 `10px clamp(20px,3vw,40px) 24px`, 세로 배치 `6px 16px 14px`, 휴대폰 `4px 12px 12px` | measured |
| 판·옆 칸 | 옆 배치 열 간격 / 옆 칸 폭 | `clamp(24px,3vw,40px)` / `clamp(300px,28vw,400px)` | measured |
| 세로 쌓기 간격 | 메인 화면 세로 줄의 카드·후보 줄·복기 칸(말풍선 칸 `.hud`)과 버튼 줄·알림·안내 줄(버튼 칸 `.cta-area`), 시작 화면 카드→버튼 | `--stack` 12px, 폭 ≤700px 10px, 높이 ≤700px 8px. **보이는** 간격(위 요소 그림자 끝 → 아래 요소 위끝). 상자 간격 = `--stack` + 위 요소 `--overhang` | proposed — 2026-11-10 사용자 지시("간격 규칙 정하고 코드 맞추고")로 값은 담당자가 정해 구현, 사용자 확인 대기 |
| 그림자 깊이(간격 보정용) | `--overhang`: 말풍선 `--drop-bubble`, 내 수 카드 `--drop-card`, 버튼 줄 `--drop-cta`, 복기 칸 5px, 첫 안내 7px, 제한 안내 3px, 후보 줄 4px | 각 요소 `box-shadow`와 같은 값 | proposed(구현됨) |
| 말풍선 안쪽 | `.bubble` padding | `16px 22px 18px` / `10px 14px 12px` | measured |
| 버튼 줄 | `.turn-actions` 간격 / 되돌리기 칸 | 12 / 10px, 72 / 64px(예비 착수 때는 `auto`로 38px) | measured |

### 외곽선과 모서리

| Role | Parts | Token / value | Status |
| --- | --- | --- | --- |
| 외곽선 XL | 판 | 5 / 4px | measured |
| 외곽선 L | 말풍선, 주 버튼, 되돌리기, 대화상자, 새 게임 확인, 첫 안내 | 4px(휴대폰 말풍선·첫 안내 3px) | measured |
| 외곽선 M | 아이콘 버튼, 알약, 갈래, 고르기, 작은 버튼, 스위치, 내 수 카드, 복기 칸, 라벨, 대결줄 | 3px | measured |
| 외곽선 S | 상단 칩 돌, 작은 표식, 판 돌 | 2.5px(휴대폰 판 돌 1.5px) | measured |
| 모서리 | 모든 표면·버튼 | 판·말풍선 26 / 18·20px, 대화상자 24px, 주 버튼·되돌리기·첫 안내 22 / 18px, 내 수 카드 20 / 16px, 복기 칸·취소 18px, 알약·갈래·고르기 16px(휴대폰 알약 14px), 아이콘·작은 버튼 14px, 라벨 12px, 대결줄·스위치 999px, 돌·표식 50% | measured |

### 그림자(입체)

모든 입체 부품은 **번짐 없는 아래쪽 단단한 그림자** `0 Ypx 0 var(--ink)`를 쓴다(비활성은 `#b9b2d6`). 판만 추가로 부드러운 그림자 `0 22px 30px #1a3d5c40`를 겹친다. 누르면 `translateY(3~5px)`로 내려가고 그림자가 1~2px로 준다.

| Role | Parts | Token / value(Y) | Status |
| --- | --- | --- | --- |
| 그림자 XL | 판 | 10 / 7px | measured |
| 그림자 L | 말풍선(`--drop-bubble`), 대화상자, 새 게임 확인 | 8px(휴대폰 말풍선 6px) | measured |
| 그림자 L− | 주 버튼·되돌리기(`--drop-cta`, 모든 상태), 첫 안내 | 7 / 6px(첫 안내 7px). 2026-11-10 전에는 휴대폰 `두기`·비활성 상태만 7px였던 불일치를 `--drop-cta`로 6px에 맞춤 | measured(적용 후 렌더) |
| 그림자 M | 내 수 카드(`--drop-card`), 복기 칸, 취소 | 5px(휴대폰 내 수 카드 4px) | measured |
| 그림자 S | 아이콘 버튼, 알약, 갈래, 고르기, 작은 버튼, 대결줄 | 4px(휴대폰 아이콘 버튼·대결줄 3px) | measured |
| 그림자 XS | 라벨, 스위치, 표식·돌 | 3px(휴대폰 돌·표식 2px) | measured |
| 안쪽 빛 | 주 버튼 아래 띠 / 현재 차례 | `inset 0 -6px 0 #e0a10f66`(go `#2f9c3a66`) / `inset 0 -3px 0 #0000001a` | measured |

### 움직임

장식 애니메이션 9종(`drop`, `twinkle`, `spin`, `spin-pulse`, `hop`, `pop`, `banner-in`, `bob`, 스위치 전환 .25s). 무한 반복 7곳(로고 별, 추천 고리 회전, 착수 예정 고리, 계산 중 점 등). `prefers-reduced-motion` 처리는 **없다**(measured, 코드).

## 화면 규칙

| ID | 규칙 | 출처 |
| --- | --- | --- |
| L1 | 1440×900·390×844(및 아래 측정 크기)에서 핵심 정보와 조작이 세로·가로 스크롤 없이 한 화면에 보인다. 높이가 모자라면 덜 중요한 것부터 접는다(카드 설명 → 내 수 카드 → 후보 라벨 순, `@container hud`) | 사용자 원칙 3 |
| L2 | 폭 ≥900px이고 가로:세로 ≥5:4면 판(왼쪽, 높이 기준 최대) + 옆 칸(말풍선 → 버튼). 그 밖은 위 막대 → 판 → 말풍선 → 버튼 세로 순서 | 출하 측정(시안 v0.3) |
| H1 | 시선 순서: ① 판과 1순위 표식 ② 말풍선의 좌표·비율(가장 큰 글자) ③ 주 버튼(노랑) ④ 후보·상대 알약 ⑤ 고지문·스위치. 설명 문장은 한 줄 이유 | 시안 v0.3 위계 |
| E1 | 입체 부품은 `--ink` 외곽선 + 번짐 없는 아래 그림자를 쓰고, 두께는 위 그림자·외곽선 표의 역할 단계를 따른다 | 출하 측정(사용자 원칙 5) |
| S1 | 메인 화면 세로 줄에서 이웃한 두 요소의 **보이는** 간격(위 요소의 그림자 끝 → 아래 요소 위끝)은 같은 칸 안(말풍선 칸, 버튼 칸)과 시작 화면 카드→버튼에서 `--stack`(12 / 폭 ≤700px 10 / 높이 ≤700px 8px, ±1px). 대국 화면의 말풍선 칸→버튼 칸은 남는 높이를 받는 자리라 `--stack` 이상. 제목→카드는 제목 묶음이라 이 규칙 밖 | 사용자 지시(2026-11-10), 값은 proposed |
| S2 | 휴대폰 좌우 여백은 12px(말풍선·버튼 줄의 보이는 외곽선까지) | 출하 측정 |
| T1 | 표시 글꼴 Jua, 문장 글꼴 Pretendard. 둘 다 자체 호스팅, 실행 중 외부 글꼴 요청 0 | 출하 측정(시안 v0.3) |
| T2 | 판 밖 글자 ≥11px, 판 안 좌표·번호 ≥8px | 출하 측정 |
| C1 | 색은 위 토큰 표의 역할로만 쓴다. 새 색이 필요하면 표에 역할을 먼저 더한다 | proposed(현재 이름 없는 리터럴 57종) |
| C2 | 글자 대비 WCAG AA(본문 4.5:1, 큰 글자 3:1). 색만으로 구별하지 않고 숫자·글자를 함께 쓴다 | proposed(접근성 기준, 기획서에 없음) |
| L3 | 누르는 컨트롤은 44×44px 이상(판 교차점 제외) | proposed(v0.1 초기 목표, 기획서에 없음) |
| M1 | 동작 감소 설정에서 무한 반복 장식 애니메이션을 멈춘다 | proposed(v0.1 기록, 기획서에 없음) |
| B1 | 판 위 표식은 반투명 점선(추천·후보·착수 예정·금수 ✕·내 수순). 예외: 예비 착수 뒤 상대 예상 수순만 상대 색 반투명 돌(불투명도 .5, 실선, 번호) | 사용자 지시(rev 14, rev 20) |

proposed 규칙(C1·C2·L3·M1)은 현재 출하 화면이 지키지 않는 기준이다. 채택·수정·제외는 사용자가 정하며, 그전에는 측정 결과만 기록하고 코드를 바꾸지 않는다.

## Rule Coverage

측정 대상(2026-11-10, S1 적용 전과 후 두 번 실행. T1·T2·C1·C2·L3·M1의 spot check는 적용 전 blob에서 한 것이고 검사 방법은 그대로다): test 빌드(`vite build --mode test`)를 `vite preview`로 5199에서 띄우고, 엔진 파일(`public/engine/rapfi*`)이 없어 `__engine`에 고정 응답 가짜 Worker를 넣어 화면 상태를 만들었다(엔진 결과·속도는 측정 대상 아님). 크기 4개(1440×900, 1366×768 = 옆 배치 / 390×844, 360×640 = 세로 배치) × 상태 7개(intro, setup, tutorial, candidates, route, help, finished) = 28 대상, 밝은 화면만(어두운 모드 없음). 스크립트: [ds-v1-audit.mjs](work/design/ds-v1-audit.mjs)(렌더), [ds-v1-spot.mjs](work/design/ds-v1-spot.mjs)(캡처 픽셀), [ds-v1-inventory.mjs](work/design/ds-v1-inventory.mjs)(코드). 캡처 `work/design/ds-v1/`.

| Rule | Check | Spot check | Layouts | Sizes | States | Unmeasured |
| --- | --- | --- | --- | --- | --- | --- |
| L1 한 화면 | audit `scroll`(문서 scrollWidth/Height > 창) | 360x640 candidates 캡처: check 스크롤 없음 / observed 맨 아래 스위치 하단까지 640px 안에 보임; S1 적용 후 375x667 undone 캡처: check 스크롤 없음 / observed 안내 줄 스위치가 667px 안에 보임 | 옆·세로 | 4 | 7 | 복기 진행 중·자세히 보기·금수 알림·엔진 실패 상태, 1920·820·768·489·430·375 크기(기존 [capture-matrix](work/design/capture-matrix.mjs) 범위) |
| E1 입체 그림자·외곽선 | audit `raisedBad`(그림자 첫 층 x0·blur0·색 ink, 외곽선 색 ink, 비활성은 `#b9b2d6`) + 역할별 Y값 | 1440x900 candidates 말풍선 아래: check 외곽선 4+그림자 8 / observed 남색 12px 줄; 360x640: check 3+6 / observed 9px(S1 적용 후 캡처도 9px) | 옆·세로 | 4 | 7 | 판 위 돌·표식 그림자, 눌림 상태, 결과 배너 text-shadow |
| S1 세로 쌓기 간격 | [stack-gap-check.mjs](work/design/stack-gap-check.mjs)(`npm run check:spacing`, 보이는 가장자리 = 그리는 상자 + 아래 그림자, 위반 시 종료 코드 1, 곁 검사로 페이지 스크롤) | 1440x900 route 버튼 줄→안내 줄: check 12 / observed 12px(적용 전 check 1 / observed 1); 360x640 candidates 말풍선→후보: check 8 / observed 8px(적용 전 2 / 2). 캡처 픽셀 [png-column.mjs](work/design/png-column.mjs) | 옆·세로 | 7(1440×900, 1366×768, 1280×720, 1024×768, 390×844, 375×667, 360×640) | 8(intro, setup, tutorial, candidates, route, undone, finished, replay) | 금수 알림·엔진 알림·제한 안내가 보이는 상태, 말풍선 안 요소 간격, 글자 줄 상자와 실제 글자 잉크의 차이, 제목→카드, 820×1180 등 세로형 태블릿 |
| S2 휴대폰 좌우 여백 | audit `sideEdges` | 390x844·360x640 candidates 말풍선 가운데 줄: check 12/12 / observed 12/12px | 세로 | 390×844, 360×640 | 7 | 판(높이 제한으로 가운데 정렬, 360×640에서 45px) |
| T1 글꼴 | audit `document.fonts.check`(Jua·Pretendard, '가') + 외부 호스트 요청 수 | 1440x900 route 캡처: check 둘 다 loaded / observed `J10에 두기`·좌표가 Jua 둥근 글자로 보임 | 옆·세로 | 4 | 7 | dev 서버(`npx vite`) 화면: 이 작업 폴더에서는 글꼴 403([ISSUES ENV-05](ISSUES.md#env-05)) |
| T2 최소 글자 | audit `minFont`(판 밖 / 판 안 최소 font-size) | not spot-checked | 옆·세로 | 4 | 7 | 글리프 실제 높이, 판 수 부족 표식 |
| C1 색 토큰 | inventory `HEX_LITERALS_OUTSIDE_ROOT`, `VAR_USE` | not spot-checked | 코드 | — | — | 렌더 색(그라데이션 합성) |
| C2 글자 대비 | audit `contrast`(불투명 배경까지 합성, text-stroke 글자·비활성 제외) | 1440x900·390x844·360x640 candidates 수 세기: check 2.65 / observed 픽셀 `#ff6f91` on `#ffffff` 2.65 | 옆·세로 | 4 | 7 | 그라데이션 배경 위 글자 102건(로고·브랜드·tagline·title-meta·coach-note·live-status·주 버튼·choose-hint), 판 안 글자 |
| L3 누르는 크기 | audit `targetsUnder44`(판 교차점·문장 안 링크 제외) | 1440x900·390x844·360x640 route 되돌리기: check 폭 38 / observed 외곽선 폭 38px | 옆·세로 | 4 | 7 | 판 교차점(v0.1부터 44px 주장 안 함) |
| M1 동작 감소 | 코드 grep `prefers-reduced-motion` | not spot-checked | 코드 | — | — | 실제 동작 감소 설정 렌더 |
| H1 위계 | 없음 — 사람의 화면 판단 | not spot-checked | — | — | — | 전부(미측정). 사용자 시각 수락으로만 닫힌다 |
| L2 배치 전환 | 없음(이번 측정은 결과 배치만 캡처) | not spot-checked | — | — | — | 900px·5:4 경계 크기 |
| B1 판 표식 | 없음 — E2E AC-020·021은 표식 존재와 반투명 돌을 검사하나 이번 턴에 돌리지 않음 | not spot-checked | — | — | — | 표식 모양 전부 |

## Report Form

Any session that changes a file listed in Rule Coverage, with or without JOEDESIGN
loaded, reports design-check results in one list, one line per check that ran:
`check | result | sizes x states, mode | rendered or code | spot check` (the row's
Spot check cell, or "not spot-checked"). Each fix takes its own line; its result
is `fixed` only when its spot check cell holds a direct observation of the fixed
thing on a target that showed it, otherwise `changed`. A `changed` fix is an open
issue: it goes under 남은 문제 (remaining work) in the report, ISSUES and ROADMAP,
never under 해결 (resolved). Outside the list, a pass or count carries its
parenthesis (sizes x states, rendered or code, spot check outcome). A turn with no
design check says `design checks: none ran`. A result that is not spot-checked is
not resolved, verified or done. A change that moves, overlaps, hides or merges an
existing element lists, under `## Display before/after`, two lines per element:
`before: element | content shown | route` and `after: ...` (`hidden` when gone).
A pair that differs stays `product decision pending` until the product definition
changes; a matching pair is a design decision.

## Open Decisions / Evidence Boundary

2026-11-10 측정 결과(값은 위 표, 판정 줄은 [TASK](TASK.md#design-system-v1)):

- 출하 화면이 proposed 기준과 어긋나는 곳: 수 세기 글자 `--pink` on 흰색 대비 2.65:1, 안내 단계 라벨 흰 글자 on `--sky-btn` 1.99:1; 44px 미만 컨트롤 16종(예비 착수 때 되돌리기 38px 폭, 휴대폰 아이콘 버튼 42px, 알약 36px, 360×640 고르기 버튼 40px 등); 동작 감소 처리 없음. 채택 여부는 사용자 결정 대기.
- 같은 역할 안 불일치(measured): 휴대폰 주 버튼 그림자 6px vs `두기`·비활성 7px; 거의 같은 오류 글자 두 값, 덮개 두 값; 칩 백돌과 판 백돌 색 차이; `--danger` 미사용; 이름 없는 리터럴 색 57종.
- 2026-11-10 S1 적용: 보이는 간격이 1~22px로 제각각이던 것을 `--stack`으로 맞췄다([TASK](TASK.md#stack-spacing)). 값(12/10/8)은 사용자 확인 대기.
- 휴대폰 높이 ≤667px 복기 상태에서 말풍선이 말풍선 칸에 잘린다(S1 검사 2쌍 겹침, 적용 전부터 있던 문제, [ISSUES LAYOUT-06](ISSUES.md#layout-06)). 해결하려면 복기 중 판 크기를 줄이거나 복기 칸·말풍선 내용을 접어야 해 사용자 결정 대기.
- 측정하지 못한 것: 실제 엔진 화면(엔진 파일 없음 — 받으려면 외부 약 42MB 내려받기 승인 필요), 그라데이션 배경 위 글자 대비, 위계(H1)·배치 전환(L2)·판 표식(B1), 독립 검토자의 규칙 범위 검토.
- 기술 측정, 화면 품질 판단, 사용자 수락은 서로 다르다. 이 문서의 어떤 측정도 사용자 시각 수락이 아니다.

## Amendment Rule

Only explicit user approval promotes DRAFT to APPROVED. Preserve APPROVED Rev N
while proposing a separately labeled DRAFT Rev N+1 in this same file. Replace the
active approved rule set only after proof and explicit approval. Local refinement
within approved intent does not automatically create a material revision.

## 이력 — 이전 시각 결정(보존)

아래는 v1 이전 기록이다. v0.1의 색·글꼴·간격 표는 v0.3 구현으로 대체됐다(현재 값은 위 Token Roles). v0.1 "상호작용 표현"과 사용자 시각 원칙·표식 예외는 현재 화면에도 유효한 기록으로 남긴다.

### 시각 방향 — 제안 v0.1

작성: 2026-10-22. 권한: 사용자가 화면 구성 선택을 맡겼으나 **이 시각안에 대한 사용자 승인 없음**. 상태: v0.1 방향을 구현에 사용했고 두 지정 크기의 실제 렌더를 개발자가 확인했다. 사용자 시각 승인과는 다르다. 실행 근거는 [TASK](TASK.md#implementation), 제품 흐름은 [ROADMAP.md](ROADMAP.md#선택한-학습-흐름)가 소유한다.

#### 방향

초보자가 판과 한 문장 해설을 번갈아 보기 쉬운 차분한 학습용 바둑판. 큰 홍보 영역·장식 이미지·랭킹·승률 게이지는 두지 않는다. 페이지 이름은 “함께 배우는 AI 오목”, 보조 문구는 “한 수씩, 이유를 보며 배워요.”

| 요소 | 제안 |
| --- | --- |
| 바탕/표면 | 따뜻한 밝은 회색 `#F6F4EE`, 설명 표면 `#FFFFFF` |
| 판/선 | 옅은 목재 단색 `#E7C996`, 격자 `#6B5237`; 사진 질감 없음 |
| 본문/보조 글자 | `#1D2925` / `#4B5C55`, 대비는 실제 렌더링에서 확인 |
| 행동/추천 | 짙은 녹색 `#1F5D49`; 선택은 사각 테두리, 추천은 원형 고리와 “추천” 표식 |
| 예상/위험 | 예상 백 수는 점선 고리+“예상” 글자, 주의는 `#8B3F20`+설명. 색만으로 구별하지 않음 |
| 돌 | 흑 `#202622`, 백 `#FAFAF5`와 어두운 외곽선. 실제 돌은 불투명, 가상 표시는 빈 고리 |
| 글꼴/규모 | 로컬 시스템 한글 sans-serif. 본문 16px, 보조 최소 14px, 제목 24–28px 제안. 원격 폰트 없음 |
| 간격/모서리 | 8px 단위 중심, 카드 16–24px 여백, 12px 모서리. 판을 설명 카드보다 크게 |

색·수치·배치는 변경 가능한 초기 선택이다. 이 문서가 검증된 접근성 인증이나 승인된 디자인 시스템은 아니다.

#### 배치

- **1440×900:** 짧은 제목/규칙·새 게임 행 아래, 왼쪽 판 520px, 간격 50px, 오른쪽 설명 350px. 실제 화면 점검 후 기본 판과 주요 행동을 같은 화면에서 조작하기 쉽도록 초기 620px 제안보다 줄였다. 긴 해설은 세로 스크롤할 수 있다.
- **390×844:** 좌우 16px 여백, 제목 → 차례/짧은 안내 → 폭 358px 이내 판 → 선택 좌표/확정 버튼 → 추천·해설 순서. 긴 해설은 자연스러운 세로 스크롤. 판 폭을 줄여 모든 글을 억지로 한 화면에 넣지 않는다. 고정 하단 바가 판/버튼을 덮지 않도록 한다.
- 판은 정사각형. 외곽 교차점도 누를 수 있도록 내부 가장자리 여백과 좌표 영역을 둔다. 열 A–O(중간 문자 생략 없음), 행 1–15, 위에서 아래로 증가. 좌상단 A1, 중심 H8. 화면·검사·해설 모두 이 기준을 공유한다.
- “현재 추천”과 “직전 수 해설”을 제목으로 분리한다. 예상 수가 있는 검토 중에는 그 판을 그대로 유지한다. 다음 판으로 넘어가면 이전 예상 고리는 지우고 직전 수 글만 출처 수와 함께 남긴다.

#### 상호작용 표현

- 종료 후 복기는 판 위의 `대국 복기`로 진입하고 같은 영역의 `이전 수 / 다음 수 / 종료 판으로`를 사용한다. `복기 중`과 표시 중인 수·색·좌표, 실제 종료 결과·총 수를 함께 표시한다. 설명 카드는 선택한 수에 해당하는 당시 해설과 기준 수를 보여주고, 기존 직전 내 수 카드·추천/예상 고리는 숨긴다. 작은 점과 승리선은 표시 중인 판에만 적용한다. 복기 중 되돌리기는 비활성화하고 종료 판으로 복귀하면 다시 사용할 수 있다. 새 게임 버튼은 계속 사용 가능하다. 시각 승인 여부와 실제 검사 근거는 [복기 기록](TASK.md#replay)을 따른다.

- 후속 승인 범위인 되돌리기는 착수 버튼 옆의 `↶ 되돌리기` 보조 버튼으로 제공한다. 두 버튼을 한 줄에 배치하고 데스크톱은 설명 오른쪽, 휴대폰은 설명 아래에 둔다. 키보드 순서는 착수 → 되돌리기다. 되돌릴 차례가 없거나 복원 분석 중이면 비활성화한다. 취소된 돌 수에 맞는 짧은 안내를 행동 영역과 live 알림에 표시한다. 이전 해설은 해당 수의 기준 표시와 함께 복원한다. 이 구성은 구현 선택이며 사용자 시각 승인으로 간주하지 않는다.

- 선택한 점은 돌을 놓기 전 좌표와 테두리로 보여준다. `H8에 두기` 버튼은 선택이 없으면 이유와 함께 비활성화한다. 일반 행동 버튼은 높이 44px 이상을 초기 목표로 둔다. 촘촘한 판의 교차점까지 모두 44px라고 주장하지 않는다.
- 컴퓨터에서 선택 가능한 교차점에 포인터를 올리면 배경이 강조된다. 별도 hover 좌표 미리보기는 없으며, 교차점을 선택한 뒤 행동 영역에 좌표가 표시된다. 터치는 hover에 의존하지 않는다. 한 번 누르면 선택, 다른 곳을 누르면 이동, 확정 버튼으로만 착수한다.
- 판은 키보드 한 번의 Tab 진입과 방향키 이동을 제공한다. 현재 점 1곳만 tab stop. Enter/Space는 선택, Tab으로 확정 버튼 이동. 점유된 점도 상태를 읽을 수 있으나 착수할 수 없다. 포커스는 보이고 화면 갱신 중 유지한다.
- 각 점은 “H8, 빈칸 / 흑 / 백”처럼 이름을 가진다. 차례·분석 완료·종료는 짧은 live 알림으로 전달하되 225칸을 매번 읽지 않는다.
- 마지막 착수에는 작은 중심 표식, 승리선에는 외곽 강조를 더한다. 추천·선택·예상·실제 돌이 겹치면 라벨과 모양을 유지한다.
- 분석 중 현재 카드 안에 “이 판을 살펴보는 중…” 표시. 실패 시 같은 카드에 재시도와 제한을 표시한다. 페이지 전체를 막는 로딩 화면이나 끝없는 spinner를 만들지 않는다.
- 동작 감소 설정에서 장식 전환을 제거한다. 애니메이션·소리·테마 전환은 초기 필수 범위가 아니다.

검증 기준과 현재 상태는 [ROADMAP의 U2](ROADMAP.md#p2)와 [V2](ROADMAP.md#p3)를 따른다. 구현 담당자의 시각 점검과 실제 사용자의 시각 승인/수락을 각각 기록한다.

### 계산형 도우미 — 제안 v0.2 (2026-10-23)

**사용자 판정 2026-10-23:** 와이어프레임(정보 배치·흐름)으로는 인정, **시각 디자인으로는 탈락(REJECTED) — 이 시각을 기반으로 발전시키지 않는다.** 아래 표에서 유지되는 것은 배치·정보 구성(판 위 상위 3곳 %, 판 옆 비교 패널, 판 아래 상태 줄, 휴대폰 칩 줄, 자세히 보기의 히트맵·갈래 목록, 판 수 부족·필승 표기 규칙)뿐이며, 색·질감·표면·글자 스타일은 새 시각 방향에서 다시 정한다.

제품 의미 원본: [기획서](product-definition/ai-coach/MASTER_PLANNING_SPEC.md)(JOEFLOW 승인 rev 12). 기준 레퍼런스: KaTrain(주, 판 위 후보별 결과 표식), Lichess(보조, 판 위 절제·수순은 판 옆) — 사용자 선택 2026-10-23, 근거 [Library/design-references.md](Library/design-references.md). 대표 화면 시안: [work/design/coach-proof.html](work/design/coach-proof.html), 캡처 `work/design/shots/`.

v0.1의 "승률 게이지를 두지 않는다"는 승인된 DEC-001(연습 대국 비율 표시)로 대체된다. 비율은 항상 판 수·"실제 승률 아님"과 함께 보이며, 게이지처럼 단독으로 쓰지 않는다.

| 요소 | 제안 |
| --- | --- |
| 판 위 상위 3곳 | 교차점 크기 원형 표식에 흑 승 %만(데스크톱 약 13px, 휴대폰 10px). 판 수는 판 위에 쓰지 않고 패널/요약 줄에 둔다(28px 표식 안의 판 수는 7px로 읽을 수 없어 KaTrain과 다르게 결정). 1순위는 기존 추천 녹색의 이중 고리 |
| 비율 색 단계 | ≥60 `#1F5D49`(흰 글자) · 52–59 `#5F8F72`(흰 글자) · 45–51 `#C8B382`(짙은 글자) · ≤44 `#E9C9B6`(`#6B2E14` 글자). 낮은 값은 연한 색으로 두어 시선이 좋은 수로 가게 한다. 숫자를 항상 함께 써서 색만으로 구별하지 않음 |
| 판 수 부족 | 점선 외곽 연한 표식 + "—", 목록에서는 "판 수 부족 · N판" |
| 상대 예상 수 | 기존 점선 고리 그대로(글자 없음), 범례와 패널 문장으로 설명 |
| 필승/필패 | 금색 `#B8860B` 외곽 고리 + "필승" 글자, 패널에 "2수 안에서 찾은 결과" 문장 |
| 자세히 보기 히트맵 | 나머지 후보는 작은 표식에 숫자만(최소 9px). 갈래 미리보기는 번호 붙은 반투명 돌 |
| 상태·범례 줄 | 판 아래 한 줄: 계산 상태(계산 중… / N곳 · 1.5초 N판) + 범례. 데스크톱에서 행동 영역이 900px 안에 들어오도록 기존 범례와 합침 |
| 옆 패널(데스크톱) | "연습 대국 비교" 카드를 기존 추천 카드 위에. 순위·좌표·흑/미정/백 막대·%·판 수·±. 아래에 예상 수 한 줄, 설명 문구, "자세히 보기" 토글. 자세히 보기에서 갈래 3개를 Lichess 수순 목록처럼 |
| 휴대폰 | 판 바로 아래 상위 3곳 칩 줄(순위·좌표·%·판 수) + "연습용 AI끼리 둔 결과 · 실제 승률 아님". 전체 카드와 갈래 목록은 행동 영역 아래 패널 |

### 사용자 시각 원칙 (2026-10-23, 사용자 지시)

v0.2 탈락 이유와 앞으로의 기준. 이 원칙은 사용자 지시이며 새 시각 방향의 판정 기준이다.

1. **게임처럼 보여야 한다.** 카드·제목·설명 문단을 쌓은 발표자료(PPT) 같은 화면이 아니다.
2. **시각적 위계가 분명해야 한다.** 무엇을 먼저 보고 다음에 무엇을 보는지가 크기·밝기·색으로 정해져야 한다.
3. **스크롤 없이 한 화면.** 1440×900과 390×844 모두 핵심 정보와 조작이 스크롤 없이 보인다.
4. **핵심 정보만.** 정보 과다 금지. 부가 설명은 필요할 때만 열린다.
5. **카툰 캐주얼 게임 그래픽.** 사용자 지시(2026-10-23): 협동 타워 디펜스류, '운빨존많겜' 같은 느낌. 굵은 외곽선, 통통하고 둥근 글자, 쨍한 색, 눌리는 입체 버튼. 해당 게임의 로고·캐릭터·이름은 쓰지 않고 표현 방식만 참고한다.

### 계산형 도우미 — 시안 v0.3 카툰 게임형 (2026-10-23, 사용자 시각 승인 없음)

시안: [work/design/coach-v2.html](work/design/coach-v2.html) (`?state=loading|default|sparse|detail|proven`), 캡처 `work/design/shots/coach-v2-*`. 위 사용자 시각 원칙 1~5를 판정 기준으로 v0.2 배치(와이어프레임)만 이어받았다.

- 한 화면: 데스크톱은 판(좌, 화면 높이 기준 최대) + 오른쪽 추천 말풍선·버튼, 휴대폰은 대결줄 → 판 → 말풍선 → 버튼. 10개 캡처 모두 세로·가로 스크롤 없음(스크립트 측정).
- 위계: ① 판과 1순위 표식(연두 구슬 + 별, 통통 튐) ② 말풍선의 좌표·%(가장 큰 글자) ③ 노란 선택 버튼 ④ 2·3순위와 백 예상 수 알약 ⑤ 하단 작은 고지문·자세히 토글. 설명 문장은 한 줄 이유만.
- 표현: 남색 `#2A2047` 굵은 외곽선과 아래로 떨어지는 입체 그림자, 하늘색 배경과 구름, 사탕 같은 돌, Jua(제목·숫자, @fontsource/jua 자체 호스팅) + Pretendard(문장, 자체 호스팅). 외부 글꼴 요청 없음.
- 색: 1순위 연두 `#6EE05A`, 필승 노랑 `#FFD23F`, 백 예상 분홍 `#FFE1EA`, 되돌리기 하늘 `#4CC3FF`. 히트맵은 연두/연연두/노랑/살구 + 숫자 병기.
- 남은 것: 실제 계산 연결, 선택 후 상태("F10에 두기"), 내 수 검토·AI 응수·종료·복기 화면을 같은 세계로 확장, 글꼴 용량(한글 전체 글꼴은 부분 집합 사용 필요) 확인.
- **2026-10-23 구현:** 사용자가 v0.3 방향 승인("이걸 기반으로 나머지 화면 확장과 실제 구현"). `src/style.css`·`src/main.ts`를 이 세계로 교체하고 시작·계산 중·추천·다른 자리 선택(작은 '추천 H8' + 초록 '두기' 버튼)·내 수 평가·AI 응수·자세히 보기·종료·복기·새 게임 확인·도움말을 같은 표현으로 확장. 구현 화면의 사용자 시각 수락은 아직 없음.

### 표식 예외: 상대 예상 수는 반투명 돌 (2026-10-24, 사용자 지시)

사용자 지시 "적의 수는 좀 다르게 표현해줘. 점선 말고 반투명 돌로."(JOEFLOW rev 20, DEC-049). 위 "사용자 시각 원칙"의 '판 위 표식은 모두 반투명 점선'에서 **예비 착수 뒤 상대 예상 수순만** 예외로 한다: 상대 돌 색의 반투명 돌(불투명도 0.5, 실선 테두리)에 번호. 내 수순·후보·금수 ✕·착수 예정은 그대로 점선. 실제 돌과 구별은 불투명도와 번호로 한다. 승률 가이드 스위치(DEC-050)는 대국 화면 아래쪽 고지문 옆에 둔다. 사용자 시각 확인 전.
