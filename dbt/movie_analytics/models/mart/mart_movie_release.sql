{{
    config(
        materialized = 'table'
    )
}}

WITH fct_ratings AS (

    -- Load the ratings fact table
    SELECT *
    FROM {{ ref('fct_ratings') }}

),

seed_dates AS (

    -- Load seeded movie release dates used to enrich the fact table
    SELECT *
    FROM {{ ref('seed_movie_release_dates') }}

)

SELECT

    -- Retain all columns from the ratings fact table
    f.*,

    -- Flag whether release date information is available for the movie
    CASE
        WHEN d.release_date IS NULL THEN 'UNKNOWN'
        ELSE 'KNOWN'
    END AS release_info_available

FROM fct_ratings f

-- Enrich ratings with release date availability using the movie identifier
LEFT JOIN seed_dates d
    ON f.movie_id = d.movie_id