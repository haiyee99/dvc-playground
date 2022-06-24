import os
import sys
import numpy as np
import pandas as pd


def create_empty_directory(path):
    os.makedirs(path, exist_ok=True)


def generate_data(nrow, ndim):
    return pd.DataFrame(np.random.random((nrow, ndim)))


if __name__ == "__main__":
    create_empty_directory("data")

    nrow = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    ndim = int(sys.argv[2]) if len(sys.argv) > 2 else 32

    data = generate_data(nrow, ndim)
    data.to_csv("data/data.csv", index=False)

    print(f"Generated {nrow} x {ndim} data")
