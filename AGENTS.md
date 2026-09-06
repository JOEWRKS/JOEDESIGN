# JOEDESIGN repository

- `docs/architecture/JOEDESIGN_OPERATING_MODEL_V1.md` is the canonical top-level role map and operating model. Read it first when changing system boundaries, authority order, process ownership, or how Product Definition, JOEFLOW, JOEDESIGN, references, DESIGN.md, implementation, verification, and user approval fit together.
- `docs/specs/joedesign-v0.1.md` is the implementation baseline; its current handoff stop is review, not competition readiness.
- `docs/specs/joedesign-craft-core-v0.1.md` is the canonical native craft doctrine. Read it before changing visual hierarchy, spacing, sizing, composition, typography hierarchy, responsive visual translation, or critique behavior.
- `docs/specs/joedesign-typography-scale-core-v0.1.md` is the canonical typography and scale doctrine. Read it before changing type roles, type scale, font-family/weight strategy, reading measure, line-height, tracking, focal scale, or responsive typography behavior.
- `docs/specs/joedesign-reference-intelligence-core-v0.1.md` is the canonical reference doctrine. Read it before changing reference provenance, evidence quality, known/unknown handling, relationship extraction, conflict handling, or external corpus policy.
- Any branch that changes shipped `skills/joedesign/**` bytes invalidates the recorded Astra semantic/smoke evidence for readiness. Refresh the skill hashes and fresh Astra evidence before claiming competition readiness for that branch.
- Ship one public skill, `joedesign`. Keep project-specific visual truth in the consuming project's root `DESIGN.md`, not in this repository's global instructions.
- Preserve Product authority, user acceptance, and the exact shared-contract boundary pinned in the spec. Source JOENESS and JOEFLOW/Product repositories are read-only inputs.
- No competitor runtime/vendor payload, inherited JOENESS behavior, installer framework, or additional subsystem without demonstrated need. Keep personal installation unchanged during development.
- Write failing contract tests before behavior changes. Run `node --test tests/joedesign-contract.tests.mjs`; recorded decision replay is not a substitute for fresh runtime smoke or actual rendered evidence. Changed skill bytes require fresh decision evidence.
- Preserve earlier failure evidence. Do not run BIO competition as part of this MVP.
