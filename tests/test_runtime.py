import io

import numpy as np
import pandas as pd
import matplotlib
import pytest

# Use non-interactive backend for tests
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from scipy import linalg, stats
from sklearn.linear_model import LinearRegression
from fastapi import FastAPI
from fastapi.testclient import TestClient
import uvicorn


EXPECTED_VERSIONS = {
    "numpy": "2.3.5",
    "pandas": "2.3.3",
    "scipy": "1.16.3",
    "scikit-learn": "1.7.2",
    "matplotlib": "3.10.7",
    "pytest": "9.0.1",
    "fastapi": "0.123.1",
    "uvicorn": "0.38.0",
}


def test_versions():
    import scipy
    import sklearn
    import fastapi as fastapi_pkg

    # Ensure we loaded the versions we pinned
    assert np.__version__ == EXPECTED_VERSIONS["numpy"]
    assert pd.__version__ == EXPECTED_VERSIONS["pandas"]
    assert scipy.__version__ == EXPECTED_VERSIONS["scipy"]
    assert sklearn.__version__ == EXPECTED_VERSIONS["scikit-learn"]
    assert matplotlib.__version__ == EXPECTED_VERSIONS["matplotlib"]
    # pytest version is validated via CLI
    assert fastapi_pkg.__version__ == EXPECTED_VERSIONS["fastapi"]
    assert uvicorn.__version__ == EXPECTED_VERSIONS["uvicorn"]


def test_numpy_basic():
    arr = np.array([1, 2, 3], dtype=np.int64)
    assert arr.sum() == 6
    assert np.dot(arr, arr) == 14


def test_pandas_basic():
    df = pd.DataFrame({"group": ["a", "a", "b"], "value": [1, 2, 3]})
    grouped = df.groupby("group")["value"].sum().to_dict()
    assert grouped == {"a": 3, "b": 3}


def test_scipy_basic():
    mat = np.array([[3.0, 2.0], [1.0, 4.0]])
    vec = np.array([5.0, 6.0])
    solution = linalg.solve(mat, vec)
    # Verify Ax ≈ b
    np.testing.assert_allclose(mat @ solution, vec)
    # stats: standard normal CDF at 0 is 0.5
    assert stats.norm.cdf(0) == pytest.approx(0.5, rel=1e-9)


def test_sklearn_basic():
    X = np.array([[1], [2], [3], [4]], dtype=np.float64)
    y = np.array([2, 4, 6, 8], dtype=np.float64)
    model = LinearRegression().fit(X, y)
    pred = model.predict(np.array([[5]], dtype=np.float64))[0]
    assert pred == pytest.approx(10.0, rel=1e-9)


def test_matplotlib_basic():
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1], label="line")
    ax.legend()
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    data = buf.read()
    assert len(data) > 0
    plt.close(fig)


def test_fastapi_app():
    app = FastAPI()

    @app.get("/ping")
    def ping():
        return {"pong": True}

    client = TestClient(app)
    resp = client.get("/ping")
    assert resp.status_code == 200
    assert resp.json() == {"pong": True}
