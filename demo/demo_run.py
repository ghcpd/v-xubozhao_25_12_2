"""Small demo script that exercises key libraries.

Run with: python demo/demo_run.py
"""
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


def main():
    print("Demo: starting tiny analytics pipeline")
    arr = np.arange(1, 6, dtype=float)
    df = pd.DataFrame({"x": arr, "y": arr * 2.0})

    X = df[["x"]].values
    y = df["y"].values

    model = LinearRegression()
    model.fit(X, y)
    pred = model.predict(np.array([[10.0]]))

    print("trained coef:", model.coef_.tolist())
    print("prediction for x=10:", pred.tolist())


if __name__ == "__main__":
    main()
