# 개인 설치 갱신 영수증 — JOEDESIGN 1.2.0 (2026-11-09)

- 저장소: main a5bb705 (태그 v1.2.0, GitHub Release 게시). 사용자 승인("게시 진행") 뒤 진행.
- Codex 설치(`%USERPROFILE%\.codex\skills\joedesign`)
  - 사전 확인: 설치본이 1.1.0 소스(05656c8)와 차이 없음(__pycache__ 제외, 줄끝 무시).
  - 백업: 사용자 문서 폴더 `JOEDESIGN-backups/20261109-v1.2.0-a5bb705/joedesign/` (47 파일, 복사 뒤 전체 SHA-256 일치 확인; before-hashes.json).
  - 교체 5 파일: SKILL.md, VERSION, references/conformance.md, references/operation.md, templates/DESIGN.md (changed-files.txt). __pycache__ 등 나머지는 그대로.
  - 검증: 저장소 skills/joedesign과 바이트 일치(31 파일, __pycache__ 제외), `version` 1.2.0, `doctor` 종료코드 0. 교체 후 전체 해시 after-hashes.json.
- Claude Code 설치(`D:\JOEWRKS\.claude\skills\joedesign` → `.local/joe-latest-20261029/JOEDESIGN` 클론): `git pull --ff-only`로 main 최신.
- 복구: 백업 폴더의 joedesign/를 `.codex\skills\joedesign`으로 되돌린 뒤 before-hashes.json과 대조.
- 한계: 새 채팅에서 지침 전달은 따로 확인하지 않음.
- 기록 정정: 태그 v1.2.0의 CHANGELOG·README 11부에는 인계 2/6의 원인과 비교 수치(G 1/5, H 1/2는 목록 사용이 아닌 h2)를 잘못 적은 문장이 있어 다음 커밋에서 고쳤다. 스킬 패키지 바이트와는 무관하며 태그는 옮기지 않았다.
