# State Matrix

Copy exact intent targets. Classify each claim and put its R, then C1, then any
escalated C2 in `reviewers` before proof. Product actions/states need Experience
claims. Add `escalation_reason` when C2 is required. The ordered routes are in
the operation reference; a reviewer name alone does not prove skill use.
Bindings are filled by the bind command, not approval or authentication.

```json
{"candidate_id":"","revision":"","scope_id":"","targets":[],"claims":[],"bindings":{}}
```
