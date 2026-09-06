# JOEDESIGN Imagery / Focal Ownership Core — Execution Handoff V1

**Status:** ACTIVE EXECUTION HANDOFF  
**Repository:** `JOEWRKS/JOEDESIGN`  
**Branch:** `codex/joedesign-v0.1-imagery-focal-core`  
**Base:** Color / Contrast Core Program Review PASS at `7417ef037062f27272c3d3527713475b7d97c6f3`

---

## 1. Mission

Implement and validate **JOEDESIGN Imagery / Focal Ownership Core v0.1 only**.

The goal is not to add image tooling. The goal is to make JOEDESIGN deliberately decide:

```text
what role the image has
→ who owns attention
→ how text and image share hierarchy
→ what crop/focal region must survive
→ how scale/negative space express priority
→ how that focal intent translates responsively
→ whether the actual render proves it
```

---

## 2. Read order

Read in this order before editing:

1. `AGENTS.md`
2. `docs/roadmaps/JOEDESIGN_V0_1_IMPLEMENTATION_ROADMAP.md`
3. `docs/specs/joedesign-imagery-focal-core-v0.1.md`
4. `docs/superpowers/plans/2026-09-06-joedesign-imagery-focal-core-v0.1.md`
5. `skills/joedesign/SKILL.md`
6. `skills/joedesign/templates/DESIGN.md`
7. current contract tests and latest Color review evidence

The doctrine is the behavior authority for this phase. The plan defines execution order.

---

## 3. Fixed scope

Implement these behaviors only:

- role before asset treatment;
- compact roles `FOCAL / SUPPORT / DECORATIVE`;
- informative/evidence imagery preserves Product meaning;
- intentional focal owner or intentional focal sequence;
- deliberate text-image dominance;
- crop/focal region before blind center-crop;
- scale/negative space express priority without fixed ratios;
- references contribute imagery relationships, not copied assets;
- responsive recrop/reposition/recomposition;
- actual render required for material image claims;
- compact Project `DESIGN.md` persistence.

---

## 4. Explicit non-goals

Do not add:

- new public skill;
- stock-photo search;
- image asset database;
- DAM integration;
- image-generation runtime dependency;
- automatic image router;
- saliency/heatmap scoring subsystem;
- asset crawler;
- background-removal pipeline;
- Composition / Anti-template Core behavior beyond what is necessary to preserve image role;
- Implementation Bridge;
- BIO project data.

Do not modify main or the user's personal installed skill.

---

## 5. Required execution order

Because changing shipped skill bytes makes prior semantic evidence stale, use this order:

```text
baseline 48/48
→ imagery contracts RED
→ minimal implementation
→ imagery 8/8
→ fresh semantic 14/14
→ full 56/56
→ Smoke H
→ final 56/56
```

If Smoke H causes any later change to `skills/joedesign/**`:

```text
skill change
→ fresh semantic 14/14 again
→ full 56/56 again
→ rerun affected Smoke H evidence
```

Do not demand the full 56/56 before refreshing semantic evidence after the first skill-byte change.

---

## 6. Static contracts

Create exactly eight Imagery Core contracts covering:

1. role before treatment and Product-content preservation;
2. focal ownership / intentional visual sequence;
3. text-image dominance;
4. crop/focal region preservation;
5. scale and negative-space priority;
6. reference relationship without asset copying/invented facts;
7. responsive focal translation;
8. compact DESIGN.md persistence + actual-render requirement.

Final expected suite size:

```text
16 Process/Authority
+ 8 Spatial Craft
+ 8 Typography
+ 8 Reference
+ 8 Color
+ 8 Imagery
= 56 tests
```

Do not alter expected semantic actions.

---

## 7. Smoke H

Use a **fictional neutral product**. Do not expose the agent/runtime to BIO.

Recommended fixture: `Specimen Review Page`.

Required fixed Product content:

- one supplied local specimen image asset;
- title;
- short metadata;
- caption;
- one required action;
- any minimal supporting facts needed for hierarchy.

APPROVED Project `DESIGN.md` should already establish that the specimen image is the primary visual focal owner and text is a quiet editorial anchor.

Before-state defect should be bounded to imagery/focal behavior, for example:

- specimen visually demoted to a generic thumbnail;
- important focal region lost in mobile crop;
- decorative treatment competes with the specimen;
- image/text relationship contradicts approved focal ownership.

Do not redesign the whole product or add new content.

### Smoke H required checks

```text
H1 pre-edit image-role map exists
H2 intended focal owner becomes visually dominant
H3 text-image hierarchy is intentional
H4 important subject/focal region remains visible
H5 desktop crop/framing is deliberate
H6 mobile crop/reposition preserves focal intent
H7 decorative treatment does not steal ownership
H8 Product and APPROVED DESIGN bytes are unchanged
H9 user acceptance remains NOT_GRANTED
```

Actual evidence:

- desktop viewport `1440×1000` before/after;
- mobile viewport `390×844` before/after;
- full-page screenshot dimensions recorded separately when height exceeds viewport;
- actual images opened/inspected;
- source/focal region and Product invariants recorded;
- PASS / FAIL / UNVERIFIED per required observable.

Do not claim crop correctness from CSS alone.

---

## 8. Failure discipline

If a gate fails:

- preserve the failing output;
- identify root cause before editing;
- do not change expected answers to match the failure;
- do not delete earlier failure evidence;
- do not expand into a new subsystem;
- report `JOEDESIGN_IMAGERY_FOCAL_CORE_NOT_READY` if unresolved.

A test-harness allowlist failure must be separated from shipped-behavior failure before any fix.

---

## 9. Final gate

READY requires all of:

```text
Imagery contracts: 8/8 PASS
Full contracts: 56/56 PASS
Fresh Astra semantic replay: 14/14 PASS
Smoke H: PASS
Desktop actual observation: PASS
Mobile actual observation: PASS
Product Truth invariant: PASS
APPROVED DESIGN invariant: PASS
User acceptance: NOT_GRANTED unless explicitly granted
Public entrypoint count: 1
Competitor dependency count: 0
Runtime dependency count: 0
BIO exposure count: 0
Clean tree
Remote branch matches reported HEAD
```

Only then report:

```text
JOEDESIGN_IMAGERY_FOCAL_CORE_READY_FOR_PROGRAM_REVIEW
```

Do not declare `IMAGERY_FOCAL_CORE = CLOSED`; Program Lead owns that verdict.

---

## 10. Final report format

```text
JOEDESIGN_IMAGERY_FOCAL_CORE_READY_FOR_PROGRAM_REVIEW

Repository:
Branch:
HEAD:
Tree:
Static contracts:
Semantic replay:
Smoke H:
Role mapping:
Focal ownership:
Text-image dominance:
Crop/focal preservation:
Desktop observation:
Mobile observation:
Product Truth invariant:
APPROVED DESIGN invariant:
User acceptance boundary:
Skill SHA-256:
DESIGN template SHA-256:
Public entrypoint count:
Competitor dependency count:
Runtime dependency count:
BIO exposure count:
Known failures:
Unverified:
```
