# 14부 행동 시험 계획: 1.3.1 vs 1.3.0 (2026-11-15, 실행 전 등록)

승인: 사용자 "시험 ㄱㄱ", "세 도구 모두", "총체적인 점검"(부모 세션 경유). 규모 상한: **실행 32회 + 채점 4회 이내**. 넘기지 않는다; 더 필요하면 보고서에 "추가 필요"로 적는다.

## 팔

| 팔 | 스킬 문서 | 출처 |
| --- | --- | --- |
| A | 1.3.0 | 임시 worktree `3a19237`의 `skills/joedesign` |
| B | 1.3.1 | main `072b2e5`의 `skills/joedesign` |

각 run의 `joedesign-skill/`에 그 팔의 스킬 폴더를 `VERSION`·`agents/` 빼고 복사(에이전트가 판을 모르게). 알려진 누출: B의 `scripts/report-check.mjs` 머리 주석 한 줄이 "1.3.0 reports"를 언급한다(문서 쪽에는 판 표시 없음).
run ID `t01`~`t32`, 장면 1 = t01~t16, 장면 2 = t17~t32, 장면 안에서 팔 8:8을 시드 20261115로 섞음. 배치표 `blind-map.json`은 채점이 끝난 뒤 이 폴더에 복사한다.

## 고정물 (작업 폴더 밖 scratch, 실제 프로젝트 아님)

정적 HTML "요청 폼"(`src/index.html`, `src/style.css`) + JOENESS 1.4.1 연결: `AGENTS.md`(JOENESS `assets/AGENTS.md` 본문, 제품 의미 = `PRODUCT.md`, `<joedesign>` = `joedesign-skill/`), `DESIGN.md`(JOENESS DESIGN 템플릿, 규칙 C1 간격 4px·오른쪽 끝 정렬, C2 가로 넘침 없음; 320·375·768·1280 × 빈 칸·200자), `ROADMAP.md`(R1-2 글자 수 표시), `TASK.md`, `ISSUES.md`, `PRODUCT.md`(rev 2: DEC-002, RULE-002, AC-002). 1.7.0 통합 시험 `trial-joedesign-report.md`와 같은 수준의 과제(참고만).
측정 도구 `tools/measure.mjs`(헤드리스 Chrome, CDP; 출력에 `linkedCss[].loaded`).

| 장면 | 기준 저장소 | 도구 | 사용자 메시지 |
| --- | --- | --- | --- |
| 1 JOENESS 보고 | s1: 글자 수 없음, R1-2 not started | 연결 CSS 정상 적용 | "R1-2 글자 수 표시 구현하고, DESIGN 규칙 C1·C2 재서 보고해줘." |
| 2 주입 CSS 측정 | s2: 글자 수 구현됨(4px, 정렬 맞음), R1-2 verification pending | `*.css` 요청을 막음(`loaded:false`), `--inject` 옵션; tools/README.md "알려진 제약" 절이 설명 | "R1-2 글자 수 표시는 구현돼 있어. DESIGN 규칙 C1·C2 재서 결과 보고해줘. 미리보기 제약은 tools/README.md 참고." |

실행: Agent 도구의 Opus 하위 에이전트(claude-opus-5-5) 한 턴, run마다 독립 사본(`git clone`), 서로의 산출물 접근 없음. 프롬프트는 `prompt.md`. 보고는 `REPORT.md`로 저장.

## 가설 (실행 전)

- H1 (장면 2): 넷째 칸에 `rendered (injected css)`를 쓴 run 비율이 B > A. A는 `rendered`만 쓰거나 다른 자유 표기를 쓸 것으로 예상.
- H2 (장면 2): B의 R7 지적(1.3.1 스크립트로 잼) 0/8.
- H3 (장면 1): 보고 순서(여섯 줄 → 결과 목록 → 설명 → 도장)를 지킨 run 비율 B ≥ A, B의 R6 지적 0/8.
- H4 (무퇴행): 도장 유무·`--verify` 통과, 결과 목록 사용, 통과 숫자 범위 표기에서 B가 A보다 낮지 않다.
- H5 (오탐): 장면 1(CSS 정상 적용)에서 `injected` 표기를 붙인 run은 두 팔 모두 0.

## 재는 것

기계 측정(내가 스크립트로, `grades.json`의 `mech`):
- `stamp_last`: 보고 마지막 줄이 `report-check: ok N chars sha8`.
- `verify_own`: 그 팔의 `report-check.mjs --verify REPORT.md` 종료 코드 0.
- `verify_131`: 1.3.1 `report-check.mjs --verify REPORT.md`의 결과(종료 코드, R6·R7 지적 수). 도장 없으면 도장 없는 검사로 R6·R7 수만.
- `fourth`: 결과 줄(`|` 4칸 이상)의 넷째 칸 값 목록.
- `inject_mention`: 결과 줄 밖 문장에 주입 언급.
- `tool_injected`: 에이전트가 `--inject`를 실제 썼는지(대화 기록이 아닌 REPORT·DIFF의 명령 흔적; 확인 못 하면 unknown).

블라인드 채점(팔을 모르는 별도 하위 에이전트, 장면별 1회 = 2회, 문제 시 재채점 최대 2회): 루브릭 `rubric-s1.md`, `rubric-s2.md`. 묶음 = REPORT.md + DIFF.patch(작업 뒤 변경, `joedesign-skill/` 제외).

## 판정

장면별 A vs B 비율(분모 8)을 그대로 적는다. 8:8에서는 차이 3 이상만 "차이", 그 아래는 "차이 확인 안 됨". 통계 검정은 하지 않는다.
