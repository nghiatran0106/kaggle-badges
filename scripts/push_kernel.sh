#!/usr/bin/env bash
# Usage: scripts/push_kernel.sh <folder-with-kernel-metadata.json>
# Pushes a notebook/script to Kaggle and polls until it finishes.
set -euo pipefail
dir="${1:?folder}"
id=$(python3 -c "import json,sys;print(json.load(open(sys.argv[1]))['id'])" "$dir/kernel-metadata.json")
kaggle kernels push -p "$dir"
while true; do
  st=$(kaggle kernels status "$id" 2>&1 | tail -1)
  echo "$(date +%T) $st"
  case "$st" in *COMPLETE*|*ERROR*|*CANCEL*) break;; esac
  sleep 20
done
