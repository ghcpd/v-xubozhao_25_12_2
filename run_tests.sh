#!/usr/bin/env bash
set -euo pipefail

VENV_DIR=".venv"

if [ -d "$VENV_DIR" ]; then
  echo "Activating virtualenv $VENV_DIR"
  # shellcheck disable=SC1091
  source "$VENV_DIR/bin/activate"
else
  echo "Virtualenv not found. Please run ./setup.sh first or set PY env var to point to Python."
  exit 1
fi

echo "Running pytest..."
pytest -q
#!/usr/bin/env bash
set -euo pipefail

if [ -f ".venv/bin/pytest" ]; then
  .venv/bin/pytest -q
else
  # Windows path
  .venv\Scripts\pytest.exe -q || pytest -q
fi
