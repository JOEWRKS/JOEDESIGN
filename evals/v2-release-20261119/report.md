# JOEDESIGN 2.0.0 후보 정리 (2026-11-19, T043)

**결론:** 2.0.0 후보를 main에 커밋 3개로 준비했다(푸시·태그·Release·설치 없음). 스킬 폴더는 1.3.4와 비교해 `VERSION` 한 파일만 다르다. node 44/44, python 142 OK(건너뜀 2), part19 회귀는 274개 R1~R6 수가 같고 R7 바뀐 파일 0이다. 위생 작업으로 무참조 docs 4개를 지우고 기록 52개를 archive로 옮겼으며, 사용자 이름이 든 홈 경로를 15개 파일에서 가렸다. 남은 38개는 테스트·기록이 해시를 고정해 그대로 두었다.

입력: [2.0 사전 조사](../v2-survey-20261119/report.md). 결과 문서: [SECURITY.md](../../SECURITY.md), [docs/QUICKSTART.md](../../docs/QUICKSTART.md), [README.md](../../README.md), [CHANGELOG 2.0.0](../../CHANGELOG.md).

## 게이트

| 항목 | 결과 |
|---|---|
| `git diff --stat v1.3.4 HEAD -- skills/joedesign` | `skills/joedesign/VERSION` 1개(`1.3.4` → `2.0.0`). 스킬 폴더 31개 파일 중 나머지 30개 바이트 동일 |
| `node --test tests/*.tests.mjs` | 44/44 통과(커밋마다 실행) |
| `python -B -m unittest discover -s tests` | 142 OK, 건너뜀 2(`JOEDESIGN_PLAYWRIGHT_MODULE` 미설정, 기준선과 같음) |
| `node evals/check-coverage-20261104/part19/regress.mjs` | 274: 1.3.3 `{"R3":269,"R5":44,"R1":75,"R6a":103,"R4":4,"R2":3,"R6b":7}`, 1.3.4 같음, R7 changed in 0 files. part18 4·part16 A 4/B 4·part14 A 16/B 16·part15-ok 42 모두 R1-R6 changed 0, R7 값은 part19 보고와 같음. 출력 파일(rule-counts-274.txt·sets.tsv·r7-changes.tsv)은 다시 써졌지만 바이트가 같아 git 변경 없음 |
| `harness_cli.py version` | `"version": "2.0.0"` |
| `git status` | 미추적 `evals/feedback-20261013/`, `evals/feedback-implementation-20261013/` 두 폴더만 |

## A. 위생

| 작업 | 수 | 비고 |
|---|---|---|
| 삭제 | 4 | `docs/superpowers/plans/2026-09-29-design-harness.md`, `plans/2026-10-06-harness-execution.md`, `specs/JOEDESIGN_DESIGN_HARNESS_V0_1_IMPLEMENTATION_HANDOFF.md`, `specs/JOEDESIGN_DESIGN_TOOL_RESEARCH_2026-09-29.md` |
| 이동 | 52 | `fixtures/contract-cases/evidence/v02-operational-validation-v1/` → `evals/archive/2026-11-19-unreferenced/v02-operational-validation-v1/`, 설명 [README](../archive/2026-11-19-unreferenced/README.md) 추가. 이동 뒤 폴더 이름 언급은 archive·조사 보고 안뿐(grep), 테스트·회귀 통과 |
| 가림 | 15 | 이동한 기록 8, RACI 초안 1(9줄), evals 6(design-conformance observed-sources.json·operational.md, handoff-visual-roles before-sha256.json, harness-v0.1 local-capabilities.json, v1-release-candidate README.md·joint-r1/summary.json). 사용자 이름이 든 홈 경로 전부 `~`로 바뀜(남은 `<user>` 0) |
| 캐시 삭제 | 3 | `skills/joedesign/scripts/__pycache__`, `scripts/harness/__pycache__`, `tests/__pycache__`(추적 안 됨) |

식별자 수(추적 파일, 대소문자 무시):

| | 전 | 후 |
|---|---|---|
| 사용자 이름이 든 파일 | 53 | 38 |
| 조사 패턴(이름·`C:` 사용자 폴더·AppData) 합집합 | 66(조사 65 + 조사 보고 자신) | 63 |

패턴 합집합이 크게 줄지 않은 이유: 가린 파일 중 여럿이 `~\\AppData\\Local\\Temp\\…`처럼 이름 없이 AppData를 담고, 조사 전에 이미 가린 13개 파일도 같은 형태다. 이름은 없다.

**그대로 둔 38개:**

- 테스트가 해시를 고정한 20개: `fixtures/contract-cases/history/astra-*/observed.json`·`review-evidence.json` 13개, `fixtures/contract-cases/evidence/astra-smoke-v1/*` 7개.
- 회귀 입력 1개: `evals/handoff-visual-roles-20261008/README.md`(files-274).
- 같은 폴더 기록이 해시를 적어 둔 17개: `evals/behavior-forward-20261010/records/*` 7개(final-artifact-manifest.json·results.json이 해시 기록), `evals/f05-impact-20261013/` 5개(completion-pins.json·managed-plan-r2.json·source-r2.json이 해시 기록), `fixtures/contract-cases/evidence/visual-translation-v02/` 5개(테스트가 읽는 폴더, review-evidence.json·fresh-review.json이 해시 기록).

## B. SECURITY.md

루트 이름을 검사하는 테스트는 없다(tests/ grep 0). 내용: 검사 항목과 결과(비밀값 0·메일 0·매니페스트 0·CI 없음, 식별자 53 → 38), 남은 것과 이유, 스크립트 신뢰 경계(report-check·capture·measure-layout·harness_cli/harness·collector), 알리는 방법. 비밀값 패턴과 매니페스트는 이번에 현재 트리만 다시 검사했다(0, 0). 이력 수치는 조사 보고 값이다.

## C. 문서

| 파일 | 전 | 후 |
|---|---|---|
| README.md | 251줄, 1,526단어, 16,859B | 145줄, 611단어, 7,477B(바이트 44%). 400자 넘는 줄 0 |
| docs/QUICKSTART.md | 없음 | 87줄 |
| docs/INSTALL.md | `1.3.4`, 1.0.0 경계·검증 링크 | `2.0.0`, 2.0.0 경계, 이 보고 링크(1.0.0 기록 링크 유지), 빠른 시작 링크 |

README: 버전 설명 두 줄(13·138행)을 한 문장 + CHANGELOG 링크로, "1.3.0"(114·237행)을 "2.0.0"으로, "Codex 기반"을 Codex·Claude Code로. `[English](#english) | [한국어](#korean)`, `## 4. 사용 방법`, VERSION·SKILL.md·conformance·execution·impact 링크 유지, QUICKSTART·SECURITY 링크 추가. 영어 절의 PowerShell 블록은 한국어 4절과 같은 명령이라 그쪽 링크로 줄였다.

Quickstart에서 확인한 것: `report-check.mjs` 표본 보고 → `report-check: ok 99 chars …` → 도장을 끝 줄로 붙인 파일 `--verify` → `stamp: match (...); text ok`, 종료 코드 0. 임시 폴더에서 junction을 만들어 `version`을 실행(대상 경로가 `operating_core`로 나옴)하고 `cmd /c rmdir`로 지운 뒤 원본 `SKILL.md`가 남는 것.

Quickstart의 남은 빈칸:

- Claude Code 연결 설치를 실제 Claude 스킬 폴더(`~/.claude/skills`)에 만들어 스킬이 발견·호출되는지는 확인하지 않았다(개인 설치 경로를 건드리지 않음). Claude Code에서의 호출 문구(`$joedesign` 대신 스킬 이름)도 확인하지 않았다.
- `doctor`·`doctor --skills-root`는 개인 스킬 폴더를 읽으므로 실행하지 않았다.
- Codex 업데이트 절차는 명령 하나로 주지 않고 단계(백업 → 삭제 → README 블록)로 적었다. 백업 해시 확인은 INSTALL.md 요청문에 맡긴다.
- macOS·Linux `ln -s` 줄은 실행하지 않았다.

## 확인된 것

- 게이트 전부(위 표). 게이트는 커밋 세 개 각각 앞에서 실행했다.
- 무참조 4개 docs·archive 폴더: 이동·삭제 뒤 테스트·회귀 통과, 이름 언급은 RACI 초안(TOOL_RESEARCH 링크 1)·조사 보고·archive README뿐.
- 커밋 전 스테이징한 추가 줄에서 사용자 이름·메일·`C:` 사용자 폴더 0건. AppData는 `~\\AppData\\…` 형태로만 있음.

## 확인되지 않은 것

- Claude Code 설치·호출, `doctor`, Playwright 경로 테스트 2개(건너뜀), 실제 Codex 실행(`harness_cli.py run`).
- 마크다운 링크가 GitHub 화면에서 렌더링되는 모습(로컬에서 경로 존재만 확인). 바꾼 문서의 상대 링크는 모두 존재하고, CHANGELOG의 옛 `skills/joedesign-harness/references/execution.md` 링크 1개는 1.3.4 때부터 끊겨 있다(고치지 않음).
- archive 안 `final/manifest.json`의 8개 해시는 가림 뒤 맞지 않는다(archive README에 기록). 다시 검증하는 스크립트는 없다.

## 세션이 대신 내린 결정

1. "고정" 판정을 preserved 357보다 넓게 잡았다: baseline-and-freeze.json의 모든 경로(362), files-274, 그리고 **같은 저장소의 다른 기록이 그 파일의 sha256을 적어 둔 경우**까지. 그래서 위탁문의 "65 중 20 + 1 외 마스킹"보다 17개를 더 남겼다.
2. 이미 이름 없이 `~`로 가린 13개 파일(longterm-G·H 분석 JSON, v1-release-candidate install-r1 로그)은 손대지 않았다.
3. archive 기록 8개는 위탁문대로 가렸고, 그 결과 내부 manifest 해시가 어긋나는 것을 README에 적었다.
4. RACI 초안은 9줄만 고쳤다. 지운 TOOL_RESEARCH 문서를 가리키는 링크 1개가 그 초안에 남아 끊어진다(위탁문 "다른 것은 고치지 않음").
5. README 영어 절의 설치 블록을 한국어 4절 링크로 대체했다(같은 명령 중복 제거, 절반 목표).
6. docs/VALIDATION.md 6·8행의 낡은 버전 문장("1.1.0 의미: 현재 지원 범위")은 범위 밖이라 고치지 않았다.
7. Quickstart 도장 단계에서 PowerShell `>>` 덧붙이기를 권하지 않았다(Windows PowerShell 5.1은 UTF-16으로 덧붙일 수 있음). 도장 줄을 손으로 끝에 붙이게 적었다.
8. 첫 위생 커밋에 README·INSTALL 수정이 함께 들어간 것을 발견해(앞선 `git add -u`), 푸시 전 로컬 커밋 두 개를 `git reset --mixed 2ace8c3`로 풀고 같은 내용을 세 묶음으로 다시 커밋했다. 공개 이력은 바뀌지 않는다.
