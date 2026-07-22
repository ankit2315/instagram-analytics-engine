with performance as (
    select * from {{ ref('fct_instagram_post_performance') }}
),

post_meta as (
    select * from {{ ref('dim_post_meta') }}
),

joined as (
    select
        performance.post_id,
        performance.published_at,
        
        post_meta.post_type,
        post_meta.caption,
        post_meta.post_url,
        post_meta.video_length_bucket,

        performance.views,
        performance.reach,
        performance.likes,
        performance.comments,
        performance.shares,
        performance.saves,
        performance.total_engagements,
        
        performance.save_rate,
        performance.share_rate,
        performance.engagement_rate,
        
        case when performance.reach is null then true else false end as is_reach_missing

    from performance
    inner join post_meta
        on performance.post_id = post_meta.post_id
)

select
    *,
    row_number() over (order by views desc) as global_views_rank,
    row_number() over (order by engagement_rate desc nulls last) as global_engagement_rate_rank

from joined
order by published_at desc
