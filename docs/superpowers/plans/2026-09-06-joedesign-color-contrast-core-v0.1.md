# JOEDESIGN Color / Contrast Core v0.1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a minimal native Color / Contrast Craft Core that assigns color by semantic role, preserves Product and project authority, controls contrast/accent hierarchy, and verifies material color behavior in actual renders.

**Architecture:** Extend the existing single `joedesign` skill with one bounded color/contrast behavior section and a minimal `DESIGN.md` persistence structure. Add eight static contracts before runtime changes, then fresh Astra semantic evidence and one neutral rendered Smoke G. Do not add a palette database, color engine, vendor dependency, parser, router, or public skill.

**Tech Stack:** Markdown skill contract, Node.js `node:test`, GPT-6 Astra xhigh semantic replay, existing browser/runtime proof harness.

**Spec:** `docs/specs/joedesign-color-contrast-core-v0.1.md`

## Global Constraints

- Product Truth and APPROVED Project `DESIGN.md` remain above JOEDESIGN Craft defaults.
- Public entrypoint count remains exactly `1` (`joedesign`).
- Competitor/runtime dependency count remains `0`.
- BIO exposure remains `0` during core implementation and validation.
- No universal JOEDESIGN palette, palette database, theme generator, color router, vendor engine, or standalone accessibility scanner.
- WCAG 2.2 AA minimums are accessibility gates where applicable, not a complete aesthetic system.
- Do not modify expected semantic answers to fit a failing runtime.
- Preserve all prior failure and validation evidence.
- Implementation Bridge is not part of this branch.

---

### Task 1: Add Color / Contrast static contracts first

**Files:**
- Create: `tests/joedesign-color-contrast-core.tests.mjs`
- Modify: `tests/joedesign-contract.tests.mjs`

**Interfaces:**
- Consumes: `skills/joedesign/SKILL.md`, `skills/joedesign/templates/DESIGN.md`, color doctrine.
- Produces: eight deterministic static contracts and an updated internal-file allowlist.

- [ ] **Step 1: Add eight failing static contracts**

Create tests that require the shipped behavior to state all of the following:

1. semantic color role is chosen before local color value;
2. contrast hierarchy and accent ownership reinforce Product priority rather than making every element equally loud;
3. neutral/surface color expresses real layer/containment relationships and does not require a panel for every group;
4. functional state colors preserve Product semantics and required meaning is not carried by color alone;
5. applicable WCAG 2.2 AA minimums are explicit while also stating they are minimum gates, not an aesthetic preset;
6. material contrast is evaluated in actual foreground/background context rather than inferred from token existence;
7. responsive/light-dark translation preserves semantic roles while values may change;
8. `DESIGN.md` can persist compact project color roles, accent ownership, surface/layer behavior, and state/contrast constraints.

Use direct source assertions consistent with the existing craft/type/reference test style. Do not build a policy simulator.

- [ ] **Step 2: Update contract 16 internal-file allowlist**

Add only the Color Core files that legitimately belong to this branch:

```text
docs/specs/joedesign-color-contrast-core-v0.1.md
docs/superpowers/plans/2026-09-06-joedesign-color-contrast-core-v0.1.md
docs/handoffs/JOEDESIGN_COLOR_CONTRAST_CORE_V1.md
tests/joedesign-color-contrast-core.tests.mjs
```

If another Program Lead-created internal Color document is already present, add that exact path only. Do not broaden the allowlist to arbitrary directories.

- [ ] **Step 3: Run RED**

Run:

```bash
node --test tests/joedesign-color-contrast-core.tests.mjs
```

Expected: one or more assertions FAIL because Color / Contrast runtime behavior and template persistence are not implemented yet.

Record the exact RED output under bounded evidence. If a test unexpectedly passes because an older general sentence happens to match, strengthen the test so it verifies the new intended contract rather than keyword coincidence.

- [ ] **Step 4: Commit test-first state**

```bash
git add tests/joedesign-color-contrast-core.tests.mjs tests/joedesign-contract.tests.mjs
git commit -m "test: define JOEDESIGN color contrast contracts"
```

---

### Task 2: Implement minimal Color / Contrast runtime behavior

**Files:**
- Modify: `skills/joedesign/SKILL.md`
- Modify: `skills/joedesign/templates/DESIGN.md`

**Interfaces:**
- Consumes: eight failing contracts and canonical color doctrine.
- Produces: one bounded Color / Contrast section in the existing skill and compact durable project-color fields.

- [ ] **Step 1: Add one bounded SKILL section**

Add a section near the other Craft Core behavior, with no new public mode. It must cover:

```text
Role before color value
Semantic color roles
Contrast hierarchy
Accent ownership
Surface/layer color relationships
State semantics + non-color cue
WCAG minimum gate where applicable
Contextual foreground/background observation
Responsive/theme role preservation
Actual render required for material visual PASS
```

Do not introduce fixed global token names or a fixed JOE palette.

- [ ] **Step 2: Add minimal DESIGN.md persistence**

Under `## Color / Surface`, add only compact project-authority slots such as:

```markdown
### Color Roles

### Accent Ownership

### Surface / Layer Relationships

### State / Contrast Constraints
```

Comments must state that only sourced/approved project-specific decisions are persisted; draft JOEDESIGN defaults do not become authority automatically.

- [ ] **Step 3: Run Color contracts GREEN**

```bash
node --test tests/joedesign-color-contrast-core.tests.mjs
```

Expected: `8 PASS / 0 FAIL`.

- [ ] **Step 4: Run full static suite**

```bash
node --test \
  tests/joedesign-contract.tests.mjs \
  tests/joedesign-craft-core.tests.mjs \
  tests/joedesign-typography-scale-core.tests.mjs \
  tests/joedesign-reference-intelligence-core.tests.mjs \
  tests/joedesign-color-contrast-core.tests.mjs
```

Expected total: `48 PASS / 0 FAIL`.

- [ ] **Step 5: Commit runtime implementation**

```bash
git add skills/joedesign/SKILL.md skills/joedesign/templates/DESIGN.md
git commit -m "feat: add bounded color contrast craft behavior"
```

---

### Task 3: Fresh Astra semantic replay

**Files:**
- Modify: `fixtures/contract-cases/observed.json`
- Preserve prior evidence under history before replacement when required by repository convention.

**Interfaces:**
- Consumes: unchanged fourteen decision scenarios and current shipped skill bytes.
- Produces: fresh GPT-6 Astra xhigh 14/14 semantic decision evidence with current skill hashes.

- [ ] **Step 1: Run one fresh semantic replay**

Runtime:

```text
model: gpt-6-astra
effort: xhigh
```

Use the unchanged 14 supplied-choice decision scenarios. Do not edit scenarios or expected answers.

- [ ] **Step 2: Verify**

Required:

```text
14/14 PASS
public entrypoint = 1
competitor dependency = 0
BIO exposure = 0
```

Record complete skill-package SHA-256 values and runtime/thread provenance.

- [ ] **Step 3: Commit semantic evidence**

Commit only bounded evidence and refreshed repository evidence. Preserve prior historical records.

---

### Task 4: Smoke G — Color / Contrast rendered proof

**Files:**
- Create under: `fixtures/contract-cases/evidence/astra-smoke-v1/smoke-g/`

**Interfaces:**
- Consumes: neutral fictional Product Truth, approved visual direction, deliberately defective color implementation.
- Produces: actual desktop/mobile before-after evidence and a color-role manifest.

- [ ] **Step 1: Build a neutral fixture**

Use a fictional **Operations Review Portal**. Do not use BIO names, assets, copy, or design direction.

Fixed Product Truth:

- page title and supporting description;
- one primary review action;
- three ordered review records;
- each record has source, timestamp, and explicit semantic status text;
- one record is the current priority item;
- all content, record order, action meaning, and statuses are immutable during visual refinement.

Approved visual intent:

```text
calm operational clarity
one clear primary action
priority record must be visually findable
records remain an open list, not a card wall
```

- [ ] **Step 2: Deliberately seed Color defects**

Before state should include multiple material defects:

- unrelated high-chroma colors on title, action, metadata, borders, and record accents;
- no clear accent owner;
- secondary/supporting text below applicable readable contrast;
- current-priority indication relying primarily on color;
- semantic state colors reused decoratively elsewhere;
- unnecessary tinted panels/layers without containment meaning;
- a mobile background/recomposition that changes contrast context and exposes at least one weak pair.

Do not change Product semantics to create the defects.

- [ ] **Step 3: Require JOEDESIGN to produce a role map before editing**

The runtime should identify, before implementation:

- foreground hierarchy roles;
- surface/layer roles;
- accent owner;
- semantic state roles;
- focus/current-priority indication;
- known accessibility failures or material contrast uncertainties.

- [ ] **Step 4: Implement bounded visual correction**

Expected behavior:

- reduce arbitrary local colors into recurring semantic roles;
- establish a clear accent owner tied to Product priority;
- preserve semantic state meaning without using color as the sole cue;
- remove or neutralize unsupported decorative reuse of state colors;
- simplify unjustified tinted panels;
- meet applicable WCAG 2.2 AA minimum contrast on required text/UI/graphical cues;
- preserve expressive/project-specific color where it does not conflict with hierarchy or accessibility;
- re-evaluate mobile against its actual background context rather than copying desktop values mechanically.

- [ ] **Step 5: Render and inspect exact targets**

Required viewports:

```text
Desktop: 1440×1000
Mobile: 390×844
```

Record actual rendered observations, not code-only assertions.

- [ ] **Step 6: Create `color-role-manifest.json`**

Minimum contents:

```text
Product invariants
approved visual intent
before color defects
semantic color-role map
dominant accent owner
before/after computed foreground-background pairs
applicable contrast ratios
state cue mapping including non-color cues
surface/layer mapping
responsive/mobile role translation
changed files
actual desktop observation
actual mobile observation
PASS/FAIL/UNVERIFIED by claim
user acceptance boundary
```

- [ ] **Step 7: Smoke G gate**

Required:

```text
Role mapping PASS
Contrast hierarchy PASS
Accent ownership PASS
Surface/layer coherence PASS
State semantics PASS
No color-only required cue PASS
Applicable accessibility gate PASS
Desktop actual observation PASS
Mobile actual observation PASS
Product Truth invariant PASS
User acceptance not granted
```

Commit durable evidence only.

---

### Task 5: Final gate and handoff

**Files:**
- Modify: `fixtures/contract-cases/review-evidence.json`
- Preserve prior failures/history.

- [ ] **Step 1: Re-run full static suite**

Required: `48 PASS / 0 FAIL`.

- [ ] **Step 2: Verify evidence integrity**

Required:

```text
Semantic replay: 14/14 PASS
Smoke G: PASS
Public entrypoint: 1
Competitor dependency: 0
Runtime vendor dependency: 0
BIO exposure: 0
```

- [ ] **Step 3: Report**

Use exactly:

```text
JOEDESIGN_COLOR_CONTRAST_CORE_READY_FOR_PROGRAM_REVIEW

Repository:
Branch:
HEAD:
Tree:

Static contracts:
Semantic replay:
Smoke G:

Skill SHA-256:
DESIGN template SHA-256:

Public entrypoint count:
Competitor dependency count:
BIO exposure count:

Known failures:
Unverified:
```

Do not declare `COLOR_CONTRAST_CORE = CLOSED`; Program Lead owns that gate.
