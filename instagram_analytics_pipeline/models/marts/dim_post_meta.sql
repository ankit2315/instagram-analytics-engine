with posts as (
    select * from {{ ref('stg_instagram_posts') }}
)

select
    post_id,
    post_type,
    caption,
    post_url,
    duration_seconds,

    case
        when duration_seconds < 15 then 'short'
        when duration_seconds between 15 and 30 then 'medium'
        when duration_seconds > 30 then 'long'
        else 'unknown'
    end as video_length_bucket

from posts
