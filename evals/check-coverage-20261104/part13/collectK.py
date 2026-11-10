# collectK.py : 13부. (1) final report of each trial from its agent transcript (and a check that the first prompt equals prompts/<id>.txt),
# (2) mechanical counts from the tool calls (product-definition reads, report-check runs, DESIGN.md Report Form reads),
# (3) stamp --verify on each sent report, (4) blind packets with arm letters scrubbed.
# Usage: collectK.py <subagents transcript dir> [<more dirs>...]
import json, pathlib, subprocess, random, sys, re
D = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-10-joedesign-k"); TS = [pathlib.Path(p) for p in sys.argv[1:]]
amap = json.loads((D/"agent-map.json").read_text(encoding="utf-8")); trials = {t["id"]: t for t in json.loads((D/"trials.json").read_text(encoding="utf-8"))}
(D/"reports").mkdir(exist_ok=True)
def transcript(aid):
    for T in TS:
        p = T/f"agent-{aid}.jsonl"
        if p.exists(): return p
    raise FileNotFoundError(aid)
def calls(aid):
    out, final, first = [], None, None
    for line in transcript(aid).read_text(encoding="utf-8").splitlines():
        try: o = json.loads(line)
        except Exception: continue
        m = o.get("message") or {}; c = m.get("content")
        if m.get("role") == "user" and first is None:
            first = c if isinstance(c, str) else "".join(b.get("text", "") for b in (c or []) if isinstance(b, dict) and b.get("type") == "text")
        if m.get("role") == "assistant" and isinstance(c, list):
            txt = "".join(b.get("text", "") for b in c if isinstance(b, dict) and b.get("type") == "text")
            if txt.strip(): final = txt
            for b in c:
                if isinstance(b, dict) and b.get("type") == "tool_use" and b.get("name") == "SubagentHandback": final = b["input"]["message"]
            out += [b for b in c if isinstance(b, dict) and b.get("type") == "tool_use"]
    return out, final, first
mech = {}
for aid, tid in amap.items():
    cs, final, first = calls(aid); assert final, tid
    want = (D/"prompts"/f"{tid}.txt").read_text(encoding="utf-8").strip()
    prompt_ok = (first or "").strip() == want
    (D/"reports"/f"{tid}.md").write_text(final.strip() + "\n", encoding="utf-8", newline="")
    s_all = [json.dumps(b["input"], ensure_ascii=False) for b in cs]
    rc_runs = [s for s in s_all if "report-check" in s]
    m = {"prompt_ok": prompt_ok, "tool_calls": len(cs),
         "state_json": any("state.json" in s for s in s_all), "spec": any("MASTER_PLANNING_SPEC" in s for s in s_all),
         "report_check_runs": len(rc_runs), "report_check_verify": any("--verify" in s for s in rc_runs),
         "r5_seen": None}
    t = trials[tid]
    if t["kind"] == "handoff":
        base = subprocess.run(["git", "-C", t["root"], "show", "HEAD:DESIGN.md"], capture_output=True, text=True, encoding="utf-8").stdout.splitlines()
        rf = next(i + 1 for i, l in enumerate(base) if l.startswith("## Report Form"))
        ev = []
        for b in cs:
            inp = b["input"]; s = json.dumps(inp, ensure_ascii=False)
            if "DESIGN.md" not in s: continue
            if b["name"] == "Read" and str(inp.get("file_path", "")).replace("\\", "/").endswith("/DESIGN.md"):
                lo = int(inp.get("offset") or 1); hi = lo + int(inp.get("limit") or 2000) - 1
                ev.append({"tool": "Read", "lines": [lo, hi], "rf": lo <= rf <= hi})
            elif b["name"] == "Grep": ev.append({"tool": "Grep", "pattern": inp.get("pattern"), "rf": None})
            else: ev.append({"tool": b["name"], "cmd": (inp.get("command") or s)[:300], "rf": None})
        m["report_form_line"] = rf; m["design_reads"] = ev
    mech[tid] = m
# stamp verify and findings with each arm's own script, and with the K script (R5) on every report
for tid, t in trials.items():
    if tid not in mech: continue
    rep = D/"reports"/f"{tid}.md"
    own = subprocess.run(["node", str(D/f"docs-{t['arm']}"/"scripts"/"report-check.mjs"), "--verify", str(rep)], capture_output=True, text=True, encoding="utf-8")
    k = subprocess.run(["node", str(D/"docs-K"/"scripts"/"report-check.mjs"), str(rep)], capture_output=True, text=True, encoding="utf-8")
    mech[tid]["verify_own"] = own.stdout.strip().splitlines()[0] if own.stdout.strip() else own.stderr.strip()
    mech[tid]["k_script_rules"] = sorted(set(re.findall(r"\[(R\d)\]", k.stdout)))
    txt = rep.read_text(encoding="utf-8")
    mech[tid]["ba_lines"] = len(re.findall(r"(?mi)^\s*(?:[-*+]\s*)?\**\s*(?:before|after)\s*\**\s*[:：]", txt))
    mech[tid]["pending_in_report"] = bool(re.search(r"product decision pending|제품\s*결정\s*대기", txt, re.I))
(D/"mech.json").write_text(json.dumps(mech, ensure_ascii=False, indent=1), encoding="utf-8", newline="")
# blind packets
B = D/"blind"; B.mkdir(exist_ok=True); mp = D/"blind-map.json"; mapping = json.loads(mp.read_text(encoding="utf-8")) if mp.exists() else {}
rng = random.Random(20261111); codes = [f"k{n:03d}" for n in range(1, 400)]; rng.shuffle(codes); used = set(mapping.values())
SKIP = (".cache/", "dist", "node_modules", "joedesign-skill/", "test-results/", "playwright-report/", "work/tmp/")
git = lambda root, *a: subprocess.run(["git", "-C", str(root), "-c", "core.quotepath=false", *a], capture_output=True, text=True, encoding="utf-8", errors="replace").stdout
tplK = (D/"docs-K"/"templates"/"DESIGN.md").read_text(encoding="utf-8")
NEWPARA = tplK[tplK.index("A change that moves, overlaps"):tplK.index("## Open Decisions")].strip()
group = {"relocate": "rf", "feature": "rf", "handoff": "handoff", "browser": "regression", "offline": "regression"}
batches = {"rf": [], "handoff": [], "regression": []}
for tid, t in trials.items():
    if tid not in mech: continue
    root = pathlib.Path(t["root"]); code = mapping.get(tid) or next(c for c in codes if c not in used); mapping[tid] = code; used.add(code)
    out = B/code; out.mkdir(exist_ok=True)
    scrub = lambda s: re.sub(r"\b[afqyz]\d\d-[KL]\b", "<project>", s.replace(str(root), "<project>").replace(str(root).replace("\\", "/"), "<project>"))
    (out/"REPORT.md").write_text(scrub((D/"reports"/f"{tid}.md").read_text(encoding="utf-8")), encoding="utf-8", newline="")
    dtxt = (root/"DESIGN.md").read_text(encoding="utf-8")
    if t["kind"] == "handoff": dtxt = dtxt.replace(" " + NEWPARA, "").replace("\n" + NEWPARA, "")  # the base K Report Form paragraph would reveal the arm
    (out/"DESIGN.md").write_text(scrub(dtxt), encoding="utf-8", newline="")
    diff = git(root, "diff", "HEAD", "--", ".", ":!joedesign-skill", ":!package-lock.json")
    parts = [f"# diff base..worktree (joedesign-skill excluded)\n{diff}"]
    for p in [p for p in git(root, "ls-files", "--others", "--exclude-standard").split("\n") if p and not p.startswith(SKIP)]:
        f = root/p
        if f.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp", ".zip", ".woff2"): parts.append(f"# untracked binary {p} ({f.stat().st_size} bytes)"); continue
        try: body = f.read_text(encoding="utf-8")[:20000] if f.stat().st_size < 400000 else f"<{f.stat().st_size} bytes>"
        except Exception as e: body = f"<unreadable: {e}>"
        parts.append(f"# untracked file {p}\n{body}")
    (out/"DIFF.patch").write_text(scrub("\n\n".join(parts)), encoding="utf-8", newline="")
    for f in ("REPORT.md", "DESIGN.md", "DIFF.patch"):
        body = (out/f).read_text(encoding="utf-8", errors="replace")
        for leak in (tid, "docs-K", "docs-L", "xbase-", "pbase-", "wbase-", "obase-", "joedesign-k"):
            assert leak not in body, (tid, f, leak)
    batches[group[t["kind"]]].append(code)
mp.write_text(json.dumps(mapping, ensure_ascii=False, indent=1), encoding="utf-8", newline="")
(D/"grade-batches.json").write_text(json.dumps({k: sorted(v) for k, v in batches.items()}, indent=1), encoding="utf-8", newline="")
for k, v in batches.items(): print(k, len(v))
bad = [t for t, m in mech.items() if not m["prompt_ok"]]; print("prompt mismatch:", bad)
