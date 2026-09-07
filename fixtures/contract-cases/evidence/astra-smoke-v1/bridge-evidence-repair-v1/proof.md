# Bridge execution-evidence repair

Resolution: **RECOVERED_EXISTING_RUN**. New semantic replay invocations: **0**. This packet repairs identity/provenance metadata only. It does not implement Bridge, repeat Composition validation, rerun Smoke F, grant user acceptance, close Bridge, freeze Pure Core, or determine competition readiness.

Pinned repository baseline: `20953484ec089e3ebd1e0912233cd1fb08f23bc4`; tree `1211dc6cf5744fcbc60a2f93bbfe92c5a951350b`. Work branch: `codex/joedesign-v0.1-bridge-evidence-repair`.

## What was corrected

The original current observation file explicitly described its `threadId` as a controller correlation UUID, but put it in the native runtime identity field. Its `rolloutSha256` equaled the formatted final-response file hash, not an execution-log hash. The existing provenance already documented some limitations. The correction does not reclassify the original result as fabrication or rewrite its diagnostic history.

| Identity / artifact | Correct value and meaning |
| --- | --- |
| Actual child execution/thread ID | `01a077af-6ed8-7cd2-929b-88e8383ab663`, independently present in child `session_meta.id` and parent `SubAgentActivity.agent_thread_id` |
| Parent/root runtime session namespace | `01a02fbe-0a39-76c1-bda3-075f0ba74d9f`, separately retained; not the child execution ID |
| Correlation UUID | `19d3ff97-553b-4745-b8ff-91282d218d6a`, historical Controller label only, not a native session ID |
| Actual child execution-log SHA-256 | `065e43afeafecd5fff08f41ad09d1ca0b25ea0df143de4c8aa7ccb1b85444026` —309780 bytes,35 records |
| Existing formatted final-response SHA-256 | `9a2df0bb641bbd820263b9fe7919e77bc374bcd4e28e300b42143d4f82958938` —4931 bytes; original file unchanged |
| Exact native final-message SHA-256 | `478afe7393ff8dd7e0ce5ce7c99ac87ac23e23f6554bc8a20abf3f94416c6648` —4410 bytes; recovered without an added newline |

The actual execution log is the stable child rollout, not the much larger supporting parent log or a sanitized excerpt. Repository-relative excerpts have their own manifest hashes and are not mislabeled as raw rollout hashes.

## Recovered input → execution → output chain

1. Parent spawn metadata records fresh `fork_turns:none`, `gpt-6-astra`, `xhigh`, task `bridge_semantic_14`. The matching parent activity/result binds that task to the child ID above. Child session metadata binds the same canonical task and parent.
2. Child actual `turn_context` records at lines8 and24 independently report `gpt-6-astra / xhigh`. CLI version is `0.153.4`. The original replay has two turns in one child thread, not two new replay sessions.
3. The only recorded child custom-tool call, line11/result14, runs `Get-Content -Raw` for `skills/joedesign/SKILL.md` and `fixtures/contract-cases/decisions.json` in the JOEDESIGN Bridge worktree. Its complete delivered text is preserved in [input-readback.txt](input-readback.txt). It equals the two exact Git-file contents plus the two PowerShell CRLF output terminators. Both inputs match source commit `ce8dff818088a4925bb7e138bdb4a20a61c81abc`, pinned baseline and current bytes.
4. The exact final response at line32 is preserved as [native-final-response.json](native-final-response.json). Parsed JSON is identical to the unchanged [existing semantic-final.json](../implementation-bridge-v1/semantic-final.json); all14 responses/actions/reasons also equal the archived pre-repair observation record. No response is regenerated, corrected or selected from a new session.
5. The initial singular `action` / `rationale` answer is retained as [native-initial-response.json](native-initial-response.json). It is the historical schema diagnostic, not a newly invented semantic failure score. Parent `send_message` and `followup_task` deliveries before the second answer are retained as bounded metadata/hash bindings.

See [runtime-provenance.json](runtime-provenance.json), [execution-excerpts.json](execution-excerpts.json) and [input-output-linkage.json](input-output-linkage.json) for exact record lines, timestamps, call IDs, input hashes, response hashes and equality results. Local raw-log paths are supplementary locators; the necessary safe metadata, complete input readback and both public answers are repository-reviewable.

The native root cwd and `session_meta.git` describe `JOEWRKS-Product`, the parent task's context, **not** the JOEDESIGN implementation commit. The explicit tool workdir and byte-matched delivered files establish which JOEDESIGN inputs were used. No Product repository content or branch is changed by this repair.

## Exact verification boundary

The three parent/child message bodies are encrypted in the stored logs. Their ciphertext is byte-identical across parent arguments and child delivery, so delivery linkage is verified without exposing or decrypting it. The plaintext request/correction content is **not recovered**. The original account that those corrections were schema-only and supplied no expected answers is preserved as historical reporting; it is not newly attested from plaintext. The observed file-access record contains only the two fixed inputs and no test/prior-response reads. This does not prove absence of every possible contextual influence.

Shared unrestricted filesystem and fresh-context metadata are not OS isolation. These limitations do not turn a response-file hash into a log hash or prevent the verified native identity/input-file/output linkage above. They are not grounds to run a new session when the requested existing-run linkage is recoverable.

## Smoke F: reused, with one additional bounded finding

**REUSED**: zero new model runs, browser renders or visual observations. All12 original Smoke F files remain byte-identical to pinned baseline. Both recorded screenshot hashes, byte lengths and PNG dimensions match the files; Product and APPROVED Design hashes match their existing records. The source/fixture/package did not change in this task.

An additional historical byte-identity claim is incorrect: [old proof](../smoke-f/proof.md) says before and after HTML are byte-identical under hash `2e4b4fe6...`. Actual before is1386 bytes / `2e4b4fe6df7f95dbd0f5bc68324fb86176827e3b6e4496bfd944a9a51f5446dd`; actual after is1385 bytes / `7ee04cc9406d202681b3a1a09ed13007fe55fcf6831c7e22298f83bcc5756b33`. The exact read-only relation is **before = after + one terminal LF byte**. No blanket whitespace normalization or new visual observation is used to hide that difference.

The original proof and both sources are retained unchanged; [smoke-f-reuse.json](smoke-f-reuse.json) supplies separate exact hashes and records the discrepancy. The first recovery helper stopped at this real mismatch; [recovery-check-diagnostic.json](recovery-check-diagnostic.json) preserves the detection and bounded follow-up. This report does not silently expand into Smoke F repair or rerendering, or claim its old byte-identity sentence is true.

Existing F1–F10 remain historical bounded observations, not fresh verdicts here. `status.attention.icon` remains unresolved as originally recorded; no icon-specific claim is added. User Acceptance remains **NOT_GRANTED**.

## Package, originals and contract suite

The original [observed.json](originals/observed.json) and [review-evidence.json](originals/review-evidence.json) are exact pre-repair archives. Original semantic final/provenance, Smoke F, tests, scenarios, expected actions, doctrine, prior failures and all other286 baseline files are unchanged. Only the two permitted current metadata files are corrected; new files stay under this repair evidence root. [preservation.json](preservation.json) records the baseline boundary and hashes.

Unchanged shipped package SHA-256:

- SKILL.md: `d73d1ce3067c6913abe5bd6d562bc87491f20e1b61c64a60cd9f522371715652`
- templates/DESIGN.md: `4ac8586fad0a8f964d4ace550f2706af49df0403f3618a5214dd17b98ee1c237`
- agents/openai.yaml: `c28a9f5e01c3ab39a5518c35d6cd6c41629f15edbadf696948339e58262e15c1`

The documented eight-file suite passed **72/0 at baseline and72/0 after the current observation metadata repair**, with exit0 and0 cancelled/skipped/todo in each. Recovered stored semantic responses match14/14 through the unchanged contract expectations; no fresh replay is implied. Complete command, exit code and actual full output are [baseline execution](baseline-suite-execution.json) / [baseline output](baseline-contract-tests.txt) and [final execution](final-suite-execution.json) / [final output](final-contract-tests.txt). Tests validate existing static/package assertions and stored responses; they do **not** authenticate model identity or execution-log provenance. Runtime linkage was independently established from the recovered records above.

Known diagnostics: original schema correction and earlier Bridge/Smoke failures are retained; the newly found terminal-LF reporting mismatch is bounded and disclosed. Unverified: encrypted prompt/correction plaintext, OS isolation, real-project efficacy, repetition stability, other browsers/platforms/accessibility, user acceptance, freeze/closure and competition claims. No new replay, implementation, expected-answer edit, forced push, merge or PR is part of this repair.
