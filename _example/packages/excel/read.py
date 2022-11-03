import pandas as pd


def read_excel(file_path, header_row_position=0, cols_types_dict=None):
    df = pd.read_excel(file_path, header=header_row_position,
                       dtype=cols_types_dict)
    return df
