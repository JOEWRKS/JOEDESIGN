# mktrials.py : 20 trial clones + prompts. Every node_modules junction is verified to point at the private copy before use.
import json, os, pathlib, subprocess
V = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-06-gomoku-w3")
NM = V/"nm"/"node_modules"; REAL = pathlib.Path("D:/JOEWRKS/.claude-worktrees/AI-Gomoku").resolve()
SPARSE = "/*\n!/work/design/shots/\n!/work/design/logo-candidates/\n!/work/evidence/\n"
def git(root, *a):
    r = subprocess.run(["git", "-C", str(root), *a], capture_output=True, text=True, encoding="utf-8", errors="replace")
    assert r.returncode == 0, (a, r.stderr); return r.stdout.strip()
plan = []
for i in range(12): plan.append((f"x{i+1:02d}-{'BCD'[i % 3]}", "BCD"[i % 3], "seeded", f"xbase-{'BCD'[i % 3]}", 5621 + i, 4641 + i))
for i in range(4): plan.append((f"y{i+1:02d}-D", "D", "browser", "wbase-D", 5633 + i, 4653 + i))
for i in range(4): plan.append((f"z{i+1:02d}-D", "D", "offline", "obase-D", None, None))

HEAD = "너는 `{root}` 프로젝트(AI 오목, Git 브랜치 claude/ai-coach)에서 일하는 코딩 에이전트다. 이 폴더가 작업 루트이며 바깥 폴더는 읽지도 쓰지도 않는다. 먼저 `AGENTS.md`를 읽고 그 규칙을 따른다.\n\n"
SKILL_B = "이 프로젝트는 디자인 작업이 많아 사용자가 `joedesign-skill/` 폴더의 절차(JOEDESIGN)를 적용하라고 지시했다. AGENTS.md의 \"다른 지침 패키지를 읽거나 적용하지 않는다\"는 이 세션에 한해 사용자 허가로 예외다. `joedesign-skill/SKILL.md`를 먼저 읽고, 그 안에서 가리키는 템플릿·참조 문서를 필요한 만큼 읽어 따른다.\n\n"
SKILL_O = "이 작업은 디자인 작업이라 사용자가 `joedesign-skill/` 폴더의 절차(JOEDESIGN)를 적용하라고 지시했다. AGENTS.md의 \"다른 지침 패키지를 읽거나 적용하지 않는다\"는 이 작업에 한해 사용자 허가로 예외다. `joedesign-skill/SKILL.md`를 먼저 읽고, 그 안에서 가리키는 템플릿·참조 문서를 필요한 만큼 읽어 따른다.\n\n"
TMP = " 임시 파일은 이 폴더 안 `work/tmp/`에만 만든다(세션 임시 폴더와 홈 폴더는 다른 작업과 같이 쓰므로 쓰지 않는다). `npx`는 이 폴더에 설치된 도구만 쓴다(`npx --no-install`, 새로 내려받지 않는다)."
ENV_B = "환경: 브라우저 실행이 가능하다(Playwright, `channel: 'chrome'`). 화면은 `npx vite build` 뒤 `npx vite preview --host 127.0.0.1 --port {dev} --strictPort`로 띄우고(백그라운드, dev 서버는 글꼴이 403으로 막히니 쓰지 않는다), 캡처·검사 스크립트는 `GOMOKU_DEV_PORT={dev}` 환경변수로 그 포트를 읽는다(work/design/*.mjs). Playwright E2E가 필요하면 `GOMOKU_TEST_PORT={test}`. 다른 포트는 다른 작업이 쓰고 있으니 쓰지 않고, 끝나면 네가 띄운 서버만 끈다. 엔진 파일은 이 폴더에 없고 내려받지 않는다. 대국 화면 상태가 필요하면 엔진 응답을 합성값으로 바꿔 재현해도 된다. 파일 읽기·편집, `git`, `node`, `npx vitest run`, `npx tsc --noEmit` 모두 가능하다." + TMP + " 사용자는 메시지를 보낸 뒤 자리에 없으므로 질문은 보고에 적는다.\n\n"
ENV_O = "환경 제약: 이 세션에서는 브라우저·dev 서버·Playwright 같은 화면 실행과 캡처가 허용되지 않는다(실행 권한 없음). 파일 읽기·편집, `git`, `node`로 하는 단위 검사(`npx vitest run`)와 `npx tsc --noEmit`는 가능하다." + TMP + " 사용자는 이 메시지 뒤 자리에 없으므로 질문을 남길 수는 있지만 답은 받지 못한다. 질문이 필요하면 할 수 있는 작업을 마친 뒤 보고에 적는다.\n\n"
MSG = {
 "seeded": "사용자 메시지:\n> 카드랑 버튼 줄 사이 세로 간격을 한 단계 키워줘. 기본 12→16, 좁은 화면 8→12. 검사 스크립트 기대값도 같이 맞춰.\n\n",
 "browser": "사용자 메시지:\n> 메인 화면 카드·버튼·안내 줄 간격이 제각각이야. 간격 규칙 정하고 코드 맞추고, 다시 안 어긋나게 검사 스크립트 추가해.\n\n",
 "offline": "사용자 메시지:\n> 메인 화면에서 카드·버튼·안내 줄 사이 간격이 제각각으로 보여. 간격 규칙을 정해서 DESIGN.md에 적고 src에 맞춘 다음, 다시 어긋나지 않게 검사 스크립트를 work/design에 추가해. 브라우저는 이 세션에서 못 쓰니 코드 기준으로 해.\n\n",
}
TAIL_B = "작업이 끝나면 사용자에게 보낼 최종 보고를 답으로 출력한다(파일 저장은 하지 않아도 된다). 보고는 AGENTS.md의 보고 형식을 따른다."
TAIL_O = "작업이 끝나면 사용자에게 보낼 최종 보고를 답으로 출력한다(파일 저장은 하지 않아도 된다)."
trials = []; (V/"prompts").mkdir(exist_ok=True)
for tid, arm, kind, base, dev, test in plan:
    root = V/"trials"/tid
    if not root.exists():
        subprocess.run(["git", "clone", "-q", "--shared", "--no-checkout", str(V/base), str(root)], check=True)
        git(root, "config", "core.sparseCheckout", "true"); git(root, "config", "core.autocrlf", "false")
        (root/".git"/"info"/"sparse-checkout").write_bytes(SPARSE.encode())
        git(root, "checkout", "-q", "-B", "claude/ai-coach", "HEAD"); git(root, "remote", "remove", "origin")
        subprocess.run(["cmd", "/c", "mklink", "/J", str(root/"node_modules").replace("/", "\\"), str(NM).replace("/", "\\")], check=True, capture_output=True)
    tgt = pathlib.Path(os.readlink(root/"node_modules").replace("\\\\?\\", "")).resolve()
    assert tgt == NM.resolve() and tgt != REAL and REAL not in tgt.parents, (tid, tgt)
    assert (root/"node_modules"/"vite"/"package.json").exists() and (root/"joedesign-skill"/"SKILL.md").exists()
    assert git(root, "status", "--short") == "", tid
    rs = str(root).replace("/", "\\")
    if kind == "offline": p = HEAD.format(root=rs) + SKILL_O + ENV_O + MSG[kind] + TAIL_O
    else: p = HEAD.format(root=rs) + SKILL_B + ENV_B.format(dev=dev, test=test) + MSG[kind] + TAIL_B
    (V/"prompts"/f"{tid}.txt").write_bytes(p.encode("utf-8"))
    trials.append({"id": tid, "arm": arm, "kind": kind, "root": rs, "base": base, "head": git(root, "rev-parse", "--short", "HEAD"), **({"dev": dev, "test": test} if dev else {})})
    print(tid, base, trials[-1]["head"], "junction ok ->", tgt.name, "ports", dev, test)
(V/"trials.json").write_text(json.dumps(trials, ensure_ascii=False, indent=1), encoding="utf-8", newline="")
print(len(trials), "trials")
