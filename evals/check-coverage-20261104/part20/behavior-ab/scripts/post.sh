# post.sh <rid> <transcript>: record one finished run next to its project
set -u
rid=$1; tr=$2
W=${SCRATCH_SH:?set SCRATCH_SH to <SCRATCH> in git-bash form}
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
OLD=$W/v133/report-check.mjs
[ -f $P/REPORT.md ] && cp $P/REPORT.md $R/REPORT.md
if tail -n 1 $P/REPORT.md | grep -qE '^report-check: ok [0-9,]+ chars [0-9a-f]{8}'; then
  { echo "# 1.3.4 --verify (stamped)"; node $CHK --verify $P/REPORT.md; echo "exit=$?"; } > $R/check-134.txt 2>&1
else
  { echo "# 1.3.4 plain check (no stamp)"; node $CHK $P/REPORT.md; echo "exit=$?"; } > $R/check-134.txt 2>&1
fi
{ echo "# 1.3.4 unstamped check"; node $CHK $P/REPORT.md; echo "exit=$?"; } >> $R/check-134.txt 2>&1
{ echo "# v1.3.3 plain check"; node $OLD $P/REPORT.md; echo "exit=$?"; } > $R/check-133.txt 2>&1
grep "exit=" $R/check-134.txt $R/check-133.txt; grep -c "\[R7\]" $R/check-134.txt $R/check-133.txt
