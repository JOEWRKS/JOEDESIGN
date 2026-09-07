# Fieldlight Rentals — Design

Status: APPROVED
Revision: 1
Product Authority: PRODUCT.md

## Visual intent

Calm, practical and trustworthy equipment selection. People should understand what each option includes, its cost and availability, then confidently make their own local selection. No option should receive an implied recommendation. Keep supporting information readable without competing with decision-relevant information or actions.

## Surface

Rental comparison and local selection, including the unselected and selected states. Desktop viewport 1440×1000; mobile viewport 390×844. Preserve information and action access on both.

## Approval boundary

This approval covers the expression intent above, not the current implementation or any future rendered candidate. No exact layout, component pattern, font, spacing value or color token is prescribed. Material changes to this approved intent require a separately proposed revision and explicit user approval.

User Acceptance: NOT_GRANTED

## Bounded hierarchy refinement — 2026-09-07

Implementation/evidence record R1; not a new approved visual authority. The approved Rev 1 intent and user-acceptance status above remain in force. Scope: the existing rental comparison, including local selection and responsive reading. Product authority remains `PRODUCT.md` Rev 1. No external reference or asset was adopted.

### Intended reading relationships

Established before the refined render: enter at the page title, compare each kit's name and day price, read its included equipment, then availability and its selection action. The preview is the concluding feedback group. Equivalent options receive equivalent space, type and action styling; emphasis changes only after a user selection.

Semantic Visual Block Tree (not DOM depth):

```text
Rental comparison surface
  Page context
    Brand
    Task title + explanatory sentence
    Shared hire terms
  Equivalent kit choices × 3
    Kit identity + day price
    Included equipment label + three equipment facts
    Availability label + value, followed by the selection action
  Selection feedback
    Preview heading + live output
```

The existing kit containers remain meaningful: each binds one independently selectable kit to its own price, equipment, availability and action. No nested panels or recommendation treatment were added.

### Implementation choices, not approved tokens

- Spacing: 48px separates the context, comparison and feedback major groups. 24px separates equivalent kits and each kit's summary/equipment/choice subgroups. 16px connects availability to its action. 8px binds title/description, name/price, equipment label/list and preview heading/output; 4px separates list facts and availability label/value. Container insets are 24px. This single task surface has no separate narrative sections requiring the default 160px section gap.
- Type: Arial remains the family, using 400/700 weights. Entry title is 48px bold, kit identity 24px bold, day amount 40px regular, feedback heading 20px bold, readable facts/body 16px, supporting labels/units/terms and controls 14px. Labels use sentence case and muted text; kit names and action labels use weight as well as placement. Price units are subordinate to their amounts.
- Responsive: at widths up to 1000px, equal kits stack in source order; title and prices use 32px, body remains 16px, and page insets become 24px. Group relationships remain consistent. Long names and output can wrap. No required information is collapsed or hidden.
- Color: retained pale neutral page, white kit surfaces, dark green text and green interaction accent. Reusable muted text `#56665f` supports labels and explanations. Solid green belongs to the user's selected action, with a thicker kit outline and explicit live-output text. The pale structural lines are decorative containment, not the sole cue to a control or state.

### Actual-output review

Evidence version: R1, the `index.html` / `styles.css` implementation from this refinement; unchanged `app.js`. All listed PNGs are actual Chrome renders, directly inspected. Screenshots capture full-page content at the named viewport, including mobile content below the fold.

| Expected observable | Actual observation / evidence | Verdict |
| --- | --- | --- |
| Title leads; kit identity and day amount precede lower-emphasis labels and readable equipment facts. | `artifacts/refined-desktop.png`, 1440×1000: title is the largest bold text, all three names and amounts are clear, equipment labels recede above 16px facts. | PASS |
| Equivalent kits are easy to compare without suggesting a preferred kit. | Same desktop render: equal-width containers, matching title/price/equipment positions and action baseline; no initial filled action. | PASS |
| Mobile preserves the same information order and readable facts. | `artifacts/refined-mobile.png`, 390×844: one column, consistent group gaps, complete lists and 48px actions; no clipped content or horizontal overflow. | PASS |
| Selecting a kit marks that kit and gives accurate local feedback. | `artifacts/refined-desktop-selected.png` (1440×1000, Interview) and `artifacts/refined-mobile-selected.png` (390×844, Room): only the chosen kit has the emphasized outline and filled button; the output names it and states no reservation was made. | PASS |
| Keyboard focus is visible and separate from selection. | `artifacts/refined-desktop-focus.png` and `artifacts/refined-mobile-focus.png`, same target viewports: a separated 3px outline surrounds the Pocket button while output still says no kit selected. | PASS |
| Narrow and near-breakpoint layouts remain legible. | `artifacts/refined-width-320.png` (320×900): title and Room name wrap with all content accessible. `artifacts/refined-width-1001.png` (1001×900): three columns retain readable content and aligned controls. | PASS |
| Text and controls retain accessible contrast across used surfaces and states. | Computed actual base pairs: body 10.98:1 on page / 11.92:1 on white; muted text 5.59:1 on page / 6.07:1 on white; action text and selected text 7.87:1; hover pair 7.05:1. Focus/meaningful control outline exceeds 3:1. | PASS |

Technical verification: PASS for the two named viewports. All three kit facts and prices match Product; all three actions work, including tomorrow's kit; each selection replaces the preceding one with exactly one `aria-pressed=true`; Enter/Space selection and reload reset pass. No browser errors or HTTP(S) requests occurred. Measurements and results are in `artifacts/verification.json`.

Product conformance: PASS for the fixed page content and local-selection contract covered above. Visual conformance: PASS for the observed light-theme renders and states listed above. Other browser/platform and forced-color rendering are not claimed as visually verified. User acceptance of this exact output: NOT_GRANTED; these observations do not promote it to approved evidence.
