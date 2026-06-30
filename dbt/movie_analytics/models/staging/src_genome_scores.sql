WITH raw_genome_scores AS (

    -- Load genome relevance scores from the raw source table
    SELECT *
    FROM PROJECT_DB.RAW.RAW_GENOME_SCORES

)

SELECT

    -- Rename columns to follow snake_case naming convention
    movieId AS movie_id,
    tagId AS tag_id,

    -- Relevance score indicating how strongly a genome tag is associated with a movie
    relevance

FROM raw_genome_scores