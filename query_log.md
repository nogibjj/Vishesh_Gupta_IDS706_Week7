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

