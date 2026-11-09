# harvestG.py <agent-id> <turn> [arm]: saves the agent's latest final text as turns/<arm>/tNN-report.md
# and counts report-check.mjs runs (Bash/PowerShell tool_use) made since the previous harvest mark.
import json, pathlib, re, sys, io, glob
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
aid, n = sys.argv[1], int(sys.argv[2]); arm = sys.argv[3] if len(sys.argv) > 3 else "G"
L = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-04-joedesign-longterm")
S = pathlib.Path("<claude projects folder>")
files = sorted(glob.glob(str(S/"*"/"subagents"/f"*{aid}*.jsonl")), key=lambda p: pathlib.Path(p).stat().st_mtime)
assert files, "no transcript for " + aid
src = pathlib.Path(files[-1])
texts, runs, pending, lines, handbacks = [], [], {}, 0, []
for line in src.open(encoding="utf-8", errors="replace"):
    lines += 1
    try: o = json.loads(line)
    except Exception: continue
    msg = o.get("message") or {}
    for c in msg.get("content") or []:
        if not isinstance(c, dict): continue
        if o.get("type") == "assistant" and c.get("type") == "text" and c.get("text", "").strip(): texts.append((lines, c["text"]))
        if c.get("type") == "tool_use" and c.get("name") == "SendMessage" and (c.get("input") or {}).get("to") == "main" and c["input"].get("message"): texts.append((lines, c["input"]["message"])); handbacks.append((lines, c["input"]["message"]))
        if c.get("type") == "tool_use" and c.get("name") == "SubagentHandback" and (c.get("input") or {}).get("message"): texts.append((lines, c["input"]["message"])); handbacks.append((lines, c["input"]["message"]))
        if c.get("type") == "tool_use" and c.get("name") in ("Bash", "PowerShell") and "report-check.mjs" in json.dumps(c.get("input") or {}, ensure_ascii=False): pending[c["id"]] = lines
        if c.get("type") == "tool_result" and c.get("tool_use_id") in pending:
            t = c.get("content"); t = "\n".join(x.get("text", "") for x in t if isinstance(x, dict)) if isinstance(t, list) else str(t)
            hit = re.search(r"report-check: (ok|\d+ finding\(s\))", t); runs.append((pending.pop(c["tool_use_id"]), hit.group(1) if hit else "no-output:" + t.strip()[:50]))
mark = L/"turns"/arm/f"harvest-mark-{aid}.json"; prev = json.loads(mark.read_text()) if mark.exists() else {"line": 0}
assert texts and texts[-1][0] > prev["line"], "no new final text since last harvest"
rep = (handbacks[-1][1] if handbacks and handbacks[-1][0] > prev["line"] else texts[-1][1]); out = L/"turns"/arm/f"t{n:02d}-report.md"; out.write_bytes((rep.rstrip("\n") + "\n").encode("utf-8"))
turn_runs = [r for l, r in runs if l > prev["line"]]
usage = L/"turns"/arm/"script-usage.json"; u = json.loads(usage.read_text(encoding="utf-8")) if usage.exists() else {}
u[f"t{n:02d}"] = turn_runs; usage.write_text(json.dumps(u, ensure_ascii=False, indent=1), encoding="utf-8")
mark.write_text(json.dumps({"line": texts[-1][0], "turn": n}))
print(f"{arm} t{n:02d} report {len(rep)} chars | report-check runs {len(turn_runs)}: {' -> '.join(turn_runs) or '(none)'} | src {src.name}")
