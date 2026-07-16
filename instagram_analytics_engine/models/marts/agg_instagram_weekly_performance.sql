with performance as (
    select * from {{ ref('fct_instagram_post_performance') }}
),

weekly_aggregated as (
    select
        -- date_trunc rounds the timestamp down to the Monday of that week
        date_trunc('week', published_at) as week_start_date,

        count(post_id) as post_count,
        count(reach) as posts_with_reach,

        sum(views) as total_views,
        sum(reach) as total_reach,
        sum(total_engagements) as total_engagements,
        sum(saves) as total_saves,
        sum(shares) as total_shares,
        sum(follows) as total_follows,

        -- Averages (Volume)
        round(avg(views), 2) as avg_views_per_post,
        round(avg(reach), 2) as avg_reach_per_post,
        
        -- True Weekly Rates
        round((sum(cast(saves as {{ dbt.type_float() }})) / nullif(sum(reach), 0)) * 100, 2) as weekly_save_rate,
        round((sum(cast(shares as {{ dbt.type_float() }})) / nullif(sum(reach), 0)) * 100, 2) as weekly_share_rate,
        round((sum(cast(total_engagements as {{ dbt.type_float() }})) / nullif(sum(reach), 0)) * 100, 2) as weekly_engagement_rate

    from performance
    group by date_trunc('week', published_at)
)

select *
from weekly_aggregated
ORDER BY week_start_date DESC
