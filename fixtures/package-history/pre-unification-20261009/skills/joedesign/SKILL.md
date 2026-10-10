---
name: joedesign
description: "Use when implementing an approved visual target, translating reference relationships into UI composition, refining typography/layout/imagery, or checking actual visual conformance. Also use for requested unapproved direction exploration. Not for Product Definition, pure backend work, nonvisual refactors or layout-unaffected copy changes."
---

# JOEDESIGN

Preserve product meaning while translating visual sources into project-specific
composition and implementation decisions. Primary work is approved-target
interpretation, implementation support and original-versus-result gap diagnosis;
new-direction exploration is conditional. Do not promise reliable original design
quality from an input alone. One entrypoint; no mandatory sequence of ceremonies.

## Establish the next decision

Inspect the request, current Product authority, root DESIGN.md, applicable
approval/rejection evidence, original visual material, real assets and relevant
implementation. Read available facts instead of asking for them again. Identify
the surface, state, version and viewport involved, not the whole project by default.

- **Approved visual target:** confirm the actual approval's scope/version/surface/
  state. Give the implementer direct access to that original and its real assets.
  With sufficient decisions, implement only the needed delta. Skip unnecessary
  alternatives, style reinvention, retranscription and repeated approval questions.
- **Ordinary reference:** a user-provided image is not approval by itself. Use only
  relevant relationships as advisory evidence. Distinguish observed source facts
  from project proposals; a new material direction remains unapproved. Explore
  only what the request or unresolved decision needs; no fixed candidate count.
- **Conflict or missing input:** name the affected relationship and authority.
  Do not silently blend conflicting references or override approved material with
  a translation, default taste or existing code. Resolve only the blocking scope;
  continue independent authorized work. Missing source access cannot be replaced
  by a claim that a prose description is the source.

Product authority owns functions, information, permissions, navigation, data,
states/transitions, recovery and behavior. Never remove required content/actions
or merge states for visual simplicity. Raise unresolved product meaning to the
current Product authority/user (through the existing lifecycle owner if present).
Do not require a framework, extra agent or whole-project restart.

## Translate only the relationships that matter

Use this short connection where a decision is needed:

**source observation → preserve/change for this project → concrete implementation
decision → observable difference in the result.**

Possible concerns, not a form to fill every time:

- Imagery: subject occupancy, text-relative scale, baseline, important regions,
  crop and negative space. Establish focal/support/decorative role and intentional
  text-image dominance. Preserve informative content and asset authorization.
- Typography: family/available weight, measure, wrapping, line height and contrast
  between roles. A still cannot establish an unavailable font or exact token.
- Space and rhythm: which groups a gap separates, repeated roles, local density,
  exceptions and the transition between adjacent image/reading sections.
- Composition: Product-priority entry point and next destinations, relative
  positions/axes, semantic containment, meaningful repetition/variation. Cards,
  hero-plus-image, three-card groups and pills need structural reasons, not a
  blanket ban. Specificity matters more than novelty.
- Responsive/state translation: what changes and what remains invariant. Recompose
  hierarchy, reading measure, crop, order and control reachability rather than
  shrinking desktop coordinates. Preserve all required information and behavior.

Label values as **measured**, **estimated**, **proposed** or **approved** when the
distinction matters; include the source or scope. Unknown facts remain unknown.
A useful proposed gap is not a recovered source measurement. Static images do
not establish unobserved hover, scroll or transitions. A screenshot's dimensions
define an observation viewport, not a page-height cap or permission to cut content.

## Apply craft without overriding the target

Use only principles relevant to the work. Establish hierarchy and visual flow
before decoration. Group by meaning rather than DOM depth. Equivalent semantic
relationships reuse spacing roles; structural sibling separation is different
from tightly bound content.

For unresolved areas, the restricted 4px-based spatial starting profile is
section 160 / major group 48 / subgroup 24 / item group 16 / tight 8 / micro 4px.
Use the subset needed, not every multiple of four. Recurring roles justify tokens;
optical adjustments do not silently create a new layout-spacing system. Approved
project values and healthy native roles take precedence, even when different.
Do not reshape an approved design to fit these defaults.

Typography is **not** the spatial 4px grid. Choose few semantic roles, families and
supported weights; coordinate size, weight, line height, measure and placement.
Starting sizes 12, 14, 16, 20, 24, 32, 40, 48, 64px are optional for unresolved
roles, not approved tokens. Inspect the actual language, typeface, line breaks and
mobile reading texture; do not manufacture hierarchy through tiny size differences
or apply Latin measure mechanically to CJK, code or tables.

Assign color by semantic role and attention priority; use surfaces for real layers
and containment. Preserve state meaning with needed non-color cues. For applicable
web work, retain WCAG 2.2 AA minimum contrast (normal text 4.5:1; large text and
meaningful UI/state visuals 3:1), with stricter project requirements taking priority.
Check relevant foreground/background pairs, image/gradient regions, focus and
interaction/theme states; a token alone proves neither contrast nor appearance.
If accessibility conflicts with an approved target, expose the affected conflict
instead of silently changing the target or declaring it compliant.

## Connect the source to implementation

Reference interpretation and the Implementation Bridge are one derivative flow:
original approved material + scoped project decisions → implementation → comparison.
Pass original source/version/surface/state and real asset pointers directly, along
with only necessary mapping decisions and unknowns. Translation supplements the
source; it never replaces or quietly amends it.

Reuse an equivalent project-native token/component/theme role first. Map exact
approved values separately from intent/rationale. Do not invent missing tokens,
rename stable roles to fit an external convention or replace healthy architecture.
For a material mapping change, show the affected role/value, authority and reason.
Existing structured tokens may help, but do not require a schema, parser, export
step or tool. Preserve unknown/custom DESIGN sections and responsive intent.

Responsibilities need not be separate agents: Product owns meaning; JOEDESIGN
interprets relationships and diagnoses gaps; the implementer owns code, responsive/
state implementation **and observing its actual result**. The controller handles
environment, isolation, execution records, verification management and handoff,
not a new visual interpretation imposed on the implementer. Do not burden the
candidate with experiment administration or require JOEFLOW.

## Keep one compact project authority

Use one root DESIGN.md. The [template](templates/DESIGN.md) is a seed only when
creating or materially updating durable decisions, not a required reread/form for
each edit. Keep source/asset pointers, approval scope, necessary project decisions
and unknowns; do not duplicate Product meaning or settled source specifications.
Existing sufficient DESIGN content needs only a real decision delta, if any.

An absent file starts DRAFT. Only explicit user approval promotes material direction
to APPROVED. Preserve APPROVED Rev N while a separately labeled DRAFT Rev N+1 is
proposed within the same file; one active approved rule set, no mandatory sidecar.
Authorized reversible draft/proof work does not need advance approval of its result.
Local refinements within approved intent need no material amendment. Material
replacement requires explicit approval after proof. Implementation permission,
“진행”, and “ㄱㄱ” are not acceptance of an exact output.

## Observe and correct the exact result

For a new/material direction, make the smallest useful target-medium proof before
broad dependent integration. Obtain the needed user response before expansion that
requires acceptance; already-approved targets and local refinements need no new
direction gate.

Before a material implementation/proof, identify the few source-based relationships
to check and the applicable target dimensions/state. Use the existing target runtime.
The implementer observes its actual output against the original; build success,
DOM/token presence and an unopened screenshot do not establish visual conformance.

For local feedback: inspect the exact current target → diagnose the affected
relationship → bounded correction → rerender and observe that target and protected
regions. Keep unrelated approved areas intact. Do not turn crop/type feedback into
full-page regeneration. If repeated correction is not resolving the evidenced gap,
diagnose the direction/source conflict before more dependent expansion; do not
automatically fan out candidates or polish indefinitely. For material motion, check
relevant start/intermediate/end, interruption/reverse and reduced-motion behavior;
still-image evidence covers only its visible state.

Use **expected relationship → actual observed fact → PASS / FAIL / UNVERIFIED**
for material claims, binding artifact/version and surface/state/viewport where
relevant. Contradiction is FAIL; missing observation is UNVERIFIED. A required FAIL
keeps the covered visual result FAIL; otherwise any required UNVERIFIED keeps it
UNVERIFIED. Continue completed/independent authorized work without fabricating the
missing check or rerunning unrelated checks to compensate.

Token mapping, technical checks, Product conformance, visual conformance and user
acceptance are separate. Visual PASS never grants acceptance. Keep the user-facing
handoff proportional: relevant output/delta, observed boundary and a next decision
only when needed, not an exhaustive craft or operational report.

## Capability boundary

Use available general tools and project runtime as needed. No competitor methodology,
vendor runtime, new public skill, asset/reference database, automatic router/scorer,
image-generation dependency or lifecycle orchestrator is required or bundled.
