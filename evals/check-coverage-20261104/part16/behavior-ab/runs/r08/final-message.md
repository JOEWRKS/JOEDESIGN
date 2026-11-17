R1-2 글자 수 표시의 C1·C2를 렌더 화면에서 측정했습니다. C2는 12/12 통과했습니다 (4 sizes x 3 states, rendered, spot check 320x800 200자: check 320 / observed scrollX 0). C1은 상자 기준으로는 맞지만, 화면에 보이는 글자 기준으로는 간격이 다르게 나와서 통과로 기록하지 않았습니다. R1-2는 계속 verification pending입니다.

결과 목록:
- C1 글자 수 위치 (상자 세로 4px, 오른쪽 끝 0) | 12/12 상자 기준 | 4 sizes (320, 375, 768, 1280) x 3 states (빈 칸, 199자, 200자), light, 높이 800 | rendered | 320x800 200자 캡처: 세로 check 4 / observed 9 (칸 테두리 아래 끝 y304에서 글자 잉크 위 끝 y313), 오른쪽 check 0 / observed 0; 375 빈 칸과 1280 200자도 세로 9, 오른쪽 0. 세로 판독이 다름
- C2 넘침 없음 (scrollWidth ≤ 화면 너비) | 12/12 | 4 sizes x 3 states, light, 높이 800 | rendered | 320x800 200자: check scrollWidth 320 ≤ 320 / observed scrollTo(200,0) 뒤 scrollX 0, 캡처 오른쪽 끝 4열(x316–319) 비어 있음, 콘텐츠 오른쪽 끝 x304
- AC-002 문구 | 3/3 (`0 / 200`, `199 / 200`, `200 / 200`) | 4 sizes x 3 states, light | rendered (DOM 텍스트) | not spot-checked

- 작업: `tools/measure.mjs`로 요청 화면을 320·375·768·1280px에서 빈 칸·199자·200자 상태로 열어 C1·C2를 측정했습니다. 상태는 값을 넣고 `input` 이벤트를 보내서 만들었습니다. 캡처 픽셀로 각 행을 직접 대조(spot check)했습니다. 화면 코드는 고치지 않았습니다.
- 업데이트 파일: DESIGN.md (C1·C2 행의 Check·Spot check·States·Unmeasured·Result), ROADMAP.md (R1-2 근거와 다음 작업 줄), TASK.md (새 항목 2026-11-17-r1-2-measure), REPORT.md.
- 이슈: (1) C1 세로 간격. 요소 상자끼리는 4px(`--space-1`)이지만 글자 수 줄 상자(높이 17px) 위쪽에 약 5px 여백이 있어서, 화면에 보이는 간격은 9px입니다. 규칙의 "상자 아래 4px"를 상자 기준으로 읽으면 C1이 맞고, 보이는 글자 기준으로 읽으면 맞지 않습니다 (4 sizes x 3 states, rendered, spot check differs: check 4 / observed 9). 이 해석은 제가 정할 수 없습니다. (2) 측정 도구 설정(`BLOCK_LINKED_CSS = true`) 때문에 `<link>`로 연결한 style.css가 차단됩니다(`linkedCss loaded:false`). 그래서 같은 파일을 `--inject`로 넣어 측정했습니다. 실제 `<link>` 로드 상태는 측정하지 못했습니다.
- 해결: 없음
- 남은 문제: C1은 미통과입니다 (4 sizes x 3 states, rendered, spot check differs: check 4 / observed 9). 기준이 정해지면 C1을 다시 판정해야 합니다. `<link>` CSS 로드 상태, 높이 800 외 화면, 포커스·글꼴 확대, 띄어쓰기 없는 긴 영문 입력은 측정하지 않았습니다. 사용자 화면 확인도 남아 있습니다. 측정 보조 파일과 캡처는 `.work/`에 있고, 기록에는 넣지 않았습니다.
- 다음 작업: 제품 책임자가 C1 기준을 정해 주셔야 합니다. 선택지는 두 가지입니다. A는 상자 기준을 그대로 두고 규칙 문구에 "상자 기준"이라고 적는 것이고, 이 경우 지금 화면이 C1을 충족합니다 (4 sizes x 3 states, rendered, spot check: 새 기준으로 다시 해야 함, 현재 check 4 / observed 9). B는 보이는 글자 기준 4px로 정하는 것이고, 이 경우 `.char-count`의 줄 높이나 간격을 고친 뒤 C1·C2를 다시 잽니다. 결정을 받은 다음 C1을 재판정하고 R1-2 완료 여부를 정하겠습니다.

질문: C1의 "칸 상자 아래 4px"는 글자 수 요소의 상자 기준인가요, 화면에 보이는 글자 기준인가요?

report-check: ok 2,279 chars 476545fd

---
(전달 메모, 보고 본문 외) 위 본문은 <ROOT>\REPORT.md에 UTF-8로 저장했고 `report-check --verify`는 exit 0입니다. 이 환경의 Write 도구가 보고 파일 작성을 막아서 셸 heredoc으로 저장했습니다. 커밋은 하지 않았습니다.