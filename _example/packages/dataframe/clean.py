import pandas as pd


def remove_empty_rows(df):
    return df.dropna(how='all', axis=0)


def remove_empty_columns(df):
    return df.dropna(how='all', axis=1)


def choose_columns(df, cols_list):
    return df[cols_list]
