# post.sh <rid> <arm a|b> <transcript>: record one finished run next to its project
set -u
rid=$1; arm=$2; tr=$3
SRC=/d/JOEWRKS/.claude-worktrees/_data/2026-11-17-joedesign-inject-behavior
R=/d/JOEWRKS/.claude-worktrees/_data/2026-11-17-reqform/runs/$rid
P=$R/project
python -I $SRC/extract.py "$tr" "D:/JOEWRKS/.claude-worktrees/_data/2026-11-17-reqform/runs/$rid/project" $R
git -C $P add -A -N
git -C $P diff -- . ':(exclude)joedesign-skill' ':(exclude).work' > $R/changed.patch
mkdir -p $R/changed
git -C $P status --short > $R/changed/status.txt
for f in $(git -C $P diff --name-only -- . ':(exclude)joedesign-skill' ':(exclude).work'); do mkdir -p $R/changed/$(dirname $f); cp $P/$f $R/changed/$f; done
cp $R/changed.patch $R/changed/DIFF.patch
ls $P/.work > $R/changed/work-files.txt 2>/dev/null || echo "(no .work)" > $R/changed/work-files.txt
OWN=$SRC/arms/$arm/skills/joedesign/scripts/report-check.mjs
NEW=$SRC/arms/b/skills/joedesign/scripts/report-check.mjs
{ echo "# own arm --verify"; node $OWN --verify $P/REPORT.md; echo "exit=$?"; } > $R/check-own.txt 2>&1
{ echo "# 1.3.2 --verify"; node $NEW --verify $P/REPORT.md; echo "exit=$?"; echo "# 1.3.2 unstamped check"; node $NEW $P/REPORT.md; echo "exit=$?"; } > $R/check-132.txt 2>&1
tail -1 $R/check-own.txt; grep -c "\[R7\]" $R/check-132.txt
