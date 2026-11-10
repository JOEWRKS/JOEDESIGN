# 13부 계획: 1.3.0 전후 표시 대조표 (K안), 2026-11-10

## 바뀐 것 (작업 폴더, 스키마·계약·CLI 그대로)

| 파일 | 내용 |
| --- | --- |
| `skills/joedesign/SKILL.md` "Decide the scope" | 기존 요소의 이동·겹침·숨김·병합은 먼저 DESIGN.md와 보고에 `## Display before/after`를 요소마다 두 줄(`before: element \| content shown \| route`, `after: ...`, 사라지면 `hidden`)로 적는다. 두 줄이 다르면 위 방식(제품 결정 대기·JOEFLOW 재진입)으로 기록, 같으면 디자인 결정 |
| 같은 파일, 뺀 문장 3개 | (1) 인계 문단 "The handoff tells that session to read DESIGN.md's Report Form section and report in that form."(12부에서 측정 안 함) (2) 6단계 "The script reads the form of the sentences, not whether a number is true."(설명문, 스크립트 머리 주석·conformance.md에 같은 말 있음) (3) "Review-only never gains write authority. The user need not prepare machine files or choose between a core and harness."(앞의 작업 종류 표 Review only 행과 중복, 측정 안 함). SKILL.md 14,216 → 14,212바이트 |
| `templates/DESIGN.md` Report Form | 같은 규칙 한 문단(인계 세션용) |
| `references/conformance.md` | report-check가 잡는 항목 목록에 R5 |
| `scripts/report-check.mjs` | R5(아래) |
| `tests/report-check.tests.mjs` | R5 테스트 5개(전체 16/16) |

R5: 보고 문장에 "이 작업이 옮겼다·겹쳤다·숨겼다·합쳤다"류 완료 동사가 있고(파일·토큰·검사·포커스·기준값·기존 규칙 설명 문장 제외) `before:`/`after:` 줄도 `display unchanged` 줄도 없으면 지적. 요소별로 짝지어 내용·경로 칸이 다르거나 한쪽이 없으면 `product decision pending`(부정문 "대기 없음" 제외) 줄이 없을 때 지적. before/after 줄은 R3 문장 검사에서 뺀다.

오탐 측정(기존 보고 306건, 블라인드 아님): R1~R4 결과 변화 0/306. 재배치 과제 보고 21건(11부 상단 바 5, 12부 a01~a12, 롱텀 턴 4 ×4) 21/21 감지. 그 밖 285건 중 R5가 걸린 것 16건: 기능 추가 중 실제 UI 이동 3(롱텀 턴 35), 빈 줄 숨김 4, 그 밖 9. 오탐 비용은 `display unchanged` 한 줄.

## 검증 설계

### (a) 한 턴 퇴행 게이트: K(1.3.0 후보) vs 1.2.1(게시본, 06573af 문서)

고정물: 11·12부 기준 저장소(xbase·pbase, 8부 wbase·obase)를 `--shared` 클론, 스킬 문서만 바꿔 넣음. node_modules 정션은 w3 사설 사본, 두 방법 확인.

| 장면 | 메시지 | 셀 | 회 |
| --- | --- | --- | --- |
| 재배치, 표시 바뀜 | 12부 r1(상단 바), r2(카드 겹치기) | 2종 × 2팔 × 4 | 16 |
| 재배치, 위치만 | 12부 r3 | 1종 × 2팔 × 4 | 8 |
| 제품 기능 추가 | 11부 턴 4(상단 바)·턴 35(접기 버튼) | 2종 × 2팔 × 3 | 12 |
| 스킬 없는 인계 | 12부 t9·t10 | 2종 × 2팔 × 3 | 12 |
| 기준표 회귀 | 8부 브라우저 y·오프라인 z | 2종 × 2팔 × 3 | 12 |
| 블라인드 채점 | 재배치·기능, 인계, 회귀 | 장면별 1 | 3 |
| 합계 | | | **63** |

재는 것: 재배치 효과(r1·r2 대기 기록 p, r3 오탐 n, before/after 줄, 스크립트 R5 지적→수정). 무퇴행 항목: state.json 읽기, 승인 rev 명시, 결과 목록 또는 none ran, `fixed`/`changed`, 도장·`--verify` 일치, 해결 줄 규칙(R4), Report Form 절 읽기, 스크립트 실행, 8부 기준표 b·c·f·g·h·s·t·u. 게이트: 어느 항목이든 K가 1.2.1보다 낮으면 기록에서 원인을 찾고, 바뀐 문구 때문이면 고쳐 그 셀을 다시 잰다. 못 고치면 게시하지 않는다.

### (b) 40턴 롱텀 재측정 ((a) 통과 뒤)

9부 하네스(backlog 40턴, 인계 턴 9·10·21·22·31, 함정 턴) 그대로, 새 고정물 L-J = L-B 기준 커밋 43344f3 + K 스킬 문서. 채점은 9부 G 40패킷과 K 40패킷을 섞어 같은 채점기 프롬프트로 10명(8패킷씩)이 함께 채점(채점기 변동을 같은 조건에서 비교). 라이브 대조 5회(턴 5·15·25·35·40, 내가 직접).

| 실행 | 회 |
| --- | --- |
| 주 세션 1(35턴 재개) | 1 |
| 인계 세션 1(5턴 재개) | 1 |
| 채점기 (G+K 80패킷 / 8) | 10 |
| 합계 | **12** (세션 기준; 턴 재개 포함 Opus 호출은 약 50) |

게이트: G 기준 h2 30/40, 8개 전부 21/40, 함정 전부, 도장 일치 전 턴, 스크립트 실행 전 주 턴 중 하나라도 떨어지면 게시하지 않는다(같은 채점기의 G 재채점과 비교).

총 Opus: (a) 63 + (b) 12 세션 = 75.

## 실행 결과(2026-11-11)

승인: "둘 다 승인 (75회)" → (a) 뒤 "13회 추가 후 40턴"(인계 팔당 6회 + 채점 1) → 40턴 첫 시도 무효 뒤 "처음부터 다시"(주 세션 +1). 총 89회 = (a) 시험 72·채점 4, (b) 무효 주 1·주 1·인계 1·채점 10.
(b) 채점은 원안의 5회가 아니라 G 40패킷 재채점을 함께 하려고 10회로 했다(승인 질문에 10회로 적음). 결과는 README 13부.
