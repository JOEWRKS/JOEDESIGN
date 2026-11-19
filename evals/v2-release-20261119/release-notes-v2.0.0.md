# JOEDESIGN 2.0.0

저장소 위생, 보안 검토 문서, 빠른 시작 문서를 더한 판입니다. **스킬 동작은 1.3.4와 같습니다.** `skills/joedesign`에서 바뀐 파일은 `VERSION` 하나이고 나머지 30개 파일은 바이트 단위로 같습니다. 보고 검사 R1~R7, 도장·`--verify`, 다른 스크립트는 그대로입니다.

## 바뀐 것

- **위생**: 아무도 참조하지 않는 `docs/superpowers` 초안 4개 삭제. `fixtures/contract-cases/evidence/v02-operational-validation-v1/`(52파일, 약 18.8MB)을 `evals/archive/2026-11-19-unreferenced/`로 이동. 사용자 이름이 든 홈 경로를 15개 파일에서 `~`로 가림. git 이력은 다시 쓰지 않음.
- **[SECURITY.md](../../SECURITY.md)**: 검사 항목과 결과(비밀값 0, 매니페스트·CI 없음), 남은 식별자와 그 이유(테스트가 해시를 고정한 파일 20개 등 38개), 스크립트 신뢰 경계, 알리는 방법.
- **[docs/QUICKSTART.md](../../docs/QUICKSTART.md)**: Codex·Claude Code 설치, 확인, 검수 요청, `report-check.mjs` 도장·`--verify`, 업데이트, 제거를 한 쪽으로.
- README 251줄 → 145줄. docs/INSTALL.md 버전 표기 2.0.0.

## 확인된 것

- `git diff --stat v1.3.4 -- skills/joedesign` = `VERSION` 1개.
- `node --test tests/*.tests.mjs` 44/44, `python -B -m unittest discover -s tests` 142 OK(건너뜀 2, 기준선과 같음).
- part19 회귀 274개: R1~R6 지적 수 1.3.4와 같음, R7 바뀐 파일 0.
- `harness_cli.py version` → 2.0.0. 스테이징한 줄에 사용자 이름·메일·`C:` 사용자 폴더 0건.

## 확인되지 않은 것

- Claude Code 쪽 설치(수동 clone + junction)에서 스킬 발견·호출, `doctor`, Playwright 경로 테스트 2개(건너뜀), 실제 Codex 실행.
- 마크다운 링크의 GitHub 렌더링(로컬에서 경로 존재만 확인). CHANGELOG의 옛 `joedesign-harness` 링크 1개는 1.3.4 때부터 끊겨 있음.
- 남은 식별자 38개 파일과 git 이력(커밋 작성자 메일 포함)은 그대로입니다. 자세한 것은 SECURITY.md.

## 세션이 대신 내린 결정

1. "고정" 판정을 테스트 핀보다 넓게 잡아, 같은 저장소의 다른 기록이 sha256을 적어 둔 파일 17개도 가리지 않았습니다.
2. 스킬 본문(SKILL.md·references·templates)은 한 글자도 바꾸지 않았습니다(성능 누락 위험 제거).

기록: [evals/v2-release-20261119/report.md](report.md), [2.0 사전 조사](../v2-survey-20261119/report.md).
