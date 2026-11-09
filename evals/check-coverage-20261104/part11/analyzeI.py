# analyzeI.py : direct counts from each trial's subagent transcript (not blind).
#  - product-definition reads (state.json / MASTER_PLANNING_SPEC / approval_status) in tool_use inputs
#  - report-check.mjs runs and each run's first output line (ok / N finding(s) / error)
#  - final report text: saved to reports/<tid>.md (last assistant text), stamp line present, --verify result
import json, pathlib, re, subprocess, sys, collections
D = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-09-joedesign-i")
S = pathlib.Path("<home>/.claude/projects/D--JOEWRKS/f551ee21-9732-4612-854f-b4ef34b2501e/subagents")
RC = D/"docs-I"/"scripts"/"report-check.mjs"
m = json.loads((D/"agent-map.json").read_text(encoding="utf-8"))
PD = re.compile(r"product-definition|state\.json|MASTER_PLANNING_SPEC|approval_status|approval-manifest", re.I)
out = {}
for aid, tid in sorted(m.items(), key=lambda kv: kv[1]):
    f = S/f"agent-{aid}.jsonl"
    if not f.exists(): continue
    recs = []
    for line in f.open(encoding="utf-8", errors="replace"):
        try: recs.append(json.loads(line))
        except Exception: pass
    pd_reads = []; rc_runs = []; pending = {}; last_text = None; tool_uses = 0
    for o in recs:
        msg = o.get("message") if isinstance(o.get("message"), dict) else None
        if not msg: continue
        c = msg.get("content")
        if isinstance(c, str): c = [{"type": "text", "text": c}]
        if not isinstance(c, list): continue
        for it in c:
            if not isinstance(it, dict): continue
            if it.get("type") == "tool_use" and it.get("name") == "SubagentHandback":
                last_text = it.get("input", {}).get("message"); continue
            if it.get("type") == "tool_use":
                tool_uses += 1
                s = json.dumps(it.get("input"), ensure_ascii=False)
                if PD.search(s) and it.get("name") in ("Bash", "Read", "Grep", "Glob", "PowerShell"):
                    pd_reads.append(it.get("name") + ": " + (it.get("input", {}).get("command") or it.get("input", {}).get("file_path") or it.get("input", {}).get("pattern") or "")[:120])
                if "report-check" in s and it.get("name") in ("Bash", "PowerShell"):
                    pending[it.get("id")] = (it.get("input", {}).get("command") or "")[:200]
            elif it.get("type") == "tool_result" and it.get("tool_use_id") in pending:
                body = it.get("content")
                if isinstance(body, list): body = "\n".join(x.get("text", "") for x in body if isinstance(x, dict))
                body = (body or "").strip()
                first = next((l for l in body.split("\n") if l.strip()), "")
                mm = re.search(r"report-check: ok [\d,]+ chars [0-9a-f]{8}", body)
                rc_runs.append(mm.group(0) if mm else ("findings: " + str(len(re.findall(r"^\s*(?:\S+\.(?:md|txt)|REPORT|report)?:?\d+\s+R\d", body, re.M))) if " R" in body else first[:100]))
                pending.pop(it.get("tool_use_id"))
    rep = (D/"reports"/f"{tid}.md")
    if last_text and (not rep.exists() or "--force" in sys.argv):
        rep.write_text(last_text.rstrip("\n") + "\n", encoding="utf-8", newline="\n")
    stamp = None; verify = None
    if rep.exists():
        txt = rep.read_text(encoding="utf-8")
        mm = re.search(r"report-check: ok [\d,]+ chars [0-9a-f]{8}\s*$", txt.strip())
        stamp = mm.group(0).strip() if mm else None
        r = subprocess.run(["node", str(RC), "--verify", str(rep)], capture_output=True, text=True, encoding="utf-8", errors="replace")
        verify = {"exit": r.returncode, "out": (r.stdout + r.stderr).strip().split("\n")[0][:120]}
        r2 = subprocess.run(["node", str(RC), str(rep)], capture_output=True, text=True, encoding="utf-8", errors="replace")
        check_now = {"exit": r2.returncode, "findings": [l[:120] for l in (r2.stdout + r2.stderr).strip().split("\n") if l.strip()][:6]}
    else:
        check_now = None
    out[tid] = {"agent": aid, "records": len(recs), "tool_uses": tool_uses, "done": last_text is not None,
                "product_definition_reads": pd_reads, "report_check_runs": rc_runs, "stamp": stamp, "verify": verify, "check_now": check_now}
(D/"analysis.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8", newline="")
for tid, v in out.items():
    print(f"{tid}: done={v['done']} tools={v['tool_uses']} pd_reads={len(v['product_definition_reads'])} rc_runs={v['report_check_runs']} stamp={'yes' if v['stamp'] else 'no'} verify={v['verify'] and v['verify']['exit']} check_now={v['check_now'] and v['check_now']['exit']}")
