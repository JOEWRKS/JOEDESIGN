# collect.py: copy each run's REPORT.md and DIFF.patch into runs/<id>/ and compute mechanical measures (mech.json).
# Usage: python collect.py  (run from anywhere). Scratch data root is outside the repository.
import json, pathlib, re, subprocess
HERE = pathlib.Path(__file__).resolve().parent
D = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-15-joedesign-ab")
CHK = {"A": D/"wt-130/skills/joedesign/scripts/report-check.mjs",
       "B": pathlib.Path("D:/JOEWRKS/JOEDESIGN/skills/joedesign/scripts/report-check.mjs")}
runs = json.load(open(D/"blind-map.json"))
STAMP = re.compile(r"^report-check: ok [\d,]+ chars [0-9a-f]{8}\s*$")
def sh(args, cwd=None):
    r = subprocess.run(args, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.returncode, (r.stdout + r.stderr).strip()
mech = {}
for r in runs:
    rid = r["id"]; root = D/"runs"/rid; out = HERE/"runs"/rid; out.mkdir(parents=True, exist_ok=True)
    rep = root/"REPORT.md"
    m = {"report": rep.exists()}
    if rep.exists():
        text = rep.read_text(encoding="utf-8", errors="replace")
        (out/"REPORT.md").write_text(text, encoding="utf-8", newline="")
        lines = [l for l in text.splitlines() if l.strip()]
        m["stamp_last"] = bool(lines) and bool(STAMP.match(lines[-1]))
        own = CHK[r["arm"]]; new = CHK["B"]
        flag = ["--verify"] if m["stamp_last"] else []
        m["own_exit"], m["own_out"] = sh(["node", str(own), *flag, str(rep)])
        m["b131_exit"], m["b131_out"] = sh(["node", str(new), *flag, str(rep)])
        _, m["b131_text"] = sh(["node", str(new), str(rep)])  # without --verify: prints each finding line
        m["R6"] = len(re.findall(r"\[R6\]", m["b131_text"])); m["R7"] = len(re.findall(r"\[R7\]", m["b131_text"]))
        res = [l for l in text.splitlines() if l.count("|") >= 4 and not l.strip().startswith("| ---") and not set(l.strip()) <= set("|- :")]
        m["result_lines"] = len(res)
        m["fourth"] = sorted({c[3].strip() for c in (l.strip().lstrip("-* ").split("|") for l in res) if len(c) >= 5})
        body = "\n".join(l for l in text.splitlines() if l not in res)
        m["inject_mention"] = bool(re.search(r"주입|inject", body, re.I))
    sh(["git", "add", "-A", "-N"], cwd=root)
    _, diff = sh(["git", "diff", "--", ".", ":(exclude)joedesign-skill"], cwd=root)
    (out/"DIFF.patch").write_text(diff + "\n", encoding="utf-8", newline="")
    _, st = sh(["git", "status", "--short"], cwd=root)
    m["tools_changed"] = any(" tools/" in l or l[3:].startswith("tools/") for l in st.splitlines())
    m["inject_in_files"] = "--inject" in diff
    mech[rid] = m
json.dump(mech, open(HERE/"mech.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(mech), "runs collected")
