# mkJ.py : 12부 (1.2.1 = J vs 1.2.0 = I) trial clones from the part-11 bases. Skill docs: J = JOEDESIGN working tree, I = git HEAD (1.2.0).
# Handoff J base = pbase-I (1.2.0 Report Form at the end) + the template's new top line under the DESIGN.md title.
# Every node_modules junction must point at the private w3 copy (os.readlink here; Get-Item .Target separately).
import json, os, pathlib, subprocess, re
D = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-10-joedesign-j")
P11 = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-09-joedesign-i")
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
for arm in ("J", "I"):
    for d in DOCS:
        b = (JD/"skills/joedesign"/d).read_bytes() if arm == "J" else subprocess.run(["git", "-C", str(JD), "show", f"HEAD:skills/joedesign/{d}"], capture_output=True, check=True).stdout
        assert b"\r" not in b, (arm, d)
        p = D/f"docs-{arm}"/d; p.parent.mkdir(parents=True, exist_ok=True); p.write_bytes(b)
for d in DOCS: assert (D/"docs-I"/d).read_bytes() == (P11/"docs-I"/d).read_bytes(), d  # 1.2.0 arm == part-11 I docs
tpl = (D/"docs-J"/"templates"/"DESIGN.md").read_text(encoding="utf-8")
TOP = next(l for l in tpl.splitlines() if l.startswith("**Reporting:**")) + "\n"
BASES = {"xbase-J": (P11/"xbase-I", "J", False), "pbase-J": (P11/"pbase-I", "J", True)}
for name, (src, arm, top) in BASES.items():
    r = D/name
    if not r.exists():
        clone(src, r)
        for d in DOCS: (r/"joedesign-skill"/d).write_bytes((D/f"docs-{arm}"/d).read_bytes())
        if top:
            dm = r/"DESIGN.md"; t = dm.read_text(encoding="utf-8"); first, rest = t.split("\n", 1)
            assert first.startswith("# ") and "**Reporting:**" not in t
            dm.write_text(first + "\n\n" + TOP + rest, encoding="utf-8", newline="\n")
        git(r, "add", "-A"); git(r, *ID, "commit", "-q", "-m", "joedesign-skill 1.2.1 문서" + (" · DESIGN.md 보고 안내 줄" if top else ""))
    for d in DOCS: assert (r/"joedesign-skill"/d).read_bytes() == (D/f"docs-{arm}"/d).read_bytes(), (name, d)
    tree = lambda root, excl: {l.split("\t")[1]: l.split()[2] for l in git(root, "ls-tree", "-r", "HEAD").split("\n") if not any(l.split("\t")[1].startswith(e) for e in excl)}
    ex = ["joedesign-skill/"] + (["DESIGN.md"] if top else [])
    assert tree(r, ex) == tree(src, ex), name
    if top:
        a = (r/"DESIGN.md").read_text(encoding="utf-8"); b = (src/"DESIGN.md").read_text(encoding="utf-8")
        assert a.replace("\n" + TOP, "", 1) == b, "only the top line differs"
    print(name, git(r, "log", "--oneline", "-1"))
src = (W3/"mktrials.py").read_text(encoding="utf-8"); ns = {}
exec(src[src.index('HEAD = "'):src.index("trials = []")], ns)
HANDOFF = "`joedesign-skill/` 폴더는 이 세션에 설치되지 않은 다른 세션의 도구이므로 읽지도 적용하지도 않는다. 프로젝트 문서(DESIGN.md, ROADMAP.md 등)는 보통대로 읽고 따른다.\n\n"
MSG = {
 "r1": "사용자 메시지:\n> 복기 모드에 상단 바 추가해: 현재 수 번호, 총 수, '종료 판으로' 버튼. 기존 복기 버튼들은 그 바로 옮겨.\n\n",
 "r2": "사용자 메시지:\n> 직전 내 수 해설 카드를 판 오른쪽 위 구석에 겹쳐서 띄워줘. 세로 자리 아끼게.\n\n",
 "r3": "사용자 메시지:\n> 복기 버튼 세 개(◀ 이전 수, 다음 수 ▶, 종료 판으로)를 복기 상태 문장 위로 올려줘. 순서와 글자는 그대로.\n\n",
 "t9": "사용자 메시지:\n> src/style.css에서 설명 카드 안 보조 글자 12px를 13px로 올려줘.\n\n",
 "t10": "사용자 메시지:\n> 안내 줄(금수·엔진 알림) 안쪽 여백 좀 줄여. 너무 두꺼워.\n\n",
}
plan = []
for arm, off, base in (("J", 0, D/"xbase-J"), ("I", 6, P11/"xbase-I")):
    for i, m in enumerate(["r1", "r1", "r2", "r2", "r3", "r3"]): plan.append((f"a{off+i+1:02d}-{arm}", arm, "relocate", m, base, None, None))
for arm, off, base in (("J", 0, D/"pbase-J"), ("I", 4, P11/"pbase-I")):
    for i, m in enumerate(["t9", "t9", "t10", "t10"]): plan.append((f"q{off+i+1:02d}-{arm}", arm, "handoff", m, base, 5721 + off + i, 4721 + off + i))
(D/"prompts").mkdir(exist_ok=True); (D/"trials").mkdir(exist_ok=True)
trials = []
for tid, arm, kind, msg, base, dev, test in plan:
    root = D/"trials"/tid
    if not root.exists():
        clone(base, root)
        subprocess.run(["cmd", "/c", "mklink", "/J", str(root/"node_modules").replace("/", "\\"), str(NM).replace("/", "\\")], check=True, capture_output=True)
    tgt = pathlib.Path(os.readlink(root/"node_modules").replace("\\\\?\\", "")).resolve()
    assert tgt == NM.resolve() and tgt != REAL and REAL not in tgt.parents, (tid, tgt)
    assert (root/"node_modules"/"vite"/"package.json").exists() and (root/"joedesign-skill"/"SKILL.md").exists()
    assert git(root, "status", "--short") == "", tid
    for d in DOCS: assert (root/"joedesign-skill"/d).read_bytes() == (D/f"docs-{arm}"/d).read_bytes(), (tid, d)
    rs = str(root).replace("/", "\\")
    if kind == "relocate": p = ns["HEAD"].format(root=rs) + ns["SKILL_O"] + ns["ENV_O"] + MSG[msg] + ns["TAIL_O"]
    else: p = ns["HEAD"].format(root=rs) + HANDOFF + ns["ENV_B"].format(dev=dev, test=test) + MSG[msg] + ns["TAIL_B"]
    (D/"prompts"/f"{tid}.txt").write_bytes(p.encode("utf-8"))
    trials.append({"id": tid, "arm": arm, "kind": kind, "msg": msg, "root": rs, "base": base.name, "head": git(root, "rev-parse", "--short", "HEAD"), **({"dev": dev, "test": test} if dev else {})})
    print(tid, base.name, trials[-1]["head"], "junction ->", tgt.parent.name + "/" + tgt.name, dev or "")
(D/"trials.json").write_text(json.dumps(trials, ensure_ascii=False, indent=1), encoding="utf-8", newline="")
# prompts must equal the part-11 prompts except root/ports/message
norm = lambda s: re.sub(r"\b(57|47)\d\d\b", "PORT", re.sub(r"trials\\[a-z]\d\d-[A-Z]", "T", s.replace("2026-11-10-joedesign-j", "DIR").replace("2026-11-09-joedesign-i", "DIR")))
assert norm((D/"prompts"/"q01-J.txt").read_text(encoding="utf-8")) == norm((P11/"prompts"/"p01-I.txt").read_text(encoding="utf-8"))
assert norm((D/"prompts"/"a01-J.txt").read_text(encoding="utf-8")) == norm((P11/"prompts"/"f01-I.txt").read_text(encoding="utf-8"))
print(len(trials), "trials")
