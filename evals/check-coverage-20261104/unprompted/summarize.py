import json, pathlib, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
D = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-04-joedesign-unprompted-ab")
trials = {t["id"]: t for t in json.loads((D / "trials.json").read_text(encoding="utf-8"))}
mapping = json.loads((D / "blind" / "map.json").read_text(encoding="utf-8"))
rows = []
for tid, code in mapping.items():
    g = D / "blind" / code / "grade.json"
    if g.exists():
        rows.append({**trials[tid], "code": code, **json.loads(g.read_text(encoding="utf-8"))})
(D / "grades.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
crits = sorted({c for r in rows for c in r["scores"]})
print(f"graded {len(rows)} / {len(trials)}")
for scene in ("S2", "S3"):
    for arm in ("A", "B"):
        sel = [r for r in rows if r["arm"] == arm and r["scene"] == scene]
        if not sel: continue
        parts = [f"{c}={sum(int(r['scores'][c]) for r in sel)}/{len(sel)}" for c in crits]
        allp = sum(1 for r in sel if all(r["scores"].values()))
        print(f"  {scene} {arm} " + " ".join(parts) + f" all={allp}/{len(sel)}")
