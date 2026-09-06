# JOEDESIGN repository

- `docs/handoffs/JOEDESIGN_COLOR_CONTRAST_CORE_V1.md` is the active execution handoff on this branch. Read it first and do not expand scope beyond Color / Contrast Core implementation and validation.
- `docs/roadmaps/JOEDESIGN_V0_1_IMPLEMENTATION_ROADMAP.md` is the canonical execution roadmap for current phase order, completion gates, and memory-loss recovery.
- `docs/architecture/JOEDESIGN_OPERATING_MODEL_V1.md` is the canonical top-level role map and operating model. Read it first when changing system boundaries, authority order, process ownership, or how Product Definition, JOEFLOW, JOEDESIGN, references, DESIGN.md, implementation, verification, and user approval fit together.
- `docs/specs/joedesign-v0.1.md` is the implementation baseline; its current handoff stop is review, not competition readiness.
- `docs/specs/joedesign-craft-core-v0.1.md` is the canonical native craft doctrine. Read it before changing visual hierarchy, spacing, sizing, composition, typography hierarchy, responsive visual translation, or critique behavior.
- `docs/specs/joedesign-typography-scale-core-v0.1.md` is the canonical typography and scale doctrine. Read it before changing type roles, type scale, font-family/weight strategy, reading measure, line-height, tracking, focal scale, or responsive typography behavior.
- `docs/specs/joedesign-reference-intelligence-core-v0.1.md` is the canonical reference doctrine. Reference Intelligence is CLOSED; do not redesign it during Color Core work.
- `docs/specs/joedesign-color-contrast-core-v0.1.md` is the canonical Color / Contrast doctrine. Read it before changing semantic color roles, contrast hierarchy, accent ownership, surface/layer color, state color, accessibility contrast behavior, or responsive/theme color translation.
- `docs/superpowers/plans/2026-09-06-joedesign-color-contrast-core-v0.1.md` is the implementation plan for this phase. Follow its TDD and Smoke G gates.
- Any branch that changes shipped `skills/joedesign/**` bytes invalidates the recorded Astra semantic/smoke evidence for branch readiness. Refresh skill hashes and fresh Astra evidence after runtime changes.
- Ship one public skill, `joedesign`. Keep project-specific visual truth in the consuming project's root `DESIGN.md`, not in this repository's global instructions.
- Preserve Product authority, user acceptance, and the exact shared-contract boundary pinned in the spec. Source JOENESS and JOEFLOW/Product repositories are read-only inputs.
- No competitor runtime/vendor payload, inherited JOENESS behavior, installer framework, palette database, automatic theme generator, router, or additional subsystem without demonstrated need. Keep personal installation unchanged during development.
- Write failing contract tests before behavior changes. Recorded decision replay is not a substitute for fresh runtime smoke or actual rendered evidence. Changed skill bytes require fresh decision evidence.
- Preserve earlier failure evidence. Do not run BIO competition as part of this phase.
