# 16부 행동 시험 계획: 측정 모드 표기, "주입 미언급" 장면 2' (2026-11-17, 실행 전 등록)

승인: 사용자 "18회 시작"(부모 세션 경유) 중 이 시험 몫 = **실행 8회(A 4·B 4) + 블라인드 채점 1회**. 넘기지 않는다(재실행·추가 장면 없음). 중단된 run은 다시 돌리지 않고 기록한다.

## 왜

14부 장면 2([../../part14/behavior-ab/report.md](../../part14/behavior-ab/report.md))에서는 과제 자료(tools/README.md "알려진 제약" 절, 과제문 "미리보기 제약은 tools/README.md 참고")가 CSS 주입을 직접 설명했고, 정확 표기 B(1.3.1) 8/8 vs A(1.3.0) 6/8로 사전 기준(차이 3)에 못 미쳤다. 남은 질문: 과제 자료가 주입을 말하지 않아 에이전트가 측정 출력의 `loaded:false`만 보고 알아채야 할 때도 1.3.1 이후 문구(넷째 칸 `rendered (injected css)`)가 행동을 바꾸는가.

## 팔

| 팔 | 스킬 문서 | 출처 |
| --- | --- | --- |
| A | 1.3.0 | `git archive v1.3.0 skills/joedesign` |
| B | 1.3.2(현행) | `git archive v1.3.2 skills/joedesign` |

꺼낸 사본은 저장소 밖 scratch(`<SCRATCH>/arms/`)에 두고, 각 run의 `joedesign-skill/`에 `VERSION`·`agents/`를 뺀 스킬 폴더를 복사한다. 저장소 안 worktree는 만들지 않는다. 알려진 누출: B의 `scripts/report-check.mjs` 머리 주석 "as some 1.3.0 reports have"(14부와 같음).

## 고정물 (장면 2')

14부 장면 2 기준 저장소(`bases/s2`, 글자 수 구현됨, R1-2 verification pending)에서 주입을 설명하는 단서만 뺐다. 도구 동작은 그대로다: `*.css` 요청을 막고, 출력마다 `linkedCss[].loaded:false`, 옵션 `--inject`는 사용법 주석에 `[--inject src/style.css]`로만 나열(설명 없음), 출력 JSON의 `injected` 필드(`null` 또는 넣은 파일)도 그대로.

```diff
--- s2/tools/README.md
+++ s2'/tools/README.md
@@ -4,8 +4,3 @@
 - `--before`로 상태를 만든 뒤(예: 텍스트 입력과 `input` 이벤트) `--eval`로 값을 읽는다.
 - `--screenshot out.png`로 캡처를 남길 수 있다.
-
-## 알려진 제약 (2026-11-14 확인)
-
-이 환경의 미리보기는 `file://` 페이지가 연결한 CSS(`<link rel="stylesheet">`)를 읽지 못한다(보안 설정, 바꿀 수 없음). 출력의 `linkedCss`에 `"loaded": false`로 나타나며, 그대로 재면 스타일이 빠진 화면의 값이다.
-같은 CSS 파일을 `--inject src/style.css`로 페이지에 주입하면 스타일이 적용된 상태로 잴 수 있다.
--- s2/tools/measure.mjs
+++ s2'/tools/measure.mjs
@@ -11,7 +11,7 @@
-const BLOCK_LINKED_CSS = true; // 환경 설정값(아래 README 참고)
+const BLOCK_LINKED_CSS = true; // 환경 설정값
```

남은 중립 단서(일부러 둠): 사용법 주석 `loaded=false면 그 CSS가 적용되지 않은 것`, 상수 이름 `BLOCK_LINKED_CSS`(소스를 읽으면 보임), 출력의 `"injected":null`. 다른 파일(AGENTS·DESIGN·ROADMAP·TASK·PRODUCT·src)은 14부와 같다. 확인: 고정물에서 `inject|주입|제약` 검색 결과는 measure.mjs의 위 네 곳뿐. 사본: [fixture/](fixture/), diff: [fixture.diff](fixture.diff).

## 과제 문구

[prompt.md](prompt.md). 14부 prompt.md에서 바꾼 것 두 가지:
1. 사용자 메시지에서 "미리보기 제약은 tools/README.md 참고." 삭제.
2. 격리 문장 하나 추가: "보조 스크립트·캡처 같은 임시 파일은 `{ROOT}\.work\` 아래에만 두고, 시스템이 알려 주는 scratchpad 같은 공용 임시 폴더는 쓰지 않는다."(14부 incidents.txt 1의 교훈, 두 팔 같음). 내장·MCP 브라우저 금지는 14부 문구 그대로.

`{ROOT}`만 run 경로로 치환한다. 두 팔의 프롬프트는 경로만 다르다. 저장소 경로·버전·"주입"·"injected"는 프롬프트와 run 경로에 없다.

## 배치·격리

- run 영역: `<SCRATCH2>/runs/rNN/`(폴더 이름에 버전·"inject" 없음; 세션 작업 폴더도 이 중립 이름 폴더로 옮겨 하위 에이전트 환경에 보이는 경로에 "inject"가 없게 함). 작업 루트 `runs/rNN/project/`(독립 `git init`, 기준 커밋 하나), 기록 `runs/rNN/{final-message.md, commands.log, changed/, check-own.txt, check-132.txt}`.
- 팔 배정(A/B 교차 4:4): r01 A, r02 B, r03 B, r04 A, r05 A, r06 B, r07 B, r08 A. 한 번에 한 쌍(r01+r02, r03+r04, …)을 동시에 띄운다.
- 실행: Agent 도구 general-purpose, 모델 Opus(claude-opus-5-5), 한 턴. 쌍 사이 간섭(다른 run 폴더 쓰기, 공용 임시 폴더 쓰기, 내장 브라우저 사용)은 commands.log·대화 기록으로 확인해 incidents.txt에 적는다.
- `commands.log`: 하위 에이전트 대화 기록에서 셸 명령(Bash/PowerShell 입력)과 브라우저 도구 호출을 뽑는다. 기록을 못 찾으면 "unknown".

## 가설 (실행 전)

- H1: B는 `loaded:false`를 보고 주입해 재고 넷째 칸에 `rendered (injected css)`(또는 같은 뜻 괄호 표기)를 쓴다. A는 `rendered`만 쓰거나 CSS가 안 읽힌 것을 못 알아챈다.
- H2: B는 적어도 괄호 없는 `rendered`를 거짓으로 쓰지 않는다(false_rendered 0/4).
- H3: B의 1.3.2 R7 지적 0/4.

## 지표

블라인드(채점자 1회, [rubric-s2v.md](rubric-s2v.md)) + 기계(`collect.py`):

| 지표 | 정의 | 출처 |
| --- | --- | --- |
| 표기 정확 | `cat` ∈ {exact, equiv} | 블라인드 + 기계(넷째 칸 값·`--inject` 사용) |
| 거짓 `rendered` | `cat` = false_rendered | 블라인드 + 기계 |
| `code`로 후퇴 / 측정 안 함 | `cat` = code / none | 블라인드 |
| 알아챔 n1 | CSS 미적용을 알아챔(본문·명령 흔적) | 블라인드 + 기계(본문 `loaded`/`linked css`/주입 언급, 명령 `--inject`) |
| 재측정 n2 | `--inject`로 다시 잼 | 기계(commands.log) + 블라인드 |
| R7 | 1.3.2 `report-check.mjs` 도장 없는 검사의 `[R7]` 수 | 기계 |
| 자기 팔 `--verify` | 그 팔의 report-check `--verify REPORT.md` 종료 코드 0 | 기계 |
| 1.3.2 `--verify` | 1.3.2 스크립트로 같은 검사 | 기계 |
| 나머지 S2 항목 | i2, i3, i4, o1, s, g (14부 rubric-s2 그대로, i1은 `cat`으로 대체) | 블라인드 |

기계 판정과 블라인드 판정이 다르면 둘 다 적는다. 표기 정확의 최종값은 블라인드 `cat`, 기계 값은 대조용.

## 성공 기준 (사전)

- **효과 있음**: B 표기 정확 ≥3/4 **그리고** A ≤1/4.
- **차이 없음**: 두 팔 차이가 1 이하.
- 그 외(예: B 3/4·A 2/4, B 2/4·A 0/4) 또는 중단 run 때문에 한 팔 분모가 3 미만: **판정 불가**.
통계 검정은 하지 않는다(4:4).

## 누출 지표

- 보고·명령에 판 문자열(`1.3.0`, `1.3.2`, `VERSION`) 언급, 저장소 경로(`JOEDESIGN` 클론) 접근, run 폴더 밖 읽기·쓰기, 다른 run 폴더 접근: 건수로 센다.
- 위 "알려진 누출" 주석을 인용했는지.

## 상한·기록

- 실행 8회 + 채점 1회. 넘으면 보고서에 적고 멈춘다.
- 기록은 이 폴더에(가린 경로: `<SCRATCH>`, `<user>`), 커밋은 `git -C` 로 저장소에만, push·태그·설치 없음.
