# Dependency upgrade report

## Before -> After

Original (`requirements_old.txt`):

- scikit-learn==0.24.1
- numpy==1.18.0
- pandas==1.1.5
- matplotlib==3.3.2
- scipy==1.5.2
- pytest==5.4.3
- fastapi==0.63.0
- uvicorn==0.13.3

Updated (`requirements.txt`):

- scikit-learn==1.3.2
- numpy==1.25.4
- pandas==2.1.3
- matplotlib==3.7.2
- scipy==1.11.3
- pytest==7.4.2
- fastapi==0.95.2
- uvicorn==0.22.0
- httpx==0.24.1
- requests==2.31.0

## Justifications / notes

- numpy: 1.18 is ancient and lacks Python 3.10+ compatibility and new features. The recommended modern 1.25.x series supports Python 3.10+ and provides performance and ABI improvements.
- pandas: 1.1.5 is EOL and predates many API changes and performance improvements. Pandas 2.x modernizes typing and performance on top of modern numpy.
- scikit-learn: 0.24.1 is from 2020; upgrading to 1.3.x brings many algorithmic improvements and bug fixes. (Note: on some platforms scikit-learn still requires binary wheels; building from source will need C toolchains.)
- scipy: 1.5.2 is outdated. 1.11.x series provides bug fixes and improvements.
- matplotlib: 3.3 is old; 3.7 provides many new features and bug fixes.
- pytest: 5.x is long outdated; pytest 7+ supports newer features and is compatible with Python 3.10+.
- fastapi / uvicorn: both upgraded to modern, supported releases that match other updated dependencies.
- httpx / requests: added to support FastAPI testing via TestClient and simpler HTTP checks.

## Reproducibility

All packages are pinned in `requirements.txt` to ensure reproducible installs. For stricter reproducibility you may also create a lock file (pip-compile or pipenv/poetry lock) depending on your preferred tooling.

## Running tests locally (quick)

```bash
./setup.sh
./run_tests.sh
```

If running on Windows PowerShell, see `README.md` for platform-specific commands.
