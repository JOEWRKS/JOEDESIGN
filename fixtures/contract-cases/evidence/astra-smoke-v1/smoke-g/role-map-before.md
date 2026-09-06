# Color / Contrast 역할맵 — 편집 전

기록 시점: before 렌더·computed style·interaction 이미지 확인 후, index.html/styles.css 편집 전.
권위: 동결된 PRODUCT.md와 Status: APPROVED인 DESIGN.md. 지시의 “APPROVED DESIGN.md”라는 별도 파일은 없으며, 실제 승인 문서는 DESIGN.md이다. 두 문서 및 helper는 수정하지 않는다.
범위: 기존 Operations Review Portal의 색상 역할, 대비, 기존 Current priority 라벨의 표시 결함. 새 방향·Product 상태·동작은 추가하지 않는다. 특정 팔레트는 승인되어 있지 않다.

## 실제 역할과 실패

D = 1440×1000, M = 390×844. 비율은 실제 computed foreground / 합성 background의 WCAG 상대휘도 계산이다. 전체 쌍과 계산식은 [before-contrast.md](before-contrast.md), 원자료·원본 파일 SHA-256은 [before-computed.json](before-computed.json).

| 역할 | 편집 전 실제 값 / 관찰 | 실패 또는 불확실성 | 한정 수정 의도 |
| --- | --- | --- | --- |
| foreground — 제목 | h1 #d400b8 / D #fafbfe, M #e3eaf4 = 4.52 / 3.86; h2 #593de0 / queue = 6.04 / 5.17; h3 #43356c / 각 row = 9.71–9.89 | 제목 대비 자체는 PASS. 마젠타·보라·녹색이 주 행동과 별도 강조점을 만듦 | 기존 body #30334a를 제목에도 재사용하여 차분한 위계 유지 |
| foreground — 보조 내용 | lead #a8adbb / body = D 2.17, M 1.85; description #a5a9b5 / 3 row = 2.13–2.17; ID #9a78d6 = 3.16–3.22; metadata #e88d25 = 2.31–2.35 | 모두 일반 텍스트 4.5 미달 | 반복 보조 foreground #586174로 통일 |
| foreground — 주변 정보 | eyebrow #19ad57 / body = D 2.84, M 2.42; count #e69131 / queue = 2.26 / 1.94; footer #adb1bc / body = 2.07 / 1.77 | 모두 4.5 미달; 정보 중요도보다 색상이 과함 | 같은 보조 foreground 적용 |
| surface — 기본·중첩 | body D #fafbfe / M #e3eaf4; queue D #edf7ef / M #dce4ef; R-01 #eff5ff, R-02 #fff0f8, R-03 #e8faf5; 각기 다른 테두리·rail | 색 자체가 실패 기준은 아님. 목록을 다색 카드로 나누어 승인된 open list 관계와 충돌. 모바일 바탕 교체는 일부 대비를 더 낮춤 | 기존 밝은 canvas #fafbfe 유지·모바일 공유; queue/row 배경과 외곽선을 투명화, 중립 구분선만 유지. 간격·폭·글꼴 유지 |
| accent — 주 행동 | #fff / #19bdd5 = 2.26; hover #fff / #f6a229 = 2.08; 외곽 border #14bba5 / body = D 2.34, M 2.00 | 텍스트 4.5 및 경계 3 미달; hover 주황이 무관한 상태색처럼 바뀜 | 주 행동 #285d8f, hover #204b73; 흰색 텍스트 유지. 이 강조 역할은 주 행동과 연결된 R-02에만 사용 |
| state — Ready | #12834d / #d1f4df = 4.05 | 12px bold이므로 4.5 필요, FAIL | 배경 유지, foreground #14633d |
| state — Needs review | #d89e22 / #fff0be = 2.09 | 4.5 미달 | 배경 유지, foreground #785514 |
| state — Blocked | #ec6666 / #ffdcdc = 2.48 | 4.5 미달 | 배경 유지, foreground #a12f36 |
| focus | 2px #a2c9ef, offset 3px; action / body D 1.67, M 1.43; R-02 / queue D 1.58, M 1.35 | 표시되지만 주변 바탕과 3 미달. 실제 Tab과 Enter로 확인 | 폭·offset 유지, focus 역할 #174f7b로 교체 |
| current-priority | R-02만 data-priority=true; #30334a / #fff0f8 = 11.23이나 Current priority는 1×1px clip; rail #f24d94 / queue D 3.06, M 2.62 | 텍스트는 숨김으로 FAIL. 다른 모든 행에도 색상 rail이 있어 우선순위가 모호함. 색 없는 의미 단서 부재 | 기존 문구를 12px bold로 표시; R-02만 accent rail, DOM의 data-priority로 스타일 적용. 상태 배지와 별개 의미 유지 |

## 편집 전에 정한 검증 관계

- 시각 흐름: 제목 → 하나의 Review priority item 행동 → 명시된 R-02 Current priority → 나머지 순서대로 목록. 제목의 크기·배치, 문서 순서와 기존 여백은 유지한다.
- D/M 실제 이미지에서 밝은 하나의 열린 목록, 읽을 수 있는 설명·메타데이터, 유일한 주 행동, 보이는 우선순위 문구를 확인한다.
- 일반 텍스트 4.5:1, 큰 글씨 3:1, 주 행동 경계·focus 3:1 이상. R-02 rail도 안/밖 바탕에서 3:1 이상으로 확인한다. 상태 배지 배경과 목록 구분선은 의미를 단독 전달하지 않으므로 장식에 3:1을 억지로 적용하지 않는다.
- 비색상 단서: Ready / Needs review / Blocked의 서로 다른 기존 텍스트; R-02의 Current priority 문구; 포커스는 새 외곽선의 출현. 주 행동 문구와 #review-r-02 이동 의미 유지.
- Tab → Enter 후 실제 R-02로 hash/focus 이동, 세 상태·유일한 priority·본문·타임스탬프·레코드 순서 보존 확인.
- before 기준 시각 결과 FAIL. after 대비·표시·겹침은 아직 UNVERIFIED이며 실제 렌더 후 판정한다. helper는 fullPage 캡처: M viewport는 390×844지만 before PNG는 전체 문서 390×985이다.
- 검증은 설치된 Chrome의 해당 두 viewport와 기본/hover/키보드 focus/anchor target focus에 한정한다. 전체 접근성 인증, 다른 브라우저·크기·테마·강제 색상·스크린리더·사용자 수락은 이 증거로 주장하지 않는다.
