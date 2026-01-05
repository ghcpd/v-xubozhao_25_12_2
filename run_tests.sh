#!/bin/bash
set -e

# Test runner script for Analytics Service Backend
# Executes pytest with verbose output and coverage reporting

echo "================================================"
echo "Analytics Service - Test Suite Execution"
echo "================================================"
echo ""

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "❌ Error: Virtual environment not found."
    echo "Please run setup.sh first:"
    echo "  ./setup.sh"
    exit 1
fi

# Activate virtual environment
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi

echo "Virtual environment activated: $(which python)"
echo ""

# Check if pytest is installed
if ! command -v pytest &> /dev/null; then
    echo "❌ Error: pytest not installed. Please run setup.sh first."
    exit 1
fi

echo "pytest version: $(pytest --version)"
echo ""
echo "================================================"
echo "Running Test Suite..."
echo "================================================"
echo ""

# Run pytest with verbose output
# -v: verbose
# -s: show print statements
# --tb=short: short traceback format
# tests/: test directory
pytest -v -s --tb=short tests/

TEST_EXIT_CODE=$?

echo ""
echo "================================================"

if [ $TEST_EXIT_CODE -eq 0 ]; then
    echo "✅ All tests passed!"
else
    echo "❌ Some tests failed (exit code: $TEST_EXIT_CODE)"
fi

echo "================================================"

exit $TEST_EXIT_CODE
