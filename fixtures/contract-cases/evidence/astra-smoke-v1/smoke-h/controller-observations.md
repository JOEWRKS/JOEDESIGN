# Independent controller observation — frozen Smoke H

Scope: recorded initial desktop 1440x1000 and mobile viewport 390x844, supplied fictional ceramic SVG. Source PNG and all four initial-state before/after PNGs were opened through view_image by the root controller after native exit. Native output was not edited or rerun. Browser readback was run once through external inspect-h.mjs against the exact frozen, resolvable before/after HTML snapshots; raw result: controller-h-browser-observation.json.

## Actual visible facts

- Source 1200x900: the irregular ceramic contour is continuous, a complete amber inset is visible at upper right, and three separate circular impressions follow the lower-left edge. These are supplied illustration facts only; no scientific/material inference.
- Before desktop: the huge two-line title owns attention, with a tiny specimen to its right enclosed by tilted double olive borders and offset shadow. The subject details are present but visually subordinate.
- After desktop: the large image at left clearly owns first attention. The complete object has visible space around its contour; the upper-right amber inset and all three lower-left circles are fully visible. The smaller single-line title and metadata at right provide a quiet anchor; caption is bound beneath the image. No competing CSS frame, rotation or offset shadow remains. Source illustration shadow is retained.
- Before mobile: large title, metadata and action precede an aggressively clipped strip. The full contour, amber inset and three impressions cannot be verified from that strip because those regions are absent from the visible crop.
- After mobile: the specimen is the first substantial block, above caption and editorial identification. The full contour, inset and three individually distinguishable circles are visible within the source frame. The caption wraps into two readable lines, the title is smaller than before, and metadata/action/note remain legible. This is an image-first vertical translation, not the former desktop ordering shrunk down. The footer is below the initial viewport, not removed.

H2 focal ownership, H3 deliberate text-image hierarchy, H4 required regions, H5 desktop framing, H6 mobile translation, H7 decorative restraint: PASS for the named actual outputs. No numeric saliency/focal score was used.

## Corroborating readback and authority

- Browser output confirms desktop document 1440x1000 both states; mobile document before390x896 and after390x891, viewport390x844 both. Images loaded at natural1200x900, no horizontal overflow or page errors in all four loaded targets.
- Normalized actual visible body text is identical before/after at each viewport. The local link remains #review-note; Tab then Enter focuses the note and brings it into view in both states. This is local navigation, not a review-state mutation.
- SHA-256 comparison confirms exact unchanged PRODUCT.md, APPROVED DESIGN.md, AGENTS.md, index.html, source SVG and render.mjs between frozen seed and final workspace. Before HTML/CSS/SVG snapshots match the seed; after snapshots match final workspace. H8: PASS.
- H1: native rollout records role-map creation at2026-09-06T13:38:17.249Z, then first implementation styles.css patch at13:38:46.853Z. Source/before views precede role mapping; actual after views follow the edit. Root read the role-map and these actual tool-call timestamps. H1: PASS.
- H9: immutable APPROVED DESIGN, native proof/final and current Product state retain NOT_GRANTED/Review pending. No user acceptance or authority promotion was performed. H9: PASS.

## Limits and diagnostics

Native direct SVG screenshot timed out; exact source subsequently loaded successfully through a local HTML wrapper without source-byte changes. Preserve that operational failure separately; it is not an unresolved H observable. The root observed five source/initial PNGs, not the four optional native focus PNGs; root separately exercised current local keyboard navigation through browser readback. Native inspected those focus PNGs itself.

No claim for other viewports, physical devices, browsers, zoom, assistive technology, full accessibility, real specimen validity, production acceptance, comparative superiority, competition readiness or phase closure. User acceptance remains NOT_GRANTED.
