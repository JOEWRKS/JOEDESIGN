# Pre-edit imagery-role map

Written after opening the actual source PNG and both before PNGs, before the first styles.css edit. Authority: PRODUCT.md and APPROVED DESIGN.md Rev 1; this map is evidence for a bounded correction, not a new authority.

| Item / role | Focal owner | Important subject / region | Text-image relationship | Observed crop / focal issue | Responsive expectation |
| --- | --- | --- | --- | --- | --- |
| assets/specimen-s17.svg — FOCAL, informative | Complete specimen; amber inset is a detail within that owner | Source 1200x900; required contour approximately x230..1000/y140..800, amber x802..926/y203..319, three impressions together x315..502/y591..699 (Product coordinates) | Image leads; title/caption/metadata quietly identify it; action follows identification | Desktop: complete required regions remain visible but specimen is a tiny illustration beside a 112px title. Mobile: a magnified central/left fragment; upper-right inset, all three impressions and most contour are absent. Source PNG visibly contains all these regions. | Desktop: enlarge specimen, lead with it, preserve negative space and every required region. Mobile: image precedes editorial block; natural proportions show the entire source canvas, with all three impressions distinct. No clipping or horizontal overflow. |
| Existing CSS double border, offset shadow and rotation — DECORATIVE | No independent focal ownership authorized | No Product information; distinct from the shadow drawn inside the immutable SVG | Frame currently surrounds and rotates both image and caption | Heavy green double lines, shadow and tilt compete with the small desktop subject and box in the mobile fragment | Remove these CSS treatments on both viewports; retain the source illustration and its own shadow unchanged. |

Source inspection: artifacts/source-specimen.png, 1200x900. The illustrated contour is continuous, the amber inset sits at upper right, and three separate circular impressions descend along the lower-left region. Empty source margins surround the specimen. No scientific/material conclusions inferred.

Before observations: artifacts/before-desktop.png, viewport/full page 1440x1000; artifacts/before-mobile.png, viewport 390x844, full page 390x896. Both were opened, not merely generated. Mobile footer lies below the initial viewport.

Semantic visual block tree: page → archive header / study / review note / footer; study → specimen with tightly associated caption / editorial identification; identification → record + title / type + status / review action. Intended flow: specimen → identifying text and caption → action → note. Existing major-group gap and caption binding can remain; title size, grid allocation/order, image sizing and decorative frame are the defect's scope.

Planned smallest correction: reverse the study's image/text emphasis with a wider first image column; lower the title scale; let the image retain intrinsic proportions; remove frame border/padding/rotation/shadow and the mobile crop overrides. Keep existing content, families, colors, remaining spacing, focus rules and local anchor behavior.
