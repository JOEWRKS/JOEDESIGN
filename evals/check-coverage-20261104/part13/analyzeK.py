# analyzeK.py : 13부 (a) unblind grades, per-arm counts for every gate item, plus mechanical counts (mech.json).
import json, pathlib
D = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-10-joedesign-k")
mp = json.loads((D/"blind-map.json").read_text(encoding="utf-8")); trials = {t["id"]: t for t in json.loads((D/"trials.json").read_text(encoding="utf-8"))}
mech = json.loads((D/"mech.json").read_text(encoding="utf-8"))
grades = {tid: json.loads((D/"blind"/code/"grade.json").read_text(encoding="utf-8")) for tid, code in mp.items()}
(D/"grades.json").write_text(json.dumps({t: {"code": mp[t], **g} for t, g in sorted(grades.items())}, ensure_ascii=False, indent=1), encoding="utf-8", newline="")
want = {"r1": "A", "r2": "B", "r3": "C", "t4": "A", "t35": "D"}
out = []
for tid, t in sorted(trials.items()):
    if t["kind"] in ("relocate", "feature") and grades[tid].get("kind") != want[t["msg"]]:
        out.append(f"KIND MISMATCH {tid} grader={grades[tid].get('kind')} msg={t['msg']}")
def sc(tid, key, part=None):
    g = grades[tid]; s = (g.get(part) or {}).get("scores", {}) if part else g.get("scores", {})
    return s.get(key)
def cnt(sel, key, part=None):
    res = {}
    for arm in ("K", "L"):
        v = [sc(t, key, part) for t in trials if trials[t]["arm"] == arm and sel(trials[t])]
        v = [x for x in v if x not in (None, "na")]; res[arm] = f"{sum(int(x) for x in v)}/{len(v)}"
    return res
rel = lambda msgs: (lambda t: t["kind"] == "relocate" and t["msg"] in msgs)
for key in ("d", "p", "o", "r", "b", "l"):
    for msgs, lab in ((("r1",), "r1"), (("r2",), "r2"), (("r1", "r2"), "r1+r2")):
        out.append(f"relocate {key} {lab}: {cnt(rel(msgs), key, 'relocate')}")
for key in ("n", "o", "r", "b", "l"): out.append(f"relocate {key} r3: {cnt(rel(('r3',)), key, 'relocate')}")
feat = lambda msgs: (lambda t: t["kind"] == "feature" and t["msg"] in msgs)
for key in ("p1", "p2", "p3", "p4", "p5", "g", "l"):
    out.append(f"feature {key} t4/t35/all: {cnt(feat(('t4',)), key, 'feature')} {cnt(feat(('t35',)), key, 'feature')} {cnt(feat(('t4', 't35')), key, 'feature')}")
for key in ("p", "o"): out.append(f"feature(top bar) relocate-{key}: {cnt(feat(('t4',)), key, 'relocate')}")
for key in ("l", "w", "r4", "g", "h", "t", "c"): out.append(f"handoff {key}: {cnt(lambda t: t['kind'] == 'handoff', key)}")
for key in ("b", "c", "f", "g", "h", "s", "t", "u"):
    out.append(f"regression {key} browser/offline: {cnt(lambda t: t['kind'] == 'browser', key)} {cnt(lambda t: t['kind'] == 'offline', key)}")
def mc(sel, f):
    r = {}
    for arm in ("K", "L"):
        ids = [t for t in trials if trials[t]["arm"] == arm and sel(trials[t])]; r[arm] = f"{sum(1 for t in ids if f(mech[t]))}/{len(ids)}"
    return r
skill = lambda t: t["kind"] != "handoff"
for lab, sel in (("relocate", lambda t: t["kind"] == "relocate"), ("feature", lambda t: t["kind"] == "feature"), ("browser", lambda t: t["kind"] == "browser"), ("offline", lambda t: t["kind"] == "offline")):
    out.append(f"mech {lab}: state.json {mc(sel, lambda m: m['state_json'])} spec {mc(sel, lambda m: m['spec'])} script-run {mc(sel, lambda m: m['report_check_runs'] > 0)} "
               f"stamp-match {mc(sel, lambda m: m['verify_own'].startswith('stamp: match'))} K-script-clean {mc(sel, lambda m: not m['k_script_rules'])} ba-lines {mc(sel, lambda m: m['ba_lines'] > 0)}")
out.append("relocate per trial (kind d p n o): " + "; ".join(f"{t} {grades[t]['kind']} " + " ".join(str(sc(t, k, 'relocate')) for k in ('d', 'p', 'n', 'o')) for t in sorted(trials) if trials[t]['kind'] == 'relocate'))
out.append("feature per trial (p1..p5 g l | rel p o): " + "; ".join(f"{t} " + "".join(str(sc(t, k, 'feature')) for k in ('p1', 'p2', 'p3', 'p4', 'p5', 'g', 'l')) + (" | " + "".join(str(sc(t, k, 'relocate')) for k in ('p', 'o')) if grades[t].get('relocate') else "") for t in sorted(trials) if trials[t]['kind'] == 'feature'))
out.append("handoff per trial (l w r4 g h t c): " + "; ".join(f"{t} " + "".join(str(sc(t, k)) for k in ('l', 'w', 'r4', 'g', 'h', 't', 'c')) for t in sorted(trials) if trials[t]['kind'] == 'handoff'))
(D/"summary.txt").write_text("\n".join(out) + "\n", encoding="utf-8", newline="")
print("\n".join(out))
