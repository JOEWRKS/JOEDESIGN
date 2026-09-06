# Color / Contrast validation notes

These notes preserve controller rulings and bounded operational diagnostics that are relevant to review. They do not convert intermediate diagnostics into current gate failures or reconstruct unavailable output.

## Rulings

- Use a sibling Git worktree and external validation scratch instead of repository-local `.worktrees` or `.superpowers` directories. Rationale: this repository enumerates every file, including ignored paths, and production/main had to remain unchanged. Cost if wrong: local workflow placement differs from generic defaults, with no shipped behavior impact.
- Exclude the exact root `.git` metadata file as well as descendants of `.git` directories in contract 16. Rationale: a linked worktree represents `.git` as a file, and metadata must not be mistaken for vendor/runtime surface. Cost if wrong: a file named exactly `.git` is metadata-exempt while every nonmetadata path remains exact-allowlisted.
- Use the user-requested eight direct source contracts rather than adding generic baseline or micro-test experiments. Rationale: fresh semantic replay and Smoke G independently cover behavior. Cost if wrong: static RED does not prove bare-model behavioral failure, and no such causal claim is made.
- Preserve the byte-exact native Smoke G final transcript and add a compact repository-relative links companion; name the controller authority precisely as `DESIGN.md` (`Status: APPROVED`). Rationale: rewriting native output would damage provenance, while reviewers need portable links and an unambiguous authority name. Cost if wrong: one additional compact evidence artifact; transient absolute links remain only in the labelled historical native transcript.

The approved sequence `RED -> minimum implementation -> Color 8/8 -> fresh semantic 14/14 -> full 48/48 -> Smoke G -> final 48/48` is recorded as explicit user direction, not an inferred controller ruling.

## Operational diagnostics and preserved failures

- The isolated worktree initially produced `39 PASS / 1 FAIL` because contract 16 treated linked-worktree `.git` metadata as runtime/vendor surface. The narrow metadata handling above resolved that setup-specific diagnostic without broadening the nonmetadata allowlist.
- Genuine preimplementation Color RED was `0 PASS / 8 FAIL`; its exact output is preserved in `color-red-tests.txt`.
- The first focused implementation run reached `7 PASS / 1 FAIL`. The failed accent-loudness assertion is known, but the complete tool output was truncated and no byte-exact full artifact remained. `color-intermediate-tests.txt` records that limitation; omitted output is intentionally not reconstructed.
- A supplementary ad-hoc semantic comparison read a nonexistent `expectedActions` property and printed `0/14`. It changed no files and is not the canonical result. The unchanged fixed `expectActions` map in the five-file suite passed all 14 supplied-choice scenarios.
- Native Smoke G first attempted to read a literal `APPROVED DESIGN.md`, which did not exist. It recovered by reading the actual `DESIGN.md`, verified `Status: APPROVED`, and left authority bytes unchanged. The bounded diagnostic is preserved in `smoke-g/native-intermediate-failure.md`.
- `git diff --check` reports trailing-blank-line warnings in byte-exact native `before-contrast.md` and `after-contrast.md`. Those artifacts remain unchanged to preserve native provenance; authored evidence files are checked separately.
- A Task 3 archive attempt from the external validation directory used repository-relative paths and copied nothing; the later absolute-path archive succeeded and was hash-verified. A cleanup/archive command and two later empty-directory cleanup attempts were rejected before execution, with no repository effect. A trailing Git status check from that external nonrepository directory returned the expected diagnostic.
- During final integration, an initial read used the misspelled parent `D:/JOEWORKS` rather than `D:/JOEWRKS`; it failed before any repository action and was immediately corrected.
- After the first evidence commit, the independent verifier passed, but adjacent Git identity/status commands were issued from the external nonrepository validation directory and returned the expected `not a git repository` diagnostic. No repository state changed; the commands were repeated from the worktree for final readback.

## Current boundaries

Current PASS claims remain limited to one fresh supplied-choice semantic sample and one neutral actual-rendered Smoke G in Chrome 152.0.7977.76: base, hover, keyboard focus, and anchor-target focus at desktop 1440x1000 and mobile 390x844 (full-page mobile image 390x985). User acceptance is `NOT_GRANTED`. Other browsers, themes, viewports, full WCAG certification, production behavior, statistical superiority, Program Lead approval, competition readiness, and `COLOR_CONTRAST_CORE = CLOSED` remain unverified or unclaimed.
