import pandas as pd


def bring_columns_to_start(columns, dataframe):
    """

    :type columns: list
    :type dataframe: pd.DataFrame
    :rtype: pd.DataFrame
    """
    column_headers = list(dataframe.columns.values)
    for column in reversed(columns):
        column_headers.insert(0, column_headers.pop(column_headers.index(column)))

    result = dataframe.ix[:, column_headers]
    return result


def bring_columns_to_end(columns, dataframe):
    """

    :type columns: list
    :type dataframe: pd.DataFrame
    :rtype: pd.DataFrame
    """

    column_headers = list(dataframe.columns.values)
    for column in columns:
        column_headers.append(column_headers.pop(column_headers.index(column)))

    result = dataframe.ix[:, column_headers]
    return result


def change_column_suffix(dataframe: pd.DataFrame, old_suffix: str, new_suffix: str) -> pd.DataFrame:
    column_names = dataframe.columns.values
    for index, column_name in enumerate(column_names):
        if column_name.endswith(old_suffix):
            column_names[index] = column_name[:-len(old_suffix)] + new_suffix

    dataframe.columns = column_names
    return dataframe
