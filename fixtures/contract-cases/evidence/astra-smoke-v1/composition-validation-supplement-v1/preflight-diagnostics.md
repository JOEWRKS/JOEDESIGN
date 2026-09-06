# Pre-Producer controller diagnostics

No Producer was invoked when these occurred; no fixture, skill, test, case, rubric or expected answer was changed to resolve them.

1. `inspect-v1-diagnostic.mjs` produced preserved `baseline-browser-readback.json` with requiredCopyPresent=false on both viewports, while all local actions/reselection/reset/storage/network checks passed. Actual screenshots and innerText show CSS text-transform produced `FIELDLIGHT RENTALS` and `INCLUDED EQUIPMENT`; case-sensitive substring matching against source-case labels was wrong. A read-only reproduction confirmed exact=false and caseFold=true. The controller-only inspector now case-folds visible text comparison. It still observes actual visible text and exact selected-state results. Corrected output is a new artifact, not an overwritten failure.
2. First `freeze-v1-diagnostic.mjs` failed with Node EISDIR at SHA reading because NUL-delimited git ls-files yielded one final empty item. Reproduction confirmed last entry=""; filtering empty delimiter entries fixes only the controller file enumeration. No preflight.json had been created, and no native launch occurred. `before.json` had been successfully captured; it is not rerun or overwritten.

These are tooling diagnostics, not Producer/design failures. Original helper revisions remain external; compact diagnostic/output evidence is shipped.
