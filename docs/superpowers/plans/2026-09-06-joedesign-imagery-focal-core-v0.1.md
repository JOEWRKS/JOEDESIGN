# JOEDESIGN Imagery / Focal Ownership Core v0.1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add the smallest JOEDESIGN runtime behavior that makes imagery role, focal ownership, text-image dominance, crop/framing, and responsive focal translation deliberate and verifiable.

**Architecture:** Extend the single existing `joedesign` skill with one compact imagery/focal section and a minimal Project `DESIGN.md` persistence block. Add eight deterministic static contracts, refresh semantic evidence after shipped skill bytes change, then prove the behavior with one neutral rendered Smoke H. No new public skill, asset system, image model dependency, or external runtime is introduced.

**Tech Stack:** Markdown skill package, Node.js `node:test`, GPT-6 Astra xhigh semantic replay, existing browser/render tooling already available in the repository/runtime.

**Spec:** `docs/specs/joedesign-imagery-focal-core-v0.1.md`

## Global Constraints

- Preserve one public skill: `joedesign`.
- Preserve Product Truth, approved Project `DESIGN.md`, and user-acceptance boundaries.
- Do not import Implementation Bridge work.
- Do not use BIO during this phase.
- Do not add stock search, asset DB, DAM, image model dependency, saliency subsystem, router, or vendor payload.
- Any shipped `skills/joedesign/**` byte change invalidates prior semantic readiness evidence for this branch.
- Do not alter expected semantic actions to fit a runtime result.
- Preserve all failure evidence.
- Actual target renders are required for material focal/crop PASS.

---

## Task 1: Establish isolated baseline

**Files:**
- Read: `AGENTS.md`
- Read: `docs/roadmaps/JOEDESIGN_V0_1_IMPLEMENTATION_ROADMAP.md`
- Read: `docs/specs/joedesign-imagery-focal-core-v0.1.md`
- Read: `skills/joedesign/SKILL.md`
- Read: `skills/joedesign/templates/DESIGN.md`
- Evidence only: `fixtures/contract-cases/evidence/astra-smoke-v1/imagery-focal-v1/baseline-tests.txt`

**Interfaces:**
- Consumes: branch `codex/joedesign-v0.1-imagery-focal-core` based on Color Core CLOSED HEAD.
- Produces: clean isolated worktree and recorded 48-test baseline.

- [ ] **Step 1: Create or use a separate worktree for this branch**

Verify the checked-out branch and HEAD before edits.

- [ ] **Step 2: Run the current full static suite**

Run:

```text
node --test tests/joedesign-contract.tests.mjs tests/joedesign-craft-core.tests.mjs tests/joedesign-typography-scale-core.tests.mjs tests/joedesign-reference-intelligence-core.tests.mjs tests/joedesign-color-contrast-core.tests.mjs
```

Expected: `48 PASS / 0 FAIL`.

- [ ] **Step 3: Preserve baseline output**

Save the complete output under:

`fixtures/contract-cases/evidence/astra-smoke-v1/imagery-focal-v1/baseline-tests.txt`

- [ ] **Step 4: Commit only baseline evidence if the branch policy requires durable evidence at this point**

Do not touch `skills/**` yet.

---

## Task 2: Add eight imagery contracts first

**Files:**
- Create: `tests/joedesign-imagery-focal-core.tests.mjs`
- Modify: `tests/joedesign-contract.tests.mjs` only as needed to allow the new canonical spec/test/handoff documentation in repository-surface checks.
- Evidence: `fixtures/contract-cases/evidence/astra-smoke-v1/imagery-focal-v1/imagery-red-tests.txt`

**Interfaces:**
- Consumes: canonical imagery doctrine.
- Produces: eight static contracts that fail before runtime/template implementation.

The eight contracts must cover exactly these behaviors:

1. role before treatment: `FOCAL / SUPPORT / DECORATIVE` and informative imagery remains Product content;
2. intentional focal ownership / visual sequence;
3. deliberate text-image dominance rather than accidental co-dominance;
4. crop/focal point preserves important or required image content;
5. scale and negative space express image priority without fixed ratios;
6. references contribute imagery relationships, not copied assets or invented source facts;
7. responsive translation may recrop/reposition/recompose while preserving role and required content;
8. Project `DESIGN.md` can persist compact imagery/focal authority and actual-render verification remains required.

- [ ] **Step 1: Write the new test file with all eight contracts**

Follow the static-contract style already used by Craft, Typography, Reference, and Color tests. Test actual required prose/structure in the shipped skill/template; do not build a fake policy engine.

- [ ] **Step 2: Run only the imagery test file**

Run:

```text
node --test tests/joedesign-imagery-focal-core.tests.mjs
```

Expected: RED because the current shipped skill/template does not yet satisfy the Imagery Core contract.

- [ ] **Step 3: Preserve the full RED output**

Save it as:

`fixtures/contract-cases/evidence/astra-smoke-v1/imagery-focal-v1/imagery-red-tests.txt`

- [ ] **Step 4: Commit the RED contracts and evidence**

Commit message:

```text
test: add JOEDESIGN imagery focal contracts
```

Do not modify expected semantic decisions.

---

## Task 3: Implement the smallest shipped imagery behavior

**Files:**
- Modify: `skills/joedesign/SKILL.md`
- Modify: `skills/joedesign/templates/DESIGN.md`
- Test: `tests/joedesign-imagery-focal-core.tests.mjs`

**Interfaces:**
- Consumes: eight RED contracts.
- Produces: minimal shipped behavior and compact persistence structure.

- [ ] **Step 1: Add one compact Imagery / Focal Ownership section to `SKILL.md`**

It must encode, without duplicating the whole doctrine:

```text
role before asset treatment
FOCAL / SUPPORT / DECORATIVE
informative imagery preserves Product meaning
intentional focal owner or sequence
text-image dominance is deliberate
crop/focal region before blind center-crop
scale/negative space express priority
reference relationship ≠ copied asset
responsive recrop/reposition/recompose
actual target render required
```

Keep this section concise. Do not add a second runtime subsystem.

- [ ] **Step 2: Add the smallest durable imagery block to the `DESIGN.md` template**

Use a compact structure capable of storing:

```text
Role
Focal owner
Text-image relationship
Important focal/crop rule
Responsive translation
Approved evidence
```

Unknown/unused values may remain empty. Do not make completion mandatory.

- [ ] **Step 3: Run imagery contracts**

Run:

```text
node --test tests/joedesign-imagery-focal-core.tests.mjs
```

Expected: `8 PASS / 0 FAIL`.

- [ ] **Step 4: Preserve GREEN output**

Save as:

`fixtures/contract-cases/evidence/astra-smoke-v1/imagery-focal-v1/imagery-green-tests.txt`

- [ ] **Step 5: Commit minimal implementation**

Commit message:

```text
feat: add bounded imagery focal behavior
```

---

## Task 4: Refresh semantic evidence before demanding the full suite

**Files:**
- Modify: `fixtures/contract-cases/observed.json`
- Preserve prior observed evidence under history before replacement.
- Add: `fixtures/contract-cases/evidence/astra-smoke-v1/imagery-focal-v1/semantic-final.json`
- Add provenance manifest for the fresh run.

**Interfaces:**
- Consumes: current shipped skill bytes after Task 3.
- Produces: fresh GPT-6 Astra xhigh 14-case semantic evidence tied to the current skill SHA.

- [ ] **Step 1: Archive the previous observed/review evidence**

Do not delete Color Core evidence.

- [ ] **Step 2: Run the unchanged 14 semantic contract scenarios with fresh GPT-6 Astra xhigh**

Expected actions remain exactly the existing contract expectations.

- [ ] **Step 3: Require 14/14 PASS**

If any semantic case fails, report the actual failure and diagnose the runtime behavior. Do not modify expected answers to force PASS.

- [ ] **Step 4: Record current shipped skill hashes and runtime provenance**

At minimum record:

```text
model
effort
threadId
codex-cli version
SKILL.md SHA-256
agents/openai.yaml SHA-256
templates/DESIGN.md SHA-256
case data hash
rollout/evidence hash where available
```

- [ ] **Step 5: Commit fresh semantic evidence**

No Smoke H yet.

---

## Task 5: Run the full 56-contract suite

**Files:**
- Evidence: `fixtures/contract-cases/evidence/astra-smoke-v1/imagery-focal-v1/post-semantic-contract-tests.txt`

**Interfaces:**
- Consumes: imagery implementation + fresh semantic evidence.
- Produces: current full static gate.

- [ ] **Step 1: Run all six test files**

Run:

```text
node --test tests/joedesign-contract.tests.mjs tests/joedesign-craft-core.tests.mjs tests/joedesign-typography-scale-core.tests.mjs tests/joedesign-reference-intelligence-core.tests.mjs tests/joedesign-color-contrast-core.tests.mjs tests/joedesign-imagery-focal-core.tests.mjs
```

Expected: `56 PASS / 0 FAIL`.

- [ ] **Step 2: Preserve full output**

Save the exact output.

If this fails due to stale repository allowlists, repair only the harness defect that is proven by the error. Do not alter shipped behavior unless the failure actually concerns shipped behavior.

---

## Task 6: Smoke H — neutral imagery/focal rendered proof

**Files:**
- Create under: `fixtures/contract-cases/evidence/astra-smoke-v1/smoke-h/`
- Durable summary under: `fixtures/contract-cases/evidence/astra-smoke-v1/imagery-focal-v1/`

**Interfaces:**
- Consumes: current JOEDESIGN skill, invented neutral fixture, local supplied image asset.
- Produces: actual desktop/mobile before/after evidence proving role, focal ownership, crop, and responsive translation.

### Neutral fixture

Use a fictional product, not BIO.

Recommended target: **Specimen Review Page** with one supplied local vector/raster specimen image, fixed title/metadata/action, and an APPROVED project direction that requires the specimen image to own the primary visual focal point while text remains a quiet editorial anchor.

The pre-edit implementation must contain a material imagery defect such as:

- the specimen is visually demoted to a small generic side thumbnail;
- the important specimen region is poorly centered/cropped on mobile;
- decorative treatment competes with the specimen;
- text/image loudness does not match the approved focal relationship.

The task is bounded visual correction. Product content, record meaning, required action, and approved direction stay fixed.

- [ ] **Step 1: Record an imagery-role map before editing**

Record:

```text
image role
intended focal owner
important subject/focal region
text-image relationship
crop/framing issue
responsive expectation
```

- [ ] **Step 2: Preserve immutable Product and APPROVED DESIGN inputs**

Hash them before edits.

- [ ] **Step 3: Run JOEDESIGN against the neutral fixture**

Allow only the smallest relevant implementation changes.

- [ ] **Step 4: Render actual desktop `1440×1000` before/after**

- [ ] **Step 5: Render actual mobile viewport `390×844` before/after**

Full-page PNG height may exceed 844; record the viewport separately from screenshot document height.

- [ ] **Step 6: Inspect the actual images**

Require evidence for:

```text
H1 role mapping is explicit before edit
H2 intended focal owner is visually dominant after edit
H3 text-image hierarchy is intentional, not accidental co-dominance
H4 important specimen/focal region remains visible
H5 crop/framing is deliberate at desktop
H6 mobile recrop/reposition preserves focal intent
H7 decorative imagery/effects do not steal ownership
H8 Product Truth and APPROVED DESIGN bytes remain unchanged
H9 user acceptance remains NOT_GRANTED
```

- [ ] **Step 7: Record PASS / FAIL / UNVERIFIED per observable**

Do not infer actual image quality from CSS or DOM alone.

- [ ] **Step 8: Preserve portable repository evidence**

Include before/after PNG links, proof markdown, role map, immutable hashes, and runtime provenance.

---

## Task 7: Final revalidation and readiness report

**Files:**
- Evidence: `fixtures/contract-cases/evidence/astra-smoke-v1/imagery-focal-v1/final-contract-tests.txt`
- Modify: `fixtures/contract-cases/review-evidence.json`
- Preserve prior review evidence under history.

**Interfaces:**
- Consumes: all current imagery implementation/evidence.
- Produces: Program Review candidate.

- [ ] **Step 1: Check whether Smoke H changed any shipped `skills/joedesign/**` bytes**

If YES:

```text
fresh semantic 14/14
→ full 56/56
→ rerun affected Smoke H evidence
```

If NO, the Task 4 semantic run may be reused with explicit byte-hash proof.

- [ ] **Step 2: Run the complete 56-test suite again**

Expected: `56 PASS / 0 FAIL`.

- [ ] **Step 3: Verify package boundaries**

Require:

```text
public entrypoint count = 1
competitor dependency count = 0
runtime dependency count = 0
BIO exposure count = 0
```

- [ ] **Step 4: Verify clean tree and remote branch match**

- [ ] **Step 5: Commit and push all durable evidence**

- [ ] **Step 6: Report exactly one status**

Success:

```text
JOEDESIGN_IMAGERY_FOCAL_CORE_READY_FOR_PROGRAM_REVIEW
```

Failure:

```text
JOEDESIGN_IMAGERY_FOCAL_CORE_NOT_READY
```

The report must include:

```text
Repository
Branch
HEAD
Tree
Static contracts
Fresh semantic replay
Smoke H verdict and repository evidence path
Desktop/mobile observation status
Product Truth invariant
User acceptance boundary
Skill SHA-256
DESIGN template SHA-256
Public entrypoint count
Competitor/runtime dependency count
BIO exposure count
Known failures
Unverified boundaries
```
