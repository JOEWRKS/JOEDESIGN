R1-2 글자 수 표시 C1·C2 측정

- 작업: R1-2 글자 수 표시를 DESIGN C1·C2 규칙으로 렌더 측정(320·375·768·1280px × 빈 칸·199자·200자, 라이트). 코드는 고치지 않음.
- 업데이트 파일: DESIGN.md(C1·C2 행의 Check·Spot check·Unmeasured·Result), ROADMAP.md(R1-2 근거, 다음 작업 줄), TASK.md(2026-11-17-r1-2-measure 새 항목), REPORT.md.
- 이슈: C1 간격이 상자 기준으로는 4px이지만 화면에 보이는 글자까지는 9px로, 규칙의 "4px"가 어느 쪽인지 정해지지 않음. 측정 도구가 페이지의 링크 CSS를 막아 `src/style.css`를 주입해서만 렌더함.
- 해결: 없음.
- 남은 문제: C1 간격 기준 소유자 판단 대기(C1은 not passed 유지), 페이지가 자체 CSS를 불러온 렌더는 확인 못 함, R1-2는 verification pending 유지, R1 사용자 화면 확인 대기.
- 다음 작업: 아래 질문에 대한 답을 받아 C1 행 확정(상자 기준이면 C1 행을 통과로 기록, 보이는 글자 기준이면 `.char-count` 간격 수정 후 재측정), 자체 CSS 로드 렌더 수단 확보.

design check results:
- C1 gap (칸 상자 bottom → 글자 수 상자 top = 4px) | 12/12 | 4 sizes x 3 states, light | rendered (injected css) | 320x700 200자: check 4 / observed 9 (캡처에서 칸 테두리 마지막 줄 y303, 글자 잉크 첫 줄 y313)
- C1 right edge (글자 수 오른쪽 끝 = 칸 오른쪽 끝) | 12/12 | 4 sizes x 3 states, light | rendered (injected css) | 320x700 200자: check 0 / observed 0 (잉크 오른쪽 x303 = 칸 테두리 x303)
- C2 overflow (scrollWidth ≤ 화면 너비) | 12/12 | 4 sizes x 3 states, light | rendered (injected css) | 320x700 200자: check 320 ≤ 320 / observed scrollTo(200,0) 후 scrollX 0, 캡처 x305–319 전 높이 비어 있음
- AC-002 표시 문구 (`0 / 200`, `199 / 200`, `200 / 200`) | 12/12 | 4 sizes x 3 states, light | rendered (injected css) | 320x700 200자: check `200 / 200` / observed 캡처의 `200 / 200`

상세 보고

C2는 통과(4 sizes x 3 states, rendered (injected css), spot check 320x700 200자 check 320 ≤ 320 / observed scrollX 0)로 기록했습니다. C1 오른쪽 끝 맞춤도 같은 범위에서 맞습니다(4 sizes x 3 states, rendered (injected css), spot check check 0 / observed 0).

C1 간격은 통과로 기록하지 않았습니다. 상자끼리 잰 값은 모든 크기·상태에서 4px(`.field`의 `gap: var(--space-1)`)인데, 캡처에서 사람이 보는 간격(칸 테두리에서 숫자 글자 윗부분까지)은 9px입니다. 차이 5px는 13px 글자의 줄 높이 안쪽 여백입니다. JOEDESIGN 규칙상 check와 직접 관찰이 다르면 그 행은 결과로 셀 수 없으므로, DESIGN.md C1 행은 not passed로 두었습니다.

측정 방식: `tools/measure.mjs`가 링크 CSS를 차단하는 설정이라(linkedCss loaded=false) 모든 측정은 같은 `src/style.css`를 주입해 렌더한 결과입니다. 페이지가 스스로 CSS를 불러왔을 때의 렌더는 관찰하지 않았습니다. 다크 모드와 사용자가 칸 크기를 바꾼 뒤의 상태도 측정 범위 밖입니다.

질문(소유자 판단 필요): C1의 "칸 상자 아래 4px"는 (가) 글자 수 요소의 상자까지 4px(현재 구현, 보이는 간격 9px)인가요, (나) 화면에 보이는 숫자 글자까지 4px인가요? (가)라면 C1 행을 통과로 기록하고, (나)라면 `.char-count` 간격을 고친 뒤 다시 재겠습니다.

report-check: ok 2,227 chars 973052a1