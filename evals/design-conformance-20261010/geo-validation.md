# GEO source snapshot validation — 2026-10-10

The user's further validation request was exercised on actual GEO application bytes
in an isolated snapshot, without installing the candidate or changing the product.

## Scope and results

Source: `D:/JOEWRKS/GEOTest/FnBShop`, runtime in
`examples/geo-fresh-market/wireframes/`. Original files were only read. The snapshot
contains DESIGN, runtime source, built HTML, styles and assets. Each copy was
hash-compared with its original; original hashes were checked again after capture.

Expectations were mapped from DESIGN before measurement: product listing at
320/390/768/1023/1024/1440 and collections at 320/390/1440, **9 targets, 51 checks,
186 measured relationships**. Scope: header height and narrow-header spacing,
all 9 products' name/price/review gaps, mobile/desktop image-to-text spacing,
both campaign cards' content gaps and top/bottom insets. This is tool validation;
the mapping has not received an independent completeness review.

Input fingerprints deliberately cover the whole copied runtime tree, including
review-board and older screenshot files. This is conservative test isolation,
not a production dependency map: an unrelated screenshot change would invalidate
all 51 checks. Do not adopt this baseline for normal project operation. Before
activation, map each check to its actual served output, shared styles/scripts,
fonts/assets and state dependencies, and test unrelated-file non-invalidation.
JOENESS independently identified this over-broad scope during review.

| Scenario | Result |
|---|---|
| Corrected mapping, original snapshot | 51 PASS; producer exit 0 |
| JOENESS consumes scoped visual result | exit 0; project_complete false |
| Same result claimed as complete | exit 2; no overall user acceptance |
| Copied CSS changed after original capture | old result rejected, exit 2 |
| Copied card gaps changed from 8 to 24 | 12 FAIL, 39 PASS; producer exit 2 |
| JOENESS consumes that current failing result | exit 2 |
| Copied CSS restored | original scoped result usable again, exit 0 |
| Same target ID, changed viewport/state/route | old observation UNVERIFIED; regression passed |

The injected failures cover 108 individual gaps (9 products × 2 gaps × 6 widths).
Only the snapshot CSS was changed and restored. Original product files were not edited.

## Mapping error discovered

First run `geo-r1` measured `.product-photo` to `.card-content`. That wrapper has
top padding: its outside edge is not the start of the text. It returned 0px and
three false failures, with 48 other checks passing. Source padding, captured boxes
and screenshot demonstrated the error. `geo-r2` measures to `.card-content h3`;
the expected values remain mobile 8 / desktop 16.

This was a measurement-mapping error, not a proven product defect. The conformance
module now explicitly requires semantic endpoint review and preservation of mapping
failures. Matching selectors and numbers alone do not prove correct interpretation.

During r1, another product task changed DESIGN (option-label spacing, empty/search
states and home-width clarification). r1 remains a dated snapshot. r2 copied the
updated DESIGN and observed no source changes during its run; those added scopes
are outside this test. Neither result certifies future changes.

## Evidence and limits

Raw runs: `.local/design-conformance-20261010/geo-r1/` and `geo-r2/`.
R2 baseline pin: `51ad469774bbe050001185c14a2cba32af11886c5796115e06e69be52285a713`.
Normal receipt SHA: `6b153aaf41510bef4874e2748fdd43deca93bd4bdc1a3d4e0b6c28cc173d2166`.
Injected receipt SHA: `857e0784bcbcdd8f6bfea01df9214a1e9807d74c6bec1c511c57659e3475b782`.
The injected receipt is stale against the restored snapshot; `injected-visual.json`
records its consumption while the defect was present.

`geo-manifest.json` pins observations, executed runners, receipts and provenance.
The per-run `runner.py` preserves the actual recipe. `run-geo-snapshot.py` reproduces
a new run with explicit product/consumer/output arguments; its later addition
snapshots the consumer to avoid concurrent edits and was not retroactively executed
for r2. R1/r2 recorded the consumer hash at completion; separate independent
consumption is needed to establish the final consumer's result without that limitation.

JOENESS subsequently performed that independent consumption in its own temporary
copy with final consumer `db37a33ce5ee2f9c210e4250b05aef1afb9712bfa6e524a80d39866b4c8c8c23`:
**8/8 expected scenarios passed**, including matching the exact injected CSS to
the 39 PASS / 12 FAIL receipt, stale-input rejection, restoration, omitted check,
changed viewport under the same ID, visual success and complete rejection.
Counterpart evidence:
`D:/JOEWRKS/작업하네스/evals/joeness-setup/runs/2026-10-10-specialist-consumption/geo-consumption-results.json`,
SHA `071ab626d56973a8afe8717c00546342720f9fcb1ac61a34c5e941eacc8aa110`.
This is an independent consumer check, not an independent visual-scope review.

Regression: **129 Python passed, 14 historical Node passed**. Logs are
`python-geo-validation.txt` and `node-geo-history.txt`.
All 46 previously hashed personal/project installation files remain unchanged.

Not established: mapping completeness, independent specialist judgment, whole-design
quality, checkout/my/policy/PDP checks, functional flows, real-device/accessibility
behavior, live model adherence, installed integration, automatic interception of
completion claims, or whole-product user acceptance. This proves an explicit local
path over pinned scope; direct chat/file bypass remains possible. No installation,
product edit, release, commit or push occurred.
