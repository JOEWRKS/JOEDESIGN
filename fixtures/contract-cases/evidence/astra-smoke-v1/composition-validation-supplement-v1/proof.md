# Composition validation supplement — one unhinted countercase

Controller verdict: **PASS for this one bounded countercase**, under the seven criteria frozen in [controller-rubric.md](controller-rubric.md). This is not a skill revision, a new semantic replay, a Smoke I rerun, a causal experiment, or a competition-readiness determination. User Acceptance: **NOT_GRANTED**.

## Fixed inputs and execution

Repository `JOEWRKS/JOEDESIGN`; branch `codex/joedesign-v0.1-composition-validation-hardening`; pinned baseline `2b75ca76d6fcadb8aedbc7c7f1390b3bc760ec28`.

The controller froze the fictional Fieldlight Rentals Product, APPROVED expression intent, source, current images and rubric before the native invocation. The fourteen preregistration files were committed as `43852b422adaee8662e753ba178bce468855fe11` before launch. The seed was a viable comparison of three independent equipment kits with modest emphasis opportunities, not a deliberately broken interface. Cards are neither a mandatory answer nor sufficient evidence of success.

- [Frozen Product](inputs/PRODUCT.md), [original APPROVED Design intent](inputs/DESIGN.md), [preregistration](pre-registration.json), [exact prompt file](producer-prompt.txt).
- The sole task prompt was: `$joedesign 이 화면의 정보 위계와 읽기 흐름을 개선해.`
- Exactly one native `gpt-6-astra / xhigh` invocation: thread `01a0781f-b804-7db3-8c1e-70f3598df0f9`, `codex-cli 0.153.4`. Actual rollout turn-context line 8 confirms model, reasoning and `danger-full-access`; launcher flags alone are not the identity evidence.
- Launch `2026-09-06T19:08:56.104Z`; final message `2026-09-06T19:16:39.879Z`; exit 0, measured process duration 464528 ms. There was no second session, follow-up prompt or controller hint.
- [Runtime provenance](runtime-provenance.json), [complete custom-tool input index and bounded result excerpts](producer-tool-records.json), [actual returned-image observations](producer-observations.json), [exact native final text](producer-final.txt).

## Isolation boundary

Fresh context/home and selective input copying supplied the fixed JOEDESIGN package, neutral Product/Design, current source/images, general execution tooling and exact short request. The rubric, this supplement assignment, previous Smoke I, reports, expected layouts/actions, tests and other-agent answers were not provided. Project skill input was only JOEDESIGN; the ordinary native system catalog also listed imagegen, openai-docs, plugin-creator, skill-creator and skill-installer. No additional skill load was observed. Personal design skills, plugins and multi-agent execution were disabled.

This was **not OS/filesystem isolation**: the process had a shared filesystem with `danger-full-access`. Recorded calls show fixed source/package reads, general renderer/Playwright/Chrome use and ordinary ancestor `AGENTS.md` discovery returning empty. No access to excluded controller/historical inputs was observed. This audit is not a guarantee that excluded paths were inaccessible. The debug prompt preview is not the actual execution sandbox authority.

## Portable actual screens and source

Chrome `152.0.7977.76`, Node `v26.3.0`, local HTML with existing Playwright tooling. No external assets, installation or production external write was needed. Repository files suffice to inspect the source and images; raw-local provenance paths are supplemental audit locators, not the only visual evidence.

| Evidence | Desktop, viewport 1440×1000 | Mobile, viewport 390×844 |
| --- | --- | --- |
| Frozen before, also returned to Producer before editing | [before/desktop.png](before/desktop.png), PNG 1440×1000 | [before/mobile.png](before/mobile.png), full-page PNG 390×1415 |
| Refined result actually returned to Producer | [refined-desktop.png](producer/artifacts/refined-desktop.png), PNG 1440×1000 | [refined-mobile.png](producer/artifacts/refined-mobile.png), full-page PNG 390×1645 |
| Independent Controller render after Producer exit | [controller desktop](controller-after/desktop.png), PNG 1440×1000 | [controller mobile](controller-after/mobile.png), full-page PNG 390×1645 |
| Producer-observed selected state | [Interview selected](producer/artifacts/refined-desktop-selected.png) | [Room selected](producer/artifacts/refined-mobile-selected.png) |
| Producer-observed focus state | [desktop focus](producer/artifacts/refined-desktop-focus.png) | [mobile focus](producer/artifacts/refined-mobile-focus.png) |

The raw native final text retains its exact original local links; the refined desktop/mobile links in the table are its portable counterparts. Optional Producer-observed width checks are [320px](producer/artifacts/refined-width-320.png) and [1001px](producer/artifacts/refined-width-1001.png), not substitutes for either required viewport.

Before source: [HTML](before/index.html), [CSS](before/styles.css), [selection logic](before/app.js). Final source: [HTML](producer/index.html), [CSS](producer/styles.css), [selection logic](producer/app.js), [Product](producer/PRODUCT.md), [Design with appended evidence](producer/DESIGN.md). [Exact source diff](source.diff) and [hash/authority binding](boundary-readback.json) make the scope reviewable without the local runtime workspace.

## Frozen rubric → independent Controller observation

The Controller opened the before pair before launch, independently rendered/opened the final pair after exit, and exercised the fixed choices at both viewports. It also opened the native desktop-selected and mobile-focus images. It does not claim to have personally inspected all six optional native images; the ten-image Producer observation record is separate.

| Criterion / expected boundary | Actual Controller evidence and judgment | Verdict |
| --- | --- | --- |
| C1 Product preservation | All three names, day prices, equipment lists, availability values and corresponding actions remain. `PRODUCT.md` and `app.js` are byte-identical. Independent browser checks exercise every choice, reselection, exactly one pressed button, accurate local output and reload reset. Tomorrow's kit remains selectable as specified. No initial recommendation, HTTP(S) request, browser error or storage entry was observed. | PASS |
| C2 Grouping / comparison | Each kit still binds its own name, price, facts, availability and button. Desktop preserves equal option weight and aligned like fields/actions; these alignments already existed and are not claimed as newly invented. In the rendered revision, clearer name/price grouping and quieter supporting labels make comparison easier without privileging one option. | PASS |
| C3 Hierarchy improvement | Before: the brand, hire note and bold equipment/availability labels compete with regular-weight kit names/prices. After: task title leads, kit names and amounts are prominent, price units/labels recede, readable equipment facts follow, and bold-label 48px controls remain distinct. This visible separation appears on both actual target renders; it is not inferred merely from changed CSS. | PASS |
| C4 No common-pattern overcorrection | The result retains appropriate independent units, with small internal semantic wrappers instead of destroying comparison boundaries. The Producer's pre-edit public statement preserves equal option weight and orders meaningful information. Its appended rationale binds each container to one independently selectable kit. Retention is evaluated for suitability, not because cards are a required answer. | PASS |
| C5 Responsive | Mobile keeps the three options in source order with readable facts, complete labels and reachable actions. Independent browser geometry shows document width390 at viewport390, no horizontal overflow; every choice works. Full-page height increases1415→1645, an explicit230px scrolling tradeoff for larger type/spacing, not a shorter-page claim or automatic failure. Desktop1440×1000 remains coherent. | PASS |
| C6 Autonomous Producer observation | Without controller follow-up, actual tool results returned two before images, two refined target images, and six selected/focus/optional-width images. Public pre-edit and post-render statements correspond to the observed revisions. One rejected patch was corrected in the same invocation before the refined render; no rendered defect requiring a new visual revision was identified. The Controller's own images/behavior checks are not counted as Producer autonomy. | PASS |
| C7 Approval boundary | Original1009-byte APPROVED Rev1 Design intent is a byte-exact prefix of the final6963-byte project file. The51-line append explicitly labels itself an unapproved implementation/evidence record, not new approved tokens or visual authority. Product is unchanged; both original and appended boundaries keep User Acceptance NOT_GRANTED. The whole project DESIGN.md file is **not** claimed unchanged. | PASS |

Behavior evidence: [corrected pre-run Controller readback](baseline-browser-readback-v2.json), [independent post-run Controller readback](controller-after-readback.json), and [native supplemental verification](producer/artifacts/verification.json). These browser checks support their listed copy/actions/geometry and state claims, not a comprehensive accessibility certification.

## Observation timing and exact source binding

Native rollout image calls/results: before37/41, refined69/73, states and optional widths86/94. The compact observation record includes exact call/result IDs, timestamps and SHA-256 of each returned image payload; all ten returned PNGs match the curated files byte-for-byte. This establishes actual image delivery, not merely screenshot creation.

After those images the Producer appended the Design evidence record and made an indentation-only HTML patch at106/110. Removed/added HTML lines are identical after trimming; no visual choice changed in that patch. The Controller then rendered the final source after process exit. Its final PNGs are byte-identical to the earlier Producer refined PNGs:

- Desktop: `7cdb0fae3668955d8226818f80ec9ded2ace1194d3fac961c853e8d157381fed`
- Mobile: `f82bc55f7b01d47d0090d9eaa2425d5bf77fa3d882a63c4a41bab490e246a007`

This closes the final-source/render binding without falsely describing the Controller rerender as another autonomous Producer observation.

## Existing gates, preservation and interpretation

The existing seven-file suite was executed once at the start and once at the end: **baseline64 PASS /0 FAIL; final64 PASS /0 FAIL**, with0 cancelled/skipped/todo in each. Durations were310.7639ms and259.4326ms respectively. Full outputs are [baseline-contract-tests.txt](baseline-contract-tests.txt) and [final-contract-tests.txt](final-contract-tests.txt); the manifest/current review supplement binds them by exact hashes. The three evidence categories and limitations are explained in [evidence-reporting.md](evidence-reporting.md).

All262 baseline tracked files other than the permitted current `review-evidence.json` are byte-preserved, including existing tests, scenarios, saved semantic responses, Smoke I, doctrine, historical reports and failures. The current review receives only an additive supplement field; no old field value is replaced. Existing semantic and Smoke I evidence is **reused, not rerun**, because package/scenario bytes are unchanged.

Shipped package SHA-256, unchanged in both repository and native input:

- `SKILL.md`: `2440962d1be29e8274722efa86d8271327206ecdef9e9566bd30fc226002cc04`
- `templates/DESIGN.md`: `4ac8586fad0a8f964d4ace550f2706af49df0403f3618a5214dd17b98ee1c237`
- `agents/openai.yaml`: `c28a9f5e01c3ab39a5518c35d6cd6c41629f15edbadf696948339e58262e15c1`

## Known diagnostics and limits

One native custom-tool patch rejection is preserved, not erased: call49/result51 rejected delete/add operations targeting the same CSS path. The same invocation corrected patch construction at55/59. The collector's zero failed **subprocess** executions must not be reported as zero overall tool errors. Exact failed/retry inputs and outputs remain in [producer-tool-records.json](producer-tool-records.json).

Two pre-run Controller diagnostics and one post-run curation diagnostic are preserved separately in [preflight-diagnostics.md](preflight-diagnostics.md) and [curation-diagnostic.md](curation-diagnostic.md). They are tooling failures with recorded resolutions, not invented Product failures. No unresolved mandatory Product/visual failure was observed in this case.

Unverified/out of scope: other products, runtime repetitions, causal contribution of individual clauses or JOEDESIGN versus bare Astra, competitive advantage, general design competence, other browser/platform/forced-color rendering and exhaustive accessibility. The one fictional task, fixed Product data and APPROVED intent constrain the conclusion. User acceptance remains not granted, not a missing technical gate. Program Lead alone determines Composition closure, Bridge closure, Pure Core Freeze and competition readiness.
