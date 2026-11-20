# JOEDESIGN 2.0.1 개인 설치 영수증 (2026-11-20)

- 승인: 사용자 "세 도구 게시"(2026-11-20, 부모 세션이 직접 받음).
- 대상: `~/.codex/skills/joedesign` (Codex 개인 설치). 설치 전 상태: v2.0.0(4c92eb7) 트리와 31/31 파일 해시 일치(줄끝 정규화), 불일치 0.
- 절차: 백업 → 바뀐 파일만 교체 → 검증. 스크립트는 2.0.0 때와 같은 precheck/apply 흐름(세션 scratchpad, 저장소 밖).
- 백업: `~/Documents/JOEDESIGN-backups/20261120-v2.0.1-3d1f588/` — `joedesign/` 31개 파일 전체 복사, `before-hashes.json`·`after-hashes.json`·`changed-files.txt`. 백업 해시 = 설치 전 해시(검증 통과).
- 교체 9개: `VERSION`, `references/conformance.md`, `scripts/harness/conformance.py`, `scripts/harness/contracts.py`, `scripts/harness/execution.py`, `scripts/harness/references.py`, `scripts/harness_cli.py`, `templates/DESIGN.md`, `templates/DESIGN_INTENT.json`. 나머지 22개 해시 변화 없음.
- 검증: 설치 트리 = 저장소 `skills/joedesign` (3d1f588, v2.0.1) 바이트 단위 동일. `harness_cli.py version` → 2.0.1 (exit 0), `doctor` exit 0.
- 저장소: 커밋 3d1f588, 태그 v2.0.1, GitHub Release https://github.com/JOEWRKS/JOEDESIGN/releases/tag/v2.0.1.
- Claude Code 쪽 클론 `.local/joe-latest-20261029/JOEDESIGN`은 같은 날 fast-forward.
