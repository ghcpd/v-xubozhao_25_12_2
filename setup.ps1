# setup.ps1 - Create virtual environment and install dependencies
# Usage: .\setup.ps1

$ErrorActionPreference = "Stop"

Write-Host "🔧 Setting up Python virtual environment..." -ForegroundColor Cyan
Write-Host ""

# Remove old venv if exists
if (Test-Path "venv") {
    Write-Host "Removing existing virtual environment..." -ForegroundColor Yellow
    Remove-Item -Recurse -Force venv
}

# Create new virtual environment
Write-Host "Creating new virtual environment..." -ForegroundColor Green
python -m venv venv

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Green
& .\venv\Scripts\Activate.ps1

# Upgrade pip
Write-Host "Upgrading pip..." -ForegroundColor Green
python -m pip install --upgrade pip

# Install dependencies
Write-Host "Installing dependencies from requirements.txt..." -ForegroundColor Green
pip install -r requirements.txt

Write-Host ""
Write-Host "✅ Setup complete!" -ForegroundColor Green
Write-Host ""
Write-Host "To activate the environment manually, run:" -ForegroundColor Cyan
Write-Host "  .\venv\Scripts\Activate.ps1" -ForegroundColor White
Write-Host ""
Write-Host "To run tests, execute:" -ForegroundColor Cyan
Write-Host "  .\run_tests.ps1" -ForegroundColor White
