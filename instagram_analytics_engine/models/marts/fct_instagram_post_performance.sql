with posts as (
    select * from {{ ref('stg_instagram_posts') }}
)

select
    post_id,
    published_at,

    views,
    reach,
    likes,
    comments,
    shares,
    saves,
    follows,

    coalesce(likes, 0)
        + coalesce(comments, 0)
        + coalesce(shares, 0)
        + coalesce(saves, 0) as total_engagements,

    round((cast(likes as {{ dbt.type_float() }}) / nullif(reach, 0)) * 100, 2) as like_rate,
    round((cast(comments as {{ dbt.type_float() }}) / nullif(reach, 0)) * 100, 2) as comment_rate,
    round((cast(shares as {{ dbt.type_float() }}) / nullif(reach, 0)) * 100, 2) as share_rate,
    round((cast(saves as {{ dbt.type_float() }}) / nullif(reach, 0)) * 100, 2) as save_rate,

    round((
        cast(
            coalesce(likes, 0)
            + coalesce(comments, 0)
            + coalesce(shares, 0)
            + coalesce(saves, 0)
            as {{ dbt.type_float() }}
        ) / nullif(reach, 0)
    ) * 100, 2) as engagement_rate

from posts