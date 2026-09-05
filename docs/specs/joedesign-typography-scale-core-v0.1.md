# JOEDESIGN Typography & Scale Core v0.1

**Status:** CANONICAL CRAFT DOCTRINE — PRE-IMPLEMENTATION BASELINE  
**Product:** JOEDESIGN  
**Scope:** native typography, type-role, readable measure, focal-scale, and proportional hierarchy doctrine  
**Dependency policy:** no competitor runtime/vendor dependency

---

# 1. Purpose

Typography is structural information, not decoration added after layout. Scale is a relationship between levels of importance, not a collection of independent font sizes or component dimensions.

JOEDESIGN must use typography and scale to make Product Truth legible at a glance and readable over time.

The primary doctrine is:

> **Role before value. Contrast must communicate hierarchy. Use the fewest typographic and scale roles that make importance, grouping, reading flow, and interaction priority unmistakable.**

Before polishing typography, JOEDESIGN should be able to answer:

1. What textual role does each repeated style perform?
2. Which role is the primary entry point and which roles support it?
3. Can adjacent hierarchy levels be distinguished without reading the words?
4. Does the type scale reinforce the existing Visual Block Tree and visual flow?
5. Is body text comfortable at the actual width, language, viewport, and typeface?
6. Are repeated roles visually identical across sections and states?
7. Does any local size, weight, tracking, or line-height exist without a reusable semantic reason?

A page with many attractive text styles but no stable role system is not a successful JOEDESIGN result.

---

# 2. Authority layers

Typography authority follows the existing JOEDESIGN hierarchy:

```text
Product Definition / approved Product Truth
        ↓
Project APPROVED DESIGN.md
        ↓
JOEDESIGN Craft Invariants
        ↓
JOE Default Typography / Scale Profile
```

- Product Definition owns content meaning, semantic heading structure where product/accessibility requires it, and required information.
- Project `DESIGN.md` owns approved families, typographic voice, scale, density, and project-specific visual roles.
- Craft invariants define how JOEDESIGN evaluates hierarchy, readability, role consistency, and proportional coherence.
- JOE defaults provide a strong starting point only when project authority has not approved a different system.

Typography must never change product meaning merely to make a composition cleaner.

---

# 3. Role before value

JOEDESIGN should first identify the roles the surface actually needs, then assign visual values.

Possible role families include:

- display / hero statement;
- page title;
- section heading;
- subsection heading;
- body / reading text;
- label / control text;
- metadata / supporting text;
- metric / emphasized data;
- code / technical text.

These are examples, not a mandatory list. Do not create every role by default.

A role must exist because a recurring semantic job exists.

Prefer:

```text
semantic job
→ reusable type role
→ canonical token/style
```

over:

```text
individual element
→ local font-size / weight guess
```

If two roles perform the same semantic job, merge them unless an observed visual distinction is necessary.

---

# 4. Hierarchy is multi-axis

Font size alone is not hierarchy.

JOEDESIGN may coordinate:

- font size;
- weight;
- line height;
- width / measure;
- placement;
- whitespace around the role;
- tone / text color;
- case and tracking;
- family or style when project authority supports it.

The hierarchy should remain understandable even when one axis becomes less available, such as smaller responsive viewports or a fallback font.

Avoid adjacent roles that differ only by a nearly imperceptible numeric change.

Example anti-pattern:

```text
Heading A: 16px / 600
Heading B: 17px / 600
Heading C: 18px / 600
```

If a role distinction cannot be perceived reliably, either strengthen the relationship through multiple axes or collapse the unnecessary role.

---

# 5. Restrained type scale

JOEDESIGN uses a deliberately small type-size vocabulary to reduce arbitrary choices while preserving strong hierarchy.

Typography is **not** governed by the spatial 4px grid. Type size must respond to the actual face, x-height, language, rendering environment, and role.

JOE default starting size set:

```text
12, 14, 16, 20, 24, 32, 40, 48, 64
```

Use only the subset the project needs.

Additional sizes such as larger editorial/display roles may be introduced when a recurring project role proves the need. Do not add a new size because one isolated screenshot appears improved.

The goal is not to force every project into these numbers. The goal is a restrained, role-based scale with visible contrast and repeated proportions.

## 5.1 Default role tendencies

When project authority does not provide a type system, the following are reasonable starting tendencies, not automatic approved truth:

| Role tendency | Typical starting size | Notes |
|---|---:|---|
| Metadata / fine supporting | `12px` | Use sparingly; never as a substitute for hierarchy |
| Compact label / secondary UI | `14px` | Short text and controls, not long-form reading by default |
| Body / primary reading | `16px` | Default web reading anchor |
| Large body / lead | `20px` | Editorial lead or high-emphasis explanatory copy |
| Small heading | `24px` | Local section/subsection depending density |
| Medium heading | `32px` | Strong section/page hierarchy |
| Large heading | `40px` | Major page emphasis |
| Display | `48–64px` | Use only when the surface needs genuine display dominance |

Do not infer HTML heading tags from these visual roles or vice versa.

---

# 6. Weight and family restraint

Use the fewest families and weights that clearly support the approved visual world.

Default preference:

- one primary family can carry most product UI;
- a secondary display or mono family requires a clear role;
- use regular/medium/bold or the smallest visually distinct supported weight set;
- do not synthesize unsupported font weights;
- avoid using bold everywhere to manufacture hierarchy;
- avoid ultra-light body text when it weakens readability or rendering consistency.

A new family is a material identity decision when it materially changes the visual voice. Treat it accordingly rather than as a local polish tweak.

---

# 7. Line height, tracking, and optical fit

Typography values must be tuned to the actual face and role.

Reasonable starting ranges:

- body / reading text: approximately `1.45–1.6` line-height;
- headings / display: approximately `1.05–1.3` line-height.

These are starting ranges, not fixed rules.

JOEDESIGN must inspect:

- x-height and apparent size;
- ascenders/descenders and clipping risk;
- line wrapping;
- paragraph texture;
- heading block height;
- tracking at actual size;
- fallback-font behavior when material.

Body tracking should normally respect the typeface default unless evidence supports adjustment. Large display type may need optical tightening. Uppercase labels may need additional tracking. Do not create arbitrary letter-spacing for every role.

Mathematical consistency does not override optical legibility.

---

# 8. Reading measure is part of typography

Typography cannot be evaluated independently from width.

For long-form English reading, approximately 60–80 characters per line is a useful reference range, not a universal law.

Do not mechanically apply Latin character-count guidance to Korean, CJK, code, tables, dashboards, or narrow mobile UI. For those contexts, inspect the actual language, line breaks, density, and reading rhythm.

A type role that is readable at one width may fail at another.

JOEDESIGN should treat measure, type size, and line height as one reading system.

Avoid:

- unnecessarily wide paragraphs;
- narrow columns that create constant wrapping;
- centered long-form paragraphs;
- body text that becomes visually secondary because it is too small or too low contrast.

---

# 9. Scale and focal proportion

Scale communicates priority beyond typography.

JOEDESIGN should coordinate the relative scale of:

- primary text block;
- artwork / image focal object;
- primary action;
- metrics / data callouts;
- repeated cards or content objects;
- supporting labels and metadata.

Product priority must determine visual weight. A decorative object must not dominate a more important product decision without an intentional art-direction reason.

Repeated objects with the same semantic role should reuse the same size role unless content requires a documented variation.

Do not make every section visually equal in scale. A deliberate visual flow requires moments of dominance, support, pause, and transition.

---

# 10. Decisive contrast, not role inflation

JOEDESIGN should prefer a small number of clearly distinct roles over many barely different ones.

When comparing adjacent roles, ask:

- Is the hierarchy visible at a glance?
- Is the difference doing a real job?
- Does the same role repeat consistently elsewhere?
- Could this be achieved by spacing, position, tone, or weight instead of inventing another size?

A new role is justified only when an existing role cannot represent a recurring semantic need without harming hierarchy or readability.

---

# 11. Responsive typography translates hierarchy

Responsive design must preserve role importance and reading comfort, not proportionally shrink desktop typography.

On narrower viewports:

- preserve semantic role mapping;
- preserve relative dominance;
- adjust measure and wrapping;
- change display scale when needed;
- keep body text comfortably readable;
- avoid multiplying one-off breakpoint sizes;
- re-render and inspect actual line breaks and hierarchy.

Fluid typography (`clamp()` or equivalent) is optional, not inherently superior. Use it only when it creates a coherent repeated role across the intended viewport range.

Do not turn every type role into an independent fluid formula.

---

# 12. Semantic structure and visual role are related but not identical

HTML heading order, accessibility semantics, and product information structure must remain correct.

JOEDESIGN may visually style roles differently when the approved visual hierarchy requires it, but must not change semantic structure for visual convenience.

Do not infer visual importance solely from `h1`/`h2`/`h3` tags, component names, DOM depth, or Figma layer names.

Visual role follows Product Truth and the semantic Visual Block Tree.

---

# 13. Typography anti-patterns

JOEDESIGN should actively challenge:

- a unique font size for every element;
- adjacent roles separated by only 1–2px with no other meaningful contrast;
- too many font families or weights without distinct jobs;
- making every heading bold and every secondary label tiny;
- giant display type used because it looks fashionable rather than because it owns the primary focal role;
- long-form body text below a comfortable reading size without density or platform justification;
- excessively wide reading measure;
- arbitrary line-height or tracking per component;
- all-caps long-form text;
- ultra-light body text with weak legibility;
- visually styling semantic headings by DOM depth alone;
- forcing all type sizes to the spatial 4px grid;
- halving desktop font sizes for mobile;
- adding independent breakpoint sizes for every element;
- accepting clipping, orphaned words, or broken line rhythm as a necessary side effect of a chosen scale;
- relying on font size alone while spacing, position, and tone contradict the intended hierarchy.

---

# 14. Typography review sequence

Review typography in this order:

```text
1. Product priority
2. Visual role map
3. Role count / duplication
4. Hierarchy contrast
5. Type family / weight authority
6. Type scale consistency
7. Reading measure
8. Line height / paragraph rhythm
9. Tracking / optical fit
10. Focal scale relationships
11. Responsive translation
12. Actual rendered evidence
```

Do not begin with decorative font selection before the role hierarchy works.

---

# 15. Minimum evidence for typography conformance

For a material proof, JOEDESIGN should be able to identify:

- the major type roles in use;
- which role owns the visual entry point;
- whether equivalent semantic roles reuse equivalent type tokens;
- whether adjacent roles are visibly distinct;
- the body/reading measure at material viewports;
- any deliberate type-size, weight, family, line-height, or tracking exception;
- actual rendered observations at the named viewport/state.

Code values alone do not prove typographic hierarchy.

---

# 16. Research basis, non-authoritative

This doctrine was checked against current public design-system practice before implementation.

- Atlassian uses role-based typography tokens and coordinates font size, weight, line-height, spacing, and color for hierarchy; its current scale is deliberately limited rather than arbitrary.
- Carbon uses calibrated type tokens and selects them according to layout architecture and productive/expressive context rather than assigning independent sizes per element.
- Current AI design-skill practice also emphasizes role scales, hierarchy through multiple axes, readable measure, and actual rendered inspection; those products are comparison evidence only and are not runtime dependencies or normative authority for JOEDESIGN.

JOEDESIGN keeps its own doctrine and will revise it only from observed project/competition evidence.

---

# 17. Canonical doctrine

> **JOEDESIGN treats typography as structural information and scale as a hierarchy relationship. It defines semantic roles before numeric values, uses the fewest roles necessary, and makes adjacent hierarchy levels decisively different through coordinated size, weight, spacing, placement, tone, measure, and optical fit. Repeated semantic roles reuse repeated type roles. Typography does not inherit the spatial 4px grid; it uses a restrained role-based scale tuned to the actual typeface, language, viewport, and reading task. Responsive typography preserves hierarchy and readability rather than shrinking desktop values mechanically. Product meaning and semantic structure remain authoritative, and actual rendered evidence—not token existence alone—determines typographic conformance.**
