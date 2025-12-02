# Dependency upgrade summary

Before (from `requirements_old.txt`):

```
scikit-learn==0.24.1
numpy==1.18.0
pandas==1.1.5
matplotlib==3.3.2
scipy==1.5.2
pytest==5.4.3
fastapi==0.63.0
uvicorn==0.13.3
```

After (new `requirements.txt`):

```
numpy==1.25.1
pandas==2.1.3
scikit-learn==1.2.2
scipy==1.10.1
matplotlib==3.7.2
fastapi==0.95.2
uvicorn==0.22.0
pytest==7.4.0
```

Rationale / Justification
- numpy: moved from 1.18 (very old; lacked optimizations and support for newer Python) to 1.25.1 which supports modern Python versions (3.10+) and provides performance and ABI improvements.
- pandas: 1.1.5 -> 2.1.3 to get long-term maintenance on pandas 2.x, speedups and improved typing/data model.
- scikit-learn: 0.24.1 -> 1.2.2 to pick a stable 1.x series with many API improvements and bug fixes; 1.2 keeps compatibility while providing model improvements.
- scipy: 1.5.2 -> 1.10.1 to match newer numeric stack and ensure compatibility with new numpy.
- matplotlib: 3.3.2 -> 3.7.2 to get newer backends, security/bug fixes and Python 3.10+ compatibility.
- fastapi: 0.63.0 -> 0.95.2 for security fixes, dependency updates and improved integration with newer Starlette/async stacks.
- uvicorn: 0.13.3 -> 0.22.0 for bugfixes and support for recent ASGI features.
- pytest: 5.4.3 -> 7.4.0 to take advantage of modern pytest features, better fixtures and improved output.

Notes on breaking changes
- Jumping across major versions (e.g., pandas 1.x -> 2.x) can include breaking API changes; if the existing code uses deprecated pandas internals, tests will highlight issues that require small code updates.
- scikit-learn 1.x changed some defaults in transformers and cross-validation; test coverage should verify existing behavior.

Next steps: add a reproducible setup script, a small demo and pytest-based runtime checks to validate the environment and detect any immediate runtime breakages.
