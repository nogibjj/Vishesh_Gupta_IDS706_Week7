import subprocess


def test_extract():
    """Test extract()"""
    result = subprocess.run(
        ["python", "python_main.py", "extract"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Extracting data..." in result.stdout


def test_load():
    """Test transform_load()"""
    result = subprocess.run(
        ["python", "python_main.py", "load"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Transforming data..." in result.stdout

def test_query():
    """tests general_query"""
    result = subprocess.run(
        [
            "python","python_main.py",
            "query",
            """
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
            )

            SELECT team, opponent, avg_goals_scored, total_matches_played
            FROM team_matches
            ORDER BY total_matches_played DESC
            LIMIT 10;
            """,
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0

if __name__ == "__main__":
    test_extract()
    test_load()
    test_query()