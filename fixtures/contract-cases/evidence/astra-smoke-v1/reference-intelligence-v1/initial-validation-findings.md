# Initial Reference Intelligence validation findings

Source checkout: `d8b35c67205e837318ae49b17333c293ebe44290` on `codex/joedesign-v0.1-reference-intelligence-validation`.

The handoff names `fb8c843629416c3f706c8d9cd72eb9c1f60889d0`. Its two descendants add the handoff and update the AGENTS pointer only. No shipped skill or expected-answer change was made by this validation.

The unmodified four-file Node suite returned **40 tests / 25 PASS / 15 FAIL**. Exact output is preserved in `initial-contract-tests.txt` in this directory.

## Stale semantic provenance: 14 failures

Cases 02–15 rejected the previous observed.json because its SKILL.md hash was `3620558694b35fdc86fc37d146cb1b8eb8ea60c630d60f42a2c09555b2ccf9d3`, while the current shipped SKILL.md is `f4395b40d01f0d73ecf869bed17fa0903eab27582556efc71eec49f7bc6e9ea1`. This is a freshness failure, not an observed new semantic response. A separate fresh native replay is required. The prior Case14 report and responses are archived byte-for-byte under `fixtures/contract-cases/history/astra-case14-regression-v1/`; the earlier Typography failure history remains untouched.

## Package allowlist: one independent failure

`tests/joedesign-contract.tests.mjs`, test 16, line 78 rejects:

`Unexpected runtime/vendor surface: docs/architecture/JOEDESIGN_OPERATING_MODEL_V1.md`

The test walks the entire repository except .git. Its exact path allowlist includes the four specs but not the mandatory operating-model document or the new active handoff. Both documentation files are outside the admitted fixtures prefix. The first rejection is the operating-model document; inspection also identifies the handoff omission, without claiming a second separately executed failure.

The operating-model document already exists at the handoff's named starting commit. Neither new semantic responses nor smoke evidence can resolve this path-level assertion. No document was removed, test bypassed, allowlist edited, expected action changed, or runtime modified to obtain a green result. Resolution belongs to the Program Lead outside this validation-only execution.

All eight Reference Intelligence static assertions passed in this initial run. This does not override the full-suite failure. Readiness must remain NOT_READY while any required gate fails.
