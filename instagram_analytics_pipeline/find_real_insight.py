import duckdb

con = duckdb.connect('dev.duckdb')

print("--- 1. Pareto Principle (Viral vs Base) ---")
q1 = """
WITH totals AS (
    SELECT 
        SUM(views) as total_views, 
        SUM(reach) as total_reach,
        COUNT(*) as total_posts
    FROM rpt_instagram_post_performance
),
top_posts AS (
    SELECT 
        SUM(views) as top_views,
        SUM(reach) as top_reach,
        COUNT(*) as top_count
    FROM (
        SELECT views, reach
        FROM rpt_instagram_post_performance
        ORDER BY views DESC
        LIMIT 8 -- Top 10% of 79 posts
    )
)
SELECT 
    t.total_views,
    tp.top_views,
    (tp.top_views * 100.0 / t.total_views) as pct_total_views,
    (tp.top_count * 100.0 / t.total_posts) as pct_total_posts
FROM totals t, top_posts tp
"""
print(con.execute(q1).df().to_string())

print("\n--- 2. Median vs Average Views (Skewness) ---")
q2 = """
SELECT 
    AVG(views) as avg_views,
    median(views) as median_views,
    AVG(views) / median(views) as skew_ratio
FROM rpt_instagram_post_performance
"""
print(con.execute(q2).df().to_string())

print("\n--- 3. Video Length Reliability ---")
q3 = """
SELECT 
    video_length_bucket,
    COUNT(*) as post_count,
    median(views) as median_views,
    AVG(views) as avg_views,
    median(engagement_rate) as median_eng_rate
FROM rpt_instagram_post_performance
GROUP BY 1
HAVING COUNT(*) >= 10
ORDER BY median_views DESC
"""
print(con.execute(q3).df().to_string())
