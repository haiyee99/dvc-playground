import logging
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from common import load_params


def standardize(df):
    logging.info("Standardizing data...")

    for column in df.columns:
        df[column] = (df[column] - df[column].mean()) / df[column].std()

    return dataframe


def split(df, **kwargs):
    logging.info("Splitting data to train and test sets...")

    return train_test_split(df, **kwargs)


if __name__ == "__main__":
    logging.getLogger().name = "Transform"
    logging.getLogger().setLevel(logging.INFO)

    dataframe = pd.read_csv("data/data.csv")
    dataframe = standardize(dataframe)

    params = load_params("transform")
    train, test = split(dataframe, **params)
    train.to_csv("data/train.csv", index=False)
    test.to_csv("data/test.csv", index=False)
