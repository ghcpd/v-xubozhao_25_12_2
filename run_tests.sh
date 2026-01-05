#!/usr/bin/env bash
set -euo pipefail
VENV_DIR=${VENV_DIR:-.venv}

if [[ "${OS:-}" == "Windows_NT" ]]; then
  source "$VENV_DIR/Scripts/activate"
else
  source "$VENV_DIR/bin/activate"
fi

pytest -q "$@"
