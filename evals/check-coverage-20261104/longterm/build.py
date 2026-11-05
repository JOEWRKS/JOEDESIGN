# Long-term A/B (2026-11-04): two --shared clones of the tables-A/B bases (A = JOEDESIGN 1.0.0 docs, B = patched docs),
# sparse checkout, node_modules junction. Capture scripts' hard-coded dev port 5199 replaced by
# `${process.env.GOMOKU_DEV_PORT ?? 5199}` in both arms (7 files, 7 lines each) so A/B can run in parallel.
# Arm A ports: dev 5199→5499 (5199 was taken by another project after turn 1), test 4473. Arm B: 5399 / 4373.
# Turn loop: send backlog[n] to the arm's agent (handoff turns to a separate no-skill agent in the same folder),
# save the hand-back as turns/<arm>/tNN-report.md, run snapshot.py <arm> NN, every 5 turns freeze `vite build`
# into live/<arm>-tNN-dist and measure it in the harness owner's browser (live/<arm>-tNN.md).
import json, pathlib, subprocess, itertools
L = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-04-joedesign-longterm")
P = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-04-joedesign-tables-ab")
SRC = pathlib.Path("D:/JOEWRKS/.claude-worktrees/AI-Gomoku"); BRANCH = "claude/ai-coach"
SPARSE = ["/*", "!/work/design/shots/", "!/work/design/logo-candidates/", "!/work/evidence/"]
def git(cwd, *a): return subprocess.run(["git", "-C", str(cwd), *a], check=True, capture_output=True).stdout
for arm in "AB":
    dst = L / f"L-{arm}"
    if dst.exists(): continue
    subprocess.run(["git", "clone", "-q", "--shared", "--no-checkout", str(P / f"base-{arm}"), str(dst)], check=True)
    git(dst, "remote", "remove", "origin"); git(dst, "sparse-checkout", "set", "--no-cone", *SPARSE)
    git(dst, "checkout", "-q", "-B", BRANCH, BRANCH)
    subprocess.run(["cmd", "/c", "mklink", "/J", str(dst / "node_modules"), str(SRC / "node_modules")], check=True, capture_output=True)
    for f in (dst / "work/design").glob("*.mjs"):
        s = f.read_text(encoding="utf-8")
        if "localhost:5199" in s:
            f.write_text(s.replace("'http://localhost:5199", "`http://localhost:${process.env.GOMOKU_DEV_PORT ?? 5199}").replace("/'", "/`"), encoding="utf-8")
    git(dst, "add", "-A", "work/design"); git(dst, "commit", "-q", "-m", "캡처 스크립트 dev 포트를 GOMOKU_DEV_PORT 환경변수로(롱텀 테스트 하네스, 양쪽 동일)")
