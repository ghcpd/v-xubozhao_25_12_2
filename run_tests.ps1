# run_tests.ps1 - Run pytest test suite
# Usage: .\run_tests.ps1

$ErrorActionPreference = "Stop"

Write-Host "🧪 Running pytest test suite..." -ForegroundColor Cyan
Write-Host ""

# Check if virtual environment exists
if (-not (Test-Path "venv")) {
    Write-Host "❌ Virtual environment not found. Run setup.ps1 first." -ForegroundColor Red
    exit 1
}

# Activate virtual environment
& .\venv\Scripts\Activate.ps1

# Run pytest with verbose output
pytest tests/ -v --tb=short --color=yes

Write-Host ""
Write-Host "✅ All tests completed!" -ForegroundColor Green
