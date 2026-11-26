# 빠른 시작 (JOEDESIGN 2.0.2)

설치 → 확인 → 첫 검수 → 보고 검사 → 업데이트 → 제거. 명령은 Windows PowerShell 기준이다. 설치 스크립트는 없고, 아래 명령을 직접 실행한다.

## 1. 설치

먼저 저장소를 복제한다(공개 저장소라 GitHub 로그인은 필요 없다).

```powershell
git clone https://github.com/JOEWRKS/JOEDESIGN.git
cd JOEDESIGN
```

### 1a. Codex

[README 4절](../README.md#4-사용-방법)의 두 번째 PowerShell 블록을 복제한 폴더에서 실행한다. `skills/joedesign`을 `$CODEX_HOME/skills/joedesign`(기본 `%USERPROFILE%\.codex\skills\joedesign`)에 복사하고 `version`·`doctor`까지 실행한다. 대상 폴더가 이미 있으면 덮어쓰지 않고 멈춘다.

### 1b. Claude Code

이 일을 하는 스크립트는 없다. 깨끗한 복제본(작업하지 않는 복제본)을 하나 두고, Claude 스킬 폴더에서 그 복제본의 `skills/joedesign`으로 연결(junction)을 만든다.

```powershell
$JoeClone = (Resolve-Path '.').Path
New-Item -ItemType Directory -Path (Join-Path $env:USERPROFILE '.claude\skills') -Force | Out-Null
New-Item -ItemType Junction -Path (Join-Path $env:USERPROFILE '.claude\skills\joedesign') -Target (Join-Path $JoeClone 'skills\joedesign')
```

macOS·Linux는 `ln -s <복제본>/skills/joedesign ~/.claude/skills/joedesign`. 연결이므로 복제본을 지우거나 옮기면 설치도 사라진다.

## 2. 확인

```powershell
python -B <설치폴더>\scripts\harness_cli.py version
python -B <설치폴더>\scripts\harness_cli.py doctor
```

- `version`: `"version": "2.0.2"`과 실제 `SKILL.md` 경로가 나와야 한다(연결 설치는 복제본 쪽 경로로 나온다).
- `doctor`: 전문 스킬(impeccable, ui-ux-pro-max, web-design-guidelines 등)이 없으면 `UNAVAILABLE`과 **종료 코드 2가 정상**이다. 발견은 호출·검수 완료와 다르다.
- `doctor`의 기본 탐색 경로는 패키지 형제 폴더, `$CODEX_HOME/skills`(CODEX_HOME이 없으면 `~/.codex/skills`), `~/.agents/skills`, `~/.claude/skills`(2.0.2)다. 없는 전문 스킬은 `missing_specialists`에 이름과 대체 실행 방법(다른 설치본의 SKILL.md를 하위 에이전트가 읽어 적용, 없으면 `not run`)이 나온다.
- `doctor`의 `collector`: 브라우저 수집 경로. `route`가 `playwright`(프로젝트에 Playwright 패키지), `cdp`(설치된 Chrome·Edge를 DevTools 프로토콜로 사용, `capture-cdp.mjs`), `none` 중 하나다. 이 값은 종료 코드에 영향이 없다.
- `--skills-root`를 주면 기본 탐색 경로를 **대체**한다(추가가 아니다). 여러 경로를 함께 보려면 경로마다 반복한다. Claude Code 설치에서 Claude 스킬 폴더와 `~/.agents/skills`를 함께 보는 예:

```powershell
python -B <설치폴더>\scripts\harness_cli.py doctor --skills-root $env:USERPROFILE\.claude\skills --skills-root $env:USERPROFILE\.agents\skills
```

## 3. 첫 디자인 검수

새 대화에서 검수만 요청한다(화면을 고치지 말라고 적는다).

```text
$joedesign
이 프로젝트의 문의 페이지를 검수만 해줘. 화면과 코드는 고치지 마.
DESIGN.md와 내가 준 참고 화면 기준으로 PC·모바일을 확인하고,
문제 목록, 확인한 결과(범위와 대조 여부 포함), 확인하지 못한 점을 나눠서 알려줘.
```

DESIGN.md나 참고 화면이 아직 없으면 요청문에서 그 줄을 빼고 "기준 문서가 없다"고 적는다. 그 기준과의 비교는 보고에서 미확인으로 남는다(SKILL.md 1단계: 원본이 없으면 그에 기댄 작업은 미결).

Claude Code에서는 `$joedesign` 대신 스킬 이름(`joedesign`)을 요청에 적는다. 결과는 문제 목록이며 사용자 수락이 아니다.

## 4. 보고 검사와 도장

에이전트는 보고 초안을 파일로 쓰고 보내기 전에 검사한다. 사람이 직접 확인할 때도 같은 명령을 쓴다.

```powershell
node <설치폴더>\scripts\report-check.mjs REPORT.md
```

1. 지적이 있으면(종료 코드 1, 줄마다 보고 줄 번호) 고치고 다시 실행한다. 종료 코드 2는 사용법·읽기 오류.
2. 지적이 없으면 `report-check: ok <글자수> chars <해시8자>` 한 줄이 나온다. 이것이 도장이다.
3. 보낸 글은 검사한 본문 그대로 두고 **맨 끝 줄에 그 도장 줄**을 붙인다.
4. 받은 쪽은 보낸 글을 파일로 저장해 확인한다.

```powershell
node <설치폴더>\scripts\report-check.mjs --verify SENT.md
```

`stamp: match (...); text ok`면 도장 아래 본문이 검사한 것과 같다. `mismatch`·`missing`이면 종료 코드 1. 도장은 형식 검사 결과이지 숫자의 참을 보증하지 않는다.

제품 수용 기준(AC) 결과는 디자인 검사가 아니다. `AC:`로 시작하는 줄이나 AC 제목 아래에 쓰면 괄호 규칙(R3)을 받지 않는다. 제품 정의가 이미 정한 표시 변화는 after 줄 끝에 `decided in rev N DEC-xxx`를 붙이면 R5가 대기 표기를 요구하지 않는다.

### 캡처와 색 관측 (2.0.2, 선택)

Playwright가 없어도 설치된 Chrome·Edge로 전 화면 캡처를 찍는다(Node 22 이상, 로컬 미리보기 주소만).

```powershell
node <설치폴더>\scripts\capture-cdp.mjs --url http://localhost:5173/ --sizes 1024x768,360x640 --dpr 2 --out captures
```

색 규칙의 직접 관측은 그 캡처의 획 중앙 행 픽셀을 읽는다. 기록은 `median M, range a–b, n px` 형식이다.

```powershell
node <설치폴더>\scripts\sample-pixels.mjs captures\page-360x640@2x-full.png --region 200,236,128,76 --expect '#8A8A8A'
```

reduced-motion은 `--reduce-motion emulate`(미디어 기능 에뮬레이션)로 찍는다. 그게 안 되는 환경에서는 `--reduce-motion inject`(페이지 자체 reduce 규칙을 조건 없이 주입)로 찍고, 결과 줄을 `rendered (reduce injected)`로 적는다.

## 5. 업데이트

| 설치 방식 | 방법 |
|---|---|
| Codex(복사본) | 복제본에서 `git pull --ff-only` → 기존 `$CODEX_HOME/skills/joedesign`을 스킬 탐색 경로 **밖**으로 백업(예: `~/Documents/JOEDESIGN-backups/<날짜>/`) → 폴더 삭제 → README 블록 다시 실행. README 블록은 폴더가 있으면 멈추므로 그대로는 업데이트에 쓸 수 없다. 백업·해시 비교 명령: [설치 안내의 백업과 해시 비교](INSTALL.md#백업과-해시-비교) |
| Claude Code(연결) | 연결한 복제본에서 `git pull --ff-only`. 연결은 그대로 둔다 |

`git pull --ff-only`는 `main` 브랜치 복제본을 전제로 하고, 태그가 아닌 최신 `main`으로 간다. 특정 버전에 맞추거나 태그를 체크아웃한 복제본(detached HEAD)이면 대신 `git fetch --tags; git checkout v2.0.2`처럼 태그를 체크아웃한다.

업데이트 뒤 `version`을 다시 실행한다.

## 6. 제거

- Codex: `$CODEX_HOME/skills/joedesign` 폴더를 지운다(필요하면 먼저 백업).
- Claude Code: 연결만 지운다. `Remove-Item` 대신 `cmd /c rmdir "%USERPROFILE%\.claude\skills\joedesign"`를 쓰면 복제본 내용은 남는다.

관련: [README](../README.md) · [설치 안내](INSTALL.md) · [보안](../SECURITY.md) · [변경 이력](../CHANGELOG.md)
