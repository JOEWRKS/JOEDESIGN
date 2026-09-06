# Operations Review Portal — Color / Contrast correction proof

승인된 PRODUCT.md / DESIGN.md의 차분한 운영 화면·단일 주 행동·찾을 수 있는 현재 우선순위·열린 목록 관계 안에서 수정했다. 구현 변경은 styles.css뿐이다. 편집 전에 [역할맵](role-map-before.md)을 작성했다. 새 디자인 권위나 사용자 수락으로 승격하지 않았다.

## 실제 렌더 증거

설치된 Playwright + Chrome 152.0.7977.76, file:// 로컬 문서, deviceScaleFactor 1, light 색상 모드. supplied render.mjs를 그대로 사용했다. 아래 4장 및 상태 시트 4장의 실제 픽셀을 열어 관찰했다.

| viewport | Before | After | 관찰 |
| --- | --- | --- | --- |
| Desktop 1440×1000 | [before](before-desktop.png) | [after](after-desktop.png) | 제목·행·본문 위치와 줄바꿈 유지. 다색 패널이 사라진 열린 목록. 어두운 주 행동이 하나이고 R-02에만 강조 rail과 Current priority 문구가 보인다. 세 상태 배지를 읽을 수 있다. |
| Mobile 390×844 | [before](before-mobile.png) | [after](after-mobile.png) | 기존 제목 2줄·설명 줄바꿈·세로 metadata 유지. R-02 ID, Current priority, Needs review가 한 줄에 겹침 없이 보인다. R-03과 footer까지 전체 문서에서 확인. |

helper의 fullPage=true로 desktop PNG는 1440×1000, mobile PNG는 before/after 모두 390×985이다. 모바일 첫 viewport는 390×844이고 나머지 내용은 아래로 스크롤한다. 전체 내용이 첫 viewport 안에 들어간다는 주장은 하지 않는다. 두 크기 모두 horizontalOverflow=false.

실제 hover, Tab focus, Enter 후 R-02 focus 캡처를 크기 변경 없이 묶은 증거: [before desktop](before-states-desktop.png), [before mobile](before-states-mobile.png), [after desktop](after-states-desktop.png), [after mobile](after-states-mobile.png). 시트의 흰색 여백·설명은 증거용이며 UI가 아니다. before의 옅은 focus가 after에서는 바탕과 구별되는 완전한 외곽선으로 보이고 잘리지 않는다. hover에서도 주 행동의 흰색 문구가 읽히며 같은 파란 계열을 유지한다.

## 실제 foreground / background와 계산

전체 35쌍 × 2 viewport의 선택자·상태·배경·기준·비율: [before 계산](before-contrast.md), [after 계산](after-contrast.md). computed style, 글자 크기·굵기, 좌표, 실제 동작 및 SHA-256: [before 원자료](before-computed.json), [after 원자료](after-computed.json).

| 역할 | After foreground / 실제 background | After 비율 | Before 대표 비율 |
| --- | --- | ---: | ---: |
| 제목 / 열린 목록 바탕 | #30334a / #fafbfe | 11.95 | h1 D 4.52, M 3.86 (대비는 기존에도 통과) |
| 설명·ID·metadata·count·eyebrow·footer | #586174 / #fafbfe | 6.01 | lead D 2.17, M 1.85 |
| 주 행동 문구 | #ffffff / #285d8f | 6.88 | 2.26 |
| 주 행동 hover 문구 | #ffffff / #204b73 | 9.07 | 2.08 |
| 주 행동 fill·border / 바깥 바탕 | #285d8f / #fafbfe | 6.65 | border D 2.34, M 2.00 |
| 주 행동 hover fill·border / 바깥 바탕 | #204b73 / #fafbfe | 8.77 | border D 2.34, M 2.00 |
| Ready | #14633d / #d1f4df | 6.15 | 4.05 |
| Needs review | #785514 / #fff0be | 5.94 | 2.09 |
| Blocked | #a12f36 / #ffdcdc | 5.55 | 2.48 |
| Current priority 문구·보조 rail | #285d8f / #fafbfe | 6.65 | 문구는 11.23이나 1×1 clip으로 숨겨짐; rail M 2.62 |
| action / R-02 focus 외곽선 | #174f7b / #fafbfe | 8.31 | D 1.67 / 1.58, M 1.43 / 1.35 |

계산: sRGB 채널을 0–1로 정규화하고 c ≤ 0.04045이면 c/12.92, 아니면 ((c+0.055)/1.055)^2.4로 선형화한다. L = 0.2126R + 0.7152G + 0.0722B; 대비 = (밝은 L+0.05)/(어두운 L+0.05).
예: #ffffff의 L=1, #285d8f의 L=0.102629879 → 1.05/0.152629879 = 6.879… → 6.88:1. #586174의 L=0.118850496, #fafbfe의 L=0.964741111 → 1.014741111/0.168850496 = 6.009… → 6.01:1. 반올림 전 값으로 판정한다.

투명 queue/row의 실제 합성 바탕은 두 크기 모두 #fafbfe이며, 상태 배지의 실제 배경은 기존 3색 그대로다. 불투명 단색이므로 이미지·그라디언트의 위치별 대비 불확실성은 없다. focus는 2px outline과 3px offset을 유지해 안팎 인접 바탕 모두 #fafbfe다. rail도 안팎에서 확인했다.

## 비색상 단서와 변경 한계

- Ready / Needs review / Blocked라는 기존 텍스트가 상태를 직접 구별한다. 세 배지의 공통 모양은 서로 다른 상태를 구별하는 단서로 주장하지 않는다. 색상은 보조 표현이다.
- Current priority는 기존 DOM 문구를 12px/700으로 표시한 것이다. clip-path가 none이고 실제 크기는 약 88×15.59px이며 R-02에만 존재한다. rail은 추가 단서이고 상태를 뜻하지 않는다.
- focus는 새로운 외곽선의 출현으로도 구별된다. Review priority item이라는 문구, 화살표, 링크 대상은 유지했다.
- 기존 body foreground를 제목에 재사용하고, 보조 텍스트·주 행동·focus에 반복 역할을 부여했다. 제목은 원래도 대비를 통과했지만 마젠타·보라 강조의 경쟁을 줄이는 수정이 승인된 차분한 위계를 회복한다.
- 다색 행 바탕/외곽선을 투명화하고 장식 구분선 #d6dbe5를 남겼다. 구분선과 상태 배지 배경은 의미·컨트롤을 단독 식별하지 않아 그 자체에 3:1 통과를 주장하지 않는다.
- 색 외 변경은 기존 priority 라벨 숨김 해제·해당 라벨의 글자 스타일·표시 공간을 위한 record-top flex-wrap뿐이다. 기본 글꼴·타이포 크기·행 순서·간격·폭·테두리 두께는 유지했다. 측정된 기존 base 텍스트/행동 좌표와 크기는 priority 라벨을 제외하고 before/after 모두 동일했다.

## 판정과 정확한 검증 경계

| 구분 | 기대 → 실제 관찰 | 판정 |
| --- | --- | --- |
| Technical | 두 크기 로컬 렌더와 style 측정 완료; 가로 넘침 없음. 파일 SHA-256 비교에서 styles.css만 변경; PRODUCT.md, DESIGN.md, AGENTS.md, render.mjs, index.html 동일 | PASS — 이 범위 |
| Product conformance | 원래 본문·레코드 순서·제목·설명·source·UTC timestamp·세 상태·R-02 단독 priority가 before/after 동일. Tab으로 주 행동 focus, Enter로 hash #review-r-02 및 activeId review-r-02; 상태 불변 | PASS — 기존 Product 보존 및 관찰한 이동 |
| Visual / contrast | D/M 실제 이미지에서 차분한 열린 목록, 단일 행동, 명시적 R-02, 읽을 수 있는 상태·보조 내용, 겹침 없는 표시. 일반 글씨 ≥4.5, 큰 글씨 ≥3, 측정된 의미 있는 경계·focus ≥3. after 70개 측정 모두 통과, 텍스트 최소 5.5533 | PASS — 지정 viewport와 관찰 상태 |
| User acceptance | 이 수정 결과에 대한 사용자 수락은 아직 없음 | 미수락; 기술·시각 PASS와 별도 |

검증 경계는 Chrome의 Desktop 1440×1000 / Mobile 390×844에서 base, pointer hover, keyboard focus, Enter 후 anchor target focus이다. 모바일은 지정 폭의 브라우저 viewport이며 실제 휴대폰 터치 환경 검증이 아니다. 다른 viewport/브라우저, 강제 색상, dark theme, 확대, 스크린리더, 동시 hover+focus 등 미관찰 조합과 전체 WCAG 인증은 UNVERIFIED / 범위 밖이다. 해당 범위 내 미해결 FAIL 또는 필요한 UNVERIFIED는 없다.

재현: `node render.mjs index.html artifacts/after-desktop.png 1440 1000`, `node render.mjs index.html artifacts/after-mobile.png 390 844`, `node artifacts/audit.mjs after`. before는 수정 전 보존 증거이며 현재 소스로 다시 생성하지 않는다. 설치·외부 요청·이미지 자산 추가는 하지 않았다.
