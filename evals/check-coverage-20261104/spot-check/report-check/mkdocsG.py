# mkdocsG.py : arm G = F + a report check script (scripts/report-check.mjs) and one instruction to run it before sending.
import pathlib, shutil
V = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-06-gomoku-w3")
G = V/"docs-G"
if G.exists(): shutil.rmtree(G)
shutil.copytree(V/"docs-F", G)
(G/"scripts").mkdir()
b = (V/"docs-G-src"/"report-check.mjs").read_bytes(); assert b"\r" not in b
(G/"scripts"/"report-check.mjs").write_bytes(b)
def sub(path, pairs):
    p = G/path; s = p.read_bytes().decode("utf-8")
    for old, new in pairs:
        assert s.count(old) == 1, (path, old[:40], s.count(old)); s = s.replace(old, new)
    assert "\r" not in s; p.write_bytes(s.encode("utf-8"))
sub("SKILL.md", [
("""   A line that is not spot-checked is never listed as resolved, verified or done.
   The project's report format decides the sections; this decides the form of each
""",
"""   A line that is not spot-checked is never listed as resolved, verified or done.
   Before sending, save the report text to a file and run this skill's
   `scripts/report-check.mjs` on it (`node <skill folder>/scripts/report-check.mjs
   <file>`); correct each finding in the text and rerun until it prints `ok`, then
   send that text. It reads the form of the sentences, not whether a number is true.
   If it cannot run, say so in the report.
   The project's report format decides the sections; this decides the form of each
"""),
])
sub("references/conformance.md", [
("""count, not a result. A line that is not spot-checked is never listed as resolved,
verified or done.
""",
"""count, not a result. A line that is not spot-checked is never listed as resolved,
verified or done. Before a report is sent its text is run through
`scripts/report-check.mjs`, which flags a missing results list, a fix line whose
result is not `fixed` or `changed`, and a check outcome stated outside the list
without its scope, rendered-or-code and spot check outcome; the report is corrected
until it prints `ok`. The script reads the form of the text, not the truth of a number.
"""),
])
print("docs-G written:", sorted(str(p.relative_to(G)).replace("\\", "/") for p in G.rglob("*") if p.is_file()))
