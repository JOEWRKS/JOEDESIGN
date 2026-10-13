# JOEDESIGN 1.0.0 validation and integration — T039, 2026-10-13

User approval verified in Manager message `01a13543-e72a-71f0-a326-5c768336ab91`.
Base `1d9502ea74d6a0fbbad730450e85f0b327b2906e`; candidate branch
`codex/joedesign-1.0.0`. VERSION is the sole package version source. Skill ID
`joedesign`, operating SKILL.md, scripts, schemas, contracts and F05 support remain
unchanged. Package delta is VERSION plus discovery metadata only.

Candidate scope: Korean README with six common sections, exact JOE roles and
handoffs, actual fresh-copy instructions, explicit existing-install refusal,
update/recovery and validation links; marketing/package version 1.0.0. Detailed
history is linked, not erased. No new installer framework or runtime capability.

Expectations fixed before candidate execution:

- Both Windows PowerShell5 and PowerShell7 execute the exact README copy block in
  temporary Codex homes from a clean 30-file distribution. Installed VERSION1.0.0
  and full file hashes must match. Existing core and legacy harness each cause
  refusal before mutation; missing specialists remain unavailable, not simulated.
- Python142 and historical Node14 must continue passing with actual browser runtime
  configured. Existing historical tests remain tied to historical package bytes.
- Candidate installed producer must link to existing JOENESS gate using actual F05
  P01/P02 evidence: explicit reviewed reuse only; missing pins/runtime changes block;
  no user acceptance promotion. This is fresh runtime execution of preserved old
  measurements, not a fresh model/visual acceptance trial.
- Source and installed package core/runtime bytes other than the two metadata
  files must equal the base. Personal installation, configuration, the two existing
  untracked feedback directories and old fixture evidence must remain unchanged.
- No personal installation, push, main merge, tag or GitHub Release before the
  corresponding QA stage. Main merge follows the already authorized cross-review.

Remote inspection: origin/main `3f76319f6c8a5929c2f55dc47b3c0e4f6a825bdb`, published
F05 branch `1d9502ea74d6a0fbbad730450e85f0b327b2906e`; local/remote tag lists empty.
GitHub repository links confirmed from the actual remotes of JOEFLOW/JOENESS.

## Executed results

- Python 3.14.5: `python -B -m unittest discover -s tests -v` — 142 PASS,
  70.695 seconds, exit0, no skips. [Full output](python-regression.txt).
  `JOEDESIGN_PLAYWRIGHT_MODULE=C:/Users/tjdwo/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright`
  and `JOEDESIGN_BROWSER_EXECUTABLE=C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe`.
- Node v26.3.0: `node --test tests/joedesign-v02.tests.mjs` — 14 PASS, no skips,
  exit0. [Full output](node-regression.txt). This is historical evidence integrity.
- `python -B evals/v1-release-candidate-20261013/verify-install.py --ps7 C:/Users/tjdwo/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/powershell/pwsh.exe --output .local/v1-release-candidate-20261013/install-r1`
  — 8/8 PASS. Each PowerShell version covered new explicit CODEX_HOME, default-home
  fallback, existing-core refusal and legacy-harness refusal. All four installed
  packages contain the exact 30 source files. Missing real specialist dependencies
  return exit2 and ready=false. Local documentation links also resolve.
  [Manifest, paths and results](install-r1/summary.json); raw shell output alongside.
- `python -B evals/f05-impact-20261013/verify-joint.py --producer C:/Users/tjdwo/AppData/Local/Temp/joedesign-v1-install-nlomhc2x/ps7-fresh/codex/skills/joedesign/scripts/harness_cli.py --gate C:/Users/tjdwo/.codex/skills/joeness-setup/scripts/review-gate.mjs --owner-run D:/JOEWRKS/작업하네스/evals/joeness-setup/runs/2026-10-13-impact-review/limited-installed.json --output .local/v1-release-candidate-20261013/joint-r1`
  — 14/14 PASS. [Exact commands, outputs and runtime pins](joint-r1/summary.json).
  Both P01/P02 require reviewed transition pins; stale/no transition, no acceptance,
  missing review pin, tampered impact pin and changed runtime are refused. No new
  measurements, renders or screenshots. The consumer here is the existing installed
  JOENESS gate; all-three new-candidate cross-review belongs to Manager.
- The other 28 package files are byte-identical to base1d9502e, including SKILL.md,
  contracts and runtime. Personal installation, configs and both feedback directories
  match the protected pre-run inventory. Existing F05 source fixtures remained intact.

The copied distribution uses tracked source files only, as delivered by a clean Git
checkout. Generated caches or user files in an older checkout are not distribution
inputs. Preserved absolute paths identify the actual runs; archived copies do not
rebind or replace old evidence. No failure occurred in these candidate checks.

This candidate changes discovery text, but does not claim a fresh autonomous model
trial of that prompt, new visual-quality acceptance, automatic integration or an
authenticated approval boundary. Earlier behavioral results retain their original
package association. Personal installation remains 0.3.0-dev. Source1.0.0 and
personal installation are separate. Tags and GitHub Release are outside this scope.

## Cross-review and main integration

Manager completed the independent review of candidate
`7069f34846bcdea4741e1a122f468347ba5c5dbf` and notified the authorized integration
stage. The new combined Codex home is
`D:/JOEWRKS/JOEWRKS-Product-isolated-installs/joe-1x-t039-manager`.
Manager verified all 17/30/172 package file hashes, JOENESS Check/Apply/Check,
JOEDESIGN version1.0.0, JOEFLOW-to-JOENESS11/11 and JOEDESIGN-to-JOENESS13/13
with19 gate invocations. The tested negative cases and original fixtures, personal
installations and protected configuration remained intact. These are scoped
integration results, not new real-product visual acceptance.

The separately owned audit is recorded under
`D:/JOEWRKS/JOEQASAM/evidence/t039-joe-1x-release/` in `candidate-audit.json`,
`joint-install.json`, `joint-operation.json` and `joint-impact.json`.
The final follow-up changes only documentation and `.gitattributes`; package and
raw-evidence Git blobs must equal candidate7069f34. The attributes preserve raw
CRLF/spacing without exempting this README or verifier code from whitespace checks.

The integration uses normal branch push and fast-forward main; no force push,
history rewrite, new worktree, personal installation, tag or GitHub Release.
The repository version is read from VERSION and the exact integrated revision from
Git main. Earlier candidate-stage restrictions above describe the verification order,
not an outstanding request for another approval.
