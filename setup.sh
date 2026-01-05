#!/usr/bin/env bash
set -euo pipefail

# Create virtual environment if missing
VENVDIR="${VENVDIR:-.venv}"
PYTHON_BIN="${PYTHON_BIN:-python3}"

if [[ ! -d "$VENVDIR" ]]; then
  echo "[setup] Creating virtual environment in $VENVDIR"
  "$PYTHON_BIN" -m venv "$VENVDIR"
fi

# Activate venv (POSIX)
# shellcheck source=/dev/null
source "$VENVDIR"/bin/activate

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo "[setup] Environment ready. Activate with: source $VENVDIR/bin/activate"
