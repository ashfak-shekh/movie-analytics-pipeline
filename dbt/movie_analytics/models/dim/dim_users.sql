WITH ratings AS (

    SELECT DISTINCT user_id
    FROM {{ ref("src_ratings") }}

),

tags AS (

    SELECT DISTINCT user_id
    FROM {{ ref("src_tags") }}

)

-- Combine users who have either rated or tagged a movie
SELECT DISTINCT user_id
FROM (

    SELECT *
    FROM ratings

    UNION

    SELECT *
    FROM tags

)