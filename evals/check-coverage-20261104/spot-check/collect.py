# collect.py : blind packets (REPORT.md + DESIGN.md + DIFF.patch) under blind/<code>/ for every trial with a saved report
import json, pathlib, subprocess, random, shutil
D = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-06-gomoku-w3")
BLIND = D/"blind"; BLIND.mkdir(exist_ok=True)
mp = BLIND/"map.json"; mapping = json.loads(mp.read_text(encoding="utf-8")) if mp.exists() else {}
rng = random.Random(20261107); codes = [f"k{n:03d}" for n in range(1, 400)]; rng.shuffle(codes); used = set(mapping.values())
SKIP = (".cache/", "dist", "node_modules", "joedesign-skill/", "test-results/", "playwright-report/", "work/tmp/")
def git(root, *a):
    return subprocess.run(["git", "-C", str(root), "-c", "core.quotepath=false", *a], capture_output=True, text=True, encoding="utf-8", errors="replace").stdout
done = []
for t in json.loads((D/"trials.json").read_text(encoding="utf-8")):
    root = pathlib.Path(t["root"]); rep = D/"reports"/f"{t['id']}.md"
    if not rep.exists(): continue
    code = mapping.get(t["id"]) or next(c for c in codes if c not in used); mapping[t["id"]] = code; used.add(code)
    out = BLIND/code; out.mkdir(exist_ok=True)
    # arm-neutral: the trial path (which carries the arm letter) is replaced
    txt = rep.read_text(encoding="utf-8").replace(str(root), "<project>").replace(str(root).replace("\\", "/"), "<project>").replace(t["id"], "<project>")
    (out/"REPORT.md").write_text(txt, encoding="utf-8", newline="")
    shutil.copyfile(root/"DESIGN.md", out/"DESIGN.md")
    diff = git(root, "diff", "HEAD", "--", ".", ":!joedesign-skill", ":!package-lock.json")
    untracked = [p for p in git(root, "ls-files", "--others", "--exclude-standard").split("\n") if p and not p.startswith(SKIP)]
    parts = [f"# diff base..worktree (joedesign-skill excluded)\n{diff}"]
    for p in untracked:
        f = root/p
        if f.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp", ".zip", ".woff2"): parts.append(f"# untracked binary {p} ({f.stat().st_size} bytes)"); continue
        try: body = f.read_text(encoding="utf-8")[:20000] if f.stat().st_size < 400000 else f"<{f.stat().st_size} bytes>"
        except Exception as e: body = f"<unreadable: {e}>"
        parts.append(f"# untracked file {p}\n{body}")
    (out/"DIFF.patch").write_text("\n\n".join(parts).replace(t["id"], "<project>"), encoding="utf-8", newline="")
    done.append((t["id"], code, len(txt), len(diff), len(untracked)))
mp.write_text(json.dumps(mapping, ensure_ascii=False, indent=1), encoding="utf-8", newline="")
for r in done: print(r)
print("collected", len(done))
