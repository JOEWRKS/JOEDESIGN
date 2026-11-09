# collectI.py : blind packets (REPORT.md, DESIGN.md, DIFF.patch) with fresh codes; arm letters and trial ids scrubbed. Usage: collectI.py <kind> [<kind>...]
import json, pathlib, subprocess, random, shutil, sys, re
D = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-09-joedesign-i")
B = D/"blind"; G = D/"grade"; B.mkdir(exist_ok=True); G.mkdir(exist_ok=True)
mp = B/"map.json"; mapping = json.loads(mp.read_text(encoding="utf-8")) if mp.exists() else {}
rng = random.Random(20261109); codes = [f"k{n:03d}" for n in range(1, 400)]; rng.shuffle(codes); used = set(mapping.values())
SKIP = (".cache/", "dist", "node_modules", "joedesign-skill/", "test-results/", "playwright-report/", "work/tmp/")
def git(root, *a):
    return subprocess.run(["git", "-C", str(root), "-c", "core.quotepath=false", *a], capture_output=True, text=True, encoding="utf-8", errors="replace").stdout
kinds = sys.argv[1:] or ["feature", "handoff", "browser", "offline"]
trials = [t for t in json.loads((D/"trials.json").read_text(encoding="utf-8")) if t["kind"] in kinds]
missing = [t["id"] for t in trials if not (D/"reports"/f"{t['id']}.md").exists()]
assert not missing, missing
done = []
for t in trials:
    tid = t["id"]; root = pathlib.Path(t["root"])
    code = mapping.get(tid) or next(c for c in codes if c not in used); mapping[tid] = code; used.add(code)
    out = B/code; out.mkdir(exist_ok=True)
    scrub = lambda s: re.sub(r"\b[fpyz]\d\d-[IH]\b", "<project>", s.replace(str(root), "<project>").replace(str(root).replace("\\", "/"), "<project>"))
    txt = scrub((D/"reports"/f"{tid}.md").read_text(encoding="utf-8"))
    (out/"REPORT.md").write_text(txt, encoding="utf-8", newline="")
    (out/"DESIGN.md").write_text(scrub((root/"DESIGN.md").read_text(encoding="utf-8")), encoding="utf-8", newline="")
    diff = git(root, "diff", "HEAD", "--", ".", ":!joedesign-skill", ":!package-lock.json")
    untracked = [p for p in git(root, "ls-files", "--others", "--exclude-standard").split("\n") if p and not p.startswith(SKIP)]
    parts = [f"# diff base..worktree (joedesign-skill excluded)\n{diff}"]
    for p in untracked:
        f = root/p
        if f.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp", ".zip", ".woff2"): parts.append(f"# untracked binary {p} ({f.stat().st_size} bytes)"); continue
        try: body = f.read_text(encoding="utf-8")[:20000] if f.stat().st_size < 400000 else f"<{f.stat().st_size} bytes>"
        except Exception as e: body = f"<unreadable: {e}>"
        parts.append(f"# untracked file {p}\n{body}")
    (out/"DIFF.patch").write_text(scrub("\n\n".join(parts)), encoding="utf-8", newline="")
    for f in ("REPORT.md", "DESIGN.md", "DIFF.patch"):
        body = (out/f).read_text(encoding="utf-8", errors="replace")
        for leak in (tid, "docs-I", "docs-H", "xbase-I", "xbase-H", "pbase-I", "wbase-I", "obase-I", "joedesign-i"):
            assert leak not in body, (tid, f, leak)
    g = G/code; g.mkdir(exist_ok=True)
    for f in ("REPORT.md", "DESIGN.md", "DIFF.patch"): shutil.copyfile(out/f, g/f)
    done.append((tid, code, t["kind"]))
mp.write_text(json.dumps(mapping, ensure_ascii=False, indent=1), encoding="utf-8", newline="")
batches = {k: sorted(c for _, c, kind in done if kind == k) for k in kinds}
bj = D/"grade-batches.json"; old = json.loads(bj.read_text(encoding="utf-8")) if bj.exists() else {}; old.update(batches)
bj.write_text(json.dumps(old, indent=1), encoding="utf-8", newline="")
for k, v in batches.items(): print(k, len(v), " ".join(f"`{c}`" for c in v))
print("collected", len(done))
