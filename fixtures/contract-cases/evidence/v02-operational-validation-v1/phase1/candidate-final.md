# JOEDESIGN v0.2 — Phase 1 candidate

Source snapshot: `b35cc11fbcb5fb64dbd55f37f34a1d7deadac3bf`.
Branch: `codex/bio02-joedesign-v02-operational-validation`.
Pinned skill package: `2ccb229353ebb2776ebed793056158efffb50b33`.
Authority: root `DESIGN.md` APPROVED Rev 1, Product master handoff, and the three KF approval records dated 2026-09-05. All six original screenshot hashes were checked against those records. The original PNGs were opened before implementation.

## Implementation

Translated the approved scene relationships into scoped production Home styles using the existing real assets. KF-01 restores the opening crop, headline mass, quiet kicker and CTA spacing. KF-02 restores its three material layers, five role labels, explicit title break and independent mobile crop. KF-03 restores the mineral/imprint masks, publication title breaks and metadata grouping. Its mobile metadata grid was adjusted after observing the original PNG and actual runtime so the journal/year no longer breaks unnecessarily.

Kept the production header's region, search, navigation and focus behavior while matching its Home signature appearance; its lower-Home compact appearance remains intact. Existing scroll ranges and three scenes remain navigable, with a biological backdrop through the copy reveal gaps. Hidden scenes are inert; reduced motion presents all three complete static compositions. Product text, `PUB-006`, routes, fixtures and lower Home components are preserved. No proof module is imported into production; the original proofs, assets, approval records, DESIGN and pinned package were not modified.

## Actual observation

New captures came from the production `/#/` route on the isolated Vite server at `127.0.0.1:8547`, Chrome 152, device scale 1, loaded Instrument Sans and decoded assets. I opened and visually inspected all six final PNGs against the original approved PNGs, plus all six reduced-motion captures. These are runtime screenshots, not reused proof images.

| Expected relationship | Actual observed fact | Result |
| --- | --- | --- |
| KF-01: dominant cyan/violet field; desktop left headline tension; mobile two-line lower headline | Both crops, two-line title, reading copy and both CTAs remain visible at 1440×900 and 390×844 | PASS for scoped static relationships |
| KF-02: biological folds carry Decode → Learn; independent vertical mobile flow | Five labels align to the same material family; mobile roles continue down the whole field rather than compressing near the top | PASS for scoped static relationships |
| KF-03: continuous dark-to-mineral contour; one publication object | Material contour, title silhouette, three metadata groups and fictional citation disclaimer are visible in both targets | PASS for scoped static relationships |

No pixel-identity claim is made: production icons and minor font rasterization/spacing remain implementation differences. The mobile metadata extension is an estimated mapping from the approved image. The six final artifacts are:

- `final-kf01-desktop-1440x900.png`
- `final-kf01-mobile-390x844.png`
- `final-kf02-desktop-1440x900.png`
- `final-kf02-mobile-390x844.png`
- `final-kf03-desktop-1440x900.png`
- `final-kf03-mobile-390x844.png`

Capture scroll positions: desktop 0 / 2475 / 4703px; mobile 0 / 2617 / 4971px (progress 0 / .5 / .95; phases A / D / G). Earlier `initial-*` and separate `reduced-*` captures remain as evidence of this one implementation attempt. `capture.mjs` and `verify.mjs` document the local reproduction environment.

## Verification and boundaries

- Existing suite: 16 files, 142 tests PASS. Final focused Home/header run: 2 files, 21 tests PASS.
- Production build PASS (existing large-chunk warning). Focused TypeScript for the three edited TSX/TS files PASS. `git diff --check` PASS.
- Full repository TypeScript still FAILS on pre-existing `TS1005` errors in `EvidenceFieldSection.tsx:21` and `PrecisionLoopSection.tsx:15`, also documented in the original approval records. Those files were not changed.
- Browser checks PASS at both viewports: search/Escape, desktop/mobile navigation and Escape, restored mobile opener focus, KF-02 CTA to Science, reverse scroll to KF-01, lower Home presence, no horizontal page overflow, complete reduced-motion scenes. No runtime page errors were observed during final captures.
- Accessibility contrast FAIL / approved-target conflict: sampling actual KF-03 backgrounds with the text temporarily hidden and compositing its CSS foreground found the Authors label at 3.03–3.61:1 desktop / 3.15–3.79:1 mobile, and disclaimer at 2.81–3.41:1 / 3.30–3.68:1. The coral kicker's sampled background range also remains below 4.5:1. These inherited approved colors conflict with the AA requirement. They were preserved for the explicitly requested static target rather than silently restyled. This candidate therefore does **not** claim overall visual/accessibility acceptance; that conflict needs an explicit scoped decision.
- Motion appearance, structural transformation quality, performance profiling, other viewport compositions and new user acceptance are UNVERIFIED. Existing scroll operation and reduced-motion completeness do not imply motion approval. No new visual direction or motion acceptance is asserted.
