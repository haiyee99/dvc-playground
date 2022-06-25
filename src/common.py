import yaml


def load_params(name):
    with open("src/params.yaml", "r") as fp:
        params = yaml.safe_load(fp)

    return params[name]
