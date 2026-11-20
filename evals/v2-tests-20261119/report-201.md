# JOEDESIGN 2.0.1 후보 준비 (2026-11-20, T044)

**결론:** 2.0.0 시험 보고 두 건에서 JOEDESIGN 몫 결함을 모두 재현하고 고쳤다. 커밋은 main에 로컬로 5개 했다(push·태그·Release·설치 없음). 코드 결함 3건은 T1 `doctor`가 `CODEX_HOME`을 무시함, 연동 D5 영수증의 절대 evidence 경로, 연동 D7 intent 행 모양 오류다. 셋 다 고치기 전에 실패하는 테스트를 먼저 만들고 확인했다. 문서 결함은 D1~D5와 연동 D9를 고쳤다. 연동 D3은 사용자 결정("3번 절차로")에 따라 `references/conformance.md`에 절차 문장 하나를 넣어 해결했다(코드 변경 없음). D8은 사용자 지시("전부 고친 다음에 게시")에 따라 `templates/DESIGN.md`를 JOENESS 모양에 맞춰 고쳤다([CHANGELOG 2.0.1](../../CHANGELOG.md)). 행동 시험은 0회다.

입력(복사본, 홈 경로·사용자 이름 가림): [QUICKSTART 실행 시험](docs-joedesign-report.md), [세 도구 연동 시험](integration-report.md).

## 결함별 처리

| ID | 재현 | 처리 | 확인 |
|---|---|---|---|
| T1 `doctor` 기본 경로가 `CODEX_HOME` 무시 | 재현됨: `CODEX_HOME=<빈 scratch>`로 `doctor`를 돌리자 실제 `~/.codex/skills`·`~/.agents/skills`의 전문 스킬 5개가 AVAILABLE로 나옴 | `execution.py`: `$CODEX_HOME/skills`, 없으면 `~/.codex/skills` | 새 테스트: 가짜 HOME·USERPROFILE + `CODEX_HOME`에서 CODEX_HOME 쪽만 발견, 가짜 홈 `.codex`는 읽지 않음. `CODEX_HOME`이 없으면 가짜 홈 `.codex` 사용. 고치기 전 ERROR |
| D2 `--skills-root`가 대체임이 안 적힘 | 코드 확인(`settings.get('skills_roots', 기본값)`, `action='append'`) | 코드 그대로. `--help`·QUICKSTART 2절(두 경로 예시)·INSTALL 표에 "대체, 반복 지정" | `doctor --help` 출력 확인 |
| 연동 D5 영수증 절대 evidence 경로 | 코드 확인(`str(p.resolve())` 3곳) | `conformance.evidence_path`: 프로젝트 안은 `/` 상대 경로, 밖은 절대 경로 | 새 테스트 2개: 상대 경로 기록(고치기 전 FAIL). `inspect-impact`가 상대 영수증과 2.0.0식 절대 영수증 둘 다에서 재사용 후보 4/4 |
| 연동 D7 템플릿 행 모양 | 재현됨: 문자열 requirements로 `retrieve` → `string indices must be integers` | `contracts.requirement_ids`, 행 모양을 붙인 오류. 템플릿에 requirement·target 예시 행 | 새 테스트 2개: `NOT_READY`, 오류에 `id`·`kind`·`description`이 들어감. 템플릿이 `INVALID_ARTIFACT`/`INVALID_TARGET`/`INVALID_ID` 없이 검증됨. 고치기 전 둘 다 FAIL |
| D1 비공개·로그인 문구 | 재현됨: `gh repo view` → `PUBLIC` | QUICKSTART·README·INSTALL 문구 교체. SECURITY.md에 공개 전제 두 곳 | 문서 |
| D3 백업 해시 명령 없음 | 재현됨(INSTALL에 명령 없음) | INSTALL "백업과 해시 비교" 블록, QUICKSTART 링크 | scratch에서 실행: 31개 일치 시 출력 없음, `VERSION`을 바꾸면 그 한 파일 표시 |
| D4 태그 고정 방법 없음 | 문서 확인 | QUICKSTART·INSTALL에 `main` 전제와 `git fetch --tags; git checkout v2.0.1` | 태그가 아직 없어 실행 안 함 |
| D5 기준 문서 없을 때 | 문서 확인 | QUICKSTART 3절 한 줄 | 문서 |
| 연동 D9 스타일시트 로드 확인 | 문서 확인(측정 전 확인 단계 없음) | `templates/DESIGN.md` Report Form 한 문장 | 행동 시험 0회 |
| 연동 D3 Result 갱신 ↔ authority stale | 연동 log/24·25(시험 보고) | 사용자 결정 "3번 절차로": `references/conformance.md` authority 설명에 절차 문장(완료 뒤 stale은 정상, 다음 과업이 새 기준선, 같은 과업 재검수는 Result를 되돌린 뒤). `conformance.py` 그대로 | 문서. 행동 시험 0회 |
| 연동 D8 DESIGN.md 머리줄·표 형식 차이 | JOENESS `assets/DESIGN.md` 읽기만(3–8행 머리줄, 10–19행 8열 표, 13행 Result) | 템플릿 정렬: `## Rule coverage`, Result 열을 더한 8열, JOENESS 머리줄 두 줄을 위에 두고 JOEDESIGN 세 줄 유지, conformance.md에 "Report Form은 DESIGN.md가 원본" 한 문장. SKILL.md 그대로 | 템플릿 문구를 고정한 테스트 없음(v02 테스트는 보관본 템플릿만 읽음), report-check는 템플릿을 읽지 않음. 게이트 재실행. 행동 시험 0회 |

## JOENESS 소비자 확인 (읽기만)

`D:\JOEWRKS\.local\joe-latest-20261029\JOENESS\skills\joeness-setup\scripts\review-gate.mjs`는 읽기만 하고 실행하지 않았다. `pathFor`(25–30줄)는 evidence 경로가 절대 경로이거나 `safeRelative`(`/` 구분, 빈 조각·`.`·`..`·`\`·`:`·제어문자 없음, NFC)일 때 받는다. 그 경로를 `--root` 기준으로 realpath하고 root 또는 `--evidence-root` 안인지 본다. 새 상대 경로는 `Path.relative_to(...).as_posix()`라 이 조건을 만족한다. 단 `--root`가 `verify-design --project`와 같은 폴더일 때만이다. 실제 통과 여부는 실행해 보지 않았다.

## 해시 고정 파일과의 충돌 사전 확인

- `fixtures/contract-cases/evidence/visual-translation-v02/baseline-and-freeze.json`의 preserved·frozen 359개 경로에는 스킬 폴더·docs·README·CHANGELOG가 없다. 그중 README는 `astra-smoke-v1/pure-core-freeze-v1/README.md` 하나뿐이고 루트 README와 다른 파일이다.
- part19 회귀는 `report-check.mjs`와 `files-274.txt`의 보고만 읽는다. 이번 변경은 그 둘을 건드리지 않는다. 다시 실행한 뒤에도 출력 파일 세 개는 git 변경이 없다.
- 미추적 `evals/feedback-20261013/`, `evals/feedback-implementation-20261013/`은 건드리지 않았다.

## 게이트

| 항목 | 결과 |
|---|---|
| `node --test tests/*.tests.mjs` | 44/44 |
| `python -B -m unittest discover -s tests` | 147 OK, 건너뜀 2 (2.0.0의 142에 이번 테스트 5개) |
| `node evals/check-coverage-20261104/part19/regress.mjs` | 274: `{"R3":269,"R5":44,"R1":75,"R6a":103,"R4":4,"R2":3,"R6b":7}`. 1.3.3과 후보가 같고 R7 바뀐 파일 0, 출력 파일 git 변경 없음 |
| `harness_cli.py version` | `"version": "2.0.1"` |
| 스테이징 diff의 사용자 이름·메일·`C:\Users` | 0건(커밋마다 확인) |
| `git diff --stat v2.0.0 HEAD -- skills/joedesign` | 9개 파일: VERSION, harness_cli.py, harness/conformance.py·contracts.py·execution.py·references.py, references/conformance.md, templates/DESIGN.md·DESIGN_INTENT.json |

## 확인되지 않은 것

- 행동 시험 0회: Report Form의 스타일시트 확인 문장, conformance.md의 D3 절차 문장, D8 템플릿 정렬, 문서 D1~D5를 실제 사용자 경로로 다시 따라 하기.
- review-gate 실행(읽기만 함). macOS·Linux `CODEX_HOME`. 태그 체크아웃 명령.

## 세션이 대신 내린 결정

CHANGELOG 2.0.1 "세션이 대신 내린 결정"과 같다. 과업 번호 T044, 프로젝트 밖 evidence는 절대 경로 유지(`verify-design --evidence-root`를 새로 달지 않음), 빈 requirements 허용 유지, D9 문장 위치는 Report Form, 연동 D11·D13은 범위 밖으로 두었다.

## 쓴 경로

이 저장소 안만 썼다. 커밋된 파일과 scratchpad(`CODEX_HOME`·백업 블록 시험용, 저장소 밖 임시 폴더)뿐이다. `~/.codex`, `~/Documents/JOEDESIGN-backups`, `D:\JOEWRKS\.claude\skills`에는 쓰지 않았다. joe-latest는 review-gate.mjs 한 파일만 읽었다. T1 재현 때 `doctor`가 실제 `~/.codex/skills`·`~/.agents/skills`의 `SKILL.md`를 읽어 해시를 냈다. 시험 보고의 결함과 같은 동작이고 쓰기는 없었다.
