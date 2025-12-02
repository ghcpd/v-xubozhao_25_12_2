import os
import sys

import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier


def test_numpy_basic():
    a = np.array([1, 2, 3])
    assert int(np.sum(a)) == 6


def test_pandas_basic():
    df = pd.DataFrame({"x": [1, 2, 3]})
    assert int(df.x.sum()) == 6


def test_sklearn_basic():
    X = [[0], [1], [2], [3]]
    y = [0, 0, 1, 1]
    clf = DecisionTreeClassifier(random_state=0)
    clf.fit(X, y)
    preds = clf.predict([[0], [3]])
    assert list(preds) == [0, 1]


def test_matplotlib_basic():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot([0, 1, 2], [0, 1, 4])
    assert fig is not None


def test_fastapi_client():
    # keep this test simple: import FastAPI and ensure a TestClient can perform a small request
    from fastapi import FastAPI

    try:
        # In some environments TestClient may use different transport libs; keep server-side simple.
        from fastapi.testclient import TestClient
    except Exception:
        pytest = __import__("pytest")
        pytest.skip("TestClient not available in this environment")

    app = FastAPI()

    @app.get("/ping")
    def ping():
        return {"ping": "pong"}

    client = TestClient(app)
    r = client.get("/ping")
    assert r.status_code == 200 and r.json() == {"ping": "pong"}
import sys
import numpy as np
import pandas as pd
import sklearn
import matplotlib
import scipy
import fastapi
import uvicorn


def test_python_version():
    # Project requires Python 3.10+
    assert sys.version_info >= (3, 10), "Python 3.10+ required"


def test_numpy_pandas_basic():
    a = np.array([1, 2, 3])
    df = pd.DataFrame({"x": a})
    assert df["x"].sum() == 6


def test_sklearn_simple_fit():
    from sklearn.linear_model import LinearRegression

    X = np.array([[1], [2], [3], [4]], dtype=float)
    y = np.array([2, 4, 6, 8], dtype=float)
    model = LinearRegression()
    model.fit(X, y)
    pred = model.predict(np.array([[5.0]]))
    assert abs(pred[0] - 10.0) < 1e-6


def test_matplotlib_import():
    # ensure plotting backend can be imported and a figure created
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot([0, 1], [0, 1])
    assert len(fig.axes) == 1


def test_scipy_import():
    from scipy import integrate

    res = integrate.quad(lambda x: x * x, 0, 1)
    assert pytest_close(res[0], 1.0 / 3.0)


def pytest_close(a, b, tol=1e-6):
    return abs(a - b) < tol


def test_fastapi_uvicorn_import():
    # basic importability check
    app = fastapi.FastAPI()
    assert hasattr(app, "routes")
    assert hasattr(uvicorn, "run")
