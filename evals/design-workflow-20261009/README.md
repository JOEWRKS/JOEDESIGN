# Design workflow reinforcement — 2026-10-09

Scope fixed before implementation: improve the Harness entry workflow and existing
local runner. Preserve frozen core, prior evidence, installs, FnBShop and unrelated
dirty work. No install, commit or push in this task. Do not resurrect the rejected
production-relationships/dependency-guard experiment.

## Expected outcomes

1. New visual direction and material changes to IA, content scale, screen families
   or task hierarchy require reference selection and a representative composition
   proof before dependent expansion, even when existing tokens remain unchanged.
2. Approved local repairs preserve their scope without unnecessary research or
   rebuilding. Missing approval, DRAFT and unchanged CSS values do not justify that exception.
3. OMD is required for unresolved new/material reference decisions; inspect originals
   and translate relationships. Other research supplements this method, not silently replaces it.
4. Actual R/C1 specialist review and independent critique distinguish composition
   quality from source/token/functional conformance. Missing evidence is unresolved.
5. The runner requires an explicit work kind and proof target family before a writer.
   It observes/reviews that family first; failure or uncertainty prevents an expansion
   writer. Expansion rechecks all targets including the proof, on the new build.
6. Review-only never gains write authority. Interrupted expansion resumes without
   repeating a completed proof; changed inputs/evidence remain stale. Existing limits apply.
7. Harness instructions reach each runtime role and changes invalidate cached execution.

Verification: meaningful runner integration regressions with explicitly synthetic
process/capture fixtures; Node v0.2 and Python regression; skill validation; source/
install integrity. These do not prove actual model compliance or visual quality.
Real-project forward use remains separate. The CLI controls its own launches, not
arbitrary edits made outside it; certification and user acceptance remain separate.

## Implemented

- Harness entrypoint now starts with the three work kinds, explicit reclassification
  triggers, source/OMD decisions and the proof-before-expansion route. It names the
  actual specialist responsibilities and separates whole-screen composition from
  technical and token conformance. Other skill defaults do not displace the user's
  chosen method. Direct-tool/non-Git work follows the same method in existing records.
- Production runtime requires work_kind and proof_target_ids covering all contracted
  states/viewports of one representative family. Invalid/missing scope blocks before
  any writer; local repair cannot include a second family under this shortcut.
- The proof gets its own implementation, capture, R/C1/conditional C2 and critic.
  Only a completed proof review permits the expansion phase. FAIL/UNVERIFIED cannot
  be offset by technical passes. Expansion captures/reviews every target again on
  the changed build. Review-only remains read-only and needs no production fields.
- Each role receives the Harness entrypoint alongside the assigned specialist.
  Guidance hashes invalidate stale resume. Completed proof is reused after a failed
  expansion step; altered proof capture bytes invalidate completed resume.
- Local reports list phase, target_ids and unreviewed_target_ids; the original seven
  policy artifacts and certification semantics remain intact.

## Verification

- First focused execution suite: **23 PASS** (`execution-tests-first.txt`).
- Final Python suite: **112 PASS**, no skip/failure (`python-tests.txt`), including
  eight new scope/order/uncertainty/resume/guidance regressions.
- Node v0.2: **14 PASS**, no skip/failure (`node-tests.txt`). **126 total**.
- Browser integration used the already available Playwright runtime and Edge against
  an isolated synthetic click-state page; no dependencies or product files installed.
- Skill quick_validate, Markdown references/anchors and source whitespace checks pass.
- `integrity.json` records the seven changed source/test files and their hashes.
  All other 66 baseline files, including frozen core and both installations, match.
  Pre-change source snapshots are preserved under `.local/design-workflow-20261009/`.

These tests exercise actual controller code with synthetic role/capture responses;
they are not live specialist or aesthetic evaluations. The browser integration tests
capture mechanics, not the quality of a design. The work-kind and representative
family selection still require honest design judgment; a string cannot prove them.
The runner blocks its expansion call, not arbitrary writes by an external agent or
an agent violating the instructed phase inside a shared component file. Independent
host enforcement and authenticated review are still unavailable.

The new runtime fields are an intentional fail-closed change for production. Old
runtime files need an explicit scope decision; old saved runs are not rebound to the
new policy. The implementation extends the previously uncommitted execution work;
it must not be represented as an independently shipped three-document patch.

Result: local workflow and controller reinforcement verified within these limits.
Fresh model compliance and real-project forward use remain unverified. Install,
commit, push, project UI work and user visual acceptance were not performed here.

## Subsequent integration authorization

After the implementation and verification above, the user requested commit/push,
a complete update log and integration into main. That source-management step is
documented in the root CHANGELOG.md and Git history. It does not change the tested
source hashes, historical observations, installation state or validation limits above.
