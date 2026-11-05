# next.py <arm> <turn>: prints the user message to send for that turn (handoff turns get the handoff preamble).
import sys, json, pathlib
L = pathlib.Path("D:/JOEWRKS/.claude-worktrees/_data/2026-11-04-joedesign-longterm")
arm, n = sys.argv[1], int(sys.argv[2]); b = {t["n"]: t for t in json.loads((L/"backlog.json").read_text(encoding="utf-8"))}
ports = json.loads((L/"ports.json").read_text(encoding="utf-8"))[arm]; t = b[n]
root = f"D:\JOEWRKS\.claude-worktrees\_data\2026-11-04-joedesign-longterm\L-{arm}"
if t["kind"] == "handoff":
    pre = (L/"preamble-handoff.md").read_text(encoding="utf-8")
    msg = pre.replace("{ROOT}", root).replace("{PORT}", str(ports["dev"])).replace("{TPORT}", str(ports["test"])).replace("{MSG}", t["msg"])
else:
    msg = f"사용자 메시지(턴 {n}):\n> {t['msg']}\n\n작업이 끝나면 최종 보고를 답으로 출력한다."
sys.stdout.buffer.write(msg.encode("utf-8"))
