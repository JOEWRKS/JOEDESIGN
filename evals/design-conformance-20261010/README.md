# Design conformance and JOENESS connection — 2026-10-10

Latest continuation: [single-core installation and scoped operating connection](operational.md).
Earlier uninstalled/no-activation statements below describe their recorded run.

Follow-up actual GEO snapshot validation: [scope, mapping failure and recovery](geo-validation.md).
This adds 9 browser conditions / 51 geometry checks, injected-defect consumption,
and same-ID changed-target regression. Latest regression is 129 Python / 14 Node;
the earlier counts and manifests below retain their original evidence identity.

Authorized by the user's GEO request to both maintainers. Work remains within the
unified JOEDESIGN source; installations and GEO product files are read-only.

## Expectations fixed before implementation

Reuse existing scoped contracts, target matrix, capture, specialist/critic review,
proof-before-expansion and stale-run guards. Add the missing source-rule/check
coverage and measured rendered geometry, not another work ledger or public skill.

JOEDESIGN owns scoped DESIGN interpretation, applicable target/check selection,
measurement and specialist verdicts. JOENESS owns consuming those verdicts and
blocking the related completion lane. The caller pins the baseline independently;
neither implementation nor its result can redefine that pin. Human authorization
and coverage review remain necessary; local files cannot authenticate authority.

Failure cases: omitted check, stacked gap/margin, partial-only pass, old output
evidence, relaxed criterion, missing/corrupt consumer result. Include normal recovery
and unaffected-scope reuse. Measure bounding-box relationships, not CSS-token presence.
Keep geometric conformance, visual quality, technical success and user acceptance
separate. The receipt always says NOT_GRANTED for acceptance.

Connection uses the agreed joeness.review-baseline.v1 / joedesign.conformance.v1
envelopes. Required check input fingerprints are SHA256 of compact UTF-8 JSON
[[relative_path, sha256_file_bytes], ...], paths sorted by UTF-8 byte order. Baseline
hash is raw-file SHA256 and must be supplied by the coordinator/consumer, not taken
from the result. Evidence integrity is not authentication or visual truth.

Current GEO evidence has before / afterInitial / finalCorrections sections; the
last is only a partial later correction. Do not combine them into a fictitious
single complete current observation. Existing installed joedesign/Harness differ
from the uninstalled 0.3.0-dev source; deployment alone would not fill the missing
rule-to-check mapping. Preserve failures and report actual connection tests below.

## Implemented and ownership

| Owner | Implemented responsibility | Handoff / final responsibility |
|---|---|---|
| JOEDESIGN | DESIGN source/rule/target coverage, independently pinned baseline comparison, rendered geometry and bound specialist verdicts, phase/expansion gate | Emits joedesign.conformance.v1 with required results, evidence, unresolved checks and per-check invalidation inputs; remains responsible for criterion meaning/measurement |
| JOENESS | Explicit review-gate.mjs consumer, current input/evidence validation, missing/failed/stale check rejection, separate completion lanes | Receives the exact result and its independently pinned expected baseline; owns whether the related TASK/ROADMAP completion claim is permitted |
| Product/design coordinator and user | Source authority, baseline coverage review and authorized changes; exact user acceptance | Product records remain with the GEO design owner. Neither tool creates a replacement ledger or grants acceptance |

Existing STATE_MATRIX, R/C1/conditional C2, independent Critic, scope and stale-run
guards are reused. New internal conformance.py and measure-layout.mjs add the missing
rule/check coverage and rendered measurement. The collector includes original frame
hashes, and the producer refuses changed frames. Production and read-only review
require a pinned design_validation baseline; absence blocks before any writer.
verify-design supports the same contract for direct/non-Git observations. Structured
specialist output requires matching claim/target, current inputs/build/capture,
ordered role coverage and independent contexts; geometry alone cannot fill it.

No hardcoded GEO spacing profile was added. The fixture's 16/40/8/32 criteria are
supplied through its own synthetic DESIGN/baseline. The actual GEO screenshots were
read as historical observation, not certified against the current source. Its
afterInitial and later partial finalCorrections remain separate.

## Executed checks

- Full Python regression: **128 PASS, 0 skipped** (`python-tests.txt`). Prior run
  of 127 tests is retained as `python-first.txt`. Tests include missing baseline,
  generic-review PASS with measured FAIL preventing expansion, receipt mutation on
  resume, real browser stacked/automatic spacing, rule/check omission, source change,
  repeated-role consistency, stale output and unaffected input reuse.
- Historical Node regression: **14 PASS, 0 skipped** (`node-history-tests.txt`).
  These still validate archived v0.2 evidence, not new visual quality.
- Final same-read baseline pin/parse hardening was followed by all **8 focused
  conformance tests PASS** (`conformance-final.txt`) and a fresh connection run r3.
- Actual Edge measurement: stacked gap **24**, combined section margin/padding **80**,
  fixed-height/auto-margin gap **160** all FAIL against this fixture's 16/40/8;
  full-child-union inset **32** PASS. Corrected 16/40/8/32 all PASS. Both snapshots
  remain in `captures/`. Font/state checks precede measurement.
- Real producer CLI → actual JOENESS source consumer: **13 expected results**
  (2 producer invocations and 11 consumer invocations) in each isolated r1/r2/r3 run.
  Missing result, missing required check, corrupt receipt, changed output, relaxed
  baseline and damaged evidence all block. Corrected visual scope, unrelated-file
  changes and recovery pass. Whole completion still blocks without user acceptance.
- The JOENESS maintainer independently consumed the r1 producer results in **10
  scenarios**, preserving the original files and mutating disposable copies only.
  Its consumer-side record is owned by that repository at
  `evals/joeness-setup/runs/2026-10-10-specialist-consumption/`.
- Skill validator, package links/anchors, historical archive hashes and unchanged
  installation hashes pass. Source and artifact identities are recorded in manifests.

## Reproduction and preserved data

The portable source recipe is `run-connection.py` plus the explicit fixture in
`tests/test_design_conformance.py`. In a fresh output directory, with an existing
browser runtime configured, run:

```powershell
$env:JOEDESIGN_PLAYWRIGHT_MODULE='<existing playwright module>'
$env:JOEDESIGN_BROWSER_EXECUTABLE='<existing browser executable>'
python evals/design-conformance-20261010/run-connection.py --consumer '<JOENESS source>/skills/joeness-setup/scripts/review-gate.mjs' --output '<new isolated directory>'
```

This creates a new observed run; it does not rebind historical absolute paths/hashes.
`connection-results.json` is r1, `connection-final-results.json` is r2, and
`connection-r3-results.json` is the final producer/consumer pair. r1/r2 consumer SHA
was `65a8c611e37c4e24f5bd50d111c86208ce7afd73c46f66886e96da07e176c5f0`;
r3 uses `7f9d728a082c38e8b4ece838286ec61365e82fbfe2f5980288e5df42147141bf`.
The consumer's final adjustment parses the same bytes it hashes. Producer pin/parse
also uses one read; this is not an atomic lock across all source files.

Raw requests/observations/receipts live in `.local/design-conformance-20261010/`;
their exact hashes and reproduction source hashes are preserved in the manifests.
Two raw browser screenshots are copied here for inspection. A clone contains the
recipe and summaries, not a claim that a historical machine's paths still resolve.

## Activation and remaining limits

Source candidate: unified JOEDESIGN **0.3.0-dev**, uncommitted and uninstalled.
Both installed old JOEDESIGN/Harness packages are unchanged (46 files checked).
GEOTest/FnBShop has no project-local skill directory at the observed locations;
the global installed entrypoints differ from this candidate. `observed-sources.json`
records hashes and product evidence pointers. File presence does not prove exactly
which bytes a past model invocation consumed; GEO's TASK records identify its older
installed-rule review. The new consumer is not active in that project's AGENTS.

This fixes the explicit producer/consumer path for a reviewed pinned scope. It does
not prove completeness or correctness of the initial natural-language DESIGN mapping,
source-to-served-build honesty, live specialist adherence, aesthetic quality or user
acceptance. Independent coverage/authority review is still necessary. Someone able
to rewrite both baseline and pin, forge observations, edit TASK directly or bypass
the CLI in chat can bypass local controls. Protected host/CI and authenticated events
are needed for stronger enforcement. No such host, installation, activation, product
edit, commit or push was performed by this source task.
