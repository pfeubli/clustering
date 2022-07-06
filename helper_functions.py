import pandas as pd


def loading_dataset(filename, sep=';'):
    return pd.read_csv(filename, sep=sep)


def loading_all_datasets(list_of_filenames):
    datasets = []
    for filename in list_of_filenames:
        datasets.append(loading_dataset(filename))
    return datasets


def clean_data(df):
    initial_rows = len(df)
    df_clean = df.dropna()
    final_rows = len(df_clean)
    return initial_rows, final_rows, df_clean
