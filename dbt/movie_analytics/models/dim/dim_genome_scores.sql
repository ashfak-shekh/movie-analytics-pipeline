WITH src_tags AS (

    SELECT *
    FROM {{ ref("src_genome_tags") }}

)

SELECT
    tag_id,

    -- Standardize tag names for consistent reporting and analysis
    INITCAP(TRIM(tag)) AS tag_name

FROM src_tags