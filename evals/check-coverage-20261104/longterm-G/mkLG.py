# mkLG.py : L-G fixture = L-B's base commit (43344f3) + joedesign-skill docs from JOEDESIGN main (de6eb3e, arm G), private node_modules junction.
import json, os, pathlib, subprocess, hashlib
L = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-04-joedesign-longterm")
NM = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-06-gomoku-w3/nm/node_modules")
REAL = pathlib.Path("D:/JOEWRKS/.claude-worktrees/AI-Gomoku").resolve()
MAIN = pathlib.Path("D:/JOEWRKS/JOEDESIGN/skills/joedesign")
DOCS = ["SKILL.md", "references/conformance.md", "references/operation.md", "references/visual-translation.md", "templates/DESIGN.md", "scripts/report-check.mjs"]
ID = ["-c", "user.name=JOEWRKS", "-c", "user.email=joewrks@example.invalid"]
def git(root, *a):
    r = subprocess.run(["git", "-C", str(root), *a], capture_output=True, text=True, encoding="utf-8", errors="replace")
    assert r.returncode == 0, (a, r.stderr); return r.stdout.strip()
r = L/"L-G"
if not r.exists():
    subprocess.run(["git", "clone", "-q", "--shared", "--no-checkout", str(L/"L-B"), str(r)], check=True)
    git(r, "config", "core.autocrlf", "false")
    git(r, "checkout", "-q", "-B", "claude/ai-coach", "43344f3"); git(r, "remote", "remove", "origin")
    assert git(r, "status", "--short") == ""
    for d in DOCS:
        b = (MAIN/d).read_bytes(); assert b"\r" not in b
        (r/"joedesign-skill"/d).parent.mkdir(parents=True, exist_ok=True); (r/"joedesign-skill"/d).write_bytes(b)
    git(r, "add", "joedesign-skill"); git(r, *ID, "commit", "-q", "-m", "joedesign-skill 문서 갱신(G, JOEDESIGN main de6eb3e)")
    subprocess.run(["cmd", "/c", "mklink", "/J", str(r/"node_modules").replace("/", "\\"), str(NM).replace("/", "\\")], check=True, capture_output=True)
for d in DOCS: assert (r/"joedesign-skill"/d).read_bytes() == (MAIN/d).read_bytes(), d
assert sorted(p.relative_to(r/"joedesign-skill").as_posix() for p in (r/"joedesign-skill").rglob("*") if p.is_file()) == sorted(DOCS)
tgt = pathlib.Path(os.readlink(r/"node_modules").replace(chr(92)*2 + "?" + chr(92), "")).resolve()
assert tgt == NM.resolve() and tgt != REAL and REAL not in tgt.parents, tgt
assert (r/"node_modules"/"vite"/"package.json").exists()
assert "GOMOKU_DEV_PORT" in (r/"work"/"design"/"capture-matrix.mjs").read_text(encoding="utf-8")
# project tree (excluding joedesign-skill) == B base
tree = lambda root, rev: {l.split("\t")[1]: l.split()[2] for l in git(root, "ls-tree", "-r", rev).split("\n") if not l.split("\t")[1].startswith("joedesign-skill/")}
assert tree(r, "HEAD") == tree(L/"L-B", "43344f3")
ports = json.loads((L/"ports.json").read_text(encoding="utf-8")); ports["G"] = {"dev": 5299, "test": 4273}
(L/"ports.json").write_text(json.dumps(ports), encoding="utf-8")
(L/"turns"/"G").mkdir(exist_ok=True)
print("L-G", git(r, "log", "--oneline", "-2").replace("\n", " | "), "| status", repr(git(r, "status", "--short")), "| junction ->", tgt)
