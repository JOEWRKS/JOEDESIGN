# TRACK: TrackB — JOEDESIGN Pure Core 합본 및 Freeze 준비

## 1. 목표

완료된 Bridge와 Composition 검증 보강을 하나의 검토 가능한 후보로 정리한다.

새 기능을 구현하지 않는다.
스킬을 변경하지 않는다.
기존 증거의 적용 범위와 한계를 보존한 상태로 Freeze 검토용 commit을 고정한다.

Program Lead 판정:
- Composition Core: CLOSED
- Composition 검증 보강: 수용
- Implementation Bridge v0.1: CLOSED — 기존 계약 및 Smoke F 범위
- Optical Core: DEFERRED
- Pure Core Freeze: 아직 미선언
- Competition readiness: 아직 미선언

## 2. 기준점

Repository:
JOEWRKS/JOEDESIGN

합본 기준:
4ae644128a71f514ea10564400d6dc70e70ae0fa

기준 tree:
77197aa9894de7c3691c28adf70df20b9fbf6fca

Composition 검증 보강 source:
6a499807826ca41a68616a0faa5d1f4007b60596

새 작업 branch:
codex/joedesign-v0.1-pure-core-freeze

정확한 합본 기준 commit에서 별도 worktree를 만든다.
같은 branch가 이미 있으면 상태를 확인하고, 강제 초기화하거나 덮어쓰지 않는다.

AGENTS.md와 아래 로드맵을 먼저 읽는다.
docs/roadmaps/JOEDESIGN_V0_1_IMPLEMENTATION_ROADMAP.md

과거 handoff의 구현·transplant 단계를 다시 실행하지 않는다.
이번 작업 범위는 본 지시문을 따른다.

## 3. 변경하지 않을 패키지

skills/joedesign/** 전체를 byte-exact로 유지한다.

SKILL.md SHA-256:
d73d1ce3067c6913abe5bd6d562bc87491f20e1b61c64a60cd9f522371715652

templates/DESIGN.md SHA-256:
4ac8586fad0a8f964d4ace550f2706af49df0403f3618a5214dd17b98ee1c237

agents/openai.yaml SHA-256:
c28a9f5e01c3ab39a5518c35d6cd6c41629f15edbadf696948339e58262e15c1

기존 tests, decisions.json, 응답 actions/reasons, Smoke 원본도 변경하지 않는다.

## 4. 실행 체크리스트

### A. 시작 상태 확인

- [ ] 기준 commit/tree와 작업공간 상태 확인
- [ ] 패키지 3개 파일 해시 확인
- [ ] 기존 8개 테스트 파일의 전체 suite 실행: 72 PASS / 0 FAIL
- [ ] 명령·종료 코드·실제 출력 보존

### B. Composition 보강 증거만 합본

다음 source commit에서:
6a499807826ca41a68616a0faa5d1f4007b60596

다음 디렉터리를 원본 bytes 그대로 가져온다:
fixtures/contract-cases/evidence/astra-smoke-v1/composition-validation-supplement-v1/

현재 review-evidence.json에는 해당 보강의 포인터와 판정 범위만 추가한다.

금지:
- Composition 보강 branch 전체 merge
- 그 branch의 SKILL.md 또는 observed.json으로 현재 파일 덮어쓰기
- 그 branch의 review-evidence.json 전체 덮어쓰기

검증 보강은 Composition 패키지 기준의 증거다.
Bridge 패키지 전체를 대상으로 새로 실행한 증거로 표현하지 않는다.
Source commit과 당시 skill hash를 그대로 보존한다.

### C. Current evidence의 단정 정리

대상:
fixtures/contract-cases/observed.json
fixtures/contract-cases/review-evidence.json

현재 요약에서 다음을 분명히 구분한다.

확인됨:
- 실제 runtime identity
- 실제 실행 로그와 응답 파일의 별도 해시
- 관찰된 고정 입력 readback
- 기존 응답과 복구된 응답의 JSON 내용 일치

확인되지 않음:
- 암호화된 요청·수정 메시지의 평문
- 정답 힌트나 이전 응답이 전달되지 않았다는 독립적 확인
- OS/filesystem 격리

상단 limitations, caseFormattingNote, 미제공 여부 필드가
미확인 사실을 현재 확인된 사실처럼 단정하지 않도록 정리한다.

과거 미제공 보고는 HISTORICALLY_REPORTED로 남긴다.
현재 독립 검증 상태는 UNVERIFIED로 구분한다.
필요하면 현재 필드는 null과 짧은 설명을 사용한다.
새 schema 체계나 검증 프레임워크를 만들지 않는다.

응답 actions/reasons, 실제 runtime ID, 원본 해시는 변경하지 않는다.
수정 전 current metadata는 증거 경로에 보존한다.
과거 provenance와 실패 기록은 소급 수정하지 않는다.

Smoke F 정정도 현재 요약에서 연결한다.
- before/after HTML은 byte-identical이 아님
- 확인된 차이는 마지막 LF 1바이트
- 별도 해시와 기존 정정 기록 유지
- status.attention.icon은 의도적 미정값 유지

### D. 로드맵과 재개 지점 갱신

수정 대상:
- AGENTS.md
- docs/roadmaps/JOEDESIGN_V0_1_IMPLEMENTATION_ROADMAP.md

현재 상태를 다음과 같이 맞춘다.
- Craft 및 Reference: CLOSED
- Composition 보강: 수용
- Bridge: CLOSED — 검증 범위와 한계 연결
- Optical: DEFERRED
- 현재 작업: Pure Core Freeze 검토 준비
- 다음 작업: Program Lead 최종 판정 후 TrackC 인계

기존 단계의 handoff는 역사 문서로 보존한다.
새로운 에이전트가 종료된 구현을 다시 시작하지 않도록 active pointer만 정리한다.
제품 역할, 디자인 철학, 스킬 동작은 바꾸지 않는다.

### E. Freeze 검토 기록 작성

기존 허용 경로 아래에 작은 기록만 추가한다.
fixtures/contract-cases/evidence/astra-smoke-v1/pure-core-freeze-v1/

최소 포함:
- 합본 기준과 가져온 증거의 source commit
- 최종 패키지 파일 목록·SHA-256
- 각 Core의 승인 근거 포인터
- current semantic 실행 ID·로그 해시·응답 해시
- 증거별 기준 버전·적용 범위·재사용 여부
- 현재 알려진 한계
- baseline/final suite 명령·종료 코드·전체 출력
- 변경 파일 목록

문구·패키지 검사 / 저장 semantic 응답 검사 / 실제 화면 검증을 구분한다.
이전 버전의 Smoke를 현재 패키지의 fresh 관찰로 일괄 승격하지 않는다.

이번 변경이 문서·증거뿐이면 새 semantic replay나 Smoke는 실행하지 않는다.
불필요한 평가를 추가하지 않는다.

### F. 최종 검증과 전달

- [ ] 전체 suite: 72 PASS / 0 FAIL
- [ ] 패키지 3개 파일 해시 불변
- [ ] 기존 테스트·scenario·응답 actions/reasons 불변
- [ ] public entrypoint 1
- [ ] competitor/runtime dependency 0
- [ ] vendor payload, DB bundle, automatic router 0
- [ ] BIO 신규 접근·작업 0
- [ ] 가져온 보강 자료의 원본 해시 일치
- [ ] 증거 포인터와 상대경로 유효
- [ ] active 문서 간 현재 단계·판정 범위 모순 없음
- [ ] 기존 실패·미확인 사항 보존

전체 suite 명령:

node --test tests/joedesign-contract.tests.mjs tests/joedesign-craft-core.tests.mjs tests/joedesign-typography-scale-core.tests.mjs tests/joedesign-reference-intelligence-core.tests.mjs tests/joedesign-color-contrast-core.tests.mjs tests/joedesign-imagery-focal-core.tests.mjs tests/joedesign-composition-anti-template-core.tests.mjs tests/joedesign-implementation-bridge.tests.mjs

확인된 결함이 있으면 정확한 범위만 보고한다.
통과시키려고 테스트나 런타임을 수정하지 않는다.

작업 branch에 commit/push하고 원격 readback을 수행한다.
최종 commit 자체의 SHA를 그 commit 안의 파일에 억지로 기록하지 않는다.
기록에는 source/package identity를, 최종 보고에는 결과 HEAD/tree를 남긴다.

## 5. 금지

- 새 기능·Core·도구·의존성 추가
- 스킬 변경 또는 기존 계약 완화
- 성공할 때까지 모델 재실행
- 역사 파일 전체 덮어쓰기
- 개인 설치·main·다른 branch 변경
- 강제 push·merge·PR·release tag 생성
- BIO 경쟁 실행
- 사용자 승인·경쟁 우위 추론

## 6. 최종 보고

TRACK: TrackB

STATUS:
JOEDESIGN_PURE_CORE_FREEZE_READY_FOR_PROGRAM_REVIEW
또는
JOEDESIGN_PURE_CORE_FREEZE_NOT_READY

Repository:
Branch:
Source baseline:
Composition supplement source:
Final HEAD / Tree:
Worktree / remote equality:

Baseline suite:
Final suite:
Shipped package unchanged:
Existing tests/scenarios/responses unchanged:
Supplement byte preservation:
Current metadata qualifications corrected:
Evidence reuse / version boundaries:
Active roadmap and AGENTS consistency:

Public entrypoint:
Competitor/runtime dependency:
BIO exposure:

Package SHA-256:
Changed files:
Freeze review record:
Known failures:
Unverified:

Pure Core Freezeとcompetition readiness는 Program Lead가 판정한다.
이번 보고에서 자체 선언하지 않는다.