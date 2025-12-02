# Dependency upgrade + pytest validation

This workspace contains an updated `requirements.txt`, simple demo, and pytest-based runtime tests.

Quick steps:

1. Create virtual env & install:

```bash
./setup.sh
```

2. Run tests:

```bash
./run_tests.sh
```

If your OS is Windows / PowerShell, create the venv with:

```powershell
py -3 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
pytest -q
```
