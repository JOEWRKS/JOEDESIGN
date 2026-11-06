# run.sh <trial> <port> : freeze the trial's final tree, serve it, measure with both instruments, stop the server. Output: live/<trial>.txt
V=/d/JOEWRKS/.claude-worktrees/_data/2026-11-06-gomoku-w3
T=$1; P=$2; OUT=$V/live/$T.txt
{ echo "== $T freeze"; bash $V/live/freeze.sh $T; echo; } > $OUT 2>&1
( cd $V/live/$T-dist && python -m http.server $P --bind 127.0.0.1 > /dev/null 2>&1 & )
sleep 2
{ echo "== truth (visible gap incl. hard shadow; expected 16, or 12 when w<=700 or h<=700)"; GOMOKU_DEV_PORT=$P node $V/nm/truth.mjs --sizes 1440x900,1366x768,390x844 2>&1 | grep -v "^$" ; echo "== m.js"; node $V/nm/measure.mjs $P 2>&1; } >> $OUT
powershell -NoProfile -Command "Get-NetTCPConnection -LocalPort $P -State Listen -ErrorAction SilentlyContinue | ForEach-Object { Stop-Process -Id \$_.OwningProcess -Force }"
echo "$T done: $(grep -c ' X$' $OUT) S1 mismatches / $(grep -c ' = ' $OUT) S1 pairs"
