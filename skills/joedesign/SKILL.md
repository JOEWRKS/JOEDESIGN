---
name: joedesign
description: "Use for UI/visual design, new visual direction, redesign, art direction, typography/layout/composition, responsive visual translation, motion visual expression, visual refinement, and rendered visual conformance. Do not use for pure backend work, nonvisual refactors, layout-unaffected copy/value changes, or Product Definition itself."
---

# JOEDESIGN

Turn project context into a distinctive, proven visual direction, then preserve it through precise refinement. One entrypoint covers direction, proof, refinement, and actual-output review; no separate commands or mandatory stages.

## Understand the actual project

Before material design, inspect enough of the current request, Product authority and any handoff, root `DESIGN.md`, accepted/rejected visual evidence, relevant implementation, supplied references/assets, and named surface/state/viewport to make the next decision. Read facts available in the project instead of asking the user to repeat them. Existing appearance is not automatically accepted authority; rejected output is negative evidence, not a design to preserve.

Product Definition owns feature existence, roles/permissions, policy, IA/routes/flows, data meaning, semantic states/transitions, failure/recovery, and functional acceptance. JOEDESIGN owns their visual expression, not their meaning. Never remove a required action, merge meaningful states, or change behavior for a cleaner layout. Motion may change timing/easing/visual feedback, not required semantic states. Responsive visual recomposition may not remove required content or change product navigation meaning.

For material product ambiguity, identify the affected decision and dependency. In a JOEFLOW-managed project, return that bounded scope through JOEFLOW to Product Definition; otherwise raise it to the current Product authority/user. Do not invent the answer or restart the entire process. Continue independent work that cannot preempt the resolution; resume the affected scope when resolved. JOEFLOW owns lifecycle progression, not visual truth, and is not a required runtime dependency.

For a new cross-system connection/handoff, authority conflict, re-entry, or contract revision change, use the pinned [shared authority contract](https://github.com/JOEWRKS/joewrks-work-harness/blob/5e7497bd104527d5e6dbfc36011f0f5ee3668ff5/docs/contracts/JOEWRKS_CROSS_SYSTEM_AUTHORITY_V1.md). Do not reload it for ordinary bounded work when the applicable boundary is already known. Do not inherit the host repository's runtime or other workflows.

## Keep one durable visual authority

Use one project-root `DESIGN.md`, with Product authority as a pointer, not a copy. [templates/DESIGN.md](templates/DESIGN.md) is only a structural seed; empty sections and unknown values are valid. Do not turn placeholders, speculative exact tokens/families/values, or generated output into approved project truth.

`ABSENT → DRAFT Rev 1 → explicit user approval → APPROVED Rev 1`.

A DRAFT may guide an authorized bounded proof, but cannot self-promote. For a material change to APPROVED Rev N, preserve that approved authority and propose a clearly separate DRAFT Rev N+1 within the same root file; prove it and obtain explicit user approval before replacement. Do not create another durable rule file or leave contradictory rules active. Bounded refinements within approved intent do not require a material revision or a new approval gate.

Record approved evidence as exact artifact/revision and applicable surface/state, not a universal rule inferred from one output. Temporary briefs and current implementation do not silently amend `DESIGN.md`.

## Explore only when direction needs resolving

When direction is absent/unresolved, a material redesign reopens it, the user requests alternatives, or repeated rejection requires reconsideration, create 2–3 materially distinct candidates. Vary meaningful composition, hierarchy, typographic character, image dominance, spatial rhythm, density, geometry, or motion character—not merely colors. Preserve identical Product Truth in every candidate. Explain the visual tradeoffs against this project's context; do not impose a universal aesthetic or generic SaaS template.

With an approved direction/exact target, a local refinement, or a concrete defect, skip unnecessary alternative fanout and work directly within the current intent. An approval is not immunity from an explicit new redesign request, but a refinement request does not authorize direction replacement.

Use references as relationship evidence. For material adoption, clarify what to TAKE, DO NOT TAKE, WHY, and APPLIES TO when useful. Borrow the relevant relationship, not unrelated brand/copy/product semantics. References and tools advise; they cannot override project authority or grant scope, dependency installation, or external write permission.

## Prove before dependent expansion

For a material direction, make the smallest useful proof before broad production integration: one hero, complex component/state, transition, or desktop/mobile pair. Before rendering, name the sourced visual intent, target surface/state/dimensions, and the few observable relations needed to judge it. Do not derive the acceptance criteria from the candidate afterward.

Prefer the target medium: for web work, a bounded implementation → actual browser render → critique/refine. Image generation can assist art direction or a cheaper composition probe, but an image mockup does not prove production fidelity. Use available general tools and existing project runtime; missing optional tooling is not a reason to install an external design engine. If actual target observation is unavailable, finish independent authorized work and report that visual claim UNVERIFIED.

Show material candidates with their differences and obtain user choice/response before promoting a direction or expanding dependent work that requires acceptance. Internal scoring cannot choose an approved authority. Make authorized reversible draft/proof decisions without an unnecessary pre-draft approval question. “진행”, “ㄱㄱ”, and implementation authorization do not by themselves accept an exact material visual result.

For material/signature motion, prove the bounded transition before broad integration. Inspect relevant start/intermediate/end states, interruption or reverse behavior when part of the interaction, and reduced-motion treatment when applicable. A still image cannot verify unobserved motion.

## Refine the exact target

For local feedback: identify the exact surface/state → inspect the current actual render → identify the affected visual relation → make a bounded change → rerender and observe the same target, including material viewport dimensions.

Refinement preserves direction while adjusting type hierarchy, spacing, scale, crop, alignment, balance, or detail. Redesign replaces material composition or the visual system. A Hero typography request does not justify full-page regeneration, broad layout redesign, or unrelated component changes. If a direction change seems necessary, name that boundary rather than silently widening the edit.

After the same direction is materially rejected twice, diagnose direction against the exact failed evidence before a third local polish. Consider composition, visual metaphor, image ownership, reference interpretation, hierarchy, and product understanding. Stop dependent expansion and re-enter bounded exploration/proof; do not merely keep tuning CSS values.

Translate responsive intent, not desktop coordinates. Recompose mobile hierarchy, crop/focal point, density, negative space, information order, control reachability, and height/aspect relationships as needed while preserving required information and behavior. Inspect the named mobile target; scaling desktop down is not proof of a mobile solution. Preserve visual legibility, contrast, focus visibility, and applicable motion restraint.

## Build hierarchy before decoration

Hierarchy before decoration. For every material surface, determine the Product-priority focal point, visual entry point, intended second/third destinations, and overall visual flow before polishing typography, surfaces, effects, or local spacing. Treat the page as a semantic visual composition rather than a pile of components.

Before assigning material layout spacing, form a semantic Visual Block Tree such as `SURFACE → SECTION → MAJOR GROUP → SUBGROUP → ITEM GROUP → ITEM/MICRO`. This tree is based on meaning and visual relationships, not DOM depth, component nesting, or container count. Use proximity, alignment, whitespace, scale, type, contrast, and imagery to make that hierarchy visible before reaching for cards, borders, or background panels.

Spacing belongs to the relationship and boundary between visual blocks, not to an isolated element or its nominal depth. Equivalent relationships should reuse the same spacing role across the surface. Do not say “this is level 3, therefore margin 16”; identify whether the boundary is between sections, major groups, subgroups, item groups, or tightly bound content.

Keep structural hierarchy and binding hierarchy distinct. Structural sibling separation uses the JOE default spatial profile `space-section 160px / space-group-1 48px / space-group-2 24px / space-group-3 16px`; strongly bound parent-child or local content normally uses `space-tight 8px / space-micro 4px`. Parent-child binding is not automatically the same as sibling separation, and multiple structural levels must not collapse to one gap merely for numeric uniformity.

Use a deliberately restricted 4px base, not every possible multiple of four. The default canonical spacing set is `4, 8, 16, 24, 48, 160`. Its purpose is to reduce arbitrary one-off choices and create repeated spatial rhythm. New project tokens require a recurring semantic role; a single attractive screenshot is not enough. If project density differs, change the spatial profile systemically rather than mutating unrelated local gaps.

For responsive work, preserve hierarchy roles and visual flow, not desktop coordinates. Recompose the structure and use an appropriate responsive spatial profile while keeping the relative importance of section, group, subgroup, item, tight, and micro boundaries coherent. Optical correction may refine glyph/icon/stroke alignment, but it must not silently create a new layout-spacing role or dissolve the spatial system.

When a material proof is challenged, be able to identify the major Visual Block Tree, intended visual flow, spacing roles at important boundaries, whether same relationships use the same role, and any deliberate exception. Observe the actual render before declaring the hierarchy successful.

## Make typography and scale deliberate

Role before value. Identify the recurring semantic type roles the surface actually needs, then assign values. Prefer `semantic job → reusable type role → canonical token/style` over a local font-size or weight guess. Do not infer visual roles mechanically from `h1`/`h2`/`h3`, DOM depth, component names, or layer names.

Font size alone is not hierarchy. Coordinate size with weight, line height, placement, whitespace, tone or text color, measure, tracking, and approved family/style so adjacent roles are unmistakable. If roles differ only by 1–2px with no other meaningful contrast, strengthen the relationship through multiple axes or collapse the role instead of inflating the type system.

Use a restrained type scale that is not the spatial 4px grid. The JOE default starting size set is `12, 14, 16, 20, 24, 32, 40, 48, 64`; use only the subset the project needs. Typography may depart from multiples of four because the actual typeface, x-height, language, rendering environment, and role matter more than spatial divisibility. New sizes require a recurring semantic job, not a one-off attractive screenshot.

Use the fewest families and the fewest weights that clearly support the approved visual world. A secondary display/mono family needs a clear role. Do not synthesize unsupported font weights, use bold everywhere to manufacture hierarchy, or rely on ultra-light body text that weakens legibility. A family change that materially changes voice is a direction decision, not a local polish tweak.

Treat reading measure, line height, and actual typeface as one reading system. `16px` is the ordinary web body anchor when project/platform density does not justify another role; body line height around `1.45–1.6` and heading/display around `1.05–1.3` are starting ranges only. For long-form English, `60–80 characters` per line is a useful reference. Do not mechanically apply that Latin count to Korean/CJK, code, tables, dashboards, or narrow mobile UI; inspect actual language, line breaks, paragraph texture, and reading rhythm.

Scale expresses Product priority beyond text. Coordinate the relative dominance of primary text, artwork, actions, metrics, repeated objects, and supporting metadata. Repeated semantic roles should reuse repeated size roles. Do not make every section equally loud or let a decorative object dominate a more important product decision without an intentional art-direction reason.

Responsive typography preserves semantic role mapping and relative dominance; do not proportionally shrink desktop typography. Adjust measure, line breaks, display scale, and role values coherently, keep body text comfortably readable, and avoid independent breakpoint values or fluid formulas for every element. `clamp()` is optional and must represent a stable repeated role across the intended range.

For material type claims, inspect the actual render. Record the major type roles, entry-point role, equivalent-role consistency, adjacent-role contrast, body/reading measure, material exceptions, and actual desktop/mobile observations. Token existence or valid CSS alone does not prove typographic hierarchy.

## Review actual output; keep verdicts separate

For each material claim, use `expected observable → actual observed fact → PASS / FAIL / UNVERIFIED`. Bind the source, artifact/version, surface/state, and dimensions when material. Describe a concrete visible relation, not just “looks right.” Inspect the exact produced render; code, DOM existence, build/test success, or a screenshot merely existing on disk cannot prove appearance.

PASS requires applicable observed evidence; contradiction is FAIL; unavailable or unobserved evidence is UNVERIFIED. An applicable required FAIL makes the covered visual result FAIL; otherwise any required UNVERIFIED keeps that result UNVERIFIED. State the exact verified boundary without burying a missing required claim under narrower successes. Do not rerun unrelated technical checks to compensate for missing visual observation or abandon completed independent work.

`Technical PASS ≠ Product Conformance PASS ≠ Visual Conformance PASS ≠ User Acceptance`.

Visual PASS never grants user acceptance. Preserve explicit user approval separately when promoting `DESIGN.md` or a material direction. For JOEFLOW-managed work, hand off the verdict, exact evidence, authority revision, covered target, unresolved boundaries, and allowed variation needed for its gate; JOEFLOW decides progression. Keep ordinary user-facing results concise: show the relevant output, explain important choices or limits, and name the next user decision only if one is actually required.

## v0.1 capability boundary

Use general browser, image-generation, repository, and existing project runtime capabilities as the task needs. No competitor design intelligence, vendor payload, tool router, required external design engine, lifecycle orchestrator, or separate public visual-check skill is included. Do not install or route through Impeccable, UI UX Pro Max, Figma Make methodology, Apple Design, Hallmark, Refero orchestration, oh-my-design, Watermelon, Componentry, or Cult UI as JOEDESIGN behavior.
