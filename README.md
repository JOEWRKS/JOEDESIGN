# JOEDESIGN

> JOEDESIGN으로 디자인해.

JOEDESIGN turns a project's approved product meaning and current context into visual direction, bounded proof, precise refinement, responsive translation, and rendered visual review. One skill covers all of these; you do not need separate direction, proof, or review commands.

It owns visual expression and the project-root `DESIGN.md`: composition, typography, color, imagery, visual controls, motion expression, and responsive recomposition. Product Definition still owns what the product does. JOEFLOW, when present, owns lifecycle progression and routes bounded product ambiguities; it is not a runtime prerequisite. Visual PASS is not user acceptance.

## Install and use

Copy only `skills/joedesign` from this repository to your project's `.agents/skills/joedesign`. Keep its three files and relative paths intact. This is a project-local copy, not an installer or a global behavior overlay. Do not copy the repository's `AGENTS.md`, tests, or specification into your project's runtime skill folder.

Start a fresh Codex session in that project. Ask **“JOEDESIGN으로 디자인해.”**, describe the target, or explicitly invoke `$joedesign`. Provide or point to current Product authority and any accepted visual evidence. JOEDESIGN will inspect what is already available.

With unresolved direction, expect distinct candidates and a small proof before expansion. With approved direction, ask for a specific refinement; unnecessary alternatives and page-wide regeneration are not required. A root `DESIGN.md` starts DRAFT, becomes APPROVED only through explicit user approval, and preserves approved authority while material revisions are proposed separately.

## Boundaries

Backend-only work, nonvisual refactors, layout-unaffected copy/value changes, and Product Definition itself do not call for JOEDESIGN. The exact [shared contract and revision](docs/specs/joedesign-v0.1.md#implementation-handoff-constraints-2026-09-06) define cross-system ownership without importing either system's internal workflow.

v0.1 intentionally includes no Impeccable, UI UX Pro Max, Figma Make methodology, Apple Design, Hallmark, Refero orchestration, oh-my-design, Watermelon, Componentry, or Cult UI runtime. There is no vendor router, JOENESS Core/distribution machinery, mandatory seven-stage ceremony, Ponytail, Superpowers product workflow, separate visual-check skill, or installer framework. General browser/image/repository capabilities and an existing project runtime remain usable.

## Verification

Run `node --test tests/joedesign-contract.tests.mjs` with Node.js. The 16 tests map 1:1 to specification §23: public discovery, fourteen deterministic replays of actual Astra scenario decisions, and pure-core package/install-copy absence checks. The replay pins all shipped skill bytes and parsed input-case data; it fails when evidence is missing or stale. JSON formatting alone does not invalidate identical scenario data; the original runtime input byte hash is also retained. It does not call a model, simulate an instruction engine, or prove that every decision was executed in a real project. The original run and evidence provenance are in `fixtures/contract-cases/observed.json`.

An optional `JOEDESIGN_INSTALLED_SKILL` environment variable points the same suite at a project-local installed copy for byte-for-byte verification. Fresh Astra xhigh smoke A/B separately verify an unresolved dashboard proof and approved Hero typography refinement. Competition and broader project generalization remain outside this MVP review gate.
