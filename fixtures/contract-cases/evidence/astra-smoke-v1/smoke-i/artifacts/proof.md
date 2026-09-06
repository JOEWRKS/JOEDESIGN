# Incident Decision Brief — composition proof

Authority: PRODUCT.md v1; root DESIGN.md **APPROVED Rev 1**, the fixture's approved design file. Both read in full and preserved byte-for-byte. User Acceptance remains **NOT_GRANTED**. This evidence does not revise authority or accept a candidate.

Pre-edit intent, Product destinations, semantic block tree, containment/motif diagnosis and responsive relationships: [timestamped structural map](20260906T153930Z/structural-map.md). Saved after opening initial renders, before CSS/HTML edits. [Before source/authority hashes](20260906T153930Z/before-manifest.json). Before source and PNGs are read-only; failed candidate source and renders are also retained unchanged.

Implementation: styles.css corrects grouping/alignment; index.html removes only the empty aria-hidden decorative div. All Product text, three findings and their order, metadata, labels, anchor, button and script remain. Existing Arial, neutral colors and blue action accent remain. No new Product content, imagery, assets or dependencies.

## Exact artifact coverage

All **ten** PNGs below were individually opened with `view_image`. PNG dimensions were read from their headers; a full-page image is not the viewport. Initial/before and candidate/final initial renders used the unchanged `node render.mjs INPUT_HTML OUTPUT_PNG WIDTH HEIGHT`; [render records](20260906T153930Z/render-log.json). Prepared/focus states used the same installed Chrome/Playwright through the local [verification script](20260906T153930Z/verify.mjs).

| Version / state | Desktop artifact — viewport 1440×1000 | Mobile artifact — viewport 390×844 |
| --- | --- | --- |
| Before, empty output | [PNG](20260906T153930Z/before/desktop.png), **1440×1000** full page | [PNG](20260906T153930Z/before/mobile.png), **390×1356** full page |
| Candidate 01, empty output — FAIL | [PNG](20260906T153930Z/after-01/desktop.png), **1440×1000** | [PNG](20260906T153930Z/after-01/mobile.png), **390×869** |
| Final 02, empty output | [PNG](20260906T153930Z/after-02/desktop.png), **1440×1000** | [PNG](20260906T153930Z/after-02/mobile.png), **390×869** |
| Final 02, prepared + button focus | [PNG](20260906T153930Z/after-02/desktop-prepared-button-focus.png), **1440×1000** | [PNG](20260906T153930Z/after-02/mobile-prepared-button-focus.png), **390×927** |
| Final 02, prepared + link focus | [PNG](20260906T153930Z/after-02/desktop-prepared-link-focus.png), **1440×1000** | [PNG](20260906T153930Z/after-02/mobile-prepared-link-focus.png), **390×927** |

Final screenshot source snapshots: [HTML](20260906T153930Z/after-02/index.html), [CSS](20260906T153930Z/after-02/styles.css). Their hashes match the working root files. Image hashes, exact element geometry, content comparison, authority hashes and browser observations: [verification.json](20260906T153930Z/verification.json).

## Expected → observed → verdict

The expectations below were recorded in the pre-edit map, not inferred from the final candidate. Visual observations refer to **Final 02** desktop/mobile initial-state images unless a prepared/focus state is specified. Coordinates are CSS pixels in the full document; geometry corroborates opened images.

| Boundary | Expected observable | Actual observed | Verdict |
| --- | --- | --- | --- |
| Structural sequence / focal ownership | Incident title + summary first; ordered evidence 1 → 2 → 3 second; one action third. Metadata supports summary. | Desktop title leads at x192/y85; summary immediately below; plain metadata follows. Finding tops y313/393/473; button y602. Mobile title y61, summary y114, metadata y210, findings y349/453/557, button y755. No shape competing with title. DOM and vertical order agree. | **PASS** |
| Semantic containment | Group meaning through alignment/proximity; no nested finding cards or ornamental metadata panels. Real section boundaries may use quiet rules. | One uninterrupted neutral surface, plain metadata, open numbered list. Two quiet rules separate evidence/action regions; no rounded shells, shadows or pill surfaces around content. The filled button alone retains control containment. | **PASS** |
| Motif justification | Every remaining familiar pattern serves Product; remove unjustified hero-image, equal-card and decorative-pill motifs. | Numbering expresses ordered evidence; section-label rail identifies evidence/action regions; rules mark those transitions; underlined link returns to findings; single filled rounded button expresses the only primary action. No residual decorative image, feature-card row, nested cards or metadata pills. | **PASS** |
| Meaningful repetition / variation | Equivalent findings repeat one heading/body treatment; differing region roles vary in hierarchy without inventing priority between findings. | All three findings use 20px headings, 16px explanations, 8px heading/body binding and 24px sibling separation. Their sequence carries recovery → remaining delay → restart prerequisite. Title is larger; section labels are smaller locators; action alone has filled accent. No arbitrary emphasis of one finding. | **PASS** |
| Desktop rhythm / intentional asymmetry | Broad introductory reading block; narrow label column beside evidence/action; shared finding-text/action start; coherent major/local spacing. | Labels at x192; list text and button both x456. Intro spans left reading origin while evidence/action shift to their common column. 48px major-region gaps contrast with 24px finding gaps and 8px local binding. Open space to the right preserves reading measure; no equal dashboard boxes. | **PASS** |
| Mobile recomposition | Labels precede content; maintain order/number gutter; wrap comfortably; stack reachable controls; no horizontal clipping. | Labels move above list/action, with 24px label-to-content gap. Main gutter 24px, finding text x48. Summary is three lines, each explanation two; metadata fits one line. Button is 342×50, followed by link; scroll reveals the complete 869px document. Prepared output wraps to two lines in the 927px document. No horizontal overflow in either state. | **PASS** |
| Type / legibility / color roles | Single title focal, distinct equivalent roles, readable support text and body measure; accent belongs to action/navigation. Normal text ≥4.5:1; focus ≥3:1. | Arial title 40px desktop / 32px mobile; body 16/24px; metadata/locators 14px. Desktop summary measure ~641px, evidence ~605px; mobile body stays 16px. Actual text/surface contrast 12.13:1; button 9.28:1; link 8.33:1; focus outline/surface 4.90:1. Quiet rules are supplementary separators, not sole semantic cues. | **PASS** |
| Focus and prepared result | Keyboard focus visibly identifies both controls; result stays bound below action without obscuring content. | Opened all four prepared/focus images: distinct outline around focused button or link, no clipped rings. Exact result appears below controls at desktop x456/y668 and mobile x24/y861. All prior content remains visible in full-page renders. | **PASS** |
| Product invariants / local behavior | Preserve every visible Product string, metadata, three ordered findings, required labels/link, single button, initially empty polite output and exact local result. | Browser comparison with before source matches all content/roles/order/actions and unchanged script. One button; one `#incident-evidence` link targeting existing findings; empty initial output with `aria-live="polite"`. Keyboard activation yields “Recovery review prepared locally. No live action performed.” Link activation reaches the fragment and preserves output. No HTTP(S) requests or browser errors. | **PASS** |
| Authority / scope invariants | PRODUCT.md and DESIGN.md byte-identical; AGENTS.md, render.mjs and installed skill unchanged; only authorized implementation files plus artifacts. | SHA-256 matches for all five fixed files; exact HTML comparison confirms only the empty decorative div was removed. Root source matches Final 02 snapshot bytes. Work stayed inside fixture; no dependencies, external lookup/writes or commits. | **PASS** |

## Failed attempt and final boundaries

The unaccepted baseline fails focal/containment/composition expectations: its large gradient competes with title and delays mobile evidence; nested cards and decorative pills manufacture boundaries. Baseline images and source remain preserved.

Candidate 01: **FAIL** for desktop alignment (finding text x456; button x432). [Observation recorded before correction](20260906T153930Z/after-01-observation.md). Candidate 02 adds only the existing 24px number-gutter inset to desktop actions/output, reset on mobile. Final observation confirms x456 alignment; mobile image bytes remain identical to Candidate 01. No failed render was overwritten.

**Technical PASS:** 25 local checks passed; named target rendering, source/hash invariants, DOM/content/order, keyboard behavior, local anchor, computed contrast and overflow. **Product Conformance PASS:** fixed fixture content/behavior verified against Product v1. **Visual Conformance PASS:** the named desktop/mobile initial and prepared/focus states, observed in Final 02 artifacts against Approved Rev 1 intent. No required FAIL or UNVERIFIED remains within that coverage.

**UNVERIFIED outside coverage:** other viewport/browser combinations and actual assistive-technology announcements; no broader conformance claim. **User Acceptance: NOT_GRANTED**, separate from every PASS above. No authority promotion or approval request is implied.
