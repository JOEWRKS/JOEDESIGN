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
   only when needed. Proposed and approved values remain distinct.
3. **Prove the representative composition.** Build the family exposing the largest
   visual risk at useful fidelity, including required wide/narrow and interaction
   states. Observe what dominates and what comes next. Low fidelity may defer finish,
   not hierarchy. Do not build dependent families before this proof is reviewed.
   Before implementation, the design owner maps the applicable DESIGN rules to
   required targets and geometric/specialist checks using the existing scoped
   [conformance contract](references/conformance.md). Have the scope/criteria
   reviewed independently of the implementation and pin that baseline in the
   consuming workflow. Missing checks cannot disappear from a completion report.
4. **Review the actual proof.** Use R/C1 and conditional C2 for affected claims, then
   fresh independent critique. Distinguish information/function preservation, source
   relationship conformance and whole-screen design quality. Challenge the composition
   itself, even if tokens match and nothing overflows. Missing observation is UNVERIFIED;
   contradiction is FAIL. Required failures or unknowns block dependent expansion.
5. **Correct, expand and integrate.** Rework structural gaps at composition level;
   use bounded correction for local gaps and stop repeated ineffective polishing.
   Expand from the reviewed relationships, then re-observe all affected targets and
   the protected proof on the changed build. Material replacement of an approved
   direction needs scoped user approval after proof; internal review cannot grant it.
6. **Report the actual outcome.** Present the artifact, meaningful visual change,
   observed scope and dominant remaining gap. Technical checks, visual judgment,
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
recording source → decision → observation → verdict in existing DESIGN/review records.
They need no new document system and must not be reported as a completed CLI run.
The runner gates its own launches, not arbitrary external edits or actual adherence
inside a role. Local records are not authenticated host receipts or proof of human
visual judgment. Unavailable specialists or evidence stay explicit, never invented.
