# JOEDESIGN 1.3.4 개인 설치 영수증 (2026-11-18)

- 승인: 사용자 "게시"(2026-11-18, 부모 세션이 직접 받음).
- 대상: `~/.codex/skills/joedesign` (Codex 개인 설치). 설치 전 상태: v1.3.3(e229704) 트리와 31/31 파일 해시 일치(줄끝 정규화), 불일치 0.
- 절차: 백업 → 바뀐 파일만 교체 → 검증. 스크립트는 1.3.3 때와 같은 precheck/apply 흐름(세션 scratchpad, 저장소 밖).
- 백업: `~/Documents/JOEDESIGN-backups/20261118-v1.3.4-cedcf9f/` — `joedesign/` 31개 파일 전체 복사, `before-hashes.json`·`after-hashes.json`·`changed-files.txt`. 백업 해시 = 설치 전 해시(검증 통과).
- 교체 4개: `VERSION`, `references/conformance.md`, `scripts/report-check.mjs`, `templates/DESIGN.md`. 나머지 27개 해시 변화 없음.
- 검증: 설치 트리 = 저장소 `skills/joedesign` (cedcf9f, v1.3.4) 바이트 단위 동일. `harness_cli.py version` → 1.3.4 (exit 0), `doctor` exit 0. 설치본 `report-check.mjs --verify`로 18부 r01 도장 보고 `stamp: match; text ok`.
- 저장소: 커밋 cedcf9f, 태그 v1.3.4, GitHub Release https://github.com/JOEWRKS/JOEDESIGN/releases/tag/v1.3.4.
