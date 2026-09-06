# JOEDESIGN Implementation Bridge v0.1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Preserve approved JOEDESIGN visual truth when it is translated into implementation tokens and project-native code without making Google design.md or any external tool a runtime dependency.

**Architecture:** Keep Project `DESIGN.md` as visual authority. The Implementation Bridge is a bounded translation contract inside the single `joedesign` skill: exact approved tokens may be mapped into an existing project token system, while unknown values remain unresolved. Google design.md compatibility is accepted as an optional structured-token input/output shape, not as authority or a required parser/CLI.

**Tech Stack:** Markdown skill contract, Node.js built-in test runner, existing JOEDESIGN fixtures/evidence.

**Spec:** `docs/architecture/JOEDESIGN_OPERATING_MODEL_V1.md`

## Global Constraints

- One public skill only: `joedesign`.
- Product Truth and APPROVED Project `DESIGN.md` remain above implementation mappings.
- No Google package/runtime dependency.
- No new parser, token database, vendor router, installer, or public command.
- Do not fabricate exact tokens from prose or unknown reference data.
- Existing project token architecture is preferred over forcing a new naming scheme.
- Technical token mapping does not prove visual conformance; actual rendered verification remains required.

---

### Task 1: Define the Implementation Bridge contract

**Files:**
- Create: `docs/specs/joedesign-implementation-bridge-v0.1.md`
- Modify: `AGENTS.md`

**Interfaces:**
- Consumes: approved Project `DESIGN.md`, project implementation context, exact sourced token values.
- Produces: canonical bridge rules for authority, mapping, unresolved values, optional Google-compatible token shapes, and verification boundaries.

- [ ] **Step 1:** Write the bridge spec with explicit authority and non-goals.
- [ ] **Step 2:** Add one AGENTS pointer to the canonical bridge spec.
- [ ] **Step 3:** Verify the spec does not introduce a new public skill, dependency, CLI, parser, or token database.
- [ ] **Step 4:** Commit.

### Task 2: Add failing bridge contracts before runtime behavior

**Files:**
- Create: `tests/joedesign-implementation-bridge.tests.mjs`
- Modify: `tests/joedesign-contract.tests.mjs`

**Interfaces:**
- Consumes: `skills/joedesign/SKILL.md` and the canonical bridge spec.
- Produces: deterministic static contracts that fail until bridge behavior exists.

Required contracts:
1. Visual authority remains in approved `DESIGN.md`; bridge mappings are derivative.
2. Exact values may be mapped; unknown values are not invented.
3. Existing project-native tokens are preferred over forced renaming.
4. Structured tokens and prose remain distinct: tokens are exact values, prose is intent/rationale.
5. Google-style YAML token shapes are optional interoperability, not a dependency.
6. Unknown/custom DESIGN.md sections must be preserved when interoperating.
7. Mapping changes require bounded diff/review when material.
8. Token/code success does not replace actual rendered visual verification.

- [ ] **Step 1:** Write the eight failing tests.
- [ ] **Step 2:** Run them and record RED evidence.
- [ ] **Step 3:** Add the new spec/test path to the repository allowlist only.
- [ ] **Step 4:** Commit.

### Task 3: Implement minimal bridge behavior in JOEDESIGN

**Files:**
- Modify: `skills/joedesign/SKILL.md`

**Interfaces:**
- Consumes: canonical bridge rules from Task 1.
- Produces: agent behavior that translates approved visual truth into project-native implementation without changing authority.

- [ ] **Step 1:** Add one compact `Bridge approved design into implementation` section.
- [ ] **Step 2:** Require exact-token provenance and unresolved-value preservation.
- [ ] **Step 3:** Prefer existing project token architecture; do not force Google names.
- [ ] **Step 4:** Support Google-style structured token frontmatter when present, preserving custom Markdown sections.
- [ ] **Step 5:** Keep lint/diff/export as optional interoperability concepts; do not require Google tooling.
- [ ] **Step 6:** Require actual rendered observation after implementation.
- [ ] **Step 7:** Run bridge contracts and full static suite.
- [ ] **Step 8:** Commit.

### Task 4: Fresh runtime verification

**Files:**
- Update only evidence/fixture files required by verification.

**Interfaces:**
- Consumes: new shipped skill bytes.
- Produces: fresh Astra semantic evidence and one bridge-specific neutral smoke.

Smoke F must prove:
- APPROVED `DESIGN.md` exact tokens are mapped to an existing project token system.
- Unknown visual values remain unresolved rather than invented.
- Existing semantic token names are preserved when equivalent.
- Optional Google-compatible structured tokens can be consumed without replacing JOEDESIGN authority.
- Custom JOEDESIGN sections survive interoperability.
- A material token mapping diff is reported.
- Successful token/code mapping remains visually UNVERIFIED until the actual render is inspected.
- User acceptance remains separate.

- [ ] **Step 1:** Refresh the 14-case Astra semantic replay for new skill bytes.
- [ ] **Step 2:** Run neutral Smoke F at desktop/mobile target where applicable.
- [ ] **Step 3:** Store compact durable evidence and hashes only.
- [ ] **Step 4:** Run full contract suite.
- [ ] **Step 5:** Report `JOEDESIGN_IMPLEMENTATION_BRIDGE_READY_FOR_PROGRAM_REVIEW` only if all required evidence passes.
