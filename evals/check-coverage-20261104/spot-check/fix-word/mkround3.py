# mkround3.py : round 3 (arm F = E + fix word slot + summary parenthesis). Bases xbase-F / wbase-F / obase-F and 12 trial clones + prompts.
# Reuses the texts of mktrials.py; every node_modules junction is verified to point at the private copy.
import json, os, pathlib, subprocess, re
V = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-06-gomoku-w3")
OLD = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-05-joedesign-report-scope-ab")
NM = V/"nm"/"node_modules"; REAL = pathlib.Path("D:/JOEWRKS/.claude-worktrees/AI-Gomoku").resolve()
DOCS = ["SKILL.md", "references/conformance.md", "references/operation.md", "references/visual-translation.md", "templates/DESIGN.md"]
ID = ["-c", "user.name=JOEWRKS", "-c", "user.email=joewrks@example.invalid"]
SPARSE = "/*\n!/work/design/shots/\n!/work/design/logo-candidates/\n!/work/evidence/\n"
def git(root, *a):
    r = subprocess.run(["git", "-C", str(root), *a], capture_output=True, text=True, encoding="utf-8", errors="replace")
    assert r.returncode == 0, (a, r.stderr); return r.stdout.strip()
def clone(src, dst):
    subprocess.run(["git", "clone", "-q", "--shared", "--no-checkout", str(src), str(dst)], check=True)
    git(dst, "config", "core.sparseCheckout", "true"); git(dst, "config", "core.autocrlf", "false")
    (dst/".git"/"info"/"sparse-checkout").write_bytes(SPARSE.encode())
    git(dst, "checkout", "-q", "-B", "claude/ai-coach", "HEAD"); git(dst, "remote", "remove", "origin")
for name, src in [("xbase-F", V/"xbase-B"), ("wbase-F", OLD/"wbase-C"), ("obase-F", OLD/"base-C")]:
    r = V/name
    if not r.exists():
        clone(src, r)
        for d in DOCS:
            b = (V/"docs-F"/d).read_bytes(); assert b"\r" not in b; (r/"joedesign-skill"/d).write_bytes(b)
        git(r, "add", "joedesign-skill"); git(r, *ID, "commit", "-q", "-m", "joedesign-skill 문서 갱신")
    for d in DOCS: assert (r/"joedesign-skill"/d).read_bytes() == (V/"docs-F"/d).read_bytes(), (name, d)
    # same project state as the D base: only joedesign-skill differs
    dbase = V/name.replace("-F", "-E")
    print(name, git(r, "log", "--oneline", "-2").replace("\n", " | "), "status:", repr(git(r, "status", "--short")))
# texts from mktrials.py (single source)
src = (V/"mktrials.py").read_text(encoding="utf-8")
ns = {}
exec(src[src.index('HEAD = "'):src.index("trials = []")], ns)
plan = [(f"x{17+i}-F", "seeded", "xbase-F", 5645 + i, 4665 + i) for i in range(4)] + \
       [(f"y{9+i:02d}-F", "browser", "wbase-F", 5649 + i, 4669 + i) for i in range(4)] + \
       [(f"z{9+i:02d}-F", "offline", "obase-F", None, None) for i in range(4)]
tj = V/"trials.json"; trials = json.loads(tj.read_text(encoding="utf-8")); have = {t["id"] for t in trials}
for tid, kind, base, dev, test in plan:
    root = V/"trials"/tid
    if not root.exists():
        clone(V/base, root)
        subprocess.run(["cmd", "/c", "mklink", "/J", str(root/"node_modules").replace("/", "\\"), str(NM).replace("/", "\\")], check=True, capture_output=True)
    tgt = pathlib.Path(os.readlink(root/"node_modules").replace(chr(92) * 2 + "?" + chr(92), "")).resolve()
    assert tgt == NM.resolve() and tgt != REAL and REAL not in tgt.parents, (tid, tgt)
    assert (root/"node_modules"/"vite"/"package.json").exists() and (root/"joedesign-skill"/"SKILL.md").exists()
    assert "one of two words" in (root/"joedesign-skill"/"SKILL.md").read_text(encoding="utf-8")
    assert git(root, "status", "--short") == "", tid
    rs = str(root).replace("/", "\\")
    if kind == "offline": p = ns["HEAD"].format(root=rs) + ns["SKILL_O"] + ns["ENV_O"] + ns["MSG"][kind] + ns["TAIL_O"]
    else: p = ns["HEAD"].format(root=rs) + ns["SKILL_B"] + ns["ENV_B"].format(dev=dev, test=test) + ns["MSG"][kind] + ns["TAIL_B"]
    (V/"prompts"/f"{tid}.txt").write_bytes(p.encode("utf-8"))
    # prompt must equal the matching D prompt except for trial id and ports
    ref = {"seeded": "x03-D", "browser": "y01-D", "offline": "z01-D"}[kind]
    norm = lambda s, t: re.sub(r"\b(56|46)\d\d\b", "PORT", s.replace(t, "TID"))
    assert norm(p, tid) == norm((V/"prompts"/f"{ref}.txt").read_text(encoding="utf-8"), ref), tid
    if tid not in have:
        trials.append({"id": tid, "arm": "F", "kind": kind, "root": rs, "base": base, "head": git(root, "rev-parse", "--short", "HEAD"), **({"dev": dev, "test": test} if dev else {})})
    print(tid, base, git(root, "rev-parse", "--short", "HEAD"), "junction ok ->", tgt.parent.name + "/" + tgt.name, "ports", dev, test)
tj.write_text(json.dumps(trials, ensure_ascii=False, indent=1), encoding="utf-8", newline="")
print(len(trials), "trials total")
