# Dependency Audit (Python ≥3.10)

| Package        | Old Version | Issues (Incompatibility / Security / EOL)                                                                 | Recommended Version | Notes / Breaking Changes                                      |
|----------------|------------:|----------------------------------------------------------------------------------------------------------|---------------------|----------------------------------------------------------------|
| numpy          | 1.18.0      | Not compatible with Python 3.10 (requires ≥1.21); several CVEs in <1.21 (e.g., CVE-2021-33430); EOL      | 1.26.4              | Latest 1.26.x stable, supports Py3.10–3.12                      |
| scipy          | 1.5.2       | Not compatible with Python 3.10 (requires ≥1.7); depends on older numpy                                  | 1.11.4              | Matches sklearn 1.4.x; supports Py3.10–3.12                    |
| scikit-learn   | 0.24.1      | No Py3.10 wheels; older API; depends on old numpy/scipy                                                  | 1.4.2               | Minor API changes (e.g., `n_features_in_` enforcement); see release notes |
| pandas         | 1.1.5       | Not compatible with Python 3.10 (requires ≥1.3.3); EOL; potential CSV injection CVEs in older releases   | 2.2.3               | PyArrow optional; string dtype behavior evolved                 |
| matplotlib     | 3.3.2       | Not compatible with Python 3.10 (requires ≥3.5); CVE-2020-25658/25664 (SVG/GIF issues)                  | 3.8.4               | Backend config changes; tight numpy floor                       |
| pytest         | 5.4.3       | Not compatible with Python 3.10 (requires ≥6.2.5); EOL                                                   | 8.3.3               | CLI options stable; new warnings filters                        |
| fastapi        | 0.63.0      | Old Starlette/Pydantic v1; missing features & security patches; pydantic v2 migration needed             | 0.115.6             | Uses pydantic v2; response_model serialization differences      |
| uvicorn        | 0.13.3      | Old h11/httptools; missing lifespan fixes; fewer ASGI features                                          | 0.30.1              | `--factory` changes; see changelog                             |
| httpx *        | —           | Needed for FastAPI TestClient (Starlette)                                                               | 0.27.2              | Added explicitly for tests                                      |
| pydantic *     | —           | FastAPI runtime dependency                                                                              | 2.9.2               | v2; `model_dump` replaces `dict()`                              |

*Added dependencies for completeness.

> Audit Date: 2025-12-02
