# summarize.py: join blind grades (blind-grades/gNN/grade.json) with mech.json via blind-map.json; write grades.json and summary.txt.
import json, pathlib
H = pathlib.Path(__file__).resolve().parent
bmap = json.load(open(H / "blind-map.json")); mech = json.load(open(H / "mech.json", encoding="utf-8"))
rows = []
for b in bmap:
    g = json.load(open(H / "blind-grades" / b["bundle"] / "grade.json", encoding="utf-8")); m = mech[b["id"]]
    rows.append({**b, "blind_cat": g["cat"], "scores": g["scores"], "fourth_blind": g["fourth"], "mech_cat": m["mech_cat"],
                 "inject_used": m["inject_used"], "R6a": m["R6a"], "R6b": m["R6b"], "R7": m["R7"], "own_exit": m["own_exit"], "b132_exit": m["b132_exit"]})
rows.sort(key=lambda r: r["id"])
json.dump(rows, open(H / "grades.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
out = []
for arm in "AB":
    R = [r for r in rows if r["arm"] == arm]; n = len(R)
    c = lambda f: sum(1 for r in R if f(r))
    out.append(f"arm {arm} (n={n}, runs {' '.join(r['id'] for r in R)})")
    out.append(f"  accurate (blind cat exact|equiv): {c(lambda r: r['blind_cat'] in ('exact','equiv'))}/{n}; mech: {c(lambda r: r['mech_cat'] in ('exact','equiv'))}/{n}")
    out.append(f"  false rendered (blind): {c(lambda r: r['blind_cat']=='false_rendered')}/{n}; mech: {c(lambda r: r['mech_cat']=='false_rendered')}/{n}")
    out.append(f"  code / none: {c(lambda r: r['blind_cat']=='code')}/{n} / {c(lambda r: r['blind_cat']=='none')}/{n}")
    for k in ("n1", "n2", "i2", "i3", "i4", "o1", "s", "g"): out.append(f"  {k}: {c(lambda r, k=k: r['scores'][k]==1)}/{n}")
    out.append(f"  --inject used (commands.log): {c(lambda r: r['inject_used'])}/{n}")
    out.append(f"  R7 findings (1.3.2): runs {c(lambda r: r['R7']>0)}/{n}; R6a runs {c(lambda r: r['R6a']>0)}/{n}; R6b runs {c(lambda r: r['R6b']>0)}/{n}")
    out.append(f"  own-arm --verify pass: {c(lambda r: r['own_exit']==0)}/{n}; 1.3.2 --verify pass: {c(lambda r: r['b132_exit']==0)}/{n}")
    out.append("  fourth cells: " + "; ".join(f"{r['id']}={sorted(set(r['fourth_blind']))}" for r in R))
(H / "summary.txt").write_text("\n".join(out) + "\n", encoding="utf-8")
print("\n".join(out))
