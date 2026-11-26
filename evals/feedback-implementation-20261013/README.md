# 묶음 A F02 자료·교차검증 및 묶음 C F05 준비

2026-10-13. 사용자 구현/검증 지시는 Manager 채팅
`01a115f2-a9fd-7c81-930a-0e225906f843`의 사용자 메시지에서 직접 확인했다.
현재 JOEDESIGN 배정은 **F02 최소 계약·생산 예시·fixture 준비/교차검토**와
**F05 진입 계약·고정 시험·구현 위치 준비**다. F05 구현은 C 통지 후다.

## 현재 결과

- JOENESS의 `joeness.roadmap-review.v1` 최소 계약에 맞춰 합성 원천,
  디자인 관찰 조각, 원천에 연결한 통합 입력, 독립 기대값 13개를 준비했다.
- 현재 선택 자료는 `f02-fixtures-v3/<ID>/input.json`,
  `design-fragment.json`, `f02-expectations-v3.json`이다.
- 소스 후보 소비 CLI에 직접 넘겨 **13/13 의미 기대값 충족**을 확인했다.
  이 수는 제품 검사 PASS 수가 아니다. 양성은 scoped complete,
  음성은 반려/미상/상충/invalid 등의 올바른 보존·차단을 뜻한다.
- 최초 실패와 fixture 매핑 수정, 이전 소스/기대값은 모두 보존했다.
- JOEDESIGN 공개 패키지28파일은 HEAD/개인 설치와 동일하다. 새 패키지 기능이나
  설치 변경 없이 계약용 자료/검증 코드만 추가했다. 기존 gate/receipt/핀 미변경.
- Manager와 JOENESS에 자료·SHA·명령·한계를 전달했다. Manager 독립 재실행 및
  격리 설치/정식 생산소비 연결 결과는 그 담당의 후속 근거로 별도 판정한다.

## 계약과 생산 자료의 의미

`F02-CASES.md`는 소비기 실행 전에 고정한 의미 사례다. 각 fixture에는 다음이 있다:

- `sources/scope.json`, `authorization.json`: 합성 납품 범위/권한.
  Manifest UNAPPROVED와 데모 범위 마감 가능성을 구분한다.
- `sources/design-observations.json`: 관찰 claim 전체
  `{outcome_id,lane,status,targets}`. 정확한 JSON pointer/value와 source SHA로 연결한다.
  source FAIL을 정규화 PASS로 바꾸면 invalid가 되어야 한다.
- `sources/exact-acceptance.json`: 관찰과 분리된 합성 exact 수락/반려/부재.
  실제 사용자 메시지나 동작·렌더 증거를 창작하지 않는다.
- `targets/*.json`과 `outputs/*.json`: route/state/viewport/theme/locale·build·출력 대응.
  같은 output 파일명이더라도 target identity가 다르면 수락을 전이하지 않는다.
- `sources/mapping-review-v2.json` 또는 v3: 검토 내용을 보존한 합성 검토 자료와
  `{scope_id,status:CONFIRMED,mapping_sha256}` 결속. mapping hash는 input에서
  `mapping_review`만 뺀 뒤 객체 키 재귀정렬/배열순서 유지/compact UTF8 JSON의 SHA256.
  이 결속은 변경 탐지이며 실제 검토자 인증이나 의미 완전성 증명이 아니다.
- `design-fragment.json`: technical/visual/acceptance의 담당 관찰 조각.
  필수 여부, 납품 최종 판단, 제품 승인 원본을 JOEDESIGN이 새로 만들지 않는다.

현재/제외 구분은 scopeowner 원천에서 받는다. 과거 제외된 실패는 source와
`sources/excluded-history.json`에 보존하고 현재 required observations와 분리한다.
JOENESS 표시가 원천 시각 판단·반려를 바꾸거나 납품 범위를 자동으로 완화하지 않는다.

## 실행과 실패 이력

1. `prepare-f02.py`: 초기13개 fixture와 기대값 생성, 기존 디렉터리 덮어쓰기 거부.
2. `audit-f02.py`: 정확한 원천 인용/해시와 의도한 음성 입력 확인, exit0.
   `f02-fixture-audit.json`은 원천 결속 검사이며 소비/시각/사용자 수락 PASS가 아니다.
3. `adapt-f02-v2.py`: 합의한 current view·한계와 canonical mapping 결속 추가.
   최초 source/기대 의미는 보존했다.
4. `consumer-runs/source-r1/results.json`: 13중12 기대 충족, harness exit1.
   소비 CLI SHA `98e604e31979373b2910baa0c20614d4c48a81dc8f486623bf7182509cd80069`.
   P02에서 제외된 mobile의 과거 관찰까지 current observations에 실어
   소비기가 `OBSERVATION` invalid4건/exit2로 거부했다. 입력 매핑 오류였다.
5. `adapt-f02-v3.py`: P02/N06의 제외된 관찰만 history로 분리했다.
   필수/제외 scope·authorization·관찰/수락 source bytes와 기대 의미는 불변이다.
6. `consumer-runs/source-r2/results.json`: **13/13 기대 충족**, harness exit0.
   소비 CLI SHA `38dcfe1f264d1d7eca40303940524f405f6a9558ebfc7e1349898fe4a82ef308`.
   각 입력·source·target 파일 전후 불변, 실행 중 CLI 해시도 불변이다.
7. 담당이 r1/r2 사이 소비기를 수정했으므로 같은 소스에서 추가 대조했다.
   `source-r2/p02-v2-control.json`: 위38dc 소스에서 v2 P02는 계속 invalid4건/exit2,
   v3 P02는 complete/exit0. 소비 규칙 완화 대신 current/history 매핑을 고친 효과다.

실제 명령·exit·stdout/stderr·해시는 각 run에 보존했다. 실행 예:

```powershell
python -B evals/feedback-implementation-20261013/run-f02-consumer.py --cli D:/JOEWRKS/작업하네스/skills/joeness-setup/scripts/roadmap-review.mjs --run-id 새실행ID --expectations f02-expectations-v3.json
```

소비 소스가 바뀌면 그 해시와 변경 근거를 새 실행으로 남긴다. 기존 run을 덮지 않는다.
기대값은 소비기로 전달하지 않고 별도 평가기가 사용한다. `ready/blocked/unknown`
기대 분류는 제품 상태 enum을 새로 정의한 것이 아니며, 실제 소비기 결과의 납품 상태,
lane 값, finding kind, exit를 함께 확인한다.

## 보존·검증 범위

`preservation.json`: source HEAD `3f76319f6c8a5929c2f55dc47b3c0e4f6a825bdb`,
패키지28파일 HEAD/설치 동일, 앞선 읽기 전용 F05 재현에서 고정한 GEO24입력과
baseline 불변. GEO 문서/제품/배포, 타 도구 원본을 이 담당이 변경하지 않았다.

이번 변경은 source-bound fixture와 그 평가 스크립트다. 수정되지 않은 패키지 전체의
과거 Python130/Node14 검사를 새로 실행했다고 주장하지 않는다. 이번 실제 실행 근거는
원천 결속 검사와 JOENESS 소스 후보의 양성/음성13사례다. 설치본·실제 브라우저·새 문맥
모델 행동·사용자 승인·실사용 비용 개선을 이 실행으로 증명하지 않는다.

## F05 및 후속 경계

`F05-ENTRY.md`에 DESIGN 무관 절/주석부터 시작하는 최소 계약, P01/P02 및
N01~N12 고정 시험표, 기존 harness 내부 구현 위치를 준비했다. CSS 정밀성 미상은
fresh 유지. C 통지 전 영향 진단 구현·선택 재사용 활성화·자동 repin은 하지 않는다.

다음은 Manager 독립 검토에 따른 좁은 계약 보정과 묶음 A 소비 연결 확인이다.
개인 설치, 새 릴리스/태그, 커밋/푸시, GEO 마감 재개는 이번 자료 준비의 결과가 아니다.
