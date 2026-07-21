with performance as (
    select * from {{ ref('fct_instagram_post_performance') }}
),

post_meta as (
    select * from {{ ref('dim_post_meta') }}
),

joined as (
    select
        post_meta.video_length_bucket,

        performance.views,
        performance.reach,
        performance.likes,
        performance.comments,
        performance.shares,
        performance.saves,
        performance.follows,
        performance.total_engagements,

        performance.like_rate,
        performance.comment_rate,
        performance.share_rate,
        performance.save_rate,
        performance.engagement_rate

    from performance
    inner join post_meta
        on performance.post_id = post_meta.post_id
)

select
    video_length_bucket,
    
    CASE
        WHEN video_length_bucket = 'short' THEN 1
        WHEN video_length_bucket = 'medium' THEN 2
        WHEN video_length_bucket = 'long' THEN 3
        ELSE 4
    END AS video_length_sort,

    count(*) as post_count,
    count(reach) as posts_with_reach,

    sum(views) as total_views,
    sum(reach) as total_reach,
    sum(total_engagements) as total_engagements,
    sum(saves) as total_saves,
    sum(shares) as total_shares,
    sum(follows) as total_follows,

    round(avg(views), 2) as avg_views_per_post,
    round(avg(reach), 2) as avg_reach_per_post,
    round(avg(total_engagements), 2) as avg_engagements_per_post,

    round(avg(like_rate), 2) as avg_like_rate,
    round(avg(comment_rate), 2) as avg_comment_rate,
    round(avg(share_rate), 2) as avg_share_rate,
    round(avg(save_rate), 2) as avg_save_rate,
    round(avg(engagement_rate), 2) as avg_engagement_rate

from joined
group by
    video_length_bucket
