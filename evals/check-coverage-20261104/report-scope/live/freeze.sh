# freeze.sh <trial> : build a frozen copy of the trial's app into live/<trial>-dist and add the measurement script
V=/d/JOEWRKS/.claude-worktrees/_data/2026-11-05-joedesign-report-scope-ab
cd $V/trials/$1 && npx vite build --outDir "$V/live/$1-dist" --emptyOutDir 2>&1 | tail -1 && cp $V/live/m.js $V/live/$1-dist/m.js && git status --short | tr '\n' ';'
