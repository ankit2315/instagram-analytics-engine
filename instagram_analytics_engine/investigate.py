import duckdb

con = duckdb.connect('dev.duckdb')

query = """
SELECT 
    date_trunc('month', published_at) as month, 
    count(*) as post_count 
FROM rpt_instagram_post_performance 
WHERE extract('year' FROM published_at) = 2025
GROUP BY 1 
ORDER BY 1
"""
print(con.execute(query).df().to_string())
