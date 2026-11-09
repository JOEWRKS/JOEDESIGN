# 연계 문서 대조 초안 (JOEDESIGN main de6eb3e vs JOENESS 1.2.0 / JOEFLOW v1.1.0, 2026-11-07)

읽은 문서: JOEDESIGN SKILL.md·conformance.md·impact.md, JOENESS SKILL.md·review-gate.md·impact-review.md·usage.md·assets/AGENTS.md·assets/DESIGN.md, JOEFLOW SKILL.md·figma-make-handoff.md.
확인 방법: 각 약속(한쪽이 "넘긴다/읽는다"고 한 것)을 상대 문서에서 찾고, 스크립트는 샘플 보고로 직접 실행.

## 발견(스크립트 직접 실행)
- F1 디자인 검사가 없는 턴: JOENESS 여섯 줄 보고만 있고 디자인 검사를 돌리지 않은 보고(백엔드·문서 턴)에 R1 "no results list"가 뜬다. SKILL은 "돌린 검사마다 한 줄"이라 0줄이 맞는데 스크립트는 1줄 이상을 요구. → 40턴에서 질문·보고 턴(20·24·28·32·36·38·40)이 어떻게 처리하는지 확인. 후보 수정: "design checks: none ran" 같은 명시 줄을 R1 충족으로 인정.
- F2 `changed` 수정이 JOENESS "해결" 줄에: "해결: 말풍선 패딩 수정" + 목록 줄 `changed`는 ok로 통과. JOENESS는 해결=확인된 수정만, JOEDESIGN은 "changed는 이슈 열림"이라 두 문서가 각자 맞지만 연결 규칙(changed는 남은 문제로)이 어느 쪽에도 없다. 후보: R4 "해결 줄의 수정 항목이 목록에서 changed면 지적".
- F2' 검사 샘플 b는 `fixed` 없이도 ok: 수정 줄의 대조 셀이 "대조 안 함"이고 결과가 changed라 규칙대로. 문제는 F2뿐.

## 발견(문서 대조)
- F3 JOEFLOW 입력 미지정: JOEDESIGN은 "Product source"라고만 하고 state.json·MASTER_PLANNING_SPEC.md·approval_status.py를 이름 짓지 않는다. JOEFLOW는 "구현 중 중대한 모호함 → DISCOVER/CLOSE 재진입, 구현이 product 결정을 만들지 않는다"고 하지만 JOEDESIGN 쪽에는 "제품 의미가 비면 코디네이터로 돌려보낸다"만 있고 재진입 경로·기록(RELAYED_USER_INTENT, NEW_PRODUCT 범위)이 없다. 40턴 백로그의 턴 4(복기 상단 바)·35(접기 버튼)는 제품 기능 추가라 이 경로가 실제로 쓰이는지 볼 수 있다(transcript에서 product-definition 읽기 여부 셈).
- F4 ROADMAP Check 칸 형식: conformance.md는 "완료 Check는 스크립트 이름이 아니라 규칙 검사 표를 가리킨다"고 하고 JOENESS는 "외부 전문 판정은 review-gate 명령을 Check 칸에"라고 한다. 하네스 없이 표만 쓰는 운영(이 시험 전부)에서 Check 칸에 무엇을 적는지 양쪽 다 예시가 없다. L-G ROADMAP CO2 Check 칸은 tsc·vitest·크기 나열로 시작(표 참조 없음).
- F5 report-check 결과는 JOENESS가 소비하지 않는다(보내기 전 형식 검사일 뿐). 문제는 아니나 "연결됐다"고 말하면 안 됨.
- F6 단독(Codex) 운영: node 없는 환경이면 "실행 못 했다"고 적는 규칙만 있음. 보고 절 형식이 없는 프로젝트에서도 결과 목록은 요구됨(의도대로).
- 겹침: 좁은 화면 정보 예산은 JOEFLOW(ux-state-taxonomy)와 JOEDESIGN(narrow-screen behavior) 둘 다 다룸. 누가 결정하는지 명시 없음(JOEFLOW는 제품 의미, JOEDESIGN은 시각 표현으로 읽히나 경계 문장 없음).

## 40턴에서 확인할 것
- 턴별 report-check 실행 수와 첫 실행 결과(script-usage.json).
- 디자인 검사 없는 턴의 처리(F1).
- `changed` 수정이 해결 줄에 간 횟수(F2).
- product-definition/ 읽기 턴 수, 턴 4·35에서 제품 범위 언급(F3).
- 인계 턴(9·10·21·22·31) 뒤 감사 턴(11·23·32)에서 표 상태 복구.

## 40턴 실행 중 발견(2026-11-08, 집계 전)
- F7 **검사한 글과 보낸 글이 다름**: 주 세션은 보고를 보내기 전 매번 스크립트를 돌렸지만(ok 41회), 돌린 파일은 "작업: …했다. 결과는 아래 결과 목록에 있다." 한두 줄과 결과 목록만 있는 뼈대(280~1,900자)였고, 실제로 보낸 보고(1,500~3,900자)는 그 뼈대를 다시 풀어 쓴 것이다. 41회 모두 뼈대가 보낸 글에 포함되지 않았고(ratio 0.23~0.64), 보낸 글을 지금 스크립트로 돌리면 주 세션 35턴 중 24턴에 지적이 남는다(R3 18턴, R1 9턴). 한 턴 시험(8부) 12건은 보낸 글이 그대로 ok였다. 즉 스크립트는 "파일"을 검사하고, 지시는 "그 텍스트를 보내라"인데, 긴 세션에서 에이전트는 검사용 요약본을 따로 만들었다. 수정 후보: 보낸 보고 자체를 파일로 남기게 하거나(보고 = 파일 내용), 하네스/JOENESS 쪽에서 보고 텍스트를 받아 검사하는 소비자를 두는 것.
- F1 재확인: 검사 없는 턴(3·8·24·25·28·32·36·40)은 스크립트를 돌리지 않고 목록 없이 보냈다. 스크립트를 돌렸다면 R1에 걸렸을 것이라 돌리지 않는 쪽을 택한 셈이다.
- F2 재확인: `changed` 수정이 "해결" 줄에 들어간 턴 3회(5·19·33). 세 번 모두 "확인 전이라 changed"라고 밝혀 적었지만 JOENESS 규칙(해결 = 확인된 수정)과는 어긋난다.
- F3 재확인: 40턴 동안 product-definition/·기획서 언급 0회(턴 4 복기 바, 35 이유 더 보기 모두 "배치는 제가 골랐다"로 처리, JOEFLOW 재진입 없음).
