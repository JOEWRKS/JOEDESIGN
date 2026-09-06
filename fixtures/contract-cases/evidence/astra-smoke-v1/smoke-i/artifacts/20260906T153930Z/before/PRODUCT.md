# Incident Decision Brief — Product Truth v1

This is a neutral fictional local fixture, not a live operations system.
Purpose: help an operations lead understand one incident and decide the next action.

Required content, fixed verbatim in index.html:
- Incident title: Delivery queue delay
- One-sentence summary: A stalled worker is delaying outgoing notices; delivery is recovering, but the next restart needs an operations review.
- Metadata: Severity: Moderate; Status: Recovering.
- Three ordered findings:
  1. Backlog is shrinking — The queue has fallen from 240 to 80 notices since the worker was isolated.
  2. New notices remain delayed — Incoming notices are still waiting six minutes before delivery begins.
  3. Restart needs a review — Confirm the replacement worker is ready before preparing a controlled restart.
- One primary action: Prepare recovery review.
- One secondary evidence link: Read incident evidence, targeting #incident-evidence (the existing findings section).

The summary precedes findings; findings remain ordered 1 → 2 → 3. The primary action remains single and explicit, after the evidence in semantic reading order. Product attention progression: understand incident/summary → read ordered evidence/findings → prepare the next action. Severity/status support the summary, not an unrelated promotional focal.

The button only updates the existing live output to: Recovery review prepared locally. No live action performed.
This is a local fixture simulation and performs no network write. Preserve this behavior and the initially empty output.

Required labels: Incident Decision Brief, Ordered findings, Next action. No imagery is required. No decorative marketing copy or new Product content may be added. Existing visible content and actions must remain; minimum semantic markup changes are permitted for composition.
