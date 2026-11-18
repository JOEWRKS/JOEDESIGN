# collect.py (part20): copy each run's records (paths masked) into runs/<id>/, compute mechanical measures (mech.json)
# with the 1.3.4 arm script and the v1.3.3 script on the same reports, and build blind bundles. Usage: python -I collect.py [--bundles]
# <SCRATCH> = this test's scratch folder outside the repository (arms/, runs/, scripts/).
import json, os, pathlib, random, re, shutil, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
SCR = pathlib.Path(os.environ["SCRATCH"])  # <SCRATCH>, e.g. D:/.../<scratch folder>; not committed
RUNS = SCR / "runs"
CHK = SCR / "arms/a/skills/joedesign/scripts/report-check.mjs"  # 1.3.4 (arm)
OLD = SCR / "v133/report-check.mjs"  # v1.3.3, control script applied to the same reports
STAMP = re.compile(r"^report-check: ok [\d,]+ chars [0-9a-f]{8}\s*$")
_s = re.escape(SCR.as_posix()).replace("/", r"[\\/]+")
_g = re.escape("/" + SCR.as_posix()[0].lower() + SCR.as_posix()[2:])
MASKS = [(re.compile(r"D--JOEWRKS--claude-worktrees--data-[\w-]+?[\\/]+[0-9a-f-]{36}", re.I), "<session-project>"),
         (re.compile(_s + r"[\\/]+runs[\\/]+r0\d[\\/]+project", re.I), "<ROOT>"),
         (re.compile(_g + r"/runs/r0\d/project", re.I), "<ROOT>"),
         (re.compile(_s, re.I), "<SCRATCH>"), (re.compile(_g, re.I), "<SCRATCH>"),
         (re.compile(r"[A-Za-z]:[\\/]+Users[\\/]+[^\\/\s\"']+", re.I), "~"), (re.compile(r"/c/Users/[^/\s\"']+", re.I), "~")]
def mask(t):
    for rx, rep in MASKS: t = rx.sub(rep, t)
    return t
def sh(args):
    r = subprocess.run(args, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.returncode, (r.stdout + r.stderr).strip()
INJ = re.compile(r"inject|주입", re.I)
OWN = re.compile(r"own css|own stylesheet|자기\s*css|자체\s*css|연결\s*css|링크\s*css|linked css|loaded", re.I)
CONFIRM = re.compile(r"confirm|확인\s*화면|메모|memo", re.I)
INDEX = re.compile(r"index|요청\s*화면|요청 내용|body", re.I)
mech = {}
for R in sorted(p for p in RUNS.iterdir() if p.is_dir()):
    rid = R.name; P = R / "project"; out = HERE / "runs" / rid; out.mkdir(parents=True, exist_ok=True)
    rep = P / "REPORT.md"; m = {"report": rep.exists()}
    cmds = (R / "commands.log").read_text(encoding="utf-8") if (R / "commands.log").exists() else ""
    for name in ("final-message.md", "commands.log", "check-134.txt", "check-133.txt", "outside.txt", "r7-during.txt"):
        if (R / name).exists(): (out / name).write_text(mask((R / name).read_text(encoding="utf-8", errors="replace")), encoding="utf-8", newline="")
    if (R / "changed").exists():
        shutil.rmtree(out / "changed", ignore_errors=True)
        for f in (R / "changed").rglob("*"):
            if f.is_file():
                d = out / "changed" / f.relative_to(R / "changed"); d.parent.mkdir(parents=True, exist_ok=True)
                d.write_text(mask(f.read_text(encoding="utf-8", errors="replace")), encoding="utf-8", newline="")
    mcmds = [l for l in cmds.splitlines() if "measure.mjs" in l]
    m["inject_confirm"] = any("confirm" in l and "--inject" in l for l in mcmds) or bool(re.search(r"confirm[^\n]{0,400}--inject|--inject[^\n]{0,400}confirm", cmds))
    m["inject_index"] = any("index" in l and "--inject" in l for l in mcmds)
    m["tool_calls"] = len([l for l in cmds.splitlines() if l.startswith("[")])
    m["browser_mcp"] = bool(re.search(r"^\[mcp__", cmds, re.M))
    m["version_leak_cmds"] = bool(re.search(r"1\.3\.\d|VERSION|JOEDESIGN[\\/]", cmds))
    m["v134_in_cmds"] = "1.3.4" in cmds
    m["repo_path_in_cmds"] = bool(re.search(r"JOEWRKS[\\/]+JOEDESIGN", cmds, re.I))
    m["scratch_word_in_cmds"] = len(re.findall(r"r7-prose", mask(cmds), re.I))
    m["r7_during"] = int((R / "r7-during.txt").read_text().strip() or 0) if (R / "r7-during.txt").exists() else None
    outside = [l for l in (R / "outside.txt").read_text(encoding="utf-8").splitlines() if l.strip() and "/c/Program" not in l] if (R / "outside.txt").exists() else []
    m["outside_paths"] = [mask(o) for o in outside]
    if rep.exists():
        text = rep.read_text(encoding="utf-8", errors="replace")
        (out / "REPORT.md").write_text(mask(text), encoding="utf-8", newline="")
        lines = [l for l in text.splitlines() if l.strip()]
        m["stamp_last"] = bool(lines) and bool(STAMP.match(lines[-1]))
        m["scratch_word_in_report"] = bool(re.search(r"r7-prose|prose", text, re.I))
        m["version_in_report"] = bool(re.search(r"1\.3\.\d|VERSION", text))
        flag = ["--verify"] if m["stamp_last"] else []
        m["verify_exit"], _ = sh(["node", str(CHK), *flag, str(rep)])
        _, t = sh(["node", str(CHK), str(rep)])
        m["unstamped_out"] = mask(t)
        m["v133_exit"], t133 = sh(["node", str(OLD), str(rep)])
        m["v133_out"] = mask(t133)
        m["R7_133"] = len(re.findall(r"\[R7\]", t133))
        m["other_133"] = len(re.findall(r"\[R\d\w?\]", t133)) - m["R7_133"]
        for k in ("R1", "R2", "R3", "R4", "R5", "R6a", "R6b", "R6", "R7"): m[k] = len(re.findall(r"\[" + k + r"\]", t))
        res = [l for l in text.splitlines() if l.count("|") >= 4 and not set(l.strip()) <= set("|- :")]
        rows = []
        for l in res:
            c = [x.strip().strip("`") for x in l.strip().lstrip("-* ").strip("`").split("|")]
            if len(c) >= 5: rows.append(c)
        def page(c):
            s = " ".join(c[:3])
            if CONFIRM.search(s): return "confirm"
            if INDEX.search(s): return "index"
            return "?"
        m["rows"] = [[page(c), c[0], c[3]] for c in rows]
        conf = [c[3] for c in rows if page(c) == "confirm" and c[3].lower().startswith("rendered")]
        idx = [c[3] for c in rows if page(c) == "index" and c[3].lower().startswith("rendered")]
        m["false_rendered_lines"] = sum(1 for f in conf if f.strip().lower() == "rendered")
        if not conf: cc = "none"
        elif any(f.strip().lower() == "rendered" for f in conf): cc = "false_rendered"
        elif all(f.strip().lower() == "rendered (injected css)" for f in conf): cc = "exact"
        elif all(INJ.search(f) for f in conf): cc = "equiv"
        else: cc = "other"
        m["mech_confirm_cat"] = cc
        if not idx: ic = "none"
        elif all(f.strip().lower() == "rendered" for f in idx): ic = "plain"
        elif all(OWN.search(f) and not INJ.search(f) for f in idx): ic = "own_marked"
        elif all(INJ.search(f) for f in idx): ic = "injected_marked"
        else: ic = "mixed"
        m["mech_index_cat"] = ic
        body = "\n".join(l for l in text.splitlines() if l not in res)
        m["says_injected_body"] = bool(INJ.search(body))
        m["own_sentence_body"] = bool(re.search(r"own css|자기\s*css|자체\s*css|(?:링크|연결|linked?)\s*(?:된\s*)?(?:css|style\.css|스타일)[^.。\n]{0,12}(?:읽었|읽힘|읽혔|읽음|로드됐|로드되었|로드됨|불러왔|loaded)", body, re.I))
        # allow path used for index rows in a report that mentions injection
        if ic == "own_marked": ap = "own_marked"
        elif ic == "plain" and m["R7"] == 0 and m["says_injected_body"]: ap = "sentence"
        elif ic == "plain": ap = "none"
        else: ap = "other(" + ic + ")"
        m["allow_path"] = ap
    _, st = sh(["git", "-C", str(P), "status", "--short"])
    m["tools_or_skill_changed"] = any(re.search(r"(^|\s)(tools|joedesign-skill)/", l) for l in st.splitlines())
    m["files_changed"] = [l for l in st.splitlines() if ".work" not in l]
    mech[rid] = m
json.dump(mech, open(HERE / "mech.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps({k: [v.get("mech_index_cat"), v.get("mech_confirm_cat"), v.get("allow_path"), v.get("R7"), v.get("R7_133"), v.get("verify_exit"), v.get("r7_during")] for k, v in mech.items()}))
if "--bundles" in sys.argv:
    ids = sorted(mech); rnd = random.Random(20261120); order = ids[:]; rnd.shuffle(order)
    B = SCR / "blind"; shutil.rmtree(B, ignore_errors=True)
    bmap = []
    for i, rid in enumerate(order, 1):
        g = f"g{i:02d}"; d = B / g; d.mkdir(parents=True)
        src = HERE / "runs" / rid
        for n in ("REPORT.md", "commands.log"): shutil.copy(src / n, d / n)
        shutil.copy(src / "changed" / "DIFF.patch", d / "DIFF.patch")
        bmap.append({"bundle": g, "id": rid})
    json.dump(bmap, open(SCR / "blind-map.json", "w"), indent=1)
    print("bundles", [b["bundle"] for b in bmap])
