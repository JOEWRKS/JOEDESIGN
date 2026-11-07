# mkdocsF.py : arm F = E + (1) fix line takes one of two words, fixed only with a direct observation,
# (2) every check outcome outside the list is followed by a parenthesis copied from its line.
import pathlib
V = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-06-gomoku-w3")
def sub(path, pairs):
    p = V/"docs-F"/path; s = p.read_bytes().decode("utf-8")
    for old, new in pairs:
        assert s.count(old) == 1, (path, old[:40], s.count(old)); s = s.replace(old, new)
    assert "\r" not in s; p.write_bytes(s.encode("utf-8"))
sub("SKILL.md", [
("""   the protected proof on the changed build. Material replacement of an approved
   direction needs scoped user approval after proof; internal review cannot grant it.
""",
"""   the protected proof on the changed build. A defect counts as fixed only after one
   direct observation of the fixed thing on a target that showed it (for clipping or
   overflow: the visible edges in a capture of that target, not the check's count);
   that observation is the fix's spot check. Material replacement of an approved
   direction needs scoped user approval after proof; internal review cannot grant it.
"""),
("""   scroll), before/after comparisons and a fix claimed from a check each take a
   line. Outside the list, the summary line included, a pass, a count, "fixed" or
   "no failures" is written only with its sizes x states and rendered-or-code in
   that same sentence; otherwise name the check and leave the outcome to its line.
   A line that is not spot-checked is never listed as resolved, verified or done.
""",
"""   scroll), before/after comparisons and each fix take a line. A fix line's result
   is one of two words: `fixed` when its spot check cell holds the direct observation
   (`375x667 replay bubble: clipped 14 before / 0 after, capture`), otherwise
   `changed`. A `changed` fix keeps its issue open, and the report text, ISSUES and
   ROADMAP use the cell's word, not "removed", "closed" or "resolved". Outside the
   list, the summary line included, every design-check pass, count, "fixed" or "no
   failures" is followed by a parenthesis copied from its line: (sizes x states,
   rendered or code, spot check outcome). Write "spacing 918/918 (12 sizes x 6
   states, rendered; spot check differs: check 16 / observed 8)", not "the check
   passed, but ..."; a sentence with no room for the parenthesis names the check and
   leaves the outcome to its line.
   A line that is not spot-checked is never listed as resolved, verified or done.
"""),
])
sub("references/conformance.md", [
("""as overflow, clipping and scroll, before/after comparisons, and a fix claimed from a
check each take their own line. Outside the list, the summary line included, a pass,
a count, "fixed" or "no failures" appears only with its sizes x states and
rendered-or-code in the same sentence; otherwise the sentence names the check and
leaves the outcome to its line. "939/939 passed" alone is a count, not a result. A
line that is not spot-checked is never listed as resolved, verified or done.
""",
"""as overflow, clipping and scroll, before/after comparisons, and each fix take their
own line. A defect counts as fixed only after one direct observation of the fixed
thing on a target that showed it (for clipping or overflow: the visible edges in a
capture, not the check's count). A fix line's result is `fixed` when its spot check
cell holds that observation, otherwise `changed`; a `changed` fix keeps its issue
open, and the report text, ISSUES and ROADMAP use the cell's word. Outside the list,
the summary line included, every design-check pass, count, "fixed" or "no failures"
is followed by a parenthesis copied from its line: (sizes x states, rendered or code,
spot check outcome); a sentence with no room for it names the check and leaves the
outcome to its line. "939/939 passed" alone, or "the check passed, but ...", is a
count, not a result. A line that is not spot-checked is never listed as resolved,
verified or done.
"""),
])
print("docs-F written")
