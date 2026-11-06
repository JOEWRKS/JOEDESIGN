# collect2.py : round 2 blind packets. D packets are copied byte-for-byte from round 1 (blind/<code>), E packets are built
# from the trial folders with the same rules as collect.py. All 24 get fresh codes (m###) and go to blind2/ and grade2/.
import json, pathlib, subprocess, random, shutil
D = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-06-gomoku-w3")
B1 = D/"blind"; B2 = D/"blind2"; G2 = D/"grade2"; B2.mkdir(exist_ok=True); G2.mkdir(exist_ok=True)
old = json.loads((B1/"map.json").read_text(encoding="utf-8"))
mp = B2/"map.json"; mapping = json.loads(mp.read_text(encoding="utf-8")) if mp.exists() else {}
rng = random.Random(20261108); codes = [f"m{n:03d}" for n in range(1, 400)]; rng.shuffle(codes); used = set(mapping.values())
SKIP = (".cache/", "dist", "node_modules", "joedesign-skill/", "test-results/", "playwright-report/", "work/tmp/")
def git(root, *a):
    return subprocess.run(["git", "-C", str(root), "-c", "core.quotepath=false", *a], capture_output=True, text=True, encoding="utf-8", errors="replace").stdout
trials = [t for t in json.loads((D/"trials.json").read_text(encoding="utf-8")) if t["arm"] in ("D", "E")]
missing = [t["id"] for t in trials if not (D/"reports"/f"{t['id']}.md").exists()]
assert not missing, missing
done = []
for t in trials:
    tid = t["id"]; root = pathlib.Path(t["root"])
    code = mapping.get(tid) or next(c for c in codes if c not in used); mapping[tid] = code; used.add(code)
    out = B2/code; out.mkdir(exist_ok=True)
    if t["arm"] == "D":
        for f in ("REPORT.md", "DESIGN.md", "DIFF.patch"): shutil.copyfile(B1/old[tid]/f, out/f)
    else:
        txt = (D/"reports"/f"{tid}.md").read_text(encoding="utf-8").replace(str(root), "<project>").replace(str(root).replace("\\", "/"), "<project>").replace(tid, "<project>")
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
        (out/"DIFF.patch").write_text("\n\n".join(parts).replace(tid, "<project>"), encoding="utf-8", newline="")
    # arm letters must not leak into a packet
    for f in ("REPORT.md", "DESIGN.md", "DIFF.patch"):
        body = (out/f).read_text(encoding="utf-8", errors="replace")
        for leak in (tid, "docs-E", "docs-D", "base-E", "base-D", "gomoku-w3"):
            assert leak not in body, (tid, f, leak)
    g = G2/code; g.mkdir(exist_ok=True)
    for f in ("REPORT.md", "DESIGN.md", "DIFF.patch"): shutil.copyfile(out/f, g/f)
    done.append((tid, code, t["kind"]))
mp.write_text(json.dumps(mapping, ensure_ascii=False, indent=1), encoding="utf-8", newline="")
shutil.copyfile(D/"rubric-seeded.md", G2/"rubric-A.md"); shutil.copyfile(D/"rubric-s3.md", G2/"rubric-B.md")
batches = {k: sorted(c for _, c, kind in done if kind == k) for k in ("seeded", "browser", "offline")}
(D/"grade-batches2.json").write_text(json.dumps(batches, indent=1), encoding="utf-8", newline="")
for k, v in batches.items(): print(k, len(v), " ".join(f"`{c}`," for c in v))
print("collected", len(done))
