# 검증 기록 읽는 법

설치 성공, 자동 검사, 실제 모델 행동, 시각 품질, 사용자 수락은 서로 다른 결과다.
1.0.0은 현재 지원 범위의 패키지 버전이며 기존 JSON 규격의 개정이나
모든 프로젝트의 품질 보장이 아니다. [1.0.0 검증·통합 기록](../evals/v1-release-candidate-20261013/README.md).

| 기록 | 확인한 범위 |
|---|---|
| [1.0.0 개인 설치](../evals/v1-personal-install-20261013/README.md) | 전체44파일 백업·2파일 갱신·30개 배포 파일 일치·실제 version/doctor; 전문 검수 호출 증거와 구분 |
| [F05 변경 영향·재사용](../evals/f05-impact-20261013/COMPLETION.md) | 검토된 DESIGN 추가, 기하 관찰 재사용, 생산·소비 연결과 설치 보존 |
| [실제 행동 시험](../evals/behavior-forward-20261010/README.md) | 원본을 제공한 신규 제작·국소 수정·확장 3과제; 조정 담당의 기준 검토 포함 |
| [디자인 준수 연결](../evals/design-conformance-20261010/README.md) | 필수 검사 누락·실패·오래된 근거 차단과 실제 생산·소비 실행 |
| [당시 운영 연결](../evals/design-conformance-20261010/operational.md) | 당시 개인 설치 전환과 지정 프로젝트 연결; 모든 프로젝트의 자동 활성화가 아님 |
| [단일 코어 통합](../evals/unified-core-20261009/README.md) | 하나의 운영 코어와 내부 실행기, 옛 두 패키지 원본 보존 |
| [대표 화면 먼저 검수](../evals/design-workflow-20261009/README.md) | 확장 전에 대표 화면을 관찰·검토하도록 한 보강 |

소스 회귀 명령:

```powershell
python -B -m unittest discover -s tests -v
node --test tests/joedesign-v02.tests.mjs
```

Python의 실제 브라우저 검사는 기존 Playwright/브라우저 경로 환경변수가 필요하다.
구체 환경은 실행 기록에 남긴다. Node v0.2 회귀는 보존된 과거 패키지·증거의
무결성을 확인하며 현재 1.0.0 모델의 자율 준수나 시각 품질을 새로 검증하지 않는다.
실행기 완료값 `REVIEW_COMPLETE_UNCERTIFIED`도 사용자 최종 승인과 다르다.

## 과거 설계와 실패 보존

- [v0.2 설계](specs/joedesign-v0.2-visual-translation.md)와 [당시 행동 증거](../fixtures/contract-cases/evidence/visual-translation-v02/README.md)
- [옛 Harness 설계](superpowers/specs/JOEDESIGN_UI_REVIEW_RACI_V0_1_DRAFT.md)와 [채택 판단](../evals/harness-v0.1/retention-decision.md)
- [실행 연동의 실패·수정](../evals/harness-execution-20261006/README.md), [병목 개선](../evals/harness-bottleneck-20261006/README.md)

예전 문서의 두 스킬 설치·동결·대기 지시는 해당 시점의 기록이다. 현재 운영은
[단일 코어](../skills/joedesign/SKILL.md)와 최신 승인 범위를 따른다. 실패·미채택 실험·
원래 캡처를 지우거나 새 패키지에 재결속하지 않는다.
