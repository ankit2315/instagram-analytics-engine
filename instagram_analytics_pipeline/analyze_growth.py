import duckdb
import pandas as pd

con = duckdb.connect('dev.duckdb')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

print("--- 1. Day of Week Analysis ---")
q1 = """
SELECT 
    dayname(published_at) as publish_day,
    COUNT(*) as post_count,
    AVG(views) as avg_views,
    AVG(engagement_rate) as avg_eng_rate,
    AVG(share_rate) as avg_share_rate
FROM rpt_instagram_post_performance
GROUP BY 1
ORDER BY avg_views DESC
"""
print(con.execute(q1).df().to_string())

print("\n--- 2. Time of Day Analysis ---")
q2 = """
SELECT 
    extract('hour' from published_at) as publish_hour,
    COUNT(*) as post_count,
    AVG(views) as avg_views,
    AVG(engagement_rate) as avg_eng_rate
FROM rpt_instagram_post_performance
GROUP BY 1
HAVING count(*) >= 3
ORDER BY avg_views DESC
"""
print(con.execute(q2).df().to_string())

print("\n--- 3. Correlation: What drives Views? ---")
q3 = """
SELECT 
    corr(views, share_rate) as share_correlation,
    corr(views, save_rate) as save_correlation,
    corr(views, engagement_rate) as eng_correlation
FROM rpt_instagram_post_performance
"""
print(con.execute(q3).df().to_string())

print("\n--- 4. Top 5 Viral Posts Context ---")
q4 = """
SELECT 
    views,
    share_rate,
    video_length_bucket,
    left(replace(caption, '\n', ' '), 100) as short_caption
FROM rpt_instagram_post_performance
ORDER BY views DESC
LIMIT 5
"""
print(con.execute(q4).df().to_string())
