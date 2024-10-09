# Vishesh_Gupta_IDS706_Week5

[![CI](https://github.com/nogibjj/Vishesh_Gupta_IDS706_Week6/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Vishesh_Gupta_IDS706_Week6/actions/workflows/cicd.yml)

# Project: ETL-Query Pipeline with Databricks

## Overview
The goal of this project is to build an ETL (Extract, Transform, Load) and Query pipeline using cloud services like Databricks. It focuses on designing complex SQL queries for a MySQL database, involving joins, aggregation, and sorting, applied to match results data.

## Complex SQL Query
This query analyzes match results over multiple seasons to calculate the average goals scored by teams that participated in both 2019 and previous seasons.

```sql
WITH all_matches AS (
    SELECT '2019' AS season, Team1 AS team, Team2 AS opponent, 
        CAST(SPLIT_PART(FT, '-', 1) AS INT) AS goals_scored,
        CAST(SPLIT_PART(FT, '-', 2) AS INT) AS goals_conceded
    FROM MatchResults2019DB
    UNION ALL
    SELECT 'previous' AS season, Team1 AS team, Team2 AS opponent, 
        CAST(SPLIT_PART(FT, '-', 1) AS INT) AS goals_scored,
        CAST(SPLIT_PART(FT, '-', 2) AS INT) AS goals_conceded
    FROM MatchResultsDB
),
team_matches AS (
    SELECT team, opponent, 
        AVG(goals_scored) AS avg_goals_scored, 
        COUNT(*) AS total_matches_played
    FROM all_matches
    WHERE team IN (
        SELECT DISTINCT team FROM (
            SELECT Team1 AS team FROM MatchResults2019DB
            UNION ALL
            SELECT Team2 AS team FROM MatchResults2019DB
            INTERSECT
            SELECT Team1 AS team FROM MatchResultsDB
            UNION ALL
            SELECT Team2 AS team FROM MatchResultsDB
        ) AS common_teams
    )
    GROUP BY team, opponent
);
```
### Query Explanation

- **CTE `all_matches`**: Combines match results from 2019 and previous seasons, extracting teams, opponents, and scores.
- **CTE `team_matches`**: Filters out teams that played in both seasons and calculates:
  - `avg_goals_scored`: Average goals scored by the team across all matches.
  - `total_matches_played`: Number of matches played by the team.

The query returns the average goals scored by each team against specific opponents and the total number of matches played, allowing analysis of team performance consistency. You can check the results in the query log [here](https://github.com/nogibjj/Vishesh_Gupta_IDS706_Week6/blob/main/query_log.md).

```
Vishesh_Gupta_IDS706_Week5/
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── .github/
│   └── workflows/cicd.yml
├── .gitignore
├── data/
│   └── match_results.csv
│   └── match_results_2019.csv
├── Makefile
├── python_main.py
├── mylib/
│   ├── __pycache__
│   ├── __init__.py
│   ├── extract.py
│   ├── query.py
│   └── transform_load.py
├── test_results.md
├── query_log.md
├── README.md
├── requirements.txt
├── MatchResultsDB.db
└── main_test.py
```

## Check format and test errors 
1. Format code `make format`
2. Lint code `make lint`
3. Test code `make test`


## References 
1. https://github.com/nogibjj/sqlite-lab
2. https://learn.microsoft.com/en-us/azure/databricks/dev-tools/python-sql-connector

