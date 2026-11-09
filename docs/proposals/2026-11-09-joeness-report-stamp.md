# JOENESS 제안: 보고 도장 소비와 ROADMAP Check 칸 형식 (JOEDESIGN 1.2.0, 2026-11-09)

대상: JOENESS `skills/joeness-setup`(SKILL.md "User guidance and reports"·"Roadmap and suitability check",
`assets/TASK.md`, `references/review-gate.md`). 이 문서는 JOEDESIGN 쪽에서 쓴 제안이며 JOENESS 저장소는
고치지 않았다. 근거는 JOEDESIGN `evals/check-coverage-20261104/longterm-G/audit-integration.md`의 F4·F5.

## 배경

JOEDESIGN 1.1.0의 보고는 보내기 전에 `scripts/report-check.mjs`를 거쳐 `report-check: ok <chars> chars <sha8>`
도장 줄로 끝난다(글자 수와 SHA-256 앞 8자리). `--verify`는 보낸 글에서 도장을 다시 계산해 대조한다.
지금은 이 도장을 아무도 받지 않는다(F5): 보내는 쪽의 형식 검사일 뿐이고, 40턴 시험에서는 검사한 뼈대와
보낸 글이 달랐던 사례가 41/41회였다(10턴 H안에서 8/8 일치로 고쳐짐). JOENESS가 도장을 기록하고 대조하면
"검사한 글 = 보낸 글 = 기록된 글"이 세 번째 자리에서 닫힌다.

ROADMAP Check 칸은 JOEDESIGN이 "규칙 검사 표를 가리킨다"고 하고 JOENESS는 "외부 전문 판정은 review-gate 명령을
적는다"고 하지만, 하네스 없이 표만 쓰는 운영에서 Check 칸에 무엇을 적는지 예시가 양쪽에 없었다(F4). 40턴
시험의 CO2 Check 칸은 tsc·vitest·크기 나열로 시작했고 표를 가리키지 않았다.

## 제안 1: TASK 기록에 도장 줄, 완료 판정 전 `--verify`

`assets/TASK.md` 항목에 한 줄을 더한다:

```
Report stamp: <report-check: ok N chars sha8, or none ran / not stamped>
```

- 디자인 검사가 있는 작업의 TASK 항목은 보낸 보고의 도장 줄을 그대로 적는다. 보고 원문은 TASK가 가리키는
  파일(예: `work/reports/<date>-<id>.md`)에 도장 줄까지 저장한다. 검사 없는 턴은 `none ran`.
- 완료 판정(ROADMAP 항목을 complete로 바꾸기 전) 절차에 한 단계를 더한다: 그 항목이 가리키는 TASK 보고 파일에
  `node <joedesign>/scripts/report-check.mjs --verify <file>`을 돌려 종료 코드 0을 확인한다. 도장이 없거나 맞지
  않으면 그 보고는 "검사되지 않은 보고"이며 항목은 verification pending으로 남는다.
- SKILL.md 보고 규칙("해결 = verified fix")에 한 문장: 결과 목록에서 `changed`인 수정은 해결 줄이 아니라
  남은 문제 줄에 적는다(JOEDESIGN R4와 같은 규칙; JOEDESIGN 쪽은 이미 `templates/DESIGN.md` Report Form 절에
  적혀 있어 스킬 없는 세션도 읽는다).
- 한계: 도장은 글의 형식과 동일성만 보장한다. 숫자가 참인지, 대조가 실제로 있었는지는 보장하지 않으며,
  파일과 도장을 함께 고쳐 쓰는 것을 막지도 않는다. Node가 없는 환경이면 "verify 못 함"으로 적고 완료를
  선언하지 않는다(review-gate와 같은 규칙).

## 제안 2: ROADMAP Check 칸이 규칙 검사 표를 가리키는 형식

`assets/ROADMAP.md` 표의 Check 칸 안내에 예시 한 줄을 더한다(SKILL.md "Roadmap and suitability check"의
review-gate 예시 옆):

```
| CO2 | 간격 규칙 v1 구현 | verification pending | DESIGN.md#rule-coverage S1~S6 행을 현재 입력에서 실행, 행마다 Spot check 기록; 결과 줄과 도장은 TASK#spacing-v1 | ... |
```

- Check 칸은 스크립트 이름이 아니라 DESIGN.md 규칙 검사 표의 행(어느 규칙, 어느 배치·크기·상태)을 가리킨다.
  한 배치만 재는 스크립트가 두 배치를 덮는 규칙을 대신할 수 없다는 것이 이 형식의 이유다.
- 기술 검사(tsc·vitest·E2E)는 같은 칸에 적되 디자인 검사와 구분해 쓴다. 기술 검사 통과가 시각 규칙 통과를
  대신하지 않는다는 JOENESS 기존 문장과 같은 뜻이다.
- JOEDESIGN `references/conformance.md`에도 같은 예시 한 줄을 넣었다(1.2.0).

## 제안하지 않는 것

- 새 스크립트·새 장부·상시 엔진. `report-check.mjs`는 JOEDESIGN 패키지의 것이고 JOENESS는 호출만 한다.
- review-gate(`joeness.review-baseline.v1`) 대체. 하네스가 있는 프로젝트는 기존 게이트가 그대로 Check 칸에 선다.
- 도장을 사람 승인·시각 수락의 증거로 쓰는 것.

## 확인 방법(제안을 받아들였을 때)

JOENESS 쪽에서 한 턴 시험 몇 회로 (1) TASK 항목에 도장 줄이 적히는 비율, (2) 완료 판정 전 `--verify` 실행 여부,
(3) `changed` 수정이 해결 줄에 가는 횟수(0이어야 함)를 센다. JOEDESIGN 쪽 기록은 1.2.0 CHANGELOG와
`evals/check-coverage-20261104/README.md` 11부.
