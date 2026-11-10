# collectJ2.py : 13부 (b) blind packets for G t01..t40 (part 9) and J2 t01..t40 (part 13) with fresh codes in blind-K/,
# 10 grader batches of 8 mixing both arms (same packet format and grader prompt as part 9: TURN.md, REPORT.md, DESIGN.md, DESIGN-prev.md).
# Arm tells removed: fixture folder names (L-G / L-J2) and the report-check stamp line (G predates the stamp). The J2 reports'
# "Display before/after" lines are content and stay (a known limit of blinding).
import json, pathlib, random, re
L = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-04-joedesign-longterm")
B = L / "blind-K"; B.mkdir(exist_ok=True)
backlog = {t["n"]: t for t in json.loads((L / "backlog.json").read_text(encoding="utf-8"))}
rng = random.Random(20261111)
codes = [f"k{n:03d}" for n in range(1, 400)]; rng.shuffle(codes)
STAMP = re.compile(r"^report-check: ok [\d,]+ chars [0-9a-f]{8}\s*$", re.M)
def scrub(s):
    s = STAMP.sub("", s)
    for a in ("L-J2", "L-G", "L-J"): s = s.replace("joedesign-longterm\\" + a, "joedesign-longterm\\<project>").replace("joedesign-longterm/" + a, "joedesign-longterm/<project>")
    return s.rstrip("\n") + "\n"
mapping = {}; i = 0
for arm in ("G", "J2"):
    for n in range(1, 41):
        key = f"{arm}-t{n:02d}"; code = codes[i]; i += 1; mapping[key] = code
        out = B / code; out.mkdir(exist_ok=True)
        assert not (out / "grade.json").exists(), code
        T = L / "turns" / arm
        (out / "REPORT.md").write_text(scrub((T / f"t{n:02d}-report.md").read_text(encoding="utf-8")), encoding="utf-8", newline="")
        (out / "DESIGN.md").write_text(scrub((T / f"t{n:02d}-DESIGN.md").read_text(encoding="utf-8")), encoding="utf-8", newline="")
        (out / "DESIGN-prev.md").write_text(scrub((T / f"t{n-1:02d}-DESIGN.md").read_text(encoding="utf-8")), encoding="utf-8", newline="")
        changed = (T / f"t{n:02d}-changed.txt").read_text(encoding="utf-8")
        t = backlog[n]; kind = "스킬 없는 인계 세션" if t["kind"] == "handoff" else "주 세션"
        body = "# 턴 " + str(n) + " (" + kind + ")\n\n사용자 메시지:\n> " + t["msg"] + "\n\n이 턴에서 바뀐 파일:\n" + (changed or "(없음)") + "\n"
        (out / "TURN.md").write_text(body, encoding="utf-8", newline="")
        for f in ("REPORT.md", "DESIGN.md", "DESIGN-prev.md"):
            txt = (out / f).read_text(encoding="utf-8")
            assert "L-J2" not in txt and "\\L-G" not in txt and "/L-G" not in txt and not STAMP.search(txt), (key, f)
(L / "blind-K-map.json").write_text(json.dumps(mapping, ensure_ascii=False, indent=1), encoding="utf-8", newline="")
allc = sorted(mapping.values()); rng.shuffle(allc)
batches = [sorted(allc[j:j + 8]) for j in range(0, 80, 8)]
(L / "grader-batches-K.json").write_text(json.dumps(batches, indent=1), encoding="utf-8", newline="")
inv = {v: k for k, v in mapping.items()}
for b in batches: print(" ".join(b), "| G", sum(inv[c].startswith("G") for c in b), "J2", sum(inv[c].startswith("J2") for c in b))
