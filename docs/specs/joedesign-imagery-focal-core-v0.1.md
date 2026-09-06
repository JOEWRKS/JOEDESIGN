# JOEDESIGN Imagery / Focal Ownership Core v0.1

**Status:** CANONICAL CRAFT DOCTRINE — IMPLEMENTATION BASELINE  
**Product:** JOEDESIGN  
**Scope:** imagery role, focal ownership, text-image dominance, crop/framing, scale/negative space, responsive translation, and rendered verification  
**Dependency policy:** no image database, stock-search runtime, image model dependency, asset crawler, or new public entrypoint

---

## 1. Purpose

JOEDESIGN should not treat imagery as a decorative slot to fill after layout is finished.

The imagery objective is:

> **Role before asset treatment. Decide what the image is doing, who owns attention, and what must remain visible before choosing scale, crop, framing, placement, or effects.**

Imagery is part of hierarchy. It can lead, support, explain, or stay quiet, but its role must be intentional and consistent with Product Truth and the approved project direction.

---

## 2. Authority order

Imagery follows the same authority order as the rest of JOEDESIGN:

```text
Product Truth
        ↓
APPROVED Project DESIGN.md
        ↓
JOEDESIGN Craft Core
        ↓
Selected project references
        ↓
JOE Default Taste
```

A visually striking asset cannot override required product content, approved hierarchy, user acceptance, or a meaningful image's semantic role.

---

## 3. Role before treatment

Before materially changing an image, classify its role in the target surface.

Use the smallest useful role vocabulary:

- **FOCAL** — owns or materially drives first visual attention;
- **SUPPORT** — reinforces the primary content or atmosphere without owning first attention;
- **DECORATIVE** — contributes texture or mood but carries no required product meaning.

Informative/evidence imagery is Product content first. It may also be visually focal or supporting, but JOEDESIGN may not crop, hide, blur, recolor, or demote required information merely to improve art direction.

Do not infer role from DOM position, asset size, filename, or the fact that an image happens to be present in a hero.

---

## 4. Focal ownership

Every material viewport or major visual region should have an intentional attention owner or an intentional sequence of owners.

Ask:

1. What should the user notice first?
2. Is imagery supposed to own that first impression?
3. If not, what role does imagery play relative to the primary text/action/content?
4. What should become second and third in the visual flow?

Avoid accidental co-dominance where title, artwork, CTA, badges, and decorative imagery all compete at the same loudness.

Multiple strong focal objects are valid when the approved concept requires a sequence, comparison, collage, editorial field, or other deliberate structure. Do not force a universal single-focal aesthetic.

---

## 5. Text ↔ image dominance

Choose the relationship intentionally rather than defaulting to a generic split hero.

Common relationships include:

```text
image-led
text-led
balanced tension
sequential reveal
supporting atmospheric field
```

The relationship is expressed through scale, placement, crop, whitespace, contrast, overlap, density, and surrounding type hierarchy.

Do not make text and image equally loud merely because both are important. Product importance and visual loudness are related but not identical; establish a readable order.

Do not automatically place text left and image right, place every image in a card, or convert artwork into a background simply because those patterns are convenient.

Composition-specific anti-template rules belong to the later Composition Core; this doctrine only rejects imagery patterns when they destroy the intended image role or focal relationship.

---

## 6. Crop, focal point, and framing

A crop is a design decision, not a neutral resize.

For material imagery, know enough to identify:

- the important subject or focal region;
- required semantic content that must remain visible;
- whether negative space is intentional and useful;
- whether the crop should feel tight, contextual, immersive, or quiet;
- whether the frame itself is part of the approved visual language.

Prefer explicit focal intent over blind `center center` cropping.

Do not crop required evidence, labels, product details, faces, or meaningful context merely to fit a component shape. If the source cannot support the needed crop, surface the constraint rather than inventing missing pixels or pretending the result is faithful.

Generated expansion or image editing may be used when authorized, but generated content is not recovered source truth and still requires target-medium proof.

---

## 7. Scale and negative space

Image scale communicates priority.

A focal image may legitimately consume a large part of the viewport. A supporting image may need to stay subordinate even if the source asset is visually dramatic.

Use negative space around imagery to control ownership and transition, not as arbitrary empty margin.

Challenge:

- oversized decorative artwork that steals Product priority;
- tiny signature imagery that cannot perform its intended focal role;
- repeated same-size images that flatten hierarchy;
- full-bleed treatment with no art-direction reason;
- dense surrounding UI that suffocates an intended focal image.

Do not enforce a fixed image ratio, max width, or percentage. The approved project direction and actual target decide the relationship.

---

## 8. Reference imagery

Reference imagery is relationship evidence, not an asset source by default.

Extract relationships such as:

- subject-to-viewport scale;
- crop tightness;
- artwork-to-copy dominance;
- image sequencing;
- edge treatment;
- negative-space strategy;
- transition from image-led to information-led content.

Do not copy proprietary assets, brand-specific visual identity, source-specific product imagery, or unsupported crop behavior just because a reference is attractive.

Unknown source imagery behavior remains unknown under the Reference Intelligence contract.

---

## 9. Responsive focal translation

Responsive imagery preserves role and focal intent, not desktop coordinates or aspect ratio.

On smaller viewports JOEDESIGN may:

- recrop around the important subject;
- change `object-position` or equivalent focal placement;
- change image height/aspect relationship;
- move imagery before or after text when Product meaning permits;
- reduce or increase image dominance to preserve the intended hierarchy;
- remove purely decorative imagery when it no longer contributes and authority permits.

Do not simply scale the desktop frame down.

Required informative/evidence imagery and required content remain governed by Product Truth.

---

## 10. Image treatment restraint

Effects such as blur, gradient masks, color overlays, duotone, border treatment, shadows, clipping, and blend modes are tools, not quality signals.

Use them only when they support the approved image role, legibility, focal relationship, or visual world.

Do not apply generic dark overlays to every hero image, decorative gradients to compensate for weak composition, or rounded-card framing to every asset by default.

Color treatment remains subject to Color / Contrast Core and actual foreground/background verification.

---

## 11. Actual-output verification

Image intent is not proven by CSS, asset dimensions, or a mockup existing on disk.

For a material image claim, inspect the actual target render and record enough of:

```text
role
focal owner
important subject / focal region
text ↔ image dominance
crop / framing
scale / negative space
responsive translation
observed result
```

Use:

```text
expected observable
→ actual observed fact
→ PASS / FAIL / UNVERIFIED
```

For web work, inspect the named desktop/mobile viewport. When the image contains meaningful content, verify that the required region remains visible and legible.

`Asset present ≠ Crop correct ≠ Focal ownership correct ≠ Visual PASS ≠ User Acceptance`.

---

## 12. Project DESIGN.md persistence

Persist only durable approved imagery relationships, not every local crop experiment.

A compact project record may include:

```text
Imagery role
Focal owner
Text-image relationship
Important focal/crop rule
Responsive translation
Approved evidence
```

Do not create a second imagery authority file.

---

## 13. Anti-overexpansion guardrails

Imagery / Focal Ownership Core v0.1 stops at design judgment and verification.

Not included:

- stock-photo search engine;
- image asset database;
- cross-project asset library;
- automatic image-generation router;
- image model dependency;
- computer-vision scoring system;
- saliency heatmap subsystem;
- asset crawler;
- DAM integration;
- automatic background removal pipeline;
- separate imagery public skill.

Use existing general tools only when the task actually requires them.

---

## 14. Anti-patterns

Challenge these behaviors:

- filling an empty layout slot with any available image;
- defaulting every hero to text-left / image-right;
- treating all imagery as decorative background;
- making every image equally large or equally loud;
- centering every crop without checking the subject;
- using mobile as a scaled desktop crop;
- letting an attractive image erase required Product information;
- hiding poor text-image hierarchy behind gradients or overlays;
- copying reference assets instead of translating the relationship;
- declaring image success without inspecting the actual render.

---

## 15. Review sequence

For material imagery work:

```text
1. Product / approved project authority
2. Image role
3. Intended focal owner / visual sequence
4. Important subject or required image content
5. Text ↔ image dominance
6. Scale / negative space
7. Crop / framing
8. Responsive focal translation
9. Actual target render
10. PASS / FAIL / UNVERIFIED
11. User approval if material
12. Persist only approved durable relationships
```

---

## 16. Canonical doctrine

> **JOEDESIGN treats imagery as hierarchy, not decoration by default. Role comes before asset treatment; focal ownership and text-image dominance are intentional; crops preserve important content and approved meaning; scale and negative space express priority; responsive work recompose focal intent rather than shrinking desktop coordinates. References contribute relationships, not copied assets. Actual target renders are required for material crop and focal claims, and no imagery decision grants user acceptance or overrides Product Truth.**
