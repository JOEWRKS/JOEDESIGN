# Product Truth — Operations Review Portal

This is a fictional, local-only operational review surface. No production data or operation exists.

## Immutable content and semantics

- Title: Review the next operational handoff.
- Description: Three handoffs are waiting for a status check. Review the current priority before moving to the remaining records.
- One primary action: Review priority item; anchor target #review-r-02. This navigates to the current-priority record; it does not change its state.
- Preserve the three records in the following order, their text, sources, timestamps, status meanings, and current-priority assignment.

| ID | Title | Description | Source | Timestamp (UTC) | Status | Current priority |
| --- | --- | --- | --- | --- | --- | --- |
| R-01 | West depot stock check | The count is ready for the next reviewer. | Inventory review | 2026-09-05 09:00 UTC | Ready | No |
| R-02 | North route timing review | Confirm the timing note before the route handoff. | Route operations | 2026-09-05 09:20 UTC | Needs review | Yes |
| R-03 | Shared equipment reconciliation | One supporting record is missing from the equipment ledger. | Equipment ledger | 2026-09-05 09:40 UTC | Blocked | No |

Status labels are explicit Product states. Color must not create or change a state. Current priority belongs only to R-02. Its existing DOM label is currently visually hidden; this is a presentation defect, not absent Product data.

No new route, data, interaction, state, field, or functional behavior is authorized. No user acceptance of any correction has occurred.
