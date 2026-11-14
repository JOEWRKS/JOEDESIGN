# summarize.py: join blind grades, mechanical measures and the arm map into grades.json and print A vs B per scene.
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
runs = json.load(open(HERE/"blind-map.json", encoding="utf-8"))
mech = json.load(open(HERE/"mech.json", encoding="utf-8"))
KEYS = {"s1": ["o1", "o2", "s", "l", "g", "n", "f"], "s2": ["i1", "i2", "i3", "i4", "o1", "s", "g"]}
out = []
for r in runs:
    g = json.load(open(HERE/"blind-grades"/r["id"]/"grade.json", encoding="utf-8"))
    m = mech[r["id"]]
    out.append({**r, "scores": g["scores"], "fourth_graded": g.get("fourth"), "order_seen": g.get("order_seen"),
                "mech": {"stamp_last": m["stamp_last"], "verify_own_ok": m["own_exit"] == 0, "verify_131_ok": m["b131_exit"] == 0,
                         "R6": m["R6"], "R7": m["R7"], "fourth": m["fourth"], "inject_mention": m["inject_mention"], "tools_changed": m["tools_changed"]}})
json.dump(out, open(HERE/"grades.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
lines = []
for sc in ("s1", "s2"):
    lines.append(f"scene {sc}  (A = 1.3.0, B = 1.3.1)")
    rows = [x for x in out if x["scene"] == sc]
    def cnt(arm, f): xs = [x for x in rows if x["arm"] == arm]; return f"{sum(1 for x in xs if f(x))}/{len(xs)}"
    for k in KEYS[sc]:
        lines.append(f"  {k:<14} A {cnt('A', lambda x: x['scores'].get(k) == 1):>5}   B {cnt('B', lambda x: x['scores'].get(k) == 1):>5}")
    for name, f in [("stamp_last", lambda x: x["mech"]["stamp_last"]), ("verify_own_ok", lambda x: x["mech"]["verify_own_ok"]),
                    ("verify_131_ok", lambda x: x["mech"]["verify_131_ok"]), ("R6=0", lambda x: x["mech"]["R6"] == 0), ("R7=0", lambda x: x["mech"]["R7"] == 0),
                    ("4th exact inj", lambda x: any(v == "rendered (injected css)" for v in x["mech"]["fourth"])),
                    ("tools_unchanged", lambda x: not x["mech"]["tools_changed"])]:
        lines.append(f"  {name:<14} A {cnt('A', f):>5}   B {cnt('B', f):>5}")
txt = "\n".join(lines); print(txt); (HERE/"summary.txt").write_text(txt + "\n", encoding="utf-8")
