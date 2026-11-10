# 개인 설치 갱신 영수증 — JOEDESIGN 1.2.1 (2026-11-10)

- 저장소: main 06573af(1.2.1). 사용자 승인("재배치 문구 빼고 게시")을 부모 세션이 전달한 뒤 진행. 1.2.0(6955f39) 대비 스킬 차이는 SKILL.md(인계 문장), VERSION, templates/DESIGN.md(Report Form 안내 줄) 세 파일이다.
- Codex 설치(`%USERPROFILE%\.codex\skills\joedesign`)
  - 사전 확인: 설치본이 1.2.0 소스(6955f39)와 차이 없음(__pycache__ 제외, 줄끝 무시).
  - 백업: 사용자 문서 폴더 `JOEDESIGN-backups/20261110-v1.2.1-edfc9e7/joedesign/`(47 파일, 복사 뒤 전체 SHA-256 일치 확인, before-hashes.json).
  - 교체: SKILL.md, VERSION, templates/DESIGN.md(changed-files.txt). 나머지 44 파일은 그대로(after-hashes.json 대조).
  - 검증: 저장소 06573af의 skills/joedesign과 바이트 일치(31 파일, __pycache__ 제외), `version` 1.2.1, `doctor` 종료코드 0.
- Claude Code 설치(`D:\JOEWRKS\.claude\skills\joedesign`, `Get-Item .Target` = `.local/joe-latest-20261029/JOEDESIGN/skills/joedesign` 정션): `git pull --ff-only`로 06573af. `version` 1.2.1, 작업 트리 깨끗함. Codex 설치본과 31 파일 내용 일치(이 클론은 core.autocrlf=true라 줄끝만 CRLF).
- 복구: 백업 폴더의 joedesign/를 `.codex\skills\joedesign`으로 되돌린 뒤 before-hashes.json과 대조.
- 사고와 정정: 첫 버전 커밋 edfc9e7에 다른 세션이 작업 폴더에서 고치던 `scripts/report-check.mjs`(R5 규칙, 미완성·미커밋)가 `git add -u`로 섞여 들어가 푸시됐고, Codex 설치에도 한때 교체됐다. 설치본의 그 파일은 백업(1.2.0)에서 되돌렸고, 저장소는 06573af에서 인덱스만으로 1.2.0 스크립트를 되돌려 푸시했다. 그 세션의 작업 트리 파일은 건드리지 않았다. 06573af를 내보낸 깨끗한 사본에서 회귀 14/14, 11/11, 142 OK(skipped=2).
- 한계: 새 채팅에서 지침이 전달되는지는 따로 확인하지 않았다. 태그 v1.2.1과 GitHub Release는 이 세션에서 권한 검사(공개 게시면 생성)에 막혀 만들지 못했다.
