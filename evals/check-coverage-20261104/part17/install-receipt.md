# 개인 설치 갱신 영수증 — JOEDESIGN 1.3.3 (2026-11-18)

- 저장소: main e229704(1.3.3, 태그 v1.3.3, [GitHub Release 449753644](https://github.com/JOEWRKS/JOEDESIGN/releases/tag/v1.3.3), Latest). 사용자 승인("게시(보정 포함)", 2026-11-18)을 부모 세션이 직접 받아 그 세션이 진행했다. 1.3.2(2777097) 대비 스킬 차이는 VERSION, references/conformance.md, scripts/report-check.mjs, templates/DESIGN.md 네 파일이다.
- Codex 설치(`%USERPROFILE%\.codex\skills\joedesign`)
  - 사전 확인: 설치본이 1.3.2 소스(태그 v1.3.2)와 31파일 모두 같았다(__pycache__ 제외, 줄끝 무시).
  - 백업: 사용자 문서 폴더 `JOEDESIGN-backups/20261118-v1.3.3-e229704/joedesign/`(31파일). 복사 뒤 전체 SHA-256이 일치했다(before-hashes.json).
  - 교체: 위 네 파일(changed-files.txt). 나머지 27파일은 해시가 그대로였다(after-hashes.json 대조).
  - 검증: 저장소 e229704의 skills/joedesign 31파일과 바이트가 일치했다. `version` 1.3.3(종료 코드 0), `doctor` 종료 코드 0.
- Claude Code 설치(`D:\JOEWRKS\.claude\skills\joedesign`, 정션 대상 `D:\JOEWRKS\.local\joe-latest-20261029\JOEDESIGN\skills\joedesign`)
  - `git pull --ff-only`로 e229704 이후 커밋이 됐고 작업 트리는 깨끗하다. `VERSION` 1.3.3.
- 복구 방법: 백업 폴더의 joedesign/를 `.codex\skills\joedesign`으로 되돌린 뒤 before-hashes.json과 대조한다. 클론은 `git -C <클론> checkout 2777097 -- skills/joedesign` 또는 2777097로 되돌린다.
- 게시 상태: 푸시(e229704), 태그 v1.3.3(e229704), GitHub Release 모두 부모 세션이 만들었다. 릴리스 노트는 `release-notes-v1.3.3.md`.
- 한계: 에이전트가 줄마다 오는 R7 지적을 보고 표기를 고치는지는 확인하지 않았다(행동 시험 0회). 정당한 섞임 보고의 실물 검증 없음.
