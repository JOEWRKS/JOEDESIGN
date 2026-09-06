# Specimen S-17 imagery correction proof

Authority: immutable PRODUCT.md and APPROVED DESIGN.md Rev 1. Scope: imagery/focal correction in styles.css only; source assets, HTML, content, action and authority remain byte-identical. User acceptance: NOT_GRANTED.

## Pre-render intent

Surface: fictional Specimen Review Page, initial state. Required browser viewports: desktop 1440x1000 and mobile 390x844, device scale 1. Full-page PNG dimensions will be recorded separately. Source inspection: supplied SVG rendered at its native 1200x900 canvas.

Criteria established before rendering/editing:
- The specimen owns first attention; title/caption/metadata are readable secondary anchors, followed by the review action.
- The complete contour, upper-right amber inset and all three lower-left impressions remain visible and unaltered.
- Desktop provides deliberate image scale and negative space; mobile retains image priority and required regions without horizontal overflow.
- Decorative border, rotation or shadow must not compete with the specimen.
- All required text remains visible; the local review-note action remains reachable with visible keyboard focus; immutable input bytes match the preserved originals.

## Before-edit observations

Opened artifacts/source-specimen.png (1200x900), artifacts/before-desktop.png (viewport/full page 1440x1000), and artifacts/before-mobile.png (viewport 390x844; full page 390x896). Source shows a continuous contour, amber inset at upper right and three distinct lower-left impressions. Desktop title dominates the tiny specimen, with a heavy double border, tilt and offset shadow competing with the image. Mobile shows only a magnified central/left fragment: inset, impressions and complete contour are missing. Text and the required action precede the image. Neither before page has horizontal overflow.

The helper timed out when screenshotting the SVG document directly. The same unchanged SVG was then rendered successfully through artifacts/source-view.html at native size using the existing render.mjs helper; the wrapper references the exact preserved local SVG. No source-asset edit or replacement was used.

The complete before implementation is preserved in artifacts/before/ with resolvable styles.css and assets/specimen-s17.svg. Baseline SHA-256 values are in artifacts/before-inputs.json. The pre-edit imagery-role map is artifacts/imagery-role-map.md.

## Correction and observed verdicts

Only styles.css changed in the implementation. The image now occupies the first, wider desktop column and precedes editorial content on mobile. The title is 40px desktop / 32px mobile instead of 112px / 64px. Intrinsic image proportions replace fixed-height cover crops and the mobile 200% width. CSS border, padding, rotation and offset shadow were removed from the figure. Existing typography families, colors, other spacing, content and focus rules remain. Exact patch: [styles.diff](styles.diff). No direction revision or acceptance is implied by the chosen column proportions.

Opened and inspected both after initial-state PNGs and all four action/note-focus PNGs listed below. After desktop image rectangle: x72/y116.5, 832x624. After mobile: x24/y97.5, 342x256.5. Both display the complete 1200x900 source canvas in its native proportions. Measurements supplement the visual observations; they are not substitutes for opening the images.

| Claim / expected observable | Before observation / verdict | After observation / verdict |
| --- | --- | --- |
| Focal ownership: specimen leads | **FAIL** — desktop oversized two-line title dominates the tiny framed object; mobile starts with title and action. | **PASS** — desktop large specimen at left commands attention beside a quiet single-line title; mobile's first major block is the complete specimen. Amber remains a detail within the specimen. |
| Hierarchy: image, identification, action | **FAIL** — text and decorative framing overpower imagery. | **PASS** — caption is bound beneath the image; title is clearly stronger than 14px metadata but secondary to the specimen. Underlined 16px action follows metadata. Mobile caption is two readable lines, then record/title/metadata/action. |
| Subject/crop: complete contour, inset, three impressions | Desktop **PASS**, mobile **FAIL** — desktop retains regions at small scale; mobile hides inset, all impressions and most contour. | **PASS** both — continuous outer contour with clear surrounding margins, complete amber inset at upper right, three separate lower-left circles. No visible truncation, distortion, blur, recoloring or replacement; source shadow is retained. |
| Desktop framing: deliberate scale/negative space | **FAIL** — a small tilted picture sits at the edge of a much larger text block. | **PASS** — 832x624 image balances a 416px editorial column across the existing 48px gap. Required regions are comfortably inside the image edges; caption, action, note and footer fit the 1000px viewport. |
| Mobile framing: image priority, all content reachable | **FAIL** — shallow magnified fragment follows the action. | **PASS** — 342x256.5 image fits the 24px page margins, before text; complete source is visible. Action and note are readable within the initial 844px viewport. Footer is below it and scroll-reachable in the 891px full page. No horizontal overflow. |
| Decorative restraint: framing stays subordinate | **FAIL** — double olive border, tilted caption and offset shadow compete. | **PASS** — no CSS frame border, rotation or shadow; aligned caption and neutral source background leave the specimen dominant. Source illustration's own shadow is unchanged. |
| Invariants: bytes, facts, action and focus preserved | Baseline input copies/hash checks **PASS**; before keyboard interaction **UNVERIFIED** (not exercised). | **PASS** — immutable inputs match baseline bytes; visible text matches before at both viewports. Tab visibly outlines Open review note, then Enter sets #review-note, focuses the note and brings it into view. Status remains Review pending; no outcome is recorded. |

## Evidence paths, dimensions and hashes

All paths below are relative to `D:/JOEWRKS/joedesign-imagery-focal-validation-20260906/runs/H/workspace/`. Each PNG was opened during this run. SHA-256 hashes bind the exact observed output. [evidence-manifest.json](evidence-manifest.json) also records absolute paths, byte sizes, and hashes for all artifacts, snapshots and current inputs.

| Actual output path | Browser viewport | Full-page PNG | SHA-256 |
| --- | --- | --- | --- |
| artifacts/source-specimen.png | 1200x900 | 1200x900 | 3b5d4c6cfb8e99ed249f2e2ea63da360a454a6708d90c0e360fa2a199d6213ff |
| artifacts/before-desktop.png | 1440x1000 | 1440x1000 | 2fc7efec9ae0240b4b6c9a4b2ec242e7049459b4cb4f8538cad41ddf97b95ac5 |
| artifacts/before-mobile.png | 390x844 | 390x896 | 54619ace6e4c8d86edd911ba8321a1c605f65d482816d4d2222876ec5599b086 |
| artifacts/after-desktop.png | 1440x1000 | 1440x1000 | 56789c49bcbb00b86ddc963b1865b2ba03ad74ae01a1195a37e06d55f6941f81 |
| artifacts/after-mobile.png | 390x844 | 390x891 | 91f5a77689a25314afa8f190eda7e76c889fa9687b1877eb41a15ccc2a6593d3 |
| artifacts/after-desktop-action-focus.png | 1440x1000 | 1440x1000 | c04d30f39766afe6172e8f9674796566d757dd88bd20152de0a8136017605dfd |
| artifacts/after-desktop-note-focus.png | 1440x1000 | 1440x1000 | b00ac35b3b5686c43ac48d6eab911d4776baff209260911abd5bd2a3c81d010b |
| artifacts/after-mobile-action-focus.png | 390x844 | 390x891 | 2c5e8927f5b65bc0c025916af28c25122ab9a72d4ae8b939169a262cd4758f4a |
| artifacts/after-mobile-note-focus.png | 390x844 | 390x891 | 9e0bf629a4559edf49f581ac84bc5d1440dcf75171d58eee4915bd8c996b7e38 |

Source/before/after initial PNGs use the existing `node render.mjs <input> <output> <width> <height>` helper. Before input: artifacts/before/index.html; after input: index.html; source input: artifacts/source-view.html. Interaction evidence uses [verify.mjs](verify.mjs) with the same already-installed Playwright and Chrome. All captures use device scale 1 and fullPage:true. No tools/dependencies were installed; no external imagery, references or network resources were used.

## Invariant evidence and limits

[verification.json](verification.json) records exact before/after text, image loading, page geometry, local resource requests, keyboard focus/anchor behavior, baseline hashes and snapshot matches. All ten bounded technical checks pass. Both snapshots contain exact local HTML/CSS/SVG inputs with working relative references. Before PNG and pre-edit map hashes remain recorded in [pre-edit-evidence-hashes.json](pre-edit-evidence-hashes.json).

| File | SHA-256 (same before/after unless stated) |
| --- | --- |
| index.html | 00bd324772a8cde52f613c97ce1dba71187dfc64f9bc250a64e3a4968d9c9120 |
| assets/specimen-s17.svg | 7cd4487dd9198034c853e06b29755a34f32aa3fbca2dddf042adb694b7575a12 |
| PRODUCT.md | c3200908ae62c4993c6c6c0ce4d1c70cc1e8710a3dd20536c48f08c5771b7627 |
| DESIGN.md (APPROVED Rev 1) | 4ac4717cb5c1f2eab59c1db5f2c6fd72684ee2ab80cc581556ea69b58ca571fe |
| styles.css before | d8694abf0dedc93a9fa03a79733bc6e7dda68ce1f75cd0b8fac52b8a3eae306f |
| styles.css after | 9d71fe197a9094cdb2203d755b12a62dda7681f3c716e220f63be67bceabcafc |

Text contrasts against the observed neutral canvas are 13.30:1 (ink), 8.27:1 (caption), and 6.44:1 (muted labels/footer); the visible 2px focus outline is 7.96:1. Text lies outside the image. These bounded contrast/focus checks pass; they do not claim a full accessibility audit. CSS visual order changes while immutable HTML/DOM order remains original; the one interactive link retains keyboard reachability.

Technical **PASS**. Product conformance **PASS** for this fixture's required visible information, immutable bytes and local action. Visual conformance **PASS** for the named initial and observed focus states at 1440x1000 and 390x844, under APPROVED Rev 1. Other viewports, browsers, zoom and assistive-technology behavior are **UNVERIFIED**. User acceptance is **NOT_GRANTED** and remains separate; the specimen is still Review pending.
