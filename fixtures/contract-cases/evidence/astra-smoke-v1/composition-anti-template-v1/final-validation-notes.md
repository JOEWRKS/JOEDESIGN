# JOEDESIGN Composition / Anti-template Core v0.1 — final validation snapshot

## Status and scope

`JOEDESIGN_COMPOSITION_ANTI_TEMPLATE_CORE_READY_FOR_PROGRAM_REVIEW`

This is a validation-only readiness status. It means the approved Composition / Anti-template gates through the final static suite are evidenced and ready for Program review. It does not claim that whole-branch Program review, push, remote-equality readback, phase closure, competition readiness, or User Acceptance has happened. The controller owns those later delivery checks; Program Lead alone may declare the core CLOSED.

- Repository: `JOEWRKS/JOEDESIGN`
- Branch: `codex/joedesign-v0.1-composition-anti-template-core`
- Final-gate source HEAD: `026a679d68e1e8a78347d64261c08dfe246d91a5`
- Final-gate source tree: `429c0a681aea9d398b1b786137f7ecf152aa6345`
- Worktree immediately before the final gate: clean
- Final-evidence commit identity: intentionally not embedded in a file that participates in that commit; the external Task 5 report and controller handoff record the resulting commit/tree/clean readback.
- Product Truth: unchanged / PASS for the bounded Smoke I fixture
- APPROVED DESIGN: unchanged / PASS for the bounded Smoke I fixture
- User Acceptance: `NOT_GRANTED`

## Exact ordered gates

1. Task 1 baseline: `56 PASS / 0 FAIL`; preserved at `baseline-tests.txt`.
2. Task 1 expected RED: `0 PASS / 8 FAIL`; preserved at `composition-red-tests.txt`. The failures were the eight missing Composition contracts before runtime changes.
3. Task 2 minimal runtime/template implementation: Composition `8 PASS / 0 FAIL`; preserved at `composition-green-tests.txt`.
4. Task 3 fresh supplied-choice semantic replay: one actual `gpt-6-astra` / `xhigh` run, `14 PASS / 0 FAIL`; exact native response, observed record, focused output, and sanitized provenance are preserved.
5. Task 3 post-semantic seven-file suite: `64 PASS / 0 FAIL`; preserved at `post-semantic-contract-tests.txt`.
6. Task 4 Smoke I: one actual `gpt-6-astra` / `xhigh` native run. Candidate 01 FAIL remains immutable; corrected candidate 02 establishes final I1–I9 PASS.
7. Task 5 final seven-file suite: run once through the exclusive capture helper, `64 PASS / 0 FAIL`; preserved at `final-contract-tests.txt` (SHA-256 `7b038b3ce4696e26f4fdf3e938c95a3519c08b3e8abffb367d6792b010344f15`, 5653 bytes).

Final static breakdown: 16 process/authority, 8 spatial craft, 8 typography/scale, 8 reference intelligence, 8 color/contrast, 8 imagery/focal, and 8 composition/anti-template; all 64 pass.

## Fresh semantic evidence

- Result: `14 PASS / 0 FAIL`, one supplied-choice run rather than fourteen scenario executions.
- Source implementation: `100f24bbe90cedf1b0b6d261e571aa372b290949`.
- Runtime: `gpt-6-astra`, `xhigh`, codex-cli 0.153.4.
- Thread: `01a0774d-d28b-7a40-b0ff-2e21f77b3331`.
- Exit: 0; wall time 47183ms.
- Rollout SHA-256: `1bfd94624e2b9ba58e978b63de13a297ae888347f1a111a6981e7d49be9770ad`.
- Expected actions and repository tests were not supplied to the producer; current `decisions.json` remains byte-identical to the frozen case input.
- Shipped package bytes remain unchanged since `100f24b`, so the semantic result remains bound to the package used by Smoke I and the final gate.

## Smoke I actual render evidence

- Product: fictional neutral Incident Decision Brief with one summary, severity/status metadata, findings 1→2→3, one primary action, and one secondary evidence link.
- Runtime: one actual `gpt-6-astra` / `xhigh` invocation, thread `01a0775f-4777-7f33-bf60-1fb0d3b05c75`, exit 0.
- I1 PASS: byte-exact structural map creation at rollout line 58 completed before first implementation edit at line 66.
- I2 PASS: title/summary, ordered evidence, and action are the first, second, and third visual destinations.
- I3 PASS: containers correspond to semantic grouping; the unjustified equal-card wall was removed.
- I4 PASS: decorative split/blob/pill defaults no longer own hierarchy; retained ordinary motifs have Product reasons.
- I5 PASS: the three equivalent findings repeat while introduction, evidence, and action vary by role.
- I6 PASS after preserved candidate 01 failure: restrained desktop label rail and content/action column establish intentional rhythm; final finding text and primary action align at x=456.
- I7 PASS: mobile moves labels above content and stacks controls while preserving priority and order rather than shrinking desktop coordinates.
- I8 PASS: Product and APPROVED DESIGN bytes, visible content, ordered findings, action behavior, evidence link, and initial output remain unchanged.
- I9 PASS: User Acceptance remains `NOT_GRANTED`.
- Desktop actual target and final full-page render: viewport 1440×1000, PNG 1440×1000.
- Mobile actual target and final full-page render: viewport 390×844, PNG 390×869; ordinary vertical scrolling is required and horizontal overflow is absent.
- Native checks: 25 passed / 0 failed. Controller browser checks: 12 passed / 0 failed. These are bounded checks, not an exhaustive accessibility certification.

## Repository and package boundary

- Public entrypoint count: 1 (`skills/joedesign`).
- Competitor dependency count: 0.
- Shipped runtime dependency count: 0.
- BIO exposure count: 0.
- `skills/joedesign/SKILL.md`: SHA-256 `2440962d1be29e8274722efa86d8271327206ecdef9e9566bd30fc226002cc04`, 21484 bytes.
- `skills/joedesign/agents/openai.yaml`: SHA-256 `c28a9f5e01c3ab39a5518c35d6cd6c41629f15edbadf696948339e58262e15c1`, 207 bytes.
- `skills/joedesign/templates/DESIGN.md`: SHA-256 `4ac8586fad0a8f964d4ace550f2706af49df0403f3618a5214dd17b98ee1c237`, 3743 bytes.
- Existing `tests/joedesign-contract.tests.mjs`: unchanged SHA-256 `19f81e1dd8507920f152425b0144dd1d0b25c3506c13631caf283db5f5e661fc`.
- Existing cases `fixtures/contract-cases/decisions.json`: unchanged SHA-256 `02b51d785c6e8ccbadc40d3949f0fbf38002581c6424265b5c3f4925b15f8b80`.
- Frozen initial set: all 206 files outside the four authorized mutable paths match the starting snapshot exactly.
- Shipped raw rollouts, event/launch/exit payloads, isolated homes, credentials, validation helpers, browser dependencies, and dependency trees: 0.
- Current review inventory covers every current Composition phase file, all 40 Smoke I packet files, current observed/cases, and both byte-exact prior-current archives. `review-evidence.json` explicitly excludes its own self-hash.

## Preserved failures and diagnostic history

- The generic Smoke I baseline defect remains preserved as source and actual desktop/mobile images.
- Candidate 01 remains preserved as FAIL because desktop finding text started at x=456 while the action started at x=432, contrary to the pre-edit shared-start-line intent. Candidate 02 changed only the bounded action/output inset and mobile reset; no shipped runtime changed.
- Task 4 default `git diff --cached --check` reported 33 CRLF lines in the exact native `before-manifest.json` as whitespace errors. A command-local `core.whitespace=cr-at-eol` check passed. Bytes were preserved and repository configuration was not changed.
- Task 2's unquoted PowerShell `HEAD^{tree}` read-only command failed; quoting the revision corrected the diagnostic with no mutation.
- Before Task 5, the controller guessed a nonexistent audit helper name, then located the actual read-only `audit-i.mjs` with `rg`; no mutation or gate failure occurred. The Task 4-only helper is intentionally not reused after refreshing current review metadata because its unchanged-review assertion would no longer apply.
- Task 5's first supplemental inventory-set verifier used an incorrect escaped Windows separator literal and reported an inventory mismatch. The corrected read-only `path.sep` normalization verified the exact 54-path set and every indexed hash/byte count; no repository mutation resulted from the failed diagnostic.
- Historical RED/output and the archived prior current review retain their original bytes and status, including the old NOT_READY pre-push snapshot. They were not rewritten to imply current readiness.

## Rulings carried from the execution ledger

1. Ruling: use the approved canonical design and five-task implementation plan without renewed brainstorming approval — the user explicitly directed execution — cost if wrong: bounded rework with failures preserved.
2. Ruling: keep plan scratch/ledger and isolated runtime outside the repository — contract 16 scans ignored files and no `.superpowers` runtime surface may enter the checkout — cost if wrong: reduced scratch discoverability, mitigated by the external ledger.
3. Ruling: treat Task 1 Step 3 as read-only and leave the existing contract test unchanged — the latest explicit allowlist override controls — cost if wrong: a preserved baseline failure.
4. Ruling: run the exact bounded RED/GREEN, unchanged fresh fourteen-case replay, and actual Smoke I sequence without added no-guidance variants or repeated microtests — the user-defined validation scope controls — cost if wrong: the evidence does not establish causal superiority or generalization beyond the observed fixture.
5. Ruling: preserve local validation provenance and the external ledger instead of deleting the plan workspace — failure evidence preservation controls — cost if wrong: bounded local disk use; only curated evidence ships.

## Known failures and unverified boundaries

Known failures are the expected Task 1 RED, the deliberate initial Smoke I defect, and preserved candidate 01 alignment failure. All are resolved by later bounded gates without rewriting their history. The command-line diagnostics above are not product or render failures.

Unverified and unclaimed: exhaustive accessibility and assistive-technology behavior; other browsers, devices, viewports, and themes; user acceptance; production incident behavior; statistical stability; causal or comparative superiority; competition closure/readiness; phase closure; controller whole-branch review; push; and remote equality. Semantic evidence is one supplied-choice replay, not per-scenario execution. Product and APPROVED DESIGN are fixed; User Acceptance is not granted.

## Controller handoff

The controller must independently review the Task 5 diff and final evidence commit, then perform any authorized non-force push and remote-equality readback. This snapshot does not claim those future actions were performed.
