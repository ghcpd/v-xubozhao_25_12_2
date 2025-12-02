# Dependency Diff (Before → After)

| Package       | Before        | After    | Justification / Notes |
|---------------|---------------|----------|------------------------|
| numpy         | 1.18.0        | 2.3.5    | Py3.10+ incompatible; security fixes; stable MSVC wheels for Py3.13.|
| scipy         | 1.5.2         | 1.16.3   | Py3.10+ incompatible; wheels available for Py3.13; supports numpy 2.x.|
| scikit-learn  | 0.24.1        | 1.7.2    | Py3.10+ incompatible; substantial API/bugfixes; aligns with scipy/numpy.|
| pandas        | 1.1.5         | 2.3.3    | Py3.10+ incompatible; CVEs in old versions; performance/features.|
| matplotlib    | 3.3.2         | 3.10.7   | Py3.10+ incompatible; CVE-2020-25658/25664; backend fixes.|
| pytest        | 5.4.3         | 9.0.1    | Py3.10+ incompatible; modern plugin APIs and bugfixes.|
| fastapi       | 0.63.0        | 0.123.1  | Many security/feature releases; now pydantic v2; Starlette 0.50.0.|
| uvicorn       | 0.13.3        | 0.38.0   | ASGI lifespan fixes; HTTP/2; dependency bumps.|
| httpx         | —             | 0.28.1   | Required for FastAPI TestClient; kept in sync with Starlette.|
| pydantic      | —             | 2.12.5   | FastAPI runtime dependency; v2 required.|

> Pytest run: **7 passed in 3.94s**
> Date: 2025-12-02
