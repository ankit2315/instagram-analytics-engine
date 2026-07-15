import duckdb
con = duckdb.connect('dev.duckdb')
res = con.execute('''
    SELECT 
        video_length_bucket, 
        post_count, 
        total_views, 
        avg_engagement_rate 
    FROM agg_instagram_video_length_performance
    ORDER BY avg_engagement_rate DESC
''').fetchall()

print("| Video Length Bucket | Post Count | Total Views | Avg Engagement Rate (%) |")
print("|---|---|---|---|")
for row in res:
    print(f"| {row[0]} | {row[1]} | {row[2]:,} | {row[3]} |")
