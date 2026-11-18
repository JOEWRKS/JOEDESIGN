# post.sh <rid> <transcript>: record one finished run next to its project
set -u
rid=$1; tr=$2
W=/d/JOEWRKS/.claude-worktrees/_data/2026-11-18-joedesign-mixed-css-behavior
R=$W/runs/$rid; P=$R/project
python -I $W/scripts/extract.py "$tr" "$(cygpath -m $P)" $R
git -C $P add -A -N
git -C $P diff -- . ':(exclude)joedesign-skill' ':(exclude).work' > $R/changed.patch
mkdir -p $R/changed
git -C $P status --short > $R/changed/status.txt
for f in $(git -C $P diff --name-only -- . ':(exclude)joedesign-skill' ':(exclude).work'); do mkdir -p $R/changed/$(dirname $f); cp $P/$f $R/changed/$f; done
cp $R/changed.patch $R/changed/DIFF.patch
git -C $P reset -q
ls $P/.work > $R/changed/work-files.txt 2>/dev/null || echo "(no .work)" > $R/changed/work-files.txt
CHK=$W/arms/a/skills/joedesign/scripts/report-check.mjs
[ -f $P/REPORT.md ] && cp $P/REPORT.md $R/REPORT.md
{ echo "# 1.3.3 --verify"; node $CHK --verify $P/REPORT.md; echo "exit=$?"; echo "# 1.3.3 unstamped check"; node $CHK $P/REPORT.md; echo "exit=$?"; } > $R/check-133.txt 2>&1
grep "exit=" $R/check-133.txt; grep -c "\[R7\]" $R/check-133.txt
