# JOEDESIGN 2.0.1

2.0.0 게시 뒤 돌린 두 시험(QUICKSTART 실행 시험, JOENESS·JOEFLOW·JOEDESIGN 연동 시험)이 찾은 결함을 고친 판입니다. 보고 검사 R1~R7, 도장·`--verify`는 그대로입니다.

## 바뀐 것

- **`doctor`가 `CODEX_HOME`을 따릅니다.** 기본 탐색 경로가 `~/.codex/skills` 고정이어서 `CODEX_HOME`을 바꾼 설치에서도 홈의 다른 설치를 읽었습니다. `--skills-root`는 기본 경로를 대체하고 반복 지정할 수 있다는 사실을 `--help`와 문서에 적었습니다.
- **영수증 evidence 경로가 프로젝트 기준 상대 경로**가 됩니다(`joedesign.conformance.v1`). 영수증은 커밋되는 파일이라 기계 경로가 남지 않습니다. 프로젝트 밖 파일은 절대 경로로 남고, 2.0.0식 절대 경로 영수증도 계속 읽힙니다.
- `retrieve`에 잘못된 모양의 requirements를 주면 `string indices…` 대신 필요한 행 모양을 알려 주는 `INVALID_INTENT` 오류를 냅니다. `templates/DESIGN_INTENT.json`에 예시 행을 넣었습니다.
- **`templates/DESIGN.md`를 JOENESS 모양에 맞췄습니다.** 표 제목 `## Rule coverage`, `Result` 열이 든 8열 표, 머리줄에 `Authority / version:`·`Approved scope:`. JOENESS와 함께 쓸 때 같은 사실을 두 모양으로 적는 일이 없어집니다. `SKILL.md` 본문은 그대로입니다.
- Report Form 한 문장: rendered 측정 전에 페이지의 스타일시트가 실제로 로드됐는지 확인합니다.
- `references/conformance.md`: JOENESS 연결 프로젝트에서 과업 완료 뒤 DESIGN `Result` 칸 갱신으로 기준선이 stale이 되는 것은 정상이고 다음 과업의 검수가 기준선을 새로 세운다는 절차 문장(사용자 결정, 코드 변경 없음).
- 문서: 저장소는 공개라 로그인이 필요 없습니다(이전 문구 수정). INSTALL에 백업·해시 비교 PowerShell 블록, 태그 체크아웃 업데이트 대안, DESIGN.md·참고 화면이 없을 때 할 일.

## 확인된 것

- 코드 결함 3건은 고치기 전 실패하는 테스트를 먼저 만들었습니다. node 44/44, python 147 OK(건너뜀 2), part19 회귀 274개 R1~R6 수 동일·R7 바뀜 0.
- 연동 시험 프로젝트 사본에서 2.0.1로 영수증을 다시 만들자(evidence가 `work/gate/...` 상대 경로) JOENESS 2.0.1 `review-gate.mjs`가 `allowed:true`로 소비했습니다(부모 세션 확인).
- v1.3.4 → 2.0.0 → 2.0.1 설치본 해시가 저장소 `skills/joedesign`과 일치(설치 영수증).

## 확인되지 않은 것

- 행동 시험 0회. 템플릿 정렬·스타일시트 확인 문장이 에이전트 행동을 바꾸는지는 보지 않았습니다.
- macOS·Linux에서 `CODEX_HOME` 동작. 실제 새 대화에서의 스킬 호출.

## 세션이 대신 내린 결정

1. `--skills-root`를 "추가" 옵션으로 바꾸지 않고 문구만 고쳤습니다(행동 범위 확대 금지).
2. 템플릿 정렬은 JOENESS 1.4.2가 정한 모양을 기준으로 삼았습니다.

기록: [report-201.md](report-201.md), 입력 시험 [docs-joedesign-report.md](docs-joedesign-report.md)·[integration-report.md](integration-report.md).
