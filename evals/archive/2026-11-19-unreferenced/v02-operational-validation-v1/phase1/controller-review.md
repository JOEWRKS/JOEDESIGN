# Phase 1 Controller independent review

Frozen BIO source snapshot: `b35cc11fbcb5fb64dbd55f37f34a1d7deadac3bf`.
Frozen Phase 1 result: `4d2fbf4287a38439e32ecc26db480a8b87d21d0a`.
Approved original: six byte-preserved PNGs in `../authority/originals/`, with
the scope and approval commits in `../authority/approved-visual-authority.md`.
Result: six `final-kf*.png` files here, from the production `/#/` route.

I opened all six original PNGs and all six final-result PNGs separately. I
then independently opened the live isolated Vite app in Chrome 152 via
Playwright at 1440×900 and 390×844, with fonts and images decoded, and
captured each of the three scroll states in memory. All six independent live
capture SHA-256 values **exactly matched** the six frozen candidate final PNGs
(listed in `../final/manifest.json`). Live phases were A/D/G respectively,
one scene visible at each state, Instrument Sans loaded, and no horizontal
overflow. This confirms the reviewed PNGs are actual reproducible browser
results, not reused proof screenshots.

| Axis | Approved source relation → actual observed result | Verdict |
| --- | --- | --- |
| C1 Product preservation | KF-01 science/pipeline actions, KF-02 ordered five roles, and KF-03 `PUB-006` publication data/disclaimer → all visible with the same wording and targets. The production Home retains lower sections; independent `pnpm test` is 16 files / 142 PASS and `pnpm build` passes. No Product data, route or root DESIGN change is in the implementation diff. | PASS for the scoped static/Home checks; other product flows unverified |
| C2 Composition | KF-01 biological field dominates with left headline tension; KF-02 left editorial intro and roles bind to the field; KF-03 single publication occupies the mineral field → each major region and focal order is retained at both named targets. | PASS |
| C3 Image | The approved cyan/violet membrane, independent mobile KF-01 crop, KF-02 folds, and KF-03 continuous dark-to-mineral contour → the actual captures retain the same asset family, scale and focal mass. Minor raster/edge differences do not alter the relationship. | PASS |
| C4 Typography | Approved title silhouettes, desktop/mobile wraps, concise metadata and disclaimer → production captures closely preserve hierarchy, line breaks and reading measure. But the low-emphasis KF-03 metadata/disclaimer and coral kicker are faint over the approved image field; candidate's actual-background sampling found approximately 2.8–3.8:1 for several text regions, below 4.5:1 AA. | PARTIAL: geometry PASS, contrast FAIL / approved-target conflict |
| C5 Spacing/rhythm | Approved KF-01 CTA grouping, KF-02 role progression, KF-03 title→rule→metadata→disclaimer → actual groups retain these gaps and density transitions at desktop/mobile. | PASS |
| C6 Responsive | Each approved mobile original is an independent 390×844 composition, not scaled desktop → actual mobile KF-01 two-line title and crop, KF-02 vertical Decode→Learn flow, KF-03 readable title/metadata order match; no horizontal overflow, controls remain present. | PASS for named viewport/static states |
| C7 Translation process | Candidate received and opened original PNGs and real assets directly, plus Product and DESIGN authority. It made one implementation attempt with local self-correction, no alternate direction, no clarification question and no DESIGN growth. Specific source-driven composition decisions appear in the diff; original was not replaced by a prose-only translation. | PASS for workflow use; no causal superiority claim |

Controller verdict: **PARTIAL**. The approved static visual relationships
translated closely and the candidate independently self-observed them, but
the specific KF-03 approved-color versus text-contrast conflict remains a
known accessibility FAIL. It must not be silently restyled or reported as
compliant. User/PM usability and any Phase 2 bounded correction remain pending
their separate judgment. Existing motion timing/easing/transitions, other
breakpoints, full Product behavior and user acceptance are not established by
these static images.

Controller verification: independent `pnpm test` exit 0 (142/142), independent
`pnpm build` exit 0 (large-chunk advisory), independent browser capture exit 0,
and `git diff --check` exit 0. The candidate reports two pre-existing full
TypeScript `TS1005` errors in untouched editorial files; the three KF approval
records document the same boundary. No Phase 1 file was modified for this
review.
