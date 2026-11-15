# 개인 설치 갱신 영수증 — JOEDESIGN 1.3.2 (2026-11-15)

- 저장소: main 2777097(1.3.2, 태그 v1.3.2, [GitHub Release 446112653](https://github.com/JOEWRKS/JOEDESIGN/releases/tag/v1.3.2), Latest). 사용자 승인("둘 다 게시", 2026-11-15)을 부모 세션이 직접 받아 그 세션이 진행했다. 1.3.1(7941c9b) 대비 스킬 차이는 VERSION, scripts/report-check.mjs, templates/DESIGN.md 세 파일이다.
- Codex 설치(`%USERPROFILE%\.codex\skills\joedesign`)
  - 사전 확인: 설치본이 1.3.1 소스(태그 v1.3.1)와 31파일 모두 같았다(__pycache__ 제외, 줄끝 무시).
  - 백업: 사용자 문서 폴더 `JOEDESIGN-backups/20261115-v1.3.2-2777097/joedesign/`(31파일). 복사 뒤 전체 SHA-256이 일치했다(before-hashes.json).
  - 교체: 위 세 파일(changed-files.txt). 나머지 28파일은 해시가 그대로였다(after-hashes.json 대조).
  - 검증: 저장소 2777097의 skills/joedesign 31파일과 바이트가 일치했다. `version` 1.3.2(종료 코드 0), `doctor` 종료 코드 0.
- Claude Code 설치(`D:\JOEWRKS\.claude\skills\joedesign`, 정션 대상 `D:\JOEWRKS\.local\joe-latest-20261029\JOEDESIGN\skills\joedesign`)
  - 사전 상태: 클론 c9f668f, 작업 트리 깨끗함.
  - `git pull --ff-only`로 2777097이 됐고 작업 트리는 깨끗하다. `VERSION` 1.3.2.
- 복구 방법: 백업 폴더의 joedesign/를 `.codex\skills\joedesign`으로 되돌린 뒤 before-hashes.json과 대조한다. 클론은 `git -C <클론> checkout 7941c9b -- skills/joedesign` 또는 7941c9b로 되돌린다.
- 게시 상태: 푸시(2777097), 태그 v1.3.2(2777097), GitHub Release 모두 부모 세션이 만들었다. 릴리스 노트는 `release-notes-v1.3.2.md`.
- 한계: 에이전트가 R6a/R6b 지적을 보고 배치를 고치는지는 확인하지 않았다(행동 시험 0회). 기존 evals 보고 106개는 새 지적을 받지만 다시 도장 찍지 않았다.
