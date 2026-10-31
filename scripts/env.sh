# Source this file: `source scripts/env.sh`
# Python venv lives in $HOME because exFAT (this drive) does not support symlinks.
export KB_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export KB_VENV="$HOME/.venvs/kaggle-badges"
if [ -f "$KB_VENV/bin/activate" ]; then
  source "$KB_VENV/bin/activate"
else
  echo "venv missing -> uv venv $KB_VENV --python 3.12 && uv pip install -r $KB_ROOT/requirements.txt" >&2
fi
