#!/bin/bash
set -e

# Setup script for Analytics Service Backend
# Creates virtual environment and installs upgraded dependencies

echo "================================================"
echo "Analytics Service - Dependency Setup"
echo "================================================"

# Check Python version
PYTHON_VERSION=$(python --version 2>&1 | awk '{print $2}')
MAJOR_VERSION=$(echo $PYTHON_VERSION | cut -d. -f1)
MINOR_VERSION=$(echo $PYTHON_VERSION | cut -d. -f2)

echo "Python version: $PYTHON_VERSION"

if [ "$MAJOR_VERSION" -lt 3 ] || ([ "$MAJOR_VERSION" -eq 3 ] && [ "$MINOR_VERSION" -lt 10 ]); then
    echo "❌ Error: Python 3.10+ required. Current version: $PYTHON_VERSION"
    exit 1
fi

echo "✅ Python version check passed"
echo ""

# Create virtual environment
echo "Creating virtual environment..."
if [ -d "venv" ]; then
    echo "Removing existing venv..."
    rm -rf venv
fi

python -m venv venv

# Activate virtual environment
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi

echo "✅ Virtual environment created and activated"
echo ""

# Upgrade pip, setuptools, wheel
echo "Upgrading pip, setuptools, and wheel..."
pip install --upgrade pip setuptools wheel --quiet

echo "✅ Base tools upgraded"
echo ""

# Install dependencies
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

echo ""
echo "================================================"
echo "✅ Setup Complete!"
echo "================================================"
echo ""
echo "Virtual environment location: $(pwd)/venv"
echo "Python executable: $(which python)"
echo ""
echo "To activate the environment, run:"
echo "  source venv/bin/activate (Linux/macOS)"
echo "  .\\venv\\Scripts\\Activate.ps1 (Windows PowerShell)"
echo ""
echo "To run tests:"
echo "  ./run_tests.sh"
echo "================================================"
