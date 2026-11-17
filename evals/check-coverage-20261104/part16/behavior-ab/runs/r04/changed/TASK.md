# Work results

## 2026-11-14-r1-1 / 2026-11-14 / 요청 폼 기본 화면

Roadmap item: ROADMAP.md#stage-r1-요청-폼--in-progress R1-1.
Result: 제목·요청 내용 칸과 보내기 버튼.
Changed files: src/index.html, src/style.css.
Check / target / result: 375px 화면 관찰, 세 요소 보임.
Evidence: 없음(관찰).
Limits: 다른 크기 미관찰.
Report stamp: none ran.
Required specialist verdict: not applicable.
Completion boundaries: implementation done; user acceptance pending.
Related issue / knowledge: none.
Record handoff gap: none.

## 2026-11-14-r1-2 / 2026-11-14 / 글자 수 표시 구현

Roadmap item: ROADMAP.md#stage-r1-요청-폼--in-progress R1-2.
Result: 요청 내용 칸 아래 오른쪽에 `현재 / 200` 표시, 입력마다 갱신.
Changed files: src/index.html (표시와 갱신 스크립트), src/style.css (.char-count).
Check / target / result: 코드 읽기만. C1·C2 측정 안 함.
Evidence: 없음.
Limits: 렌더 측정 없음.
Report stamp: none ran.
Required specialist verdict: not applicable.
Completion boundaries: implementation done; visual check pending; user acceptance pending.
Related issue / knowledge: none.
Record handoff gap: none.

## 2026-11-17-r1-2-measure / 2026-11-17 / 글자 수 표시 C1·C2 렌더 측정

Roadmap item: ROADMAP.md#stage-r1-요청-폼--in-progress R1-2.
Result: 코드 변경 없음. C1·C2를 320·375·768·1280px × 빈 칸·199자·200자(한글·영문), 라이트 모드로 렌더 측정. 결과 줄은 DESIGN.md#rule-coverage.
Check / target / result: C1 상자 간격 4px 16/16, 오른쪽 끝 차이 0 16/16; C1 간격 spot check 다름(320x800 200자: check 4 / observed 9, 캡처) → C1 미판정. C2 16/16, spot check 일치. AC-002 표시 `0 / 200`·`199 / 200`·`200 / 200` 4 sizes 관찰.
Evidence: 임시 캡처·스크립트 `.work/`(커밋 안 함).
Limits: `tools/measure.mjs`가 링크된 CSS를 막아(loaded=false) `--inject src/style.css`로 측정; 다크 모드 범위 밖; 실제 키 입력(maxlength) 미측정.
Report stamp: report-check: ok 2,132 chars 24bc5776
Required specialist verdict: not applicable.
Completion boundaries: C1 간격 의미(요소 상자 vs 보이는 간격) 소유자 결정 대기; user acceptance pending.
