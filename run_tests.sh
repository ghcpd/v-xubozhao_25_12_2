#!/usr/bin/env bash
set -euo pipefail

VENVDIR="${VENVDIR:-.venv}"

if [[ -d "$VENVDIR"/bin ]]; then
  # shellcheck source=/dev/null
  source "$VENVDIR"/bin/activate
elif [[ -d "$VENVDIR"/Scripts ]]; then
  # for Git Bash on Windows
  # shellcheck source=/dev/null
  source "$VENVDIR"/Scripts/activate
else
  echo "[run_tests] Virtualenv not found at $VENVDIR. Run ./setup.sh first." >&2
  exit 1
fi

export PYTHONPATH="${PYTHONPATH:-$(pwd)}"

pytest -q
