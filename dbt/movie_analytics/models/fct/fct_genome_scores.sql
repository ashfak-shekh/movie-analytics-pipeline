WITH src_scores AS (

    SELECT *
    FROM {{ ref("src_genome_scores") }}

)

SELECT
    movie_id,
    tag_id,
    ROUND(relevance, 4) AS relevance_score

FROM src_scores

-- Retain only meaningful tag associations
WHERE relevance > 0