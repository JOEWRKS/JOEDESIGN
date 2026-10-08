---
name: joedesign-harness
description: "Use for reference-grounded material UI design or redesign needing scoped synthesis, visual proof and evidence-bound review. Coordinates JOEDESIGN and targeted UI specialists; not a visual style or backend workflow."
---

# JOEDESIGN Design Harness

Design quality is the primary objective. Start from Product authority, approved
DESIGN.md and originals, real content/assets, and the current implementation.
Use `joedesign` for visual translation; this skill coordinates the work and its
evidence. A reference, specialist recommendation or draft cannot replace an
approved project decision or the user's exact acceptance.

## RACI is the work route

For each material finding, identify its claim and route before review. The first
role (R) makes the observation and draft judgment. The second (C1) checks that
same result from its own expertise. In a recorded conflict, uncertainty or
recurring failure, involve the third (C2) for diagnosis. C2 cannot vote away a
FAIL. The implementation lead remains accountable for the integrated scene and
code; Harness owns procedural gates, Product authority owns meaning, and the user
owns exact visual acceptance. Inform affected roles of the result and limits.

Follow the [category routes and evidence contract](references/operation.md#raci-as-the-work-route).
For a bound claim, `python <this-skill>/scripts/harness_cli.py raci <run-dir>
--claim-id <id>` prints the work assignment; it does not execute it.
Read the applicable specialist skill, inspect the actual target, and record the
skill source/version, context and observation. Skill names in a matrix are not
execution evidence, and reading several skills in one context does not create
independent reviewers. The CLI checks the planned role order locally; it counts
actual reviews only when a trusted host attests skill use and sequence. This package
has no such host adapter:
local checks remain UNVERIFIED and cannot issue final APPROVED.

## Produce and test the difficult slice

1. Scope the actual content, actions, states, constraints, assets and target
   viewports. Run `python <this-skill>/scripts/harness_cli.py --help`; read
   [operation and artifact contracts](references/operation.md) before initialization.
   For handed-off priorities, notice density or design-system work, follow
   [Product meaning to visual roles](references/operation.md#product-meaning-to-visual-roles).
   The design owner maintains the scoped visual system in the existing root
   DESIGN.md; review information completeness and visible hierarchy separately.
2. Retrieve OMD only for a concrete open reference decision. OMD is data, not
   authority or a visual-quality ranking. Inspect the chosen original yourself;
   use one Primary and at most two Secondary references with distinct axis owners.
   Map each adopted source relationship to product meaning, spatial/responsive
   implementation and a result that could disprove the choice.
3. For a new or materially revised direction, use [visual production](references/visual-production.md)
   to choose and prove the focal asset, composition and transition at display scale.
   An approved local repair needs only affected guidance. Build the hard target
   state and narrow layout before dependent expansion.
4. Use the CLI's synthesis, contract, state matrix and scoped proof gates. Observe
   the whole screen and required interaction sequence in the target runtime.
   Structural failure returns to synthesis; repeated failed local repair requires
   a new diagnosis. `bundle ... expand` needs current structural and visual proof,
   not merely a capture set or passing technical checks.
5. Route findings through RACI, then use a fresh-context `critic` for independent
   internal diagnosis. Keep conformance, whole-screen quality, function,
   technical checks and user acceptance separate. Preserve failed candidates and
   exact build/state evidence. Report unsupported claims as UNVERIFIED.

Exact user rejection remains REJECTED for that output; implementation permission
such as “진행” or “ㄱㄱ” is not visual acceptance. A provisional focal asset, static
motion still or uncalibrated critic cannot establish finished quality. Present the
actual result and dominant unresolved gap without claiming that a local CLI run
authenticated skill use, visual success or user approval.
