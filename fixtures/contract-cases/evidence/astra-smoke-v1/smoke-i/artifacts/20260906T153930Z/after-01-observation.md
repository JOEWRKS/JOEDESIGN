# Candidate 01 — observed before bounded correction

Source: read-only [after-01/index.html](after-01/index.html) and [after-01/styles.css](after-01/styles.css). Both actual PNGs opened with view_image: [desktop](after-01/desktop.png), viewport/PNG 1440×1000; [mobile](after-01/mobile.png), viewport 390×844, full-page PNG 390×869.

Expected → observed → verdict:
- Incident → ordered evidence 1/2/3 → action, with one title focal: visible in both images; no decorative shape or competing panel → PASS.
- Semantic containment without nested cards/pills: open surface, region rules, unboxed metadata and vertically repeated findings visible in both → PASS.
- Desktop section labels form a narrow rail; finding text and action share a start line: labels align at x192, finding text begins x456, button begins x432 → FAIL against the pre-edit alignment expectation.
- Mobile labels move above content, numbers remain visible, controls stack after evidence: observed; full-width button and evidence link fit, no horizontal overflow → PASS.

Candidate visual result: FAIL for the exact desktop alignment relation. Preserve all candidate files and renders; do not overwrite. Bounded correction: inset desktop actions and result by the existing 24px list-number gutter; retain full-width mobile controls by resetting that inset in the existing breakpoint. No authority, content, behavior, type, or palette change. No user acceptance is inferred.
