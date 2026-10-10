# Unified-core main integration validation

The user authorized commit, push and main integration after the three behavioral
trials, followed by real use. Version remains `0.3.0-dev`; no release tag, additional
installation or user visual acceptance is created by this integration.

Included: the single public operating core and internal harness; measured design
conformance and scoped producer/consumer linkage; preserved split-package history;
regression and actual assisted behavioral evidence. Detailed rationale and limits
remain in CHANGELOG and the preceding evaluation directories.

Before committing:

- Fetched origin; `main` and `origin/main` remained at `0efacd8` with no intervening
  remote changes. The unified branch starts at that same base.
- Python regression: 130 PASS, no skips; existing Playwright and Edge configured.
- Historical Node regression: 14 PASS, no skips.
- Artifact audit: 56 protected inputs unchanged; current package equals all 28
  pinned behavioral-test files; original freeze hashes unchanged; retained frame
  bytes verified, including explicitly archived failed attempts.
- All 28 staged package blobs equal the validated working files byte-for-byte.
- Git whitespace checking uses `cr-at-eol,-blank-at-eof` to preserve existing
  Windows bytes and the pinned visual-translation document's final blank line.
  No package was reformatted to silence those byte-preservation notices.

Logs are adjacent. The earlier new/repair/extension outcomes (54/32/249 PASS)
remain under `../behavior-forward-20261010/`; they were not rerun or relabeled as
unassisted behavior. Historical no-push statements describe those earlier phases.
Git history and remote refs identify the integration commit; this record does not
claim that a planned push succeeded before it actually occurs.
