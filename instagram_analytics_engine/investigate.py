import duckdb
import pandas as pd

con = duckdb.connect('dev.duckdb')

print('--- 2026 Weekly Performance ---')
query1 = """
SELECT 
    week_start_date, 
    post_count, 
    total_reach, 
    total_engagements, 
    weekly_engagement_rate 
FROM agg_instagram_weekly_performance 
WHERE extract('year' FROM week_start_date) = 2026
ORDER BY week_start_date
"""
print(con.execute(query1).df().to_string())

print('\n--- 2026 Individual Posts ---')
query2 = """
SELECT 
    published_at, 
    reach, 
    total_engagements, 
    engagement_rate 
FROM rpt_instagram_post_performance 
WHERE extract('year' FROM published_at) = 2026
ORDER BY published_at
"""
print(con.execute(query2).df().to_string())
