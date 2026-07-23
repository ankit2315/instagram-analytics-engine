with combined as (
    select * from {{ ref('Oct-03-2024_Apr-03-2025_2473370336446386') }}
    union all
    select * from {{ ref('Apr-04-2025_Feb-12-2026_1872339153476004') }}
)

select
    -- identifiers
    "Post ID"                            as post_id,

    -- time
    strptime("Publish time", '%m/%d/%Y %H:%M') as published_at,

    -- content info
    lower("Post type")                   as post_type,
    "Description"                        as caption,
    "Permalink"                          as post_url,

    -- metrics
    cast("Duration (sec)" as float)      as duration_seconds,
    cast("Views" as int)                 as views,
    cast("Reach" as int)                 as reach,
    cast("Likes" as int)                 as likes,
    cast("Comments" as int)              as comments,
    cast("Shares" as int)                as shares,
    cast("Saves" as int)                 as saves,
    cast("Follows" as int)               as follows

from combined
where "Post ID" is not null
