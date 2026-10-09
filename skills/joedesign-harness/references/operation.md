# Operation and artifact contracts

Contents: CLI; Product meaning to visual roles; artifact fields; evidence service;
RACI; known boundaries.

For actual role execution, local browser collection and resumable bounded repair,
see [local production execution](execution.md). The commands below retain their
original policy semantics; `run` has a separate, explicitly uncertified work status.
The [entry workflow](../SKILL.md#decide-the-scope-before-making-the-screen) governs
new direction, material extension and local repair in both CLI and direct-tool work.
These artifact and trust details do not replace the representative-proof sequence.

## CLI

Requires Python 3.11+. Use the script's absolute path from any project directory.
Each candidate owns a separate artifact directory; the examples use
`.design-harness/candidate-a`. The CLI never changes the target application's code.

```powershell
python <skill>/scripts/harness_cli.py doctor
python <skill>/scripts/harness_cli.py init .design-harness/candidate-a --intent intent.json
python <skill>/scripts/harness_cli.py index <local-omd-references-root> --output index.json
python <skill>/scripts/harness_cli.py retrieve index.json --intent intent.json --output shortlist.json
python <skill>/scripts/harness_cli.py bundle .design-harness/candidate-a synthesis --output synthesis.json
python <skill>/scripts/harness_cli.py bind .design-harness/candidate-a --run-id run-1 --build-id <actual-build-id> --context-id <actual-builder-context>
python <skill>/scripts/harness_cli.py raci .design-harness/candidate-a --claim-id <claim-id>
python <skill>/scripts/harness_cli.py advance .design-harness/candidate-a INTENT_READY
python <skill>/scripts/harness_cli.py check .design-harness/candidate-a
python <skill>/scripts/harness_cli.py guard .design-harness/candidate-a --change change.json
python <skill>/scripts/harness_cli.py repair .design-harness/candidate-a
python <skill>/scripts/harness_cli.py handoff .design-harness/candidate-a --output report.json
```

Fill the artifacts between commands. `raci` prints the ordered work assignment
for one bound claim and says execution is UNVERIFIED; it neither invokes a skill
nor certifies its use. `bind` records current identity after the lock,
contract and matrix are complete; it does not approve or authenticate anything.
Every transition must be requested in sequence: DRAFT → INTENT_READY → REFERENCES_FOUND
→ REFERENCE_LOCKED → CONTRACT_READY → IMPLEMENTED → CRAFTED → PROOF_COMPLETE
→ CRITIC_REVIEWED → APPROVED. USER_REVIEW is allowed early and records an event,
without claiming intermediate stages completed. REWORK returns to DRAFT.
An input change invalidates downstream recorded stages. States are execution records;
the assessed gates govern certification. `bundle ... expand` now requires complete
proof, passing Structure and VisualInternal, a current independent Critic and all
remaining categories passing. Technical/structural passes alone cannot authorize
dependent visual expansion. Scoped experiments remain possible without certification,
but still follow source inspection, representative proof and actual specialist review.
The trusted `bundle ... expand` gate and the local runner's operational expansion gate
are different: local review can schedule authorized work without issuing APPROVED.

Exit 0: command succeeded (for check/handoff, all approval conditions passed).
Exit 2: useful result generated but incomplete/blocked. Exit 1: invalid input or I/O.
Output files use exclusive creation. Init refuses a nonempty destination. Failed
advance does not modify the manifest. Bind stages both matrix and manifest and rolls
back a failed replacement. If the OS also blocks rollback, recovery copies are retained
in a reported `.harness-transaction-*` directory; no success is reported. This is not a
filesystem power-loss atomicity guarantee. Seven runtime artifacts use UTF-8; Markdown
artifacts contain exactly one fenced JSON payload, which is the machine contract.
Additional prose is not machine-validated or authoritative over that payload.

No network call is performed by index/retrieve. Point to the OMD local reference
directory containing company DESIGN.md files. Top-level scalar YAML metadata is
read without evaluating YAML directives; nested verification claims remain in the
source document. Unknown quality is UNKNOWN even if a verification section exists.
Duplicate IDs and escaped symlinks fail. Source paths and hashes permit reinspection.
Term matching is document retrieval, not aesthetic fit. Hard metadata filters use
explicit `reference_filters` lists (for example category); missing fields do not match.

## Product meaning to visual roles

For an information-hierarchy handoff or design-system change, compare the current
Product source with the revision actually consumed by the implementation. Planning
completion does not establish implementation coverage. Carry only the affected
information priority, exposure condition and decision/action into the existing
intent requirements/constraints and contract translations. Use `expected` and
`falsifier` to connect that meaning to visible type, color, spacing and grouping;
do not invent a new schema, document or role roster.

Product owns importance, required meaning, when information must be available and
accessibility constraints. The design owner translates those into visual roles
and maintains their durable decisions in the one root DESIGN.md. For the affected
scope, make usable the color chips/values, semantic uses and foreground/background
combinations; type roles with size, supported weight and line height; spacing
between elements, groups and sections; and common components with relevant states
and responsive differences. Reuse healthy native tokens/components and link their
implementation. Existing sufficient decisions need only the actual delta, not a
mandatory exhaustive token table or a second system. Distinguish current code,
proposed changes and approved decisions; code values are not approval evidence.

A Product document may mix mandatory constraints, proposed visual values and
approved visual values. Check each affected value's source and approval scope;
document location alone cannot classify it. Preserve approved values, and never
relabel them as proposals to bypass a conflict. Where an adjustment changes meaning,
exposure or a mandatory constraint, send the specific conflict and proposed tradeoff
to the existing Product/PM owner. The design owner supplies the visual alternative;
material visual replacement follows the user's scoped approval. Keep uncertain
authority explicit and continue unaffected work, without a whole-project restart.

The implementer observes the affected render and interactions against those roles;
the existing PM/lifecycle owner, if present, checks that the handoff preserved
meaning and exposure. These are responsibilities, not extra required agents. In
existing claims, separate content availability from visible hierarchy: can the
reader locate the key information and next action while still finding required
conditions at the required moment? Compare repeated components and the actual
narrow/wide targets for competing notice panels, repeated secondary text, wrapping
and grouping. Repetition or a notice box is not itself a failure. Do not hide
required warnings/errors through tiny or faint text or unauthorized deferral.
Record the expected relationship, observed fact and scoped verdict; source code or
token presence alone leaves visual hierarchy UNVERIFIED. Use the affected existing
Structure, Craft, VisualQuality, Responsive and Experience claims as appropriate,
not a new universal checklist. User visual acceptance remains separate.

## Artifact fields

Every scoped artifact carries candidate_id, revision and scope_id. IDs must be unique
within each collection. Source identity and product requirements are never inferred
from a style name. All examples below are field descriptions, not observations.

| Artifact | Required content |
|---|---|
| DESIGN_INTENT.json | product_source; requirements[{id,kind:content/action/state,description}]; constraints[{id,description}]; required_axes; exact targets; assets; search_terms; rejected_patterns |
| REFERENCE_CANDIDATES.json | retrieval output, catalog fingerprint, unresolved requirements. Not a lock |
| REFERENCE_LOCK.md | references[{id,role:primary/secondary,owns,source,source_sha256,observation:{kind:render/interaction,pointer,description},take,do_not_take,applies_to,unknown}] |
| DESIGN_CONTRACT.md | product_invariants (exact requirement IDs), reference_ids, patterns, structure_claims, protected_regions, translations described below |
| STATE_MATRIX.md | exact intent targets, claims, bindings of intent/lock/contract canonical hashes |
| CRITIQUE.md | context_id, receipt_id, snapshot, calibration_id, results[{claim_id,verdict,observed,evidence_ids}], findings[{kind:structural/local,verdict,reason}] |
| EVIDENCE_MANIFEST.json | run, items, reviews, repairs, resolutions, append-only history, acceptance_receipt_id |

Target: `{id, route, surface, family, viewport:[width,height], state, theme, locale,
required_kinds:[render/interaction/technical]}`. Each target is one exact state; include
opening/below-fold/error/loading/selected/narrow cases where the real brief requires them.
Do not drop required rows to pass. A true scope revision requires Product authority and
new bindings, review and approval. No OUT_OF_SCOPE laundering switch exists.

Translation: `{id, reference_id, axis, requirement_ids, constraint_ids,
source_observation, source_kind, rationale, spatial_rule, responsive_rule,
implementation:{component,selector}, expected, falsifier, target_ids}`.
All required content/actions/constraints and design axes must be covered.
Interaction/motion adds `motion:{origin:proposed/observed,trigger,start,end,interrupt,reduced}`.
Observed motion requires an interaction source; a static source can support a new
proposed interaction hypothesis, which must be tested on the actual result.

Claim: `{id,category,target_id,kind,required:true/false,expected,reviewers,
escalation_reason?}`. `reviewers` is the ordered R → C1 → C2 route, not a set of
interchangeable names. The first two roles are required for every non-Technical claim;
Technical starts with its implementer. A declared escalation requires the route's
third role. Existing evidence is not silently promoted to this newer review contract.

Base target categories: Technical, Accessibility, Responsive, Craft, Structure,
VisualConformance, VisualQuality. Product actions/states also require Experience for
each target. AnimationPerformance and ReactPerformance are conditional claims when
the relevant implementation or cost is in scope. Technical and performance claims
require technical evidence; Accessibility/Experience require interaction; the other
categories require render evidence. Additionally,
each translation whose axis is `motion` requires required VisualConformance and
VisualQuality claims of kind `interaction` for each of its target_ids. These add
`translation_id` pointing to that motion translation; they do not replace the required
render claims. Observe actual temporal continuity/pacing, not merely an endpoint click.
Ordinary non-motion actions do not incur expressive-motion claims. Every target
requires render; when Product includes actions/states it also requires interaction.
Contract-listed Structure claims must remain required Structure/render claims.
Structure tests the relationship
and task flow, not just individual component appearance.

Asset: `{id,status:VERIFIED/PROVISIONAL/MISSING/REJECTED,critical,source,role}`.
VERIFIED means actual intended resource rendered; a font download alone is insufficient.
Inspect actual family/weight/glyphs, unexpected fallback, crop and language/content length.
Keep fixtures explicit; do not turn synthetic results into factual product evidence.

Change guard input: `{role:craft/implementer,changed_axes,routes,families,selectors,
product_mutation,ownership_mutation}`. Guard reports broad selector risks; it is not
a complete CSS parser and cannot detect impacts the caller did not supply. Inspect
the real diff and protected surfaces. Material imagery/color/interaction changes
belong to synthesis; local optical refinements stay within the locked contract.

Repair: `{cause_id,hypothesis,outcome:IMPROVED/FAIL/UNVERIFIED/REGRESSION,
before_evidence,after_evidence,protected_regions,observation}`. Preserve original attempts.
An unresolved structural finding blocks craft/expansion; do not delete it to proceed.
Rework needs a new hypothesis/revision and new observations, not a renamed same repair.
An IMPROVED record used for certification requires current evidence binding and a
host repair receipt. New self-authored success text does not clear failed attempts.

## Evidence service and trust boundary

`scripts/harness/evidence.py` exposes `assess(bundle, host=None)` and HostVerifier.
The CLI deliberately supplies no host. An embedding host must implement
`resolve(receipt_id)` using its own immutable execution and authenticated user-event
store. It must protect the verifier/policy from the implementation writer. A JSON
file reader, same-process separation or an agent-provided signature key is insufficient.
No trust plugin or host service is installed by this package.

Canonical snapshot: SHA256 of sorted compact UTF-8 JSON of intent, lock, contract,
matrix. Matrix bindings hash intent/lock/contract. Actual build/run IDs must correspond
to the captured implementation, fonts/assets/content and target data, not caller labels.
The host must refuse mixed/changed-build captures and preserve prior unresolved failures.

- Capture item: id, target_id, exact target object, kind, path, sha256, receipt_id,
  run_id, build_id, snapshot, action and result. Interaction requires action/result.
  The receipt has kind=capture, evidence_kind matching item.kind, and matching fields.
  Local bytes are hashed again; receipt existence alone does not validate a target.
- Review: id, claim_id, verdict, observed, evidence_ids, reviewer, context_id,
  receipt_id, snapshot, run_id, build_id, evidence_hash, raci_step, sequence. A
  specialist review also has skill_id, skill_sha256 and skill_receipt_id. Its host
  receipt has kind=review and matching fields. `sequence` must be host-issued and
  monotonic within the run. The host must separately resolve the
  skill receipt as kind=skill_use, with the same claim/reviewer/context/snapshot/
  run/build and actual source hash; its host event sequence precedes the review.
  R precedes C1, and C1 precedes C2 when present. A name or locally written hash
  alone is not proof the skill was read. An unobserved/self-authored PASS never
  authenticates itself. Reported FAIL remains blocking until attested resolution.
- Critic: corresponding receipt kind=critic with exact input snapshot/results/context,
  run_id, build_id, evidence_ids and evidence_hash for all reviewed captures.
  Context must differ from builder and prior reviewers. The bundle excludes builder
  scores/rationale, but the host must actually launch the fresh context.
- Calibration: kind=calibration, status=IN_SCOPE, snapshot, approved_by,
  evaluation_id, criteria_id, held_out=true. Host resolves whether the human-approved
  evaluation applies to current model/rules/domain, not the implementation agent.
- Acceptance: kind=user_acceptance, actor=user,
  decision=APPROVE_EXACT_OUTPUT or REJECT_EXACT_OUTPUT,
  snapshot, candidate_id, revision, scope_id, build_id, message. Host authenticates the
  actual user event and exact scope; a user-like string in an artifact is insufficient.
  Exact rejection reports REJECTED and requires material rework even when internal
  categories pass. A later revision is PENDING until its own scoped user decision;
  preserve the earlier rejection as history rather than attaching it to new output.

`capture_binding(items,evidence_ids)` computes evidence_hash over the selected capture
records sorted by ID, projecting id/target/kind/sha256/run_id/build_id/snapshot into
canonical JSON. Reusing an evidence ID cannot authenticate new content or a new build.
The host must produce/verify this binding independently of the implementation writer.

Preserve historical reviews; old PASS is stale rather than a competing current review.
Old FAIL remains unresolved until a host-attested resolution. Resolution fields:
`{id,receipt_id,resolves:[failure IDs],observed,snapshot,run_id,build_id,evidence_ids,evidence_hash}`;
receipt kind=resolution. It must use current evidence of the appropriate claim kind;
structural findings cannot be cleared by technical-only observations. A stable finding
ID is recommended; legacy unkeyed findings use `finding:<index>`, repairs `repair:<index>`.
Original failed records remain intact. Required findings and additional consultants'
FAILs feed the same assessment used by transitions and handoff. Active dangling claim/
target IDs block completion. A removed claim's historical FAIL still needs resolution.

These are integration contracts. Synthetic test receipts demonstrate policy behavior,
not that a real host has been connected or is tamper-proof. Missing host → UNVERIFIED.
The controller cannot guarantee the honesty of arbitrary free-text chat; official
handoff is generated from assessment and equality-checked if submitted for validation.

## RACI as the work route

Classify each material finding before review. The matrix locks the ordered route:

| Claim category | R | C1 | C2 when escalated |
|---|---|---|---|
| Structure, VisualConformance, VisualQuality | JOEDESIGN (J) | Impeccable (I) | UI UX Pro Max (U) |
| Craft | Impeccable (I) | JOEDESIGN (J) | UI UX Pro Max (U) |
| Experience: content, input, error, recovery | UI UX Pro Max (U) | web-design-guidelines (V) | Impeccable (I) |
| Accessibility, Responsive implementation | web-design-guidelines (V) | UI UX Pro Max (U) | Impeccable (I) |
| AnimationPerformance, when applicable | Optimize Web Animations (M) | web-design-guidelines (V) | Impeccable (I) |
| ReactPerformance, when applicable | React Best Practices (R) | web-design-guidelines (V) | UI UX Pro Max (U) |
| Technical | Implementer | — | — |

The R owns the observation and draft verdict; C1 checks the same claim with a
distinct perspective. Use C2 for a recorded conflict, uncertainty or recurring
failure, and add `escalation_reason` plus the third reviewer to the claim. C2 helps
diagnose; it never votes away a demonstrated FAIL. Other specialists may submit
additional findings, but cannot replace R or C1. The claim route is a minimum,
not permission to ignore a material defect outside these labels.
The CLI flags an attested R/C1 verdict conflict even if the author omitted an
escalation reason. It cannot infer unrecorded uncertainty or a relationship between
free-text repair causes and claims; the implementation lead must surface those.

A is distinct from rank: the implementation lead owns integrated code and scene
review, Harness owns evidence/gates, JOEDESIGN owns visual synthesis, the fresh
Critic owns independent internal diagnosis, Product authority owns meaning, and
the user owns exact visual acceptance. I receives the scoped result and unresolved
limits; it is not another review pass. Neither A nor a majority of specialists can
overrule an observed failure or user rejection. The policy commands validate this
route and attested records when a trusted host is supplied. The separate `run`
command launches local specialist processes, but includes no authenticated host.
Local runs stay uncertified.

## What this does not prove

The code validates coverage, identity and the declared relationships. It cannot judge
whether a filled rationale is insightful or whether a composition is beautiful.
Early actual render, integrated visual review and human evaluation remain necessary.
No live OMD visual inspection, calibrated Critic service or authenticated receipt
backend is bundled. The optional local collector and Codex runner are described in
the execution reference; their local records are not authenticated host receipts.
The original seven artifact filenames are retained; handwritten duplicate JSON Schemas
are avoided in favor of the executable validators and templates they consume.
