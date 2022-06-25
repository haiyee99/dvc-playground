import os
import json
import random
from common import load_params


def get_metric():
    return {
        "metric_a": random.random(),
        "metric_b": random.random(),
    }


def get_plot():
    return [
        {
            "x_axis": random.random(),
            "y_axis": random.random(),
        }
        for i in range(100)
    ]


if __name__ == "__main__":
    params = load_params("random_plot")
    random.seed(params["seed"])

    metric = get_metric()
    plot = get_plot()

    os.makedirs("metrics", exist_ok=True)
    with open("metrics/metric.json", "w") as fp:
        json.dump(metric, fp)

    os.makedirs("plots", exist_ok=True)
    with open("plots/plot.json", "w") as fp:
        json.dump(plot, fp)
