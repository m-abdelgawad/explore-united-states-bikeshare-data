from packages.dataframe.clean import remove_empty_rows, remove_empty_columns, \
    choose_columns
from packages.excel.read import read_excel


def clean_df(sheet_path, cols_types_dict):

    df = read_excel(file_path=sheet_path, header_row_position=1,
                    cols_types_dict=cols_types_dict)

    df = remove_empty_rows(df)

    df = remove_empty_columns(df)

    df = choose_columns(df, cols_list=list(cols_types_dict.keys()))

    return df
