# done.py <jsonl>...: exit 0 when every transcript has an assistant SubagentHandback tool call
import json, sys
ok = True
for p in sys.argv[1:]:
    hit = False
    try:
        for l in open(p, encoding="utf-8", errors="replace"):
            try: d = json.loads(l)
            except Exception: continue
            if d.get("type") != "assistant": continue
            for c in (d.get("message") or {}).get("content") or []:
                if isinstance(c, dict) and c.get("type") == "tool_use" and "Handback" in (c.get("name") or ""): hit = True
    except FileNotFoundError: pass
    ok = ok and hit
sys.exit(0 if ok else 1)
