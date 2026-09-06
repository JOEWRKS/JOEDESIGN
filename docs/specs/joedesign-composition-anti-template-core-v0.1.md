# JOEDESIGN Composition / Anti-template Core v0.1

**Status:** CANONICAL CRAFT DOCTRINE — IMPLEMENTATION BASELINE  
**Product:** JOEDESIGN  
**Scope:** composition grammar, structural hierarchy, containment, repetition/variation, anti-template judgment, responsive recomposition  
**Dependency policy:** no pattern database, template detector service, vendor runtime, or new public entrypoint

---

# 1. Purpose

JOEDESIGN should compose interfaces from Product priority and visual relationships instead of defaulting to familiar AI/SaaS layout recipes.

The objective is:

> **Structure before pattern. Choose composition because it expresses the Product hierarchy and flow, not because the pattern is familiar, trendy, or easy to generate.**

Anti-template does not mean avoiding common UI forms. It means refusing to use a form without a project-specific structural reason.

---

# 2. Composition starts from Product priority

Before choosing a page pattern, identify:

- what the user must notice first;
- what should follow second and third;
- what information belongs together;
- what must remain independently actionable;
- whether the surface is narrative, task-driven, comparative, exploratory, transactional, or mixed;
- where structural transitions should occur.

Prefer:

```text
Product priority / task or narrative sequence
→ semantic visual blocks
→ structural relationships
→ composition
→ styling details
```

over:

```text
familiar template
→ fit content into slots
→ decorate
```

A composition that cannot explain why its major regions exist is not yet justified.

---

# 3. Pattern is a consequence, not an authority

Common patterns may be correct when they serve the Product.

Examples:

- a card can be correct for a genuinely bounded independent object;
- a two-column split can be correct when two peers need simultaneous comparison;
- a hero with adjacent imagery can be correct when text and image intentionally share focal ownership;
- pills can be correct for compact selectable/filterable categories;
- repeated tiles can be correct when the Product exposes a repeated collection with equivalent status.

The same patterns become defects when used only because they are familiar.

Do not automatically choose:

- `headline + paragraph + CTA + right image`;
- three equal feature cards;
- a wall of rounded containers;
- decorative pill clouds;
- floating gradient/blob ornaments;
- identical section shells repeated down the page;
- equal visual loudness for every section.

These are **challenge triggers**, not blanket bans.

---

# 4. Semantic containment before cards

A card, panel, box, or surface should normally correspond to a meaningful containment relationship such as:

- an independently selectable object;
- a reusable bounded record;
- a stateful unit;
- a discrete comparison target;
- an interaction surface that needs local grouping;
- content that must remain visually distinct from its surroundings.

Do not add a container merely to make loose content look designed.

If proximity, alignment, typography, whitespace, sequence, or a rule can express the relationship more clearly, prefer the lighter structure.

Containment should reveal semantics, not manufacture them.

---

# 5. Structural contrast creates rhythm

Composition needs variation in scale, density, alignment, whitespace, and grouping when the Product priorities differ.

Avoid making every section:

- the same height;
- the same number of columns;
- equally boxed;
- equally loud;
- equally centered;
- equally dense;
- equally decorative.

Use repetition when it communicates equivalence or continuity. Use variation when Product priority, content role, or narrative phase changes.

A repeated visual grammar should have an explicit repeated semantic job.

---

# 6. Intentional asymmetry is allowed

Symmetry is not a default requirement.

Asymmetry can improve hierarchy, narrative momentum, editorial character, or focal control when:

- the visual entry point remains clear;
- reading/task order remains understandable;
- alignment relationships stay intentional;
- negative space is controlled;
- the Product does not require peer-equivalent comparison.

Do not introduce asymmetry merely to look unconventional.

Distinctiveness is a consequence of a strong project-specific structure, not random imbalance.

---

# 7. Anti-template is not novelty scoring

JOEDESIGN must not replace generic structure with arbitrary novelty.

Do not:

- make controls unfamiliar solely to look different;
- hide required information for dramatic composition;
- reorder Product semantics without authority;
- break accessibility or reachability for visual tension;
- increase interaction cost only to avoid a common pattern;
- reject an ordinary component when it is the clearest Product solution.

The target is **specificity**, not novelty.

Ask:

> **Could this exact structural choice be explained from this project's Product Truth, visual authority, and content relationships?**

If yes, a common pattern may be appropriate. If no, challenge it.

---

# 8. References do not become templates

Reference Intelligence may contribute a relationship such as:

- editorial asymmetry;
- long-form pacing;
- dense comparison structure;
- a restrained metadata rail;
- a transition from immersive opening to evidence-heavy content.

Do not flatten references into a generic mixed style or copy their complete page grammar.

Use:

```text
reference relationship
→ project-specific structural translation
→ actual proof
```

not:

```text
reference page
→ copy section sequence and component shells
```

Selected references remain below APPROVED Project DESIGN.md and JOEDESIGN Craft authority.

---

# 9. Composition and focal ownership

Composition coordinates the previously defined Craft layers rather than replacing them.

- Spatial Core owns semantic spacing relationships.
- Typography & Scale owns type hierarchy.
- Color / Contrast owns color roles and accent ownership.
- Imagery / Focal Ownership owns image role, crop, and image dominance.
- Composition Core decides how those roles form the larger structural sequence.

Do not duplicate those systems inside Composition Core.

A material composition should be explainable as a set of major structural regions and their relative dominance.

---

# 10. Responsive composition is recomposition

Mobile is not a compressed desktop composition.

Preserve:

- semantic groups;
- Product priority;
- task/narrative order;
- required information and controls;
- equivalent repeated roles.

Allow:

- columns to become a sequence;
- secondary rails to move inline;
- dense comparisons to change presentation;
- asymmetry to simplify;
- repeated objects to change density;
- visual transitions to occur at different spatial moments.

Do not preserve desktop coordinates or ornamental structure when they damage mobile hierarchy.

---

# 11. Material composition review

Before declaring a material composition successful, be able to identify:

1. Product-priority first/second/third destinations;
2. major semantic regions;
3. the intended task or narrative flow;
4. why each major container exists;
5. where repetition communicates equivalence;
6. where variation communicates a change in role or priority;
7. any familiar pattern used and its project-specific justification;
8. any intentionally rejected generic pattern and why;
9. desktop/mobile structural translation.

Then inspect the actual target render.

Code structure, DOM correctness, component count, or layout-token existence cannot establish composition quality.

---

# 12. Project DESIGN.md persistence

Persist only durable approved composition decisions, for example:

```text
Composition Intent
- Primary structural sequence
- Major region roles
- Containment rules
- Repetition / variation rules
- Intentional asymmetry or alignment logic
- Explicit anti-patterns for this project
- Responsive composition intent
```

Do not store a giant catalog of forbidden templates.

A project-specific approved pattern may override JOE default caution when Product Truth and evidence justify it.

---

# 13. Anti-overexpansion guardrails

Composition / Anti-template Core v0.1 does not include:

- a template database;
- screenshot-classification service;
- AI-slop scoring model;
- visual novelty score;
- saliency model;
- pattern marketplace;
- automatic competitor comparison;
- generated layout search engine;
- separate composition skill;
- vendor runtime dependency.

A future subsystem requires demonstrated competition or production evidence that the lightweight judgment contract is insufficient.

---

# 14. Anti-patterns

Challenge these behaviors:

- choosing a layout before understanding Product priority;
- putting every content group into a card;
- repeating identical section shells without repeated semantics;
- using `hero + right image` automatically;
- forcing three equal features because three-column grids are familiar;
- adding pills that are neither selectable nor semantically categorical;
- adding floating ornaments that compete with Product hierarchy;
- making every section equally loud;
- copying a reference's page grammar instead of its relevant relationship;
- shrinking desktop composition into mobile;
- creating novelty that increases Product friction;
- claiming composition PASS without observing the actual render.

---

# 15. Canonical doctrine

> **JOEDESIGN composes from Product priority, semantic relationships, and task or narrative flow before choosing a familiar layout pattern. Common patterns remain valid when they have a project-specific structural reason; otherwise they are challenged rather than used by default. Containers correspond to real containment, repetition expresses real equivalence, variation expresses meaningful change, and intentional asymmetry may support hierarchy without becoming novelty for its own sake. Mobile recomposes the same priorities rather than shrinking desktop coordinates. References contribute relationships, not complete templates. Material composition claims require actual target renders, while Product Truth, approved visual authority, accessibility, and user acceptance remain separate boundaries.**
