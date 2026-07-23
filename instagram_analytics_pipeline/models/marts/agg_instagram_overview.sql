with performance as (
    select * from {{ ref('fct_instagram_post_performance') }}
)

select
    count(post_id) as total_posts,
    sum(views) as total_views,
    sum(reach) as total_reach,
    sum(total_engagements) as total_engagements,
    
    round((sum(case when reach is not null then cast(total_engagements as {{ dbt.type_float() }}) else 0 end) / nullif(sum(reach), 0)) * 100, 2) as overall_engagement_rate

from performance
