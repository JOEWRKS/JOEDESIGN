# liveG.sh <turn> <port> : freeze L-G's current tree as a production build in live/G-tNN-dist and serve it on <port> (background). Stop with: taskkill via the pid file.
N=$(printf "%02d" $1); P=$2; L=/d/JOEWRKS/.claude-worktrees/_data/2026-11-04-joedesign-longterm
cd $L/L-G && npx vite build --outDir $L/live/G-t$N-dist --emptyOutDir > $L/live/G-t$N-build.log 2>&1 || { echo build failed; tail -5 $L/live/G-t$N-build.log; exit 1; }
git -C $L/L-G status --short > $L/live/G-t$N-status-after-build.txt
for q in $(netstat -ano | grep ":$P .*LISTENING" | awk '{print $NF}' | sort -u); do taskkill //PID $q //F >/dev/null 2>&1; done
( cd $L/live/G-t$N-dist && python -m http.server $P --bind 127.0.0.1 > $L/live/G-t$N-preview.log 2>&1 & )
sleep 1; netstat -ano | grep ":$P .*LISTENING" | awk '{print $NF}' | sort -u > $L/live/G-t$N.pid
sleep 1; echo "serving live/G-t$N-dist on http://127.0.0.1:$P (pid $(cat $L/live/G-t$N.pid))"
