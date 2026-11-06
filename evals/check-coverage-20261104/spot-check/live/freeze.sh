# freeze.sh <trial> : frozen build of the trial's final working tree into live/<trial>-dist (reads the trial, writes only under live/)
V=/d/JOEWRKS/.claude-worktrees/_data/2026-11-06-gomoku-w3
cd $V/trials/$1 && npx --no-install vite build --outDir "$V/live/$1-dist" --emptyOutDir 2>&1 | tail -1 && git status --short | tr '
' ';'
