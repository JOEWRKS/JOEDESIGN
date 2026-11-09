# Design conformance and completion handoff

Use under the one [operating core](../SKILL.md). JOEDESIGN owns design interpretation,
required check coverage, actual measurement and specialist judgments. The coordinator
or JOENESS owns the related task/roadmap completion condition. This is a scoped
evidence contract, not another progress ledger or a general aesthetic scorer.

## Minimum form: the DESIGN rule-coverage table

Every project that states a measurable visual rule keeps a rule-coverage table in
its root DESIGN.md (see the [template](../templates/DESIGN.md)): one row per rule
with the check that measures it, its spot check, the layouts, sizes and states it
runs on, and what it leaves unmeasured. Hand-written audit scripts are fine as checks when each rule
they cover has its own row with that scope. A rule without a check row is unmeasured,
never passed; a "0 violations" result speaks only for the listed rows. The project's
completion Check (JOENESS ROADMAP) points at this table rather than at a script name,
so a script that measures one layout cannot stand for a rule that covers two. After
a change to any file the table lists, the rows of every affected rule run again.
With the harness, the pinned JSON baseline below is the machine form of the same
table and must agree with it; without the harness, the table is the contract.

A check row is trusted only after its own spot check: on one target, compare the
check's reading with a direct observation of the quantity the rule itself names. A
rule about the visible gap between two cards is observed at the rendered edges a
person sees (shadow included), not at a wrapper element the script happens to select.
When the two readings differ, the check or the row is wrong and is fixed before the
result counts. Every row records this in its Spot check cell: the target with both
readings, or "not spot-checked". An empty cell, or a row inherited without a recorded
comparison, means not spot-checked, and a spot check on one row says nothing about
another. Approval of a value does not make an unspot-checked row true.

Reports give design-check results in one results list, one line per check that ran,
each line in the form `check | result | sizes x states, mode | rendered or code |
spot check` (the target with both readings, or "not spot-checked"). Side checks such
as overflow, clipping and scroll, before/after comparisons, and each fix take their
own line. A defect counts as fixed only after one direct observation of the fixed
thing on a target that showed it (for clipping or overflow: the visible edges in a
capture, not the check's count). A fix line's result is `fixed` when its spot check
cell holds that observation, otherwise `changed`; a `changed` fix keeps its issue
open, and the report text, ISSUES and ROADMAP use the cell's word. Outside the list,
the summary line included, every design-check pass, count, "fixed" or "no failures"
is followed by a parenthesis copied from its line: (sizes x states, rendered or code,
spot check outcome); a sentence with no room for it names the check and leaves the
outcome to its line. "939/939 passed" alone, or "the check passed, but ...", is a
count, not a result. A line that is not spot-checked is never listed as resolved,
verified or done. Before a report is sent, the whole message is written to a file
and run through `scripts/report-check.mjs`, which flags a missing results list (a turn
with no design check says `design checks: none ran` instead), a fix line whose result
is not `fixed` or `changed`, a check outcome stated outside the list without its
scope, rendered-or-code and spot check outcome, and a `changed` fix named under 해결;
the file is corrected until the script prints `report-check: ok <chars> chars <sha8>`,
and that stamp line ends the sent text so `--verify` can confirm the checked text is
the sent text. The script reads the form of the text, not the truth of a number.

## Fix the required scope before implementation

Read the actual project's DESIGN source and approval scope. Map each applicable
rule to its required screen/state/viewport and method. Check that mapping against
the source with a reviewer other than the implementation's own completion judgment.
Do not blindly copy a fixture, infer approval from current CSS, or make the user
transcribe machine fields. Preserve mandatory rules and any unresolved authority.

The consumer/coordinator stores the resulting baseline hash separately from the
producer's receipt. Criterion removal/relaxation, target reduction and authority
changes need a scoped reason and the appropriate authorization; prepare a new
reviewed baseline and pin rather than silently updating the old expectation.
The tool detects changes relative to a pin; it cannot prove the first mapping was
complete, the authorization reference was genuine, or both files were not rewritten.

Baseline is a JSON file with schema `joeness.review-baseline.v1`:

- `scope_id`, `authorization_ref`: the actual affected outcome and scope/approval locator.
- `authority`: nonempty `{path,sha256}` list of current project-relative DESIGN/approved
  source files. Changed source bytes invalidate this baseline until reviewed.
- `targets`: the exact current intent target objects (route, state, viewport etc.).
- `rules`: `{id,source_ref,target_ids,methods}` list, methods `geometry`/`specialist`.
  This independently reviewed inventory defines coverage; every rule/target/method
  pair requires a check. Missing coverage is blocked, not inferred to be irrelevant.
- `required_checks`: `{check_id,rule_id,target_id,lane:"visual",method,criterion,
  criterion_sha256,inputs}`. IDs unique. Criterion hash is canonical JSON SHA256
  (recursive key sort, compact UTF-8, arrays ordered). Inputs name every relevant
  built/source asset, shared style and runtime/configuration condition for that check.
- `required_lanes:["visual"]`, `required_acceptance:true` may be supplied. Visual
  conformance alone never grants acceptance or unrelated implementation/technical success.

Inputs use NFC POSIX relative paths contained in the project. Their fingerprint is
SHA256 of compact UTF-8 JSON `[[path,sha256(file bytes)],...]`, sorted by UTF-8 path
bytes, no trailing newline. Include the actual served output and its build/runtime
dependencies; source files alone cannot prove the server is serving that build.
Bind captured route/state/viewport as well. A consumer can detect changed listed
inputs, not undisclosed dependencies or a dishonest server/build correspondence.

For operational scopes, include the target's served entry/output, imported runtime
modules, state/data inputs, shared styles and relevant fonts/images. Corroborate
this list with actual browser requests and response bytes in the required state;
requests alone do not reveal every lazy, conditional or future dependency. Keep
other routes, review-board exports and old evidence out unless they affect this
check. Test that unrelated evidence preserves proof, a family-specific output
invalidates that family, and shared style changes invalidate all affected checks.
Shared files remain whole-file dependencies; do not claim selector-level precision.

## Measure relationships in the actual render

Geometry criteria support these bounding-box measurements:

| kind | Fields | Actual measurement |
|---|---|---|
| pair | from, to, from_edge, to_edge | Corresponding observed elements' edge difference |
| gap | container, items, axis x/y | Consecutive matching child rectangles in DOM order, across every container |
| inset | container, items, edge | Container edge to the union of all matching child rectangles |

Each criterion also has `expected_count`, `min`, `max`, `tolerance`, optionally
`max_spread` for repeated-role consistency. Use project-derived values, including
intentional responsive exceptions. No global 8/16/40 rule is installed. Selectors
must cover all applicable instances; missing/hidden elements and unexpected counts
remain UNVERIFIED. A wrapping row may need its own explicit target/selector rather
than a linear-gap interpretation. Element rectangles are not glyph ink bounds;
line height, borders and optical corrections require the correct scoped criterion.
Map each endpoint to the source's semantic object: image-to-text means the actual
text element's box, not the outside of a padded text wrapper. Before fixing the
baseline, inspect the matched elements and their box relationships. A selector
that matches and returns numbers can still encode the wrong requirement. Preserve
mapping mistakes and their corrections as validation history; do not relax the
expected value to fit a mistaken selector or present this mapping as independently
reviewed when it was not.

The collector measures after actual state actions/assertions and font readiness.
It records rectangles and computed box diagnostics, not just declarations. A gap
therefore includes stacked margin/gap and fixed-height/auto-margin effects. Inset
uses all children, avoiding a false measurement from only the last, shorter child.
Failures do not erase the observation; fix and capture a new candidate/output.

Specialist criteria have `claim_id`, `category`, `expected` matching a required
STATE_MATRIX claim. The existing ordered specialist and independent critic report
must bind the same baseline, inputs, build, target and real evidence. Missing review
or any unresolved verdict remains blocking. DOM geometry does not replace whole
composition, motion-quality judgment or user acceptance.

## Execute and consume

For `run`, add to the existing runtime settings:

```json
"design_validation": {
  "baseline": "C:/approved-scope/design-checks.json",
  "baseline_sha256": "<independently pinned raw file SHA256>"
}
```

The runner validates coverage before writing, passes pinned checks and current
per-check fingerprints to capture.mjs, evaluates the resulting observations and
binds specialist findings. Required failure/unknown blocks phase completion and
expansion even when generic reviews pass. It writes `DESIGN_CONFORMANCE-<cycle>.json`
beside the existing execution report. Changed receipts/evidence cannot be reused on
resume. A proof-only receipt is incomplete for a larger consumer baseline.

For direct tools/non-Git projects, use the same baseline and collector protocol:
capture request `design` has baseline_sha256, input_fingerprints and required checks;
each observation contains the exact target, build_id, frames, and measured design
data. `frame_hashes` records each frame's SHA256 at capture time; later frame changes
remain UNVERIFIED. Produce these from actual observation, never invent them to fill a receipt.
The Python `harness.conformance.bindings` helper computes current input bindings.
Then evaluate using the copied skill's absolute CLI path:

```text
python <joedesign>/scripts/harness_cli.py verify-design --project <root> --baseline <file> --baseline-sha256 <pin> --observation <actual-observation.json> --output <new-result.json>
```

Repeat --observation for other targets. Add --reviews for the runner-produced
DESIGN_REVIEWS file when specialist checks are required. Missing observations are
UNVERIFIED. Exit 0 means only these required checks passed; exit 2 blocks them;
exit 1 means invalid/missing input. No exit value grants exact user acceptance.

Receipt schema is `joedesign.conformance.v1`: scope_id, baseline_sha256, results,
unresolved, acceptance=NOT_GRANTED. Each result has check_id, target_id, method,
criterion_sha256, status, input_fingerprint, evidence[{path,sha256}]. Extra measured
values explain geometry verdicts. Evidence paths can be absolute in the isolated
artifact directory; authorize that directory explicitly in the consumer.

JOENESS consumes this exact file against its independently pinned expectation,
recomputes current inputs/evidence, and blocks the related completion lane for
missing, malformed, failed or stale checks. JOEDESIGN does not update the product's
canonical TASK/ROADMAP for it. Use separate scoped baselines so independent work
continues; the consumer may explicitly reuse unchanged checks under reviewed new
baselines. Never claim an uninstalled/unconnected consumer is protecting a project.

For an append-only DESIGN comment or an independently reviewed unrelated section,
the read-only [bounded impact diagnosis](impact.md) can identify old geometry
evidence that remains applicable. It produces candidates, never a new PASS receipt
or reuse permission. CSS/runtime changes and specialist judgments need fresh proof.
Use only a separately reviewed, explicitly pinned consumer transition to reuse a
candidate; ordinary stale-evidence checks still apply without that transition.

Local files and process records remain unauthenticated. Neither tool prevents
someone changing both pin and baseline, forging observations, bypassing the CLI,
editing a work record directly or saying “done” in chat. Protected host/CI enforcement
and authenticated source/approval events are separate. Report those limits plainly.
