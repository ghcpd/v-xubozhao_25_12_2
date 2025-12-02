#!/usr/bin/env bash
set -euo pipefail
PYTHON=${PYTHON:-python3}
VENV_DIR=${VENV_DIR:-.venv}

if [ ! -d "$VENV_DIR" ]; then
  "$PYTHON" -m venv "$VENV_DIR"
fi

if [[ "${OS:-}" == "Windows_NT" ]]; then
  source "$VENV_DIR/Scripts/activate"
else
  source "$VENV_DIR/bin/activate"
fi

python -m pip install --upgrade pip
pip install -r requirements.txt
