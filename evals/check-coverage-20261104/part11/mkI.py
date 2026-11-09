# mkI.py : 11부 (I안) trial clones. Bases from the w3 fixture trees; skill docs replaced (I = JOEDESIGN working tree, H = git HEAD 1.1.0).
# Every node_modules junction is verified to point at the private copy (os.readlink here; Get-Item .Target separately).
import json, os, pathlib, subprocess, re, sys
D = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-09-joedesign-i")
W3 = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-06-gomoku-w3")
JD = pathlib.Path("D:/JOEWRKS/JOEDESIGN")
NM = W3/"nm"/"node_modules"; REAL = pathlib.Path("D:/JOEWRKS/.claude-worktrees/AI-Gomoku").resolve()
DOCS = ["SKILL.md", "references/conformance.md", "references/operation.md", "references/visual-translation.md", "templates/DESIGN.md", "scripts/report-check.mjs"]
ID = ["-c", "user.name=JOEWRKS", "-c", "user.email=joewrks@example.invalid"]
SPARSE = "/*\n!/work/design/shots/\n!/work/design/logo-candidates/\n!/work/evidence/\n"
def git(root, *a):
    r = subprocess.run(["git", "-C", str(root), *a], capture_output=True, text=True, encoding="utf-8", errors="replace")
    assert r.returncode == 0, (a, r.stderr); return r.stdout.strip()
def clone(src, dst):
    subprocess.run(["git", "clone", "-q", "--shared", "--no-checkout", str(src), str(dst)], check=True)
    git(dst, "config", "core.sparseCheckout", "true"); git(dst, "config", "core.autocrlf", "false")
    (dst/".git"/"info"/"sparse-checkout").write_bytes(SPARSE.encode())
    flatten(dst)
    git(dst, "checkout", "-q", "-B", "claude/ai-coach", "HEAD"); git(dst, "remote", "remove", "origin")
def flatten(repo):
    # --shared clones of --shared clones nest alternates too deep; list every ancestor object store directly
    seen = []; todo = [pathlib.Path(repo)/".git"/"objects"]
    while todo:
        od = todo.pop(0); alt = od/"info"/"alternates"
        if not alt.exists(): continue
        for line in alt.read_text(encoding="utf-8").splitlines():
            if not line.strip(): continue
            q = pathlib.Path(line.strip()); q = q if q.is_absolute() else (od/q).resolve()
            if q not in seen: seen.append(q); todo.append(q)
    (pathlib.Path(repo)/".git"/"objects"/"info"/"alternates").write_text("".join(str(s).replace(chr(92), "/") + chr(10) for s in seen), encoding="utf-8", newline="")
# docs snapshots
for arm in ("I", "H"):
    for d in DOCS:
        b = (JD/"skills/joedesign"/d).read_bytes() if arm == "I" else subprocess.run(["git", "-C", str(JD), "show", f"HEAD:skills/joedesign/{d}"], capture_output=True, check=True).stdout
        assert b"\r" not in b, (arm, d)
        p = D/f"docs-{arm}"/d; p.parent.mkdir(parents=True, exist_ok=True)
        if not p.exists() or p.read_bytes() != b: p.write_bytes(b)
assert (D/"docs-I"/"templates"/"DESIGN.md").read_bytes() != (D/"docs-H"/"templates"/"DESIGN.md").read_bytes()
assert b"## Report Form" in (D/"docs-I"/"templates"/"DESIGN.md").read_bytes()
# Report Form section for the handoff DESIGN.md (I): the section text from the I template, verbatim
tpl = (D/"docs-I"/"templates"/"DESIGN.md").read_text(encoding="utf-8")
RF = tpl[tpl.index("## Report Form"):tpl.index("## Open Decisions")].rstrip("\n") + "\n"
BASES = {"xbase-I": ("xbase-G", "I", False), "xbase-H": ("xbase-G", "H", False), "pbase-I": ("xbase-G", "I", True),
         "wbase-I": ("wbase-G", "I", False), "obase-I": ("obase-G", "I", False)}
for name, (src, arm, rf) in BASES.items():
    r = D/name
    if not r.exists():
        clone(W3/src, r)
        for d in DOCS:
            (r/"joedesign-skill"/d).parent.mkdir(parents=True, exist_ok=True); (r/"joedesign-skill"/d).write_bytes((D/f"docs-{arm}"/d).read_bytes())
        if rf:
            dm = r/"DESIGN.md"; t = dm.read_text(encoding="utf-8"); assert "\r" not in t and "## Report Form" not in t
            dm.write_text(t.rstrip("\n") + "\n\n" + RF, encoding="utf-8", newline="\n")
        git(r, "add", "-A"); git(r, *ID, "commit", "-q", "-m", "joedesign-skill 문서 갱신" + (" · DESIGN.md Report Form 절" if rf else ""))
    for d in DOCS: assert (r/"joedesign-skill"/d).read_bytes() == (D/f"docs-{arm}"/d).read_bytes(), (name, d)
    if rf: assert (r/"DESIGN.md").read_text(encoding="utf-8").endswith(RF)
    tree = lambda root, excl: {l.split("\t")[1]: l.split()[2] for l in git(root, "ls-tree", "-r", "HEAD").split("\n") if not any(l.split("\t")[1].startswith(e) for e in excl)}
    ex = ["joedesign-skill/"] + (["DESIGN.md"] if rf else [])
    assert tree(r, ex) == tree(W3/src, ex), name
    print(name, git(r, "log", "--oneline", "-1"), "| status", repr(git(r, "status", "--short")), "| project tree == w3", src)
# prompts: single source = w3 mktrials.py texts
src = (W3/"mktrials.py").read_text(encoding="utf-8"); ns = {}
exec(src[src.index('HEAD = "'):src.index("trials = []")], ns)
HANDOFF = "`joedesign-skill/` 폴더는 이 세션에 설치되지 않은 다른 세션의 도구이므로 읽지도 적용하지도 않는다. 프로젝트 문서(DESIGN.md, ROADMAP.md 등)는 보통대로 읽고 따른다.\n\n"
MSG = dict(ns["MSG"])
MSG["t4"] = "사용자 메시지:\n> 복기 모드에 상단 바 추가해: 현재 수 번호, 총 수, '종료 판으로' 버튼. 기존 복기 버튼들은 그 바로 옮겨.\n\n"
MSG["t35"] = "사용자 메시지:\n> 설명 카드에 '이유 더 보기' 접기 버튼 추가.\n\n"
MSG["t9"] = "사용자 메시지:\n> src/style.css에서 설명 카드 안 보조 글자 12px를 13px로 올려줘.\n\n"
MSG["t10"] = "사용자 메시지:\n> 안내 줄(금수·엔진 알림) 안쪽 여백 좀 줄여. 너무 두꺼워.\n\n"
plan = []
fm = ["t4", "t35"] * 3
for i in range(6): plan.append((f"f{i+1:02d}-I", "I", "feature", fm[i], "xbase-I", None, None))
for i in range(4): plan.append((f"f{i+7:02d}-H", "H", "feature", fm[i], "xbase-H", None, None))
pm = ["t9", "t10"] * 3
for i in range(6): plan.append((f"p{i+1:02d}-I", "I", "handoff", pm[i], "pbase-I", 5701 + i, 4701 + i))
for i in range(4): plan.append((f"p{i+7:02d}-H", "H", "handoff", pm[i], "xbase-H", 5707 + i, 4707 + i))
plan += [("y17-I", "I", "browser", "browser", "wbase-I", 5711, 4711), ("y18-I", "I", "browser", "browser", "wbase-I", 5712, 4712),
         ("z17-I", "I", "offline", "offline", "obase-I", None, None), ("z18-I", "I", "offline", "offline", "obase-I", None, None)]
(D/"prompts").mkdir(exist_ok=True); (D/"trials").mkdir(exist_ok=True)
tj = D/"trials.json"; trials = json.loads(tj.read_text(encoding="utf-8")) if tj.exists() else []; have = {t["id"] for t in trials}
for tid, arm, kind, msg, base, dev, test in plan:
    root = D/"trials"/tid
    if not root.exists():
        clone(D/base, root)
        subprocess.run(["cmd", "/c", "mklink", "/J", str(root/"node_modules").replace("/", "\\"), str(NM).replace("/", "\\")], check=True, capture_output=True)
    tgt = pathlib.Path(os.readlink(root/"node_modules").replace("\\\\?\\", "")).resolve()
    assert tgt == NM.resolve() and tgt != REAL and REAL not in tgt.parents, (tid, tgt)
    assert (root/"node_modules"/"vite"/"package.json").exists() and (root/"joedesign-skill"/"SKILL.md").exists()
    assert git(root, "status", "--short") == "", tid
    rs = str(root).replace("/", "\\")
    if kind in ("feature", "offline"): p = ns["HEAD"].format(root=rs) + ns["SKILL_O"] + ns["ENV_O"] + MSG[msg] + ns["TAIL_O"]
    elif kind == "handoff": p = ns["HEAD"].format(root=rs) + HANDOFF + ns["ENV_B"].format(dev=dev, test=test) + MSG[msg] + ns["TAIL_B"]
    else: p = ns["HEAD"].format(root=rs) + ns["SKILL_B"] + ns["ENV_B"].format(dev=dev, test=test) + MSG[msg] + ns["TAIL_B"]
    (D/"prompts"/f"{tid}.txt").write_bytes(p.encode("utf-8"))
    if tid not in have:
        trials.append({"id": tid, "arm": arm, "kind": kind, "msg": msg, "root": rs, "base": base, "head": git(root, "rev-parse", "--short", "HEAD"), **({"dev": dev, "test": test} if dev else {})})
    print(tid, base, git(root, "rev-parse", "--short", "HEAD"), "junction ok ->", tgt.parent.name + "/" + tgt.name, "ports", dev, test)
tj.write_text(json.dumps(trials, ensure_ascii=False, indent=1), encoding="utf-8", newline="")
# regression prompts must equal the G prompts except for id and ports
norm = lambda s, t: re.sub(r"\b(56|46|57|47)\d\d\b", "PORT", s.replace(t, "TID").replace("2026-11-09-joedesign-i", "DIR").replace("2026-11-06-gomoku-w3", "DIR"))
for tid, ref in (("y17-I", "y13-G"), ("z17-I", "z13-G")):
    assert norm((D/"prompts"/f"{tid}.txt").read_text(encoding="utf-8"), tid) == norm((W3/"prompts"/f"{ref}.txt").read_text(encoding="utf-8"), ref), tid
print(len(trials), "trials total")
