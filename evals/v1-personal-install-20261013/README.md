# JOEDESIGN 1.0.0 personal installation — T040, 2026-10-13

Direct user approval verified in Manager message
`01a13565-86fd-7c91-84df-8bd546d76049`. The approved source is main
`4295aeb47adb7e384c62c1fe1bc47a3cad946ebc`. This step changes the personal
installation and records only; the tested source package is unchanged.

## Exact scope and backup

- Target: `C:/Users/tjdwo/.codex/skills/joedesign`.
- Before: version0.3.0-dev, 44 files. Source: version1.0.0, 30 tracked files.
- Backup: `D:/JOEWRKS/JOEDESIGN/.local/t040-personal-install-20261013/backup`.
  The entire installation was copied with `shutil.copytree` before any write,
  and all44 file hashes matched. This path is outside the Codex and agents skill
  discovery directories; no renamed old skill was left in discovery.
- Preflight asserted exact source Git blobs, 44 installed files, and exactly two
  differing source files: `VERSION` and `agents/openai.yaml`. The14 extra files
  are existing Python caches. Any unexpected delta would stop before installation.
- Immediately before applying, source/target/backup hashes were checked again.
  `shutil.copyfile(source/name, target/name)` was used for those two names only.
  The exception path restores those two original files from the verified backup;
  no restoration was needed or claimed as a new executed rollback trial.
- After: version1.0.0, 44 files, exactly two changed, zero added/deleted. All30
  package files match source; other42 installed files, including14 caches, match
  the original. Configuration and both untracked feedback directories are unchanged.
  Other product installations are owned by their respective agents and are not
  included in this owner's preservation check.

[Receipt](receipt.json) contains the full old/new/source/backup manifests,
changed/new/deleted lists, exact installed commands and their JSON output.
The local protected-file preflight is `.local/t040-personal-install-20261013/before.json`.
The first staged whitespace check flagged this Windows-generated receipt's CRLF.
Its exact bytes were retained with a receipt-only Git attribute, as for T039 raw
evidence; source code and documentation whitespace checks remain enabled.

## Actual installation checks

```powershell
python -B C:/Users/tjdwo/.codex/skills/joedesign/scripts/harness_cli.py version
python -B C:/Users/tjdwo/.codex/skills/joedesign/scripts/harness_cli.py doctor
```

Both returned exit0. `version` reported1.0.0 and the installed operating SKILL.md.
`doctor` found the real Impeccable, UI UX Pro Max, web-design-guidelines, React best
practices and animation optimization skills at their existing paths. Every available
path and reported SHA256 was compared with its actual file; no placeholder was used.
It reported ready_for_synthesis=true, host_verifier=UNAVAILABLE and
automatic_certification=false. Discovery and byte identity are not proof of actual
specialist invocation, browser observations, behavior compliance or user acceptance.

No full regression repeat: source/runtime remain byte-identical to the T039-tested
package (Python142/Node14, isolated install8 and owner joint14). Manager owns fresh
cross-checks of the three actual installations before central tag/Release publication.
This owner did not create a tag or GitHub Release. Existing F05 geometry-only reuse,
fresh specialist judgments and independent user-acceptance limits remain unchanged.

## Recovery

If this metadata-only update must be rolled back, first compare the current44 files
with receipt.new_manifest and backup44 with receipt.old_manifest. Stop on intervening
user edits. Preserve the current installation, then restore the two changed files
from backup and verify all44 against old_manifest. Do not delete preserved caches,
modify other skills or claim that recovering bytes restores external execution state.
