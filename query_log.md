```sql

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
            
```

```response from databricks
[Row(home_team='Sunderland AFC', away_team='Arsenal FC', avg_home_team_wins=0.0, total_matches_played=1), Row(home_team='Chelsea FC', away_team='Wolverhampton Wanderers FC', avg_home_team_wins=1.0, total_matches_played=1), Row(home_team='Bolton Wanderers FC', away_team='Liverpool FC', avg_home_team_wins=0.0, total_matches_played=1), Row(home_team='Manchester City FC', away_team='Chelsea FC', avg_home_team_wins=1.0, total_matches_played=1), Row(home_team='Newcastle United FC', away_team='Stoke City FC', avg_home_team_wins=0.0, total_matches_played=1), Row(home_team='Sunderland AFC', away_team='Manchester United FC', avg_home_team_wins=0.0, total_matches_played=1), Row(home_team='Newcastle United FC', away_team='Wigan Athletic FC', avg_home_team_wins=0.0, total_matches_played=1), Row(home_team='Liverpool FC', away_team='Blackpool FC', avg_home_team_wins=0.0, total_matches_played=1), Row(home_team='Wigan Athletic FC', away_team='Wolverhampton Wanderers FC', avg_home_team_wins=1.0, total_matches_played=1), Row(home_team='Stoke City FC', away_team='Manchester United FC', avg_home_team_wins=0.0, total_matches_played=1)]
```

```sql

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
            
```

```response from databricks
[Row(home_team='West Bromwich Albion FC', away_team='Sunderland AFC', avg_home_team_wins=1.0, total_matches_played=4), Row(home_team='Tottenham Hotspur FC', away_team='Everton FC', avg_home_team_wins=0.0, total_matches_played=4), Row(home_team='Aston Villa FC', away_team='Everton FC', avg_home_team_wins=1.0, total_matches_played=4), Row(home_team='Sunderland AFC', away_team='Arsenal FC', avg_home_team_wins=0.0, total_matches_played=4), Row(home_team='Sunderland AFC', away_team='Birmingham City FC', avg_home_team_wins=0.0, total_matches_played=4), Row(home_team='Chelsea FC', away_team='West Bromwich Albion FC', avg_home_team_wins=1.0, total_matches_played=4), Row(home_team='Tottenham Hotspur FC', away_team='Wolverhampton Wanderers FC', avg_home_team_wins=1.0, total_matches_played=4), Row(home_team='Wigan Athletic FC', away_team='Chelsea FC', avg_home_team_wins=0.0, total_matches_played=4), Row(home_team='West Ham United FC', away_team='Bolton Wanderers FC', avg_home_team_wins=0.0, total_matches_played=4), Row(home_team='Blackpool FC', away_team='West Bromwich Albion FC', avg_home_team_wins=1.0, total_matches_played=4)]
```

```sql

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
            
```

```response from databricks
[Row(home_team='Manchester United FC', away_team='Liverpool FC', avg_home_team_wins=1.0, total_matches_played=1), Row(home_team='Aston Villa FC', away_team='West Ham United FC', avg_home_team_wins=1.0, total_matches_played=1), Row(home_team='Liverpool FC', away_team='Arsenal FC', avg_home_team_wins=0.0, total_matches_played=1), Row(home_team='Aston Villa FC', away_team='Everton FC', avg_home_team_wins=1.0, total_matches_played=1), Row(home_team='Everton FC', away_team='Wolverhampton Wanderers FC', avg_home_team_wins=0.0, total_matches_played=1), Row(home_team='Tottenham Hotspur FC', away_team='Aston Villa FC', avg_home_team_wins=1.0, total_matches_played=1)]
```

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
            )

            SELECT team, opponent, avg_goals_scored, total_matches_played
            FROM team_matches
            ORDER BY total_matches_played DESC
            LIMIT 10;
            
```

```response from databricks
[Row(team='Liverpool FC', opponent='Arsenal FC', avg_goals_scored=1.8, total_matches_played=5), Row(team='Everton FC', opponent='Wolverhampton Wanderers FC', avg_goals_scored=1.8, total_matches_played=5), Row(team='Aston Villa FC', opponent='West Ham United FC', avg_goals_scored=1.8, total_matches_played=5), Row(team='Aston Villa FC', opponent='Everton FC', avg_goals_scored=1.5, total_matches_played=4), Row(team='Tottenham Hotspur FC', opponent='Aston Villa FC', avg_goals_scored=2.5, total_matches_played=4), Row(team='Manchester United FC', opponent='Liverpool FC', avg_goals_scored=2.0, total_matches_played=4), Row(team='Chelsea FC', opponent='West Bromwich Albion FC', avg_goals_scored=6.0, total_matches_played=3), Row(team='Sunderland AFC', opponent='Birmingham City FC', avg_goals_scored=2.0, total_matches_played=3), Row(team='Stoke City FC', opponent='Tottenham Hotspur FC', avg_goals_scored=1.0, total_matches_played=3), Row(team='West Ham United FC', opponent='Bolton Wanderers FC', avg_goals_scored=1.0, total_matches_played=3)]
```

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
            )

            SELECT team, opponent, avg_goals_scored, total_matches_played
            FROM team_matches
            ORDER BY total_matches_played DESC
            LIMIT 10;
            
```

```response from databricks
[Row(team='Aston Villa FC', opponent='West Ham United FC', avg_goals_scored=1.7142857142857142, total_matches_played=7), Row(team='Liverpool FC', opponent='Arsenal FC', avg_goals_scored=1.8571428571428572, total_matches_played=7), Row(team='Everton FC', opponent='Wolverhampton Wanderers FC', avg_goals_scored=1.8571428571428572, total_matches_played=7), Row(team='Tottenham Hotspur FC', opponent='Aston Villa FC', avg_goals_scored=2.5, total_matches_played=6), Row(team='Manchester United FC', opponent='Liverpool FC', avg_goals_scored=2.0, total_matches_played=6), Row(team='Aston Villa FC', opponent='Everton FC', avg_goals_scored=1.5, total_matches_played=6), Row(team='Chelsea FC', opponent='West Bromwich Albion FC', avg_goals_scored=6.0, total_matches_played=4), Row(team='Sunderland AFC', opponent='Birmingham City FC', avg_goals_scored=2.0, total_matches_played=4), Row(team='West Bromwich Albion FC', opponent='Sunderland AFC', avg_goals_scored=1.0, total_matches_played=4), Row(team='West Ham United FC', opponent='Bolton Wanderers FC', avg_goals_scored=1.0, total_matches_played=4)]
```

