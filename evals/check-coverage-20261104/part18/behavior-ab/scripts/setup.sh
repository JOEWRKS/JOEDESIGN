# setup.sh <rid>: make runs/<rid>/project from the scene M fixture and the 1.3.3 skill copy
set -eu
W=/d/JOEWRKS/.claude-worktrees/_data/2026-11-18-joedesign-mixed-css-behavior
P=$W/runs/$1/project
mkdir -p $P/joedesign-skill
cp -r $W/base/m/. $P/
for d in SKILL.md references scripts templates; do cp -r $W/arms/a/skills/joedesign/$d $P/joedesign-skill/; done
cd $P && git init -q && git add -A && git -c user.name=run -c user.email=run@local commit -q -m base && git log --oneline | head -1
