# Neutral fixture execution

Use only this project and its local JOEDESIGN skill. Read PRODUCT.md and project DESIGN.md (Status: APPROVED) before editing. Source assets, Product and DESIGN bytes are immutable.

Change only styles.css for the requested bounded visual correction. index.html already contains every required content item and action; preserve its bytes. CSS may recompose the existing structure. No external references, dependencies, generated expansion, new content or external effects.

Use existing local render helper: node render.mjs <html-or-svg-file> <output.png> <viewport-width> <viewport-height>. It uses the already installed Playwright and Chrome; no install needed. The source SVG can be opened through this helper to a PNG for actual visual inspection. Output files go only in artifacts/. Before/after page screenshots use viewport 1440x1000 and390x844; fullPage capture height is distinct from viewport height.

Preserve before-state implementation and renders before edits. When creating source snapshots, keep relative image/style references resolvable by including exact copies of their local inputs; a broken image cannot prove the before or after state. Write an imagery-role map before the first implementation edit. Open/inspect the actual source and before/after PNGs; screenshots existing on disk are not observation. Record exact output paths, hashes, viewport and full-page dimensions, claim-specific observations and limits. Keep a compact proof in artifacts/proof.md. No user acceptance is granted.
