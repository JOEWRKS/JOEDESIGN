# Smoke I portable companion proof

Final candidate 02 passes I1–I9 for this fictional Incident Decision Brief in local Chrome 152.0.7977.76 at desktop 1440×1000 and mobile viewport 390×844. The deliberately defective baseline and the first candidate's desktop alignment failure remain preserved. User Acceptance is **NOT_GRANTED**. Final branch testing and program review are separate gates.

This companion supplies working repository-relative links without rewriting the [exact native proof](artifacts/proof.md), [exact native final](native-final.txt), [pre-edit structural map](artifacts/20260906T153930Z/structural-map.md), or [controller observations](controller-observations.md).

## Actual targets

| Version / empty-output state | Desktop image, viewport 1440×1000 | Mobile image, viewport 390×844 |
| --- | --- | --- |
| Preserved defect baseline | [1440×1000 PNG](artifacts/20260906T153930Z/before/desktop.png) | [390×1356 PNG](artifacts/20260906T153930Z/before/mobile.png) |
| Candidate 01 — alignment FAIL | [1440×1000 PNG](artifacts/20260906T153930Z/after-01/desktop.png) | [390×869 PNG](artifacts/20260906T153930Z/after-01/mobile.png) |
| Final candidate 02 | [1440×1000 PNG](artifacts/20260906T153930Z/after-02/desktop.png) | [390×869 PNG](artifacts/20260906T153930Z/after-02/mobile.png) |

The native runtime opened all six images above and four additional prepared/focus images linked from its exact proof. The controller independently opened the six initial-state images above. These are original native PNGs; no replacement render or image edit was used. The final mobile page scrolls vertically; its 869px image is not claimed to fit entirely inside an 844px viewport. Optional prepared mobile images are 390×927.

## I1–I9

| Observable | Verdict | Evidence and boundary |
| --- | --- | --- |
| I1 pre-edit structural map | PASS | Native map creation call: rollout line 58, `2026-09-06T15:42:22.757Z`; successful result line 62, `15:42:24.509Z`; first HTML/CSS edit line 66, `15:43:22.035Z`. The first creation payload reconstructs the exact preserved map bytes. Its heading's `15:39:30Z` labels baseline capture, not map creation. [Independent chronology](controller-chronology.json) and [matching tool results](tool-order-verification.json). |
| I2 Product destinations | PASS | The incident heading and summary lead; subordinate metadata supports them. Ordered evidence follows, then the single recovery action after finding 3 on both targets. |
| I3 semantic containment | PASS | Open surface, proximity and quiet region rules replace nested cards. Numbered heading/sentence groups stay together; the actual primary control retains its filled boundary. |
| I4 motif justification | PASS | The empty decorative blob is removed; pill and shell class names remain inert to minimize markup changes. Numbering, section labels, rules, rounded primary button and underlined link each have a stated Product role. |
| I5 repetition / variation | PASS | Findings repeat equivalent heading/body treatment. Introduction, section labels, evidence and action vary in position, scale and accent according to role. |
| I6 desktop rhythm / asymmetry | PASS after preserved candidate-01 FAIL | The section-label rail and wider content column express the reading sequence. Final finding text and button begin at x456. Candidate 01 began the button at x432; its recorded failure precedes the two-rule correction. |
| I7 mobile recomposition | PASS | Labels move above content, numbers retain a gutter, text wraps and controls stack. Desktop ornament and nested card padding disappear; Product sequence and horizontal fit remain. |
| I8 fixed Product / approved authority | PASS | Frozen fixture, seed and before snapshots match for PRODUCT, DESIGN, AGENTS and renderer. All three installed/shipped skill hashes match the fresh semantic producer. HTML removes only the empty aria-hidden div; script and Product content remain. Independent browser checks confirm visible text, ordered findings, single local action, evidence link and empty initial output. |
| I9 acceptance separation | PASS | [DESIGN.md](DESIGN.md) remains APPROVED Rev 1 with explicit User Acceptance: NOT_GRANTED. Candidate conformance does not grant acceptance. |

I2–I9 judgments combine the actual opened images with the controller's exact observations and [independent browser readback](controller-browser-observation.json). [Change verification](change-verification.json) binds fixed input/source/skill bytes; [source.diff](source.diff) shows the bounded implementation delta. The native [verification output](artifacts/20260906T153930Z/verification.json) records 25 local checks; the independent readback records 12 checks. Both sets pass within their reported coverage.

## Preserved failure and provenance

The baseline intentionally fails the approved open composition intent. Candidate 01 then fails the native map's exact desktop shared-start-line expectation: finding text x456, button x432. Its [failure observation](artifacts/20260906T153930Z/after-01-observation.md), sources and both PNGs remain intact. The native call sequentially wrote that record, marked it read-only, then added the existing 24px number-gutter inset to desktop actions/output and reset it to zero on mobile. Candidate 02 repairs the desktop relation; candidate 01 and 02 mobile PNG bytes are identical. No skill, authority or criteria change was used to obtain PASS.

There was one native invocation and no native failed command. Actual runtime was `gpt-6-astra` / `xhigh`, thread `01a0775f-4777-7f33-bf60-1fb0d3b05c75`, `codex-cli 0.153.4`, exit 0, recorded duration 622605ms. [Native provenance](native-provenance.json) binds the source implementation, frozen fixture commit/tree, binary, rollout, launch, prompt-input, final, collector and full shipped package hashes. [Tool-order verification](tool-order-verification.json) records four actual image-call batches and ten returned image blocks. The collector's broad substring count of seven includes prose mentions in document patches and is not used as the actual call count.

## Portable source and original-link mapping

The exact [before HTML](artifacts/20260906T153930Z/before/index.html) resolves its adjacent [CSS](artifacts/20260906T153930Z/before/styles.css); the exact [final HTML](artifacts/20260906T153930Z/after-02/index.html) resolves its adjacent [CSS](artifacts/20260906T153930Z/after-02/styles.css). The [failed candidate HTML](artifacts/20260906T153930Z/after-01/index.html) and [CSS](artifacts/20260906T153930Z/after-01/styles.css) are also portable. These pages use no external assets or runtime dependencies.

Native `artifacts/...` paths retain their original layout below this packet, so map/proof source and image links work. Absolute workspace links in the verbatim native final map to those same relative artifact paths here. Controller shorthand such as `after-02/desktop.png` is relative to `artifacts/20260906T153930Z/`. Fixed root [PRODUCT](PRODUCT.md), [DESIGN](DESIGN.md) and [AGENTS](AGENTS.md) are included byte-exact. The original native proof's `verify.mjs` link identifies an external validation-only helper: its exact output is included as verification.json, and its SHA-256 is recorded in tool-order-verification.json. That script and the installed renderer/browser dependencies are intentionally not shipped as new infrastructure. Raw rollout/events, isolated homes and credentials remain external.

[manifest.json](manifest.json) mechanically inventories every packet file with SHA-256 and byte length, excluding its own self-hash. PASS is limited to this neutral fixture, named browser/viewports, recorded sources and observed local simulation. Other browsers/devices/viewports/themes, complete accessibility, assistive-technology announcements, production behavior, user acceptance, comparative superiority, competition readiness and phase closure are unverified or not claimed.
