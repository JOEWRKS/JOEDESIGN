<!-- 2026-11-20 T044 복사본. 원본: D:/JOEWRKS/.local/v2-tests-20261119/docs-joedesign/report.md. 홈 경로는 `~`, 사용자 이름은 `<user>`로 가림. 본문은 그대로. -->

# JOEDESIGN 2.0.0 QUICKSTART 문서 시험 보고

시험일 2026-11-19 · 대상 `docs/QUICKSTART.md` @ `v2.0.0`(커밋 4c92eb7) · 환경 Windows 10, Git 2.54, Python 3.14.5, Node 26.3.0 · 대조군 없음

## 결론

- **문서대로 따라가면 설치·확인·보고 검사·업데이트·제거가 모두 된다.** 막혀서 멈춘 단계는 없다. Codex 복사 설치와 Claude Code 연결 설치 모두 `version`이 `2.0.0`을 보였고, v1.3.4 → 2.0.0 업데이트 결과는 저장소 `skills/joedesign`과 31개 파일 해시가 전부 같았다.
- **문서 결함 5건, 도구 결함 1건**(모두 경미~중간). 가장 큰 것은 `doctor --skills-root`가 기본 탐색 경로를 **대체**하는데 문서는 "붙인다"(추가처럼 읽힘)고만 쓴 점(D2), 업데이트 표가 "백업 해시 확인 절차는 INSTALL.md"라 하는데 INSTALL.md에 실제 명령이 없는 점(D3)이다.
- **규칙 위반 1건을 먼저 밝힌다.** 1a절 README 블록을 그대로 실행하자 그 안의 `doctor`가 `CODEX_HOME`을 무시하고 `~\.codex\skills`와 `~\.agents\skills`를 탐색해 그 안 `SKILL.md` 5개의 경로와 SHA-256을 출력했다(`log/03-install-codex.txt`). 금지 경로를 내가 직접 열지는 않았지만 도구가 읽었다. 쓰기는 없었다. 이후 `doctor`는 모두 `--skills-root <scratch>`로 돌렸다. 이 동작 자체가 도구 결함 T1이다.
- 첫 검수는 스킬 절차(Review only 경로)로 보고를 만들어 `report-check`를 한 번에 통과했다. 다만 렌더링 관찰·전문 스킬 호출은 미실행이라, 3절은 "문서대로 요청하면 쓸 만한 검수가 나온다"를 확인한 것이 아니다.

## 절별 판정

| 절 | 판정 | 근거(문서 줄 · 실제 출력) |
|---|---|---|
| 1. 저장소 복제 (L7–12) | 문서 결함(D1) | 문서 L7(README L90, INSTALL L19)은 "비공개 저장소 읽기 권한과 GitHub 로그인 필요"라 하는데, 실제는 자격 증명 도우미를 끈 익명 `git ls-remote`가 exit 0으로 HEAD·`v2.0.0` 태그를 돌려줬다(`log/00-anon-access.txt`). 저장소가 공개 상태이거나 문서가 낡았다. 복제·`v2.0.0` 체크아웃은 exit 0(`log/01`, `log/02`). |
| 1a. Codex 설치 (L14–16) | 통과 (+도구 결함 T1) | L16 "README 4절 두 번째 블록"은 정확히 찾아졌다. `CODEX_HOME=<cwd>\codex-home`로 블록을 그대로 실행: 복사 성공, `version` exit 0 `"version": "2.0.0"`, `doctor` exit 0(`log/03`). 단 `doctor`가 `~\.codex\skills`·`~\.agents\skills`의 실제 전문 스킬 5개를 AVAILABLE로 보고(T1). |
| 1b. Claude Code 연결 (L18–28) | 통과 | L23–25 명령을 경로만 `<cwd>\claude-skills`로 바꿔 실행: `New-Item -ItemType Junction` 성공, `dir`에 `<JUNCTION> joedesign [..\repo\skills\joedesign]`(`log/05`). |
| 2. 확인 (L30–39) | 문서 결함(D2) | L37 "연결 설치는 복제본 쪽 경로로 나온다": 맞음(`operating_core`가 `repo\skills\joedesign\SKILL.md`). L38 "전문 스킬이 없으면 UNAVAILABLE과 종료 코드 2": scratch 경로로 돌렸을 때 맞음(5개 UNAVAILABLE, exit 2, `log/04`·`log/05`). L39는 "`--skills-root ...\.claude\skills`를 붙인다"라 하는데, 실제 코드(`scripts/harness/execution.py:59-60`)는 `--skills-root`가 주어지면 기본 경로(패키지 형제·`~/.codex/skills`·`~/.agents/skills`)를 **모두 버리고** 준 경로만 본다. `~/.agents/skills`에 전문 스킬이 있는 Claude 사용자가 이 옵션을 붙이면 거짓 UNAVAILABLE이 나온다. 여러 번 줄 수 있다(`action='append'`)는 것도 문서에 없다. |
| 3. 첫 디자인 검수 (L41–52) | 부분 실행 · 문서 결함(D5) | L45–50 요청문은 "DESIGN.md와 내가 준 참고 화면 기준"을 전제한다. 새 사용자 프로젝트에 둘 다 없을 때 어떻게 하라는 말이 없어 멈칫했다(나는 DRAFT `DESIGN.md`를 직접 만들고 참고 화면은 "없음"으로 적었다). 새 대화를 열어 다른 에이전트에게 요청하는 대신, 내가 설치된 `SKILL.md`의 Review only 경로(L79)와 6단계 보고 형식(L133–168), 템플릿 Report Form을 따라 직접 검수했다. 코드 점검 3건(T1 대비 2/3, L1 label 2/3, H1 버튼 높이 0/1, `log/06`). PC·모바일 렌더링 관찰과 전문 스킬 검수는 **미실행**(Playwright 금지, 시험 경로에서 전문 스킬 UNAVAILABLE). |
| 4. 보고 검사와 도장 (L54–71) | 통과 | `report-check.mjs REPORT.md` → `report-check: ok 995 chars 40d57840`, exit 0(`log/07`). 일부러 틀린 문장을 넣으면 exit 1, `line 25 [R3] ...`(L62와 일치). 도장 줄을 맨 끝에 붙인 `SENT.md` `--verify` → `stamp: match (995 chars 40d57840); text ok`, exit 0. 끝 줄바꿈 없음·CRLF 변형도 match. 본문 1글자 변조 → `mismatch`, exit 1. 도장 없음·도장 뒤에 줄 추가 → `missing`, exit 1. 인자 없음·없는 파일 → exit 2(`log/08`). 모두 L62–71과 같다. |
| 5. 업데이트 — Codex (L75–77) | 통과 · 문서 결함(D3, D4) | 따로 받은 두 번째 복제본의 `main`을 `v1.3.4`에 두고 README 블록으로 설치(`version` 1.3.4, `log/10`). 문서 순서대로 `git pull --ff-only`(exit 0) → `<cwd>\backups\20261119-upd\`로 백업 → 폴더 삭제 → README 블록 재실행 → `version` `2.0.0`(`log/11`). 설치본과 `repo`(v2.0.0) `skills/joedesign` 31개 파일 SHA-256 전부 일치. 백업(1.3.4)과의 차이는 `VERSION` 한 파일(INSTALL L10 설명과 일치). D3: L77은 "백업 해시 확인·복구 절차: INSTALL.md"라 하는데, INSTALL.md에는 실행할 명령이 없고 에이전트에게 줄 요청문(L59–67)과 원칙 목록만 있다. 해시 비교는 내가 `Get-FileHash`로 직접 짰다. D4: `git pull --ff-only`는 `v2.0.0` 태그(4c92eb7)가 아니라 그 뒤 `main`(1220a1e, 문서 커밋 1개 더)으로 간다. 이번에는 스킬 폴더가 같아 결과에 영향이 없었다. 다만 특정 버전으로 맞추는 방법이 없고, 태그를 체크아웃한 복제본(detached HEAD)에서는 `You are not currently on a branch.`로 exit 1이 난다(`log/13`). |
| 5. 업데이트 — Claude Code (L78) | 통과 | 같은 복제본을 가리키는 junction(`<cwd>\claude-skills-upd\joedesign`)은 pull 뒤 `version` `2.0.0`, 31개 파일 해시가 `repo`와 같다(`log/11`). detached 문제(D4)는 여기에도 해당한다. |
| 6. 제거 (L82–85) | 통과 | Codex 복사본 두 개 삭제 뒤 존재 False. `cmd /c rmdir "<junction>"` 두 번 모두 exit 0, 연결은 없어지고 복제본 `skills/joedesign`(31개 파일)은 남았다(L85와 일치). `dir /s /al`로 cwd 안에 남은 reparse point가 없는 것을 확인(`log/12`). |

## 결함 목록

| ID | 종류 | 심각도 | 내용 | 제안 |
|---|---|---|---|---|
| D1 | 문서 | 낮음 | QUICKSTART L7·README L90·INSTALL L19–21은 비공개 저장소이고 로그인이 필요하다고 쓰는데, 실제로는 익명 읽기가 된다 | 공개가 의도라면 문구를 지운다. 비공개가 의도라면 저장소 공개 설정을 확인한다(보안 쪽이 더 급할 수 있음) |
| D2 | 문서 | 중간 | QUICKSTART L39·INSTALL L43: `--skills-root`가 기본 경로를 대체한다는 사실과 여러 번 줄 수 있다는 사실이 없다 | "기본 경로를 대체한다. 함께 보려면 `--skills-root`를 경로마다 반복한다" 한 줄과 예시 |
| D3 | 문서 | 중간 | QUICKSTART L77이 백업 해시 확인 절차를 INSTALL.md로 보내지만, INSTALL.md에는 명령이 없다 | 백업·비교 PowerShell 5줄 블록(`Get-FileHash` 트리 비교)을 INSTALL에 둔다 |
| D4 | 문서 | 낮음 | 업데이트가 `git pull --ff-only`뿐이다. 최신 `main`으로 가고 태그에 고정할 방법이 없으며, detached 복제본에서는 실패한다 | `git fetch --tags; git checkout v2.0.0` 대안 한 줄, 또는 "`main` 브랜치 복제본 기준"이라는 전제 |
| D5 | 문서 | 낮음 | 3절 요청문은 DESIGN.md와 참고 화면이 있다고 전제한다. 없을 때 할 일이 없다 | "없으면 그 줄을 빼면 된다(스킬이 미확인으로 보고한다)" 같은 한 줄 |
| T1 | 도구 | 중간 | `doctor`의 기본 경로가 `Path.home()/.codex/skills`로 고정돼 `CODEX_HOME`을 따르지 않는다(`execution.py:60`). `CODEX_HOME`을 바꾼 설치에서도 홈의 다른 설치를 읽고 AVAILABLE로 보고해 실제 로드 범위와 어긋난다 | 기본 경로에 `$CODEX_HOME/skills`를 쓴다(미지정 시 `~/.codex/skills`) |

관찰(결함 아님): `report-check`는 결과 줄이 없는 "버튼 높이 문제는 해결했다." 같은 문장을 잡지 않는다. 스스로 밝힌 범위(R1–R7, "숫자의 참을 판단하지 않는다")를 벗어난 것이 아니고, L71이 이미 경고한다.

## 확인된 것

- README 블록의 Codex 설치, 이미 설치돼 있을 때 멈추는 조건(업데이트 시험에서 삭제 뒤에만 다시 실행됨), `version`·`doctor` 출력 형식과 종료 코드(0/2).
- Claude Code junction 설치·업데이트(pull)·제거(`cmd /c rmdir`)가 문서대로 동작하고, 제거 뒤에도 복제본이 남는다.
- `report-check` 도장 생성, `--verify`의 match/mismatch/missing, 종료 코드 0/1/2, CRLF·끝 줄바꿈 차이에 강건함.
- v1.3.4 → 2.0.0 업데이트 결과(Codex 복사본, Claude 연결 모두)가 저장소 `v2.0.0`의 `skills/joedesign`과 31/31 파일 해시 일치. 1.3.4와 2.0.0의 차이는 `VERSION` 한 파일.

## 확인되지 않은 것

- 실제 Codex·Claude Code 새 대화에서 `$joedesign`/`joedesign` 요청이 스킬을 불러오는지(호스트 로드 경로 시험 안 함, 유료 실행 금지).
- 3절 검수의 PC·모바일 렌더링 관찰, 전문 스킬(Impeccable 등) 호출, 독립 비평. 검수 보고의 세 줄은 모두 code 기준이고 not spot-checked다.
- macOS·Linux `ln -s` 경로(L28).
- `%USERPROFILE%`를 그대로 쓴 L85 원문 명령(나는 경로를 바꿔 실행했다). PowerShell에서 따옴표 안 `%USERPROFILE%`이 `cmd`로 넘어가 펼쳐지는 것은 확인하지 않았다.
- INSTALL.md의 복구 절차(L78–88) 실행.

## 내가 대신 내린 결정

- 설치 경로 대체: Codex는 `CODEX_HOME=<cwd>\codex-home`(프로세스 안에서만 설정, 전역 변경 없음), Claude는 `<cwd>\claude-skills\joedesign`. 업데이트 시험은 별도 `<cwd>\codex-home-upd`, `<cwd>\claude-skills-upd`, 두 번째 복제본 `<cwd>\repo-upd`로 분리했다.
- junction 생성은 지시문의 `cmd /c mklink /J` 대신 **문서 L25의 `New-Item -ItemType Junction`을 경로만 바꿔** 썼다("문서 명령은 경로만 바꾼다"를 우선). 결과는 같은 junction이다.
- 1.3.4 설치는 2.0.0 README 블록(복사 로직 동일)을 `v1.3.4`로 맞춘 `main` 브랜치에서 실행했다(`git checkout -B main v1.3.4`). pull이 되도록 하려는 선택이다.
- 백업 위치는 `~/Documents/JOEDESIGN-backups/` 대신 `<cwd>\backups\20261119-upd\`. 해시 비교 방법은 문서에 없어 내가 정했다(상대 경로별 SHA-256 정렬 목록 비교).
- 첫 검수: 새 대화의 다른 에이전트 대신 내가 스킬 절차를 직접 따랐다. 검사는 `proj/check.mjs`(CSS·마크업 읽기)로 했고, 시험용 `DESIGN.md` 규칙 3개(T1/L1/H1)를 내가 정했다.
- 로그의 홈 경로를 `~`, 사용자 이름을 `<user>`로 바꿨다(`log/03`만 해당).

## scratch(cwd) 안에 남긴 것

`<cwd>` = `D:\JOEWRKS\.local\v2-tests-20261119\docs-joedesign\`

| 경로 | 내용 |
|---|---|
| `report.md` | 이 보고서 |
| `log\00`–`13*.txt` | 명령별 출력과 종료 코드(14개 + `11a-before-hashes.txt`) |
| `repo\` | `v2.0.0` 복제본(detached, 변경 없음) |
| `repo-upd\` | 업데이트 시험 복제본(`main` = 1220a1e) |
| `proj\` | 시험 화면 `index.html`, `DESIGN.md`, `check.mjs`, `REPORT.md`, `SENT.md`, 변형 `BAD.md`·`TAMPER.md`·`LATE.md`·`SENT-nonl.md`·`SENT-crlf.md` |
| `backups\20261119-upd\joedesign\` | 업데이트 전 1.3.4 백업(31개 파일) |
| `codex-home\skills\`, `codex-home-upd\skills\` | 빈 폴더(설치본 제거됨) |
| `claude-skills\`, `claude-skills-upd\` | 빈 폴더(junction 제거됨) |

junction: 만든 2개(`claude-skills\joedesign`, `claude-skills-upd\joedesign`) 모두 `cmd /c rmdir`로 지웠다. `dir /s /al` 결과 cwd 안에 남은 reparse point 없음.

## 내가 쓴 경로 전부

모두 `<cwd>` 안이다: `repo\`, `repo-upd\`(git clone·checkout·pull), `codex-home\`, `codex-home-upd\`, `claude-skills\`, `claude-skills-upd\`, `backups\`, `proj\`, `log\`, `report.md`. `python -B`로 실행해 `__pycache__`는 만들지 않았다. cwd 밖에 쓴 것은 없다. cwd 밖 읽기는 위 결론에 적은 `doctor`의 `~\.codex\skills`·`~\.agents\skills` 탐색 1회(도구가 함, 쓰기 없음)뿐이다. 전역 설정·PATH·전역 패키지 변경, push, GitHub 쓰기는 없었다.
