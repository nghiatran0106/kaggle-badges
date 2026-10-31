#!/usr/bin/env bash
# Makes the dataset PUBLIC and pushes the public notebook (usability 15/17 -> expected 17/17).
# Run this yourself: it publishes content under your Kaggle profile.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
slug=tranphunghia233871/connectx-self-play-game-logs

sed -i 's/"isPrivate": true/"isPrivate": false/' "$here/upload/dataset-metadata.json"
kaggle -W datasets metadata --update -p "$here/upload" "$slug"
kaggle -W kernels push -p "$here/notebook"
echo "Check usability in a few minutes: kaggle datasets list --mine -s connectx"
