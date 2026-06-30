WITH raw_genome_tags AS (

    -- Load genome tag reference data from the raw source table
    SELECT *
    FROM PROJECT_DB.RAW.RAW_GENOME_TAGS

)

SELECT

    -- Rename columns to follow snake_case naming convention
    tagId AS tag_id,

    -- Descriptive name of the genome tag
    tag

FROM raw_genome_tags