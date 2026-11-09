너는 블라인드 채점기다. 폴더 `D:\JOEWRKS\.claude-worktrees\_data\2026-11-04-joedesign-longterm\blind\` 아래 패킷 8개를 채점한다: {CODES}. 각 패킷 폴더에는 `TURN.md`(사용자 메시지, 이 턴에 바뀐 파일 목록), `REPORT.md`(에이전트 보고), `DESIGN.md`(턴 뒤 DESIGN.md 전문), `DESIGN-prev.md`(턴 전 DESIGN.md)가 있다. 이 파일들만 읽는다. 다른 폴더는 읽지 않는다. 패킷은 여러 턴짜리 세션의 한 턴씩이며, 어느 조건·어느 세션인지 추측하지 말고 내용만으로 채점한다.

채점 기준은 `D:\JOEWRKS\.claude-worktrees\_data\2026-11-04-joedesign-longterm\rubric.md`를 먼저 읽고 그대로 따른다(h1~h8, 각 1/0, 해당 없음은 1에 note "N/A").

각 패킷 폴더에 `grade.json`을 UTF-8로 저장한다. 형식:
{"scores": {"h1": 0|1, "h2": 0|1, "h3": 0|1, "h4": 0|1, "h5": 0|1, "h6": 0|1, "h7": 0|1, "h8": 0|1}, "note": "근거 2~4문장(어느 절·문장에서 봤는지, N/A 표시)", "summary": "이 턴이 한 일 한 문장"}

저장이 거부되면 답에 JSON을 그대로 싣는다. 마지막 답은 패킷별 한 줄 `코드: h1=1 h2=0 ...` 8줄과 저장 여부 한 줄로 끝난다.
