# JOEDESIGN

## 하나의 운영 코어

**JOEDESIGN** 하나를 호출한다. [최상위 운영지침](skills/joedesign/SKILL.md)이
작업 범위와 단계를 정하고, 조정 담당자가 각 역할의 결과를 통합한다.
하네스는 그 안의 실행·증거 관리 기능이며 별도로 선택할 스킬이 아니다.

현재 작업본: **0.3.0-dev 통합 개발본**. 단일 버전 원본은
[VERSION](skills/joedesign/VERSION)이다. 이전 main 반영본 `0efacd8`은
코어 v0.2 + Harness v0.1이었다. 이번 main 통합 대상은 단일 코어와
디자인 준수 검증 보강이며, 정식 릴리스·사용자 시각 수용과는 별개다.
[전체 업데이트 내역](CHANGELOG.md)과 [통합 검증 기록](evals/unified-core-20261009/README.md)을 참조한다.

## 작업 흐름과 책임

신규 디자인과 중요한 확장은 **참조 결정 → 시각 번역 → 대표 화면 제작 →
전문 검수 → 확장 → 통합 관찰**로 진행한다. 승인된 관계 안의 국소 수정은
정확한 대상 진단·수정·관찰로 범위를 줄인다. 검토만 요청하면 쓰기 권한은 없다.
기존 색상·폰트를 썼다는 이유로 화면 구조 변경이 국소 수정이 되지는 않는다.

| 담당 | 책임 |
|---|---|
| 조정 담당자 A | 작업 범위, 역할 배정, 단계 전환, 통합 결과 |
| Product | 기능·정보·상태·행동의 의미와 필수 조건 |
| 시각 역할 J | 원본 해석, 구도·위계·시각 관계와 구현 비교 |
| 구현 담당 | 코드·상태·반응형 구현과 실제 결과 관찰 |
| 전문 검수 | Impeccable, UI UX Pro Max, web-design-guidelines와 필요한 성능 전문가 |
| 독립 Critic | 새 컨텍스트에서 현재 증거와 기준으로 진단 |
| 사용자 | 정확한 결과에 대한 최종 시각 수용 |

전문 역할은 같은 운영 코어 아래 배정된 단계만 수행한다. R → C1 → 필요 시
C2는 검토 순서이며 투표가 아니다. 대표 화면의 필수 실패·미확인은 의존하는
확장을 막는다. 확장 뒤에는 바뀐 빌드에서 기존 대표 화면까지 다시 확인한다.

## 패키지 사용과 이전 설치 마이그레이션

설치 단위는 `skills/joedesign/` 폴더 **전체**다. 이를 프로젝트 또는 개인의
스킬 경로에 `joedesign`으로 배치하고 `$joedesign` 또는 “JOEDESIGN으로 디자인해”로
호출한다. 필요한 전문 스킬은 실제로 사용 가능한 상태여야 한다.
저장소 문서·평가 자료는 설치할 필요가 없다.

기존의 `joedesign`과 `joedesign-harness`를 함께 설치한 환경에서는, 설치를 갱신할
때 두 구 폴더를 발견 경로 밖에 보존하고 통합 `joedesign` 하나로 교체한다.
폴더를 덧씌우기만 해 구 Harness 진입점을 남기지 않는다. 2026-10-10 후속 지시로
이 PC의 개인 설치는 통합 0.3.0-dev로 전환했다. 기존 개인·프로젝트 구 설치본은
발견 경로 밖에 보존했다. Git 갱신은 설치 갱신이 아니며, 다른 PC의 설치 상태를
뜻하지 않는다. [운영 연결 기록](evals/design-conformance-20261010/operational.md).

CLI와 캡처 경로는 이제 `joedesign/scripts/` 아래다. 기존 runtime JSON의
외부 `skills.J` 재정의는 제거한다. J는 항상 같은 패키지 내부를 사용한다.
옛 실행을 새 정책으로 재개하지 말고 기존 증거를 보존한 새 후보를 준비한다.

```powershell
python skills/joedesign/scripts/harness_cli.py version
python skills/joedesign/scripts/harness_cli.py doctor
python skills/joedesign/scripts/harness_cli.py --help
```

[실행 설정](skills/joedesign/references/execution.md)과
[계약·RACI 상세](skills/joedesign/references/operation.md)는 해당 작업에서 읽는다.
브라우저 수집과 역할 실행에는 이미 제공된 런타임을 사용하며 자동 설치하지 않는다.
직접 도구를 쓰거나 Git이 없는 프로젝트도 같은 운영 순서를 적용하되 CLI 실행으로
주장하지 않는다.

## 검증과 한계

```powershell
python -m unittest discover -s tests -v
node --test tests/joedesign-v02.tests.mjs
```

Python은 현재 실행·계약 정책과 단일 패키지 복사·역할 전달을 검사한다.
브라우저 통합 검사는 기존 Playwright/브라우저 경로를 환경변수로 제공했을 때 실행된다.
Node v0.2 검사는 [보존된 패키지](fixtures/package-history/pre-unification-20261009/manifest.json)에
과거 행동 증거가 그대로 연결되는지만 확인한다. 새 운영지침의 모델 준수나 디자인
품질 증거로 이전 결과를 재사용하지 않는다.

로컬 실행 완료는 `REVIEW_COMPLETE_UNCERTIFIED`이며 최종 APPROVED가 아니다.
인증된 호스트 receipt는 제공하지 않는다. 실행 순서·자동 검사·실제 모델 준수·
시각 품질·사용자 수용은 서로 다른 검증이다. 원본을 제공한 격리 과제 3건에서
실제 에이전트의 신규 제작·확장·국소 수정과 전문 검토를 확인했다.
신규54·수정32·확장249개 필수 검사가 통과했으며, 기준 검토 중 발견한 누락과
페이지 이동 시 상태 초기화의 수정 이력도 보존했다.
[행동 검증과 한계](evals/behavior-forward-20261010/README.md)를 참조한다.
조정 담당자의 개입 없는 준수 보장이나 실제 제품 전체의 시각 수용을 뜻하지 않는다.

2026-10-10 소스 보강은 DESIGN 규칙별 필수 대상·검사방법을 별도 기준점에
고정하고, 실제 렌더의 합산 여백과 전문 판정을 검사한다. `run`은 이제
`design_validation` 기준 파일과 독립적으로 보존한 SHA256이 필요하다.
`verify-design`은 비Git/직접 도구 관찰도 같은 기준으로 판정하여 JOENESS가
소비할 결과를 낸다. 누락·실패·오래된 근거는 관련 디자인 단계와 확장을 막는다.
[필드·실행·책임 경계](skills/joedesign/references/conformance.md)와
[실제 생산자→소비자 연결 검증](evals/design-conformance-20261010/README.md)을 참조한다.
개인 설치 전환과 지정 담당자의 GEO 검수 경로 활성화는 완료했다.
최종 범위와 한계는 [운영 연결 기록](evals/design-conformance-20261010/operational.md)을 참조한다.

## 보존한 설계와 증거

- [v0.2 설계](docs/specs/joedesign-v0.2-visual-translation.md)와 [당시 행동 증거](fixtures/contract-cases/evidence/visual-translation-v02/README.md)
- [이전 Harness 설계](docs/superpowers/specs/JOEDESIGN_UI_REVIEW_RACI_V0_1_DRAFT.md)와 [채택 판단](evals/harness-v0.1/retention-decision.md)
- [실행 연동의 실패·수정](evals/harness-execution-20261006/README.md), [병목 개선](evals/harness-bottleneck-20261006/README.md), [대표 화면 선검수 보강](evals/design-workflow-20261009/README.md)

이 기록은 각 시점의 소스와 범위를 설명한다. 과거 두 스킬 설치 안내와 동결
지시는 현재 운영 경로가 아니며, 실패·미채택 실험·과거 관찰은 그대로 보존한다.
