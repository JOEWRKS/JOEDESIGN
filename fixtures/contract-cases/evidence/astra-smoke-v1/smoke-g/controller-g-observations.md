# Controller actual-image observations — Smoke G

The four actual native PNGs were opened with the local image viewer, not inferred from a test or screenshot existence. Observations below apply to these exact bytes; native completion and final artifact identity must also be checked before final gate.

- before-desktop.png: 149aa57ae5dcf2e61b41a5678e1f7a29c5f9b43ee87626a8d2556e78a1adffe6
- after-desktop.png: 01368b15217fc22315817ee8b6845f0e0b213275c6537b4ae976c963e6031466
- before-mobile.png: 1225d70f9e7fa67ed3a4adadbae7d99ca9b1a218f7c6d5fcc80cbbb82a1846ce
- after-mobile.png: d75a2260b5fb178a0309bc21ac8572edfe6cf41514720475dbca97995a0ce22b

## Before

Desktop: magenta headline, green eyebrow and queue wrapper, violet queue heading, cyan action, orange metadata, and differently tinted/railed rows compete. Supporting descriptions are visibly faint. R-02 has a colored rail but no visible Current priority text. Explicit status labels exist but yellow and red text is weak.

Mobile: a darker blue-gray canvas and nested tinted queue change the foreground/background context. The pale lead and footer are especially weak. The three Product records remain in order, but the priority indication still depends on the rail's hue rather than an explicit visible label.

## After

Desktop: the large dark heading provides the entry point; one solid blue review action is the dominant colored control. Descriptions and metadata share a readable, quieter slate role. The rows are an open list on the common canvas with thin neutral separators, not individually tinted panels. R-02 alone retains the blue priority rail and now visibly says Current priority; Ready, Needs review and Blocked retain distinct literal labels and their original record assignment.

Mobile: the same semantic color hierarchy survives independently on the actual common light canvas. The two-line title and primary action stay prominent; full-page content is readable through the three ordered records. Current priority fits alongside R-02 and its Needs review label without overlap. No required text is clipped or hidden in the observed page; vertical scrolling remains necessary, and a full-page image does not imply that all content fits inside the 844px viewport.

## Boundary

These are bounded visual observations, not user acceptance or a full accessibility certification. Actual independent DOM/computed-color, frozen-input, and interaction verification is still required before final technical/Product/contrast PASS. No judgment about an unprovided theme, production system, other browser, statistical consistency, or comparative superiority is made.

## Independent completion readback

Native execution finished once with exit 0, thread 01a07666-dd97-7a20-800a-087f437002c8, actual gpt-6-astra/xhigh. The four image hashes above were checked again after completion and are unchanged. The only native tracked change against the frozen fixture commit is styles.css. No worker/controller correction was made.

A separate Chrome readback inspected before/after at both exact viewports. Exact Product payload/order/action target, normalized body text, PRODUCT.md, APPROVED DESIGN.md, AGENTS.md and render.mjs all remain unchanged. The after state has 26 visible text elements per viewport, all above their applicable minimum, with no unsupported gradient/opacity context or horizontal overflow. Minimum observed after text ratio is 5.5533252875311545 (Blocked label); Current priority is visible and 6.648377872586666. The same values were independently recomputed on the actual mobile canvas rather than inferred from desktop.

Controller also opened actual focus crops at both viewports: a complete 2px solid outline, offset 3px, surrounds the primary action and focused R-02; the label and status remain separated and visible. The outline is 8.314699070021883:1 against its adjacent canvas (see independent summary for full precision). Hover text and primary focus/base text remain above 4.5. The native keyboard Tab/Enter readback additionally verifies the original #review-r-02 target; controller programmatic focus is corroborating visual evidence, not a second claimed keyboard traversal.

Verdict: bounded desktop/mobile visual, Product invariant and applicable contrast PASS. User acceptance remains NOT_GRANTED. Outside-target limitations above remain UNVERIFIED; they do not become claims from the passing bounded proof.
