# JOEDESIGN

> JOEDESIGN으로 디자인해.

JOEDESIGN turns a project's approved product meaning and current context into visual direction, bounded proof, precise refinement, responsive translation, and rendered visual review. One skill covers all of these; you do not need separate direction, proof, or review commands.

It owns visual expression and the project-root `DESIGN.md`: composition, typography, color, imagery, visual controls, motion expression, and responsive recomposition. Product Definition still owns what the product does. JOEFLOW, when present, owns lifecycle progression and routes bounded product ambiguities; it is not a runtime prerequisite. Visual PASS is not user acceptance.

## Test version — v0.1-test

A working MVP frozen for practical evaluation, not a production release or a claim of design superiority.

| Item | Value |
| --- | --- |
| Version | `v0.1-test` |
| Date | `2026-09-07` |
| Test branch | `codex/joedesign-v0.1-test` |
| Frozen core / evidence source | `7f890c60ed3837efc1693aeeba33759f12c85383` |
| Source tree | `0945d2b7dafc671bd7afdd3b5b5daaf2678f8b6c` |
| Program decision | Pure Core Freeze approved; JOEDESIGN arm may be handed off for comparison |
| Package change in this snapshot | None; documentation only |

Pin the exact test commit used for an evaluation; do not follow a moving branch during the run. The immutable source commit above supplies the same three-file skill package. This version label is a branch/document designation, not a Git tag or a published GitHub Release.

| File under `skills/joedesign/` | SHA-256 |
| --- | --- |
| `SKILL.md` | `d73d1ce3067c6913abe5bd6d562bc87491f20e1b61c64a60cd9f522371715652` |
| `templates/DESIGN.md` | `4ac8586fad0a8f964d4ace550f2706af49df0403f3618a5214dd17b98ee1c237` |
| `agents/openai.yaml` | `c28a9f5e01c3ab39a5518c35d6cd6c41629f15edbadf696948339e58262e15c1` |

### Test ownership

| Owner | Responsibility |
| --- | --- |
| JOEDESIGN lead / TrackB | Preserve the frozen core; assess demonstrated defects after evaluation |
| TrackC implementation agent | BIO production implementation; remains paused until its own resumption is authorized |
| Existing TrackC lead chat | BIO brief, product priorities, evaluation criteria and adoption decisions |
| New TrackE agent | Comparison execution, independent run contexts, evidence collection and anonymization; does not select a winner itself |

Publishing this snapshot does not start the comparison or resume BIO production. See the [roadmap](docs/roadmaps/JOEDESIGN_V0_1_IMPLEMENTATION_ROADMAP.md) for the current phase and corrected track roles. Historical review packets retain their original pending statuses and role wording; they are not current execution instructions.

## Install and use

Copy only `skills/joedesign` from this repository to your project's `.agents/skills/joedesign`. Keep its three files and relative paths intact. This is a project-local copy, not an installer or a global behavior overlay. Do not copy the repository's `AGENTS.md`, tests, or specification into your project's runtime skill folder.

Start a fresh Codex session in that project. Ask **“JOEDESIGN으로 디자인해.”**, describe the target, or explicitly invoke `$joedesign`. Provide or point to current Product authority and any accepted visual evidence. JOEDESIGN will inspect what is already available.

With unresolved direction, expect distinct candidates and a small proof before expansion. With approved direction, ask for a specific refinement; unnecessary alternatives and page-wide regeneration are not required. A root `DESIGN.md` starts DRAFT, becomes APPROVED only through explicit user approval, and preserves approved authority while material revisions are proposed separately.

## Boundaries

Backend-only work, nonvisual refactors, layout-unaffected copy/value changes, and Product Definition itself do not call for JOEDESIGN. The exact [shared contract and revision](docs/specs/joedesign-v0.1.md#implementation-handoff-constraints-2026-09-06) define cross-system ownership without importing either system's internal workflow.

v0.1 intentionally includes no Impeccable, UI UX Pro Max, Figma Make methodology, Apple Design, Hallmark, Refero orchestration, oh-my-design, Watermelon, Componentry, or Cult UI runtime. There is no vendor router, JOENESS Core/distribution machinery, mandatory seven-stage ceremony, Ponytail, Superpowers product workflow, separate visual-check skill, or installer framework. General browser/image/repository capabilities and an existing project runtime remain usable.

## Verification

The inherited freeze record contains **72 PASS / 0 FAIL** for the eight-file suite. This is an aggregate of wording/package assertions and saved semantic-response checks, not 72 practical design jobs. Documentation publication is not a new model replay, browser observation or test run.

Run the full suite with Node.js:

```sh
node --test tests/joedesign-contract.tests.mjs tests/joedesign-craft-core.tests.mjs tests/joedesign-typography-scale-core.tests.mjs tests/joedesign-reference-intelligence-core.tests.mjs tests/joedesign-color-contrast-core.tests.mjs tests/joedesign-imagery-focal-core.tests.mjs tests/joedesign-composition-anti-template-core.tests.mjs tests/joedesign-implementation-bridge.tests.mjs
```

`tests/joedesign-contract.tests.mjs` alone remains the 16-test Process/Authority subset. Its fourteen saved-response checks do not call a model. An optional `JOEDESIGN_INSTALLED_SKILL` environment variable verifies a project-local installed copy against the shipped three-file package.

[Freeze review evidence](fixtures/contract-cases/evidence/astra-smoke-v1/pure-core-freeze-v1/README.md) records original commands, outputs, package identities and version-scoped Smoke evidence. The recovered Bridge run verifies native identity and input/output linkage; independent exclusion of hints in encrypted messages and OS isolation remain UNVERIFIED. No new observation is implied by copying historical evidence. Real-project quality, generalization, comparative advantage and User Acceptance remain unverified.
