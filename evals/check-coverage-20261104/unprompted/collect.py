# Blind packets for the JOEDESIGN tables A/B: REPORT.md + DESIGN.md (after) + DIFF.patch under blind/<code>/.
import json, pathlib, subprocess, random, shutil

D = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-04-joedesign-unprompted-ab")
BLIND = D / "blind"; BLIND.mkdir(exist_ok=True)
map_path = BLIND / "map.json"
mapping = json.loads(map_path.read_text(encoding="utf-8")) if map_path.exists() else {}
rng = random.Random(20261105); codes = [f"q{n:03d}" for n in range(1, 300)]; rng.shuffle(codes)
used = set(mapping.values())


def git(root, *a):
    return subprocess.run(["git", "-C", str(root), *a], capture_output=True, text=True, encoding="utf-8", errors="replace").stdout


done = []
for t in json.loads((D / "trials.json").read_text(encoding="utf-8")):
    root = pathlib.Path(t["root"]); rep = root / "REPORT.md"
    if not rep.exists():
        continue
    code = mapping.get(t["id"]) or next(c for c in codes if c not in used); mapping[t["id"]] = code; used.add(code)
    out = BLIND / code; out.mkdir(exist_ok=True)
    shutil.copyfile(rep, out / "REPORT.md"); shutil.copyfile(root / "DESIGN.md", out / "DESIGN.md")
    fixture = git(root, "log", "--format=%H", "--grep=joedesign-skill 문서", "-1").strip()
    diff = git(root, "diff", fixture, "--", ".", ":!REPORT.md", ":!joedesign-skill")
    untracked = [p for p in git(root, "ls-files", "--others", "--exclude-standard").split("\n") if p and p != "REPORT.md"]
    parts = [f"# git log\n{git(root, 'log', '--oneline', '-4')}\n# diff fixture..worktree (joedesign-skill excluded)\n{diff}"]
    for p in untracked:
        f = root / p
        try:
            body = f.read_text(encoding="utf-8")[:20000] if f.stat().st_size < 400000 else f"<{f.stat().st_size} bytes>"
        except Exception as e:
            body = f"<unreadable: {e}>"
        parts.append(f"# untracked file {p}\n{body}")
    (out / "DIFF.patch").write_text("\n\n".join(parts), encoding="utf-8")
    done.append((t["id"], code, len(rep.read_text(encoding="utf-8")), len(diff)))
map_path.write_text(json.dumps(mapping, ensure_ascii=False, indent=1), encoding="utf-8")
for row in done:
    print(row)
print("collected", len(done))
