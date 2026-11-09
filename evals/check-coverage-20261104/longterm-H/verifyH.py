# verifyH.py <arm> : run report-check --verify on every harvested report of the arm; record stamp match per turn.
import json, pathlib, subprocess, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
L = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-04-joedesign-longterm"); arm = sys.argv[1]
S = str(L/"docs-H"/"scripts"/"report-check.mjs")
out = {}
for p in sorted((L/"turns"/arm).glob("t??-report.md")):
    r = subprocess.run(["node", S, "--verify", str(p)], capture_output=True, text=True, encoding="utf-8")
    out[p.stem[:3]] = r.stdout.strip(); print(p.stem[:3], r.stdout.strip())
(L/"turns"/arm/"stamp-verify.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
m = sum(1 for v in out.values() if v.startswith("stamp: match")); print(f"match {m}/{len(out)}")
