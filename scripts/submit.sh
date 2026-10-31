#!/usr/bin/env bash
# Usage: scripts/submit.sh <competition-slug> <file> "<message>"
# Submits a file via Kaggle CLI, logs it to submissions.log, then shows latest results.
# Note: kaggle CLI exits 0 even on HTTP errors, so we check its output instead.
set -euo pipefail
comp="${1:?competition slug}"; file="${2:?submission file}"; msg="${3:?message}"
root="$(cd "$(dirname "$0")/.." && pwd)"

[ -f "$file" ] || { echo "No such file: $file" >&2; exit 1; }
kaggle competitions submission-limits "$comp" | grep -i "remaining"
out=$(kaggle competitions submit "$comp" -f "$file" -m "$msg" 2>&1 | grep -v '%|' || true)
echo "$out"
if ! grep -q "Successfully submitted" <<<"$out"; then
  if grep -q "403" <<<"$out"; then
    echo ">> 403: accept the rules first: https://www.kaggle.com/competitions/$comp/rules" >&2
  fi
  exit 1
fi
printf '%s\t%s\t%s\t%s\n' "$(date -Iseconds)" "$comp" "$file" "$msg" >> "$root/submissions.log"
sleep 5
kaggle competitions submissions "$comp" | head -5
