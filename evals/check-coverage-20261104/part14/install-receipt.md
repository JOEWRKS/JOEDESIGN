# 개인 설치 갱신 영수증 — JOEDESIGN 1.3.1 (2026-11-15)

- 저장소: main 7941c9b(1.3.1, 태그 v1.3.1, [GitHub Release 445437133](https://github.com/JOEWRKS/JOEDESIGN/releases/tag/v1.3.1), Latest). 사용자 승인("게시", 2026-11-15)을 부모 세션이 직접 받아 그 세션이 진행했다. 1.3.0(3a19237) 대비 스킬 차이는 SKILL.md, VERSION, references/conformance.md, scripts/report-check.mjs, templates/DESIGN.md 다섯 파일이다.
- Codex 설치(`%USERPROFILE%\.codex\skills\joedesign`)
  - 사전 확인: 설치본이 1.3.0 소스(3a19237)와 31파일 모두 같았다(__pycache__ 제외, 줄끝 무시).
  - 백업: 사용자 문서 폴더 `JOEDESIGN-backups/20261115-v1.3.1-7941c9b/joedesign/`(47파일). 복사 뒤 전체 SHA-256이 일치했다(before-hashes.json).
  - 교체: 위 다섯 파일(changed-files.txt). 나머지 42파일은 해시가 그대로였다(after-hashes.json 대조).
  - 검증: 저장소 7941c9b의 skills/joedesign 31파일과 바이트가 일치했다. `version` 1.3.1(종료 코드 0), `doctor` 종료 코드 0.
- Claude Code 설치(`D:\JOEWRKS\.claude\skills\joedesign`, 정션 대상 `D:\JOEWRKS\.local\joe-latest-20261029\JOEDESIGN\skills\joedesign`)
  - 사전 상태: 클론 3a19237, 작업 트리 깨끗함.
  - `git pull --ff-only`로 7941c9b가 됐고 작업 트리는 깨끗하다. `VERSION` 1.3.1.
- 복구 방법: 백업 폴더의 joedesign/를 `.codex\skills\joedesign`으로 되돌린 뒤 before-hashes.json과 대조한다. 클론은 `git -C <클론> checkout 3a19237 -- skills/joedesign` 또는 3a19237으로 되돌린다.
- 게시 상태: 푸시(7941c9b), 태그 v1.3.1(7941c9b), GitHub Release 모두 부모 세션이 만들었다. 릴리스 노트는 `release-notes-v1.3.1.md`.
- 한계: 새 채팅에서 지침이 실제로 전달되는지, 에이전트가 새 배치·표기를 따르는지는 확인하지 않았다(행동 시험 0회).
