# Independent implementation review and resolution

Fresh reviewer: collaboration task `/root/harness_final_review`, gpt-6-astra / xhigh.
Reviewed baseline 893e018 through d93a98b, read-only. This is code review, not a visual Critic run.
Seven important findings were reproduced. No minor findings were reported.

| Finding | Correction | Regression |
|---|---|---|
| New build could reuse old capture IDs/reviews | Bind reviews/Critic to run, build and selected capture content hashes | new_build_cannot_reuse_old_review_receipts; changed_capture_bytes_in_same_run |
| Structural findings/repair stop absent from final assessment | Central assessment aggregates findings and repair disposition; transitions consume it | structural_findings_block_assessment; structural_failure_blocks_craft_bundle_and_stage |
| Technical evidence could replace all visual evidence | Category-specific kinds; required render and Product action/state interaction coverage | technical_only_cannot_replace_visual_or_interaction_requirements |
| Historical records made rework permanently stuck | Preserve stale PASS without duplicate current aggregation; attest resolutions of historical FAIL; improved cycles can close | historical_pass_does_not_duplicate_current_review; historical_failure_requires_attested_current_resolution; later_observed_improvement |
| Contract structural claim could become optional | Mandated claims must remain required Structure/render | contract_structure_claim_cannot_be_made_optional |
| Dangling records/additional consultant FAIL ignored | Validate active foreign keys; any unresolved consultant FAIL blocks its claim | dangling_active_records_block_assessment; other_consultant_failure_cannot_be_ignored |
| Second bind write failure left matrix changed | Stage pair, rollback committed replacement, retain backups if OS blocks recovery | bind_second_replace_failure_restores_both_original_artifacts |

Observed RED: 11 regression failures after fixture binding fields were updated.
Additional resolution-kind test exposed technical evidence clearing a structural failure;
fixed within the same review fix pass. Final Python suite: 61 tests passing.
No second independent review was claimed; fixes are verified by reproducing tests and the suite.

## Rulings on reviewer exclusions

- Missing host backend: accepted as an explicit integration limit; complete-tool/readiness
  claims remain withheld. Risk: automatic closure/expansion unavailable locally until integration.
- Aesthetic quality cannot be inferred from text fields: accepted; actual render and user
  evaluation still needed. Risk: well-filled but poor concepts still require human/visual detection.
- Host calibration/fresh context: host must actually enforce these, not trust artifact labels.
  Risk: an incorrectly implemented trusted provider can undermine the policy.
- Malformed inputs causing nonzero failure: fail-closed at the CLI but diagnostics may be rough.
  Risk: some malformed nested records can produce a traceback rather than a field-level error;
  no approval is emitted. Not treated as a pass bypass or readiness evidence.
- Doctor reports file availability only: accepted; installed files do not prove invocation.
