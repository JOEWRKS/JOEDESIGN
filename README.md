# JOEDESIGN

## 1. 핵심 요약

- **역할:** Codex 기반 화면 제작·구현·디자인 검수 지원.
- **운영:** 단일 코어 아래 단계별 역할 배정 및 결과 통합.
- **버전:** **1.0.0** — [VERSION](skills/joedesign/VERSION) 기준.
- **적용 대상:** 신규 화면 제작, 기존 화면 확장·수정, 디자인 기준 준수 검수.

## 2. 설계 목적

- 승인된 요구사항·참고 화면·디자인 기준과 실제 구현 결과의 차이 축소를 목적으로 설계.
- 대표 화면 제작 → PC·모바일 관찰 → 전문 검수 → 필요한 범위 확장에 집중.
- 반복적인 여백·글자·배치·상태 점검과 검수 기록 정리 지원.
- 제품 요구사항 결정과 최종 사용자 수락은 별도 책임으로 유지.

## 3. 주요 기능

| 기능 | 범위 | 산출물 |
|---|---|---|
| 화면 제작·구현 | 신규 웹사이트·앱 화면, 필요한 범위의 UI 코드 구현 | 화면 구현 및 PC·모바일 확인 결과 |
| 기존 화면 보강 | 여백·글자·배치·모바일 사용성 수정, 화면 확장 | 변경 화면 및 변경 근거 |
| 디자인 검수 | 정한 시각 기준과 실제 결과 대조 | 검수 근거·문제 목록·미확인 항목 |
| 기준 관리 | 프로젝트 디자인 기준 정리 | 프로젝트의 `DESIGN.md` |

검수만 요청한 경우: 화면 수정 대신 문제 목록 제공. 아래 내용은 보고 형식 예시이며 실제 검증 결과와 구분.

```text
대상: 문의 페이지 PC·모바일
변경: 입력 순서, 오류 안내, 모바일 버튼 배치
확인: 입력 오류와 정상 전송 상태, 화면별 여백 기준
남음: 실제 이메일 도착 여부는 확인하지 못함
사용자 수락: 최종 화면 확인 필요
```

## 4. 사용 방법

### 설치

- 실행 환경: Windows PowerShell, **Codex·Git·Python 3** 필요.
- 저장소 접근: 비공개 저장소 읽기 권한 및 GitHub 로그인 필요.
- 최초 설치: 작업 폴더에서 아래 복제 명령 실행.
- 기존 복제본: 저장소 폴더로 이동 후 두 번째 블록부터 실행.

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

| 확인 항목 | 판정 범위 |
|---|---|
| `version` | 실제 설치 버전 확인 |
| `doctor` | 필요한 전문 스킬의 발견·누락 상태 확인 |
| `UNAVAILABLE` | [설치·의존성 안내](docs/INSTALL.md)에 따른 준비 필요 |

설치 성공과 전문 검수 준비 상태의 별도 확인 필요.
업데이트·구형 설치 이전·복구: [설치 안내](docs/INSTALL.md) 참고.
저장소 갱신과 이미 복사한 개인 설치본 갱신은 별도 절차.

### 실행 요청

Codex 새 대화에 아래 요청 입력. 참고 화면·자료가 있는 경우 함께 전달.

```text
$joedesign
이 프로젝트의 문의 페이지를 만들어줘.
기존 요구사항과 DESIGN.md, 내가 준 참고 화면부터 확인해.
대표 화면을 먼저 만들고 PC·모바일에서 검수한 다음 필요한 범위로 확장해.
마지막에는 변경점, 확인한 결과, 아직 확인하지 못한 점을 나눠서 알려줘.
```

## 5. 도구 간 연결

| 도구 | 역할 |
|---|---|
| [JOEFLOW](https://github.com/JOEWRKS/JOEFLOW) | 요구사항·규칙·예외·완료 기준 확정 |
| **JOEDESIGN** | 화면 제작·시각 기준 수립·디자인 검수 |
| [JOENESS](https://github.com/JOEWRKS/JOENESS) | 작업 순서·진행 상태·완료 근거 관리 |

**JOENESS 작업 정리 → JOEFLOW 요구사항 확정 → JOEDESIGN 화면 제작·검수
→ 구현 담당 개발 → 결과 검증 → JOENESS 완료·잔여 기록**

- JOENESS: 전 과정의 작업 상태 관리.
- 단독 사용: 필요한 도구만 선택 사용 가능.
- 구현 역할: 화면 제작 중 UI 코드 구현 병행 가능. 실제 역할은 작업 범위에 따라 배정.
- 문의 폼 인계 예시: JOEFLOW의 **필수 입력·오류 조건·완료 기준**을 JOEDESIGN에 전달.
  JOEDESIGN의 **화면별 검수 근거·미확인 항목·사용자 수락 상태**를 구현 담당과 JOENESS에 전달.
- 검수 결과 자동 소비: [생산·소비 연결 설정](skills/joedesign/references/conformance.md) 필요.
  세 도구 설치만으로 자동 연결·승인 불가.

## 6. 한계

- 지원 범위: 화면 제작·확장·국소 수정·검수. 제품 요구사항 결정·최종 사용자 수락은 별도.
  **1.0.0은 지원 범위의 패키지 버전. 무결점 보장과 구분.**
- 전문 검수 의존성: Impeccable, UI UX Pro Max, web-design-guidelines 등 해당 스킬 필요.
  자동 실행·브라우저 수집: 기존 Codex 실행기, Node, Playwright·브라우저 필요.
  해당 도구의 자동 설치는 패키지 지원 범위 외.
- 기존 검사 재사용: 독립 검토된 **DESIGN 끝의 무관한 주석·절 추가와 기하 검사**에 한정.
  CSS·실행 파일·제공 빌드 변경 또는 미상 의존성은 새 관찰 필요.
  전문 디자인 판단은 새 검토 필요. [정확한 조건](skills/joedesign/references/impact.md).
- 누락·실패·오래된 근거의 통과·수락 처리 금지.
  로컬 해시·검토 기록의 사용자 신원 인증 및 파일·채팅 직접 수정 우회 방지 보장 불가.

[설치·복구](docs/INSTALL.md) · [운영지침](skills/joedesign/SKILL.md) ·
[실행 설정](skills/joedesign/references/execution.md) · [변경 이력](CHANGELOG.md) ·
[검증 기록과 한계](docs/VALIDATION.md)
