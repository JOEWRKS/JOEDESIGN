# analyzeJ.py : unblind grades, per-arm counts, plus DESIGN.md read counts (handoff) and product-definition reads (relocate)
import json, pathlib
D = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-10-joedesign-j")
mp = json.loads((D/"blind-map.json").read_text(encoding="utf-8")); trials = {t["id"]: t for t in json.loads((D/"trials.json").read_text(encoding="utf-8"))}
grades = {tid: json.loads((D/"blind"/code/"grade.json").read_text(encoding="utf-8")) for tid, code in mp.items()}
(D/"grades.json").write_text(json.dumps({t: {"code": mp[t], **g} for t, g in sorted(grades.items())}, ensure_ascii=False, indent=1), encoding="utf-8", newline="")
want = {"r1": "A", "r2": "B", "r3": "C"}
lines = []
for tid in sorted(grades):
    t = trials[tid]; g = grades[tid]
    if t["kind"] == "relocate" and g.get("kind") != want[t["msg"]]: lines.append(f"KIND MISMATCH {tid} grader={g.get('kind')} msg={t['msg']}")
def cnt(kind, msgs, key):
    out = {}
    for arm in ("J", "I"):
        v = [grades[t]["scores"][key] for t in grades if trials[t]["kind"] == kind and trials[t]["arm"] == arm and trials[t]["msg"] in msgs]
        v = [x for x in v if x != "na"]; out[arm] = f"{sum(v)}/{len(v)}"
    return out
for key in ("d", "p", "r", "b", "l"):
    for msgs, lab in ((("r1",), "r1 top bar"), (("r2",), "r2 overlay"), (("r1", "r2"), "r1+r2")):
        lines.append(f"relocate {key} {lab}: {cnt('relocate', msgs, key)}")
for key in ("n", "r", "b", "l"): lines.append(f"relocate {key} r3 position-only: {cnt('relocate', ('r3',), key)}")
for key in ("l", "w", "r4", "g", "h", "t", "c"): lines.append(f"handoff {key}: {cnt('handoff', ('t9', 't10'), key)}")
reads = json.loads((D/"design-reads.json").read_text(encoding="utf-8"))
lines.append("handoff per trial (l w r4 g h t c): " + "; ".join(f"{t} " + "".join(str(grades[t]['scores'][k]) for k in ('l', 'w', 'r4', 'g', 'h', 't', 'c')) for t in sorted(grades) if t.startswith("q")))
lines.append("relocate per trial (kind d p n): " + "; ".join(f"{t} {grades[t]['kind']} " + " ".join(str(grades[t]['scores'][k]) for k in ('d', 'p', 'n')) for t in sorted(grades) if t.startswith("a")))
(D/"summary.txt").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="")
print("\n".join(lines))
