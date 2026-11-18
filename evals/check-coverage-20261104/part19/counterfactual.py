# counterfactual.py (part19): no model runs. Re-runs part18's counterfactual against the 1.3.4 candidate
# report-check in this repo. For each real part18 report, write the index ("own css") lines' fourth cell as bare
# `rendered` (variant A), then also drop prose `(own css)` mentions (variant B), remove the stamp, and run the
# check without --verify. Usage: python -I evals/check-coverage-20261104/part19/counterfactual.py  -> counterfactual.tsv
import pathlib, re, subprocess
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent
CHK = str(ROOT / "skills" / "joedesign" / "scripts" / "report-check.mjs")
P18 = HERE.parent / "part18" / "behavior-ab"
TMP = HERE / "counterfactual-variants"; TMP.mkdir(exist_ok=True)  # the rewritten reports, kept for the record
rows = ["run\tvariant\tbare_index_lines\tR7\tother_findings\tR7_lines"]
for rep in sorted(P18.glob("runs/r0*/REPORT.md")):
    rid = rep.parent.name
    text = rep.read_text(encoding="utf-8")
    lines = [l for l in text.splitlines() if not re.match(r"^report-check: ok", l)]
    a = []; n = 0
    for l in lines:
        if l.count("|") >= 4 and re.search(r"\|\s*rendered \(own css\)\s*\|", l):
            l = re.sub(r"\|\s*rendered \(own css\)\s*\|", "| rendered |", l); n += 1
        a.append(l)
    for var, body in (("A_cell_only", a), ("B_cell_and_prose", [re.sub(r"\s*\(?rendered \(own css\)\)?|own css", "", l) if l.count("|") < 4 else l for l in a])):
        f = TMP / f"{rid}-{var}.md"; f.write_text("\n".join(body) + "\n", encoding="utf-8")
        r = subprocess.run(["node", CHK, str(f)], capture_output=True, text=True, encoding="utf-8")
        out = r.stdout + r.stderr
        r7 = re.findall(r"^.*\[R7\].*$", out, re.M)
        other = len(re.findall(r"\[R\d\w?\]", out)) - len(r7)
        rows.append(f"{rid}\t{var}\t{n}\t{len(r7)}\t{other}\t{' / '.join(x.split(':')[0] for x in r7)}")
(HERE / "counterfactual.tsv").write_text("\n".join(rows) + "\n", encoding="utf-8")
print("\n".join(rows))
