---
name: joedesign
description: "Design, implement and review UI through one operating workflow: inspect visual sources, translate them into the product, prove the key composition, and expand through specialist review. Also use for scoped visual repairs. Not for Product Definition, pure backend work or nonvisual refactors."
---

# JOEDESIGN

This is the single operating core for JOEDESIGN. It governs design decisions,
implementation, observation and specialist review. The harness is an internal
execution mechanism, not another skill or authority the user must select.
User authority and Product meaning govern the work; specialist defaults do not
replace this operating route. Read detailed modules only for the current stage.

## One owner, bounded roles

The coordinating agent is A: it owns scope, assignments, stage transitions and the
integrated result. Product owns meaning; the user owns exact visual acceptance.
A preserves these authorities and cannot vote away a failure or rejection.
I receives the result and remaining limits; it is not an extra reviewer.

**If you received a role assignment**, apply this core within that assignment.
Use its stage, targets, originals, allowed changes and required observations.
Return the scoped result and gaps to the coordinator. Do not restart the workflow,
launch more roles, reinterpret a locked direction or expand the assignment.
A material conflict returns to the coordinator; it does not authorize a workaround.

| Responsibility | Owner and stage input |
|---|---|
| Scope, source selection, stage transitions and integration | Coordinator, using the route below |
| Visual interpretation, composition and source comparison (J) | JOEDESIGN's [visual translation module](references/visual-translation.md); add [visual production](references/visual-production.md) for material composition/assets/motion |
| Implementation and actual observation | Assigned implementer, using originals, the scoped decision and visual modules; responsible for rendered/state behavior |
| Craft (I) | Actual Impeccable skill |
| Content, input and recovery (U) | Actual UI UX Pro Max skill |
| Accessibility and responsive implementation (V) | Actual web-design-guidelines skill |
| Animation or React performance (M/R) | Respective performance skill only when applicable |
| Independent diagnosis | Fresh-context critic, actual evidence and scoped criteria; no builder/reviewer conclusions |

Responsibilities are not a requirement to create an agent for every step. Material
review uses actual specialist skills and the ordered R → C1 → conditional C2 route
in [operation](references/operation.md#raci-as-the-work-route). Role names alone do
not establish skill use. C2 diagnoses conflict, uncertainty or recurring failure.

## Decide the scope before making the screen

Read the request, Product source, root DESIGN.md, originals/assets, scoped approval
or rejection and actual implementation. State the work kind and next stage briefly;
do not ask for facts already available. Reclassify when product or visual scope changes.

The Product source is the project's product definition. When the project has
`product-definition/<slug>/state.json` (JOEFLOW), read `MASTER_PLANNING_SPEC.md`
beside it and the approval state first (`scripts/approval_status.py <state.json>`
from the JOEFLOW skill when it is installed; otherwise the `approval` block of
state.json: status and approved revision), and name that revision as the Product
Authority in DESIGN.md. The definition decides which screens, actions, states,
rules and wording exist; this skill decides how they look. A request that needs a
user-visible behavior the approved definition does not contain (a new control,
screen, state, rule or text) is not decided here: record it as `product decision
pending` (제품 결정 대기) with the missing item and the revision read, send it back
through JOEFLOW's implementation re-entry (DISCOVER/CLOSE for the affected scope;
the user's words passed on by another session are `RELAYED_USER_INTENT`, a feature
added to a running product is `NEW_PRODUCT` scoped to the change), and continue the
visual work the definition already covers. If the user's own request is that
behavior, build what the user specified and keep its product record pending: the
definition is extended in JOEFLOW, not by code or DESIGN.md, and any part of the
behavior the user did not specify is a product question for that re-entry, not a
design choice. The report lists the pending item under remaining work, never as
decided or done. Build on an unapproved revision only when the user directed
implementation before approval, and say so in the report.

| Work kind | Route |
|---|---|
| New direction: no adequate visual target | Source decision → representative composition → review → expansion |
| Material extension/redesign: changed IA, screen families, content scale, task hierarchy or dominant composition | Recheck affected sources → prove changed composition → review → expansion |
| Local repair: identified target and approved relationships remain valid | Inspect exact target → bounded correction → observe affected/protected regions; involve relevant specialists for material claims |
| Review only | Inspect current source and output → scoped specialist review → findings; no implementation or repair authority |

Unchanged colors/fonts/components do not make a new structure a local repair.
Product approval, DRAFT, a wireframe or permission to implement is not approval
of a visual composition. Unestablished local-repair conditions use the new/material
route. Continue independent authorized work without expanding an unproved direction.

## Execute the applicable stages

1. **Establish the source.** Reuse an adequate approved original for its exact scope.
   For unresolved reference decisions in new/material work, retrieve OMD and inspect
   originals. Select one Primary and at most two Secondary with distinct roles.
   Search results, brand names and prose summaries are not original inspection.
   Other tools may supplement this work; provider failure does not silently waive
   OMD or source comparison. Keep dependent work unresolved when sources are unavailable.
2. **Translate into the product.** Apply the visual translation module to attention
   order, grouping, density, imagery and narrow-screen behavior using real content.
   Preserve required functions, information, states and recovery. Keep one compact
   root DESIGN.md with sources, approval scope and necessary semantic role decisions;
   reuse native roles before introducing variations. Use the [template](templates/DESIGN.md)
   only when needed. Proposed and approved values remain distinct. A shared token gets a
   token-role row (role → parts → token → measured/proposed/approved); values read from
   shipped code are measured, not approved.
3. **Prove the representative composition.** Build the family exposing the largest
   visual risk at useful fidelity, including required wide/narrow and interaction
   states. Observe what dominates and what comes next. Low fidelity may defer finish,
   not hierarchy. Do not build dependent families before this proof is reviewed.
   Before implementation, the design owner maps the applicable DESIGN rules to
   required targets and geometric/specialist checks using the existing scoped
   [conformance contract](references/conformance.md): at minimum the DESIGN
   rule-coverage table (rule → check → spot check → layouts, sizes, states →
   unmeasured), and the pinned JSON baseline when the harness runs. Have the
   scope/criteria reviewed independently of the implementation and pin that baseline
   in the consuming workflow. A rule with no check row is unmeasured, never passed;
   missing checks cannot disappear from a completion report. Before a check's result
   counts for a rule, compare its reading on one target with a direct observation of
   the quantity the rule names (for a visible gap: the rendered edges a person sees,
   shadow included, not a wrapper box). If they differ, fix the check or the row.
   Every row's Spot check cell records the outcome: the target with both readings, or
   "not spot-checked". One row's spot check does not cover another row, and a row
   inherited without a recorded comparison is not spot-checked.
4. **Review the actual proof.** Use R/C1 and conditional C2 for affected claims, then
   fresh independent critique. Distinguish information/function preservation, source
   relationship conformance and whole-screen design quality. Challenge the composition
   itself, even if tokens match and nothing overflows. Missing observation is UNVERIFIED;
   contradiction is FAIL. Required failures or unknowns block dependent expansion.
5. **Correct, expand and integrate.** Rework structural gaps at composition level;
   use bounded correction for local gaps and stop repeated ineffective polishing.
   Expand from the reviewed relationships, then re-observe all affected targets and
   the protected proof on the changed build. A defect counts as fixed only after one
   direct observation of the fixed thing on a target that showed it (for clipping or
   overflow: the visible edges in a capture of that target, not the check's count);
   that observation is the fix's spot check. Material replacement of an approved
   direction needs scoped user approval after proof; internal review cannot grant it.
6. **Report the actual outcome.** Present the artifact, meaningful visual change,
   observed scope (the rule-coverage rows that ran and the rows left unmeasured)
   and dominant remaining gap. Design-check results go in one results list, one line
   per check that ran, every line in this form:
   `check | result | sizes x states, mode | rendered or code | spot check`,
   for example `spacing S1 | 939/939 | 9 sizes x 8 states, light | rendered |
   1440x900 bubble to chips: check 12 / observed 12` or `overflow | 72/72 | 12 sizes
   x 6 states, light | rendered | not spot-checked`. Side checks (overflow, clipping,
   scroll), before/after comparisons and each fix take a line. A fix line's result
   is one of two words: `fixed` when its spot check cell holds the direct observation
   (`375x667 replay bubble: clipped 14 before / 0 after, capture`), otherwise
   `changed`. A `changed` fix keeps its issue open, and the report text, ISSUES and
   ROADMAP use the cell's word, not "removed", "closed" or "resolved". Outside the
   list, the summary line included, every design-check pass, count, "fixed" or "no
   failures" is followed by a parenthesis copied from its line: (sizes x states,
   rendered or code, spot check outcome). Write "spacing 918/918 (12 sizes x 6
   states, rendered; spot check differs: check 16 / observed 8)", not "the check
   passed, but ..."; a sentence with no room for the parenthesis names the check and
   leaves the outcome to its line.
   A line that is not spot-checked is never listed as resolved, verified or done.
   Before sending, write the whole message you are about to send, every section and
   sentence of it, to a file and run this skill's `scripts/report-check.mjs` on it
   (`node <skill folder>/scripts/report-check.mjs <file>`); correct each finding in
   that file and rerun until it prints `report-check: ok <chars> chars <sha8>`. Send
   the file's text unchanged with that stamp line as its last line, so a reader can
   see that the checked text is the sent text (`--verify` recomputes it). A shortened
   or separate draft checked in place of the message is not a check. When no design
   check ran this turn, the report says `design checks: none ran` in one line in
   place of the results list; the sentence rules still apply. A fix whose line says
   `changed` is listed under remaining work, never under 해결. The script reads the
   form of the sentences, not whether a number is true. If it cannot run, say so in
   the report.
   The project's report format decides the sections; this decides the form of each
   result. Technical checks, visual judgment,
   workflow completion, certification and exact user acceptance remain distinct.
   User rejection remains REJECTED for that output; no counts or role labels erase it.

## Execution support

For CLI-managed work, the coordinator prepares source-grounded contracts using
[operation](references/operation.md), then follows [execution](references/execution.md).
Production requires work_kind and proof_target_ids; the runner reviews the proof
before launching expansion. A pinned design_validation baseline is required for
production and review. Rendered relationships include combined margin/padding/gap,
control height, wrapping and repeated-role consistency; CSS values alone are not
measurements. Missing/failed/stale conformance blocks the relevant phase even when
generic specialist claims pass. Use verify-design for direct/non-Git observations,
and pass its result to JOENESS's completion consumer where connected; JOEDESIGN
does not own that work ledger or grant user acceptance.
Review-only never gains write authority. The user need
not prepare machine files or choose between a core and harness.

Direct host/browser tools and non-Git projects follow the same operating route,
recording source → decision → observation → verdict in existing DESIGN/review records;
the DESIGN rule-coverage table is the minimum record of what was measured. When a
design is handed to a project session that cannot load JOEDESIGN, the token-role and
rule-coverage tables travel in DESIGN.md with their status, and so does its Report
Form section (the result-line form, `fixed`/`changed`, `changed` under remaining
work), so that session can keep the rules and report in the same form without this
skill. They need no new document system and must not be reported as a completed
CLI run.
The runner gates its own launches, not arbitrary external edits or actual adherence
inside a role. Local records are not authenticated host receipts or proof of human
visual judgment. Unavailable specialists or evidence stay explicit, never invented.
