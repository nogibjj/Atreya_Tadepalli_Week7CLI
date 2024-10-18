```sql

            SELECT baseball.team, 
            avg(mlb.Winning) AS winning_pct,
            avg(mlb.Salary) avg_payroll 
            FROM ids706_data_engineering.default.baseball AS baseball
            RIGHT JOIN ids706_data_engineering.default.mlb_baseball_1 AS mlb
            ON baseball.team = mlb.Team
            GROUP BY baseball.team
            ORDER BY avg_payroll DESC;
            
```

```response from databricks
[Row(team='New York Yankees', winning_pct=52.0, avg_payroll=228995945.0), Row(team=None, winning_pct=52.0, avg_payroll=179234079.5), Row(team='Philadelphia Phillies', winning_pct=45.0, avg_payroll=159578214.0), Row(team='Boston Red Sox', winning_pct=59.0, avg_payroll=158967286.0), Row(team='Detroit Tigers', winning_pct=57.0, avg_payroll=149046844.0), Row(team='San Francisco Giants', winning_pct=46.0, avg_payroll=142180333.0), Row(team='Texas Rangers', winning_pct=55.0, avg_payroll=127197575.0), Row(team='Chicago White Sox', winning_pct=38.0, avg_payroll=124065277.0), Row(team='Toronto Blue Jays', winning_pct=45.0, avg_payroll=118244039.0), Row(team='St. Louis Cardinals', winning_pct=59.0, avg_payroll=116702085.0), Row(team='Washington Nationals', winning_pct=53.0, avg_payroll=112431770.0), Row(team='Cincinnati Reds', winning_pct=55.0, avg_payroll=110565728.0), Row(team='Chicago Cubs', winning_pct=40.0, avg_payroll=104150726.0), Row(team='Baltimore Orioles', winning_pct=52.0, avg_payroll=91793333.0), Row(team='Milwaukee Brewers', winning_pct=45.0, avg_payroll=91003366.0), Row(team='Arizona Diamondbacks', winning_pct=50.0, avg_payroll=90158500.0), Row(team='Atlanta Braves', winning_pct=59.0, avg_payroll=89288193.0), Row(team='New York Mets', winning_pct=45.0, avg_payroll=88877033.0), Row(team='Seattle Mariners', winning_pct=43.0, avg_payroll=84295952.0), Row(team='Cleveland Indians', winning_pct=56.0, avg_payroll=82517300.0), Row(team='Kansas City Royals', winning_pct=53.0, avg_payroll=80491725.0), Row(team='Minnesota Twins', winning_pct=40.0, avg_payroll=75562500.0), Row(team='Colorado Rockies', winning_pct=45.0, avg_payroll=75449071.0), Row(team='San Diego Padres', winning_pct=46.0, avg_payroll=71689900.0), Row(team='Oakland Athletics', winning_pct=59.0, avg_payroll=68577000.0), Row(team='Pittsburgh Pirates', winning_pct=58.0, avg_payroll=66289524.0), Row(team='Tampa Bay Rays', winning_pct=56.0, avg_payroll=57030272.0), Row(team='Miami Marlins', winning_pct=38.0, avg_payroll=39621900.0), Row(team='Houston Astros', winning_pct=31.0, avg_payroll=24328538.0)]
```

