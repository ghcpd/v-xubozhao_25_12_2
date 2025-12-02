import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import scipy.stats as stats
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from fastapi import FastAPI
from fastapi.testclient import TestClient
import uvicorn


def test_numpy_basic_math():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    assert np.array_equal(a + b, np.array([5, 7, 9]))


def test_pandas_dataframe_ops():
    df = pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})
    df["z"] = df["x"] + df["y"]
    assert df["z"].tolist() == [5, 7, 9]


def test_scipy_stats_cdf():
    val = stats.norm.cdf(0)
    assert abs(val - 0.5) < 1e-9


def test_sklearn_logistic_regression():
    X, y = make_classification(
        n_samples=50,
        n_features=4,
        n_informative=2,
        n_redundant=0,
        random_state=42,
    )
    model = LogisticRegression(max_iter=200)
    model.fit(X, y)
    acc = model.score(X, y)
    assert acc > 0.8


def test_matplotlib_plot(tmp_path):
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1])
    out = tmp_path / "test_plot.png"
    fig.savefig(out)
    assert out.exists() and out.stat().st_size > 0
    plt.close(fig)


def test_fastapi_with_testclient():
    app = FastAPI()

    @app.get("/ping")
    def ping():
        return {"pong": True}

    client = TestClient(app)
    resp = client.get("/ping")
    assert resp.status_code == 200
    assert resp.json() == {"pong": True}


def test_uvicorn_config_instantiation():
    cfg = uvicorn.Config("tests.test_runtime:dummy_app", factory=True)
    assert cfg.app == "tests.test_runtime:dummy_app"


def dummy_app():
    app = FastAPI()
    @app.get("/")
    def root():
        return {"ok": True}
    return app
