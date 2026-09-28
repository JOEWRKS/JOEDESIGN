# JOEDESIGN Design Harness v0.1 — 구현 보고

상태: **JOEDESIGN_DESIGN_HARNESS_V0_1_IMPLEMENTATION_NOT_READY**

실행 코어와 스킬 패키지는 구현했다. 전체 설계의 완료 조건 중 실제 browser 수집·
인증된 host receipt·fresh visual Critic 실행/보정·운영 품질 평가가 충족되지 않았으므로
전체 구현 완료나 production-ready를 선언하지 않는다.

Repository: D:/JOEWRKS/joedesign-harness-v01-worktree
Branch: codex/joedesign-harness-v01
Baseline: 893e0181f77e1af87cf9a651f291b6929e5109b0

## 실제 구현한 범위

| 영역 | 구현과 확인 |
|---|---|
| Public skill | joedesign-harness, 자체 포함 패키지와 임시 프로젝트 복사 실행 |
| Intent | 제품 요구/제약/정확한 target 검증. 제품 의미를 스타일로 추정하지 않음 |
| OMD | 로컬 DESIGN.md 메타데이터 인덱스, SHA256/출처, 후보 검색, UNKNOWN 보존 |
| Reference Lock | Primary 1/Secondary 최대 2, 축 owner 충돌·미관찰·누락 거부 |
| Synthesis | 콘텐츠/행동/제약→공간·반응형·모션 규칙→구현 대상→반증 조건의 연결 검증 |
| Scope/Craft | 공유 selector 경고, route/family 확대와 craft의 방향 변경 거부 |
| State/Evidence | 정확한 target/state/build/캡처 내용과 검수 연결, 기술 증거의 시각 증거 대체 차단 |
| Critic/User | 별도 입력 bundle, 컨텍스트·보정·정확한 승인 receipt 판정 인터페이스 |
| Repair | 구조 실패 즉시 재설계, 동일 원인 수리 반복 중지, 이력 보존과 인증된 해결 기록 |
| CLI | init/index/retrieve/doctor/bind/check/advance/bundle/guard/repair/handoff |

이 코드는 글자나 필드가 채워졌다는 이유로 좋은 디자인이라고 판정하지 않는다.
잘못된 구조를 의미적으로 알아보는 능력은 실제 렌더 검토와 사용자 평가로 확인해야 한다.

## 검증 결과

- `python -m unittest discover -s tests -v`: **61 PASS / 0 FAIL**, exit 0.
- `node --test tests/joedesign-v02.tests.mjs`: **14 PASS / 0 FAIL**, exit 0.
- Python compileall: exit 0.
- skill-creator `quick_validate.py` (UTF-8 모드): valid, exit 0.
- `git diff --check`: exit 0.
- 기존 `skills/joedesign/`: baseline 대비 diff 없음, 3개 파일 SHA256 동일.
- F1–F12: 대응 자동 회귀 테스트 통과. 시각 품질 테스트로 해석하지 않음.
- 실제 고정 OMD 문서 3개 인덱싱/검색: 성공. 시각 관찰/콘셉트 적합성은 미검증.
- CLI 통합: 합성 fixture의 단계 진행, 호스트 미연결 시 PROOF_COMPLETE 차단,
  미검증 handoff, 구조 실패 후 craft bundle 거부 확인.
- 독립 코드 검토: 중요한 결함 7개 발견, 재현 RED→수정 GREEN. 상세는 review-resolution.md.

초기 외부 package validator 실행은 Windows 기본 cp949 디코딩으로 실패했고,
`python -X utf8`로 재실행하여 통과했다. 제품 스크립트의 문자열 입출력은 UTF-8을 명시한다.
초기 test helper의 미구현 CLI stdout 파싱 오류도 assertion 기반 RED로 고쳐 재실행했다.
검토 수정 전의 11개 실패와 추가 해결 증거 종류 실패를 숨기지 않고 기록했다.

## 이전 OMD 실패에 대한 조치

사용자의 BIO/02 사례를 **합성 회귀 fixture**로 만들었다. 과거 화면을 새로 평가했다고
주장하지 않는다. 제품 연결이 없는 장식적 패널/라인, 빠진 interaction 축, 정지 이미지에서
관찰했다고 주장한 모션을 거부한다. 구조적 FAIL이면 첫 발견에서 craft/확장을 막는다.
현재 상태 보고도 같은 판정을 사용하므로 별도 handoff 경로로 완료를 우회할 수 없다.

## 남은 조건과 명확한 한계

1. **실제 host 연결 없음.** 현재 callable 도구에서 controller용 immutable execution/
   authenticated user-event receipt API를 찾지 못했다. Python CLI의 기본 HostVerifier는
   unavailable이다. 로컬 파일을 신뢰하는 대체 옵션을 만들지 않았다. 따라서 CLI는
   최종 APPROVED와 자동 확장을 허가하지 못한다. 이 경계를 충족하는 호스트 연결이 필요하다.
2. **브라우저 수집 자동 연결 없음.** 실제 프로젝트의 브라우저 도구로 캡처/동작을 관찰한 뒤
   수집 기록을 연결해야 한다. 이번 테스트의 render 파일은 명시적 합성 데이터다.
3. **실제 시각 Critic/보정과 품질 A/B 미실행.** 이번 독립 검토는 Python 코드 검토이며,
   새 스킬이 실제 화면 품질을 높였다는 증거가 아니다.
4. **강제 범위.** CLI의 단계·보고 출력은 제어하지만, 에이전트가 CLI를 우회해 직접 앱 코드를
   수정하거나 채팅에서 과장하는 행위까지 전역적으로 통제하지 않는다. 이를 막았다고 하지 않는다.
5. **입력 신뢰.** 의미 없는 rationale를 채운 경우는 문자열 검사만으로 판별할 수 없다.
   scope guard도 공급된 diff 영향 범위에 의존하며 완전한 CSS 분석기가 아니다.

개인 설치·원격 push·main 통합·BIO 작업물 수정은 하지 않았다. 이 브랜치와 소스는 보존한다.
추가 mandatory dependency는 Python stdlib 외에 없다. OMD corpus는 저장소에 복사하지 않았다.

## 구현 중 판단과 비용

- 다른 저장소에 연결된 앱 worktree 도구 대신 JOEDESIGN 전용 Git worktree 사용.
  비용: 앱의 관리 첨부가 아닌 로컬 경로로 추적한다.
- 현재 사용자의 Harness 구현 요청을 이전 v0.2의 새 public skill 금지보다 우선 적용.
  비용: 원래 코어와 추가 패키지의 검증 경계를 계속 구분해야 한다.
- 중복 JSON Schema/여러 forwarding script 대신 실행 validator와 단일 CLI 채택.
  비용: 일반 JSON Schema 도구와의 직접 호환 및 개별 스크립트 이름은 제공하지 않는다.
- 호스트 인증을 흉내 내지 않고 미연결로 유지. 비용: 실제 전체 흐름의 자동 완료가 아직 불가능하다.
- 개발용 스킬 셸 도구는 Git Bash로 실행. 초기 Python 실행 실패는 제품 변경을 일으키지 않았다.
- 코드 리뷰에서 제외한 사항과 판단 비용은 review-resolution.md에 기록했다. 미뤄둔 minor는 없다.

현재 적절한 결론: **실행 가능한 구현 후보와 회귀 방어는 확보했으며, 완성된 디자인 도구라는 판정은 보류한다.**
