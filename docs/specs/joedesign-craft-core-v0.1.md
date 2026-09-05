# JOEDESIGN Craft Core v0.1

**Status:** CANONICAL CRAFT DOCTRINE — PRE-IMPLEMENTATION BASELINE  
**Product:** JOEDESIGN  
**Scope:** native visual-craft philosophy and spatial-hierarchy grammar  
**Dependency policy:** no competitor runtime/vendor dependency

---

# 1. Purpose

JOEDESIGN must not only manage design work correctly. It must also carry a clear native philosophy for what makes a visual composition coherent, legible, intentional, and structurally unified.

This document defines that philosophy before implementation so later features, heuristics, and benchmark changes do not dilute the original intent.

The primary craft objective is:

> **Hierarchy before decoration. Build an intentional visual flow first; use spacing, scale, typography, position, contrast, imagery, and surface treatment to reinforce that hierarchy.**

JOEDESIGN must be able to answer, before polish:

1. Where should the eye enter?
2. What should it see second and third?
3. Which information belongs together?
4. Which boundary marks a meaningful change of topic, function, or narrative?
5. Does the visual weight match the Product Truth priority?
6. Does the spacing system make those relationships visible without relying on decorative containers?

A visually attractive result that cannot answer these questions is not a successful JOEDESIGN result.

---

# 2. Authority layers

Craft authority is layered so product meaning and project-specific design truth remain protected.

```text
Product Definition / approved Product Truth
        ↓
Project APPROVED DESIGN.md
        ↓
JOEDESIGN Craft Invariants
        ↓
JOE Default Taste / Spatial Profile
```

- Product Definition owns meaning and behavior.
- Project `DESIGN.md` owns approved project-specific visual truth.
- Craft Invariants define how JOEDESIGN reasons about hierarchy, grouping, spacing, flow, and visual coherence.
- JOE Default Taste provides a strong default when the project has not approved a conflicting visual decision.

Project-specific density, style, or art direction may change the default profile. Such changes should be deliberate and systemic, not local arbitrary values.

---

# 3. Craft invariants

## 3.1 Visual hierarchy is first-class

Every material surface must have an intentional hierarchy.

JOEDESIGN should determine:

- primary focal point;
- secondary information;
- tertiary/supporting information;
- visual entry point;
- next visual destination;
- major transitions in the reading/task flow.

Do not give every element equal visual weight.

Hierarchy should be expressed through coordinated relationships between:

- composition and placement;
- scale and proportion;
- typography;
- spacing and whitespace;
- contrast and tone;
- image/artwork ownership;
- motion when applicable.

Font size alone is not hierarchy.

## 3.2 Visual flow must be deliberate

A surface is not a collection of components. It is a sequence of visual attention.

JOEDESIGN should be able to describe the intended flow in plain language, for example:

```text
Headline establishes the entry point
→ artwork carries attention toward the evidence block
→ evidence hierarchy resolves into the primary action
→ section spacing marks the next narrative chapter
```

If the observed render creates a materially different flow, the composition must be reconsidered rather than explained away.

## 3.3 Group by meaning before styling

Related information becomes a visual group before it becomes a card, component, bordered region, or background surface.

Use proximity, alignment, whitespace, scale, and typographic relation before adding decorative containers.

The same semantic relationship should reuse the same visual role unless project-specific evidence requires otherwise.

## 3.4 System before one-off values

Arbitrary local spacing and sizing should be treated as evidence that a role or scale may be missing.

A value is not justified merely because it looks acceptable in one location.

JOEDESIGN should prefer:

```text
semantic relationship
→ reusable role
→ canonical token
```

over:

```text
individual element
→ local margin/padding guess
```

---

# 4. Visual Block Tree

Before assigning material spacing, JOEDESIGN should interpret the surface as a semantic visual tree rather than relying on DOM depth or component nesting.

Default structural model:

```text
SURFACE
└─ SECTION
   └─ MAJOR GROUP
      └─ SUBGROUP
         └─ ITEM GROUP
            └─ ITEM / MICRO CONTENT
```

The labels may change by project. The relationship logic must not.

A `SECTION` is a meaningful narrative or functional chapter.

A `MAJOR GROUP` is a high-level unit inside a section.

A `SUBGROUP` is a distinct cluster inside a major group.

An `ITEM GROUP` is a repeated or smaller content cluster.

`ITEM / MICRO CONTENT` contains tightly bound content such as icon-label, eyebrow-headline, label-value, or other local relations.

This hierarchy is semantic. It must not be inferred mechanically from HTML nesting, React component boundaries, Figma frames, or visual containers.

---

# 5. Spacing belongs to boundaries, not elements

This is the central spatial rule.

> **Spacing belongs to the relationship between two visual blocks. It is not an intrinsic property of an element.**

Do not reason:

```text
This is a level-3 element, therefore margin-bottom: 16px.
```

Reason instead:

```text
These two blocks are sibling item groups inside the same subgroup,
therefore their boundary uses the group-3 spacing role.
```

This prevents a common failure where one level is accidentally collapsed into another because individual child elements reuse the same local margin.

## 5.1 Structural separation hierarchy

JOE default spatial roles:

| Relationship role | Default token | Meaning |
|---|---:|---|
| `space-section` | `160px` | between distinct narrative / functional sections |
| `space-group-1` | `48px` | between major groups inside one section |
| `space-group-2` | `24px` | between subgroups inside one major group |
| `space-group-3` | `16px` | between item groups / repeated local groups |
| `space-tight` | `8px` | strongly bound content inside one group |
| `space-micro` | `4px` | micro relations such as icon-label or label-value |

These values are the JOE default profile, not a universal requirement for every product density.

The hierarchy itself is more important than the exact numbers.

If a project needs a compact or unusually spacious density, change the spatial profile as a system and preserve role distinctions. Do not independently mutate one section to `43px`, another to `37px`, and another to `52px` without a semantic reason.

## 5.2 Same relationship, same role

If two relationships are structurally equivalent, they should use the same spacing role across the surface.

Example:

```text
SECTION A
├─ GROUP A1
│  ├─ SUBGROUP A1-a
│  │  ├─ ITEM GROUP A1-a-1
│  │  └─ ITEM GROUP A1-a-2   ← 16
│  └─ SUBGROUP A1-b          ← 24
└─ GROUP A2                  ← 48

SECTION B                      ← 160 from SECTION A
├─ GROUP B1
│  ├─ SUBGROUP B1-a
│  │  ├─ ITEM GROUP B1-a-1
│  │  └─ ITEM GROUP B1-a-2   ← 16
```

A's level-3 sibling relation and B's level-3 sibling relation both use `space-group-3`.

That does **not** mean every parent-child or nested relation inside A also becomes `16px`.

## 5.3 Parent-child binding is not sibling separation

Structural separation and content binding are different questions.

Example:

```text
Text Block
├─ Eyebrow
├─ Headline
├─ Description
└─ Actions
```

These nodes can belong to one semantic group while having different binding strength.

Possible default relation:

```text
Eyebrow
  ↓ 8
Headline
  ↓ 16
Description
  ↓ 24
Actions
```

The values come from the relationship roles, not from the raw nesting depth.

Do not automatically assign a structural level token to every parent-child relation.

---

# 6. Structural hierarchy vs binding hierarchy

JOEDESIGN must distinguish two spatial concepts.

## Structural hierarchy

Defines separation between meaningful groups.

```text
SECTION
→ MAJOR GROUP
→ SUBGROUP
→ ITEM GROUP
```

Primary roles:

```text
160 / 48 / 24 / 16
```

## Binding hierarchy

Defines how tightly content is related inside a group.

Primary roles:

```text
8 / 4
```

`16` may also be used inside a content block when that relationship genuinely corresponds to an item-group boundary, but not merely because it is available.

Never collapse structural levels simply to make spacing numerically uniform.

Uniformity means equivalent relationships reuse equivalent roles, not that every gap becomes identical.

---

# 7. The meaning of the 4px grid

JOEDESIGN uses a 4px spatial base for a specific reason:

> **Reduce the number of arbitrary spatial choices so repeated proportions create visual unity, rhythm, and predictability across the design.**

The intent is not to allow every possible multiple of four.

Bad interpretation:

```text
Anything divisible by 4 is acceptable:
20, 28, 36, 44, 52, 68, 76 ...
```

Preferred interpretation:

```text
Use a deliberately small canonical token set built on a 4px base.
```

Default canonical spacing set:

```text
4, 8, 16, 24, 48, 160
```

Additional project tokens may be introduced only when a recurring semantic role proves the need.

The 4px spatial grid primarily governs:

- margin;
- padding;
- gap;
- section/group spacing;
- repeated layout offsets;
- recurring component spatial dimensions where appropriate.

It does not require every typography value, line-height, letter-spacing, border width, fluid dimension, or image-derived size to be divisible by four.

## Optical correction

Mathematical consistency does not override observed optical balance.

However, optical correction must not silently create a new spacing role.

A very small non-layout nudge may be used for glyph/icon/stroke alignment when visually necessary, but layout spacing should remain on the canonical spatial system.

If many optical exceptions are required, reassess the underlying hierarchy or token profile instead of accumulating local fixes.

---

# 8. Size systems follow the same philosophy

JOEDESIGN should not create a different size for every individual element without a reusable role.

Repeated dimensions should be organized by semantic roles where appropriate, for example:

- control height roles;
- icon size roles;
- container width roles;
- image/artwork scale roles;
- radius roles;
- type roles.

Typography does not have to use 4px multiples, but it should still use a restrained role-based scale rather than unrelated one-off font sizes.

The goal is not numeric sameness. The goal is a visible system of repeated proportions.

---

# 9. Whitespace is active hierarchy

Whitespace is not leftover empty space and it is not automatically better when larger.

Whitespace communicates:

- grouping;
- separation;
- importance;
- rhythm;
- pause;
- transition;
- density.

A larger gap should normally correspond to a more important structural boundary.

A smaller gap should normally communicate stronger semantic binding.

Do not use borders, cards, backgrounds, or separators to compensate for grouping that spacing and alignment should already make clear.

---

# 10. Responsive translation

Responsive design preserves hierarchy roles and visual flow, not desktop coordinates.

Do not proportionally shrink every desktop gap.

Instead:

1. preserve semantic grouping;
2. preserve priority order;
3. preserve relative boundary importance;
4. select a responsive spatial profile appropriate to the viewport/density;
5. re-render and inspect the actual visual flow.

If desktop uses a spacious profile and mobile needs a denser profile, the profile should change coherently rather than through unrelated per-element overrides.

---

# 11. Anti-patterns

JOEDESIGN should actively challenge these patterns:

- arbitrary margin/padding values attached independently to elements;
- treating DOM/component depth as visual hierarchy;
- applying the same gap to multiple hierarchy levels without semantic justification;
- using different gaps for equivalent relationships in different sections;
- making every gap identical in the name of consistency;
- adding cards/borders because semantic grouping is unclear;
- using every 4px multiple as if it were a valid design token;
- introducing a one-off spacing value because one screenshot looks acceptable;
- shrinking desktop spacing numerically for mobile without rebuilding the hierarchy;
- using optical correction to bypass a broken spatial system;
- allowing decorative styling to determine hierarchy after the fact.

---

# 12. Craft review sequence

Before declaring a material composition visually successful, inspect in this order:

```text
1. Product priority
2. Visual entry point
3. Visual flow
4. Semantic Visual Block Tree
5. Structural hierarchy
6. Binding hierarchy
7. Spacing-role consistency
8. Scale / typography / contrast relationships
9. Imagery / focal ownership
10. Responsive translation
11. Optical refinement
12. Decorative detail
```

Do not reverse this order by polishing surfaces before the hierarchy works.

---

# 13. Minimum evidence for spatial consistency

For a material design proof, JOEDESIGN should be able to identify:

- the major Visual Block Tree;
- the intended visual flow;
- which spacing roles are used at the material boundaries;
- whether equivalent relationships reuse the same role;
- any deliberate exception and its reason;
- the actual rendered observation.

The system does not need to expose all of this ceremony to the user in ordinary work, but the reasoning must remain internally coherent and recoverable when a design decision is challenged.

---

# 14. Canonical doctrine

> **JOEDESIGN builds visual hierarchy before decoration. It organizes content into semantic visual blocks, designs an intentional path for the eye, and assigns spacing to relationships between those blocks rather than to isolated elements. Equivalent hierarchy boundaries reuse equivalent spacing roles. Different hierarchy levels remain visibly distinct. Layout spacing comes from a deliberately small 4px-based token system whose purpose is to reduce arbitrary choices and create visual unity—not to make every gap identical or to permit every multiple of four. Project-specific density may change the profile, but it should change systemically. Optical judgment may refine the result, but it must not dissolve the hierarchy or replace the spacing system with local exceptions.**
