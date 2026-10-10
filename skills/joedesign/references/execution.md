# Local production execution

`run` connects the existing scoped contracts to actual Codex executions, a local
browser collector, ordered R/C1/conditional C2 reviews, a fresh-context critic,
and bounded repairs. It does not install dependencies, publish the application,
or certify user approval. The original `check`, `advance`, `bundle` and `raci`
contracts retain their existing meanings.

## Prepare once, then run

The coordinating agent reads the user's actual brief, original sources and project
authority and prepares the existing seven artifacts using `init` and `bind`.
First apply the [work-kind decision and design route](../SKILL.md): source inspection
and reference translation precede these implementation contracts. Do not fabricate
a lock from a brand name or invoke the runner to skip a missing reference decision.
Validate the intent, lock, contract and matrix before launching production. Do not
ask the user to transcribe these JSON artifacts. Keep one candidate directory
outside the target Git checkout (neither directory may contain the other).

The target must be a disposable/authorized project checkout. Scope the request to
the approved target, new-direction proof or local repair as applicable. A material
direction change still requires a revised contract and its actual authority; this
runner cannot grant that permission. Run only a local preview already supplied by
the project; the collector does not start or stop application servers.

Create a runtime JSON outside the project with real paths. Example shape only:

```json
{
  "request": "Implement the authorized bounded slice described by this contract.",
  "work_kind": "new_direction",
  "proof_target_ids": ["wide-selected", "narrow-selected"],
  "design_validation": {
    "baseline": "C:/path/to/independently-reviewed-design-checks.json",
    "baseline_sha256": "<independently pinned raw file SHA256>"
  },
  "codex_executable": "C:/path/to/existing/codex.exe",
  "collector_command": ["node", "C:/path/to/joedesign/scripts/capture.mjs"],
  "browser": {
    "base_url": "http://127.0.0.1:3000",
    "playwright_module": "C:/path/to/existing/node_modules/playwright",
    "executable": "C:/path/to/existing/browser.exe",
    "probes": {
      "narrow-selected": {
        "actions": [{"type": "click", "selector": "#record-beta"}],
        "assertions": [{"selector": "#detail", "text": "Beta", "visible": true}]
      }
    }
  },
  "reference_images": ["C:/path/to/actual-original.png"],
  "max_cycles": 2,
  "timeout_seconds": 600
}
```

The IDs above are examples; use the exact targets in the prepared intent. Production
and review both require the [scoped design conformance baseline](conformance.md).
The caller's independent pin must not be derived from the result. Missing required
checks, failed rendered geometry or stale observations block the applicable phase.
Production
requires work_kind (new_direction, material_extension or local_repair) and a nonempty
proof_target_ids list containing every contracted viewport/state of one representative
family. Select the family exposing the largest visual risk, not the easiest screen.
The controller validates explicit selection and coverage, not the truth of a prose
classification. Do not group unrelated families under one name to evade the proof.
A local repair scopes the entire run to its affected family; material expansion uses
the broader contract and still proves a representative family first.

The runner plans and implements that proof only, collects its actual render/interaction
evidence and runs R/C1, conditional C2 and fresh critique. Any required FAIL or
UNVERIFIED stops dependent expansion. Only a completed local proof review launches
the remaining scope. Expansion then recollects and reviews **all** targets on the new
build, including the protected proof. This operational decision never issues host
certification or substitutes for any material approval required by the user.

For one-family work there is no second expansion pass. For multiple families,
proof-* and expansion-* execution records preserve both phases. A failed proof report
lists unreviewed_target_ids; it is not a verdict on the unbuilt remainder. Fix local
findings within the bounded allowance or prepare a revised contract for structural
rework. Broad material changes must not be smuggled into a local repair.

Older production runtime files must add these explicit fields. Do not silently infer
proof scope from target order or replay old production evidence under this policy.
Read-only runs need neither field and retain their full-scope review behavior.

`probes` keys must match the intent's exact target IDs. Actions support click,
fill, press, hover, scroll and bounded observation waits. Predicates must describe
the requested state. A `press` without a selector uses the page keyboard (for
example Tab from the initial document); selector-based press first focuses that
element. Each action records the focused element and `:focus-visible` state.
An assertion may include `focused: true`. Predicates must describe
the requested state, not just the presence of a page. Interaction evidence requires
an actual non-wait action. The collector captures viewport frames, a full-page
image, configured predicates, final URL and browser errors. Those predicates are
not an exhaustive accessibility/functional test. Frame samples cannot certify
continuous motion quality; declared motion quality stays UNVERIFIED in this adapter.
The collector permits only an explicitly configured localhost/loopback preview.

Playwright and its browser are optional external execution capabilities, NOT new
mandatory dependencies for the stdlib contract CLI. Use the project's existing
runtime or the host-provided runtime. Do not auto-install either. A custom
`collector_command` is an explicit executable argument array, never a shell string;
it receives the collection request as stdin and returns one JSON object with
`captures` and `errors`. It cannot issue trusted receipts.

JOEDESIGN is one copied package. J always resolves to its own operating core, with
the internal visual translation/production modules supplied for J assignments.
An external `skills.J` override is rejected; remove it when migrating. Every role
receives that same core before its specialist source and performs only its assigned
stage, rather than starting another workflow. `doctor` uses this same resolution.
External specialists resolve from sibling skill packages, then installed `.codex`
and `.agents` paths. An optional `skills` object maps external role letters to exact
SKILL.md paths; `skills_roots` can replace the external search roots. Missing required
specialists (including possible C2) block launch. Explicit
skill paths do not silently fall back. The runner passes the actual skill body,
source path and hash; it neither rewrites specialist packages nor chooses a model.
Codex uses its configured model and tools. A separate `exec` creates each context.

```powershell
python <skill>/scripts/harness_cli.py run <candidate> --project <checkout> --runtime runtime.json --check-only
python <skill>/scripts/harness_cli.py run <candidate> --project <checkout> --runtime runtime.json
python <skill>/scripts/harness_cli.py run <candidate> --project <checkout> --runtime runtime.json --resume
python <skill>/scripts/harness_cli.py run <new-review-candidate> --project <checkout> --runtime runtime.json --review-only
```

`--check-only` checks inputs and source availability; it is not a live capability
probe. A real run performs read-only synthesis, scoped implementation, collection,
R reviews, C1 reviews, conditional C2 diagnosis, then an independent critic. Each
specialist sees only its assigned claims. C2 sees the disputed observations;
the critic does not inherit builder summaries or prior reviewer verdicts. A
specialist FAIL cannot be averaged away by C2 or the critic.
Review citations may include locked reference IDs for comparison, but a PASS
also needs an actual capture matching the claim's target and evidence kind.
Unknown IDs block the review; invalid output is retained as a failed attempt,
not cached as a completed review.

`--review-only` reviews an existing implementation without synthesis, implementation
or repair writes. It takes fresh browser captures and runs the same R/C1/conditional
C2 and critic checks. Unresolved findings remain NEEDS_REPAIR; the mode never
silently grants write authority. Resume a review run with both `--resume` and
`--review-only`. A different runtime/policy still requires a new candidate; do not
rebind previous results to changed code.

The native CLI receives an explicit `--` before its stdin prompt marker because
`--image` accepts multiple arguments. Byte-identical screenshots are attached once;
all original image paths, hashes and attachment aliases remain in `input.json`.
Distinct frames are retained. Scoped reviewers are directed to relevant source
sections and assigned claims; missing observations still require UNVERIFIED.
The review packet also carries hash-matched collected JSON, project-root AGENTS.md
and existing in-project component files explicitly named by the contract. These
are current source contents, not builder rationale or earlier reviewer verdicts.
Each text file is limited to 64 KiB and the packet's source context to 256 KiB;
non-text, missing, outside-project component paths and oversized files are not
inlined. Original paths stay available for additional investigation. Copies and
hashes are saved in `source-context.json`; this optimization does not disable tools
or change the model, deadline, required verdicts or certification policy.
Every role receives the single JOEDESIGN operating core and its assigned role sources.
Operating core/reference hashes participate in execution identity so a resumed
run cannot silently reuse reviews under changed workflow instructions.

When concrete repair hypotheses remain, a new implementation attempt is followed
by fresh captures and every required review for this bounded scope. A missing
repair hypothesis or exhausted configured attempt allowance stops with NEEDS_REPAIR,
not PASS. This allowance bounds one invocation, not the eventual quality target.
The existing rework policy also applies: a structural FAIL stops immediately;
the same claim unresolved across two cycles stops for material rework even when
`max_cycles` is larger. Claims are counted once per cycle, not once per reviewer.
The implementation must return BLOCKED rather than silently changing a locked
direction. Use a new reviewed candidate revision for material rework.

## Records, resume and limitations

`EXECUTION_STATE.json`, versioned `EXECUTION_REPORT-<cycle>.json` and unique
`execution/` attempt directories preserve inputs, native events, output, errors,
file fingerprints and actual context IDs. The seven original policy artifacts
are not overwritten. An assessment of collected local evidence is included in
each report; native reviews remain execution records, not forged host receipts.

The exclusive `execution.lock` prevents concurrent writers. Ordinary failures
release it. After a controller crash, inspect the recorded PID and child process
tree and ensure they have stopped before manually removing that exact stale lock.
Never remove a live lock. Interrupted/partially changed writer work requires
inspection and a new candidate revision; resume does not blindly repeat it.

Resume reuses completed steps only while contract/runtime/skill identities,
project contents, result files and captures still match. Non-writing phases that
change source stop the run without discarding user edits. The fingerprint includes
tracked and nonignored project files, not arbitrary ignored build output, remote
data or dependency directories. Source identity is not independent attestation of
all rendered resources. Prefer a fixed local preview with known resources; actual
build/data provenance still belongs to the host integration contract.

Read-only subprocess sandbox requests and fresh contexts reduce accidental edits
and inherited conclusions; local logs are writable by the same account and are
not a protected trust service. A misconfigured runtime or MCP tool can weaken that
boundary. The external host must enforce policy, actual skill use, build identity,
calibration and authenticated user events before final certification is possible.

Statuses:

- INPUTS_READY: configuration checked; no roles executed.
- BLOCKED: execution/capability/input failure; inspect exact recorded cause.
- NEEDS_REPAIR: completed review found failures or unverified observations.
- REVIEW_COMPLETE_UNCERTIFIED: no reported unresolved claims in this run; no host
  certification, calibrated quality claim or user acceptance follows.

For `run`, exit 0 means REVIEW_COMPLETE_UNCERTIFIED (or successful check-only),
exit 2 means a blocked/unresolved report, and exit 1 means invalid setup. This differs
from the existing `check`/`handoff` exit 0, which still requires actual approval.
No local result sets `approved: true`. Present the actual output and remaining
limits to the user; never describe the absence of reported defects as proven design
quality improvement or treat implementation permission as exact visual acceptance.
