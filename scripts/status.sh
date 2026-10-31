#!/usr/bin/env bash
# Quick overview of what exists on your Kaggle account.
set -uo pipefail
u=$(kaggle config view | awk '/username/{print $3}')
echo "== user: $u"
echo "== kernels";  kaggle kernels list --mine --sort-by dateRun | head -12
echo "== datasets"; kaggle datasets list --mine | head -8
echo "== models";   kaggle models list --owner "$u" | head -8
for c in titanic playground-series-s6e10 connectx; do
  echo "== submissions: $c"; kaggle competitions submissions "$c" 2>&1 | head -4
done
