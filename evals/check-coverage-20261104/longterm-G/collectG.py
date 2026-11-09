# collectG.py : blind packets for G t01..t40 (new q-codes) + B t01..t40 (existing codes re-copied); grader batches of 8 mixing both arms.
import json, pathlib, random, shutil
L = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-04-joedesign-longterm")
B = L / "blind"
backlog = {t["n"]: t for t in json.loads((L / "backlog.json").read_text(encoding="utf-8"))}
mp = B / "map.json"
mapping = json.loads(mp.read_text(encoding="utf-8"))
rng = random.Random(20261107)
codes = [f"q{n:03d}" for n in range(1, 400)]
rng.shuffle(codes)
used = set(mapping.values())
done = []
for arm in ("B", "G"):
    for n in range(1, 41):
        rep = L / "turns" / arm / f"t{n:02d}-report.md"
        assert rep.exists(), (arm, n)
        key = f"{arm}-t{n:02d}"
        code = mapping.get(key) or next(c for c in codes if c not in used)
        mapping[key] = code
        used.add(code)
        out = B / code
        out.mkdir(exist_ok=True)
        if arm == "G" and (out / "grade.json").exists():
            raise SystemExit("G packet already graded: " + code)
        shutil.copyfile(rep, out / "REPORT.md")
        shutil.copyfile(L / "turns" / arm / f"t{n:02d}-DESIGN.md", out / "DESIGN.md")
        shutil.copyfile(L / "turns" / arm / f"t{n-1:02d}-DESIGN.md", out / "DESIGN-prev.md")
        changed = (L / "turns" / arm / f"t{n:02d}-changed.txt").read_text(encoding="utf-8")
        t = backlog[n]
        kind = "스킬 없는 인계 세션" if t["kind"] == "handoff" else "주 세션"
        body = "# 턴 " + str(n) + " (" + kind + ")\n\n사용자 메시지:\n> " + t["msg"] + "\n\n이 턴에서 바뀐 파일:\n" + (changed or "(없음)") + "\n"
        (out / "TURN.md").write_text(body, encoding="utf-8")
        done.append(code)
mp.write_text(json.dumps(mapping, ensure_ascii=False, indent=1), encoding="utf-8")
codes_sorted = sorted(done)
batches = [codes_sorted[i:i + 8] for i in range(0, len(codes_sorted), 8)]
(L / "grader-batches-r2.json").write_text(json.dumps(batches, indent=1), encoding="utf-8")
print("packets", len(done), "batches", len(batches), "| B codes keep old p-codes:", sum(1 for c in done if c.startswith("p")), "| new q-codes:", sum(1 for c in done if c.startswith("q")))
