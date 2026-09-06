# JOEDESIGN Color / Contrast Core v0.1

**Status:** CANONICAL COLOR / CONTRAST DOCTRINE — IMPLEMENTATION BASELINE  
**Product:** JOEDESIGN  
**Scope:** semantic color roles, contrast hierarchy, accent ownership, surface/layer color, state color, accessibility, responsive/theme translation  
**Dependency policy:** no palette database, vendor color engine, automatic theme generator, or new public entrypoint

---

## 1. Purpose

Color in JOEDESIGN exists to reinforce Product priority, visual hierarchy, state meaning, and the approved visual world. It is not decoration applied after layout and it is not a fixed JOE palette imposed on every project.

Core rule:

> **Role before color value. Decide what visual job the color performs, then choose or reuse the value that serves that job in the current project.**

This doctrine extends the existing `Hierarchy before decoration` and `Role before value` principles into color.

---

## 2. Authority order

Color decisions follow the existing authority order.

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

A project-approved palette or color behavior overrides JOEDESIGN defaults unless it violates Product Truth or an applicable accessibility requirement.

Do not replace an approved palette merely because another palette is more fashionable, more conventional, or easier to tokenize.

---

## 3. Color roles before palette values

Before assigning material color values, identify the recurring semantic jobs the surface needs. Common role classes include:

- primary / secondary / muted foreground;
- base / raised / nested surface or layer;
- subtle / strong / interactive boundary;
- primary interaction or focal accent;
- success / warning / error / informational state;
- focus / selection / current-state indication;
- expressive or decorative color.

These are role classes, not mandatory token names. A project may need fewer, more, or differently named roles.

Prefer:

```text
semantic job
→ reusable color role
→ project value
```

over:

```text
local element
→ attractive hex value
```

Equivalent roles should behave consistently across the relevant surface. A new color value requires a recurring role, a material expressive reason, or an approved project-specific exception.

---

## 4. Contrast is hierarchy, not maximum darkness

Contrast should make Product priority legible.

Primary information, supporting information, metadata, boundaries, and inactive/background material should not all have the same visual loudness. Build an intentional contrast hierarchy while keeping required content legible.

Do not solve hierarchy by making every important element saturated, bold, or maximally dark. Use color together with typography, scale, spacing, placement, and imagery.

Hue difference alone is not a reliable hierarchy mechanism. When distinction matters, verify luminance/contrast and provide another cue when color alone would carry meaning.

A visually quieter role may use lower relative contrast, but accessibility minimums still apply where required.

---

## 5. Accent ownership

High-chroma or otherwise attention-dominant color should have a clear owner on a bounded surface.

Before using a strong accent, identify what owns it:

- the primary action;
- a focal metric or state;
- signature artwork;
- a navigation/current-state signal;
- another explicitly prioritized object.

Do not spread the same attention-dominant accent across unrelated headings, icons, borders, cards, badges, and backgrounds until everything competes equally.

A surface may intentionally use more than one accent when Product semantics or approved art direction requires distinct roles. The rule is not “one accent color only”; the rule is **each strong color must have a clear role and must not dissolve focal hierarchy**.

If imagery or artwork owns the visual focus, interface accent may need to become quieter so the two systems do not compete.

---

## 6. Neutral and surface hierarchy

Surface color should represent actual structural or visual relationships rather than create a panel for every group.

Use neutral/background/layer changes when they help express:

- containment;
- depth or stacking;
- a meaningful region transition;
- interaction state;
- focal separation;
- the approved art direction.

Do not create endless cards, tinted boxes, or alternating backgrounds solely to make sections feel designed.

Equivalent layer roles should behave consistently. Light and dark themes may assign different values while preserving the same semantic role relationships.

A flat design does not need artificial elevation color; a layered design does not need every layer to use a unique color.

---

## 7. Functional state color preserves Product semantics

State color may express an existing Product state but may not invent or change the state itself.

Examples:

```text
Product says ERROR
→ JOEDESIGN chooses an error expression

Product does not define WARNING
→ JOEDESIGN may not invent a warning state to create visual variety
```

Success, warning, error, information, selection, focus, active, and disabled treatments must remain semantically distinguishable where the product requires them.

Do not use color as the only cue for a required state or action when another visual cue is needed for comprehension. Pair color with text, iconography, shape, position, underline, border, or other appropriate indication.

Do not repurpose a semantic state color for unrelated decoration when doing so would weaken or confuse its meaning.

---

## 8. Accessibility is a gate, not an aesthetic preset

For web work, use WCAG 2.2 AA contrast requirements where applicable as the minimum accessibility gate:

- normal text: at least `4.5:1` against its background;
- large-scale text: at least `3:1` against its background;
- meaningful UI component/state visuals and required graphical objects: at least `3:1` against adjacent colors.

Color must not be the sole means of conveying information where another cue is required.

These numbers are minimum conformance thresholds, not a complete color-design system and not a requirement that every visual relationship use maximum contrast.

Applicable platform, project, or organizational requirements may be stricter and take precedence.

Inactive/decorative exceptions in accessibility standards are not permission to make useful information unreadable.

---

## 9. Contextual contrast

A color role is only valid in context.

Inspect the actual foreground/background pair, including:

- light and dark surfaces;
- nested layers;
- imagery or gradients behind text;
- hover/focus/selected states;
- disabled/inactive states when they still carry useful information;
- desktop/mobile recomposition when the background relationship changes.

A token that passes on one background may fail on another. Do not treat token existence as proof of contrast.

Thin strokes, icons, and low-opacity elements may appear weaker in actual rendering than their source value suggests; observe the produced target where the distinction is material.

---

## 10. Responsive and theme translation

Preserve semantic color roles and relative priority, not exact desktop color placement.

Responsive recomposition may change which object owns the accent or which surface sits behind content if the visual structure changes. The resulting mobile hierarchy must still communicate the same Product priority and states.

Across light/dark or project themes:

```text
role stays stable
→ value may change
```

Do not duplicate arbitrary per-breakpoint colors when a stable semantic role can express the same intent.

---

## 11. Expressive color and gradients

Expressive color, gradients, glow, translucent color, and unusual combinations are allowed when they serve the approved visual direction.

They still must preserve:

- Product priority;
- readable foreground relationships;
- state clarity;
- focal ownership;
- target-medium legibility.

Do not prohibit expressive color merely because a neutral token system would be easier to manage. Conversely, do not add gradients or high-chroma effects merely to make a generic composition feel distinctive.

---

## 12. Project DESIGN.md persistence

Persist only durable, project-specific color decisions that are sourced or approved.

Useful durable information may include:

- semantic color roles;
- palette or token mappings;
- accent ownership rules;
- surface/layer relationships;
- state color semantics;
- light/dark/theme behavior;
- meaningful contrast or accessibility constraints;
- approved exceptions.

JOEDESIGN draft defaults or exploratory colors do not automatically become project authority.

---

## 13. Review sequence

For a material Color / Contrast review:

```text
1. Product priority and semantic states
2. APPROVED project color authority
3. Major color-role map
4. Focal / accent owner
5. Foreground/background contrast hierarchy
6. Surface/layer relationships
7. State and interaction color meaning
8. Applicable accessibility gate
9. Responsive/theme/background translation
10. Actual rendered observation
```

Report material exceptions rather than hiding them in local values.

---

## 14. Anti-overexpansion guardrails

Color / Contrast Core v0.1 does not include:

- a universal JOEDESIGN brand palette;
- a large named-color database;
- automatic palette generation;
- automatic dark-mode generation;
- color-trend lookup;
- vendor theme engines;
- APCA-as-required-runtime policy;
- a standalone accessibility scanner;
- a new public color skill;
- a requirement that every project use the same token names.

Add these only if competition or real project evidence demonstrates a need.

---

## 15. Anti-patterns

Challenge these behaviors:

- choosing hex values before understanding color roles;
- using accent color on every element that should feel important;
- making every section equally saturated or contrast-heavy;
- relying on hue alone for required meaning;
- using semantic error/success colors as unrelated decoration;
- creating cards or tinted panels without a containment/layer reason;
- keeping a token because it exists even when it fails on the actual background;
- assuming desktop contrast remains valid after mobile recomposition;
- forcing every project into a neutral SaaS palette;
- replacing an approved expressive palette with a generic accessible-looking theme instead of fixing the exact failing relationship;
- treating WCAG minimum ratios as a complete aesthetic system;
- adding color-system machinery that the project does not need.

---

## 16. Canonical doctrine

> **JOEDESIGN assigns color by semantic role before value. Color reinforces Product priority through intentional contrast hierarchy, clear accent ownership, coherent surface relationships, and state semantics without becoming the sole carrier of required meaning. Project-approved palettes remain authoritative; light/dark and responsive variants preserve roles rather than exact values. Accessibility minimums are hard gates where applicable, not an aesthetic preset. Material color claims are verified against the actual rendered foreground/background context, while palette databases, automatic theme engines, and other color sub-platforms remain outside v0.1 until demonstrated need exists.**
