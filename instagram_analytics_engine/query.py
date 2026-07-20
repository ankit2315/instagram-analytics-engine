import duckdb
con = duckdb.connect('dev.duckdb')
res = con.execute('''
    SELECT 
        global_views_rank,
        caption, 
        views, 
        engagement_rate 
    FROM rpt_instagram_post_performance
    ORDER BY global_views_rank ASC
    LIMIT 3
''').fetchall()

print("| Rank | Caption (Preview) | Views | Engagement Rate (%) |")
print("|---|---|---|---|")
for row in res:
    caption = row[1].replace('\n', ' ') if row[1] else "No caption"
    # Truncate caption for display
    caption = caption[:40] + "..." if len(caption) > 40 else caption
    print(f"| {row[0]} | {caption} | {row[2]:,} | {row[3]} |")
