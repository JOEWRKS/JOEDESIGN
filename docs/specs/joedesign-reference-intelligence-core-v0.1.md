# JOEDESIGN Reference Intelligence Core v0.1

**Status:** CANONICAL REFERENCE DOCTRINE — IMPLEMENTATION BASELINE  
**Product:** JOEDESIGN  
**Scope:** reference provenance, evidence awareness, relationship extraction, and bounded adoption  
**Dependency policy:** no bundled reference corpus, vendor runtime, automatic router, or new public entrypoint

---

# 1. Purpose

JOEDESIGN should benefit from strong external design references without becoming a style-copy engine, a vendor router, or a database-heavy design framework.

The reference objective is:

> **Use references to learn relationships, not to outsource authority. Preserve what is known, keep what is unknown explicit, and adopt only the visual relationships that serve the current Product Truth and project design authority.**

Reference Intelligence exists to improve design judgment while keeping the system light.

---

# 2. Authority order

References never sit above project truth.

```text
Product Definition / approved Product Truth
        ↓
Project APPROVED DESIGN.md
        ↓
JOEDESIGN Craft Invariants
        ↓
Selected project references
        ↓
JOE Default Taste
```

A reference may inform a design decision. It may not silently alter product meaning, replace an approved project direction, grant user acceptance, or become durable project authority by itself.

---

# 3. Apply reference discipline only when it matters

Do not require a formal reference worksheet for every screenshot, mood image, or casual inspiration.

The compact reference record becomes necessary when JOEDESIGN is about to **materially adopt** a relationship, token pattern, compositional idea, typographic behavior, imagery treatment, interaction treatment, or other reusable design decision from a reference.

For material reference adoption, be able to identify:

- `SOURCE` — where the reference came from;
- `EVIDENCE QUALITY` — how trustworthy the claimed facts are;
- `KNOWN` — what the source actually supports;
- `UNKNOWN` — what is not evidenced;
- `TAKE` — the specific relationship worth adopting;
- `DO NOT TAKE` — unrelated or project-inappropriate parts;
- `WHY` — why the relationship serves this project;
- `APPLIES TO` — the bounded target where it is relevant.

This may remain internal during ordinary work. Expose it to the user only when comparison, approval, ambiguity, or provenance makes it useful.

---

# 4. Evidence quality measures trust, not taste

Evidence quality answers:

> **How confidently can JOEDESIGN treat this description, token, behavior, or relationship as actually belonging to the reference?**

It does **not** answer:

> **How beautiful, prestigious, fashionable, or appropriate is this reference?**

A highly verified reference can still be a poor fit for the project. A weakly documented reference can still inspire a useful relationship, but unsupported details must remain unknown.

Use lightweight qualitative evidence labels when useful, for example:

- `strong` — primary/official or clearly verified evidence;
- `supported` — traceable curated/secondary evidence with reasonable support;
- `weak` — incomplete, inferred, stale, or poorly sourced evidence.

Do not turn these labels into an elaborate scoring system.

---

# 5. Unknown means unknown

Never fill an unsupported reference value because it seems plausible.

Examples:

```text
Unknown font weight → UNKNOWN
Unknown mobile behavior → UNKNOWN
Unknown spacing token → UNKNOWN
Unknown motion timing → UNKNOWN
```

Do not convert these into guessed values and later treat the guesses as source truth.

If a missing value must be designed for the current project, make it a JOEDESIGN/project design decision and label it as such. It is not a recovered reference fact.

---

# 6. Extract relationships, not recipes

A useful reference is usually valuable because of a relationship such as:

- image dominance relative to copy;
- heading/body contrast;
- editorial asymmetry;
- negative-space rhythm;
- object scale relative to viewport;
- foreground/background treatment;
- section transition behavior;
- repeated component density;
- artwork-to-evidence progression;
- restrained or expressive interaction character.

Prefer:

```text
reference relationship
→ why it works
→ project-specific translation
→ target-medium proof
```

over:

```text
reference brand
→ copy its tokens/components/layout
→ rename content
```

Exact brand copy, proprietary assets, unrelated product semantics, and source-specific content are normally `DO NOT TAKE` unless the user explicitly owns or authorizes them.

---

# 7. Multiple references remain scoped

Multiple references may contribute different relationships to one project.

Example:

```text
Reference A → editorial type hierarchy
Reference B → biological artwork ownership
Reference C → restrained interaction rhythm
```

Do not silently blend them into an undefined average style.

When references conflict on a material decision:

1. identify the conflict;
2. preserve the project authority already approved;
3. choose or explore a bounded translation intentionally;
4. prove the affected target;
5. obtain user approval when the decision is material.

Reference count does not create authority by majority vote.

---

# 8. External corpus policy

External corpora are **optional reference sources**, not required JOEDESIGN runtime dependencies.

Current useful source classes include:

- curated/evidence-graded builders such as oh-my-design Builder;
- broader DESIGN.md collections such as awesome-design-md;
- user-provided sites, screenshots, files, products, and brand systems;
- other web or repository references relevant to the task.

Default preference when equivalent material is available:

```text
higher provenance clarity
→ stronger evidence support
→ broader but less verified corpus
```

This ordering concerns source reliability, not aesthetic superiority.

JOEDESIGN v0.1 must not:

- bundle the oh-my-design or awesome-design-md corpus;
- require either service to run;
- automatically route every design task through an external corpus;
- install a reference crawler/router;
- create a persistent cross-project reference database;
- expose another public skill for reference handling.

Reference lookup is conditional: use it when the current project lacks enough visual evidence, the user requests references, a material direction is unresolved, or comparison would materially improve the decision.

---

# 9. Durable project authority remains local

External reference material does not become project authority just because JOEDESIGN used it successfully.

The durable path is:

```text
External reference
→ bounded relationship extraction
→ project-specific candidate/proof
→ actual rendered observation
→ explicit user approval when material
→ Project DESIGN.md
```

Only the approved project-specific decision belongs in durable visual authority.

A project may record a reference pointer and the relationship it informed. It should not copy an external reference database into the root `DESIGN.md`.

---

# 10. Relationship to future DESIGN.md interoperability

Google Stitch / Google `design.md` interoperability belongs to a future **Implementation Bridge**, not this Reference Intelligence Core.

Reference Intelligence decides what a reference means and whether a relationship is worth adopting.

The future Implementation Bridge may handle structured tokens, lint, diff, and exports.

Do not mix these responsibilities now.

---

# 11. Anti-overexpansion guardrails

Reference Intelligence Core v0.1 stops at design judgment.

Not included:

- reference crawler;
- vector database;
- embeddings/search index;
- automatic brand-style matching;
- persistent taste profile;
- provenance sidecar framework;
- System Graph;
- adoption receipt subsystem;
- vendor/plugin router;
- reference marketplace;
- automatic style scoring;
- competitor bundling.

A future addition requires real project or competition evidence that the lighter contract is insufficient.

---

# 12. Anti-patterns

Challenge these behaviors:

- treating a prestigious brand as automatic authority;
- copying a whole design system when only one relationship is relevant;
- inventing missing reference tokens or responsive behavior;
- letting a curated source override Product Truth;
- treating evidence quality as an aesthetic score;
- merging conflicting references without naming the conflict;
- creating a new style from the average of many unrelated references;
- forcing reference research when project visual authority is already sufficient;
- dumping large external DESIGN.md files into project authority;
- requiring source ceremony for trivial inspiration.

---

# 13. Review sequence

For material reference adoption:

```text
1. Product / project authority
2. What decision actually needs help?
3. Source / provenance
4. Evidence quality
5. Known / unknown
6. TAKE / DO NOT TAKE
7. WHY / APPLIES TO
8. Conflict check against other references and approved design
9. Project-specific translation
10. Actual target-medium proof
11. User approval if material
12. Persist only the approved project decision
```

---

# 14. Canonical doctrine

> **JOEDESIGN uses references as evidence for relationships, not as replacement authority. Material adoption records enough provenance to distinguish known facts from unknowns, extracts only the relationship that serves the current project, keeps conflicts explicit, and proves the project-specific translation in the target medium. Evidence quality affects trust in source claims, not aesthetic authority. External corpora remain optional lookup sources and are never bundled or automatically routed through JOEDESIGN. The system stays lightweight: no crawler, vector database, vendor router, or reference sub-platform is justified without demonstrated need.**
