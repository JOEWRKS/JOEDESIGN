# JOEDESIGN 2.0.2 개인 설치 영수증 (2026-11-26)

- 승인: 사용자 "추천대로 게시"(2026-11-26, 부모 세션이 직접 받음). 하위 세션이 대신 내린 결정 6건 중 허용 오차만 "채널 ±8 그리고 대비 ±0.2"로 바꿨고(fe5fd59) 나머지는 확정.
- 대상: `~/.codex/skills/joedesign` (Codex 개인 설치). 설치 전 상태: v2.0.1(3d1f588) 트리와 31/31 파일 바이트 일치, 불일치 0, 추가 파일 0.
- 절차: 백업 → 바뀐 파일만 교체 → 검증. 스크립트는 2.0.1 때와 같은 precheck/apply 흐름(세션 scratchpad, 저장소 밖; 파일 바이트는 릴리스 커밋의 blob에서 읽음).
- 백업: `~/Documents/JOEDESIGN-backups/20261126-v2.0.2-59bede8/` — `joedesign/` 31개 파일 전체 복사, `before-hashes.json`·`after-hashes.json`·`changed-files.txt`. 백업 해시 = 설치 전 해시(검증 통과).
- 교체 8개: `SKILL.md`, `VERSION`, `references/conformance.md`, `scripts/capture.mjs`, `scripts/harness/execution.py`, `scripts/harness_cli.py`, `scripts/report-check.mjs`, `templates/DESIGN.md`. 추가 2개: `scripts/capture-cdp.mjs`, `scripts/sample-pixels.mjs`. 삭제 0. 나머지 23개 해시 변화 없음.
- 검증: 설치 트리 33개 파일 = 저장소 `skills/joedesign` (59bede8, v2.0.2) 바이트 단위 동일. `harness_cli.py version` → 2.0.2 (exit 0), `doctor` exit 0(`collector` 블록: route cdp, Chrome 일반 설치 경로, `CHROME_PATH` UNSET).
- 저장소: 커밋 59bede8, 태그 v2.0.2, GitHub Release https://github.com/JOEWRKS/JOEDESIGN/releases/tag/v2.0.2.
- Claude Code 쪽 클론 `.local/joe-latest-20261029/JOEDESIGN`은 같은 날 fast-forward(junction `joedesign`이 2.0.2를 가리킴).
- 확인하지 않은 것: 행동 시험(새 문구를 에이전트가 따르는지), 실제 새 대화에서의 스킬 호출.
