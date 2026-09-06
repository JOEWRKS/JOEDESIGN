# JOEDESIGN Color / Contrast Core v0.1 — Codex Handoff

**Repository:** `JOEWRKS/JOEDESIGN`  
**Branch:** `codex/joedesign-v0.1-color-contrast-core`  
**Role:** implementation + validation only  
**Program Lead owns:** doctrine, final gate, competition decision

## Authority order

Read in this order before editing:

1. `AGENTS.md`
2. `docs/roadmaps/JOEDESIGN_V0_1_IMPLEMENTATION_ROADMAP.md`
3. `docs/architecture/JOEDESIGN_OPERATING_MODEL_V1.md`
4. `docs/specs/joedesign-color-contrast-core-v0.1.md`
5. `docs/specs/joedesign-craft-core-v0.1.md`
6. `docs/specs/joedesign-typography-scale-core-v0.1.md`
7. `docs/specs/joedesign-reference-intelligence-core-v0.1.md`
8. `docs/superpowers/plans/2026-09-06-joedesign-color-contrast-core-v0.1.md`

Reference Intelligence is already CLOSED. Do not reopen or redesign it.

Implementation Bridge exists on another branch and is out of scope here.

---

## Mission

Implement and validate **Color / Contrast Core only**.

Target behavior:

```text
Role before color value
→ semantic color roles
→ contrast hierarchy
→ accent ownership
→ surface/layer coherence
→ state semantics
→ applicable accessibility gate
→ contextual actual-render verification
```

The goal is stronger visual hierarchy, not a universal palette or more process.

---

## Hard boundaries

Do not:

- change Product authority behavior;
- change `DESIGN.md` lifecycle;
- add a new public skill or public mode;
- add a palette database;
- add automatic palette/theme generation;
- add a color router or vendor engine;
- install Google/OmD/Awesome/competitor runtime dependencies;
- add Implementation Bridge code;
- use BIO project content or design direction;
- modify existing expected semantic actions to fit a failure;
- erase historical failures/evidence;
- declare `COLOR_CONTRAST_CORE = CLOSED` yourself.

Keep the implementation minimal. The expected shipped change is one bounded `SKILL.md` craft section plus a compact `DESIGN.md` Color / Surface persistence structure.

---

## Required execution

Follow the implementation plan exactly:

`docs/superpowers/plans/2026-09-06-joedesign-color-contrast-core-v0.1.md`

Use TDD:

```text
contracts first
→ observe RED
→ minimal runtime/template implementation
→ GREEN
→ full static suite
→ fresh semantic replay
→ Smoke G
→ final gate
```

### Static gate

Expected final suite:

```text
48 PASS / 0 FAIL
```

Breakdown:

```text
Process / Authority   16
Spatial Craft          8
Typography / Scale     8
Reference Intelligence 8
Color / Contrast       8
```

### Semantic gate

Fresh runtime:

```text
gpt-6-astra
reasoning: xhigh
```

Use the existing unchanged 14 decision scenarios.

Required:

```text
14/14 PASS
```

### Smoke G

Neutral fictional target only: **Operations Review Portal**.

Required target viewports:

```text
Desktop 1440×1000
Mobile 390×844
```

Smoke G must prove:

- semantic color-role map before editing;
- one clear dominant accent owner or an explicit justified multi-accent role model;
- primary/supporting contrast hierarchy;
- no arbitrary state-color reuse for decoration;
- meaningful state/current-priority cues are not color-only;
- surface/layer color corresponds to actual structural relationships;
- applicable WCAG 2.2 AA contrast minimums are met;
- mobile/background context is rechecked independently;
- actual browser render is observed;
- Product Truth remains unchanged;
- user acceptance is not inferred.

Durable evidence must include at least:

```text
before-desktop.png
after-desktop.png
before-mobile.png
after-mobile.png
color-role-manifest.json
```

Keep additional evidence only when it materially supports the gate.

---

## External standards boundary

Use the doctrine as the local authority. For accessibility calculations, WCAG 2.2 AA minimums apply where relevant:

```text
normal text: 4.5:1
large-scale text: 3:1
meaningful UI/state/non-text visual information: 3:1
```

Do not convert these minimums into a universal high-contrast aesthetic rule.

---

## Final report

If every gate passes, report exactly:

```text
JOEDESIGN_COLOR_CONTRAST_CORE_READY_FOR_PROGRAM_REVIEW

Repository:
Branch:
HEAD:
Tree:

Static contracts:
Semantic replay:
Smoke G:

Smoke G:
- Role mapping:
- Contrast hierarchy:
- Accent ownership:
- Surface/layer coherence:
- State semantics:
- Color-only cue prevention:
- Accessibility gate:
- Desktop observation:
- Mobile observation:
- Product Truth invariant:
- User acceptance boundary:

Skill SHA-256:
DESIGN template SHA-256:

Public entrypoint count:
Competitor dependency count:
BIO exposure count:

Known failures:
Unverified:
```

If any required item fails:

```text
JOEDESIGN_COLOR_CONTRAST_CORE_NOT_READY
```

Preserve the failure and stop. Do not weaken the gate or change expected answers to obtain READY.
