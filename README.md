# JOEDESIGN

## 지금 사용할 스킬 (2026-09-30)

| 요청 | 사용할 스킬 | 역할 |
|---|---|---|
| 승인된 화면·원본을 구현하거나 국소 수정 | [`joedesign`](skills/joedesign/SKILL.md) | 제품 의미를 보존하며 원본의 시각 관계를 구현하고 실제 화면을 확인 |
| 참조를 조사·번역해 새로운 시각 방향을 만들거나 큰 범위의 검증 수행 | [`joedesign-harness`](skills/joedesign-harness/SKILL.md)와 `joedesign` | Harness가 참조·계약·증거·검수 절차를 관리하고 JOEDESIGN이 시각 판단을 수행 |

Impeccable은 타이포·간격·광학 정렬·표현 모션, UI UX Pro Max는 콘텐츠·상태·입력·복구,
web-design-guidelines는 시맨틱·키보드·접근성·반응형 구현을 교차 점검한다.
React·애니메이션 성능 스킬은 해당 구현 문제가 있을 때만 사용한다. 이들은
별도 승인권자나 자동 실행 에이전트가 아니다. OMD는 필요한 참조를 찾는 자료원이다.
사용자와 Product 요구, 승인된 `DESIGN.md`와 원본을 대체하지 않는다.

현재 Harness 소스는 설치된 **기존판**의 런타임 파일과 일치한다. 전체 화면과
모션 검증을 보완한 [시각 제작 지침](skills/joedesign-harness/references/visual-production.md)은
포함한다. 별도 실험의 관계 진단·의존성 검사 확장안은 품질 이득이 확인되지 않아
채택하지 않았다. [설계·RACI·현재 상태](docs/superpowers/specs/JOEDESIGN_UI_REVIEW_RACI_V0_1_DRAFT.md)와
[A/B 채택 판단](evals/harness-v0.1/retention-decision.md)을 참조한다.

이 저장소 커밋은 스킬을 설치하거나 기존 설치본을 바꾸지 않는다. Harness CLI는
로컬 참조·계약·증거의 일관성을 검사하지만 렌더링이나 미감을 자동 판정하지
않는다. 인증된 호스트 receipt가 없어 로컬 실행만으로 최종 `APPROVED`도 발행하지
못한다. 실제 디자인 품질과 정확한 사용자 승인은 별도 관찰·판단 대상이다.

## 저장소 실행·검증

The separate [joedesign-harness skill](skills/joedesign-harness/SKILL.md) implements
OMD corpus retrieval, grounded design contracts, scoped transitions, structural
rework and evidence/approval policy. The original joedesign v0.2 package is unchanged.
See [usage and trust boundaries](skills/joedesign-harness/references/operation.md)
and [verification/limitations](evals/harness-v0.1/README.md).

Run `python skills/joedesign-harness/scripts/harness_cli.py --help`.
Tests: `python -m unittest discover -s tests -v` and
`node --test tests/joedesign-v02.tests.mjs`.
새 프로젝트에서 소스를 사용할 때는 두 스킬 폴더를 프로젝트의 스킬 경로에
함께 배치한다. 저장소의 spec·AGENTS·평가 기록은 런타임 스킬 입력이 아니다.
실제 제품·원본·자산·상태를 제공하고 필요한 스킬만 호출한다.

## 보존된 v0.2 기록 — 현재 사용 안내는 위 표

> JOEDESIGN으로 디자인해.

JOEDESIGN preserves product meaning while translating approved visual material and
selected reference relationships into project-specific composition and implementation
decisions, then diagnoses differences between the original and actual output.

## v0.2 Visual Translation — implementation candidate

Primary: implement/refine an approved visual target using its original material and
real assets. Conditional: propose an unapproved direction when a reference-based
decision is unresolved. Sufficient inputs need only the implementation delta, not
compulsory alternatives or a rewritten design brief. A supplied image is not approval.

This is a candidate for Program Review, not a production release, user acceptance,
design-quality guarantee or evidence of specialist superiority.

- Branch: codex/joedesign-v0.2-visual-translation.
- Pinned v0.1 baseline: 2a815ee49d8f7ca6a7c1e483df315eda1fa709d7;
  preserved branch codex/joedesign-v0.1-test.
- [Change spec / contract mapping](docs/specs/joedesign-v0.2-visual-translation.md).
- [v0.2 당시 역할표](docs/architecture/JOEDESIGN_OPERATING_MODEL_V1.md).
- [Evidence, hashes, instruction sizes and limits](fixtures/contract-cases/evidence/visual-translation-v02/README.md).

## v0.2 당시 코어 단독 설치 안내

Copy only skills/joedesign into your project's .agents/skills/joedesign, preserving
the three files and relative paths. No installer or global behavior overlay is needed.
This repository's spec, AGENTS, tests, operational reports and diagnostic history are
not candidate runtime input. This task does not perform a personal install.

In a fresh project session invoke $joedesign or ask “JOEDESIGN으로 디자인해.”
Point to Product authority, original visual material/assets and the exact request.
Identify what is actually approved, including version/surface/state, versus ordinary
references. The skill reads existing decisions and keeps a single root DESIGN.md;
the compact template is needed only for creating/materially updating those decisions.

Source observation → project preserve/change → implementation decision → observable
result difference. This connection supplements the originals; a controller must not
replace them with a taste paragraph. Native project tokens/components remain useful.
The implementer still observes its actual render. Build/token success is not visual
conformance, and visual conformance is not user acceptance.

## Verification and history

Current command: node --test tests/joedesign-v02.tests.mjs

The suite checks the three-file package, a temporary project-local copy, historical
bytes, frozen inputs and linkage/review of fresh functional responses. It does not
call a model and does not turn textual decisions into rendered proof. The evidence
packet records actual executions separately, including failures and limitations.

The pre-change original suite was run: 72 PASS / 0 FAIL. Its exact test sources now
live under fixtures/contract-cases/history/v01-test-sources/; their relative imports
are intentionally unmodified. To rerun that historical suite, use a separate checkout
of the pinned v0.1 commit and the original command in the evidence packet. Do not run
those archived tests against v0.2 or relabel v0.1 semantic/Smoke evidence as v0.2.

TrackE is CLOSED. JOEDESIGN and UI UX Pro Max specialist value remains NOT TESTED;
TEST B was platform-blocked, not a method failure. No diagnostic rerun is authorized.
Real-project visual validation with newly approved designs and actual assets is
PENDING; none were supplied here. No BIO production, comparison, personal install,
main merge, release tag or new runtime dependency is part of this candidate.
