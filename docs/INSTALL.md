# 설치·업데이트·복구

## 핵심 요약

| 항목 | 기준 |
|---|---|
| 설치 단위 | `skills/joedesign/` 전체 |
| 스킬 ID·실행 요청 | `joedesign` · `$joedesign` |
| 버전 원본 | [VERSION](../skills/joedesign/VERSION) |
| 1.0.0 변경 경계 | 기존 JSON schema/contract 버전 및 과거 증거의 의미 유지 |

## 최초 설치

- 설치 명령: [README의 PowerShell 명령](../README.md#4-사용-방법).
- 실행 위치: 복제한 저장소 폴더.
- 설치 위치: `$CODEX_HOME/skills/joedesign`.
  CODEX_HOME 미지정 시 `%USERPROFILE%/.codex/skills/joedesign`.
- 기존 `joedesign` 또는 `joedesign-harness` 발견 시: 덮어쓰기 없이 중단.
- 비공개 저장소 접근: 저장소 읽기 권한·GitHub 로그인 필요.
  `git clone` 인증 오류 시 Git Credential Manager의 GitHub 로그인 연결.
  2단계 인증은 GitHub 화면에서 직접 완료. 토큰의 채팅·저장소 파일 기입 금지.
- 설치 후 실행: Codex 새 대화에서 `$joedesign` 입력.
- 다른 운영체제: 전체 폴더의 해당 Codex 스킬 경로 복사 가능. 위 명령은 Windows 전용.
- 프로젝트별 설치: 해당 호스트의 실제 검색 경로 확인 후 적용.
  동일 이름의 복수 설치본은 활성 경로 확인 필요.

## 설치 확인·의존성

설치 폴더의 `scripts/harness_cli.py`를 **절대 경로로** 실행.

```text
python -B <설치폴더>/scripts/harness_cli.py version
python -B <설치폴더>/scripts/harness_cli.py doctor
```

| 항목 | 확인·준비 기준 |
|---|---|
| `version` | `1.0.0` 및 실제 운영지침 경로 확인 |
| `doctor` | 발견 경로·누락된 전문 스킬 확인. 준비 부족 시 종료코드 2는 정상 진단 결과 |
| 기본 전문 검수 | `impeccable`, `ui-ux-pro-max`, `web-design-guidelines` 필요 |
| 추가 전문 검수 | 모션·React 성능 검수에 해당 전문 스킬 준비 |
| 기본 검색 경로 | 패키지 형제 폴더, 사용자 `.codex/skills`, `.agents/skills` |
| 사용자 지정 경로 검사 | `doctor --skills-root <스킬들상위폴더>` |
| 자동 실행 | 기존 Codex 실행기·Python 3 필요 |
| 브라우저 수집 | 기존 Node·Playwright 패키지·브라우저 경로 추가 필요 |
| 진단 CLI | Python 표준 라이브러리 사용. pip 설치 불필요 |

- 전문 스킬: 실제 제공처의 설치 방법 적용. 이름만 같은 가짜 파일·폴더로 누락 대체 금지.
- `AVAILABLE`: 발견 결과. 실제 전문 스킬 호출·검수 완료와 구분.
- 실행 구성: [실행 설정](../skills/joedesign/references/execution.md).
- 검증 환경: [1.0.0 검증 기록](../evals/v1-release-candidate-20261013/README.md).

## 기존 설치 업데이트

Git 저장소 갱신과 설치 폴더 갱신은 별도 절차.
새 패키지의 버전·파일 해시·실제 활성 설치 경로 선확인.
담당 에이전트 전달용 요청 예시:

```text
이 JOEDESIGN 저장소의 검증된 패키지로 내 설치를 업데이트해줘.
실제로 검색되는 설치 경로와 현재 버전부터 확인해.
기존 joedesign, 남아 있다면 구 joedesign-harness를 전부 파일 목록과 해시로 기록하고
스킬 검색 경로 밖에 백업해. 백업의 전체 파일 해시가 맞는지 먼저 확인해.
검토한 패키지 전체와 최종 설치가 일치하도록 바꾸고 version/doctor를 실행해.
설정·다른 스킬·제품 파일은 보존하고, 실패 시 검증한 백업으로 원복해.
바뀐 파일과 미확인 의존성, 복구 경로를 보고해.
```

- 백업 위치 예시: 사용자 문서 폴더의 `JOEDESIGN-backups/<날짜와고유이름>/`.
- 백업 전제: 실제 스킬 검색 대상 밖인지 확인.
  `.codex/skills` 아래 옛 패키지의 이름 변경 보관 금지 — 중복 발견 가능.
- 보존 대상: 기존 생성 캐시·사용자 추가 파일. 임의 일괄 삭제 금지.
- 실패 대응: 복사 실패·입력 변경 시 중단. 고정한 백업과 전후 목록으로 복구.
- 구형 두 패키지 이전: 별도 공개 진입점 `joedesign-harness` 정리 필요.
  현재 운영은 내부 하네스를 포함한 `joedesign` 하나로 통합.
- 이미 이전한 설치: 과거 이전 작업의 재실행 불필요.

## 복구·이전 실행 자료

1. 새 실행 중단 및 변경 전 백업의 전체 파일 해시 검증.
2. 실패한 현재 설치 별도 보존. 사용자 추가 변경의 자동 덮어쓰기 금지.
3. 업데이트 전 기록한 경로로 백업 복원. 전체 해시·`version` 대조.
4. 기존 설정·다른 스킬·제품 파일 보존 확인. 새 대화에서 재개.

- CLI·캡처 경로: `joedesign/scripts/`.
- 구 runtime JSON: 외부 `skills.J` 재정의 제거 및 같은 패키지 내부 코어 사용.
- 이전 두 패키지 실행: 새 정책으로 재개 금지. 새 작업 후보 준비.
- 과거 자료: 예전 기준·receipt·캡처 원본 보존. 1.0.0의 새 행동 증거로 재표시 금지.

[예전 설치 전환 기록](../evals/design-conformance-20261010/operational.md) ·
[F05 백업·복구 검증](../evals/f05-impact-20261013/COMPLETION.md)
