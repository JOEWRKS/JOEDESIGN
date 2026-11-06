# summarize.py : join blind grades with trial arms. seeded = x*, browser S3 = y* (new D) + w05..w08 (old C, regraded), offline S3 = z* (new D) + 4 old C (regraded)
import json, pathlib, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
V = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-06-gomoku-w3")
trials = {t["id"]: t for t in json.loads((V/"trials.json").read_text(encoding="utf-8"))}
mapping = json.loads((V/"blind"/"map.json").read_text(encoding="utf-8"))
rows = []
for tid, code in sorted(mapping.items()):
    g = V/"blind"/code/"grade.json"
    if not g.exists(): continue
    t = trials.get(tid) or {"arm": "C", "kind": "browser" if tid.startswith("w") else "offline"}
    rows.append({"id": tid, "arm": t["arm"], "kind": t["kind"], "code": code, **json.loads(g.read_text(encoding="utf-8"))})
(V/"grades.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8", newline="")
print(f"graded {len(rows)} / {len(mapping)}")
for kind, crits in (("seeded", ["x", "g", "h", "s", "t", "u"]), ("browser", ["b", "c", "f", "g", "h", "s", "t", "u"]), ("offline", ["b", "c", "f", "g", "h", "s", "t", "u"])):
    for arm in ("B", "C", "D"):
        sel = [r for r in rows if r["arm"] == arm and r["kind"] == kind]
        if not sel: continue
        extra = " outcome=" + ",".join(r.get("x_outcome", "?") for r in sel) if kind == "seeded" else ""
        print(f"  {kind} {arm} " + " ".join(f"{c}={sum(int(r['scores'].get(c, 0)) for r in sel)}/{len(sel)}" for c in crits) + extra)
    for r in rows:
        if r["kind"] == kind: print("    ", r["id"], r["code"], " ".join(f"{c}{r['scores'].get(c)}" for c in crits), r.get("x_outcome", ""))
