- 작업: R1-2 글자 수 표시의 DESIGN 규칙 C1·C2를 `node tools/measure.mjs`로 쟀다(4개 너비 x 빈 칸·200자, 라이트). 미리보기가 연결 CSS를 읽지 못해(`linkedCss` loaded false) 모든 측정은 `--inject src/style.css`로 같은 CSS를 주입한 화면이다. 코드는 고치지 않았다.
- 업데이트 파일: DESIGN.md (C1·C2 행의 Check·Spot check·Unmeasured·Result), ROADMAP.md (R1-2 증거 칸, 다음 작업 줄), TASK.md (2026-11-15-r1-2-check 새 항목), REPORT.md.
- 이슈: C1의 세로 4px이 무엇 사이의 거리인지 갈린다. 상자 기준으로는 4px이지만, 화면에서 사람이 보는 칸 아랫선과 글자 사이는 9px다(13px 글자의 줄 높이 여백). 결함인지 규칙 해석 문제인지는 책임자 판단이 필요하다.
- 해결: 없음
- 남은 문제: C1 세로 기준 결정 대기, 그 결정 전에는 C1을 통과로 기록하지 않음. 연결 CSS가 실제로 로드되는 화면(일반 브라우저)은 이 환경에서 관찰 못 함. 다크 모드는 승인 범위 밖이라 안 잼. 사용자 화면 확인(R1 끝) 남음. R1-2는 verification pending 유지.
- 다음 작업: 책임자 답에 따라 (a) 상자 기준이면 C1 행을 그대로 두고 spot check 기준을 상자로 고쳐 다시 대조, (b) 글자 기준이면 `.char-count` 간격 조정 후 C1·C2 전체 재측정.

상세 보고

design checks:
- C1 오른쪽 끝 | 8/8 | 4 sizes x 2 states, light (injected css) | rendered | 320x800 200자: check 0 / observed 0 (칸 테두리와 글자 잉크 모두 303열, capture)
- C1 세로 4px | 8/8 (상자 top − 칸 bottom = 4) | 4 sizes x 2 states, light (injected css) | rendered | 320x800 200자: spot check differs: check 4 / observed 9 (칸 아랫선 303행, 글자 잉크 시작 313행, capture)
- C2 가로 넘침 | 8/8 (scrollWidth = 화면 너비) | 4 sizes x 2 states, light (injected css) | rendered | 320x800 200자: check 320 ≤ 320 / observed 가장 오른쪽 잉크 303열, scrollTo(200) 뒤 scrollX 0 (capture)
- AC-002 글자 수 문구 | 3/3 (`0 / 200`, `199 / 200`, `200 / 200`) | 1~4 sizes x 3 states, light (injected css) | rendered | not spot-checked
- 연결 CSS 없이 잰 화면 | 참고용, 규칙 판정에 안 씀 (320 빈 칸: 세로 −19, 오른쪽 차 55) | 1 size x 1 state, light | rendered | not spot-checked

질문(책임자): C1의 "상자 아래 4px"은 글자 수 요소의 상자까지(지금 구현, 화면상 보이는 틈 9px)인가, 보이는 글자까지 4px인가?

report-check: ok 1,659 chars c56d8a1e
