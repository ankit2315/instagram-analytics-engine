import duckdb
import os

# Create the exports directory if it doesn't exist
os.makedirs('exports', exist_ok=True)

# Connect to the DuckDB database
con = duckdb.connect('dev.duckdb')

# Export the 3 final marts to CSV
con.execute("COPY (SELECT * FROM agg_instagram_video_length_performance) TO 'exports/agg_instagram_video_length_performance.csv' (HEADER, DELIMITER ',')")
con.execute("COPY (SELECT * FROM agg_instagram_weekly_performance) TO 'exports/agg_instagram_weekly_performance.csv' (HEADER, DELIMITER ',')")
con.execute("COPY (SELECT * FROM rpt_instagram_post_performance) TO 'exports/rpt_instagram_post_performance.csv' (HEADER, DELIMITER ',')")

print("Successfully exported all 3 marts to the 'exports' folder!")
