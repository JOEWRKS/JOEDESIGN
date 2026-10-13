# F05 bounded impact contract — candidate source implementation

Scope fixed before implementation: DESIGN append-only comment or reviewed unrelated
section; all other baseline definitions, runtime input bytes, target identity and
observed build remain equal. This document and tests refine F05-ENTRY.md, not a
new product requirement. Diagnostic is read-only, `reuse_authorized:false`.

`inspect-impact --project ROOT --request FILE --request-sha256 PIN
--review-sha256 INDEPENDENT_PIN [--evidence-root ROOT] [--output NEW_FILE]`.
Every referenced input is pinned, root-contained and read again before returning.
Explicit evidence roots admit old immutable capture paths; no source is executed.

Request `joedesign.impact-request.v1`:

- `old_baseline`, `new_baseline`, `old_result`, `served`, `review`: `{path,sha256}`
  under project root. CLI request and semantic-review pins are separate expectations.
- `authority_before`: `[{path: originalAuthorityPath, snapshot:{path,sha256}}]`.
  Snapshot raw bytes must equal old authority hash. Current original bytes must equal
  new authority hash. Authority path set is unchanged.

Semantic review `joedesign.impact-review.v1`:

- `scope_id`, `transition_sha256`: canonical hash of request excluding `review`.
- `implementation_context`, `review_context`: nonempty and distinct; context names
  and local pins are not authenticated actors.
- `authority_analysis`: unique rows for all authority paths:
  `{path,kind:UNCHANGED|COMMENT_APPEND|UNRELATED_SECTION_APPEND,rationale}`.
  Byte prefix/append shape is machine checked; noninterference with global rules,
  exceptions and coverage is a substantive scoped review, not inferred from hashes.
- `checks`: unique known check IDs with `{check_id,verdict:UNAFFECTED|AFFECTED|UNKNOWN,
  rationale,source_refs:[{path,sha256}],blocking_findings:[]}`.
  References identify inspected source material. Missing per-check review is unknown;
  nonempty blockers (including current rejection) never become reusable candidates.
- `scope_analysis`: nonempty explanation of why added material does not change
  applicability, defaults, exceptions or required coverage in this pinned scope.

Current served record `joedesign.served-build.v1`:

- `scope_id`, `baseline_sha256` (new), `targets` unique rows:
  `{target: exactTargetObject, build_id, dependencies_complete:true|false,
  resources:[{path,sha256,response_sha256}], limitations:[]}`.
- Every per-target check input must be covered. Each file and response hash must
  match current bytes. Missing/extra/unmapped dependencies or unobserved dynamic
  conditions require fresh observation. `dependencies_complete` is reviewed local
  collection evidence, never proof of every future dependency or server honesty.
- This record corroborates unchanged served output; it is not a new geometry,
  specialist or user-acceptance receipt. No invented HTTP responses.

Output `joedesign.impact.v1` includes:

- `scope_id`, `request:{path,sha256}`, `transition_sha256`, old/new baseline refs,
  old_result ref, served ref, `review` (semantic review) ref and authority_before snapshots.
- `authority_delta`: raw old/new hashes, kind, appended-byte hash and rationale.
- `checks`: exactly one per new required ID, with definition/target/criterion,
  current fingerprint, `classification:reusable-candidate|rerun|unknown`, reasons
  and the previous immutable check result. No PASS or acceptance promotion.
- `findings`: invalid/conflict/unknown structural or shared-context problems;
  `integrity`: files read and hashes; all reread before report return.
- `reuse_authorized:false`, `acceptance:NOT_GRANTED`, `trust:LOCAL_UNAUTHENTICATED`.

Old receipt scope/baseline/coverage/target/method/criterion/fingerprint must match;
FAIL/UNVERIFIED/unresolved stays nonreusable. Evidence byte hashes are checked.
For every old target, an evidence observation must bind its exact object, old
baseline, fingerprint, old build_id, design measurements and rendered frame hashes.
Only geometry checks are candidates in v1. Specialist checks require fresh scoped
review; old specialist judgments are not recreated from DOM checks. Partial proofs
cannot fill full scopes.

Only authority hashes and authorization_ref may differ between old/new baselines.
Removal, relaxation, target change, acceptance weakening or opaque-context edits
block this v1 transition. Runtime changes are rerun/unknown, not CSS-precision claims.

## Consumer review after diagnostic (separate file; no circular hash)

Proposed `joeness.impact-reuse-review.v1`: `scope_id`, `impact_sha256`, exact old/new
baseline hashes, `old_result_sha256`, `semantic_review_sha256`, confirmed candidate
check IDs and substantive `source_refs`. Consumer receives independent pins for
impact, this review, both baselines and old receipt, and verifies definitions,
inputs, evidence and coverage itself. JOENESS finalizes its exact consumer schema.
No implicit waiver of current user rejection/acceptance requirements.

This separate reviewed transition can later permit limited reuse without rewriting
old receipt, old baseline or old frames. Until source review and joint execution,
the unchanged existing gate must still reject authority-changed old evidence.
