import duckdb

con = duckdb.connect('dev.duckdb')

print("--- Variance Analysis: Views vs Engagement Rate ---")
q1 = """
SELECT 
    STDDEV(views) / AVG(views) as views_cov,
    STDDEV(reach) / AVG(reach) as reach_cov,
    STDDEV(engagement_rate) / AVG(engagement_rate) as eng_rate_cov
FROM rpt_instagram_post_performance
WHERE engagement_rate IS NOT NULL
"""
print(con.execute(q1).df().to_string())

print("\n--- Summary Stats ---")
q2 = """
SELECT 
    MIN(engagement_rate) as min_er,
    percentile_cont(0.25) WITHIN GROUP (ORDER BY engagement_rate) as q1_er,
    median(engagement_rate) as median_er,
    percentile_cont(0.75) WITHIN GROUP (ORDER BY engagement_rate) as q3_er,
    MAX(engagement_rate) as max_er
FROM rpt_instagram_post_performance
WHERE engagement_rate IS NOT NULL
"""
print(con.execute(q2).df().to_string())
