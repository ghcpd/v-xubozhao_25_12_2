"""Small demo script to exercise core libraries quickly.

Run: python demo/demo_basic.py
"""
import numpy as np
import pandas as pd

print("numpy version:", np.__version__)
print("pandas version:", pd.__version__)

arr = np.array([1, 2, 3, 4])
print("sum:", arr.sum())

df = pd.DataFrame({"a": [10, 20, 30]})
print("df sum:", df.a.sum())
