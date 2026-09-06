# JOEDESIGN Composition / Anti-template Core v0.1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a small native Composition / Anti-template judgment layer that composes from Product priority and semantic relationships instead of defaulting to generic AI/SaaS layout recipes.

**Architecture:** Extend the existing single `joedesign` skill with one bounded composition section and one compact `DESIGN.md` persistence block. Add eight static contracts, then refresh semantic evidence because shipped skill bytes change, then prove the behavior in a neutral actual-render Smoke I. No parser, template database, visual-scoring model, vendor runtime, or new public skill is added.

**Tech Stack:** Markdown skill/docs, Node.js `node:test`, GPT-6 Astra xhigh semantic replay, existing local browser/Playwright validation harness.

**Spec:** `docs/specs/joedesign-composition-anti-template-core-v0.1.md`

## Global Constraints

- Base branch state is Imagery / Focal Ownership CLOSED at `ad22a9a761eb89ec03ace3fd94625f6a6db6927e`.
- Work only on `codex/joedesign-v0.1-composition-anti-template-core` in an isolated worktree.
- Preserve one public skill: `skills/joedesign/SKILL.md`.
- Preserve Product authority, APPROVED `DESIGN.md`, Visual PASS/User Acceptance separation, and prior CLOSED Craft behavior.
- No BIO data, screenshots, references, or project context.
- No competitor/vendor runtime, template database, anti-slop classifier, novelty score, layout-search engine, router, or new dependency.
- Do not alter semantic expected actions to fit model output.
- Preserve all RED/failure evidence.
- Any change under `skills/joedesign/**` invalidates previous branch-level semantic readiness and requires fresh Astra evidence.

---

## File Structure

- Create: `tests/joedesign-composition-anti-template-core.tests.mjs` — eight static Composition contracts.
- Modify: `skills/joedesign/SKILL.md` — minimal runtime doctrine only.
- Modify: `skills/joedesign/templates/DESIGN.md` — compact durable composition authority block.
- Modify: `tests/joedesign-contract.tests.mjs` — allow new canonical spec/test files while preserving competitor/runtime-surface gate.
- Modify: `fixtures/contract-cases/observed.json` — fresh semantic producer after shipped skill change.
- Modify: `fixtures/contract-cases/review-evidence.json` — final bounded evidence summary.
- Create evidence under `fixtures/contract-cases/evidence/astra-smoke-v1/composition-anti-template-v1/` and `fixtures/contract-cases/evidence/astra-smoke-v1/smoke-i/`.

---

### Task 1: Establish RED contracts

**Files:**
- Create: `tests/joedesign-composition-anti-template-core.tests.mjs`
- Modify: `tests/joedesign-contract.tests.mjs`

**Interfaces:**
- Consumes: current `skills/joedesign/SKILL.md` and `skills/joedesign/templates/DESIGN.md`.
- Produces: eight failing static contracts defining the minimal runtime surface.

- [ ] **Step 1: Verify the existing baseline**

Run the current 56-test suite before any implementation change:

```bash
node --test \
  tests/joedesign-contract.tests.mjs \
  tests/joedesign-craft-core.tests.mjs \
  tests/joedesign-typography-scale-core.tests.mjs \
  tests/joedesign-reference-intelligence-core.tests.mjs \
  tests/joedesign-color-contrast-core.tests.mjs \
  tests/joedesign-imagery-focal-core.tests.mjs
```

Expected: `56 PASS / 0 FAIL`.

Save the complete output under:

`fixtures/contract-cases/evidence/astra-smoke-v1/composition-anti-template-v1/baseline-tests.txt`

- [ ] **Step 2: Write the eight Composition static tests**

Create `tests/joedesign-composition-anti-template-core.tests.mjs` following the existing doctrine-test style. It must assert these exact behaviors:

```js
import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const skill = readFileSync(path.join(root, 'skills/joedesign/SKILL.md'), 'utf8');
const template = readFileSync(path.join(root, 'skills/joedesign/templates/DESIGN.md'), 'utf8');
const composition = skill.match(/^## [^\r\n]*composition[^\r\n]*\r?\n[\s\S]*?(?=^## |(?![\s\S]))/im)?.[0] ?? '';
const compositionTemplate = template.match(/^## Composition\r?\n[\s\S]*?(?=^## |(?![\s\S]))/m)?.[0] ?? '';

test('composition — Product priority and task or narrative flow precede pattern choice', () => {
  assert.match(composition, /Product priority/i);
  assert.match(composition, /task|narrative/i);
  assert.match(composition, /before.*(?:pattern|layout)|structure before pattern/i);
});

test('composition — cards and containers require semantic containment rather than decoration', () => {
  assert.match(composition, /semantic containment/i);
  assert.match(composition, /card|container/i);
  assert.match(composition, /do not|challenge|not.*merely/i);
});

test('composition — familiar AI SaaS patterns are challenge triggers not blanket bans', () => {
  assert.match(composition, /hero.*right image|three.*feature|3.*card|pill/i);
  assert.match(composition, /challenge trigger/i);
  assert.match(composition, /not.*blanket ban|not.*ban/i);
});

test('composition — repetition expresses equivalence and variation expresses meaningful change', () => {
  assert.match(composition, /repetition.*equivalence|equivalence.*repetition/i);
  assert.match(composition, /variation.*(?:change|priority|role)|(?:change|priority|role).*variation/i);
});

test('composition — intentional asymmetry may support hierarchy without novelty for its own sake', () => {
  assert.match(composition, /intentional asymmetry/i);
  assert.match(composition, /hierarchy|narrative|focal/i);
  assert.match(composition, /novelty/i);
});

test('composition — distinctiveness never overrides Product Truth usability or accessibility', () => {
  assert.match(composition, /Product Truth|Product/i);
  assert.match(composition, /usability|interaction cost|reachability/i);
  assert.match(composition, /accessibility/i);
});

test('composition — mobile recomposes priority instead of shrinking desktop coordinates', () => {
  assert.match(composition, /recompose/i);
  assert.match(composition, /mobile/i);
  assert.match(composition, /desktop coordinates|compressed desktop|shrink/i);
});

test('composition — DESIGN persists compact structural authority and material claims require actual renders', () => {
  assert.match(compositionTemplate, /## Composition/);
  assert.match(compositionTemplate, /### Structural Sequence/);
  assert.match(compositionTemplate, /### Major Region Roles/);
  assert.match(compositionTemplate, /### Containment Rules/);
  assert.match(compositionTemplate, /### Repetition \/ Variation/);
  assert.match(compositionTemplate, /### Responsive Composition/);
  assert.match(compositionTemplate, /### Approved Evidence/);
  assert.match(composition, /actual target render|actual render/i);
});
```

- [ ] **Step 3: Update only the repository-file allowlist**

In contract 16, add only:

```text
docs/specs/joedesign-composition-anti-template-core-v0.1.md
docs/superpowers/plans/2026-09-06-joedesign-composition-anti-template-core-v0.1.md
docs/handoffs/JOEDESIGN_COMPOSITION_ANTI_TEMPLATE_CORE_V1.md
tests/joedesign-composition-anti-template-core.tests.mjs
```

Do not weaken the runtime/vendor dependency assertions.

- [ ] **Step 4: Run RED and preserve it**

Run:

```bash
node --test tests/joedesign-composition-anti-template-core.tests.mjs
```

Expected: FAIL because the composition section/template block do not yet exist.

Save full output as:

`fixtures/contract-cases/evidence/astra-smoke-v1/composition-anti-template-v1/composition-red-tests.txt`

- [ ] **Step 5: Commit RED**

```bash
git add tests/joedesign-composition-anti-template-core.tests.mjs tests/joedesign-contract.tests.mjs fixtures/contract-cases/evidence/astra-smoke-v1/composition-anti-template-v1/composition-red-tests.txt
git commit -m "test: define composition anti-template contracts"
```

---

### Task 2: Add the minimal Composition runtime behavior

**Files:**
- Modify: `skills/joedesign/SKILL.md`
- Modify: `skills/joedesign/templates/DESIGN.md`

**Interfaces:**
- Consumes: the eight RED contracts and canonical doctrine.
- Produces: one bounded Composition section and one compact persistence block.

- [ ] **Step 1: Add one bounded Composition section to `SKILL.md`**

Add a single `##` section near the other Craft sections. Keep it compact and behavior-oriented. It must cover:

```text
Structure before pattern.
Product priority + task/narrative flow before layout recipe.
Semantic containment before card/panel use.
Common AI/SaaS motifs are challenge triggers, not blanket bans.
Repetition = semantic equivalence; variation = meaningful role/priority change.
Intentional asymmetry allowed when hierarchy remains clear.
Specificity over novelty; Product Truth/usability/accessibility remain boundaries.
References contribute relationships, not complete page grammar.
Mobile recomposes semantic priority rather than shrinking desktop coordinates.
Material composition claims require actual target renders.
```

Do not add a template catalog or automatic detector.

- [ ] **Step 2: Add compact `DESIGN.md` persistence**

Add:

```markdown
## Composition

### Structural Sequence
<!-- Primary first → second → third structural progression. -->

### Major Region Roles
<!-- Major semantic regions and relative dominance. -->

### Containment Rules
<!-- What is legitimately card/panel/container bounded, and what stays open. -->

### Repetition / Variation
<!-- Which structures repeat because roles are equivalent; where structure intentionally changes. -->

### Project-specific Anti-patterns
<!-- Only durable project-specific patterns to avoid; no global template blacklist. -->

### Responsive Composition
<!-- How priority/order/containment recomposes across target viewports. -->

### Approved Evidence
<!-- Exact approved artifact/revision/surface/state/viewport. -->
```

- [ ] **Step 3: Run Composition contracts**

```bash
node --test tests/joedesign-composition-anti-template-core.tests.mjs
```

Expected: `8 PASS / 0 FAIL`.

Save output as:

`fixtures/contract-cases/evidence/astra-smoke-v1/composition-anti-template-v1/composition-green-tests.txt`

- [ ] **Step 4: Commit minimal runtime**

```bash
git add skills/joedesign/SKILL.md skills/joedesign/templates/DESIGN.md fixtures/contract-cases/evidence/astra-smoke-v1/composition-anti-template-v1/composition-green-tests.txt
git commit -m "feat: add bounded composition anti-template behavior"
```

---

### Task 3: Refresh semantic evidence and run the full 64-test gate

**Files:**
- Modify: `fixtures/contract-cases/observed.json`
- Modify: `fixtures/contract-cases/review-evidence.json`
- Create bounded semantic evidence under `fixtures/contract-cases/evidence/astra-smoke-v1/composition-anti-template-v1/`.

**Interfaces:**
- Consumes: final shipped `skills/joedesign/**` bytes after Task 2.
- Produces: fresh GPT-6 Astra xhigh 14-case evidence bound to those bytes.

- [ ] **Step 1: Hash the full shipped skill package**

Record SHA-256 for exactly:

```text
skills/joedesign/SKILL.md
skills/joedesign/agents/openai.yaml
skills/joedesign/templates/DESIGN.md
```

- [ ] **Step 2: Run one fresh isolated Astra semantic replay**

Use `gpt-6-astra`, effort `xhigh`, and the unchanged 14 deterministic scenarios in `fixtures/contract-cases/decisions.json`.

Required result:

```text
14 PASS / 0 FAIL
```

Do not edit expected actions to obtain PASS.

Persist sanitized producer provenance, final response, thread ID, CLI version, rollout hash, scenario hashes, and skill hashes.

- [ ] **Step 3: Update `observed.json` only from the fresh producer**

Preserve the previous current evidence under a versioned `fixtures/contract-cases/history/` directory before replacing it.

- [ ] **Step 4: Run the full suite**

```bash
node --test \
  tests/joedesign-contract.tests.mjs \
  tests/joedesign-craft-core.tests.mjs \
  tests/joedesign-typography-scale-core.tests.mjs \
  tests/joedesign-reference-intelligence-core.tests.mjs \
  tests/joedesign-color-contrast-core.tests.mjs \
  tests/joedesign-imagery-focal-core.tests.mjs \
  tests/joedesign-composition-anti-template-core.tests.mjs
```

Expected: `64 PASS / 0 FAIL`.

Save output as:

`fixtures/contract-cases/evidence/astra-smoke-v1/composition-anti-template-v1/post-semantic-contract-tests.txt`

- [ ] **Step 5: Commit semantic evidence**

Commit only the fresh evidence and observed/review updates.

---

### Task 4: Smoke I — generic-template defect to project-specific composition

**Files:**
- Create: `fixtures/contract-cases/evidence/astra-smoke-v1/smoke-i/**`

**Interfaces:**
- Consumes: current JOEDESIGN skill and neutral fictional fixture only.
- Produces: actual browser evidence for Composition / Anti-template behavior.

- [ ] **Step 1: Build a neutral fictional fixture**

Use a fictional product named **Incident Decision Brief**.

`PRODUCT.md` must fix:

```text
Purpose: help an operations lead understand one incident and decide the next action.
Required content: incident title, one-sentence summary, severity/status metadata, three ordered findings, one primary action, one secondary evidence link.
Required order: summary before findings; findings 1→2→3 remain ordered; primary action remains single and explicit.
No decorative imagery is required.
```

`DESIGN.md` must be APPROVED and require:

```text
calm analytical tone
clear single first destination
open reading flow rather than dashboard density
one dominant action
user acceptance = NOT_GRANTED
```

The initial implementation should intentionally exhibit a plausible generic-template defect without changing Product content:

```text
centered hero + decorative right-side gradient/blob
three equal boxed finding cards
several decorative pills
same rounded surface treatment for summary, findings, and action
mobile = compressed desktop stacking
```

This fixture is a defect probe, not a statement that those patterns are always wrong.

- [ ] **Step 2: Record a pre-edit composition map before changing CSS/HTML**

Record:

```text
Product first/second/third destinations
major semantic regions
which containers are semantically justified
which familiar patterns are present
which patterns lack project-specific justification
intended desktop/mobile structural relationship
```

The timestamp/evidence must precede the first implementation edit.

- [ ] **Step 3: Let JOEDESIGN make the bounded correction**

The correction must preserve Product content/actions and APPROVED DESIGN authority.

It may change layout/CSS and only the minimum markup necessary to express the same semantics.

It must not add external assets, dependencies, or new Product content.

- [ ] **Step 4: Render actual before/after targets**

Required:

```text
Desktop viewport: 1440×1000
Mobile viewport: 390×844
```

Open and inspect the actual images.

- [ ] **Step 5: Judge these observables**

```text
I1 pre-edit structural map exists before edit
I2 first/second/third visual destinations match Product priority
I3 containers correspond to real containment; no unjustified equal card wall remains
I4 familiar motifs retained only when explicitly justified; decorative split-hero/pill/blob defaults do not drive hierarchy
I5 repetition and variation reflect semantic equivalence/change rather than identical section shells
I6 desktop structure has intentional rhythm/asymmetry without arbitrary novelty
I7 mobile recomposes the same priority instead of merely shrinking/stacking desktop ornaments
I8 Product Truth and APPROVED DESIGN bytes/semantics remain unchanged
I9 User Acceptance remains NOT_GRANTED
```

PASS is bounded to the named fixture/browser/viewports.

- [ ] **Step 6: Preserve failure and iteration evidence**

If the first Smoke I attempt fails any observable, preserve the failure before iteration. Do not overwrite it.

- [ ] **Step 7: If Smoke I changes shipped skill bytes, re-enter semantic validation**

If any `skills/joedesign/**` file changes during Smoke I:

```text
fresh semantic 14/14 again
→ full 64/64 again
→ rerun affected Smoke I proof
```

If only fixture/evidence files change, the Task 3 semantic producer remains valid.

---

### Task 5: Final gate and handoff

**Files:**
- Modify: `fixtures/contract-cases/review-evidence.json`
- Add final bounded summaries under the composition evidence directories.

- [ ] **Step 1: Run the final full suite**

Run all seven test files again.

Required: `64 PASS / 0 FAIL`.

Save as:

`fixtures/contract-cases/evidence/astra-smoke-v1/composition-anti-template-v1/final-contract-tests.txt`

- [ ] **Step 2: Verify the final repository boundary**

Report:

```text
public entrypoint count = 1
competitor dependency count = 0
runtime dependency count = 0
BIO exposure count = 0
skill SHA-256
DESIGN template SHA-256
branch HEAD/tree/clean status
```

- [ ] **Step 3: Final readiness report**

Only if every required gate passes, report:

```text
JOEDESIGN_COMPOSITION_ANTI_TEMPLATE_CORE_READY_FOR_PROGRAM_REVIEW
```

Include:

```text
Repository
Branch
HEAD
Tree
Static contracts: 64/64
Composition: 8/8
Semantic replay: 14/14 fresh
Smoke I: I1–I9
Skill SHA-256
DESIGN template SHA-256
Public entrypoint count
Competitor/runtime dependency counts
BIO exposure count
Known failures
Unverified boundaries
```

If any required gate is unresolved, report:

```text
JOEDESIGN_COMPOSITION_ANTI_TEMPLATE_CORE_NOT_READY
```

Do not claim phase closure or competition readiness; Program Lead owns those decisions.
