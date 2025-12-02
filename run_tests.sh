#!/bin/bash

# run_tests.sh - Run pytest test suite
# Usage: bash run_tests.sh

set -e  # Exit on any error

echo "🧪 Running pytest test suite..."
echo ""

# Activate virtual environment
if [ -d "venv" ]; then
    source venv/bin/activate
else
    echo "❌ Virtual environment not found. Run setup.sh first."
    exit 1
fi

# Run pytest with verbose output and coverage
pytest tests/ -v --tb=short --color=yes

echo ""
echo "✅ All tests completed!"
