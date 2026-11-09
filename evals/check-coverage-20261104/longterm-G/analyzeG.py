# analyzeG.py : direct counts per arm over turns/<arm>/tNN-report.md — report-check findings (run now with the repo script),
# six-bullet 해결 line containing a `changed` fix, product-definition mentions, script runs from script-usage.json (G only).
import json, pathlib, re, subprocess, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
L = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-04-joedesign-longterm")
S = "D:/JOEWRKS/JOEDESIGN/skills/joedesign/scripts/report-check.mjs"
backlog = {t["n"]: t for t in json.loads((L/"backlog.json").read_text(encoding="utf-8"))}
usage = json.loads((L/"turns/G/script-usage.json").read_text(encoding="utf-8")) if (L/"turns/G/script-usage.json").exists() else {}
out = {}
for arm in ("A", "B", "G"):
    rows = []
    for n in range(1, 41):
        p = L/"turns"/arm/f"t{n:02d}-report.md"
        if not p.exists(): continue
        txt = p.read_text(encoding="utf-8")
        r = subprocess.run(["node", S, str(p)], capture_output=True, text=True, encoding="utf-8")
        findings = [l for l in r.stdout.splitlines() if l.startswith(("report [", "line "))]
        rules = sorted({re.search(r"\[(R\d)\]", l).group(1) for l in findings if re.search(r"\[(R\d)\]", l)})
        has_list = not any("[R1]" in l for l in findings)
        bare = any("[R3]" in l for l in findings)
        sol = re.search(r"해결[:：\*]*\s*(.*)", txt)
        sol_line = sol.group(1)[:200] if sol else ""
        changed_in_sol = bool(sol and re.search(r"changed", sol_line))
        pd = "product-definition" in txt or "MASTER_PLANNING" in txt or "기획서" in txt
        runs = usage.get(f"t{n:02d}", []) if arm == "G" else None
        rows.append({"turn": n, "kind": backlog[n]["kind"], "findings": len(findings), "rules": rules, "list": has_list, "bareR3": bare,
                     "changed_in_haegyeol": changed_in_sol, "product_def_mention": pd, "runs": runs, "chars": len(txt)})
    out[arm] = rows
    main = [r for r in rows if r["kind"] == "main"]; hand = [r for r in rows if r["kind"] == "handoff"]
    def c(sel, k): return sum(1 for r in sel if r[k])
    print(f"{arm}: turns {len(rows)} | script-clean(0 findings) main {len(main)-sum(1 for r in main if r['findings'])}/{len(main)} handoff {len(hand)-sum(1 for r in hand if r['findings'])}/{len(hand)}"
          f" | no-list(R1) main {len(main)-c(main,'list')} | bare-outcome(R3) main {c(main,'bareR3')} handoff {c(hand,'bareR3')}"
          f" | changed-under-해결 {c(rows,'changed_in_haegyeol')} | product-def mention {c(rows,'product_def_mention')}")
    if arm == "G":
        ran = [r for r in main if r["runs"]]; print(f"   G script runs: main turns with ≥1 run {len(ran)}/{len(main)}; turns with none: {[r['turn'] for r in main if not r['runs']]}; first-run not ok: {[(r['turn'], r['runs'][0]) for r in ran if r['runs'][0] != 'ok']}")
        print("   main turns with findings now:", [(r["turn"], r["rules"]) for r in main if r["findings"]])
(L/"analysisG.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
