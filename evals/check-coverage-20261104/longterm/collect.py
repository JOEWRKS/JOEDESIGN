# Blind per-turn packets for the long-term A/B: blind/<code>/ = {TURN.md (user msg + changed files), REPORT.md, DESIGN.md (after), DESIGN-prev.md}
import json, pathlib, random, shutil
L = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-04-joedesign-longterm")
B = L / "blind"; B.mkdir(exist_ok=True)
backlog = {t["n"]: t for t in json.loads((L/"backlog.json").read_text(encoding="utf-8"))}
map_path = B / "map.json"
mapping = json.loads(map_path.read_text(encoding="utf-8")) if map_path.exists() else {}
rng = random.Random(20261106); codes = [f"p{n:03d}" for n in range(1, 400)]; rng.shuffle(codes); used = set(mapping.values())
done = 0
for arm in ("A", "B"):
    for n in range(1, 41):
        rep = L/"turns"/arm/f"t{n:02d}-report.md"
        if not rep.exists(): continue
        key = f"{arm}-t{n:02d}"; code = mapping.get(key) or next(c for c in codes if c not in used); mapping[key] = code; used.add(code)
        out = B/code; out.mkdir(exist_ok=True)
        shutil.copyfile(rep, out/"REPORT.md")
        shutil.copyfile(L/"turns"/arm/f"t{n:02d}-DESIGN.md", out/"DESIGN.md")
        prev = L/"turns"/arm/f"t{n-1:02d}-DESIGN.md"
        shutil.copyfile(prev, out/"DESIGN-prev.md")
        changed = (L/"turns"/arm/f"t{n:02d}-changed.txt").read_text(encoding="utf-8")
        t = backlog[n]
        (out/"TURN.md").write_text(f"# 턴 {n} ({'스킬 없는 인계 세션' if t['kind']=='handoff' else '주 세션'})\n\n사용자 메시지:\n> {t['msg']}\n\n이 턴에서 바뀐 파일:\n{changed or '(없음)'}\n", encoding="utf-8")
        done += 1
map_path.write_text(json.dumps(mapping, ensure_ascii=False, indent=1), encoding="utf-8")
print("packets", done)
