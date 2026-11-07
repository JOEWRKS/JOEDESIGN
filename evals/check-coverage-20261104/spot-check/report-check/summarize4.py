# summarize4.py : round 4. Joins blind4 grades (grade4/<code>/grade.json) with trial arms; F (regraded) vs G, same graders.
import json, pathlib, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
V = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-06-gomoku-w3")
trials = {t["id"]: t for t in json.loads((V/"trials.json").read_text(encoding="utf-8"))}
mapping = json.loads((V/"blind4"/"map.json").read_text(encoding="utf-8"))
r1 = {r["id"]: r for r in json.loads((V/"grades3.json").read_text(encoding="utf-8"))}
rows = []
for tid, code in sorted(mapping.items()):
    g = V/"grade4"/code/"grade.json"
    if not g.exists(): continue
    t = trials[tid]
    rows.append({"id": tid, "arm": t["arm"], "kind": t["kind"], "code": code, **json.loads(g.read_text(encoding="utf-8"))})
(V/"grades4.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8", newline="")
print(f"graded {len(rows)} / {len(mapping)}")
CR = {"seeded": ["x", "g", "h", "s", "t", "u"], "browser": ["b", "c", "f", "g", "h", "s", "t", "u"], "offline": ["b", "c", "f", "g", "h", "s", "t", "u"]}
for kind, crits in CR.items():
    for arm in ("F", "G"):
        sel = [r for r in rows if r["arm"] == arm and r["kind"] == kind]
        if not sel: continue
        extra = " outcome=" + ",".join(r.get("x_outcome", "?") for r in sel) if kind == "seeded" else ""
        print(f"  {kind} {arm} " + " ".join(f"{c}={sum(int(r['scores'].get(c, 0)) for r in sel)}/{len(sel)}" for c in crits) + extra)
    for r in rows:
        if r["kind"] != kind: continue
        was = r1.get(r["id"])
        note = "  (round 3: " + " ".join(f"{c}{was['scores'].get(c)}" for c in crits) + ")" if was else ""
        print("    ", r["id"], r["code"], " ".join(f"{c}{r['scores'].get(c)}" for c in crits), r.get("x_outcome", ""), note)
for arm in ("F", "G"):
    sel = [r for r in rows if r["arm"] == arm]
    br = [r for r in sel if r["kind"] != "offline"]
    if sel: print(f"  all scenes {arm}: " + " ".join(f"{c}={sum(int(r['scores'].get(c, 0)) for r in sel)}/{len(sel)}" for c in ("g", "h", "s", "t")) +
                  "   browser scenes: " + " ".join(f"{c}={sum(int(r['scores'].get(c, 0)) for r in br)}/{len(br)}" for c in ("g", "h", "s", "t", "u")))
