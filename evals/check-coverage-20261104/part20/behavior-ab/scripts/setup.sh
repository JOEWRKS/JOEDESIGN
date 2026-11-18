# setup.sh <rid>: make runs/<rid>/project from the scene M-L fixture and the 1.3.4 skill copy
set -eu
W=${SCRATCH_SH:?set SCRATCH_SH to <SCRATCH> in git-bash form}
P=$W/runs/$1/project
mkdir -p $P/joedesign-skill
cp -r $W/base/m/. $P/
for d in SKILL.md references scripts templates; do cp -r $W/arms/a/skills/joedesign/$d $P/joedesign-skill/; done
cd $P && git init -q && git add -A && git -c user.name=run -c user.email=run@local commit -q -m base && git log --oneline | head -1
