# Project Design — 함께 배우는 AI 오목

**Reporting:** follow the `## Report Form` section below exactly (보고는 `## Report Form` 절을 그대로 따른다).

**Status:** DRAFT — 디자인 시스템 v1 (2026-11-10). 값은 출하된 `src/style.css`(마지막 변경 커밋 `8ab7db7`, rev 20)에서 읽은 **measured** 값이다. 사용자가 이 v1 표를 승인하지 않았으므로 approved 값은 없다.
**Revision:** 1
**Product Authority:** JOEFLOW `product-definition/ai-coach/MASTER_PLANNING_SPEC.md` rev 20 (`state.json` definition_status CLOSED, 사용자 승인 Manifest `47304076…`, [ROADMAP P6](ROADMAP.md#p6)). 화면·동작·문구는 그쪽이 정하고, 이 문서는 보이는 방식만 정한다.

## Visual Sources and Approval Scope

| 원천 | 범위 | 상태 |
| --- | --- | --- |
| 사용자 시각 원칙 1~5 (2026-10-23, [아래 이력](#사용자-시각-원칙-2026-10-23-사용자-지시)) | 모든 화면의 판정 기준: 게임처럼, 위계, 스크롤 없는 한 화면, 핵심 정보만, 카툰 캐주얼 그래픽 | 사용자 지시 |
| 시안 v0.3 카툰 게임형 ([work/design/coach-v2.html](work/design/coach-v2.html)) | 방향(“이걸 기반으로 나머지 화면 확장과 실제 구현”) | 사용자 방향 승인(시안 기준) |
| 판 위 표식 점선, 상대 예상 수 반투명 돌 (rev 14, rev 20 DEC-049) | 판 표식 | 사용자 지시 |
| 출하 구현 `src/style.css` @ `8ab7db7` | 아래 토큰 값 전부 | measured — 구현 화면의 사용자 시각 수락 없음 |
| v0.1 제안 색(`#F6F4EE`, `#1F5D49` 등)·v0.2 시각 | — | v0.3으로 대체/탈락. 토큰 근거로 쓰지 않음 |

## 디자인 시스템 v1 — Token Roles

**토큰 파일(2026-11-10 사용자 지시 “토큰은 tokens.css로 분리”):** 이름 붙은 토큰 변수 값(색 `:root`, `--rec-ring`, `--stack`, `--drop`, `--board-drop`과 그 크기별 값)은 `src/tokens.css`에 있고 `src/style.css` 맨 위에서 `@import`한다. 판 크기 계산용 배치 변수(`--top`, `--cta`, `--hud-min`, `--side`, `--gap`, `--pad`, `--size`, `--rbar`)와 원시 색 값은 `src/style.css`에 남아 있다. 아래 Rule Coverage의 “변경 파일”에는 두 파일이 모두 들어간다.

같은 역할은 모든 크기에서 같은 토큰을 쓴다. “데스크톱/휴대폰” 값은 `@media (max-width: 700px)`에서 바뀌는 쌍이다. Status는 모두 **measured**(출하 코드에서 읽음). `미토큰`은 코드에 CSS 변수 없이 원시 값으로 박혀 있는 역할이며, 이름은 **proposed**다. 원시 값 목록은 `node work/design/token-inventory.mjs`로 다시 뽑는다.

### 색

| Role | Parts | Token / value | Status |
| --- | --- | --- | --- |
| 외곽선·본문 글자·입체 그림자 | 모든 테두리, 그림자, 본문 글자 (사용 126곳) | `--ink` `#2a2047` | measured |
| 보조 글자 | 라벨, 부제, 비활성 글자 | `--ink-soft` `#6b6290` | measured |
| 설명 문장 글자 | `#card-text`, `#review-text` | `#4a4170` (미토큰, proposed `--ink-body`) | measured |
| 표면 | 말풍선, 버튼, 대화상자, 대결줄 | `--paper` `#ffffff` | measured |
| 보조 표면 | 내 수 평가 카드, 도움말 메모 | `--cream` `#fff7e3` | measured |
| 하늘 바탕 | `body` 그라데이션 `--sky-1` `#5fd0ff` → `--sky-2` `#9be7ff` → `#bdf0ff` + 흰 구름 원 | `--sky-1`, `--sky-2` | measured |
| 하늘 바탕 위 글자 | `.title-meta`, `.coach-note`, `.alt-title` | `#22507a` (미토큰, proposed `--on-sky`) | measured |
| 판 | 나무 그라데이션, 격자·별점 | `--wood-1` `#ffd98a`, `--wood-2` `#f5bd5c`, `--grid` `#a46a2c` | measured |
| 판 격자선 진하기 | `.lines`(격자선, 별점·좌표 글자 제외) | `--grid-line-opacity` .4(이전 .55) — 캡처 픽셀 나무색 대비 약 1.75 → 1.5:1 | 사용자 지시 2026-11-10 “판 격자선 색 좀 연하게”, 값은 담당자 선택 |
| 흑돌 | 돌, 칩, 갈래 번호 | 방사 그라데이션 `#8a84b5`→`#3a2f63`→`#1c1533` (미토큰, proposed `--stone-b-*`) | measured |
| 백돌 | 돌, 칩 | `#ffffff`→`#f3eedf`→`#d9d1bd` | measured |
| 주 행동(노랑) | 주 버튼, 선택된 고르기, 차례 표시, 필승 | `--sun` `#ffd23f`, 진한 `--sun-dark` `#e09a12` | measured |
| 추천·좋음(연두) | 1순위·추천 표식, 라벨, 두기 버튼 | `--lime` `#6ee05a`, 진한 `--lime-dark` `#2f9c3a` | measured |
| 추천 고리 | 판 위 1순위 추천 표식 `.m1`의 점선 테두리(가이드 대체 `.hint` 포함) | `--rec-ring` `#17692a` — 판 나무색 대비 4.0~5.0:1. 이전 `--lime-dark` `#2f9c3a`는 2.1~2.6:1 | 사용자 지시(2026-11-10 “더 진한 초록으로”), 값은 담당자 선택 |
| 승률 가이드 스위치 켬(파랑) | `.toggle[aria-pressed=true]` 막대·버튼 바탕 | 라이트 `--switch-on` `#1f6fe0` · `--switch-on-bg` `#dcebff`(막대 대 바탕 3.94:1, 이전 연두 대 흰 바탕 약 1.6:1) / 다크 `#5aa2ff` · `#1f3566`(4.57:1) | 사용자 지시(2026-11-10 “눈에 띄게, 파란색 계열로”), 값은 담당자 선택 ([TASK](TASK.md#toggle-blue)) |
| 상대·주의(분홍) | 상대 예상 수, 금수 ✕, 마지막 수 점, 수 세기 글자 | `--pink` `#ff6f91`, 연한 `--pink-soft` `#ffe1ea` | measured |
| 보조 행동(하늘 버튼) | 되돌리기, 시작 라벨, 안내 단계 | `--sky-btn` `#4cc3ff` | measured |
| 비율 단계 | 히트맵 `--mid` `#b8ec7a`, `--even` `#ffe07a`, `--low` `#ffb199` (판 위는 알파 45~50%) | `--mid`, `--even`, `--low` | measured |
| 비활성 | 비활성 주 버튼·되돌리기 바탕/테두리 | `#e9e5f5` / `#b9b2d6` (미토큰, proposed `--disabled-bg`/`--disabled-line`) | measured |
| 오류 글자 | 엔진 실패 안내, 제한 안내 | `#b0213f`, `#b23a3a` (미토큰 2개 — 하나로 합칠지 open) | measured |
| (미사용) | 어디에도 쓰이지 않음 | `--danger` `#ff6b6b` | measured — 사용 0곳 |

### 글꼴

| Role | Parts | Token / value | Status |
| --- | --- | --- | --- |
| 표시 글꼴 | 로고, 제목, 좌표·승률 숫자, 모든 버튼·라벨 | `'Jua'` 400 (`@fontsource/jua` 자체 호스팅, 한글+라틴) | measured |
| 문장 글꼴 | 설명·캡션·도움말 문장 (`:root`) | `'Pretendard Variable'` 동적 부분 집합, 굵기 550~800 | measured |
| 숫자 | 전체 | `font-variant-numeric: tabular-nums`, 줄 높이 1.5 | measured |
| 글자 외곽선 | 로고 8px, 브랜드 5px, 큰 승률 6/5px, 결과 배너 10px | `-webkit-text-stroke` + `paint-order: stroke fill`, 색 `--ink` | measured |

글자 크기(px, 데스크톱 / 휴대폰): 로고 clamp(44, 12vw·9dvh, 96) · 결과 배너 clamp(40, 14cqw, 110) · 추천 좌표 64/40 · 추천 승률 56/40 · 주 버튼 30/25 · 대화상자 제목 26 · 말풍선 제목 22/18 · 알약·갈래 19/17 · 대결줄 17/15 · 본문 15/13 · 보조 14/12 · 캡션 12(설명 카드 `#current-card` 안 `.caption` 13 — **사용자 지시** 2026-11-10 “설명 카드 안 보조 글자 12px를 13px로”, [TASK](TASK.md#card-caption-13)) · 하한: 말풍선(추천 말풍선·내 수 평가 작은 말풍선) 안 글자 12px 이상(사용자 지시 2026-11-10, 좁은 칸의 `.hero-sub`와 `#review-context` 11→12) / 말풍선 밖은 11(휴대폰 `.coach-note`)·11.5(휴대폰 도움말 라이선스) 그대로. 판 안 표식 숫자는 `cqw` 비례(최소 8~13px)로 별도.

### 선·그림자·모서리

| Role | Parts | Token / value | Status |
| --- | --- | --- | --- |
| 입체 그림자(번짐 없는 아래 그림자) | 모든 떠 있는 요소 | `box-shadow: 0 Npx 0 var(--ink)` — N 단계 아래 | measured |
| 그림자: 카드 `--sh-card` | 말풍선, 내 수 평가, 복기 패널, 첫 안내, 복기 바, 도움말 창과 그 안 설명 상자(2026-11-10 “도움말 창을 카드 스타일로”) | 6px / 휴대폰 5px (이전 8·7·5 섞임) | 사용자 지시 2026-11-10 “역할별로 통일”, 값은 담당자 선택 |
| 그림자: 대화상자 `--sh-dialog` | 새 게임 확인(도움말 창은 2026-11-10부터 카드 역할) | 8px | 사용자 지시 2026-11-10, 값은 이전과 같음 |
| 그림자: 주 버튼 `--sh-main` | `.primary`(일반·`.mini`·`.go`·비활성), `.undo`(일반·비활성) | 7px / 휴대폰 6px (+ 안쪽 아래 `inset 0 -6px 0`) | measured(값 변경 없음, 토큰 이름만) |
| 그림자: 보조 버튼 `--sh-btn` | 알약, pill, 고르기, 아이콘 버튼, 취소, 승률 가이드 스위치 | 4px (이전 아이콘 휴대폰 3, 취소 5, 스위치 3) | 사용자 지시 2026-11-10, 값은 담당자 선택 |
| 그림자: 라벨·칩 `--sh-label` | 카드 라벨, 대결줄, 간이 분석 줄 | 3px (이전 대결줄 4) | 사용자 지시 2026-11-10, 값은 담당자 선택 |
| 판 위 그림자 | 돌·표식 3px(휴대폰 2px), 판 10px/7px | 역할 통일 대상 아님(판 안) | measured |
| 판 그림자 | `.board` | `0 10px 0 ink, 0 22px 30px #1a3d5c40` / 휴대폰 7px 단색 | measured |
| 눌림 | 버튼 `:active` | `translateY(3px)`+그림자 1px (주 버튼 5px+2px) — 그림자만큼 내려앉음 | measured |
| 외곽선 굵기 | 판 5/4 · 말풍선·주 버튼·대화상자 4/3 · 보조 버튼·카드 3 · 돌·작은 표식 2.5/1.5 | `--ink` 실선(판 위 기준 외 표식은 점선) | measured |
| 모서리 | 판 26/18 · 말풍선 26/20 · 대화상자 24 · 주 버튼 22/18 · 평가 카드 20/16 · 복기·취소 18 · 알약·고르기·메모 16 · 아이콘·pill 14 · 라벨 12 · 알약형 999 · 돌·표식 50% | — | measured |

### 간격·크기

| Role | Parts | Token / value | Status |
| --- | --- | --- | --- |
| 간격 단계 | flex/grid gap | 4 · 6 · 8 · 10 · 12 · 14 · 18 (8의 배수 체계 아님; 가장 많은 값 8px 17곳, 10px 13곳) | measured |
| 화면 여백 | `.stage` | 데스크톱 옆 배치 `clamp(20px, 3vw, 40px)`, 세로 배치 16px, 휴대폰 8px(2026-11-10 12→8, “휴대폰에서 판 더 크게”) | 휴대폰 값: 사용자 지시, 값은 담당자 선택 |
| 대결줄 높이·판 여유 | `#app` 첫 줄, 판 크기 계산의 여유 `--slack` | 64px / 휴대폰 52px(2026-11-10 58→52) · 여유 40px / 휴대폰 32px(높이 760 이하 휴대폰은 40 유지) | 사용자 지시 2026-11-10, 값은 담당자 선택 |
| 시작 화면 로고 | `.logo-art`, `.logo` | 그림 `zoom: .75`(112→84px), 제목 `clamp(36px, min(10vw, 7dvh), 72px)`(이전 최대 96px) | 사용자 지시 2026-11-10 “로고 영역 높이 줄여”, 값은 담당자 선택 |
| 판–옆 칸 | 데스크톱 옆 배치 열 간격·옆 칸 폭 | `clamp(24px, 3vw, 40px)` · `clamp(300px, 28vw, 400px)` | measured |
| 쌓임 간격 `--stack` | 말풍선 칸·버튼 칸 안의 블록 사이(보이는 간격), 칸 사이·판 아래 최소 | 12px / 휴대폰(폭 ≤ 700) 10px / 높이 ≤ 700 8px | **approved** — 사용자 승인 2026-11-10(턴 24 “저번에 간격 값 승인했으니까 DESIGN에 승인으로 바꿔” — 그 이전 승인 기록은 TASK·DESIGN에서 찾지 못해, 이 메시지를 승인 근거로 기록) |
| 블록 그림자 여백 `--drop` | 블록 아래 여백 = 그 블록의 입체 그림자 길이 | 그림자 역할 토큰을 그대로 씀: 카드 `--sh-card`, 버튼 줄 `--sh-main`, 알약 줄·안내 줄 `--sh-btn`, 간이 분석 줄 `--sh-label` | 방식(그림자 길이만큼 아래 여백): approved(간격 규칙과 함께) / 그림자 길이 값 자체: proposed(그림자 역할, 사용자 확인 전) |
| 판 그림자 여백 `--board-drop` | 세로 배치에서 판 칸 아래 | 10px / 휴대폰 7px / 옆 배치 0 | **approved** — 사용자 승인 2026-11-10(턴 24 “저번에 간격 값 승인했으니까 DESIGN에 승인으로 바꿔” — 그 이전 승인 기록은 TASK·DESIGN에서 찾지 못해, 이 메시지를 승인 근거로 기록) |
| 알림 줄 안쪽 여백 | 금수 알림 `.forbid-notice`·엔진 알림 `.engine-alert` | 위아래 3 · 좌우 10 (높이 39→33, 14px 글자 한 줄) | 줄이기: 사용자 지시 2026-11-10 “안내 줄(금수·엔진 알림) 안쪽 여백 좀 줄여” / 값 3·10: 담당자 선택, 사용자 확인 전 ([TASK](TASK.md#notice-padding)) |
| 조작 높이 | 데스크톱: 주 버튼·되돌리기 76 · 알약·갈래·아이콘 46 · 고르기·스위치 44 · pill 42. 휴대폰(폭 ≤ 700): 주 버튼·되돌리기 60, **판 밖 다른 모든 버튼 높이·폭 ≥ 44**(아이콘 44×44, 알약·pill·스위치 44, 고르기·다시 분석·취소 최소 44, 되돌리기 폭 ≥ 64) | 휴대폰 값: 사용자 지시 2026-11-10 / 나머지 measured |
| 배치 전환 | 옆 배치: 폭 ≥ 900 그리고 가로:세로 ≥ 5:4. 휴대폰 값: 폭 ≤ 700 | — | measured |

## 다크 모드 (2026-11-10, 사용자 지시 — DRAFT)

사용자 지시: “다크 모드 추가해. 시스템 설정 따라가게. 색 토큰만 바꾸는 식으로.” 상태: 구현, **사용자 시각 확인 전**, 다크 색 값은 담당자 선택. 제품 정의(JOEFLOW rev 20)에 테마 기능이 없고 v0.1은 “테마 전환은 초기 필수 범위가 아니다”라고 적었으므로 다크 모드 자체는 **product decision pending**(제품 결정 대기, 읽은 revision 20) — 지시대로 구현했고 정의 반영은 JOEFLOW 재진입에서 한다.

- 방식: `src/tokens.css`의 `@media (prefers-color-scheme: dark)`에서 색 토큰 값만 바꾼다. 화면별 다크 규칙은 없다. `color-scheme: light dark`.
- 준비(라이트 화면 변화 없음, DS-EQ 2249/2249 동일): 한 토큰이 여러 역할을 하던 곳을 나눴다 — `--ink`(글자) / `--line`(외곽선·입체 그림자·글자 외곽선) / `--board-line`(판 안 돌·표식 외곽선, 두 모드 모두 진하게) / `--on-fill`·`--on-fill-soft`(노랑·연두·하늘·분홍 채움과 판 위 글자, 두 모드 모두 진하게). 판 밖 원시 색 13종을 역할 토큰으로 바꿈: `--ink-body`, `--on-sky`, `--on-sky-2`, `--sky-3`, `--error`, `--error-strong`, `--accent-text`, `--ok-bg`, `--warn-bg`, `--disabled-bg`, `--disabled-line`, `--switch-off`(+ 엔진 막대 바탕 `--paper`).
- 다크 값: 밤하늘 `--sky-1/2/3` #141d3d/#1a2650/#22305e, 표면 `--paper` #2b2550·`--cream` #3a3160, 글자 `--ink` #f3f0ff·`--ink-soft` #c4bce6·`--ink-body` #ddd7f5, 외곽선·그림자 `--line` #a79fe0(짙은 외곽선은 밤하늘 대비 1.3:1이라 안 보여 밝은 라벤더로), 하늘 위 글자 #a9d8ff/#9fd0ff, 오류·강조 #ff9a9a/#ff8fa8/#ff8fb4, 채움 #24452f/#4a2530/#3a3458/#5a5280/#4a4370. 승률 가이드 스위치 켬(다른 세션 추가, [TASK](TASK.md#toggle-blue)) `--switch-on` #5aa2ff·`--switch-on-bg` #1f3566.
- 그대로 두는 것: 판(나무·격자·좌표·돌·표식·추천 고리), 노랑·연두·하늘·분홍 채움, 하늘의 흰 반투명 구름(밤하늘에서는 회색 원으로 보임 — 사용자 판단 필요).

## 화면 규칙

상태 표기: **사용자 지시**는 사용자가 정한 기준, **measured**는 출하 화면이 지금 따르는 관계를 적은 것(승인 전까지 제안 수준의 규칙).

1. **한 화면, 스크롤 없음** (사용자 지시): 1440×900·390×844를 포함한 모든 지원 크기에서 페이지 가로·세로 스크롤과 화면 밖·잘린 요소가 없다. 남는 높이가 모자라면 덜 중요한 것부터 접는다(설명 문장 → 평가 문장 → 라벨 순, `@container hud` 단계).
2. **위계** (사용자 지시): ① 판과 기준 표식 ② 말풍선의 좌표·승률(화면에서 가장 큰 글자) ③ 노란 주 버튼 ④ 2·3순위·상대 예상 알약 ⑤ 작은 고지문·토글. 크기·밝기 순서가 이 차례를 거스르지 않는다.
3. **핵심 정보만** (사용자 지시): 설명은 한 줄 이유(말풍선 3줄, 휴대폰 2줄 잘림). 부가 설명은 `자세히 보기`·도움말에서만 연다.
4. **카툰 입체 표현** (사용자 지시 + measured 값): 떠 있는 모든 요소는 `--paper`/`--cream` 표면 + `--ink` 실선 외곽선 + 번짐 없는 `--ink` 아래 그림자. 누르면 그림자 길이만큼 내려앉는다(2026-11-10 사용자 지시로 모든 버튼 통일: 그림자 길이 − 1px 내려가고 1px 남음, 그림자 아래 끝 제자리, 쉬는 때의 안쪽 음영 유지). 흐린 번짐 그림자는 판 하나만 쓴다.
5. **판 위 표식** (사용자 지시 rev 14·rev 20): 실제 돌만 불투명·실선. 추천·후보·착수 예정·내 수순·금수 ✕는 점선. 상대 예상 수순만 반투명(0.5) 실선 돌 + 번호.
6. **색만으로 구별하지 않는다** (measured, v0.1부터 유지): 승률 색 단계·표식 색에는 항상 숫자·글자·모양이 함께 있다.
7. **글꼴 역할** (measured): 숫자·버튼·제목은 Jua, 두 줄 이상 문장은 Pretendard. 한 요소에 두 글꼴을 섞지 않는다.
8. **크기 전환** (measured): 폭 ≤ 700은 휴대폰 토큰 쌍, 폭 ≥ 900·가로:세로 ≥ 5:4는 판 왼쪽 + 옆 칸, 그 밖은 판 → 말풍선 → 버튼 세로 배치. 같은 역할은 전환 뒤에도 같은 토큰 단계를 쓴다.
8-1. **휴대폰 가로**(사용자 지시 2026-11-10 “휴대폰 가로 모드(844×390) 대응해”, 값은 담당자 선택 — 사용자 확인 전): 높이 ≤ 500이고 가로:세로 ≥ 5:4이면 판 왼쪽(화면 높이에 맞춤) + 오른쪽 칸 `clamp(300px, 48vw, 420px)`. 대결줄 48px, 주 버튼 60px, 판 밖 버튼 44px 이상(규칙 9의 휴대폰에 포함), 말풍선 글자·안쪽 여백은 세로 휴대폰 값(외곽선·모서리·그림자는 데스크톱 값). 시작 화면은 제목·시작 버튼 왼쪽 / 고르기 오른쪽, 복기 바는 두 칸 위 전체 폭, 도움말은 세 단. 두 요소가 모두 숨은 빈 안내 줄은 높이를 차지하지 않는다.
9. **조작 크기 하한**: 휴대폰(폭 ≤ 700)은 판 밖 모든 버튼 높이·폭 ≥ 44px — **사용자 지시**(2026-11-10 “휴대폰에서 보조 버튼 포함 전부 44px 이상”). 주 버튼은 60px. 데스크톱은 measured ≥ 36px(출하 최소 pill 42). 판 교차점은 대상 아님.
10. **동작 감소**(사용자 지시 2026-11-10, v0.1 “동작 감소 설정에서 장식 전환을 제거한다”를 구현): 시스템의 동작 줄이기(`prefers-reduced-motion: reduce`)가 켜지면 모든 CSS 애니메이션·전환을 끈다 — 착수 예정·추천 고리 회전, 로고 별 반짝임·돌 떨어짐, 결과 배너 등장, 계산 중 점, 스위치·막대 전환. 고리는 회전 없이 같은 자리에 점선 그대로 남는다.

## 간격 규칙 (2026-11-10, 사용자 요청 “간격 규칙 정하고 코드 맞추고”)

상태: **APPROVED** — 사용자 승인 2026-11-10(턴 24 “저번에 간격 값 승인했으니까 DESIGN에 승인으로 바꿔” — 그 이전 승인 기록은 TASK·DESIGN에서 찾지 못해, 이 메시지를 승인 근거로 기록). 승인 범위: SP-1~3 규칙과 `--stack` 12/10/8·`--board-drop` 10/7/0 값, “보이는 간격” 기준. 범위 밖(사용자 확인 전 그대로): 그림자 길이 값, 휴대폰 좌우 여백 8px·대결줄 52px·판 여유 `--slack`(턴 19), 알림 줄 안쪽 여백 3/10(턴 10). 문서 전체 Status는 DRAFT 그대로. 값(12/10/8)은 출하 HUD 간격 값을 그대로 썼고, 바뀐 것은 “상자 간격”이 아니라 “보이는 간격”을 같게 만든 방식이다.

- **SP-1 블록 사이:** 말풍선 칸(`.hud`)과 버튼 칸(`.cta-area`) 안에서 위아래로 쌓인 블록(첫 안내, 평가 카드, 말풍선, 간이 분석 줄, 알약 줄, 금수·엔진 알림, 버튼 줄, 되돌리기 안내, 안내 줄) 사이의 **보이는 간격 = `--stack`**. 보이는 간격은 위 블록에서 실제로 칠해진 가장 아래(테두리·바탕·글자 상자 + 번짐 없는 아래 그림자)부터 아래 블록의 칠해진 가장 위까지. 구현: 칸의 `gap: var(--stack)` + 각 블록 `margin-bottom: var(--drop)`(그 블록 그림자 길이).
- **SP-2 칸 사이:** 판 → 첫 블록, 말풍선 칸의 마지막 블록 → 버튼 칸의 첫 블록은 보이는 간격 **≥ `--stack`**. 남는 높이는 여기에 둔다(버튼 줄은 화면 아래에 붙는다). 세로 배치에서는 판 칸 아래에 `--board-drop`을 두고 판 크기 계산에서 같은 값을 뺀다(판 폭 최대 10px 작아짐: 820x1180 664→654, 768x1024 508→498, 489x866 446→439, 375x667 297→290, 360x640 270→263).
- **SP-3 그림자 단계:** 같은 역할 버튼은 상태(보조·두기·비활성)가 바뀌어도 같은 그림자 단계(주 버튼 7/6)를 쓴다. 그래야 `--drop` 하나로 간격이 맞는다.
- 새 블록을 추가하면 그 블록의 그림자 길이를 `--drop`으로 주고 `work/design/spacing-check.mjs --expect`를 돌린다.

## 복기 상단 바 (2026-11-10, 사용자 지시)

사용자 지시: “복기 모드에 상단 바 추가해: 현재 수 번호, 총 수, '종료 판으로' 버튼. 기존 복기 버튼들은 그 바로 옮겨.” 상태: 구현, 사용자 시각 확인 전.

- 복기 중에만 판 위(옆 배치는 판·옆 칸 두 칸 위 전체 폭)에 흰 표면 바 한 줄: 왼쪽 큰 숫자 `현재 수` + `/ 총 N수`, 오른쪽 `◀ 이전 수` `다음 수 ▶` `종료 판으로`(기존 버튼 그대로, 같은 id·같은 동작). 바 그림자 5px, 바 → 판 보이는 간격 ≥ `--stack`(SP-2). 키보드 순서는 바가 판보다 먼저.
- 바 높이(데스크톱 60px, 휴대폰 52px) + 그림자 + `--stack`만큼 판 크기 계산에서 뺀다(`--rbar`). 높이 760 이하 휴대폰은 복기 중 말풍선 칸 최소 높이 160 → 170px.
- 말풍선 칸의 복기 패널에는 `복기 중 · n수 색 좌표`와 `종료된 대국: 결과 · 총 N수`가 그대로 남는다. 현재 수는 대결줄 `복기 n/N수`, 바, 패널 세 곳에 보인다(줄일지는 사용자 결정 — Open Decisions).
- 제품 정의(JOEFLOW rev 20)는 복기를 “기존 기능”으로만 두고 버튼 위치를 정하지 않는다. 버튼·수 표시의 위치 이동은 내용과 경로가 같아 디자인 결정이다(아래 Display before/after). 복기 상단 바라는 새 표시 영역은 정의에 없어 **product decision pending**(제품 결정 대기, 읽은 revision 20) — 사용자 지시대로 구현했고 정의 반영은 JOEFLOW 재진입에서 한다.

## 이유 더 보기 (2026-11-10, 사용자 지시 — product decision pending)

사용자 지시: “설명 카드에 '이유 더 보기' 접기 버튼 추가.” 제품 정의(JOEFLOW rev 20)에 없는 새 조작이므로 **product decision pending**(제품 결정 대기, 읽은 revision 20) — 지시대로 구현했고 정의 반영은 JOEFLOW 재진입에서 한다. 아래 동작 중 사용자가 정하지 않은 것(버튼이 보이는 조건, 펼친 뒤 글자 “이유 접기”, 카드 내용이 바뀌면 닫힘, 좁은 칸에서 알약 줄 접기)은 담당자가 고른 것이며 같은 재진입의 질문이다.

- 버튼: 설명 카드(`#current-card`) 오른쪽 위, 카드 라벨과 같은 줄에 겹쳐 둔다(새 줄을 만들지 않음). 글자 버튼(밑줄), 누르는 영역 데스크톱 36px·휴대폰 44px. 설명 문장이 줄 수 제한으로 잘리거나 좁은 칸 접기로 숨었을 때만 보인다(1440x900처럼 다 보이면 버튼 없음). `aria-expanded`, `aria-controls="card-text"`.
- 펼침: 줄 수 제한과 좁은 칸 접기를 풀고 설명 전체를 보인다. 글자는 “이유 접기”. 그 때문에 말풍선 칸이 넘치면(측정) 펼친 동안만 후보 알약 줄을 접는다.
- 카드 설명이 바뀌면(다음 수 등) 닫힌 상태로 돌아간다.

## Display before/after

2026-11-10 복기 상단 바:

- before: 이전 수·다음 수·종료 판으로 버튼 | 같은 라벨·동작 | 대국 화면 → 종료 → 대국 복기 (위치: 말풍선 칸 복기 패널)
- after: 이전 수·다음 수·종료 판으로 버튼 | 같은 라벨·동작 | 대국 화면 → 종료 → 대국 복기 (위치: 판 위 복기 상단 바)
- before: 현재 수 번호·총 수 | 현재 수 번호, 총 수 | 대국 화면 → 종료 → 대국 복기 (위치: 대결줄, 복기 패널)
- after: 현재 수 번호·총 수 | 현재 수 번호, 총 수 | 대국 화면 → 종료 → 대국 복기 (위치: 대결줄, 복기 패널, 복기 상단 바)

두 쌍 모두 내용과 경로가 같아 위치 변경은 디자인 결정이다. 복기 상단 바라는 새 표시 영역은 product decision pending(위 절).

2026-11-10 이유 더 보기:

- before: 후보 알약 줄(2·3순위) | 후보 좌표와 승률 | 대국 화면 → 내 차례 추천
- after: 후보 알약 줄(2·3순위) | 이유를 펼쳐 말풍선 칸이 넘칠 때만 hidden, 접으면 다시 보임 | 대국 화면 → 내 차례 추천 → 이유 더 보기

내용이 다르므로 product decision pending(이유 더 보기 절과 같은 재진입).

## Rule Coverage

**한 번에 실행(2026-11-10):** `npm run design:check`(기본 2크기), `-- --all`(12크기), `-- --sizes WxH,...`, `-- --only 이름,...`, CSS 정리 전후 비교는 `-- --save-baseline` 후 `-- --baseline`. 빌드 → preview(`GOMOKU_DEV_PORT`, 기본 5199) → tokens(DS-T·F·H·O), spacing(DS-SP·SP-O·TOUCH·RB), shadow(DS-SH), ring(DS-RING), board-marks(DS-BM), contrast(DS-CR), motion(DS-MO), contrast-code(DS-C, 정보용 — 실패해도 종료 코드에 넣지 않음) 순서로 돌고, 하나라도 실패하면 종료 코드 1. 전체 출력은 `.cache/design-check/<이름>.log`. 검사는 동시에 4개씩 돌고(`-- --jobs N`, `-- --serial`), 간격 검사는 크기별로 3개씩 동시에 돈다(`GOMOKU_SIZE_JOBS`) — 2026-11-10 속도 개선, 검사 내용·범위는 같음. 아래 개별 스크립트도 그대로 쓸 수 있다.

검사 스크립트: `work/design/spacing-check.mjs`(간격·넘침, 렌더, `--expect`면 어긋날 때 종료 코드 1), `work/design/pixel-runs.mjs`(캡처 픽셀 세로줄), `work/design/ds-v1-check.mjs`(렌더), `work/design/ds-v1-spot.mjs`(캡처 픽셀 스폿), `work/design/ds-v1-contrast.mjs`(코드), `work/design/token-inventory.mjs`(코드). 렌더 검사는 `vite build` 후 `vite preview`로 띄운 빌드에서 잰다(dev 서버는 이 작업 폴더에서 글꼴 403 — [ISSUES ENV-05](ISSUES.md#env-05)). 엔진 파일이 없는 동안 대국 상태에 들어갈 수 없어 상태는 시작 화면(엔진 실패 표시)·도움말뿐이다([ISSUES ENV-06](ISSUES.md#env-06)).

**검사 크기(2026-11-10 사용자 지시 “1440이랑 390만”):** `spacing-check.mjs`·`ds-v1-check.mjs`·`capture-matrix.mjs`는 기본으로 1440x900·390x844 두 크기만 돈다(`work/design/sizes.mjs`). 아래 표의 Sizes 열이 12인 행은 `--all`(또는 `GOMOKU_ALL_SIZES=1`)로 돌렸을 때의 범위이고, 기본 실행에서는 나머지 10크기(1920x1080, 1366x768, 1280x720, 1024x768, 820x1180, 768x1024, 489x866, 430x932, 375x667, 360x640)가 **unmeasured**다. 이 10크기에서만 드러난 결함이 있었다(DS-03 작은 휴대폰 복기 잘림, 휴대폰 버튼 36~40px, 1280x720 시작 화면 간격).

| Rule | Check | Spot check | Layouts | Sizes | States | Unmeasured |
| --- | --- | --- | --- | --- | --- | --- |
| DS-O 한 화면(규칙 1) | ds-v1-check DS-O: 문서 스크롤, 화면 밖, 잘림 | 1440x900 intro: check 0 out/clip/scroll / observed 캡처 `work/design/shots/ds-v1-1440x900-intro.png`에서 모든 요소 가장자리가 화면 안 | 세로·옆 배치·휴대폰 | 12 (1920x1080~360x640) | intro(엔진 실패), help | 대국 상태 전부(추천·예정·평가·종료·복기). rev 20 매트릭스(72장)는 같은 style.css의 과거 근거이며 이번에 재실행 안 함 |
| DS-T 토큰 역할 렌더 일치(토큰 표) | ds-v1-check DS-T: 역할별 계산 스타일 = 표 값, 글꼴 로드 상태 | 2026-11-10 재확인(그림자 통일 뒤): 1440x900 말풍선 그림자 check 6px / observed 6px(픽셀 x=1000, 356–365 = 테두리 4 + 그림자 6); 390x844 check 5px / observed 5px(x=40, 569–576 = 3 + 5). 이전 기록 8px/8px은 통일 전 값 | 세로·옆 배치·휴대폰 | 12 | intro | 판·알약·돌·표식 역할, 색 토큰 중 ink·paper 밖, 높이 720 이하의 `.tagline` |
| DS-F 글자 하한 11px | 코드: token-inventory FONT_PX 최소 11px(판 밖). 렌더: ds-v1-check DS-F | not spot-checked | 세로·옆 배치·휴대폰 | 12 | intro | 대국 상태·도움말 렌더 글자(휴대폰 도움말 11.5px은 코드로만) |
| DS-H 조작 높이(규칙 9) | ds-v1-check DS-H: 판 밖 보이는 버튼 높이 | 1440x900 주 버튼: check 76 / observed 76 (픽셀 727–802) | 세로·옆 배치·휴대폰 | 12 | intro | 대국 상태의 알약·갈래·pill·스위치·취소 |
| DS-SP 간격 규칙 SP-1·SP-2(·SP-3) | spacing-check: 블록 쌍별 보이는 간격 = `--stack` ±0.5px(SP-1), ≥ `--stack`−0.5px(SP-2). 대국 상태는 검사 전용 가짜 엔진(`work/design/stub-engine.mjs`, 배치 전용) | 2026-11-10 재확인(그림자 통일·휴대폰 판 변경 뒤): 1440x900 candidates 말풍선→알약 check 12 / observed 12(픽셀 x=1000, 365→378), 내 수 평가→말풍선 check 12 / observed 12(135→148); 390x844 말풍선→알약 check 10 / observed 10(x=40, 576→587). 이전 기록(x=956 등)은 변경 전 캡처 | 세로·옆 배치·휴대폰 | 12 | setup, tutorial, candidates, preview, reset-confirm, undone, finished, replay-start, replay, help, forbid-notice-forced(DOM 강제), engine-alert, engine-stopped | 자세히 보기, 실제 금수 자리(강제 표시로 대신), 실제 엔진 문구 길이, 블록 안 내부 여백 |
| DS-RB 복기 상단 바(바 표시, 바 → 판 SP-2, 넘침) | spacing-check: replay-start·replay 상태의 `replay-bar>board` ≥ `--stack`, 넘침 | 390x844 replay: check 10 / observed 10 (픽셀 x=200, 바 아래 111-118 → 판 129); 1440x900 replay: check 17 / observed 17 (x=500, 131-138 → 156) | 세로·옆 배치·휴대폰 | 12 | replay-start, replay | 실제 엔진 대국의 긴 수(두 자리·세 자리 수) 폭, 무승부 |
| DS-TOUCH 휴대폰 조작 크기(규칙 9) | spacing-check touch: 폭 ≤ 700에서 판 밖 보이는 버튼 높이·폭 ≥ 44px. ds-v1-check DS-H(시작 화면) 같은 기준 | 375x667 candidates 알약: check 44 / observed 44 (픽셀 x=40, 위 테두리 473 → 아래 테두리 끝 516); 375x667 승률 가이드 스위치: check 44 / observed 44 (x=295, 608 → 651) | 휴대폰 | 5 (489x866, 430x932, 390x844, 375x667, 360x640) | setup, tutorial, candidates, preview, reset-confirm, undone, finished, replay-start, replay, help | 폭 700 초과 태블릿 터치, 실제 엔진 문구로 늘어난 버튼 |
| DS-RING 추천 고리 색 | `work/design/ring-check.mjs`: `.m1` 테두리 계산 색과 판 나무색(`--wood-1`, `--wood-2`) 대비 ≥ 3:1, 캡처에서 고리 근처 가장 진한 초록 픽셀 | 1440x900 candidates: check rgb(23,105,42) / observed 캡처 픽셀 rgb(23,105,42), 확대 비교 `work/design/shots/ring-1440x900-before-after.png` | 세로·옆 배치·휴대폰 | 12(--all) | candidates | 필승 고리(노랑), 가이드 대체 `.hint` 상태(가짜 엔진으로 재현 안 됨), 다른 점선 후보(남색)와의 구별 |
| DS-EQ CSS 정리 전후 계산 스타일 동일 | `work/design/css-equivalence.mjs dump/diff`: 판 밖 모든 요소·판 위 표식의 내용 길이와 무관한 계산 스타일 28개 속성과 토큰 변수 28개 | 390x844 candidates 말풍선→알약: dump 같음 / observed 10px 그대로(픽셀 x=40, 575→586) | 세로·옆 배치·휴대폰 | 4 (1440x900, 820x1180, 390x844, 360x640) | setup, tutorial, candidates, preview, help | 종료·복기·알림 상태, 너비·높이처럼 내용에 따라 바뀌는 값 |
| DS-CR 렌더 대비(라이트·다크) | `work/design/contrast-check.mjs`: 판 밖 글자 ≥ 4.5:1(큰 글자 3:1, 외곽선 2px 이상이면 외곽선 색 포함), 버튼 경계 ≥ 3:1, 실제 바탕(그라데이션은 가장 나쁜 색) | 다크 1440x900 candidates 설명 문장: check 통과(#ddd7f5 on #2b2550) / observed 캡처 픽셀 rgb(221,215,245) on rgb(43,37,80) 10.19:1 | 옆 배치·휴대폰 | 2 (기본) | setup, tutorial, candidates, preview, finished, replay, help × light·dark | 판 위 표식 글자, 알림 상태, 구름 위 글자, 비활성 버튼(예외) |
| DS-BM 판 위 표식 대비(라이트·다크) | `work/design/board-marks-check.mjs`: 추천 고리 `.m1`·금수 ✕ `.mark.forbid` 계산 색 대 판 나무색 ≥ 3:1, 캡처 픽셀 | 다크 1440x900 금수 ✕: check 1.55~1.96:1 / observed 픽셀 rgb(223,112,142) 1.80:1; 추천 고리: check 3.99~5.03:1 / observed 4.34:1 | 옆 배치·휴대폰 | 2 (기본) | 금수 자리가 있는 흑 차례 × light·dark | 필승 고리, 후보 점선 숫자, 상대 예상 돌 |
| 도움말 창 카드 스타일 | `#help-dialog` = 말풍선 카드(외곽선 4/3, 모서리 26/20, 그림자 `--sh-card`, 안쪽 여백 16·22·18 / 10·14·12), `.help-note` = 내 수 평가 카드(크림, 외곽선 3, 모서리 20/16, 그림자 `--sh-card`) | 사용자 지시 2026-11-10, 값은 카드 값 그대로(사용자 확인 전) | shadow-check card 역할, spacing/tokens 넘침(help 상태) |
| DS-SH 그림자 역할 통일 | `work/design/shadow-check.mjs`: 역할(카드·대화상자·주 버튼·보조 버튼·라벨) 안 모든 보이는 요소의 아래 그림자 길이가 하나 | 1440x900 candidates 말풍선: check 6 / observed 6(픽셀 x=1000, 356–365 = 테두리 4 + 그림자 6); 내 수 평가: check 6 / observed 6(127–135 = 3 + 6) | 세로·옆 배치·휴대폰 | 12(--all) | setup, tutorial, candidates, preview, reset-confirm, finished, replay, help | 판 위 돌·표식, 알림 줄(그림자 없음), 누른 상태 |
| DS-MO 동작 감소(규칙 10) | `work/design/motion-check.mjs`: reduce에서 실행 중 CSS 애니메이션 0개(시작 화면·예비 착수), 착수 예정 고리 0.6초 간격 두 캡처가 같음. no-preference는 대조군(움직여야 통과) | 1440x900 reduce 예비 착수: check 0개·캡처 같음 / observed 계산 스타일 animation none, 점선 고리 그대로(`work/design/shots/motion-reduce-1440x900-preview-ring.png`) | 옆 배치·휴대폰 | 2 (기본) | setup, preview × reduce·no-preference | 종료 배너·첫 안내·계산 중 점 상태(전역 규칙이라 같은 방식으로 꺼짐, 개별 측정 안 함) |
| 휴대폰 가로(규칙 8-1) | design:check `--all`에 844x390 추가(`work/design/sizes.mjs`), 휴대폰 판정 `isPhone`(폭 ≤ 700 또는 높이 ≤ 500·가로:세로 ≥ 5:4)으로 터치 흉내·44px 검사. spacing-check는 위아래로 겹치는 쌍만 간격을 잼(옆 칸 쌍 제외) | 844x390 캡처 12장 직접 봄(시작·추천·복기·도움말) | 휴대폰 가로 | 844x390(--all), 740x360·667x375는 `--sizes`로만 | 13 | 740x360 복기·금수 알림 잘림([DS-08](ISSUES.md#ds-08)), 실제 기기 주소창 높이 |
| DS-BT 말풍선 글자 12px 이상 | `work/design/bubble-text-check.mjs`(design:check의 bubble-text): `#current-card`·`#review-card` 안 보이는 글자 렌더 크기 ≥ 12px | 390x844 예비 착수 `.hero-sub`: check 12px / observed 캡처에서 그 줄 글자가 이전보다 커짐(확대 비교 `work/design/shots/bubble-text-390x844-before-after.png`) | 세로·옆 배치·휴대폰·휴대폰 가로 | 13(--all) | setup, candidates, preview, finished, replay | 자세히 보기 상태, AI 응수 중(review) 상태의 `#review-context` |
| DS-PR 눌림 효과(규칙 4) | `work/design/press-check.mjs`(design:check의 press): 마우스를 누른 채 계산 스타일 — 내려간 거리 + 남은 그림자 = 쉬는 그림자, 남은 그림자 값이 모든 버튼에서 하나, 안쪽 음영 유지 | 390x844 종료 “새 게임!”: check 5px 내려감 + 1px / observed 캡처 픽셀 위 테두리 10→15행, 아래 테두리+그림자 끝 75행 그대로(`work/design/shots/press-390x844-rest.png`, `-down.png`) | 세로·옆 배치·휴대폰·휴대폰 가로 | 13(--all) | 시작·추천·예비 착수·새 게임 확인·종료의 버튼 13종 | 키보드(Enter) 누름, 터치 누름(마우스로 흉내) |
| 이유 더 보기 | spacing-check의 reason-open 상태(버튼이 보이면 열어 간격·넘침·터치 측정 후 닫음), tokens·bubble-text·press | 390x844: 닫힘/열림 캡처 직접 봄(`work/design/shots/reason-390x844-closed-open.png`) — 버튼은 라벨 줄 오른쪽, 열면 설명 한 줄 보이고 알약 줄 유지 | 세로·옆 배치·휴대폰·휴대폰 가로 | 13(--all), 버튼은 8크기에서 보임 | candidates·reason-open | 실제 엔진의 긴 설명, 키보드 조작, 화면 읽기 프로그램 |
| DS-SP-O 간격 변경 뒤 넘침 | spacing-check overflow: 문서 스크롤·화면 밖·잘림·잘린 그림자(shadow-clip, 2026-11-10 추가) | 375x667 forbid-notice-forced 말풍선 그림자: check shadow-clip / observed 8행(정상 9행), 픽셀 x=30 | 세로·옆 배치·휴대폰 | 12 | setup, tutorial, candidates, preview, reset-confirm, undone, finished, replay-start, replay, help, forbid-notice-forced, engine-alert, engine-stopped | 자세히 보기 |
| DS-S(대체됨 → DS-SP) 말풍선 → 주 버튼 보이는 간격 | ds-v1-check S: 상자 간격과 그림자 뺀 보이는 간격 | 1440x900: check 20 / observed 20; 390x844: check 22 / observed 22; 375x667: check 6 / observed 6 (ds-v1-spot 픽셀) | 세로·휴대폰(시작 화면) | 12 | intro | 승인된 기준값 없음(Open Decisions). 대국 상태 HUD 간격 |
| DS-C 글자 대비 | ds-v1-contrast: 토큰 글자/바탕 15쌍 WCAG 비 | not spot-checked | — | — | — (코드 값) | 그라데이션·구름 위 실제 픽셀 대비, 판 위 표식 숫자 |
| DS-V 위계·카툰 표현(규칙 2·4) | 수동 관찰: 캡처 `ds-v1-1440x900-intro.png`, `ds-v1-390x844-help.png` | not spot-checked (관찰 자체만 있음) | 옆 배치·휴대폰 | 2 | intro, help | 대국 화면 위계(가장 중요한 추천 화면) |
| DS-M 판 표식(규칙 5) | E2E AC-020·021(`tests/e2e/game.spec.ts`) | not spot-checked | — | 1440x900, 390x844 | 예정 수순 | 이번에 실행 못 함(엔진 없음) |

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

- **사용자 승인 필요:** 이 v1 토큰·화면 규칙 전체(DRAFT → APPROVED는 사용자 명시 승인만).
- **조작 높이(데스크톱):** 휴대폰은 44px로 정해졌다(사용자 지시). 데스크톱·태블릿(폭 > 700)의 pill 42px 등을 44로 맞출지는 미정.
- ~~간격 규칙 SP-1~3 값 확인~~ → 2026-11-10 사용자 승인(턴 24, 위 간격 규칙 절). 시작 화면의 제목·말풍선·버튼 사이 18px(작은 화면 `--stack`)는 SP-2 ≥ 기준으로 승인 범위 안.
- **수 세기 분홍 글자 대비:** `--pink` `#ff6f91` on `#ffffff` 2.65:1(15px Jua) — [ISSUES DS-01](ISSUES.md#ds-01).
- **미토큰 원시 색 값 57종(알파 포함)·미사용 `--danger`:** CSS 변수로 정리(이름 proposed)하는 코드 작업은 아직 하지 않았다. 하면 DS-T·DS-O 전 행 재실행.
- **간격 단계:** 4·6·8·10·12·14·18 그대로 둘지, 8 기준 단계로 줄일지.
- 대국 상태 렌더 검사는 엔진 파일을 받은 뒤 다시 돌린다(ENV-06).
- **복기 중 현재 수 세 곳 표시:** 대결줄 `복기 n/N수`·복기 상단 바·패널 `복기 중 · n수`. 하나를 빼면 숨김 변경이라 사용자 결정이 필요하다.

## Amendment Rule

Only explicit user approval promotes DRAFT to APPROVED. Preserve APPROVED Rev N
while proposing a separately labeled DRAFT Rev N+1 in this same file. Replace the
active approved rule set only after proof and explicit approval. Local refinement
within approved intent does not automatically create a material revision.

---

## 이력 — 시각 방향 기록 (v0.1 ~ rev 20)

아래는 이전 기록을 그대로 둔 것이다. 색·글꼴 값은 위 v1 토큰 표가 현재 출하 값이며, v0.1·v0.2의 색 제안은 대체됐다.

### 시각 방향 — 제안 v0.1 (색·글꼴은 v0.3으로 대체)

작성: 2026-10-22. 권한: 사용자가 화면 구성 선택을 맡겼으나 **이 시각안에 대한 사용자 승인 없음**. 상태: v0.1 방향을 구현에 사용했고 두 지정 크기의 실제 렌더를 개발자가 확인했다. 사용자 시각 승인과는 다르다. 실행 근거는 [TASK](TASK.md#implementation), 제품 흐름은 [ROADMAP.md](ROADMAP.md#선택한-학습-흐름)가 소유한다.

### 방향

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

### 배치

- **1440×900:** 짧은 제목/규칙·새 게임 행 아래, 왼쪽 판 520px, 간격 50px, 오른쪽 설명 350px. 실제 화면 점검 후 기본 판과 주요 행동을 같은 화면에서 조작하기 쉽도록 초기 620px 제안보다 줄였다. 긴 해설은 세로 스크롤할 수 있다.
- **390×844:** 좌우 16px 여백, 제목 → 차례/짧은 안내 → 폭 358px 이내 판 → 선택 좌표/확정 버튼 → 추천·해설 순서. 긴 해설은 자연스러운 세로 스크롤. 판 폭을 줄여 모든 글을 억지로 한 화면에 넣지 않는다. 고정 하단 바가 판/버튼을 덮지 않도록 한다.
- 판은 정사각형. 외곽 교차점도 누를 수 있도록 내부 가장자리 여백과 좌표 영역을 둔다. 열 A–O(중간 문자 생략 없음), 행 1–15, 위에서 아래로 증가. 좌상단 A1, 중심 H8. 화면·검사·해설 모두 이 기준을 공유한다.
- “현재 추천”과 “직전 수 해설”을 제목으로 분리한다. 예상 수가 있는 검토 중에는 그 판을 그대로 유지한다. 다음 판으로 넘어가면 이전 예상 고리는 지우고 직전 수 글만 출처 수와 함께 남긴다.

### 상호작용 표현

- 종료 후 복기는 판 위의 `대국 복기`로 진입하고 같은 영역의 `이전 수 / 다음 수 / 종료 판으로`를 사용한다. (2026-11-10부터 이 세 버튼은 [복기 상단 바](#복기-상단-바-2026-11-10-사용자-지시)에 있다.) `복기 중`과 표시 중인 수·색·좌표, 실제 종료 결과·총 수를 함께 표시한다. 설명 카드는 선택한 수에 해당하는 당시 해설과 기준 수를 보여주고, 기존 직전 내 수 카드·추천/예상 고리는 숨긴다. 작은 점과 승리선은 표시 중인 판에만 적용한다. 복기 중 되돌리기는 비활성화하고 종료 판으로 복귀하면 다시 사용할 수 있다. 새 게임 버튼은 계속 사용 가능하다. 시각 승인 여부와 실제 검사 근거는 [복기 기록](TASK.md#replay)을 따른다.

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
