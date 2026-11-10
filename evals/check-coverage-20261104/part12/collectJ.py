# collectJ.py : (1) final report of each trial from its agent transcript, (2) DESIGN.md reads in handoff trials
# (did the session see the top "Reporting" line / the Report Form section), (3) blind packets with arm letters scrubbed.
# Usage: collectJ.py <subagents transcript dir>
import json, pathlib, subprocess, random, shutil, sys, re
D = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-10-joedesign-j"); T = pathlib.Path(sys.argv[1])
amap = json.loads((D/"agent-map.json").read_text(encoding="utf-8")); trials = {t["id"]: t for t in json.loads((D/"trials.json").read_text(encoding="utf-8"))}
(D/"reports").mkdir(exist_ok=True)
def calls(aid):
    out, final = [], None
    for line in (T/f"agent-{aid}.jsonl").read_text(encoding="utf-8").splitlines():
        try: o = json.loads(line)
        except Exception: continue
        m = o.get("message") or {}; c = m.get("content")
        if m.get("role") == "assistant" and isinstance(c, list):
            txt = "".join(b.get("text", "") for b in c if isinstance(b, dict) and b.get("type") == "text")
            if txt.strip(): final = txt
            for b in c:  # the final report is delivered through the SubagentHandback tool
                if isinstance(b, dict) and b.get("type") == "tool_use" and b.get("name") == "SubagentHandback": final = b["input"]["message"]
            out += [b for b in c if isinstance(b, dict) and b.get("type") == "tool_use"]
    return out, final
reads = {}
for aid, tid in amap.items():
    cs, final = calls(aid); assert final, tid
    (D/"reports"/f"{tid}.md").write_text(final.strip() + "\n", encoding="utf-8", newline="")
    if trials[tid]["kind"] != "handoff": continue
    dm = (pathlib.Path(trials[tid]["root"])/".git"/"..").resolve()
    base = subprocess.run(["git", "-C", trials[tid]["root"], "show", "HEAD:DESIGN.md"], capture_output=True, text=True, encoding="utf-8").stdout.splitlines()
    top = next((i + 1 for i, l in enumerate(base) if l.startswith("**Reporting:**")), None); rf = next(i + 1 for i, l in enumerate(base) if l.startswith("## Report Form"))
    ev = []
    for b in cs:
        s = json.dumps(b["input"], ensure_ascii=False)
        if "DESIGN.md" not in s: continue
        inp = b["input"]
        if b["name"] == "Read" and str(inp.get("file_path", "")).replace("\\", "/").endswith("/DESIGN.md"):
            lo = int(inp.get("offset") or 1); hi = lo + int(inp.get("limit") or 2000) - 1
            ev.append({"tool": "Read", "lines": [lo, hi], "top": bool(top and lo <= top <= hi), "rf": lo <= rf <= hi})
        elif b["name"] == "Grep":
            ev.append({"tool": "Grep", "pattern": inp.get("pattern"), "top": None, "rf": None})
        else:
            ev.append({"tool": b["name"], "cmd": (inp.get("command") or s)[:300], "top": None, "rf": None})
    reads[tid] = {"top_line": top, "report_form_line": rf, "events": ev}
(D/"design-reads.json").write_text(json.dumps(reads, ensure_ascii=False, indent=1), encoding="utf-8", newline="")
# blind packets
B = D/"blind"; B.mkdir(exist_ok=True); mp = D/"blind-map.json"; mapping = json.loads(mp.read_text(encoding="utf-8")) if mp.exists() else {}
rng = random.Random(20261110); codes = [f"m{n:03d}" for n in range(1, 400)]; rng.shuffle(codes); used = set(mapping.values())
SKIP = (".cache/", "dist", "node_modules", "joedesign-skill/", "test-results/", "playwright-report/", "work/tmp/")
git = lambda root, *a: subprocess.run(["git", "-C", str(root), "-c", "core.quotepath=false", *a], capture_output=True, text=True, encoding="utf-8", errors="replace").stdout
batches = {"relocate": [], "handoff": []}
for tid, t in trials.items():
    root = pathlib.Path(t["root"]); code = mapping.get(tid) or next(c for c in codes if c not in used); mapping[tid] = code; used.add(code)
    out = B/code; out.mkdir(exist_ok=True)
    scrub = lambda s: re.sub(r"\b[aq]\d\d-[JI]\b", "<project>", s.replace(str(root), "<project>").replace(str(root).replace("\\", "/"), "<project>"))
    (out/"REPORT.md").write_text(scrub((D/"reports"/f"{tid}.md").read_text(encoding="utf-8")), encoding="utf-8", newline="")
    # the handoff J base differs from I only by the top DESIGN.md line; drop that line so the packet does not reveal the arm
    dtxt = (root/"DESIGN.md").read_text(encoding="utf-8")
    dtxt = re.sub(r"\n\*\*Reporting:\*\*[^\n]*\n", "\n", dtxt, count=1)
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
        for leak in (tid, "docs-J", "docs-I", "xbase-", "pbase-", "joedesign-j", "joedesign-i", "**Reporting:**"):
            assert leak not in body, (tid, f, leak)
    batches[t["kind"]].append(code)
mp.write_text(json.dumps(mapping, ensure_ascii=False, indent=1), encoding="utf-8", newline="")
(D/"grade-batches.json").write_text(json.dumps({k: sorted(v) for k, v in batches.items()}, indent=1), encoding="utf-8", newline="")
for k, v in batches.items(): print(k, " ".join(sorted(v)))
for tid, r in reads.items(): print(tid, [(e["tool"], e.get("lines") or e.get("pattern") or e.get("cmd", "")[:120], e["top"], e["rf"]) for e in r["events"]])
