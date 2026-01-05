"""
Minimal demo to exercise key dependencies.
Run: python demo.py
"""
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from fastapi import FastAPI
from fastapi.testclient import TestClient
import scipy.stats as stats


def main():
    # numpy + pandas
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    s = a + b
    df = pd.DataFrame({"a": a, "b": b, "sum": s})
    print("DataFrame:\n", df)

    # scipy + sklearn
    X, y = make_classification(
        n_samples=50, n_features=4, n_informative=2, n_redundant=0, random_state=42
    )
    model = LogisticRegression(max_iter=200)
    model.fit(X, y)
    acc = model.score(X, y)
    print(f"LogisticRegression accuracy: {acc:.3f}")
    print(f"Phi(0) from scipy.stats.norm: {stats.norm.cdf(0):.6f}")

    # matplotlib
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1], label="line")
    ax.legend()
    fig.savefig("demo_plot.png")
    plt.close(fig)
    print("Saved demo_plot.png")

    # fastapi + httpx TestClient
    app = FastAPI()

    @app.get("/ping")
    def ping():
        return {"pong": True}

    client = TestClient(app)
    resp = client.get("/ping")
    print("FastAPI /ping:", resp.status_code, resp.json())


if __name__ == "__main__":
    main()
