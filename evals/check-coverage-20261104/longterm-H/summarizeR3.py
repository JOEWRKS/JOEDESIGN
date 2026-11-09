# summarizeR3.py : H t01-10 vs G t01-10 (regraded, same graders), plus G's earlier r2 grades for the same turns.
import json, pathlib, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
L = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-04-joedesign-longterm")
backlog = {t["n"]: t for t in json.loads((L/"backlog.json").read_text(encoding="utf-8"))}
m = json.loads((L/"blind/map.json").read_text(encoding="utf-8")); rows = []
for key, code in m.items():
    arm, t = key.split("-t"); n = int(t)
    if n > 10 or arm not in ("G", "H"): continue
    for label, fn in ((arm, "grade.json"), (arm + "-r2", "grade-r2.json")):
        g = L/"blind"/code/fn
        if g.exists(): rows.append({"arm": label, "turn": n, "kind": backlog[n]["kind"], "code": code, **json.loads(g.read_text(encoding="utf-8"))})
(L/"grades-r3.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
crits = ["h1","h2","h3","h4","h5","h6","h7","h8"]
def line(label, sel):
    if not sel: return
    print(f"  {label:14s} " + " ".join(f"{c}={sum(int(r['scores'].get(c,0)) for r in sel)}/{len(sel)}" for c in crits) + f" all={sum(1 for r in sel if all(int(r['scores'].get(c,0)) for c in crits))}/{len(sel)}")
for a in ("G-r2", "G", "H"):
    sel = [r for r in rows if r["arm"] == a]; print(a, "graded", len(sel))
    line(f"{a} all", sel); line(f"{a} main", [r for r in sel if r["kind"] == "main"]); line(f"{a} handoff", [r for r in sel if r["kind"] == "handoff"])
print("-- 턴별 h2 (G 재채점 / H)")
for n in range(1, 11):
    g = [r for r in rows if r["arm"] == "G" and r["turn"] == n]; h = [r for r in rows if r["arm"] == "H" and r["turn"] == n]
    print(f"  t{n:02d} {backlog[n]['kind']:7s} G={g[0]['scores']['h2'] if g else '-'} H={h[0]['scores']['h2'] if h else '-'}")
