# Controller independent actual-render observations — Smoke I

Root directly opened all six native-produced original-detail PNGs: baseline desktop/mobile, failed candidate 01 desktop/mobile, final candidate 02 desktop/mobile. No screenshot was regenerated or edited for this review. Relative source paths below refer to the portable Smoke I packet, preserving native artifact layout.

## Expected → observed → verdict

| Check | Actual observation | Verdict |
|---|---|---|
| I2 Product first/second/third destinations | In after-02/desktop.png the bold incident heading opens the page, followed by its summary and subordinate metadata. The ordered evidence occupies the next major region; the sole filled action follows finding 3. after-02/mobile.png preserves that same readable sequence. | PASS |
| I3 semantic containment | The earlier nested rounded region/card walls are absent. Whitespace, alignment and quiet rules distinguish actual regions. Each numbered finding remains a heading/sentence group; only the actual primary control needs a filled bounded surface. | PASS |
| I4 justified motifs | The decorative blob, promotional identifier/metadata pills and generic split opening no longer drive the composition. A familiar rounded filled button and underlined link remain because they are real primary/secondary controls; ordinary patterns have not been blanket-banned. | PASS |
| I5 repetition / variation | All three findings repeat number, heading, body and spacing for equivalent evidence roles. Broad incident introduction, narrow section labels, evidence column and action accent vary because their jobs differ, not to create random novelty. | PASS |
| I6 intentional desktop rhythm | Section labels form a restrained left rail; evidence occupies the wider reading column. Candidate 01 placed the button 24px left of the finding text despite the fixed shared-start-line intent. Candidate 02 visibly aligns both at the same start; only the existing desktop number-gutter inset and mobile reset changed. | PASS after preserved candidate-01 FAIL |
| I7 mobile recomposition | The desktop label rail moves above its content. Numbered findings wrap naturally without card padding; controls stack and the primary button uses available width. No blob or desktop ornamental height remains. Required content fits horizontally and continues vertically; this is not merely a smaller desktop image. | PASS |
| I8 Product and approved authority | Actual browser readback finds unchanged normalized visible text, identical ordered findings, one unchanged local action and one unchanged evidence link. Initial output is empty; keyboard activation produces the same local-only result before/after. Fixed PRODUCT.md, DESIGN.md and AGENTS.md equal seed and before-snapshot bytes. | PASS |
| I9 acceptance separation | APPROVED DESIGN.md preserves its fixed intent and explicit User Acceptance: NOT_GRANTED. This review judges a candidate, not user acceptance or promotion. | NOT_GRANTED preserved |

I1 PASS: controller-chronology.json binds actual map creation at rollout line 58 / 2026-09-06T15:42:22.757Z before first CSS/HTML edit at line 66 / 15:43:22.035Z. Root decoded the literal creation patch as data and verified that its exact UTF-8 bytes equal the final map; no post-edit criteria replacement occurred. The map heading labels capture time, not creation time. Four actual image-call batches (lines 41, 78, 105, 125) are distinguished from prose merely mentioning view_image.

## Actual targets and independent readback

- Browser: Chrome 152.0.7977.76, headless local rendering.
- Desktop viewport: 1440×1000; baseline and both candidate full-page PNGs: 1440×1000.
- Mobile viewport: 390×844; baseline full-page PNG: 390×1356; candidate 01 and 02 full-page PNGs: 390×869. The final bottom link continues below the initial viewport and is reachable by normal vertical scrolling; no false claim that the whole page fits in 844px is made.
- controller-browser-observation.json records four actual page loads (baseline/final × desktop/mobile), unchanged visible text/finding order/action behavior, empty initial output, zero horizontal overflow and zero page errors. This is not a visual scorer or a replacement for opening the PNGs.

## Preserved failure and cause

after-01-observation.md identifies the exact failed desktop alignment relation before correction. Direct inspection of its PNG confirms the offset. The source comparison from after-01/styles.css to after-02/styles.css adds only a 24px margin-left to desktop actions/output and resets it to zero in the existing mobile breakpoint. The final PNG confirms that relation is repaired; the mobile image remains equivalent. No skill or authority change was used to obtain the result.

The read-only git --no-index comparison returned 1 because it found the expected CSS difference; its local LF/CRLF warning did not modify source bytes and is not a test failure.

## Exact boundary

PASS covers this neutral fictional fixture, these source snapshots, named local browser, default rendered state and viewport sizes, plus the observed local simulation. It does not establish other browsers/devices/viewports/themes, complete accessibility or assistive-technology conformance, production incident behavior, user acceptance, statistical superiority, competition readiness or phase closure.
