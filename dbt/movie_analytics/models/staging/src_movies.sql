WITH raw_movies AS (

    -- Load raw movie data from the Netflix source table
    SELECT *
    FROM {{ source('movie', 'movies') }}

)

SELECT

    -- Rename columns to follow snake_case naming convention
    movieId AS movie_id,

    -- Movie title
    title,

    -- Genre(s) associated with the movie
    genres

FROM raw_movies