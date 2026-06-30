WITH src_movies AS (

    SELECT *
    FROM {{ ref('src_movies') }}

)

SELECT
    movie_id,

    -- Standardize movie titles and convert genres into an array for easier analysis
    INITCAP(TRIM(title)) AS movie_title,

    SPLIT(genres, '|') AS genre_array,

    genres

FROM src_movies