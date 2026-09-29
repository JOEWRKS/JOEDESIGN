# RACI route and instruction audit — 2026-09-30

The user's current direction makes RACI the Harness work route. This change is
separate from the rejected production-relationships extension recorded in
`retention-decision.md`; it does not claim better design output from that A/B.

The main `SKILL.md` previously repeated the category-role list, artifact and
receipt details, repair rules, and quality caveats already present in
`references/operation.md` and `references/visual-production.md`. It now states
only the governing R→C1→conditional C2 process and when to open those references.
Whitespace word count fell from 951 to 558 (106 to 63 lines). The old design
spec's detailed priority table assigned conflicting third reviewers for some
claims; it now links to the runtime category route as the single executable
source. The JOEDESIGN core and third-party specialist skill files were unchanged.

The matrix validator requires the ordered route. Review assessment requires
host-issued review sequence and a separate specialist `skill_use` receipt tied
to the claim, source hash, context, run, build, and snapshot. A role label alone
remains UNVERIFIED; attested R/C1 conflict requests C2. The `raci` CLI prints an
assignment with `execution: UNVERIFIED`, not a completion claim.

Validation: Python unittest suite 80/80, Node v0.2 regression 14/14, skill
quick validator passed, and `git diff --check` passed. These tests use a
synthetic FixtureHost. The shipped CLI has no authenticated host adapter, so
actual skill invocation, visual quality improvement, and user acceptance are
still unverified.
