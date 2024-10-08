import os
from databricks import sql
import pandas as pd
from dotenv import load_dotenv


# load the csv file and insert into databricks
def load(dataset="data/match_results.csv", dataset_2="data/match_results_2019.csv"):
    payload = pd.read_csv(dataset, delimiter=",", skiprows=1)
    payload2 = pd.read_csv(dataset_2, delimiter=",", skiprows=1)
    load_dotenv()
    server_h = os.getenv("SERVER_HOSTNAME")
    access_token = os.getenv("ACCESS_TOKEN")
    http_path = os.getenv("HTTP_PATH")
    with sql.connect(
        server_hostname=server_h,
        http_path=http_path,
        access_token=access_token,
    ) as connection:
        c = connection.cursor()
        c.execute("SHOW TABLES FROM default LIKE 'match_result*'")
        result = c.fetchall()
        if not result:
            c.execute(
                """
                CREATE TABLE MatchResultsDB (
                    Round INTEGER,
                    Date TEXT,
                    "Team 1" TEXT,
                    "Team 2" TEXT,
                    FT TEXT
                )
                """
            )
            # insert
            for _, row in payload.iterrows():
                convert = (_,) + tuple(row)
                c.execute(f"INSERT INTO MatchResultsDB VALUES {convert}")
        c.execute("SHOW TABLES FROM default LIKE 'match_result_2019*'")
        result = c.fetchall()
        if not result:
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS MatchResults2019DB (
                    Round INTEGER,
                    Date TEXT,
                    "Team 1" TEXT,
                    "Team 2" TEXT,
                    FT TEXT
                )
                """
            )
            for _, row in payload2.iterrows():
                convert = (_,) + tuple(row)
                c.execute(f"INSERT INTO MatchResults2019DB VALUES {convert}")
        c.close()

    return "success"