# 보안 (JOEDESIGN 2.0.0)

결론: 저장소는 공개다(2026-11-20 `gh repo view` PUBLIC). 비밀값·의존성 매니페스트·CI는 없다. 개인 식별자(홈 경로·사용자 이름)는 현재 트리 38개 파일과 git 이력에 남아 있고, 이유는 테스트·기록이 그 파일의 해시를 고정하기 때문이다. 스크립트는 셸 문자열 실행·eval·네트워크 라이브러리를 쓰지 않는다. 다만 `capture.mjs` 설정 JSON과 harness의 runtime JSON은 코드 실행 경로이므로 그 파일이 신뢰 경계다.

근거: [`evals/v2-survey-20261119/report.md`](evals/v2-survey-20261119/report.md) 3절(2026-11-19 조사), [`evals/v2-release-20261119/report.md`](evals/v2-release-20261119/report.md)(2.0.0 정리 결과).

## 검사한 것과 결과

| 항목 | 범위 | 결과 |
|---|---|---|
| 비밀값 패턴(AWS 키, GitHub 토큰, `sk-`/`sk-ant-`, Slack, Google API 키, JWT, PRIVATE KEY, DB 연결 문자열, `api_key/secret/password/token = "…"`) | 현재 트리, 전체 이력(`git log --all -p -G`) | 0건 |
| 비밀 파일 이름(`.env`, `.pem`, `.key`, `id_rsa`, `.p12`, `credentials`) | 이력 속 파일 이름 | 0건 |
| 메일 주소 | 현재 트리, 이력 | 0건 |
| 개인 식별자(Windows 사용자 이름, 그 이름이 든 홈 폴더 경로) | 현재 트리 | 2.0.0 전 사용자 이름이 든 파일 53개 → 2.0.0에서 15개를 `~`·`<user>`로 가림 → **38개 남음** |
| 의존성 매니페스트(`package.json`, lock, `requirements*.txt`, `pyproject.toml`) | 저장소 전체 | 0개. 실행 의존성은 Python 3.11+ 표준 라이브러리, Node 내장 모듈, 선택 사항인 기존 Playwright·브라우저·Codex CLI |
| CI(`.github/`) | 저장소 | 없음. 워크플로·secrets 사용 0 |

## 남은 것과 이유

- **해시가 고정된 20개**: `fixtures/contract-cases/history/astra-*`·`evidence/astra-smoke-v1/*`. `tests/joedesign-v02.tests.mjs`가 이 파일들의 해시를 비교하므로 가리면 테스트가 실패한다.
- **회귀 입력 1개**: `evals/handoff-visual-roles-20261008/README.md`. `files-274.txt` 회귀(part15·17·19 regress)의 입력이라 가리면 수치 비교의 바탕이 바뀐다.
- **기록이 해시를 적어 둔 17개**: `evals/behavior-forward-20261010/records/*` 7개, `evals/f05-impact-20261013/*` 5개, `fixtures/contract-cases/evidence/visual-translation-v02/*` 5개(이 폴더는 테스트가 읽는다). 가리면 같은 폴더의 manifest·결과 파일에 적힌 해시와 어긋난다.
- **git 이력**: 위 식별자는 과거 커밋에도 있다. 이력은 다시 쓰지 않는다(사용자 결정). 이력에서 지우려면 이력 재작성과 강제 푸시가 필요하고, 그러면 태그 v1.x와 기존 기록의 커밋 참조가 깨진다.
- 남은 식별자는 홈 폴더 경로와 사용자 이름뿐이며 비밀값이 아니다. 저장소가 공개라 누구나 읽을 수 있다.

## 스크립트의 신뢰 경계

| 스크립트 | 읽는 것 | 쓰는 것 | 실행·네트워크 |
|---|---|---|---|
| `skills/joedesign/scripts/report-check.mjs` | 명령줄로 준 파일 하나(`--verify` 포함) | 없음(표준 출력·종료 코드) | 없음. import는 `node:fs`·`node:crypto`뿐, eval·child_process 없음. 보고서 내용이 다른 파일을 열게 할 수 없음 |
| `scripts/capture.mjs` | 표준 입력의 설정 JSON | 설정의 `output_dir`(경로 제한 없음)에 PNG·관찰 JSON | headless Chromium을 추가 플래그 없이 띄움. `base_url`은 http/https와 localhost·127.0.0.1·[::1]만 허용, 대상이 그 origin을 벗어나면 중단. 페이지가 부르는 하위 리소스는 막지 않음. **설정의 `playwright_module`(임의 모듈 require)과 `executable`(임의 브라우저 경로)은 코드 실행 경로라 설정 JSON 자체가 신뢰 경계다.** 측정값은 페이지 JS가 바꿀 수 있음 |
| `scripts/measure-layout.mjs` | 설정의 selector | 없음 | 페이지 안 `page.evaluate`만 |
| `scripts/harness_cli.py`, `scripts/harness/*.py` | 명령줄 경로 인자, runtime·baseline·observation JSON | `--output`·실행 root 아래에만(원자적 쓰기) | 하위 프로세스는 argv 목록으로만(`shell=True` 없음): `git`, Windows 시간 초과 시 `taskkill`, `runner.py`의 `codex exec --sandbox read-only|workspace-write`. 네트워크 라이브러리 없음. baseline 입력 경로는 `..`·절대 경로·링크 탈출을 거부 |
| harness collector | runtime JSON의 `collector_command`(argv) | collector가 정함 | **설계상 신뢰한다**: 설정한 명령을 그대로 실행하고, 그 출력의 capture 경로를 위치 제한 없이 읽어 해시를 잰다. runtime JSON과 collector는 사용자가 고른 것이어야 한다 |

설치 스크립트는 없다. README의 PowerShell 블록은 스킬 폴더를 Codex 스킬 폴더로 복사만 하며, 대상이 이미 있으면 멈춘다.

## 알리는 방법

- 비밀값이 아닌 문제(스크립트 동작, 문서 오류): GitHub 저장소 `JOEWRKS/JOEDESIGN`에 이슈.
- 민감한 문제(비밀값·개인정보 노출 등): 이슈 본문에 세부 내용을 쓰지 말고 저장소 소유자에게 비공개 연락을 요청한다. GitHub의 비공개 취약점 신고 기능이 켜져 있는지는 확인하지 않았다.
