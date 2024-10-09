import os
import requests
import pandas as pd


def extract(url="https://raw.githubusercontent.com/footballcsv/england/refs/heads/master/2010s/2010-11/eng.1.csv",
    url_2="https://raw.githubusercontent.com/footballcsv/england/refs/heads/master/2010s/2019-20/eng.1.csv",
    file_path="data/match_results.csv",
    file_path_2="data/match_results_2019.csv"):
    if not os.path.exists("data"):
        os.makedirs("data")
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    with requests.get(url_2) as r:
        with open(file_path_2, "wb") as f:
            f.write(r.content)
    df = pd.read_csv(file_path)
    df_2 = pd.read_csv(file_path_2)

    df_subset = df.head(100)
    df_subset_2 = df.head(100)

    df_subset.to_csv(file_path, index=False)
    df_subset_2.to_csv(file_path_2, index=False)
    return file_path, file_path_2
