import duckdb
con = duckdb.connect('dev.duckdb')
res = con.execute('''
    SELECT 
        week_start_date, 
        post_count, 
        total_views, 
        weekly_engagement_rate 
    FROM agg_instagram_weekly_performance
    ORDER BY week_start_date DESC
    LIMIT 10
''').fetchall()

print("| Week Start Date | Post Count | Total Views | Weekly Engagement Rate (%) |")
print("|---|---|---|---|")
for row in res:
    week_str = row[0].strftime('%Y-%m-%d') if row[0] else 'N/A'
    print(f"| {week_str} | {row[1]} | {row[2]:,} | {row[3]} |")
