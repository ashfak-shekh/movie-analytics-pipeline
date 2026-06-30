{{
    config(
        materialized = 'table'
    )
}}

WITH raw_ratings AS (

    -- Load raw movie ratings from the source table
    SELECT *
    FROM PROJECT_DB.RAW.RAW_RATINGS

)

SELECT

    -- Rename columns to follow snake_case naming convention
    userId AS user_id,
    movieId AS movie_id,

    -- Rating provided by the user for a movie
    rating,

    -- Convert Unix timestamp into a readable timestamp format
    TO_TIMESTAMP_LTZ(timestamp) AS rating_timestamp

FROM raw_ratings