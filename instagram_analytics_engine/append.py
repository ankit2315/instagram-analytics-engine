with open('models/marts/schema.yml', 'a', encoding='utf-8') as f:
    f.write('''
  - name: agg_instagram_overview
    description: "Executive overview mart containing lifetime performance totals. One row table."
    columns:
      - name: total_posts
        description: "Total lifetime posts."
''')
