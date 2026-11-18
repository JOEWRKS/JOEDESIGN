# extract.py <transcript.jsonl> <run_root> <out_dir>
# Writes commands.log (every tool call: shell commands in full, file tools with their path)
# and outside.txt (tool calls whose paths point outside run_root).
import json, sys, pathlib, re
src, root, out = sys.argv[1], sys.argv[2], pathlib.Path(sys.argv[3])
rootn = root.replace("\\", "/").lower().rstrip("/")
lines, outside, final = [], [], ""
r7_results = 0
PATHRE = re.compile(r"[A-Za-z]:[\\/][^\s\"'`|;&<>)]*|/[a-z]/[^\s\"'`|;&<>)]*|/tmp[^\s\"'`|;&<>)]*", re.I)
def norm(p):
    p = p.replace("\\", "/")
    m = re.match(r"^/([a-z])/(.*)", p, re.I)
    if m: p = m.group(1) + ":/" + m.group(2)
    return p.lower()
for raw in open(src, encoding="utf-8", errors="replace"):
    try: ev = json.loads(raw)
    except Exception: continue
    msg = ev.get("message") or {}
    if not isinstance(msg, dict): continue
    content = msg.get("content")
    if not isinstance(content, list): continue
    for c in content:
        if not isinstance(c, dict): continue
        if c.get("type") == "tool_use":
            name, inp = c.get("name"), c.get("input") or {}
            if name in ("Bash", "PowerShell"):
                s = f"[{name}] {inp.get('command','')}"
            else:
                keys = {k: v for k, v in inp.items() if k in ("file_path", "path", "pattern", "url", "query", "notebook_path")}
                s = f"[{name}] {json.dumps(keys, ensure_ascii=False)}"
            lines.append(s)
            text = json.dumps(inp, ensure_ascii=False) if name not in ("Bash", "PowerShell") else inp.get("command", "")
            if name not in ("Bash", "PowerShell"): text = " ".join(str(v) for k, v in inp.items() if k in ("file_path", "path", "notebook_path"))
            for p in PATHRE.findall(text):
                n = norm(p)
                if len(n) > 3 and not n.startswith(rootn) and not n.startswith("c:/program files"):
                    outside.append(f"{name}: {p}")
            if name.startswith("mcp__"): outside.append(f"{name}: (mcp tool)")
            if "andback" in (name or ""):
                final = next((v for v in inp.values() if isinstance(v, str) and len(v) > 50), json.dumps(inp, ensure_ascii=False))
        if c.get("type") == "tool_result":
            cc = c.get("content"); s = json.dumps(cc, ensure_ascii=False) if not isinstance(cc, str) else cc
            if "[R7]" in s: r7_results += 1
        if msg.get("role") == "assistant" and c.get("type") == "text" and not final:
            lasttext = c.get("text", "")
out.mkdir(parents=True, exist_ok=True)
(out / "commands.log").write_text("\n".join(lines) + "\n", encoding="utf-8")
(out / "outside.txt").write_text("\n".join(sorted(set(outside))) + "\n", encoding="utf-8")
(out / "final-message.md").write_text(final, encoding="utf-8")
(out / "r7-during.txt").write_text(str(r7_results) + chr(10), encoding="utf-8")
print(r7_results, "tool results with [R7];", len(lines), "tool calls;", len(set(outside)), "outside paths")
