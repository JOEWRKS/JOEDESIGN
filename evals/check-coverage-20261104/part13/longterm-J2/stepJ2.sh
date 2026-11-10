# stepJ2.sh <agent-id> <done-turn> : harvest that turn (arm J2) + snapshot L-J2, then write the next turn's message
# from the backlog (next.py) to turns/J2/tNN-msg.txt and print it. Only that file's text is sent; no hand-written messages.
L=/d/JOEWRKS/.claude-worktrees/_data/2026-11-04-joedesign-longterm; cd $L
python -X utf8 harvestG.py $1 $2 J2 | tr -d '\r' | cut -c1-160
python -X utf8 snapshot.py J2 $2 | tr -d '\r' | cut -c1-200
N=$(( $2 + 1 ))
if [ $N -le 40 ]; then
  F=turns/J2/t$(printf %02d $N)-msg.txt
  python -X utf8 next.py J2 $N > $F
  echo "----- next t$N kind: $(python -X utf8 -c "import json;print({t['n']:t for t in json.load(open('backlog.json',encoding='utf-8'))}[$N]['kind'])") file: $F"
  cat $F; echo
fi
