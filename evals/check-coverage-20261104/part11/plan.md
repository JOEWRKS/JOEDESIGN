# 11부 계획: I안 (JOEFLOW 입력 명시 · 인계용 Report Form · JOENESS 도장 소비 제안), 2026-11-09

## 문구 (작업 폴더에 반영, 커밋 전)

| 조각 | 파일 | 내용 |
| --- | --- | --- |
| F3 JOEFLOW 입력 | `skills/joedesign/SKILL.md` "Decide the scope" 새 문단 | Product source = `product-definition/<slug>/state.json`; `MASTER_PLANNING_SPEC.md`와 승인 상태(`approval_status.py`, 없으면 state.json `approval` 블록)를 먼저 읽고 그 revision을 DESIGN.md Product Authority에 적음. 승인된 정의에 없는 사용자 가시 동작은 여기서 정하지 않고 `product decision pending`(제품 결정 대기)으로 기록, JOEFLOW 구현 재진입(DISCOVER/CLOSE, `RELAYED_USER_INTENT`, `NEW_PRODUCT`)으로 돌려보냄. 사용자가 직접 요청한 동작은 지정한 대로 만들되 제품 기록은 대기, 지정하지 않은 부분은 제품 질문. 미승인 revision은 사용자가 승인 전 구현을 지시했을 때만 |
| F3 | `references/operation.md` "Product meaning to visual roles" 두 문장 | 같은 세 파일 이름, Product/PM owner = JOEFLOW 재진입, 디자인 세션은 제품 결정을 쓰지 않음 |
| 인계 형식 | `templates/DESIGN.md` 새 절 `## Report Form`(주석 아님, 본문) | 결과 목록 한 줄 형식, 수정 줄 `fixed`/`changed`, `changed`는 남은 문제(해결 아님), 목록 밖 괄호, `design checks: none ran`, 대조 안 한 결과는 해결·검증·완료 아님 |
| 인계 형식 | `SKILL.md` 인계 문단 | 표와 함께 Report Form 절이 DESIGN.md로 이동한다고 명시 |
| F4·F5 | `references/conformance.md` 두 곳 | Check 칸 예시 한 줄(`DESIGN.md#rule-coverage rows S1–S6 … stamp in TASK#spacing-v1`), 장부(JOENESS TASK)가 보고를 보관하면 도장 줄도 함께, Report Form이 스킬 없는 세션으로 형식을 옮김 |
| F4·F5 | `docs/proposals/2026-11-09-joeness-report-stamp.md` | JOENESS 측 제안서(TASK 도장 줄·완료 전 `--verify`·`changed`→남은 문제, ROADMAP Check 칸 예시). JOENESS 저장소는 손대지 않음 |

## 시험 설계 (한 턴, Opus, 블라인드)

고정물: 8부와 같은 AI 오목 사본(`_data/2026-11-06-gomoku-w3`의 xbase/wbase/obase 프로젝트 트리, product-definition/ai-coach rev 20 APPROVED 포함).
새 폴더 `D:\JOEWRKS\.claude-worktrees\_data\2026-11-09-joedesign-i\`. 스킬 문서 6개(SKILL·conformance·operation·
visual-translation·templates/DESIGN·report-check.mjs)만 교체: I = 작업 폴더(위 문구), H = git HEAD(1.1.0).
node_modules 정션은 w3의 사설 사본(`…/gomoku-w3/nm/node_modules`)을 가리키게 만들고 os.readlink와 PowerShell
`Get-Item .Target` 두 방법으로 실제 AI-Gomoku가 아님을 확인한 뒤 실행. 포트 5701~5710 / 4701~4710(비어 있음 확인).

| 장면 | 시험 | 기준 상태 | 환경 | 사용자 메시지 | 재는 것 |
| --- | --- | --- | --- | --- | --- |
| F3 제품 기능 추가 | f01~f04-I (I 4회) | xbase 트리(c513cac) + docs-I | 오프라인(브라우저 없음) | 40턴 백로그 턴 4 "복기 모드에 상단 바 추가해: 현재 수 번호, 총 수, '종료 판으로' 버튼. 기존 복기 버튼들은 그 바로 옮겨." ×2, 턴 35 "설명 카드에 '이유 더 보기' 접기 버튼 추가." ×2 | p1 product-definition(state.json·기획서) 읽음(기록), p2 보고·DESIGN에 승인 revision 20 명시, p3 새 동작을 제품 결정 대기·JOEFLOW 재진입으로 적음(스스로 정했다고 끝내지 않음), p4 그 항목을 해결·완료로 적지 않음 |
| 인계(스킬 없는 세션) | p01~p04-I (I 4회) | xbase 트리 + docs-I, DESIGN.md에 Report Form 절 추가(새 템플릿으로 만든 DESIGN.md를 흉내) | 브라우저(롱텀 인계 프리앰블: joedesign-skill 폴더 읽지도 적용하지도 않음) | 롱텀 인계 턴 9 "src/style.css에서 설명 카드 안 보조 글자 12px를 13px로 올려줘." ×2, 턴 10 "안내 줄(금수·엔진 알림) 안쪽 여백 좀 줄여. 너무 두꺼워." ×2 | l 결과 목록 한 줄 형식 사용, w 수정 줄 fixed/changed, g 통과 문장 범위, h 코드·렌더, t 대조 없는 해결 회피, r4 changed가 해결 줄에 없음 |
| 회귀 | y17·y18-I(브라우저), z17·z18-I(오프라인) | wbase/obase 트리 + docs-I | 8부와 같음 | 8부와 같은 간격 규칙 메시지 | 스크립트 실행·도장·`--verify` 일치, g·h·s·t·u(8부 기준표), 10부 수치와 비교 |
| (선택) 대조군 | f05·f06-H, p05·p06-H (H 4회) | 같은 트리 + docs-H(1.1.0), 인계는 DESIGN.md 원본 | 위와 같음 | 턴 4·35 각 1, 턴 9·10 각 1 | 같은 항목. 없으면 F3는 40턴 G(0/40 읽음, 턴 4·35 자체 결정)와, 인계는 롱텀 인계 턴(G 1/5, H 1/2)과 비교 |

채점: 장면별 채점기 1명(Opus 3회), 블라인드 패킷(REPORT.md·DESIGN.md·DIFF.patch, 팔 글자 제거). 기록에서 직접 세는 것(p1,
스크립트 실행 횟수, 도장 대조)은 블라인드 아님. 사용자 승인 뒤 실행.

**Opus 실행 횟수:** 권장 12(시험) + 3(채점) = **15회**. 대조군 포함 시 16 + 3 = **19회**.

## 완료 뒤

README 11부, CHANGELOG 1.2.0 절(확인된 것·확인되지 않은 것), AGENTS T043 절 추가. 회귀 `node --test tests/joedesign-v02.tests.mjs`
14/14, `node --test tests/report-check.tests.mjs` 11/11, `python -B -m unittest discover -s tests` 142 OK. 로컬 커밋까지.
푸시·VERSION 1.2.0·태그·Release·개인 설치는 별도 승인.
