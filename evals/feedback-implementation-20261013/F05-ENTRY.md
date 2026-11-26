# F05 묶음 C 진입 준비 — 구현 전 고정안

2026-10-13. Manager T035의 순서 A→B→C를 따른다. 지금은 계약·시험 설계와
구현 위치 준비이며 **진단 코드/선택 재사용/repin/설치 활성화 전**이다.
현재 gate와 receipt는 변경하지 않는다. F02 묶음 A와 병렬 원장을 만들지 않는다.

## 첫 지원 범위

DESIGN의 무관 주석/절 변경을 읽기 전용으로 대조하고, 이전 결과를 재사용할
**후보 근거**를 생산한다. v1에서 일반 selector/CSS 분석은 만들지 않는다.
CSS·런타임·폰트·자산 등 파일 내부 영향의 정밀성을 입증하지 못하면 fresh 유지.
이 지원 범위는 권한 있는 원본 변경을 자동으로 승인한다는 뜻이 아니다.

무관 절의 의미는 제목·ID나 문자열 일치만으로 결정하지 않는다. 이전/현재 원문,
해당 규칙의 적용 범위와 공통 예외를 대조한 독립 검토가 필요하다. 검토 없이
주석/절을 삭제한 정규화 hash를 새로운 권한 기준으로 사용하지 않는다.

## 최소 입출력 계약 초안

입력은 이전/현재의 project/scope identity, 별도 고정한 baseline+pin, authority
원문, rule/target/criterion과 각 적용범위, 실제 제공빌드 대응과 입력 목록,
이전 receipt/capture, 변경 영역과 독립 영향 검토 근거다. 현재 기대값을 생산자
receipt에서 역으로 취하지 않는다. 파일 읽기는 지정한 허용 루트 내부로 제한한다.

출력은 immutable한 비교 보고로 구성한다:

- 비교한 source/baseline/target/build/evidence의 정확한 식별과 전후 hash.
- check별 `reusable-candidate`, `rerun`, `unknown`, 이유, 원문/검토/실제입력 근거.
- 전체 비교의 `invalid`(형식·identity·누락/중복·변조), `conflict`(상충하는
  권한/검토), `unknown`(필요한 증거 부재)을 개별 원인과 구별.
- 필수 check 집합과 결과 집합의 동일성, 삭제/완화/대상 축소 및 필요한 승인.
- `reuse_authorized:false`, 변경하지 않은 기존 gate/receipt/pin의 식별.
- 미지원 CSS·조건부/늦은 의존성·서버 대응 한계 및 재관찰할 최소 알려진 범위.

`reusable-candidate`는 소비 허용이나 PASS가 아니다. 이후 Manager 검토와 공동
계약·실제 생산자→소비자 검증을 통과한 제한 전환만 JOENESS가 소비한다.
기존 `--previous-baseline` 공유 문맥 제약을 우회하는 자체 receipt는 만들지 않는다.
누락/중복/약화/위조가 있으면 최상위 후보 허용을 막고 근거를 보존한다.

## 고정 시험표

기대값은 분석기 구현 전에 고정한다. 각 행은 독립 합성 fixture와 원본불변 검사를
갖고, 사례에서 쓴 정확한 파일 hash/명령/exit/실패를 보존한다.

| ID | 변경/증거 | 기대 결과 |
|---|---|---|
| F05-P01 | DESIGN 주석만 변경; 모든 검사 의미/타깃/입력/제공빌드 동일; 독립 영향 검토 있음 | 전 검사 reusable-candidate, 재사용 권한 false; gate는 기존 stale 유지 |
| F05-P02 | 독립 검토된 무관 DESIGN 절 추가; 기존 적용규칙·공통예외·입력 불변 | 해당 검사 후보. 새 절 자체의 새 필수검사를 누락시키지 않음 |
| F05-N01 | P01 동일 변경이나 독립 검토 없음 | unknown, 자동 repin·수락·재사용 없음 |
| F05-N02 | 동일 ID의 규칙 완화/범위 축소/예외 추가 | 승인·기준 재검토 필요; 후보 불가 |
| F05-N03 | 이전 필수 check/target 삭제, 중복 또는 인위적으로 old 항목 생략 | coverage invalid; 빠진 항목을 비용 절감으로 세지 않음 |
| F05-N04 | CSS 주석 또는 selector 일부 변경 | v1 정밀판정 미지원, fresh; P01 성공을 CSS 정밀성으로 확대하지 않음 |
| F05-N05 | 공유 token, cascade/order, 상속·media조건 변경 | 영향 입력 검사 fresh; 이름/측정 selector가 같아도 후보 불가 |
| F05-N06 | lazy/conditional asset 또는 제공빌드 대응 불명 | unknown/fresh. 요청 목록만으로 의존 완전성 추정 금지 |
| F05-N07 | 캡처 byte 변조 또는 다른 route/state/viewport/theme/locale | integrity/identity invalid, 후보 불가 |
| F05-N08 | old 결과 FAIL/UNVERIFIED/사용자 반려, 또는 stale 판정 | 결과 유지; unchanged를 PASS/수락으로 승격하지 않음 |
| F05-N09 | 위조된 impact 자술, 다른 source hash에 대한 검토, 소비 pin과 불일치 | identity/검토결속 invalid; report가 자기 기대값을 정하지 않음 |
| F05-N10 | 일부만 검토·새 관찰 실패·중단 후 재개 | 완료된 독립 범위 보존, 나머지 unknown/rerun; 중복/누락 없이 인계 |
| F05-N11 | 실제 제공빌드는 변경됐으나 source 파일만 동일 | 이전 화면 증거로 새 빌드 주장 금지; fresh 또는 대응미상 |
| F05-N12 | 제품에서 읽은 기준/receipt/캡처를 테스트 이후 다시 읽음 | 원본 hash 불변; 임시 사본 밖 수정 없음 |

## 구현 위치와 책임

- C 착수 후 JOEDESIGN 기존 내부 `skills/joedesign/scripts/harness/`에
  영향 진단 모듈을 추가하고 `harness_cli.py`에 읽기 전용 명령을 연결하는 안.
  설명은 기존 `references/conformance.md`의 조건부 절에 두고 공개 스킬은 추가하지 않는다.
- 회귀는 기존 `tests/`의 별도 영향진단 시험에, 교차도구 계약 fixture는 이 평가
  폴더에 둔다. Python 표준 라이브러리와 기존 런타임 범위에서 준비한다.
- JOENESS가 소비 측 구현/검증을 소유한다. 어느 한쪽만 완성된 상태에서 활성화하지 않는다.
- source 회귀→Manager 독립 검토→격리 복사/실제 생산소비 연결→허용된 관리 설치
  순서. GEO 제품은 읽기 전용, 기존 마감 상태 유지.
- 비용 검증은 P01/P02에서 재관찰 수·호출·수동 판단·시간 감소와 음성 사례 차단을
  함께 확인한다. 전수 재관찰을 계속 요구하는 진단만으로 F05 해결이라고 하지 않는다.

이 문서는 구현 위치/시험 기대값 제안이며 새 schema의 일방적 확정이나 묶음 C
진입을 뜻하지 않는다. 상세 필드와 재사용 활성화는 JOENESS·Manager 교차검토 후 정한다.
