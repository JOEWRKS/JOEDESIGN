# reset-w.py : return the 4 stopped browser trials (w01..w04) to their clean base commit, junction-safe
import os, pathlib, subprocess
V = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-05-joedesign-report-scope-ab")
NM = pathlib.Path("D:/JOEWRKS/.claude-worktrees/AI-Gomoku/node_modules")
assert (NM/"vite"/"package.json").exists()
for t in ["w01-B", "w02-B", "w03-B", "w04-B"]:
    root = V/"trials"/t
    # 1) list every reparse point under the trial (no following)
    links = []
    for d, dirs, files in os.walk(root, followlinks=False):
        for n in list(dirs):
            p = pathlib.Path(d)/n
            if os.path.isjunction(p) or os.path.islink(p):
                links.append(p); dirs.remove(n)
    print(t, "links:", [str(l.relative_to(root)) for l in links])
    for l in links:
        os.rmdir(l)            # removes the link only
        assert not os.path.lexists(l)
    assert (NM/"vite"/"package.json").exists()
    head = subprocess.run(["git", "-C", str(root), "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip()
    subprocess.run(["git", "-C", str(root), "reset", "--hard", "-q"], check=True)
    subprocess.run(["git", "-C", str(root), "clean", "-fdxq"], check=True)
    st = subprocess.run(["git", "-C", str(root), "status", "--short"], capture_output=True, text=True).stdout
    subprocess.run(["cmd", "/c", "mklink", "/J", str(root/"node_modules").replace("/", "\\"), str(NM).replace("/", "\\")], check=True, capture_output=True)
    tgt = os.readlink(root/"node_modules")
    print(t, head, "status:", repr(st), "junction ->", tgt, (root/"node_modules"/"vite"/"package.json").exists())
