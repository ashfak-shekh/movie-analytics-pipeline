{{
    config(
        materialized = 'table'
    )
}}

WITH raw_tags AS (

    -- Load raw user-generated movie tags from the source table
    SELECT *
    FROM {{ source('movie', 'tags') }}

)

SELECT

    -- Rename columns to follow snake_case naming convention
    userId AS user_id,
    movieId AS movie_id,

    -- User-provided tag for the movie
    tag,

    -- Convert Unix timestamp into a readable timestamp format
    TO_TIMESTAMP_LTZ(timestamp) AS tag_timestamp

FROM raw_tags