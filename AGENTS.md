# JOEDESIGN repository

## T043 검사 범위 표 보강 (2026-11-04, 현재)

- 사용자 지시: JOEFLOW 검증 완료 후 JOEDESIGN 보강(이 세션 채팅). 오목 세션의 규칙 위반
  원인(한 배치·크기만 잰 검사가 규칙 통과로 기록됨)에 대한 DESIGN 측 대응.
- 변경: templates/DESIGN.md의 Token Roles·Rule Coverage 절, SKILL.md 2·3·6단계와 인계 문단,
  references/conformance.md 최소 형식 절, operation·visual-translation 한 문장. 문서만.
- 보존: 실행 코드·스키마·계약, 기존 태그·Release, 미추적 feedback 폴더. 버전은 2026-11-09 사용자 위임
  ("임자 하고 싶은 대로 해")으로 1.1.0으로 올리고 태그·Release·개인 설치 갱신까지 진행(CHANGELOG 1.1.0 절).
- 검증: evals/check-coverage-20261104 (단일 턴 48회 + 40턴 롱텀 80패킷 블라인드 A/B,
  회귀 14/14·142 OK). 롱텀에서는 우위 없음, 보고 통과 주장 범위는 B가 낮음, 검사 표와 실측
  4px 어긋남 1건 발견.
- 추가(2026-11-05, 사용자 지시 "보강 완료하고 커밋하자"): 그 두 빈틈에 대한 문구. SKILL.md
  3단계(표본 대조, 안 했으면 "not spot-checked")·6단계(통과 숫자마다 같은 문장에 범위),
  conformance.md·templates/DESIGN.md 같은 계약. 한 턴 24회 블라인드 비교(report-scope/)에서
  보고 범위·대조 수행은 개선, 퇴행 없음. 브라우저 시험의 행 전부 표기(0/4)·'해결' 한정(1/4)은
  미달로 남음. 롱텀 재측정 없음.
- 추가(2026-11-06, 사용자 지시 "한번에 묶어서 진행하고 결과 보고해" — 브라우저 보고 규율 보강과
  결함 심은 검증): Rule Coverage 표의 Spot check 열, 대조 안 한 행의 결과를 해결로 적지 않는 문구
  (templates/DESIGN.md, SKILL.md 3·6단계, conformance.md, visual-translation.md 한 줄). 한 턴 20회
  블라인드 확인(spot-check/): 심은 결함을 밝힌 시험 B 0/4·C 3/4·D 4/4, 행 전부 표기 C 0/8 → D 8/8.
  보고 문장의 통과 범위는 개선 없음(C 6/8, D 3/8).
- 추가(2026-11-06, 사용자 지시 "보강 진행" — 보고 문장 범위 보강): 보고의 검사 결과를 한 목록에
  정해진 형식 한 줄씩 적는 문구(SKILL.md 6단계, conformance.md 한 문단). 한 턴 12회 + D 12회
  재채점(spot-check/result-lines/): 결과 목록 사용 12/12, 브라우저 두 장면 통과 문장 범위 D 2/8 →
  E 5/8(채점기 변동 큼, 방향만). 맨 위 요약 문장의 범위와 대조 없는 '해결' 표기는 미달로 남음.
  2026-11-06의 두 추가는 사용자 승인("커밋·푸시") 뒤 한 커밋으로 main에 반영.
- 추가(2026-11-07, 사용자 지시 "다음 보강" → 선택 "남은 두 빈틈 묶음"): 수정 줄의 결과를
  `fixed`/`changed`로 고정하고 목록 밖 검사 결과에 괄호를 붙이는 문구(SKILL.md 5·6단계, conformance.md
  한 문단). 한 턴 12회 + E 12회 재채점(spot-check/fix-word/): 대조 없는 '해결' 표기 E 브라우저 4/4 →
  F 0/12(보고 원문 기준), 요약 문장 범위는 미달로 남음(결함 심은 과제 2/4). 2026-11-07 G안과 한 커밋으로 main 반영.
- 추가(2026-11-07, 사용자 질문 "안 고쳐진 것까지 고칠 수는 없어?" → 승인 "시험 실행"): 보고를 보내기
  전에 돌리는 검사 스크립트 `skills/joedesign/scripts/report-check.mjs`와 그 지시(SKILL.md 6단계,
  conformance.md 한 문장), `tests/report-check.tests.mjs`. 한 턴 12회 + F 12회 재채점
  (spot-check/report-check/): 12회 모두 스크립트 실행, 범위 없는 "통과" F 3/12 → G 0/12, 블라인드 g·h
  7/12·7/12 → 12/12·12/12, 대조 없는 '해결' 0/12 유지. 사용자 승인("커밋·푸시") 뒤 F안과 한 커밋으로 main 반영.
- 추가(2026-11-08, 사용자 지시 "게시 전에 장기 측정 돌려서 검증 완료하고 부족한 부분 찾아"): 40턴 롱텀
  G 1세션 + B 재채점(evals/check-coverage-20261104/longterm-G/, README 9부)과 JOENESS·JOEFLOW·단독 연계
  문서 대조(longterm-G/audit-integration.md). 결과 G h2 30/40 vs B 12/40, 8개 전부 21/40. 빈틈 F1~F7
  발견, 스크립트가 보낸 글이 아닌 뼈대 파일만 검사한 것이 가장 큼. 게시·버전 변경은 보류, 사용자 결정 대기.
- 추가(2026-11-09, 사용자 승인 "H안 설계부터" → "시험 실행"): 도장(ok에 글자 수·해시, 보고 끝 줄, `--verify`),
  검사 없는 턴 한 줄, R4. 10턴 1세션 + G 10턴 재채점(longterm-H/, README 10부): 도장 일치 8/8, 보낸 글 지적 0/8,
  블라인드 8개 전부 8/8. 9·10부와 함께 1.1.0으로 커밋·게시(2026-11-09).
- 사고(2026-11-09, 내 실수): L-G(G 40턴 최종 작업 트리)에 `git checkout -- .`이 실행돼 추적 파일 변경이 되돌아감.
  스냅샷·보고·패킷·고정 빌드는 보존. longterm-G/incidents.txt.
- 검증 중 사고: 시험본 정션 오류로 실제 AI-Gomoku 작업 폴더에 캐시 폴더 3개가 생겼다가 삭제됨
  (추적 파일 변경 없음). 기록은 report-scope/incidents.txt.
- 추가(2026-11-09, 사용자 승인 "더 많이 확실하게 검증해" → 대조군 포함 실행): I안. SKILL.md "Decide the scope" 문단(JOEFLOW
  state.json·기획서·approval_status 읽기, 제품 결정 대기·재진입), operation.md 두 문장, templates/DESIGN.md `## Report Form` 본문 절,
  conformance.md Check 칸 예시·도장 보관, docs/proposals/2026-11-09-joeness-report-stamp.md(JOENESS 측 제안, 그 저장소는 미수정).
  한 턴 블라인드 24회(I 16, H 대조군 8) + 채점 3(evals/check-coverage-20261104/part11/, README 11부): 제품 정의 읽기 6/6 vs 0/4, 인계
  결과 목록 4/6 vs 0/4, 회귀 퇴행 없음. 시험본은 `_data/2026-11-09-joedesign-i/`, 정션은 사설 node_modules(두 방법 확인). 남은
  서버 9개를 내가 종료, 실제 AI-Gomoku 변경은 연결된 오목 세션 것(part11/incidents.txt). 사용자 승인("게시 진행") 뒤 1.2.0으로 올리고 태그·Release·개인 설치 갱신(part11/install-receipt.md).
- 추가(2026-11-10, 부모 세션 위임 과제 "JOEDESIGN 1.2.1 소개정" → 사용자 승인 "둘 다 승인"(시험 22회)): SKILL.md 재배치 경계 두 문장·인계 문단 한 문장, operation.md 한 문장,
  templates/DESIGN.md 제목 아래 Report Form 안내 줄. 한 턴 20회 + 블라인드 채점 2(evals/check-coverage-20261104/part12/, README 12부): 인계 Report Form 절 읽기 4/4 vs 2/4,
  `fixed`/`changed` 4/4 vs 2/4, 재배치 대기 기록 2/4 vs 2/4(경계 문구 효과 없음), 위치만 바꾼 과제의 오탐 0, 퇴행 없음. 남은 vite 서버 4개를 내가 종료, 실제 AI-Gomoku 변경은
  오목 세션 것(part12/incidents.txt). 사용자 승인("재배치 문구 빼고 게시") 뒤 재배치 경계 문구(SKILL.md 두 문장, operation.md 한 문장)를
  빼고 Report Form 안내 줄·인계 문장만 1.2.1로 게시(VERSION·태그·Release·개인 설치, part12/install-receipt.md). 전후 표시 대조 절차는 다음 과제.
  정정: 태그 v1.2.1은 06573af(주 세션이 생성), GitHub Release 게시됨. edfc9e7에 섞인 1.3.0 세션의 미완성 R5 코드와 되돌림 기록은 part12/incidents.txt.
- 추가(2026-11-10~11, 부모 세션 위임 과제 "JOEDESIGN 1.3.0" → 사용자 승인 "둘 다 승인 (75회)", "13회 추가 후 40턴", "처음부터 다시"(총 89회)): 재배치·겹침·숨김·병합은
  `## Display before/after` 요소별 전후 두 줄로 판정(SKILL.md 한 문장, 효과 미확인 세 문장 삭제로 14,212B ≤ 1.2.1 14,216B), templates/DESIGN.md Report Form 한 문단,
  conformance.md R5, report-check.mjs R5와 테스트 16/16. 한 턴 72회 + 채점 4(evals/check-coverage-20261104/part13/, README 13부): 표시가 바뀐 재배치 대기 8/8 vs 1/8, 오탐 0,
  기존 항목은 같거나 높음. 40턴 L-J2 + 채점 10(part13/longterm-J2/): G 재채점 대비 h2 33 vs 27, 8개 전부 29 vs 20, 함정·도장·스크립트 전부, h1·인계 h3·h7 각 1턴 낮음.
  내 실수: 첫 40턴 시도에서 턴 6에 백로그 밖 메시지를 보내 무효 처리(part13/longterm-J-void1/). 또 1.2.1 게시 세션 커밋에 미완성 R5가 섞였다가 그 세션이 되돌렸다(06573af).
  로컬 커밋까지, 푸시·VERSION 1.3.0·태그·Release·개인 설치는 승인 대기.
- 완료 순서: 로컬 커밋 → Manager 검토 → 푸시. 태그·Release·개인 설치는 별도 사용자 승인.

## T042 README 영어 기본화 (2026-10-13, 현재)

- 사용자 지시: 영어 설명 우선 배치, 한국어 설명 보존. Manager 채팅의
  01a1358c-9939-72c1-bb82-b2c9f805af77 확인.
- 구성: 제품 H1 → 언어 이동 링크 → 영어 6개 항목 → 한국어 본문 원문.
  한국어 최초 H1만 중복 제외. 한국어 본문·기존 heading 앵커·실행 명령 보존.
- 범위: README 및 최소 현행 기록. 상세 문서·Release·버전·태그·설치·runtime 변경 금지.
- 완료 순서: 번역·원문 보존·링크 검증 → 로컬 커밋 → Manager 독립검토 후 푸시.
  실제 GitHub 렌더링 검토는 Manager 담당. 기존 미추적 자료 보존, 새 worktree 금지.

## T041 현행 사용자 안내 문체 정비 (2026-10-13, 현재)

- 사용자 지시: 보고서 형식·명사형 종결 적용. Manager 채팅의
  01a13577-0da5-7002-922a-0a17a4a80b4b 및 01a13577-619f-7772-b1b2-09b06328b35c 확인.
- 대상: README.md, docs/INSTALL.md, docs/VALIDATION.md의 현행 사용자 안내.
- README 구성: 핵심 요약 → 설계 목적 → 주요 기능 → 사용 방법 → 도구 간 연결 → 한계.
- 보존: 명령·프롬프트 예시, 지원 범위, 검증 수치, 과거 이력·설계·evidence,
  skills/ 전체·코드·버전·개인 설치·기존 태그. 다른 제품 파일·전역 설정 변경 금지.
- 변경 기록: 현행 범위의 최소 기록 추가만 허용. 과거 기록 재작성 금지.
- 완료 순서: 문서 검증 → 일반 로컬 커밋 → Manager 검토 → 통지 후 일반 푸시.
  검토 전 푸시, 태그 재지정, 새 worktree 금지. Release 본문 수정은 Manager 담당.

## Personal installation and release directive (2026-10-13, current)

The user explicitly approved T040 in Local QA Manager, message
01a13565-86fd-7c91-84df-8bd546d76049: update personal installations, publish tags
and GitHub Releases, and verify. This supersedes T039's no-install/no-release
boundary only for that scope. JOEDESIGN owns its exact personal-package update
and product records; Manager owns the three-installation cross-check and central
tag/Release publication. Do not create duplicate tags or releases here.
The personal joedesign package is now1.0.0: 44-file verified backup outside skill
discovery, only VERSION/agents metadata changed, other42 files preserved.
Source package/runtime, other skills, global settings and feedback dirs stay intact.
See evals/v1-personal-install-20261013/README.md for receipt and verification limits.
Documentation-only completion may be committed and pushed normally to main.
No new worktree, force push, feature expansion, product changes or GEO messages.

## JOE tools 1.x integration directive (2026-10-13, current)

The user approved T039 in Local QA Manager: common simple Korean README, package
version alignment and verified main integration. JOEDESIGN targets 1.0.0 from
1d9502ea74d6a0fbbad730450e85f0b327b2906e. This supersedes earlier 0.3.0-dev freezes
only for this version/documentation candidate; skill IDs, schema versions, runtime
contracts, preserved source/evidence and F05 limits remain unchanged.
Candidate7069f34 passed repository and Manager isolated cross-review. Manager
notified completion and authorized the user's ordinary branch push/main integration.
Finalize documentation and raw-evidence attributes only; preserve package bytes.
Do not update personal installations, create tags or GitHub releases in this
integration step. No new worktree, generic feature expansion, other JOE source edits, product
changes or GEO messages. Preserve/exclude the two existing untracked feedback dirs.
Report exact source/version/install hashes and limits here and to the user-authorized
Manager. T039/Q5 belongs to Manager; repository candidate evidence belongs here.

## Main integration authorization (2026-10-10, current)

After the three scoped behavioral trials, the user explicitly authorized committing,
pushing and merging this unified-core work into main before further real use.
This supersedes earlier no-commit/no-push restrictions for this integration only.
Include the improvements, preserved history, validation and limits. Version remains
0.3.0-dev; integration is not a release tag, whole-product acceptance, another
installation change or permission to message GEO. Report completion here.

## Direct reporting correction (2026-10-10)

The user explicitly directed that JOEDESIGN reinforcement and decisions be reported
and assessed in this chat, not sent to the GEO Website design chat. Do not request
further GEO work or delegate reinforcement judgments there. Existing completed
activation remains recorded; do not roll it back or expand it without direction.
Report scope, validation and remaining decisions directly to the user.

## Scoped operational continuation (2026-10-10)

After the real GEO snapshot validation, the user said to proceed with remaining
criteria review, dependency scoping and completion integration. Coordinate with
the JOENESS owner; that owner handles its installation and completion caller.
JOEDESIGN owns its single-core installation transition with recoverable backups
outside skill discovery and exact package verification. This supersedes the
earlier no-install restriction for that scoped transition only. GEO shared record
activation belongs to its designated design owner; do not edit product UI or
declare whole-product completion. No new commit/push/release authorization.

## Design conformance connection (2026-10-10)

The user requested JOEDESIGN/JOENESS responsibility separation and executable
missing/failed/stale-check gates after GEO's repeated spacing omissions. Integrate
this inside the single core. JOEDESIGN owns source-rule/target coverage and rendered
geometry/specialist judgments; JOENESS owns consuming the scoped result and limiting
task completion. Use the independently pinned contract described in
skills/joedesign/references/conformance.md. Do not duplicate product ledgers or edit
the GEO shared files. Tests must include actual producer/consumer linkage, not just
field presence. Local pins/evidence do not authenticate user approval or prevent
direct file/chat bypass. Installations and project activation remain unchanged.

## Single operating core directive (2026-10-09, current)

The user requested one operating core governing all stages and role assignments.
The active entrypoint and operating authority is skills/joedesign/SKILL.md. The
harness is internal implementation in that same package, not a second public skill.
This supersedes the previous freeze of the current skills/joedesign/ directory and
the two-package routing instructions below. Preserve original v0.2/Harness bytes
in fixtures/package-history/pre-unification-20261009/ and Git history; do not rebind
old behavior evidence to the unified package. The unified source is 0.3.0-dev;
the previous main integration remains core v0.2 + Harness v0.1.

The coordinator is A and owns scope, assignments, transitions and integrated results.
Role workers apply the same core within their assignment. Keep Product meaning,
visual decisions, actual specialist use, observed proof and user acceptance distinct.
Run Python regression and the Node v0.2 historical-evidence regression. New package
copy/runtime checks must exercise the unified source; historical tests do not prove
its live model behavior. Do not modify installations, JOENESS, JOEFLOW or product
working files. The prior commit/push/main authorization was completed; this source
integration step does not by itself publish a new release or update installations.
Current change rationale and validation: evals/unified-core-20261009/README.md.

## Historical directives (superseded where the current directive differs)

## Integration directive (2026-10-09)

The user authorized committing and pushing the completed reinforcement, documenting
its improvements and limitations, and merging the current branch into main. This
supersedes the historical no-main/no-push restriction for this integration only.
Current component versions remain JOEDESIGN core v0.2 and Design Harness v0.1;
identify this update by its Git commit and CHANGELOG.md. Do not treat main integration
as installation, release certification, visual-quality validation or user acceptance.
Preserve the frozen core, historical evidence and existing personal installations.

## Current RACI directive (2026-09-30)

The user explicitly made RACI the work principle and requested a duplication audit
of the main skill instructions. This supersedes the prior source/install parity
and no-install rule only for the scoped `joedesign-harness` RACI update. Keep
`skills/joedesign/`, JOENESS, JOEFLOW and unrelated installed skills unchanged.
R → C1 → conditional C2 is an execution route, not a vote. A owns the integrated
result and I receives it. A role label alone cannot prove that a specialist skill
was used; the CLI requires trusted skill-use/review receipts and still ships no
host adapter. Do not claim live RACI enforcement from synthetic tests.

## Current Harness decision (2026-09-30)

The existing Harness baseline retained its visual-production/motion-quality
correction. The later production-relationships, dependency-guard and
`inspect-relations` experiment was not adopted: two bounded A/B tasks did not show
unique design-quality value. See `evals/harness-v0.1/retention-decision.md`.
The active design/RACI path below is updated with this decision; historical proposal
language is background, not proof that every described visual judgment is automated.
Keep repository tests, browser evidence, human
quality judgment and user acceptance distinct.

## Active task: Design Harness v0.1 (2026-09-29)

The user explicitly authorized implementing the r2 design, including a separate
`joedesign-harness` package and Python stdlib controller. For this branch that
authorization supersedes the earlier candidate-only prohibition on new public
skills/parsers. Preserve every byte of `skills/joedesign/` and historical evidence.
The active spec is docs/superpowers/specs/JOEDESIGN_UI_REVIEW_RACI_V0_1_DRAFT.md;
the accompanying original handoff is subordinate where r2 changes it.
Do not modify JOENESS, JOEFLOW, unrelated installed skills, or the user's BIO working files.
Run both the v0.2 Node regression and `python -m unittest discover -s tests -v`.
Static validation, live host attestation, human visual quality and user acceptance
remain separate. No quality or tamper-resistance claim from fixtures alone.

## Preserved v0.2 scope and history (below)

- Current branch is the v0.2 Visual Translation implementation candidate. Read README, docs/specs/joedesign-v0.2-visual-translation.md and its evidence pointer before resuming. This is Program Review, not user acceptance or production readiness.
- Preserve pinned v0.1 2a815ee49d8f7ca6a7c1e483df315eda1fa709d7, branch codex/joedesign-v0.1-test, historical responses/Smokes/failures and archived test-source bytes. Never rebind old evidence to a changed package.
- One public joedesign; Product meaning, scoped approved originals/root DESIGN.md, proposals and user acceptance stay distinct. Defaults do not override approved source material.
- Any shipped package byte change requires appropriate fresh behavior evidence before readiness claims. Freeze expectations before seeing candidate results; keep failures and correction history.
- Run node --test tests/joedesign-v02.tests.mjs for this version. It checks package/history/evidence integrity and saved qualitative review, not live model behavior or visual quality. v0.1 source tests are historical; run the original suite only at its pinned revision.
- No new platform, parser/exporter, router/scorer, database, public skill or competitor/runtime dependency. No personal install, main integration, force push or release tag under this candidate task.
- TrackE is CLOSED; specialist value NOT TESTED. Do not reopen TEST B, reuse diagnostic designs/scores for tuning or resume TrackC BIO production. Real-project visual validation requires separately supplied approved material/assets and remains PENDING.
- Canonical current role map: docs/architecture/JOEDESIGN_OPERATING_MODEL_V1.md (v0.2 content). Earlier handoffs/doctrines and the labeled v0.1 roadmap body are historical, not instructions to restart completed work.
