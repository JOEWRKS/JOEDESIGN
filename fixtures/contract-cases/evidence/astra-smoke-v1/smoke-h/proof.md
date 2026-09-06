# Smoke H portable companion proof

This companion translates the exact native Smoke H output into repository-relative links and combines it with the controller's independent readback. It does not rewrite the preserved [native proof](native-proof.md), [native final](native-final.txt), or [pre-edit role map](role-map-before.md). The fixture is fictional, neutral, and uses only the supplied local [synthetic SVG](assets/specimen-s17.svg).

## Actual rendered evidence

Both the native runtime and the controller opened the source and four initial-state images. The controller opened exactly these five images, not the optional native focus captures.

| Target | Before | After | Viewport | Full-page PNG |
| --- | --- | --- | --- | --- |
| Desktop | [before](before-desktop.png) | [after](after-desktop.png) | 1440x1000 | 1440x1000 both |
| Mobile | [before](before-mobile.png) | [after](after-mobile.png) | 390x844 | 390x896 before; 390x891 after |

[Source specimen](source-specimen.png) is 1200x900. The complete irregular contour, upper-right amber inset, and three lower-left circular impressions are visible in the source. The before mobile capture is an aggressively clipped strip that omits those required regions. After correction, desktop gives the specimen the larger first column and mobile begins with the complete specimen; both after images preserve the source canvas and its important regions.

The controller's exact image observations are preserved in [controller-observations.md](controller-observations.md). Its separate Chrome readback is [controller-browser-observation.json](controller-browser-observation.json). The native runtime's full technical readback is [verification.json](verification.json).

## H1-H9 verdicts

| Observable | Verdict | Evidence |
| --- | --- | --- |
| H1 role mapping is explicit before edit | **PASS** | [Role map](role-map-before.md) records role, owner, regions, relationship, defect, and responsive expectation. Native rollout timestamp `2026-09-06T13:38:17.249Z` precedes the first `styles.css` patch at `13:38:46.853Z`; source and before-image views precede the map. |
| H2 intended focal owner is visually dominant after edit | **PASS** | Both independent image reads find the large specimen owns first attention on desktop and is the first substantial mobile block. |
| H3 text-image hierarchy is intentional | **PASS** | After desktop uses a quiet 40px title beside the 832x624 image; mobile uses a 32px title after image and caption. Metadata and action remain secondary and readable rather than co-dominant. |
| H4 important focal regions remain visible | **PASS** | Complete contour, complete amber inset, and three individually distinguishable impressions are visible in source and both after captures. |
| H5 desktop framing is deliberate | **PASS** | The source is shown at intrinsic 4:3 proportion with visible surrounding margin; the image leads a 2:1 grid and the former competing frame is absent. |
| H6 mobile translation preserves focal intent | **PASS** | Mobile independently reflows image then caption then identification/action at 342x256.5; it is not a shrunken desktop row. No crop or horizontal overflow remains. |
| H7 decoration does not steal ownership | **PASS** | The CSS double border, offset shadow, padding, and rotation are removed; the immutable illustration's own internal shadow remains. |
| H8 Product Truth and approved authority remain unchanged | **PASS** | Exact hashes below and controller comparison cover PRODUCT, APPROVED DESIGN, AGENTS, index, source SVG, render helper, and resolvable before/after snapshots. Only `styles.css` changed in the native fixture. |
| H9 user acceptance remains separate | **PASS** | DESIGN retains `NOT_GRANTED`, Product state remains `Review pending`, and neither native nor controller output promotes acceptance. |

## Immutable and output identity

| File | SHA-256 |
| --- | --- |
| PRODUCT.md | `c3200908ae62c4993c6c6c0ce4d1c70cc1e8710a3dd20536c48f08c5771b7627` |
| DESIGN.md | `4ac4717cb5c1f2eab59c1db5f2c6fd72684ee2ab80cc581556ea69b58ca571fe` |
| AGENTS.md | `892cea5e1ee73668bbad0489368adc8a62adcb31dff7758e885deedbab6c2a1b` |
| index.html | `00bd324772a8cde52f613c97ce1dba71187dfc64f9bc250a64e3a4968d9c9120` |
| assets/specimen-s17.svg | `7cd4487dd9198034c853e06b29755a34f32aa3fbca2dddf042adb694b7575a12` |
| render.mjs, validation-only and not shipped here | `a6c3283de91f30917317f52aed00e73f6002750d2e8fc6646bf4cb4266ee93cb` |
| styles.css before | `d8694abf0dedc93a9fa03a79733bc6e7dda68ce1f75cd0b8fac52b8a3eae306f` |
| styles.css after | `9d71fe197a9094cdb2203d755b12a62dda7681f3c716e220f63be67bceabcafc` |

The portable [before HTML](before/index.html) resolves [before CSS](before/styles.css) and its exact local asset. The portable [after HTML](after/index.html) resolves [after CSS](after/styles.css) and its exact local asset. [manifest.json](manifest.json) binds every shipped evidence file.

## Native provenance, diagnostic, and limits

The one initial native invocation completed with exit 0 using actual `gpt-6-astra` / `xhigh`; thread `01a076ee-20ca-77b1-8628-39cd36560799`; `codex-cli 0.153.4`; binary SHA-256 `a1cf6360ca71918d5466bc3a32d9f18b7044c9128756d1949e715d277b88c9b6`. Shipped runtime dependency count is 0; installed Playwright/Chrome was validation-only. [native-provenance.json](native-provenance.json) records binary, rollout, prompt-input, final, exit and skill hashes plus ordered image/edit events.

One native command failed: direct screenshot of the SVG document timed out after 30 seconds. The exact command and output are preserved in `native-provenance.json`. The unchanged SVG was then successfully rendered through a local HTML wrapper and opened. This is a preserved operational failure, not an unresolved H observable.

The PASS is bounded to local Chrome desktop 1440x1000 and mobile viewport 390x844, their recorded full-page outputs, the supplied synthetic source, and the local review-note navigation. Other viewports, physical devices, browsers, zoom, assistive technology, full accessibility, real specimen validity, production acceptance, comparative superiority, competition readiness, and phase closure are **UNVERIFIED / not claimed**. User acceptance remains **NOT_GRANTED**.
