# F02 생산 자료 — 구현 전 고정 의미 사례

Manager가 사용자 구현/검증 승인 원문을 인계했다. 현재 묶음 A에서 JOEDESIGN은
JOENESS가 소비할 최소 관찰/판정 자료와 fixture를 준비한다. 실제 납품 표시 및
제품 scope/승인 원본은 각 소유자에게 남긴다. 개인 설치와 기존 review gate는 미변경.

모든 fixture는 **합성**이다. 사용자 메시지·시각 수락·GEO QA 결과를 창작해서
실제 기록으로 넣지 않는다. 합성 수락/반려는 그 fixture의 source/target/output에만
묶고 인증된 사용자 근거라고 주장하지 않는다.

| ID | 최소 입력의 의미 | 소비 결과의 의무 |
|---|---|---|
| F02-P01 | 승인된 비런칭 demo scope의 필수 시각/기술 관찰 완료, 운영 범위 밖; Manifest UNAPPROVED | demo 납품 가능과 Manifest 미승인/운영 미검증을 함께 보존; 무한 유예/전체승인 모두 금지 |
| F02-N01 | 기술 PASS지만 필수 화면에 exact 사용자 REJECTED | 해당 scope 납품 차단, 거절 범위/근거 노출 |
| F02-N02 | 2필수 target 중 하나만 ACCEPTED, 나머지 수락 근거 없음 | 부분수락 보존, 미수락 target을 특정; 전체수락/전체반려로 축약 금지 |
| F02-N03 | 현재 필수 관찰 미수행 또는 근거 부족 | unknown; 임의 FAIL/반려 또는 완료로 바꾸지 않음 |
| F02-N04 | source/output hash 또는 target identity 불일치 | invalid/stale 범위 특정; 현재 증거로 소비 금지 |
| F02-N05 | 동일 exact target에 상충하는 현행 ACCEPTED/REJECTED 근거, 대체관계 없음 | conflict, 개수나 최신파일 mtime로 자동 승자 선정 금지 |
| F02-P02 | 과거 필수 화면이 현행 승인된 scope에서 제외; 과거 실패 보존 | 필수 잔여에서 제외하되 제외 출처/실패 이력 보존; 디자인 생산자가 필수 여부를 독단 결정하지 않음 |
| F02-N06 | 위 P02이나 현행 제외 권한/출처 없음 | unknown/conflict, 범위 밖 자술만으로 제외 금지 |
| F02-N07 | visual PASS이나 technical 미검증, 또는 전역 quality/acceptance가 빠짐 | 각 축 유지; geometry PASS를 다른 축 PASS/수락으로 복제하지 않음 |
| F02-N08 | 같은 output 이름이나 다른 route/state/viewport 또는 다른 scope revision | invalid/unknown으로 식별 실패 설명, 다른 target 수락 전이 금지 |
| F02-N09 | malformed/중복target·필수 ID 누락·tampered evidence | invalid; 누락 없는 것처럼 빈 배열·0건으로 보이지 않음 |

JOEDESIGN 출력에 담을 최소 의미: 평가 source/target/output identity, 기술 관찰,
시각 판정, exact 수락/반려/부재·부분 범위, 원천 증거와 적용 범위, 미상/범위 밖
상태의 근거. 필수/제외 여부는 제품 scope 또는 권한 있는 결정에서 받는다.
JOENESS 소비 형식과 교차검토 후 fixture를 직렬화한다. 이 표는 schema 정의 전의
독립 기대값이며 통합 소비 시험을 실행했다고 주장하지 않는다.
