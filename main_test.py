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
        ["python", "python_main.py", "transform_load"],
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
            SELECT m1.Team1 AS home_team, m1.Team2 AS away_team,
            AVG(CASE 
                WHEN CAST(SPLIT_PART(m1.FT, '-', 1) AS INTEGER) > CAST(SPLIT_PART(m1.FT, '-', 2) AS INTEGER) THEN 1
                ELSE 0
                END) AS avg_home_team_wins,
            COUNT(*) AS total_matches_played
            FROM MatchResultsDB m1
            JOIN MatchResults2019DB m2 ON m1.Team1 = m2.Team1 
                                    AND m1.Team2 = m2.Team2
            GROUP BY m1.Team1, m1.Team2
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