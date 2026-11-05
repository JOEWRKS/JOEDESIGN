# summarize.py : join blind grades with trial arms and print per-arm totals (offline v*, browser w*)
import json, pathlib, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
D = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-05-joedesign-report-scope-ab")
trials = {t["id"]: t for t in json.loads((D/"trials.json").read_text(encoding="utf-8"))}
mapping = json.loads((D/"blind"/"map.json").read_text(encoding="utf-8"))
rows = []
for tid, code in sorted(mapping.items()):
    g = D/"blind"/code/"grade.json"
    if g.exists(): rows.append({"id": tid, "arm": trials[tid]["arm"], "kind": trials[tid]["kind"], "code": code, **json.loads(g.read_text(encoding="utf-8"))})
(D/"grades.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8", newline="")
crits = ["b", "c", "f", "g", "h", "s", "t", "u"]
print(f"graded {len(rows)} / {len(mapping)}")
for kind in ("offline", "browser"):
    for arm in ("B", "C"):
        sel = [r for r in rows if r["arm"] == arm and r["kind"] == kind]
        if not sel: continue
        print(f"  {kind} {arm} " + " ".join(f"{c}={sum(int(r['scores'].get(c, 0)) for r in sel)}/{len(sel)}" for c in crits))
    for r in rows:
        if r["kind"] == kind: print("    ", r["id"], r["code"], " ".join(f"{c}{r['scores'].get(c)}" for c in crits))
