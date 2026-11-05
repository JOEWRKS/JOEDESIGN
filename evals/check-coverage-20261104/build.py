# JOEDESIGN token-role / rule-coverage table A/B (2026-11-04).
# Fixture: AI-Gomoku at cbf7531^ (just before the real "디자인 시스템 v1" commit on 2026-10-24), --shared clones.
# Each trial carries a joedesign-skill/ folder: arm A = JOEDESIGN 1.0.0 (git HEAD), arm B = patched working tree.
import json, pathlib, subprocess, itertools, collections, sys

D = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-04-joedesign-tables-ab")
SRC = pathlib.Path("D:/JOEWRKS/.claude-worktrees/AI-Gomoku"); JD = pathlib.Path("D:/JOEWRKS/JOEDESIGN")
REF = "cbf7531^"; BRANCH = "claude/ai-coach"
SPARSE = ["/*", "!/work/design/shots/", "!/work/design/logo-candidates/", "!/work/evidence/"]
SKILL_FILES = ["SKILL.md", "templates/DESIGN.md", "references/conformance.md", "references/operation.md", "references/visual-translation.md"]
MODELS = ["opus", "sonnet"]; ARMS = ["A", "B"]; REPS = 4


def git(cwd, *a):
    return subprocess.run(["git", "-C", str(cwd), *a], check=True, capture_output=True).stdout


def clone(src, dst, ref):
    subprocess.run(["git", "clone", "-q", "--shared", "--no-checkout", str(src), str(dst)], check=True)
    git(dst, "remote", "remove", "origin"); git(dst, "sparse-checkout", "set", "--no-cone", *SPARSE)
    git(dst, "checkout", "-q", "-B", BRANCH, ref)
    git(dst, "config", "user.name", "JOEWRKS"); git(dst, "config", "user.email", "joewrks@example.invalid")


def skill_bytes(arm, rel):
    if arm == "A":
        return git(JD, "show", f"HEAD:skills/joedesign/{rel}")
    return (JD / "skills/joedesign" / rel).read_bytes()


commit = git(SRC, "rev-parse", REF).decode().strip()
for arm in ARMS:
    base = D / f"base-{arm}"
    if base.exists():
        continue
    clone(SRC, base, commit)
    for rel in SKILL_FILES:
        p = base / "joedesign-skill" / rel; p.parent.mkdir(parents=True, exist_ok=True); p.write_bytes(skill_bytes(arm, rel))
    git(base, "add", "joedesign-skill"); git(base, "commit", "-q", "-m", "joedesign-skill 문서(이 작업용)")
    print("base", arm, git(base, "rev-parse", "--short", "HEAD").decode().strip())

trials = []; n = 0
for model, arm, rep in itertools.product(MODELS, ARMS, range(1, REPS + 1)):
    n += 1; tid = f"t{n:02d}-{arm}-{model}"; root = D / "trials" / tid
    if not root.exists():
        clone(D / f"base-{arm}", root, BRANCH)
        subprocess.run(["cmd", "/c", "mklink", "/J", str(root / "node_modules"), str(SRC / "node_modules")], check=True, capture_output=True)
    trials.append({"id": tid, "arm": arm, "model": model, "rep": rep, "root": str(root)})
(D / "trials.json").write_text(json.dumps(trials, ensure_ascii=False, indent=1), encoding="utf-8")
print("fixture commit", commit[:7], "trials", len(trials), collections.Counter((t["arm"], t["model"]) for t in trials))
