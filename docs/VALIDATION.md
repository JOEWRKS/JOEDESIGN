# 검증 기록·판정 범위

## 핵심 요약

- 판정 구분: 설치 성공 / 자동 검사 / 실제 모델 행동 / 시각 품질 / 사용자 수락.
- 1.0.0 의미: 현재 지원 범위의 패키지 버전.
- 보장 제외: 기존 JSON 규격 개정, 모든 프로젝트의 품질 보장.
- 통합 근거: [1.0.0 검증·통합 기록](../evals/v1-release-candidate-20261013/README.md).

## 검증 근거

| 기록 | 확인한 범위 |
|---|---|
| [1.0.0 개인 설치](../evals/v1-personal-install-20261013/README.md) | 전체44파일 백업·2파일 갱신·30개 배포 파일 일치·실제 version/doctor; 전문 검수 호출 증거와 구분 |
| [F05 변경 영향·재사용](../evals/f05-impact-20261013/COMPLETION.md) | 검토된 DESIGN 추가, 기하 관찰 재사용, 생산·소비 연결과 설치 보존 |
| [실제 행동 시험](../evals/behavior-forward-20261010/README.md) | 원본을 제공한 신규 제작·국소 수정·확장 3과제; 조정 담당의 기준 검토 포함 |
| [디자인 준수 연결](../evals/design-conformance-20261010/README.md) | 필수 검사 누락·실패·오래된 근거 차단과 실제 생산·소비 실행 |
| [당시 운영 연결](../evals/design-conformance-20261010/operational.md) | 당시 개인 설치 전환과 지정 프로젝트 연결; 모든 프로젝트의 자동 활성화가 아님 |
| [단일 코어 통합](../evals/unified-core-20261009/README.md) | 하나의 운영 코어와 내부 실행기, 옛 두 패키지 원본 보존 |
| [대표 화면 먼저 검수](../evals/design-workflow-20261009/README.md) | 확장 전에 대표 화면을 관찰·검토하도록 한 보강 |

## 소스 회귀 검사

```powershell
python -B -m unittest discover -s tests -v
node --test tests/joedesign-v02.tests.mjs
```

- Python 실제 브라우저 검사: 기존 Playwright·브라우저 경로 환경변수 필요.
  구체 환경은 해당 실행 기록 참고.
- Node v0.2 회귀: 보존된 과거 패키지·증거의 무결성 확인.
  현재 1.0.0 모델의 자율 준수·시각 품질에 대한 새 검증과 구분.
- 실행기 완료값 `REVIEW_COMPLETE_UNCERTIFIED`: 사용자 최종 승인과 구분.

## 과거 설계·실패 보존

- [v0.2 설계](specs/joedesign-v0.2-visual-translation.md) 및 [당시 행동 증거](../fixtures/contract-cases/evidence/visual-translation-v02/README.md)
- [옛 Harness 설계](superpowers/specs/JOEDESIGN_UI_REVIEW_RACI_V0_1_DRAFT.md) 및 [채택 판단](../evals/harness-v0.1/retention-decision.md)
- [실행 연동의 실패·수정](../evals/harness-execution-20261006/README.md), [병목 개선](../evals/harness-bottleneck-20261006/README.md)

- 예전 두 스킬 설치·동결·대기 지시: 해당 시점의 기록으로 보존.
- 현재 운영 기준: [단일 코어](../skills/joedesign/SKILL.md) 및 최신 승인 범위.
- 실패·미채택 실험·원래 캡처: 삭제 또는 새 패키지로의 재결속 금지.
