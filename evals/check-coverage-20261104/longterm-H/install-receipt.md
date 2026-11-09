# 개인 설치 갱신 영수증 — JOEDESIGN 1.1.0 (2026-11-09)

- 저장소: main a29753f (태그 v1.1.0, GitHub Release 게시). 사용자 위임("임자 하고 싶은 대로 해") 뒤 진행.
- Codex 설치(`%USERPROFILE%\.codex\skills\joedesign`)
  - 백업: 사용자 문서 폴더 `JOEDESIGN-backups/20261109-v1.1.0-a29753f/joedesign/` (47 파일, 복사 뒤 전체 SHA-256 일치 확인; before-hashes.json).
  - 교체 4 파일: SKILL.md, VERSION, references/conformance.md, scripts/report-check.mjs (changed-files.txt). __pycache__ 등 나머지는 그대로.
  - 검증: 저장소 skills/joedesign과 차이 없음(__pycache__ 제외), `version` 1.1.0, `doctor` 종료코드 0. 교체 후 전체 해시 after-hashes.json.
- Claude Code 설치(`D:\JOEWRKS\.claude\skills\joedesign` → `.local/joe-latest-20261029/JOEDESIGN` 클론): `git pull --ff-only`로 a29753f, 저장소와 내용 동일(줄끝만 CRLF).
- 복구: 백업 폴더의 joedesign/를 `.codex\skills\joedesign`으로 되돌린 뒤 before-hashes.json과 대조.
- 한계: 새 채팅에서 지침 전달은 따로 확인하지 않음. 전문 스킬(impeccable·ui-ux-pro-max·web-design-guidelines)은 doctor가 AVAILABLE로 보고.
