import json, pathlib, collections, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
D = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-04-joedesign-tables-ab")
trials = {t["id"]: t for t in json.loads((D / "trials.json").read_text(encoding="utf-8"))}
mapping = json.loads((D / "blind" / "map.json").read_text(encoding="utf-8"))
rows = []
for tid, code in mapping.items():
    g = D / "blind" / code / "grade.json"
    if g.exists():
        gr = json.loads(g.read_text(encoding="utf-8")); rows.append({**trials[tid], "code": code, **gr})
(D / "grades.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
crits = sorted({c for r in rows for c in r["scores"]})
print(f"graded {len(rows)} / {len(trials)}")
for arm in ("A", "B"):
    for model in (None, "opus", "sonnet"):
        sel = [r for r in rows if r["arm"] == arm and (model is None or r["model"] == model)]
        if not sel: continue
        parts = [f"{c}={sum(int(r['scores'][c]) for r in sel)}/{len(sel)}" for c in crits]
        allp = sum(1 for r in sel if all(r["scores"].values()))
        print(f"  {arm} {model or 'all':6s} " + " ".join(parts) + f" all={allp}/{len(sel)}")
