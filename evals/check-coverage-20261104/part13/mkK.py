# mkK.py : 13부 (1.3.0 후보 = K vs 1.2.1 게시본 = L) trial clones. Skill docs: K = JOEDESIGN working tree, L = git HEAD (1.2.1).
# Bases: part-11 xbase-I/wbase-I/obase-I (w3 project trees) and part-12 pbase-J (handoff DESIGN.md = 1.2.1 top line + Report Form).
# Handoff K base = pbase-J with its Report Form section replaced by the K template's section (only that section differs).
# Every node_modules junction must point at the private w3 copy (os.readlink here; Get-Item .Target separately).
import json, os, pathlib, subprocess, re
D = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-10-joedesign-k")
P11 = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-09-joedesign-i")
P12 = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-10-joedesign-j")
W3 = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-06-gomoku-w3")
JD = pathlib.Path("D:/JOEWRKS/JOEDESIGN")
NM = W3/"nm"/"node_modules"; REAL = pathlib.Path("D:/JOEWRKS/.claude-worktrees/AI-Gomoku").resolve()
DOCS = ["SKILL.md", "references/conformance.md", "references/operation.md", "references/visual-translation.md", "templates/DESIGN.md", "scripts/report-check.mjs"]
ID = ["-c", "user.name=JOEWRKS", "-c", "user.email=joewrks@example.invalid"]
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
    (dst/".git"/"info"/"sparse-checkout").write_bytes(SPARSE.encode())
    flatten(dst)
    git(dst, "checkout", "-q", "-B", "claude/ai-coach", "HEAD"); git(dst, "remote", "remove", "origin")
D.mkdir(exist_ok=True)
for arm in ("K", "L"):
    for d in DOCS:
        b = (JD/"skills/joedesign"/d).read_bytes() if arm == "K" else subprocess.run(["git", "-C", str(JD), "show", f"HEAD:skills/joedesign/{d}"], capture_output=True, check=True).stdout
        assert b"\r" not in b, (arm, d)
        p = D/f"docs-{arm}"/d; p.parent.mkdir(parents=True, exist_ok=True); p.write_bytes(b)
assert subprocess.run(["git", "-C", str(JD), "describe", "--tags", "--exact-match", "HEAD"], capture_output=True, text=True).returncode != 0 or True
tplK = (D/"docs-K"/"templates"/"DESIGN.md").read_text(encoding="utf-8")
RFK = tplK[tplK.index("## Report Form"):tplK.index("## Open Decisions")].rstrip("\n") + "\n"
assert "Display before/after" in RFK
BASES = {"xbase-K": (P11/"xbase-I", "K", False), "xbase-L": (P11/"xbase-I", "L", False),
         "pbase-K": (P12/"pbase-J", "K", True), "pbase-L": (P12/"pbase-J", "L", False),
         "wbase-K": (P11/"wbase-I", "K", False), "wbase-L": (P11/"wbase-I", "L", False),
         "obase-K": (P11/"obase-I", "K", False), "obase-L": (P11/"obase-I", "L", False)}
for name, (src, arm, rf) in BASES.items():
    r = D/name
    if not r.exists():
        clone(src, r)
        for d in DOCS:
            (r/"joedesign-skill"/d).parent.mkdir(parents=True, exist_ok=True); (r/"joedesign-skill"/d).write_bytes((D/f"docs-{arm}"/d).read_bytes())
        if rf:
            dm = r/"DESIGN.md"; t = dm.read_text(encoding="utf-8"); i = t.index("\n## Report Form\n") + 1
            assert "\r" not in t and t.count("\n## Report Form\n") == 1 and "\n## " not in t[i:], "Report Form is the last section"
            dm.write_text(t[:i] + RFK, encoding="utf-8", newline="\n")
        git(r, "add", "-A"); git(r, *ID, "commit", "-q", "-m", f"joedesign-skill {arm} 문서" + (" · DESIGN.md Report Form 절 1.3.0" if rf else ""))
    for d in DOCS: assert (r/"joedesign-skill"/d).read_bytes() == (D/f"docs-{arm}"/d).read_bytes(), (name, d)
    tree = lambda root, excl: {l.split("\t")[1]: l.split()[2] for l in git(root, "ls-tree", "-r", "HEAD").split("\n") if not any(l.split("\t")[1].startswith(e) for e in excl)}
    ex = ["joedesign-skill/"] + (["DESIGN.md"] if rf else [])
    assert tree(r, ex) == tree(src, ex), name
    print(name, git(r, "log", "--oneline", "-1"))
src = (W3/"mktrials.py").read_text(encoding="utf-8"); ns = {}
exec(src[src.index('HEAD = "'):src.index("trials = []")], ns)
HANDOFF = "`joedesign-skill/` 폴더는 이 세션에 설치되지 않은 다른 세션의 도구이므로 읽지도 적용하지도 않는다. 프로젝트 문서(DESIGN.md, ROADMAP.md 등)는 보통대로 읽고 따른다.\n\n"
MSG = dict(ns["MSG"])
MSG.update({
 "r1": "사용자 메시지:\n> 복기 모드에 상단 바 추가해: 현재 수 번호, 총 수, '종료 판으로' 버튼. 기존 복기 버튼들은 그 바로 옮겨.\n\n",
 "r2": "사용자 메시지:\n> 직전 내 수 해설 카드를 판 오른쪽 위 구석에 겹쳐서 띄워줘. 세로 자리 아끼게.\n\n",
 "r3": "사용자 메시지:\n> 복기 버튼 세 개(◀ 이전 수, 다음 수 ▶, 종료 판으로)를 복기 상태 문장 위로 올려줘. 순서와 글자는 그대로.\n\n",
 "t35": "사용자 메시지:\n> 설명 카드에 '이유 더 보기' 접기 버튼 추가.\n\n",
 "t9": "사용자 메시지:\n> src/style.css에서 설명 카드 안 보조 글자 12px를 13px로 올려줘.\n\n",
 "t10": "사용자 메시지:\n> 안내 줄(금수·엔진 알림) 안쪽 여백 좀 줄여. 너무 두꺼워.\n\n",
})
MSG["t4"] = MSG["r1"]
plan = []; port = iter(range(5731, 5800))
for arm, off in (("K", 0), ("L", 12)):
    for i, m in enumerate(["r1"] * 4 + ["r2"] * 4 + ["r3"] * 4): plan.append((f"a{off+i+1:02d}-{arm}", arm, "relocate", m, f"xbase-{arm}"))
for arm, off in (("K", 0), ("L", 6)):
    for i, m in enumerate(["t4", "t35"] * 3): plan.append((f"f{off+i+1:02d}-{arm}", arm, "feature", m, f"xbase-{arm}"))
for arm, off in (("K", 0), ("L", 6)):
    for i, m in enumerate(["t9", "t10"] * 3): plan.append((f"q{off+i+1:02d}-{arm}", arm, "handoff", m, f"pbase-{arm}"))
for arm, off in (("K", 0), ("L", 3)):
    for i in range(3): plan.append((f"y{off+i+1:02d}-{arm}", arm, "browser", "browser", f"wbase-{arm}"))
    for i in range(3): plan.append((f"z{off+i+1:02d}-{arm}", arm, "offline", "offline", f"obase-{arm}"))
(D/"prompts").mkdir(exist_ok=True); (D/"trials").mkdir(exist_ok=True)
trials = []
for tid, arm, kind, msg, base in plan:
    root = D/"trials"/tid
    if not root.exists():
        clone(D/base, root)
        subprocess.run(["cmd", "/c", "mklink", "/J", str(root/"node_modules").replace("/", "\\"), str(NM).replace("/", "\\")], check=True, capture_output=True)
    tgt = pathlib.Path(os.readlink(root/"node_modules").replace("\\\\?\\", "")).resolve()
    assert tgt == NM.resolve() and tgt != REAL and REAL not in tgt.parents, (tid, tgt)
    assert (root/"node_modules"/"vite"/"package.json").exists() and (root/"joedesign-skill"/"SKILL.md").exists()
    assert git(root, "status", "--short") == "", tid
    for d in DOCS: assert (root/"joedesign-skill"/d).read_bytes() == (D/f"docs-{arm}"/d).read_bytes(), (tid, d)
    rs = str(root).replace("/", "\\"); dev = test = None
    if kind in ("handoff", "browser"): dev = next(port); test = dev - 1000
    if kind in ("relocate", "feature", "offline"): p = ns["HEAD"].format(root=rs) + ns["SKILL_O"] + ns["ENV_O"] + MSG[msg] + ns["TAIL_O"]
    elif kind == "handoff": p = ns["HEAD"].format(root=rs) + HANDOFF + ns["ENV_B"].format(dev=dev, test=test) + MSG[msg] + ns["TAIL_B"]
    else: p = ns["HEAD"].format(root=rs) + ns["SKILL_B"] + ns["ENV_B"].format(dev=dev, test=test) + MSG[msg] + ns["TAIL_B"]
    (D/"prompts"/f"{tid}.txt").write_bytes(p.encode("utf-8"))
    trials.append({"id": tid, "arm": arm, "kind": kind, "msg": msg, "root": rs, "base": base, "head": git(root, "rev-parse", "--short", "HEAD"), **({"dev": dev, "test": test} if dev else {})})
(D/"trials.json").write_text(json.dumps(trials, ensure_ascii=False, indent=1), encoding="utf-8", newline="")
# prompts equal the earlier parts' prompts except root/ports
norm = lambda s: re.sub(r"\b(56|46|57|47)\d\d\b", "PORT", re.sub(r"trials\\[a-z]\d\d-[A-Z]", "T", re.sub(r"2026-11-\d\d-(joedesign-[a-z]|gomoku-w3)", "DIR", s)))
P = lambda d, t: norm((d/"prompts"/f"{t}.txt").read_text(encoding="utf-8"))
assert P(D, "a01-K") == P(P12, "a01-J") and P(D, "a09-K") == P(P12, "a05-J") and P(D, "a05-K") == P(P12, "a03-J")
assert P(D, "f02-K") == P(P11, "f02-I") and P(D, "f01-K") == P(P11, "f01-I")
assert P(D, "q01-K") == P(P12, "q01-J") and P(D, "q02-K") == P(P12, "q03-J")
assert P(D, "y01-K") == P(P11, "y17-I") and P(D, "z01-K") == P(P11, "z17-I")
print(len(trials), "trials; prompts match parts 11/12")
