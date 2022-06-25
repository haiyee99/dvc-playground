import json
import pandas as pd


def create_description(df):
    return {
        "nrow": df.shape[0],
        "ncol": df.shape[1],
    }


if __name__ == "__main__":
    train = pd.read_csv("data/train.csv")
    test = pd.read_csv("data/test.csv")

    desc = {
        "train": create_description(train),
        "test": create_description(test),
    }

    with open("data/description.json", "w") as fp:
        json.dump(desc, fp)
