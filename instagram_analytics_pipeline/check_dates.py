import duckdb
con = duckdb.connect('dev.duckdb')
res = con.execute('SELECT min(published_at), max(published_at), count(*) FROM fct_instagram_post_performance').fetchone()
print(f"First post: {res[0]}")
print(f"Last post: {res[1]}")
print(f"Total posts: {res[2]}")
