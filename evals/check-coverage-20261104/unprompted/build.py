# Unprompted-scene A/B (2026-11-04): same bases as the tables A/B, scenes S2/S3, Opus only.
import json, pathlib, subprocess, itertools, collections
D = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-04-joedesign-unprompted-ab")
P = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-04-joedesign-tables-ab")
SRC = pathlib.Path("D:/JOEWRKS/.claude-worktrees/AI-Gomoku"); BRANCH = "claude/ai-coach"
SPARSE = ["/*", "!/work/design/shots/", "!/work/design/logo-candidates/", "!/work/evidence/"]
SCENES = ["S2", "S3"]; ARMS = ["A", "B"]; REPS = 8
def git(cwd, *a):
    return subprocess.run(["git", "-C", str(cwd), *a], check=True, capture_output=True).stdout
def clone(src, dst):
    subprocess.run(["git", "clone", "-q", "--shared", "--no-checkout", str(src), str(dst)], check=True)
    git(dst, "remote", "remove", "origin"); git(dst, "sparse-checkout", "set", "--no-cone", *SPARSE)
    git(dst, "checkout", "-q", "-B", BRANCH, BRANCH)
    git(dst, "config", "user.name", "JOEWRKS"); git(dst, "config", "user.email", "joewrks@example.invalid")
trials = []; n = 0
for scene, arm, rep in itertools.product(SCENES, ARMS, range(1, REPS + 1)):
    n += 1; tid = f"u{n:02d}-{scene}-{arm}"; root = D / "trials" / tid
    if not root.exists():
        clone(P / f"base-{arm}", root)
        subprocess.run(["cmd", "/c", "mklink", "/J", str(root / "node_modules"), str(SRC / "node_modules")], check=True, capture_output=True)
    trials.append({"id": tid, "scene": scene, "arm": arm, "model": "opus", "rep": rep, "root": str(root)})
(D / "trials.json").write_text(json.dumps(trials, ensure_ascii=False, indent=1), encoding="utf-8")
print("trials", len(trials), collections.Counter((t["scene"], t["arm"]) for t in trials))
