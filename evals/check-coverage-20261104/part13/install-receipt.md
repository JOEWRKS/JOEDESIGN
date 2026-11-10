# 개인 설치 갱신 영수증 — JOEDESIGN 1.3.0 (2026-11-11)

- 저장소: main daf8cfe(1.3.0, 태그 v1.3.0). 사용자 승인("1.3.0 게시")을 부모 세션이 전달한 뒤 진행했다. 1.2.1(06573af) 대비 스킬 차이는 SKILL.md, VERSION, references/conformance.md, scripts/report-check.mjs, templates/DESIGN.md 다섯 파일이다.
- Codex 설치(`%USERPROFILE%\.codex\skills\joedesign`)
  - 사전 확인: 설치본이 1.2.1 소스(06573af)와 31파일 모두 같았다(__pycache__ 제외, 줄끝 무시).
  - 백업: 사용자 문서 폴더 `JOEDESIGN-backups/20261111-v1.3.0-daf8cfe/joedesign/`(47파일). 복사 뒤 전체 SHA-256이 일치했다(before-hashes.json).
  - 교체: 위 다섯 파일(changed-files.txt). 나머지 42파일은 해시가 그대로였다(after-hashes.json 대조).
  - 검증: 저장소 daf8cfe의 skills/joedesign 31파일과 바이트가 일치했다. `version` 1.3.0, `doctor` 종료 코드 0.
- Claude Code 설치(`D:\JOEWRKS\.claude\skills\joedesign`, `Get-Item .Target` = `D:\JOEWRKS\.local\joe-latest-20261029\JOEDESIGN\skills\joedesign` 정션)
  - 사전 상태: 클론 a9c0cd0, 작업 트리 깨끗함.
  - `git pull --ff-only`로 daf8cfe가 됐고 작업 트리는 깨끗하다. `version` 1.3.0, Codex 설치본과 31파일 내용이 일치했다(줄끝 무시).
- 복구 방법: 백업 폴더의 joedesign/를 `.codex\skills\joedesign`으로 되돌린 뒤 before-hashes.json과 대조한다. 클론은 `git -C <클론> checkout 06573af -- skills/joedesign` 또는 a9c0cd0으로 되돌린다.
- 게시 상태: 푸시(d078327, daf8cfe)와 태그 v1.3.0(daf8cfe)은 했다. GitHub Release 생성은 이 세션에서 권한 검사(공개 게시면 생성)에 막혔다. 릴리스 노트는 `evals/check-coverage-20261104/part13/release-notes-v1.3.0.md`에 준비했다.
- 한계: 새 채팅에서 지침이 실제로 전달되는지는 따로 확인하지 않았다.
