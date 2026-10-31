#!/usr/bin/env bash
# Count consecutive UTC days with a submission to ANY entered competition (read from Kaggle).
set -uo pipefail
slugs=$(kaggle -W competitions list --group entered -v 2>/dev/null | tail -n +2 | cut -d, -f1 | sed 's#.*/##')
days=$(for s in $slugs; do
  kaggle -W competitions submissions "$s" -v 2>/dev/null | grep -oE '[0-9]{4}-[0-9]{2}-[0-9]{2}' | head -200
done | sort -u)
today=$(date -u +%F); d=$today
grep -qx "$d" <<<"$days" || d=$(date -u -d yesterday +%F)
n=0
while grep -qx "$d" <<<"$days"; do n=$((n + 1)); d=$(date -u -d "$d -1 day" +%F); done
echo "current streak: $n day(s); submitted today (UTC $today): $(grep -qx "$today" <<<"$days" && echo yes || echo NO)"
