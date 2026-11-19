# JOEDESIGN 2.0 사전 조사 (읽기 전용, 2026-11-19)

기준: main `ba31c18`, 추적 파일 2,657개, `skills/joedesign` 트리 해시 `928b5b900e326afc62d4694616452f9e4155e082`.
테스트 기준선(이 조사 중 실행): node `--test tests/*.tests.mjs` 44/44 통과, python `-B -m unittest discover -s tests` 142 OK(건너뜀 2, Playwright 환경 변수 없음).
표기: 홈 경로 `~`, Windows 사용자 이름 `<user>`, 메일 `<email>`.

## 결론

1. 스킬 폴더는 자기 안에서 닫혀 있다: SKILL.md·templates·references·script 머리말이 README·docs·evals를 하나도 가리키지 않는다. 다만 `VERSION`이 스킬 폴더 안에 있어 "2.0.0"으로 올리면 "스킬 폴더 해시가 1.x와 같다"는 게시 조건과 부딪힌다. 둘 중 하나를 먼저 정해야 한다.
2. 위생 작업의 함정은 테스트다. node 테스트가 docs 17개와 fixtures 340개(합 357개)의 해시를 고정하고, 회귀 스크립트는 `files-274.txt`의 상대 경로(evals 하위 19개 폴더)와 `../../../skills/...` 깊이, git 태그 v1.3.2·v1.3.3에 묶여 있다. evals를 그대로 옮기면 깨진다.
3. 제거 후보는 5건이다(파일 4개와 폴더 1개, 합 56파일·약 18.9MB). 그 밖에 조건부 1건, 무시 목록에 든 캐시 3곳이 있다. 이 가운데 18.8MB는 아무도 참조하지 않는 `fixtures/.../v02-operational-validation-v1`이다. 바이트가 같은 중복 135묶음은 git이 blob을 한 번만 저장하므로 지워도 이득이 없다.
4. 보안: 비밀값 패턴은 현재 트리·전체 이력 모두 0건, `<email>`도 0건, CI·의존성 매니페스트는 없다. 개인 식별자(`<user>`, `C:/Users`, `C:\\Users`, AppData)는 현재 트리 65개 파일에 남아 있다. 이 중 20개는 테스트가 해시를 고정한 파일이라 가리기(마스킹)를 하면 테스트가 깨진다. 이력에서는 68개 경로에 남아 있다.
5. 사용 문서: README는 251줄, 1,526단어다. 버전 설명 두 줄(13·138행)이 각각 약 2,000자이고, "1.3.0" 표기가 낡았다(114·237행). Claude Code 설치, `report-check.mjs`·`--verify`, 업데이트 명령은 사람이 읽는 문서에 없다.

## 1. 목록

### 1-a. 실행 중 에이전트가 읽는 것 (31개, 전부 `skills/joedesign/`)

| 묶음 | 파일 | 크기(B) |
|---|---|---|
| 진입 | SKILL.md, VERSION(`1.3.4`), agents/openai.yaml | 14,766 · 6 · 288 |
| references | conformance.md, execution.md, impact.md, operation.md, visual-production.md, visual-translation.md | 14,324 · 13,467 · 4,243 · 21,375 · 9,377 · 8,647 |
| templates | DESIGN.md, CRITIQUE.md, DESIGN_CONTRACT.md, DESIGN_INTENT.json, EVIDENCE_MANIFEST.json, REFERENCE_CANDIDATES.json, REFERENCE_LOCK.md, STATE_MATRIX.md | 5,943 외 7개(각 1KB 미만) |
| scripts | report-check.mjs, capture.mjs, measure-layout.mjs, harness_cli.py, harness/ 10개(.py) | 28,106 · 6,591 · 2,732 · 9,530 · 합 138,105 |

저장소 밖에서 실행 중 읽는 것: JOEFLOW의 `scripts/approval_status.py`와 프로젝트의 `product-definition/<slug>/state.json`·`MASTER_PLANNING_SPEC.md`(SKILL.md 50–53행), 대상 프로젝트 루트의 `AGENTS.md`(runner.py 120행), 전문 스킬 탐색 경로인 패키지 형제 폴더·`~/.codex/skills`·`~/.agents/skills`(execution.py 59–60행). 저장소 최상위 파일 가운데 스킬이 읽는 것은 없다.

### 1-b. 사람이 읽는 것

| 파일 | 줄/크기 | 비고 |
|---|---|---|
| README.md | 251줄, 16,859B | 영어 + 한국어 |
| CHANGELOG.md | 443줄, 47,467B | evals 경로 33개 참조 |
| AGENTS.md | 260줄, 25,223B | 이 저장소에서 일하는 에이전트용 지시. evals 경로 8개 참조 |
| docs/INSTALL.md, docs/VALIDATION.md | 91줄, 43줄 | evals 경로를 각각 3개, 12개 참조 |
| docs/architecture·decisions·handoffs·proposals·roadmaps·specs | 18개 | 과거 v0.1/v0.2 설계 |
| docs/superpowers/plans·specs | 8개, 174,847B | 오래된 초안 |
| evals/.../part13~19 release-notes-v1.3.x.md | 5개 | Release 본문 원본 |
| .gitignore, .gitattributes | 각 4줄, 7줄 | 아래 1-f |

### 1-c. 테스트와 테스트가 읽는 것

| 테스트 | 읽는 것 |
|---|---|
| tests/report-check.tests.mjs | `skills/joedesign/scripts/report-check.mjs`를 import |
| tests/joedesign-v02.tests.mjs | `fixtures/contract-cases/evidence/visual-translation-v02/baseline-and-freeze.json`. 여기 적힌 **preserved 357개** 해시를 비교한다(docs 17개: specs v0.1 8, handoffs 5, decisions 1, superpowers/plans/2026-09-06-* 3 / fixtures 340개: astra-smoke-v1 310, history 27, decisions·observed·review-evidence.json). 그 밖에 frozen 2개(visual-translation-v02/inputs·expectations.json), fresh-review.json의 artifacts, `fixtures/package-history/pre-unification-20261009`(27개) |
| tests/test_harness_package.py | `fixtures/package-history/pre-unification-20261009`, `evals/harness-v0.1/baseline-package.json`, `skills/joedesign` 복사본 |
| tests/test_*.py 나머지 12개와 harness_support.py | `skills/joedesign/scripts`(임시 폴더에서 실행, 저장소 파일은 읽지 않음) |

회귀 스크립트(테스트 밖, CHANGELOG·AGENTS가 결과를 인용):

| 스크립트 | 여는 파일 |
|---|---|
| part15/regress.mjs | `../../../skills/joedesign/scripts/report-check.mjs`, `part14/regression/files-274.txt`의 274개, `part14/regression/verify-stamped-1.3.1.tsv`. 결과를 자기 폴더에 씀 |
| part17/regress.mjs | 위와 같음, 그리고 `git show v1.3.2:...report-check.mjs`, part14·16의 `behavior-ab/blind-map.json`, `part15/verify-stamped-1.3.2.tsv` |
| part19/regress.mjs | 위와 같음, 그리고 `git show v1.3.3:...`, part14·16·18의 blind-map.json |
| part15/run-ab.mjs, part19/counterfactual.py | 자기 폴더의 blind-map·grades·runs, report-check.mjs |

`files-274.txt`의 274개는 모두 존재한다. 그 분포는 cc/part13 128, cc/spot-check 38, cc/longterm-G 34, cc/longterm 26, cc/part11 12, cc/longterm-H 11, cc/part12 10, cc/report-scope 3, cc/README 1, cc/unprompted 1, 그리고 다른 evals 9개 폴더의 README류 9개다(cc = `evals/check-coverage-20261104`).

### 1-d. 기록(evals)

| evals 최상위 | 파일 | 크기(B) |
|---|---|---|
| check-coverage-20261104 | 1,884 | 8,540,305 |
| behavior-forward-20261010 | 40 | 2,646,935 |
| f05-impact-20261013 | 62 | 456,323 |
| design-conformance-20261010 | 32 | 367,627 |
| v1-release-candidate-20261013 | 62 | 269,226 |
| handoff-visual-roles-20261008 | 11 | 71,429 |
| main-integration-20261010 | 4 | 50,350 |
| harness-v0.1 | 13 | 41,882 |
| harness-bottleneck-20261006 / harness-execution-20261006 | 2 / 2 | 40,258 / 30,270 |
| unified-core-20261009 / design-workflow-20261009 | 5 / 5 | 34,070 / 30,256 |
| v1-personal-install-20261013 / quality-repair-v1 | 2 / 1 | 25,446 / 3,813 |
| **합** | **2,125** | **12,608,190** |

| check-coverage 하위 | 파일 | 크기(B) | | 하위 | 파일 | 크기(B) |
|---|---|---|---|---|---|---|
| (최상위 파일) | 9 | 111,349 | | part16 | 140 | 419,947 |
| longterm | 266 | 593,358 | | part17 | 7 | 24,902 |
| longterm-G | 107 | 483,394 | | part18 | 86 | 292,912 |
| longterm-H | 38 | 151,708 | | part19 | 17 | 61,483 |
| part11 | 91 | 536,486 | | part20 | 89 | 305,087 |
| part12 | 75 | 400,147 | | report-scope | 62 | 350,622 |
| part13 | 456 | 2,916,603 | | reports | 32 | 46,877 |
| part14 | 119 | 577,329 | | spot-check | 208 | 1,028,573 |
| part15 | 10 | 46,259 | | unprompted | 72 | 193,269 |

fixtures: contract-cases 425개(26.6MB, 이 중 evidence/v02-operational-validation-v1 52개 18.8MB, astra-smoke-v1 310개 7.0MB), package-history 27개. 저장소 pack은 25.6MiB다.
evals·fixtures의 스크립트는 131개다. 이 가운데 35개는 다른 어떤 파일도 이름을 언급하지 않는다(대부분 cc/spot-check·part11~13의 collect/mk/summarize*.py, liveH.sh, liveJ2.sh). 이 스크립트들은 기록을 만든 도구여서 기록과 함께 두는 편이 맞고, 제거 후보로 세지 않았다.

### 1-e. 제거 후보 (참조 없음, 기록·테스트·회귀 입력이 아님)

| # | 경로 | 근거 |
|---|---|---|
| 1 | docs/superpowers/plans/2026-09-29-design-harness.md | 저장소 전체에서 파일 이름 언급 0회, preserved 357에 없음 |
| 2 | docs/superpowers/plans/2026-10-06-harness-execution.md | 언급 0회, preserved에 없음 |
| 3 | docs/superpowers/specs/JOEDESIGN_DESIGN_HARNESS_V0_1_IMPLEMENTATION_HANDOFF.md (37KB) | 언급 0회, preserved에 없음 |
| 4 | docs/superpowers/specs/JOEDESIGN_DESIGN_TOOL_RESEARCH_2026-09-29.md (26KB) | 언급 1회(아래 6번 초안에서만) |
| 5 | fixtures/contract-cases/evidence/v02-operational-validation-v1/ (52파일, 18.8MB) | 폴더 이름 언급 0회(자기 안 제외), 테스트·preserved·274에 없음. 식별자 포함 파일 8개. 기록이므로 삭제보다 archive 쪽 |
| 6 (조건부) | docs/superpowers/specs/JOEDESIGN_UI_REVIEW_RACI_V0_1_DRAFT.md (59KB) | AGENTS.md(과거 지시)와 docs/VALIDATION.md가 링크함. `C:/Users/<user>/...` 9줄 포함. 옮기면 링크 2곳을 고쳐야 함 |
| 캐시 | skills/joedesign/scripts/__pycache__/, scripts/harness/__pycache__/, tests/__pycache__/ | 추적 안 됨, .gitignore가 무시함. 로컬 정리만 하면 됨 |

옮기면 안 되는 것: docs/specs v0.1 8개, docs/handoffs 5개, docs/decisions 1개, docs/superpowers/plans/2026-09-06-* 3개. 모두 preserved 해시 대상이고, 경로가 바뀌면 node 테스트가 깨진다.
중복 영수증: install-receipt.md 9개와 release-notes 5개는 버전마다 하나씩이라 중복이 아니다. 바이트가 같은 파일 135묶음(사본 240개)은 대부분 longterm turn 변경 목록과 같은 캡처다. git은 blob을 한 번만 저장하므로 지워도 크기 이득이 0이다.

### 1-f. 미추적·무시

- `git status`의 미추적 항목은 `evals/feedback-20261013/`(36K)와 `evals/feedback-implementation-20261013/`(2.8M), 합 563파일이다. 손대지 않았다.
- `.gitignore`: `__pycache__/`, `*.pyc`, `.superpowers/`, `.design-harness/`
- `.git/info/exclude`: `/.local/`(466MB 로컬 작업 자료), `/LOCAL-START-HERE.md`. 그 밖에 빈 폴더 `.agents/skills`가 있다(git은 빈 폴더를 추적하지 않음).

## 2. 참조 그래프

| 출발 | 도착 (모두 존재 확인) |
|---|---|
| SKILL.md | references/visual-translation.md, visual-production.md, operation.md#raci-as-the-work-route, conformance.md, execution.md, operation.md; templates/DESIGN.md(2회, Report Form 절); `scripts/report-check.mjs`; JOEFLOW `scripts/approval_status.py`(외부) |
| references/conformance.md | ../SKILL.md, ../templates/DESIGN.md, impact.md, `scripts/report-check.mjs`, `scripts/harness_cli.py`, capture.mjs |
| references/execution.md | ../SKILL.md, conformance.md, `scripts/harness_cli.py`, `scripts/capture.mjs`(예시 경로), 프로젝트 AGENTS.md |
| references/operation.md | execution.md, ../SKILL.md#decide-the-scope-before-making-the-screen, `scripts/harness_cli.py`, templates 7종(CRITIQUE·DESIGN_CONTRACT·DESIGN_INTENT·EVIDENCE_MANIFEST·REFERENCE_CANDIDATES·REFERENCE_LOCK·STATE_MATRIX), `scripts/harness/evidence.py`, JOEFLOW 파일 |
| references/visual-production.md | ../SKILL.md#decide-the-scope…, operation.md#product-meaning-to-visual-roles |
| references/visual-translation.md | ../SKILL.md, visual-production.md, ../templates/DESIGN.md |
| references/impact.md | `scripts/harness_cli.py` |
| templates/DESIGN_CONTRACT.md | DESIGN.md(프로젝트 것) |
| report-check.mjs 머리말 | "DESIGN template's Report Form section"(이름만), 없음 |
| capture.mjs | ./measure-layout.mjs, 설치된 `playwright` 모듈 |
| harness_cli.py | harness/*.py, ../VERSION, ../SKILL.md, ../references/visual-*.md |

헤딩 앵커 3개(`#raci-as-the-work-route`, `#product-meaning-to-visual-roles`, `#decide-the-scope-before-making-the-screen`)가 실제 헤딩과 맞는다. 스킬이 가리키는 README·docs 구절은 없다. 따라서 README를 줄여도 스킬 동작에는 영향이 없다.

README를 줄여도 남아야 할 것:
- 다른 문서가 가리키는 README 앵커. docs/INSTALL.md 14행이 `../README.md#4-사용-방법`을 가리킨다(한국어 헤딩 "## 4. 사용 방법").
- README가 가리키는 스킬 파일: VERSION, SKILL.md, references/conformance.md·execution.md·impact.md.
- README의 `[English](#english) | [한국어](#korean)` 앵커.

README가 스킬 내용을 되풀이하는 곳:
- 13행(영어)과 138행(한국어). 1.1.0~1.3.4 변경을 한 줄에 이어 쓴 약 2,000자 버전 설명이며, CHANGELOG와 SKILL.md 6단계·report-check 규칙 R5~R7을 되풀이한다.
- 108·120행, 228·244행. conformance·impact 조건을 요약한다(링크로 대체 가능).

## 3. 보안 검토 (보고만 함, 고치지 않음)

### (i) 비밀값

| 범위 | 패턴 | 결과 |
|---|---|---|
| 현재 트리 | AWS 키, GitHub 토큰(ghp/gho/github_pat), `sk-`/`sk-ant-`, Slack xox, Google AIza, JWT, PRIVATE KEY 머리말, DB 연결 문자열(user@), `Password=` | 0 |
| 현재 트리 | `api_key/secret/password/token = "8자 이상"` | 0 |
| 전체 이력(`git log --all -p -G`) | 위 두 묶음 | 0 |
| 이력 속 파일 이름 | `.env`, `.pem`, `.key`, `id_rsa`, `.p12`, `credentials` | 0 |

### (ii) 개인 식별자 (현재 트리 = HEAD 추적 파일, 대소문자 무시)

| 식별자 | 파일 | 등장 수 | docs | skills | 이력: 해당 줄을 바꾼 커밋 / 그 줄이 있던 경로 |
|---|---|---|---|---|---|
| `<user>` | 53 | 202 | 1 | 0 | 28 / 68 |
| `<email>` | 0 | 0 | 0 | 0 | 0 / 0 (gmail.com 자체도 0) |
| `C:/Users` | 39 | 87 | 1 | 0 | 26 / 42 |
| `C:\Users`(백슬래시 1개) | 1 | 2 | 0 | 0 | 3 / 5 |
| `C:\\Users`(JSON 이스케이프) | 14 | 117 | 0 | 0 | 10 / 22 |
| `AppData` | 17 | 66 | 0 | 0 | 7 / 17 |
| 합집합(파일) | **65** | | 1 | 0 | |

- 폴더별 분포: fixtures/contract-cases 33(astra 계열 history·smoke 15, v02-operational 8, visual-translation-v02 evidence 5, 기타), evals/v1-release-candidate 11, behavior-forward 7, f05-impact 5, handoff-visual-roles 2, design-conformance 2, cc/longterm-G 2, cc/longterm-H 1, harness-v0.1 1, docs/superpowers 1.
- **65개 중 20개는 preserved 해시 대상이다.** 가리면 `tests/joedesign-v02.tests.mjs`가 실패한다. 1개는 files-274 회귀 입력이라, 가리면 R1~R7 수가 달라질 수 있다.
- 이미 `~`로 가린 파일은 7개다(`~/Documents/JOEDESIGN-backups`, `~/.codex/...` 형태, 2026-11-18 install receipt 작업분).
- docs에 남은 것: `docs/superpowers/specs/JOEDESIGN_UI_REVIEW_RACI_V0_1_DRAFT.md` 316–324행, `C:/Users/<user>/.codex|.agents/skills/...` 9줄.
- 위탁문은 "그 밖의 역사 파일 약 260개가 남았다"고 했지만, 이 조사의 패턴으로 센 현재 트리 파일은 65개다. 차이의 원인은 확인하지 못했다(아래 "확인되지 않은 것").

### (iii) 스크립트

| 스크립트 | 외부 입력 | 쓰는 곳 | 프로세스·네트워크 | 프로젝트 밖 읽기 가능성 |
|---|---|---|---|---|
| report-check.mjs | argv[0] 경로 하나(`--verify` 포함). 그 Markdown 본문을 정규식으로 검사 | 없음(stdout·종료 코드만) | 없음. eval·child_process 없음 | 보고서 내용이 다른 경로를 열게 하지 못함. 인자로 준 파일만 읽음 |
| capture.mjs | stdin JSON: `browser.base_url`(http/https + localhost·127.0.0.1·[::1]만 허용), `playwright_module`(임의 경로 require), `executable`(임의 브라우저 경로), `output_dir`, targets, probes(selector·click/fill/press/hover/scroll/wait), design.checks | `output_dir`에 PNG·observation JSON(경로 제한 없음) | **브라우저를 띄움**: `chromium.launch({headless: true, executablePath?})`, 다른 플래그 없음(`--no-sandbox` 없음). 네트워크: 설정한 로컬 origin으로만 이동, origin을 벗어나면 예외. 페이지가 불러오는 하위 리소스는 막지 않음. 다운로드 없음 | 페이지는 파일을 읽게 할 수 없음. 그러나 설정 JSON의 `playwright_module`은 임의 코드 실행 경로이므로 설정 파일 자체가 신뢰 경계다. 측정값은 페이지 JS가 조작할 수 있음 |
| measure-layout.mjs | 설정의 selector·edge·axis | 없음 | `page.evaluate` 안에서만 동작 | 없음 |
| harness_cli.py | argparse 경로 인자(--project, --baseline, --observation, --reviews, --runtime, --evidence-root, --skills-root, --output 등) | `--output`·`root` 아래 artifact(원자적 쓰기, `.harness-` 임시 파일), `advance`가 EVIDENCE_MANIFEST 덮어씀 | 하위 모듈 참고. 네트워크 없음 | 아래 참고 |
| harness/execution.py | runtime JSON: `collector_command`(argv 목록), `skills`, `skills_roots`, `reference_images`, request | 실행 root 아래 attempt 폴더, `execution.lock` | `subprocess.run(['git', ...])` 목록 인자, shell=False. collector는 설정한 argv 그대로 실행 | 수집기 출력의 capture `path`를 위치 제한 없이 `resolve(strict=True)`로 읽음. 수집기를 믿는다는 전제 |
| harness/runner.py | 작업 패킷 | `folder/process/{stdin.txt,stdout.jsonl,stderr.txt}`, schema·input·source-context.json | `subprocess.Popen(argv)` 목록 인자, shell=False. `codex exec --json --sandbox read-only|workspace-write -c approval_policy="never" --cd <project>`. 시간 초과 시 Windows는 `taskkill /T /F` | 검토 패킷에 프로젝트 AGENTS.md, 프로젝트 안 component 파일(`is_relative_to` 확인), 해시가 맞는 capture JSON 내용을 실음(64KB/개, 256KB 합) |
| harness/conformance.py | baseline JSON, observation JSON(CLI 경로), reviews | 없음(호출자가 씀) | 없음 | baseline 입력 경로는 `input_path`가 막음(`..`, 절대 경로, `\`, `:`, 제어문자, 심볼릭 링크 탈출 거부). observation의 `frames` 경로는 제한 없이 해시만 계산(내용은 출력하지 않음) |
| harness/impact.py | request JSON, `--evidence-root` | `--output` | 없음 | 증거 절대 경로는 project와 `--evidence-root` 안으로 제한, 64MB 상한 |
| harness/references.py | corpus 폴더의 DESIGN.md들 | 없음 | 없음 | 심볼릭 링크가 root를 벗어나면 거부 |
| harness/io.py, pipeline.py, contracts.py, evidence.py | 경로·JSON | `write_artifact`(덮어쓰기는 명시 시에만), 트랜잭션 백업 | 없음 | 없음 |

- `eval`·`exec`·`new Function`·`os.system`·`shell=True`·`pickle`·네트워크 라이브러리(urllib, requests, socket, fetch)는 스킬 스크립트 어디에도 없다.
- 설치 스크립트는 저장소에 없다. README 4절의 PowerShell 블록이 `$CODEX_HOME/skills/joedesign`(기본값 `%USERPROFILE%\.codex\skills\joedesign`)에 복사하며, 기존 설치가 있으면 중단한다.
- `doctor`는 `~/.codex/skills`와 `~/.agents/skills`를 읽는다. 이 조사에서는 `version`만 실행했다.

### (iv) 의존성 매니페스트

`package.json`, `package-lock.json`, `requirements*.txt`, `pyproject.toml`, yarn/pnpm lock 파일이 저장소 어디에도 없다(evals·fixtures 포함). lockfile이 없으므로 `npm audit`은 실행하지 않았다. 실행 의존성: Python 3.11+ 표준 라이브러리(operation.md 15행), Node(report-check는 내장 모듈만 사용), 선택 사항으로 기존 Playwright·브라우저와 Codex CLI.

### (v) CI

`.github/`가 없어 워크플로·권한·secrets 사용이 0이다.

## 4. 사용 안내

README: 251줄, 1,526단어(wc 기준), 16,859B. 구조는 영어 6절과 한국어 6절이 같은 순서다: 1 Summary/핵심 요약, 2 Design Purpose/설계 목적, 3 Key Features/주요 기능, 4 Usage/사용 방법(Installation/설치, Example request/실행 요청), 5 Tool Integration/도구 간 연결, 6 Limitations/한계. 400자를 넘는 줄은 13행(1,994자)과 138행(2,026자) 두 개다.

### Quickstart 한 쪽 초안 (지금 있는 명령만 사용)

| 단계 | 명령 | 문서 상태 |
|---|---|---|
| 1a 설치(Codex) | `git clone https://github.com/JOEWRKS/JOEDESIGN.git` → `cd JOEDESIGN` → README 4절 블록(`Copy-Item -LiteralPath '.\skills\joedesign' -Destination $JoeTarget -Recurse`, 대상 `$CODEX_HOME/skills/joedesign`) | 있음(README 51–68행, INSTALL 12–25행) |
| 1b 설치(Claude Code) | (명령 없음) 예: `~/.claude/skills/joedesign`에 같은 폴더를 복사 | **없음**. README·INSTALL은 Codex만 다룬다. `doctor`의 기본 탐색 경로에 `~/.claude/skills`가 없어 `--skills-root`를 따로 줘야 한다. **누락** |
| 2 확인 | `python -B <설치폴더>/scripts/harness_cli.py version` → `python -B <설치폴더>/scripts/harness_cli.py doctor` (전문 스킬이 없을 때 종료 코드 2는 정상) | 있음(README 66–67행, INSTALL 29–46행). 이 조사에서 `version`은 `1.3.4`를 출력함 |
| 3 첫 디자인 검토 | 대화: `$joedesign` + 검토 요청(README 84–90행 예시는 제작 요청이고, 검토 전용 예시 문장은 없음). CLI: `harness_cli.py verify-design --baseline <json> --baseline-sha256 <hash> --project <dir> --observation <json>`, `harness_cli.py run <root> --project <git-root> --runtime <runtime.json> --review-only [--check-only]` | 대화 예시는 있으나 검토 전용이 아님. CLI 단계는 references/execution.md·conformance.md(에이전트용)에만 있음. **사람용 단계 누락** |
| 4 보고와 검사 | `node <설치폴더>/scripts/report-check.mjs REPORT.md` → `report-check: ok <chars> chars <sha8>`가 나올 때까지 고침 → 보낸 글 끝에 그 줄 → `node <설치폴더>/scripts/report-check.mjs --verify SENT.md` | SKILL.md 6단계, conformance.md, 스크립트 머리말, docs/proposals에만 있음. **README·INSTALL에 없음** |
| 5 새 버전으로 업데이트 | `git pull` 다음 설치 폴더 교체. 명령 없음, INSTALL 53–76행은 에이전트에게 맡기는 요청문만 있음 | **명령 누락**. README 블록은 기존 설치가 있으면 `throw`로 멈추므로 업데이트에 쓸 수 없음(모순은 아니지만 빈칸) |

모순·낡은 표기:
- README 114·237행 "1.3.0은 지원 범위의 패키지 버전"(현재 1.3.4).
- README 11·136행 "Codex 기반". 사용자는 Claude Code에서도 쓰지만 문서에 없다.
- INSTALL 51행의 검증 환경 링크는 1.0.0 기록이다.
- INSTALL 10행 "1.0.0 변경 경계".

## 5. D 후보 (조치하지 않음)

### 중복·낡을 문장

| 위치 | 내용 | 2.0에서 |
|---|---|---|
| README 13·138행 | 1.1.0~1.3.4 변경 서술, 줄마다 약 2,000자 | CHANGELOG 링크 한 줄로 줄일 후보 |
| README 114·237행 | "1.3.0 …" | 낡음 |
| docs/INSTALL.md 38행 | `version`이 `1.3.4`인지 확인 | 버전을 올리면 고쳐야 함 |
| docs/INSTALL.md 10·51행 | 1.0.0 경계·1.0.0 검증 기록 | 낡음 |
| skills (동결, 목록만) | 결과 줄 계약(`check \| result \| …`, `fixed`/`changed`, `rendered (injected css)`, 순서)을 SKILL.md 133–171행, conformance.md 33–68행, templates/DESIGN.md 56–87행에 세 번 씀 | 인계용으로 일부러 둔 중복(1.2.x 결정). 스킬 동결이라 범위 밖 |
| skills (동결) | 글자까지 같은 문장 1개: "A line that is not spot-checked is never listed as resolved, verified or done." (SKILL.md 157행, conformance.md 50행 부근) | 범위 밖 |
| skills (동결) | report-check.mjs 25행 "as some 1.3.0 reports have", operation.md 15행 "Python 3.11+" | 2.0에서 낡는 버전 표기. 범위 밖 |
| AGENTS.md | T043 절이 2026-11-04~18 과정을 날짜·버전별로 서술(260줄) | 이 저장소 작업자용. 2.0에서 요약하거나 archive할 후보 |

스킬 폴더 안에는 날짜(2026-…)와 T 번호가 없다.

### 버전 문자열이 있는 파일

| 파일 | `1.3.4` 수 | `1.3.x` 수 |
|---|---|---|
| skills/joedesign/VERSION | 1 | 1 |
| skills/joedesign/scripts/report-check.mjs | 0 | 1 (주석 "1.3.0 reports") |
| README.md | 2 | 4 |
| docs/INSTALL.md | 1 | 1 |
| CHANGELOG.md | 3 | 29 |
| AGENTS.md | 4 | 20 |
| tests/report-check.tests.mjs | 3 | 8 (모두 테스트 이름표, 판정에는 쓰이지 않음) |
| evals/** | 16개 파일 | 69개 파일 (기록, 고치지 않을 대상) |

버전 문자열을 판정하는 테스트: 하드코딩한 것은 없다. `tests/test_harness_package.py` 42행은 `harness_cli.py version` 출력을 같은 복사본의 VERSION 파일과 비교하므로, 버전을 올려도 통과한다. `tests/joedesign-v02.tests.mjs`는 보관된 v0.2 패키지(fixtures/package-history)만 고정한다.
**충돌**: `skills/joedesign/VERSION`과 `harness_cli.py version`·`doctor` 출력이 스킬 폴더 안에 있다. "2.0.0"으로 올리면 트리 해시 `928b5b90…`가 바뀌어 "스킬 폴더 해시가 1.x와 같다"는 게시 조건을 지킬 수 없다. 둘 중 하나를 골라야 한다: VERSION을 1.3.4로 두고 2.0은 저장소 태그로만 표시하거나, 게시 조건을 "VERSION을 뺀 나머지 파일이 같다"로 바꾸거나.

## 확인된 것

- 스킬 31개 파일의 링크 21개와 앵커 3개가 모두 실제 파일·헤딩과 맞는다. 스킬에서 README·docs·evals로 가는 링크는 0개다.
- node 44/44, python 142 OK(건너뜀 2: `JOEDESIGN_PLAYWRIGHT_MODULE` 미설정). 이 조사 중 실행했고, `-B`로 캐시를 쓰지 않았다.
- preserved 357개 해시 고정(docs 17개 포함), files-274 전부 존재, 회귀 스크립트가 태그 v1.3.2·v1.3.3과 `../../../` 깊이에 의존.
- 비밀값 0(트리·이력), `<email>` 0(트리·이력), CI·매니페스트 0.
- 식별자: 현재 트리 65개 파일, 그중 preserved 20개, files-274 1개, docs 1개, skills 0개.
- capture.mjs는 headless Chromium을 추가 플래그 없이 띄우고, 로컬 origin으로만 이동한다. 셸 문자열 실행, eval, 다운로드는 없다.

## 확인되지 않은 것

- 위탁문의 "약 260개" 미마스킹 파일 수와 이 조사의 65개가 다른 이유. 패턴 차이(예: `D:\JOEWRKS` 같은 다른 경로, 다른 저장소)일 수 있다. 이 조사의 패턴은 `<user>`, `C:/Users`, `C:\Users`, `C:\\Users`, `AppData`다.
- 이력 수치의 뜻: `git log -G`로 센 것은 "해당 줄을 더하거나 뺀 커밋"과 "그 커밋이 건드린 경로"다. 모든 과거 blob 안의 등장 수가 아니다.
- `doctor` 출력(개인 스킬 폴더를 읽으므로 실행하지 않음), Playwright 경로 테스트 2개, `harness_cli.py run` 실제 실행(Codex 실행기 필요).
- evals 안의 상호 참조(기록끼리의 상대 링크) 전체 수는 세지 않았다. README·docs·CHANGELOG·AGENTS가 evals 경로를 참조하는 수만 셌다(0·15·33·8).
- 35개 무참조 스크립트가 실제로 재실행 가능한지.
- `.local/`(466MB) 내용. info/exclude로 제외된 로컬 자료라 열어보지 않았다.

## 세션이 대신 내린 결정

- 경계: 저장소 안 `.local/`은 위탁문이 금지한 `D:\JOEWRKS\.local`과 다른 폴더다. 그래도 크기만 쟀고 내용은 읽지 않았다.
- 테스트 두 묶음을 실행했다. 읽기 전용 조사지만 2.0 게시 조건(테스트 전부 통과)의 기준선이 필요하다고 판단했다. 임시 폴더만 쓰고 `-B`를 붙였으며, 끝난 뒤 `git status`가 시작 때와 같음을 확인했다.
- 바이트가 같은 중복 파일과 무참조 eval 스크립트는 제거 후보에서 뺐다. 앞쪽은 git 크기 이득이 0이고, 뒤쪽은 기록을 만든 도구다.
- `v02-operational-validation-v1`은 "기록이지만 아무도 참조하지 않음"으로 보아 제거 후보에 넣되, 처리 방식은 삭제가 아니라 archive로 적었다.
- 식별자 수는 대소문자를 무시한 `git grep -I`(바이너리 제외) 기준이다. 사용자 이름은 `%USERPROFILE%`의 마지막 경로 이름에서 얻었다.
