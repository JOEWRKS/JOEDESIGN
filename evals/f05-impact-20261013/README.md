# F05 bounded impact implementation — 2026-10-13

T035 Bundle C, authorized by the user in Local QA Manager message
`01a134a6-354f-7891-8e31-8be7b9e857bf`. Existing main integration is complete;
this follow-up is uncommitted source work, version remains `0.3.0-dev`.
No product, personal installation, old receipt, baseline pin or release changed.

## Source and current validation

- `skills/joedesign/scripts/harness/impact.py`: pinned read-only diagnosis of
  append-only DESIGN comments or independently reviewed unrelated new sections.
  Full baseline context, required coverage, target, runtime, served bytes/build,
  immutable measurements/frames and review bindings must hold. Geometry only.
- `harness_cli.py inspect-impact`: separate request/review pins, explicit evidence
  roots, exclusive new output. Always `reuse_authorized:false` / `NOT_GRANTED`.
- Conditional package reference `references/impact.md`, linked from conformance;
  no extra public skill or operating core. CONTRACT.md records this scoped contract.
- Python **142/142**, no skips; historical Node **14/14**, no skips. Logs adjacent.
  The 12 new tests include CLI output immutability, positive comment/section,
  missing/mismatched pins, criterion/coverage/target/acceptance changes, CSS bytes,
  served mismatch, late dependencies, old failure, current rejection, partial review,
  frame corruption and a forged PASS contradicted by raw measurements.
- Manager initially found CRLF section appends incorrectly blocked: 14/15 synthetic
  cases. Original raw prefix equality was retained and LF/CRLF append boundaries
  accepted. Regression covers both. Manager rerun **15/15**, actual diagnostic **2/2**.
  Failure history remains in Manager `f05-diagnostic-manager.json`; corrected results
  in `f05-diagnostic-manager-green.json`, actual review in `f05-actual-manager.json`,
  under `D:/JOEWRKS/JOEQASAM/evidence/t035-joe-implementation/`.

## Actual evidence, distinct from synthetic tests

`build-fixtures.py --output NEW_DIR` uses the existing capture.mjs/Edge runtime.
Saved final paths: `.local/f05-impact-20261013/real-v1/P01` and `P02`.
`real-v1/summary.json` contains exact pins, preserved-input hashes and commands are
in each `diagnostic-process.json`. Do not overwrite or relabel these records.

Each static fixture first rendered four checks (16/40/8/32 px), saved actual box
measurements and three PNGs, then changed only DESIGN by a comment (P01) or an
explicitly print-only future section (P02). `collect-served.mjs` subsequently
navigated the page and hashed actual HTTP response bytes against the current file.
It made **zero geometry reads and zero screenshots**. The fixture is one HTML file
with inline CSS and no JS/assets/dynamic dependencies; this does not prove a real
application's lazy dependency inventory. No live product was edited or tested.

The producer's semantic review files are clearly labeled drafts for independent
inspection. Manager separately read authority/HTML, inspected the PNG and recomputed
16/40/8/32 from captured boxes; confirmed these exact additions do not affect web
rules/defaults/exceptions/coverage. This is locally recorded review, not authenticated
user acceptance or universal semantic classification.

Per positive case: **4 old checks become candidates without 4 new DOM measurements
or 3 new PNGs**. One current browser navigation/response collection and explicit
semantic/consumer reviews remain necessary. Total wall-time, manual review cost and
benefit on dynamic production projects have not been measured. The existing gate
still rejects all four as STALE until the separately reviewed transition is supplied;
diagnosis alone is not the completed F05 reuse capability.

## Isolated package and remaining sequence

`verify-isolated.py --output NEW_DIR --fixtures real-v1 --gate <JOENESS source>`
creates an exact 30-file copy, executes both producer positives and both existing
consumer stale cases. Recorded at `.local/f05-impact-20261013/isolated-r2/summary.json`:
**30/30 raw SHA matches, four CLI expectations passed**; installed 28 files, original
fixture inputs and source package unchanged. Python uses `-B`; caches are not package
content. This is an isolated copy, not skill discovery or a personal installation.

Next: JOENESS diagnostic consumer actual connection → Manager review → explicit-pin
limited gate reuse, positive/negative actual and isolated joint execution → Manager
managed installation decision. Preserve old failures, rejection and acceptance gates.
Source snapshot/patch and pin manifest accompany the handoff. No merge/tag now.

Managed installation preparation: take an exact complete inventory of the current
personal package, back it up outside all skill discovery roots, compare the backup
byte-for-byte, replace only this authorized package with the reviewed isolated bytes,
verify the exact complete inventory and rerun installed producer/consumer linkage.
Keep the backup for recovery. Recheck source/install drift before any mutation; a
changed package needs review. No such installation has been performed in this phase.
