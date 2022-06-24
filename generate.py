import os
import numpy as np
import pandas as pd


def create_empty_directory(path):
    os.makedirs(path, exist_ok=True)


def generate_data(nrow, ndim):
    return pd.DataFrame(np.random.random(nrow, ndim))


if __name__ == "__main__":
    create_empty_directory("data")

    data = generate_data(100, 32)
    data.to_csv("data/data.csv", index=False)
