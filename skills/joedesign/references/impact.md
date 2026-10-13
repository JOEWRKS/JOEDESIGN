# Bounded DESIGN impact diagnosis

Use this only when existing DESIGN bytes are preserved and a comment or unrelated
section is appended. Review applicability, defaults, exceptions and new requirements
against the original before treating it as unrelated. A heading or HTML comment is
not evidence of semantic independence. Original authority changes still need their
own authorization; this tool does not grant it.

```text
python <joedesign>/scripts/harness_cli.py inspect-impact --project <root> --request <file> --request-sha256 <pin> --review-sha256 <independent-pin> --output <new-report>
```

Repeat `--evidence-root` to admit old absolute capture paths outside the project.
Request/source paths stay inside the project. Inputs are pinned and reread before
return; output cannot overwrite an existing file. Exit 0 means every required check
is a candidate; exit 2 means invalid, unknown or rerun checks; exit 1 is an execution
or output error. No exit value authorizes reuse or user acceptance.

Request `joedesign.impact-request.v1` contains pinned `{path,sha256}` references
`old_baseline`, `new_baseline`, `old_result`, `served`, `review`, and
`authority_before:[{path,snapshot:{path,sha256}}]`. The snapshots preserve original
authority bytes. Old/new baseline definitions must be identical except authority
hashes and `authorization_ref`; rules, targets, coverage, criteria, acceptance and
opaque fields cannot change. Only root `DESIGN.md` may change in this version.

`review` has schema `joedesign.impact-review.v1`, `scope_id`, `transition_sha256`
(canonical JSON SHA256 of the request excluding `review`), distinct nonempty
`implementation_context`/`review_context`, and substantive `scope_analysis`.
`authority_analysis` covers every authority path exactly once with `path`, `kind`
(`UNCHANGED`, `COMMENT_APPEND` or `UNRELATED_SECTION_APPEND`), and `rationale`.
`checks` contains unique known `check_id`, `verdict` (`UNAFFECTED`, `AFFECTED`,
`UNKNOWN`), `rationale`, pinned `source_refs`, and `blocking_findings`.
Missing review stays unknown. Current rejection/blockers cannot become reuse.
The independent review pin is a separate CLI expectation, not inferred from the
request. Context labels and local pins do not authenticate the reviewer.

`served` has schema `joedesign.served-build.v1`, `scope_id`, current
`baseline_sha256`, and one row per target in `targets`. Each row has the complete
`target`, observed `build_id`, `dependencies_complete`, `limitations`, and
`resources:[{path,sha256,response_sha256}]`. Actual served response bytes must equal
current runtime inputs; coverage must include exactly all declared inputs for that
target. Collect and review the real scoped dependency set. Never fill these fields
from source hashes alone or infer completeness from an initial request list. Late,
conditional or unmapped resources remain unknown until observed. A record is local
evidence, not proof of server identity or future responses.

Output `joedesign.impact.v1` binds these refs (semantic review under key `review`),
authority raw deltas, complete current check coverage, current fingerprints,
previous results/evidence, read integrity and counts. Per-check classification is
`reusable-candidate`, `rerun` or `unknown` with reasons. Its `reuse_authorized` is
always false, `acceptance` is `NOT_GRANTED`, `trust` is `LOCAL_UNAUTHENTICATED`.

Geometry candidates require the old PASS and its exact criterion/target/input/build,
unchanged frames, and a fresh evaluation of the immutable old measurements against
the unchanged criteria. This is not a new browser measurement. Previous failure or
unresolved evidence remains nonreusable. Specialist checks require fresh scoped
review. CSS, font, asset or other runtime byte changes require observation; this
version does not analyze CSS/cascade/selector precision.

JOENESS owns the separate pinned consumer review and transition. Until that
transition is implemented, reviewed and connected, old authority-stale receipts
remain blocked. Keep old receipt/baseline/frames immutable; do not repin them or
write a replacement PASS receipt to bypass the consumer. Reuse can satisfy only the
unchanged technical checks, never product closure or exact user acceptance.
