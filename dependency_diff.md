# Dependency Upgrade Diff (requirements_old.txt → requirements.txt)

| Package | Before | After | Key Changes / Justification |
|---------|--------|-------|-----------------------------|
| numpy | 1.18.0 | 2.3.5 | Python 3.10+ support; performance, SIMD, dtype enhancements; security fix (e.g., CVE-2021-41496); removal of deprecated aliases (`np.bool`, etc.) from 1.20+ — audit code for deprecated names. |
| scipy | 1.5.2 | 1.16.3 | Python ≥3.11; many new modules/features; depends on numpy ≥1.25; potential API removals of long-deprecated symbols. |
| scikit-learn | 0.24.1 | 1.7.2 | Python ≥3.10; improved estimators, array API, threadpoolctl updates; some deprecated params removed (e.g., `normalize` in linear models). |
| pandas | 1.1.5 | 2.3.3 | Python ≥3.9; nullable dtypes improvements, copy-on-write default (>=2.1); some deprecated args removed; check for `DataFrame.append` removal (use `pd.concat`). |
| matplotlib | 3.3.2 | 3.10.7 | Python ≥3.10; richer type hints, style updates; deprecated rcParams removed; default backend changes may apply. |
| pytest | 5.4.3 | 9.0.1 | Python ≥3.10; new assertion introspection, config changes; deprecated `--result-log` removed; ensure plugins are compatible. |
| fastapi | 0.63.0 | 0.123.1 | Big jump; now on Pydantic v2 (breaking changes in validators, `Config` → `model_config`); Starlette upgraded; check all response/request models. |
| uvicorn | 0.13.3 | 0.38.0 | Python ≥3.9; improved hot-reload/watchfiles; default log config changes; httptools/websockets updated. |
| httpx | — | 0.28.1 | Added to support FastAPI TestClient and HTTP validation in tests. |

> **Compatibility note:** All selected versions provide wheels for Python 3.13 on Windows, ensuring smooth installs and reproducibility.
