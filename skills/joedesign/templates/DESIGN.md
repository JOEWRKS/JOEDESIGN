# Project Design

**Reporting:** follow the `## Report Form` section below exactly (보고는 `## Report Form` 절을 그대로 따른다).

**Status:** DRAFT
**Revision:** 1
**Product Authority:** <pointer>

<!-- Compact seed, not a required form. Keep only needed project decisions;
unknown/empty is valid. Do not retranscribe settled source specifications. -->

## Visual Sources and Approval Scope

<!-- Original artifact/version + direct real-asset pointers + surface/state/viewport.
Distinguish approved visual targets from ordinary references. Supplied ≠ approved.
Record actual approval and its scope; do not fabricate approval or source facts. -->

## Project Decisions

<!-- Only needed relationships: source observation → preserve/change → concrete
implementation/native-role mapping → expected observable difference.
Distinguish measured / estimated / proposed / approved values when relevant.
Include relevant hierarchy/flow, spacing, type, color, imagery/crop or responsive/
state invariants; do not fill every craft topic or replace originals with prose. -->

## Token Roles

<!-- Required whenever a shared token (shadow, spacing step, radius, type size, color)
is used by more than one part. One row per role; the same role uses the same token
at every size. A part with no row has no token claim. Status per row: measured
(read from the shipped code), proposed, or approved (with the approval locator). -->

| Role | Parts | Token / value | Status |
| --- | --- | --- | --- |

## Rule Coverage

<!-- Required whenever this file states a measurable rule. One row per rule: which
check (script/command or manual observation) measures it, on which layouts, sizes
and states, and what it leaves unmeasured. A rule with no check is unmeasured, never
passed; "0 violations" means only the listed rows. The project's completion Check
(JOENESS ROADMAP) points here. After a change to any listed file, re-run the rows
of every affected rule. With the harness, the pinned JSON baseline must agree with
this table; without it, this table is the contract. Before a row counts, spot-check
it: compare the check's reading on one target with a direct observation of the
quantity the rule names. Fill the Spot check cell in every row with
"<target>: check N / observed M", or "not spot-checked"; an empty cell means not
spot-checked, and one row's spot check does not cover another row. When a result is
quoted elsewhere (report, ROADMAP), quote it with this row's layouts, sizes and
states, and with "not spot-checked" when that is the row's state; such a result is
not listed as resolved or verified. -->

| Rule | Check | Spot check | Layouts | Sizes | States | Unmeasured |
| --- | --- | --- | --- | --- | --- | --- |

## Report Form

Any session that changes a file listed in Rule Coverage, with or without JOEDESIGN
loaded, reports design-check results in one list, one line per check that ran:
`check | result | sizes x states, mode | rendered or code | spot check` (the row's
Spot check cell, or "not spot-checked"). Each fix takes its own line; its result
is `fixed` only when its spot check cell holds a direct observation of the fixed
thing on a target that showed it, otherwise `changed`. A `changed` fix is an open
issue: it goes under 남은 문제 (remaining work) in the report, ISSUES and ROADMAP,
never under 해결 (resolved). Outside the list, a pass or count carries its
parenthesis (sizes x states, rendered or code, spot check outcome). A turn with no
design check says `design checks: none ran`. A result that is not spot-checked is
not resolved, verified or done. A change that moves, overlaps, hides or merges an
existing element lists, under `## Display before/after`, two lines per element:
`before: element | content shown | route` and `after: ...` (`hidden` when gone).
A pair that differs stays `product decision pending` until the product definition
changes; a matching pair is a design decision.

## Open Decisions / Evidence Boundary

<!-- Missing source facts, conflicts and unobserved targets. Original and rendered
artifact pointers when relevant. Technical/visual checks and user acceptance remain
separate. Preserve existing custom sections instead of forcing this shape. -->

## Amendment Rule

Only explicit user approval promotes DRAFT to APPROVED. Preserve APPROVED Rev N
while proposing a separately labeled DRAFT Rev N+1 in this same file. Replace the
active approved rule set only after proof and explicit approval. Local refinement
within approved intent does not automatically create a material revision.
