#!/bin/bash

# setup.sh - Create virtual environment and install dependencies
# Usage: bash setup.sh

set -e  # Exit on any error

echo "🔧 Setting up Python virtual environment..."

# Remove old venv if exists
if [ -d "venv" ]; then
    echo "Removing existing virtual environment..."
    rm -rf venv
fi

# Create new virtual environment
echo "Creating new virtual environment..."
python -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

echo "✅ Setup complete!"
echo ""
echo "To activate the environment manually, run:"
echo "  source venv/bin/activate"
echo ""
echo "To run tests, execute:"
echo "  bash run_tests.sh"
