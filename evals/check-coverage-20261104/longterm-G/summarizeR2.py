# summarizeR2.py : round-2 long-term summary — A (round-3 grades), B-r3 (round-3 grades), B (regraded now), G (graded now); same rubric h1~h8.
import json, pathlib, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
L = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-04-joedesign-longterm")
backlog = {t["n"]: t for t in json.loads((L/"backlog.json").read_text(encoding="utf-8"))}
mapping = json.loads((L/"blind/map.json").read_text(encoding="utf-8"))
rows = []
for key, code in mapping.items():
    arm, t = key.split("-t"); n = int(t); d = L/"blind"/code
    for label, fn in ((arm, "grade.json"), (arm + "-r3", "grade-r3.json")):
        g = d/fn
        if not g.exists(): continue
        if label == "A-r3": continue
        rows.append({"arm": label, "turn": n, "kind": backlog[n]["kind"], "code": code, **json.loads(g.read_text(encoding="utf-8"))})
(L/"grades-r2.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
crits = ["h1","h2","h3","h4","h5","h6","h7","h8"]
arms = ["A", "B-r3", "B", "G"]
for a in arms: print(a, "graded", sum(1 for r in rows if r["arm"] == a))
def line(label, sel):
    if not sel: return
    parts = [f"{c}={sum(int(r['scores'].get(c,0)) for r in sel)}/{len(sel)}" for c in crits]
    print(f"  {label:16s} " + " ".join(parts) + f" all={sum(1 for r in sel if all(int(r['scores'].get(c,0)) for c in crits))}/{len(sel)}")
for a in arms:
    sel = [r for r in rows if r["arm"] == a]
    line(f"{a} all", sel); line(f"{a} main", [r for r in sel if r["kind"] == "main"]); line(f"{a} handoff", [r for r in sel if r["kind"] == "handoff"])
print("-- 10턴 블록 h2 / h3 / h1")
for a in arms:
    for lo in (1, 11, 21, 31):
        sel = [r for r in rows if r["arm"] == a and lo <= r["turn"] < lo+10]
        if sel: print(f"  {a:5s} t{lo:02d}-{lo+9:02d} h2={sum(r['scores']['h2'] for r in sel)}/{len(sel)} h3={sum(r['scores']['h3'] for r in sel)}/{len(sel)} h1={sum(r['scores']['h1'] for r in sel)}/{len(sel)}")
print("-- 함정 턴 h4/h6/h8 (3·8·21·24·31·37)")
for n in (3, 8, 21, 24, 31, 37):
    print(f"  t{n:02d}: " + " | ".join(f"{a} h4={r[0]['scores']['h4']} h6={r[0]['scores']['h6']} h8={r[0]['scores']['h8']}" for a in arms if (r := [x for x in rows if x['arm']==a and x['turn']==n])))
print("-- 범위 축소 턴 h5 (6·25·34)")
for n in (6, 25, 34):
    print(f"  t{n:02d}: " + " | ".join(f"{a} h5={r[0]['scores']['h5']}" for a in arms if (r := [x for x in rows if x['arm']==a and x['turn']==n])))
print("-- 같은 채점기(r2)에서 B vs G 턴별 h2 차이: B만 1 / G만 1 / 둘 다 / 둘 다 0")
bb = {r["turn"]: r["scores"]["h2"] for r in rows if r["arm"] == "B"}; gg = {r["turn"]: r["scores"]["h2"] for r in rows if r["arm"] == "G"}
both = [n for n in bb if n in gg]
print("  ", sum(1 for n in both if bb[n] and not gg[n]), "/", sum(1 for n in both if gg[n] and not bb[n]), "/", sum(1 for n in both if bb[n] and gg[n]), "/", sum(1 for n in both if not bb[n] and not gg[n]), f"(n={len(both)})")
