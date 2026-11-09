# snapshot.py <arm> <turn>: copies DESIGN.md, records hash manifest + files changed since previous snapshot.
import sys, hashlib, json, pathlib, subprocess
L = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-04-joedesign-longterm")
arm, n = sys.argv[1], int(sys.argv[2]); root = L / f"L-{arm}"; out = L / "turns" / arm
SKIP = ("node_modules", ".git", "work/design/matrix", "work/design/shots", "test-results", "playwright-report", "dist", ".cache")
def manifest():
    m = {}
    for p in root.rglob("*"):
        rel = p.relative_to(root).as_posix()
        if p.is_dir() or any(rel == s or rel.startswith(s + "/") for s in SKIP): continue
        if p.suffix.lower() in (".png", ".jpg", ".webm", ".zip"): continue
        m[rel] = hashlib.sha256(p.read_bytes()).hexdigest()[:16]
    return m
cur = manifest(); prev_p = out / f"t{n-1:02d}-manifest.json"
prev = json.loads(prev_p.read_text(encoding="utf-8")) if prev_p.exists() else {}
changed = sorted([k for k in cur if cur.get(k) != prev.get(k)] + [k for k in prev if k not in cur])
(out / f"t{n:02d}-manifest.json").write_text(json.dumps(cur, indent=0), encoding="utf-8")
(out / f"t{n:02d}-changed.txt").write_text("\n".join(changed), encoding="utf-8")
d = root / "DESIGN.md"
(out / f"t{n:02d}-DESIGN.md").write_bytes(d.read_bytes() if d.exists() else b"")
log = subprocess.run(["git", "-C", str(root), "log", "--oneline", "-3"], capture_output=True, text=True, encoding="utf-8").stdout
(out / f"t{n:02d}-git.txt").write_text(log + subprocess.run(["git", "-C", str(root), "status", "--short"], capture_output=True, text=True, encoding="utf-8").stdout, encoding="utf-8")
print(arm, n, "changed", len(changed), changed[:12])
