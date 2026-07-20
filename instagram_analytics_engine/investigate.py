import duckdb
import pandas as pd

con = duckdb.connect('dev.duckdb')

query = """
SELECT 
    reach, 
    total_engagements, 
    engagement_rate 
FROM rpt_instagram_post_performance 
WHERE date_trunc('week', published_at) = '2024-10-21 00:00:00'
"""
print(con.execute(query).df())
