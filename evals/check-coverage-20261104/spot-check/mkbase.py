# mkbase.py : build the base repos for this run (junction-safe; node_modules points at the private copy, never at the real project)
#   xbase-B : 43344f3 + "spacing v1" state taken from the 2026-11-05 trial w03-B, with the seeded defect (see seed())
#   xbase-C / xbase-D : xbase-B + skill docs C (= shipped 87e69b3) / D (docs-D)
#   wbase-D : browser S3 base (old wbase-C) + docs D      obase-D : offline S3 base (old base-C) + docs D
import os, pathlib, shutil, subprocess, sys
V = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-06-gomoku-w3")
OLD = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-05-joedesign-report-scope-ab")
NM = V/"nm"/"node_modules"
REAL = pathlib.Path("D:/JOEWRKS/.claude-worktrees/AI-Gomoku")
DOCS = ["SKILL.md", "references/conformance.md", "references/operation.md", "references/visual-translation.md", "templates/DESIGN.md"]
SHIPPED = pathlib.Path("D:/JOEWRKS/JOEDESIGN/skills/joedesign")
ID = ["-c", "user.name=JOEWRKS", "-c", "user.email=joewrks@example.invalid"]
SPARSE = "/*\n!/work/design/shots/\n!/work/design/logo-candidates/\n!/work/evidence/\n"

def git(root, *a, check=True):
    r = subprocess.run(["git", "-C", str(root), *a], capture_output=True, text=True, encoding="utf-8", errors="replace")
    if check and r.returncode: raise SystemExit(f"git {a} in {root}: {r.stderr}")
    return r.stdout.strip()

def clone(src, dst, rev=None):
    assert not dst.exists(), dst
    subprocess.run(["git", "clone", "-q", "--shared", "--no-checkout", str(src), str(dst)], check=True)
    git(dst, "config", "core.sparseCheckout", "true"); git(dst, "config", "core.autocrlf", "false")
    (dst/".git"/"info"/"sparse-checkout").write_bytes(SPARSE.encode())
    git(dst, "checkout", "-q", "-B", "claude/ai-coach", rev or "HEAD")
    git(dst, "remote", "remove", "origin")

def link(root):
    """node_modules junction -> private copy; verified before anything runs."""
    assert (NM/"vite"/"package.json").exists()
    l = root/"node_modules"; assert not os.path.lexists(l), l
    subprocess.run(["cmd", "/c", "mklink", "/J", str(l).replace("/", "\\"), str(NM).replace("/", "\\")], check=True, capture_output=True)
    tgt = pathlib.Path(os.readlink(l).replace("\\\\?\\", ""))
    assert tgt.resolve() == NM.resolve(), (l, tgt)
    assert REAL.resolve() not in tgt.resolve().parents and tgt.resolve() != REAL.resolve(), tgt
    assert (l/"vite"/"package.json").exists()
    return tgt

def put_docs(root, src):
    for d in DOCS:
        b = (src/d).read_bytes(); assert b"\r" not in b
        (root/"joedesign-skill"/d).write_bytes(b)

def seed(root):
    """Seeded defect: the rule says gaps are measured between visible boxes (border box + hard drop shadow),
    the check measures border boxes only, and the CSS no longer returns the shadow depth as bottom margin.
    Result: check passes while the visible gap under every shadowed block is short by the shadow depth."""
    def sub(rel, old, new, count=1):
        p = root/rel; t = p.read_bytes().decode("utf-8"); assert t.count(old) == count, (rel, old[:50], t.count(old))
        p.write_bytes(t.replace(old, new).encode("utf-8"))
    css = "src/style.css"
    sub(css, "\n     그림자 깊이(--lift-*)는 그 요소의 아래 여백으로 되돌려, 그림자가 간격을 먹지 않게 한다. 검사: work/design/spacing-check.mjs */", " 검사: work/design/spacing-check.mjs */")
    for old in [" padding-bottom: var(--lift-board);", " margin-bottom: var(--lift-card);", " margin-bottom: var(--lift-xs);", " margin-bottom: var(--lift-chip);",
                " margin-bottom: var(--lift-btn);", " margin-bottom: var(--lift-tutorial);"]:
        sub(css, old, "")
    sub(css, " margin-bottom: var(--lift-small);", "", count=2)
    sub(css, " padding-bottom: var(--lift-chip);", "", count=2)
    sub(css, ".hud > .limited { margin: 0 0 var(--lift-xs);", ".hud > .limited { margin: 0;")
    chk = "work/design/spacing-check.mjs"
    t = (root/chk).read_bytes().decode("utf-8")
    a = t.index("  // 입체 그림자:"); b = t.index("  const check = (rule")
    t = t[:a] + "  const vBottom = el => Math.max(el.getBoundingClientRect().bottom, ...kids(el).filter(k => !k.closest('#board')).map(vBottom));\n" + t[b:]
    (root/chk).write_bytes(t.encode("utf-8"))
    d = (root/"DESIGN.md").read_bytes().decode("utf-8")
    a = d.index("**고치기 전 측정("); b = d.index("**기준:**")
    d = d[:a] + d[b:]
    old = " 그림자 깊이(`--lift-*`)는 그 요소의 아래 여백으로 되돌려 다음 요소와의 간격에 끼어들지 않게 한다."
    assert d.count(old) == 1; d = d.replace(old, "")
    (root/"DESIGN.md").write_bytes(d.encode("utf-8"))
    k = (root/"TASK.md").read_bytes().decode("utf-8")
    old = " 입체 그림자 깊이만큼 아래 여백,"; assert k.count(old) == 1; k = k.replace(old, "")
    a = k.index("- 고치기 전 빌드:"); b = k.index("- 고친 뒤(2026-11-05)")
    k = k[:a] + k[b:]
    (root/"TASK.md").write_bytes(k.encode("utf-8"))

step = sys.argv[1]
if step == "xbase-files":
    x = V/"xbase-B"; clone(OLD/"wbase-B", x)
    assert git(x, "rev-parse", "--short", "HEAD") == "43344f3"
    src = OLD/"trials"/"w03-B"
    for rel in ["DESIGN.md", "ROADMAP.md", "TASK.md", "src/style.css", "work/design/spacing-check.mjs", "work/design/fake-engine-worker.js"]:
        shutil.copyfile(src/rel, x/rel)
    seed(x); print("junction ->", link(x)); print(git(x, "status", "--short"))
elif step == "xbase-commit":
    x = V/"xbase-B"
    git(x, "add", "DESIGN.md", "ROADMAP.md", "TASK.md", "src/style.css", "work/design/spacing-check.mjs", "work/design/fake-engine-worker.js", "work/design/spacing-v1.log")
    git(x, *ID, "commit", "-q", "-m", "메인 화면 간격 규칙 v1과 간격 검사 스크립트")
    print(git(x, "log", "--oneline", "-3")); print("status:", repr(git(x, "status", "--short")))
elif step == "arms":
    for name, src, docs, msg in [("xbase-C", V/"xbase-B", SHIPPED, "joedesign-skill 문서 갱신"), ("xbase-D", V/"xbase-B", V/"docs-D", "joedesign-skill 문서 갱신"),
                                 ("wbase-D", OLD/"wbase-C", V/"docs-D", "joedesign-skill 문서 갱신"), ("obase-D", OLD/"base-C", V/"docs-D", "joedesign-skill 문서 갱신")]:
        r = V/name; clone(src, r); put_docs(r, docs)
        git(r, "add", "joedesign-skill"); git(r, *ID, "commit", "-q", "-m", msg)
        print(name, git(r, "log", "--oneline", "-2").replace("\n", " | "), "status:", repr(git(r, "status", "--short")))
