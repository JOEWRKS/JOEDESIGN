# JOEDESIGN

[English](#english) | [한국어](#korean)

<a name="english"></a>

**English**

## 1. Summary

- **Role:** UI creation, implementation, and design review in Codex and Claude Code.
- **Operation:** One operating core, with stage-specific role assignments and integrated results.
- **Version:** **2.0.2** — defined in [VERSION](skills/joedesign/VERSION). Per-version changes: [CHANGELOG (Korean)](CHANGELOG.md).
- **Use cases:** New UI creation, existing UI extensions and repairs, and design conformance review.

## 2. Design Purpose

- Reduce gaps between approved requirements, reference screens, design standards, and actual implementation.
- Representative screen → desktop/mobile observation → specialist review → scoped expansion.
- Product requirements and final user acceptance stay separate responsibilities.

## 3. Key Features

| Feature | Output |
|---|---|
| UI creation and implementation | Implemented screens and desktop/mobile checks |
| Existing UI improvements | Updated screens and change rationale |
| Design review (review-only requests get an issue list, no screen changes) | Review evidence, issues, and unverified items |
| Standards management | Project `DESIGN.md` |

## 4. Usage

- Install, first review, report check and update: [Quickstart (Korean)](docs/QUICKSTART.md).
- Codex install block: [Korean section 4](#4-사용-방법) (same commands). Updates and recovery: [installation guide (Korean)](docs/INSTALL.md).
- Request: start a new conversation with `$joedesign` and the task, for example "Build a contact page; check requirements, DESIGN.md and my reference screens first; finish with changes, verified results and unverified items."

## 5. Tool Integration

| Tool | Role |
|---|---|
| [JOEFLOW](https://github.com/JOEWRKS/JOEFLOW) | Requirements, rules, exceptions, and acceptance criteria |
| **JOEDESIGN** | UI creation, visual standards, and design review |
| [JOENESS](https://github.com/JOEWRKS/JOENESS) | Task sequence, progress, and completion evidence |

Each tool works on its own. Automated consumption of review results needs the [producer/consumer configuration](skills/joedesign/references/conformance.md); installing all three does not by itself connect or approve anything.

## 6. Limitations

- **2.0.0 identifies the package's supported scope, not a guarantee of defect-free results.**
- Specialist review needs skills such as Impeccable, UI UX Pro Max and web-design-guidelines; automated runs need an existing Codex executor; browser capture needs Node and an installed Chrome or Edge (Playwright is used when the project already has it). None are installed by the package.
- Reuse of earlier checks is narrow: [exact conditions](skills/joedesign/references/impact.md). Missing, failed or stale evidence is never promoted to a pass.

[Quickstart](docs/QUICKSTART.md) · [Security](SECURITY.md) · [Installation](docs/INSTALL.md) · [Operating instructions](skills/joedesign/SKILL.md) ·
[Execution setup](skills/joedesign/references/execution.md) · [Changelog](CHANGELOG.md) · [Validation](docs/VALIDATION.md)

---

<a name="korean"></a>

**한국어**

## 1. 핵심 요약

- **역할:** Codex·Claude Code에서 화면 제작·구현·디자인 검수 지원.
- **운영:** 단일 코어 아래 단계별 역할 배정 및 결과 통합.
- **버전:** **2.0.2** — [VERSION](skills/joedesign/VERSION) 기준. 버전별 변경은 [변경 이력](CHANGELOG.md) 참고.
- **적용 대상:** 신규 화면 제작, 기존 화면 확장·수정, 디자인 기준 준수 검수.

## 2. 설계 목적

- 승인된 요구사항·참고 화면·디자인 기준과 실제 구현 결과의 차이 축소.
- 대표 화면 제작 → PC·모바일 관찰 → 전문 검수 → 필요한 범위 확장.
- 제품 요구사항 결정과 최종 사용자 수락은 별도 책임으로 유지.

## 3. 주요 기능

| 기능 | 산출물 |
|---|---|
| 화면 제작·구현 | 화면 구현 및 PC·모바일 확인 결과 |
| 기존 화면 보강 | 변경 화면 및 변경 근거 |
| 디자인 검수(검수만 요청하면 화면 수정 없이 문제 목록) | 검수 근거·문제 목록·미확인 항목 |
| 기준 관리 | 프로젝트의 `DESIGN.md` |

## 4. 사용 방법

처음 쓰는 경우: [빠른 시작](docs/QUICKSTART.md)(설치·확인·첫 검수·보고 검사·업데이트·제거).

### 설치 (Codex, Windows PowerShell)

- 필요: Codex·Git·Python 3. 공개 저장소라 GitHub 로그인 불필요.
- 기존 복제본이 있으면 저장소 폴더로 이동 후 두 번째 블록부터 실행.
- Claude Code 설치: [빠른 시작](docs/QUICKSTART.md) 1b.

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

- `version`: 실제 설치 버전. `doctor`: 전문 스킬 발견·누락. 전문 스킬이 없으면 `UNAVAILABLE`과 종료 코드 2가 정상.
- 이 블록은 기존 설치가 있으면 멈춤. 업데이트·구형 설치 이전·복구: [설치 안내](docs/INSTALL.md).

### 실행 요청

새 대화에 아래처럼 입력. 참고 화면·자료가 있으면 함께 전달.

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

각 도구는 단독으로도 사용 가능. 검수 결과 자동 소비는 [생산·소비 연결 설정](skills/joedesign/references/conformance.md) 필요. 세 도구 설치만으로 자동 연결·승인 불가.

## 6. 한계

- **2.0.0은 지원 범위의 패키지 버전. 무결점 보장과 구분.**
- 전문 검수에는 Impeccable, UI UX Pro Max, web-design-guidelines 등, 자동 실행에는 기존 Codex 실행기, 브라우저 수집에는 Node와 설치된 Chrome·Edge 필요(프로젝트에 Playwright가 있으면 그것을 씀). 패키지가 설치하지 않음.
- 기존 검사 재사용은 좁게 한정: [정확한 조건](skills/joedesign/references/impact.md). 누락·실패·오래된 근거의 통과 처리 금지.

[빠른 시작](docs/QUICKSTART.md) · [보안](SECURITY.md) · [설치·복구](docs/INSTALL.md) · [운영지침](skills/joedesign/SKILL.md) ·
[실행 설정](skills/joedesign/references/execution.md) · [변경 이력](CHANGELOG.md) · [검증 기록과 한계](docs/VALIDATION.md)
