# mkK2.py : 13부 (a) 추가 인계 12회 (사용자 결정 "13회 추가 후 40턴"): q13~q18-K, q19~q24-L, same bases/prompts as mkK.py, ports 5749~5760.
import json, os, pathlib, subprocess, re
D = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-10-joedesign-k")
W3 = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-06-gomoku-w3")
NM = W3/"nm"/"node_modules"; REAL = pathlib.Path("D:/JOEWRKS/.claude-worktrees/AI-Gomoku").resolve()
DOCS = ["SKILL.md", "references/conformance.md", "references/operation.md", "references/visual-translation.md", "templates/DESIGN.md", "scripts/report-check.mjs"]
SPARSE = "/*\n!/work/design/shots/\n!/work/design/logo-candidates/\n!/work/evidence/\n"
def git(root, *a):
    r = subprocess.run(["git", "-C", str(root), *a], capture_output=True, text=True, encoding="utf-8", errors="replace")
    assert r.returncode == 0, (a, r.stderr); return r.stdout.strip()
def flatten(repo):
    seen = []; todo = [pathlib.Path(repo)/".git"/"objects"]
    while todo:
        od = todo.pop(0); alt = od/"info"/"alternates"
        if not alt.exists(): continue
        for line in alt.read_text(encoding="utf-8").splitlines():
            if not line.strip(): continue
            q = pathlib.Path(line.strip()); q = q if q.is_absolute() else (od/q).resolve()
            if q not in seen: seen.append(q); todo.append(q)
    (pathlib.Path(repo)/".git"/"objects"/"info"/"alternates").write_text("".join(str(s).replace(chr(92), "/") + chr(10) for s in seen), encoding="utf-8", newline="")
def clone(src, dst):
    subprocess.run(["git", "clone", "-q", "--shared", "--no-checkout", str(src), str(dst)], check=True)
    git(dst, "config", "core.sparseCheckout", "true"); git(dst, "config", "core.autocrlf", "false")
    (dst/".git"/"info"/"sparse-checkout").write_bytes(SPARSE.encode()); flatten(dst)
    git(dst, "checkout", "-q", "-B", "claude/ai-coach", "HEAD"); git(dst, "remote", "remove", "origin")
trials = json.loads((D/"trials.json").read_text(encoding="utf-8")); have = {t["id"] for t in trials}
ref = (D/"prompts"/"q01-K.txt").read_text(encoding="utf-8")  # template: root/ports/message are the only variables
MSG = {"t9": "src/style.css에서 설명 카드 안 보조 글자 12px를 13px로 올려줘.", "t10": "안내 줄(금수·엔진 알림) 안쪽 여백 좀 줄여. 너무 두꺼워."}
plan = [(f"q{13+i:02d}-K", "K", m) for i, m in enumerate(["t9", "t10"] * 3)] + [(f"q{19+i:02d}-L", "L", m) for i, m in enumerate(["t9", "t10"] * 3)]
for i, (tid, arm, msg) in enumerate(plan):
    dev = 5749 + i; test = dev - 1000; root = D/"trials"/tid
    if not root.exists():
        clone(D/f"pbase-{arm}", root)
        subprocess.run(["cmd", "/c", "mklink", "/J", str(root/"node_modules").replace("/", "\\"), str(NM).replace("/", "\\")], check=True, capture_output=True)
    tgt = pathlib.Path(os.readlink(root/"node_modules").replace("\\\\?\\", "")).resolve()
    assert tgt == NM.resolve() and tgt != REAL and REAL not in tgt.parents, (tid, tgt)
    assert git(root, "status", "--short") == "", tid
    for d in DOCS: assert (root/"joedesign-skill"/d).read_bytes() == (D/f"docs-{arm}"/d).read_bytes(), (tid, d)
    rs = str(root).replace("/", "\\")
    p = ref.replace("trials\\q01-K", "trials\\" + tid).replace("5731", str(dev)).replace("4731", str(test)).replace(MSG["t9"], MSG[msg])
    assert p.count(tid) == 1 and str(dev) in p and MSG[msg] in p
    (D/"prompts"/f"{tid}.txt").write_bytes(p.encode("utf-8"))
    if tid not in have: trials.append({"id": tid, "arm": arm, "kind": "handoff", "msg": msg, "root": rs, "base": f"pbase-{arm}", "head": git(root, "rev-parse", "--short", "HEAD"), "dev": dev, "test": test})
norm = lambda s: re.sub(r"\b(57|47)\d\d\b", "PORT", re.sub(r"trials\\[a-z]\d\d-[A-Z]", "T", s))
for tid, msg in (("q13-K", "t9"), ("q14-K", "t10"), ("q19-L", "t9"), ("q20-L", "t10")):
    refid = "q01-K" if msg == "t9" else "q02-K"
    assert norm((D/"prompts"/f"{tid}.txt").read_text(encoding="utf-8")) == norm((D/"prompts"/f"{refid}.txt").read_text(encoding="utf-8")), tid
(D/"trials.json").write_text(json.dumps(trials, ensure_ascii=False, indent=1), encoding="utf-8", newline="")
print(len(trials), "trials;", [t[0] for t in plan])
