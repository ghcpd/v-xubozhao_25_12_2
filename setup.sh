#!/usr/bin/env bash
# Create a reproducible virtual environment and install pinned dependencies.
set -euo pipefail

VENV_DIR=".venv"
PY=${PY:-python}

echo "Creating virtual environment at $VENV_DIR"
$PY -m venv "$VENV_DIR"
echo "Activating and upgrading pip"
source "$VENV_DIR/bin/activate"
python -m pip install --upgrade pip setuptools wheel
echo "Installing pinned dependencies from requirements.txt"
pip install -r requirements.txt
echo "Setup complete. Activate with: source $VENV_DIR/bin/activate"
#!/usr/bin/env bash
# Reproducible environment setup: creates a venv in .venv and installs pinned dependencies
set -euo pipefail

python -m venv .venv
echo "Created virtualenv in .venv"

# Use the pip inside the venv to install requirements
if [ -f ".venv/bin/pip" ]; then
  .venv/bin/pip install --upgrade pip
  .venv/bin/pip install -r requirements.txt
else
  # Windows path
  .venv\Scripts\pip.exe install --upgrade pip
  .venv\Scripts\pip.exe install -r requirements.txt
fi

echo "Dependencies installed into .venv"