WITH raw_links AS (

    -- Load external movie identifier mappings from the raw source table
    SELECT *
    FROM PROJECT_DB.RAW.RAW_LINKS

)

SELECT

    -- Rename columns to follow snake_case naming convention
    movieId AS movie_id,

    -- IMDb identifier for the movie
    imdbId AS imdb_id,

    -- TMDb identifier for the movie
    tmdbId AS tmdb_id

FROM raw_links