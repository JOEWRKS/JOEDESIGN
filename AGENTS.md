# JOEDESIGN repository

- `docs/specs/joedesign-v0.1.md` is the implementation baseline; its current handoff stop is review, not competition readiness.
- `docs/specs/joedesign-craft-core-v0.1.md` is the canonical native craft doctrine. Read it before changing visual hierarchy, spacing, sizing, composition, typography hierarchy, responsive visual translation, or critique behavior.
- Any branch that changes shipped `skills/joedesign/**` bytes invalidates the recorded Astra semantic/smoke evidence for readiness. Refresh the skill hashes and fresh Astra evidence before claiming competition readiness for that branch.
- Ship one public skill, `joedesign`. Keep project-specific visual truth in the consuming project's root `DESIGN.md`, not in this repository's global instructions.
- Preserve Product authority, user acceptance, and the exact shared-contract boundary pinned in the spec. Source JOENESS and JOEFLOW/Product repositories are read-only inputs.
- No competitor runtime/vendor payload, inherited JOENESS behavior, installer framework, or additional subsystem without demonstrated need. Keep personal installation unchanged during development.
- Write failing contract tests before behavior changes. Run `node --test tests/joedesign-contract.tests.mjs`; recorded decision replay is not a substitute for fresh runtime smoke or actual rendered evidence. Changed skill bytes require fresh decision evidence.
- Preserve earlier failure evidence. Do not run BIO competition as part of this MVP.
