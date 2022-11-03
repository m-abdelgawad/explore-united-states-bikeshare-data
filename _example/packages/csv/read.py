import pandas as pd


def read_csv(file_path, cols_types_dict=None):

    df = pd.read_csv(file_path, dtype=cols_types_dict)
    return df
