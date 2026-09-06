# Research Briefing Portal — bounded reference proof

범위: 현재 정적 페이지의 시각적 관계 조정. 권위는 `PRODUCT.md`와 `DESIGN.md` APPROVED Rev 1이며 두 문서와 레퍼런스는 변경하지 않는다. 새로운 디자인 권위나 사용자 승인을 생성하지 않는다.

## 레퍼런스 채택 판단 — 렌더 전

| 항목 | Reference A | Reference B |
| --- | --- | --- |
| SOURCE | 소유자가 제공한 `reference-a.md`; 실제 사이트·이미지 없음 | 소유자가 제공한 `reference-b.md`; 실제 사이트·스타일시트 없음 |
| EVIDENCE QUALITY | 명시된 관계에는 강한 근거. 미기재 값의 근거는 아님 | 명시된 관계에 근거 있음. 미적 적합성 점수는 아님 |
| KNOWN | 편집적 비대칭, 큰 제목/본문 대비, 이미지·텍스트 사이 여백, 낮은 장식 밀도 | 촘촘한 모듈 카드 그리드, 조밀한 메타데이터 묶음, 반복 박스 |
| UNKNOWN | 정확한 폰트, 모바일 간격, 모션 타이밍 | 반응형 순서, 정확한 간격 토큰 |
| TAKE | 제목/본문의 크기 대비, 비대칭 여백, 박스 없는 편집적 그룹 | 각 레코드 내부의 출처·날짜 결속 |
| DO NOT TAKE | 출처 브랜드·카피, 확인되지 않은 값, 존재하지 않는 참조 이미지 | 카드 그리드·반복 박스, 확인되지 않은 반응형 순서 |
| WHY | 차분한 편집적 위계와 단일 주 초점에 부합 | 메타데이터 결속은 유용하나 카드 벽은 승인 방향과 충돌 |
| APPLIES TO | hero, 제목/lead 관계, 열린 요약 목록 | 각 요약의 source/time 묶음만 |

근거 품질과 채택 적합성은 별개다. B의 확인된 카드 관계도 승인 방향보다 우선하지 않는다. 복수 레퍼런스를 다수결로 혼합하지 않는다.

## 의도·관찰 기준 — 렌더 전

- 대상: 초기 정적 상태의 전체 페이지. 실제 Chrome 뷰포트 desktop 1440×1000 / mobile 390×844, full-page PNG before/after. 전체 이미지 높이는 콘텐츠에 따라 뷰포트보다 길 수 있다.
- 시각 흐름: 주 제목 → 설명과 `Read the briefing` → `Research summary` → R-01/R-02/R-03의 본문과 메타데이터.
- Visual Block Tree: 페이지 → masthead / hero / summary / footer. hero → 제목 / lead+action / 보조 장식. summary → 섹션 제목 / ordered records. record → 식별자 / 제목+본문 / source+date.
- 간격 역할: 기존 페이지 밀도에 맞춘 프로젝트 프로필. 주요 영역 48px, 목록·레코드 그룹 24px, 항목 내부 16px, 제목·본문 및 메타데이터 결속 8px, 미세 결속 4px. 데스크톱 비대칭 열 간격 48px. 모바일도 의미별 역할을 유지한다. 기본 160px 섹션 간격은 이 짧은 브리핑에 적용하지 않는다.
- 타이포 역할: 기존 로컬 Arial 유지. 주 제목 desktop 64px / mobile 40px, 섹션 제목 24px, 레코드 제목 20px, 본문 16px, 보조 메타데이터 14px, 식별자 12px. 값은 프로젝트 판단이며 레퍼런스에서 추출한 값이 아니다. 굵기 400/700만 사용한다.
- 모션: 새 모션을 도입하지 않는다. 참조 타이밍은 미확인 상태로 유지한다.

| 검증할 관계 | 렌더 전 expected observable |
| --- | --- |
| 주 초점 | 주 제목이 섹션·레코드 제목보다 확연히 크고, 장식은 제목보다 약하다. 본문은 16px로 유지된다. |
| 편집적 그룹 | desktop에서 넓은 주 텍스트와 작은 보조 장식 사이 비대칭 여백이 보인다. 반복 카드는 없다. |
| 메타데이터 결속 | source와 date가 페이지 양 끝으로 흩어지지 않고 각 레코드 아래 하나의 근접 그룹으로 읽힌다. |
| 모바일 번역 | 제목/설명/action/요약 순서가 유지되고 제목 줄바꿈·메타데이터 재배치가 390px 안에 들어온다. 세 레코드와 날짜가 모두 읽힌다. |
| 제품 보존·사용성 | 정확한 카피·레코드 순서·출처·날짜·footer 유지. 단일 action은 #research-summary로 이동하며 키보드 초점이 보인다. 가로 넘침 없음. |

## 실제 관찰

로컬 proof P1, 2026-09-06. 아래 네 PNG를 모두 직접 열어 관찰했다. 기존 `render.mjs`의 실제 로컬 Chrome/Playwright 렌더이며, 실행 뷰포트와 full-page 이미지 크기를 구분한다.

| 실행 뷰포트 | before / PNG 크기 | final after / PNG 크기 |
| --- | --- | --- |
| Desktop 1440×1000 | [before-desktop.png](before-desktop.png) · 1440×1059 | [after-desktop.png](after-desktop.png) · 1440×1000 |
| Mobile 390×844 | [before-mobile.png](before-mobile.png) · 390×1216 | [after-mobile.png](after-mobile.png) · 390×1300 |

| 사전 기준 | actual observed fact — before → final after | 판정 |
| --- | --- | --- |
| 주 초점 | before의 26px 주 제목은 24px 섹션 제목과 크기가 유사했다. after는 desktop 64px 두 줄, mobile 40px 세 줄로 명확한 진입점이다. 본문 16px / 레코드 제목 20px / 섹션 제목 24px는 양쪽에서 동일하다. 작은 우측 장식이 주 제목과 경쟁하지 않는다. | PASS |
| 편집적 그룹 | before는 제목·설명·장식이 같은 좌측 축에 쌓였다. after desktop은 넓은 제목 영역과 우측 180×76px 장식 사이에 빈 공간이 생겼다. 요약 제목은 좌측, 순서 있는 레코드는 우측에 놓이며 배경 박스 없이 얇은 구분선만 사용한다. | PASS |
| 메타데이터 결속 | before desktop의 source/date는 행 양 끝에 있었다. after는 세 레코드 모두 같은 줄에서 16px 간격으로 붙는다. mobile은 출처 바로 아래에 날짜를 4px 간격으로 배치해 같은 레코드로 읽힌다. | PASS |
| 모바일 번역 | 좌우 24px, 읽기 폭 342px. 주 제목 → 3줄 lead → action → 요약 → R-01/R-02/R-03 → footer 순서를 직접 확인했다. 장식은 생략되고 레코드 식별자가 제목 위로 이동한다. 본문은 2–3줄, 출처·날짜는 모두 잘림 없이 표시된다. 마지막 레코드는 스크롤 아래에 있다. | PASS |
| 제품·사용성 | DOM과 Product Truth 대조에서 제목·lead·action·3개 레코드의 카피/순서/출처/날짜·footer가 정확히 일치한다. 두 뷰포트 모두 가로 넘침 없음. Tab 초점 테두리를 [desktop](focus-desktop.png) / [mobile](focus-mobile.png) 캡처에서 직접 확인했다. Enter로 #research-summary에 도달한다. | PASS |

타이포 관찰: desktop lead 폭 534px(60ch), 짧은 요약 본문 최대 712px(80ch)로 각각 두 줄/한 줄이다. mobile 본문 폭 342px와 24.8px 행간을 유지했다. 반복 레코드의 제목·본문·메타데이터 역할이 일관되며, 식별자는 12px 보조 역할이다. h2/h3는 크기뿐 아니라 섹션 위치와 반복 여부로 구별된다. 텍스트/배경 대비는 본문 13.19:1, 보조 텍스트 6.28:1, 액션 8.67:1이다.

국소 보정: [첫 mobile 렌더](iteration-1-mobile.png)에서 `text-wrap: balance`가 ‘stronger’만 가운데 줄에 남겼다. mobile에서만 일반 줄바꿈으로 바꿔 최종 ‘Shared spaces, / stronger daily / routines.’를 확인했다. Desktop은 두 줄을 유지한다. 모바일 전체 높이는 84px 증가했으며, 제목 위계와 식별자·메타데이터의 별도 행을 위한 비용이다.

검증 경계: **Technical PASS / Product Conformance PASS / Visual Conformance PASS**는 위 두 뷰포트와 초기 정적 상태 및 단일 앵커/키보드 초점에 한한다. Desktop은 요약이 이미 화면 안에 있어 fragment만 바뀌고, mobile은 스크롤 434px 후 요약 상단이 화면의 24px에 놓인다. **새 렌더에 대한 User Acceptance는 미확인**이며, 이를 승인된 디자인의 새 revision으로 승격하지 않는다. 미제공 참조 폰트·반응형 값·모션은 여전히 UNKNOWN이다.

재현: `node render.mjs index.html artifacts/after-desktop.png 1440 1000`, `node render.mjs index.html artifacts/after-mobile.png 390 844`.

[checks.json](checks.json)에 브라우저 관측값·문구 대조·최종 HTML/CSS 및 PNG SHA-256을 기록했다. [before-hashes.json](before-hashes.json)과 비교해 Product/Design, 두 레퍼런스, renderer, 설치된 skill의 불변성을 확인했다. 변경한 구현 파일은 `index.html`(기존 R-01–03 식별자 표시)과 `styles.css`뿐이다.
