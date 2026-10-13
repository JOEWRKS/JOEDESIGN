# JOEDESIGN

## 1. 이게 뭐냐

**어떻게 보이고 사용될지 만들고 확인한다.**

Codex에서 화면을 만들고 고칠 때 사용하는 디자인 스킬이다.
패키지 버전은 **1.0.0**이며, [VERSION](skills/joedesign/VERSION)에서 확인한다.

## 2. 언제 쓰냐

- 새 웹사이트나 앱의 화면을 만들 때.
- 기존 화면의 여백·글자·배치·모바일 사용성을 고칠 때.
- 만든 화면이 정한 디자인 기준에 맞는지 검수할 때.

## 3. 바로 시작하기

Windows PowerShell 기준이다. **Codex, Git, Python 3**가 필요하며, 비공개
저장소이므로 GitHub에서 이 저장소를 읽을 권한으로 로그인해야 한다.

처음 설치한다면 작업 폴더에서 실행한다. 이미 내려받았다면 그 저장소 폴더로
이동한 뒤 두 번째 블록부터 실행한다.

```powershell
git clone https://github.com/JOEWRKS/JOEDESIGN.git
cd JOEDESIGN
```

```powershell
$ErrorActionPreference = 'Stop'
$JoeCodexHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $env:USERPROFILE '.codex' }
$JoeSkills = Join-Path $JoeCodexHome 'skills'
$JoeTarget = Join-Path $JoeSkills 'joedesign'
if ((Test-Path -LiteralPath $JoeTarget) -or (Test-Path -LiteralPath (Join-Path $JoeSkills 'joedesign-harness'))) {
    throw '기존 설치가 있습니다. docs/INSTALL.md의 업데이트·복구 안내를 먼저 확인하세요.'
}
New-Item -ItemType Directory -Path $JoeSkills -Force | Out-Null
Copy-Item -LiteralPath '.\skills\joedesign' -Destination $JoeTarget -Recurse
python -B (Join-Path $JoeTarget 'scripts/harness_cli.py') version
python -B (Join-Path $JoeTarget 'scripts/harness_cli.py') doctor
```

`version`은 설치 버전을, `doctor`는 필요한 전문 스킬의 준비 상태를 보여준다.
`UNAVAILABLE`이면 [설치·의존성 안내](docs/INSTALL.md)를 확인한다.
설치 성공만으로 전문 검수까지 준비된 것은 아니다.

Codex에서 새 대화를 열고 다음 요청을 복사한다. 참고할 화면·자료가 있으면 함께 전달한다.

```text
$joedesign
이 프로젝트의 문의 페이지를 만들어줘.
기존 요구사항과 DESIGN.md, 내가 준 참고 화면부터 확인해.
대표 화면을 먼저 만들고 PC·모바일에서 검수한 다음 필요한 범위로 확장해.
마지막에는 변경점, 확인한 결과, 아직 확인하지 못한 점을 나눠서 알려줘.
```

업데이트·구형 설치 이전·복구는 [설치 안내](docs/INSTALL.md)를 따른다.
저장소를 갱신해도 이미 복사한 설치본은 자동으로 바뀌지 않는다.

## 4. 무엇을 받게 되냐

화면 구현, 프로젝트의 `DESIGN.md`에 정리한 디자인 기준, 검수 결과와 남은 문제를 받는다.
검수만 요청하면 수정 대신 문제 목록을 받는다. 아래는 보고 형식 예시이며 실제 검증 결과가 아니다.

```text
대상: 문의 페이지 PC·모바일
변경: 입력 순서, 오류 안내, 모바일 버튼 배치
확인: 입력 오류와 정상 전송 상태, 화면별 여백 기준
남음: 실제 이메일 도착 여부는 확인하지 못함
사용자 수락: 최종 화면 확인 필요
```

## 5. 다른 JOE 도구와 함께 쓰기

| 도구 | 역할 | 맡는 일 |
|---|---|---|
| [JOEFLOW](https://github.com/JOEWRKS/JOEFLOW) | 무엇을 만들지 확실하게 정한다. | 요구사항·규칙·예외·완료 기준 |
| **JOEDESIGN** | 어떻게 보이고 사용될지 만들고 확인한다. | 화면·시각 기준·디자인 검수 |
| [JOENESS](https://github.com/JOEWRKS/JOENESS) | 작업이 어디까지 됐고 무엇이 남았는지 관리한다. | 작업 순서·기록·재개·완료 근거 |

**JOENESS로 작업 정리 → JOEFLOW로 만들 것 확정 → JOEDESIGN으로 화면 제작·검수
→ 구현 담당이 개발 → 결과 검증 → JOENESS에 완료·잔여 기록**

JOENESS는 전 과정에서 사용한다. 필요한 도구만 단독으로 써도 된다.
화면 제작 중 UI 코드 구현을 함께 맡길 수도 있으며, 실제 개발 역할은 작업 범위에 맞게 정한다.

문의 폼을 만든다면 JOEFLOW의 **필수 입력·오류 조건·완료 기준**을 JOEDESIGN에
전달한다. JOEDESIGN은 화면을 만들고 **화면별 검수 근거·미확인 항목·사용자 수락
상태**를 구현 담당과 JOENESS에 넘긴다. 검수 결과를 자동으로 읽게 하려면
[생산·소비 연결 설정](skills/joedesign/references/conformance.md)이 필요하다.
세 도구를 설치하는 것만으로 자동 연결되거나 승인되지는 않는다.

## 6. 지원 범위·주의사항

- 화면 제작·확장·국소 수정·검수를 지원한다. 무엇을 만들지 정하는 일과 최종
  사용자 수락은 별도다. **1.0.0은 지원 범위의 패키지 버전이며 무결점 보장이 아니다.**
- 실제 전문 검수에는 Impeccable, UI UX Pro Max, web-design-guidelines 등 해당
  스킬이 필요하다. 자동 실행·브라우저 수집에는 기존 Codex 실행기, Node와
  Playwright·브라우저도 필요하며, 이 패키지가 대신 설치하지 않는다.
- 기존 검사 재사용은 독립 검토된 **DESIGN 끝의 무관한 주석·절 추가와 기하 검사**에
  한정한다. CSS·실행 파일·제공 빌드가 바뀌거나 의존성이 미상이면 새 관찰이 필요하다.
  전문 디자인 판단도 새 검토가 필요하다. [정확한 조건](skills/joedesign/references/impact.md).
- 누락·실패·오래된 근거를 통과나 수락으로 바꾸지 않는다. 로컬 파일의 해시와
  검토 기록은 사용자 신원 인증이나 파일·채팅 직접 수정의 우회 방지를 보장하지 않는다.

[설치·복구](docs/INSTALL.md) · [운영지침](skills/joedesign/SKILL.md) ·
[실행 설정](skills/joedesign/references/execution.md) · [변경 이력](CHANGELOG.md) ·
[검증 기록과 한계](docs/VALIDATION.md)
