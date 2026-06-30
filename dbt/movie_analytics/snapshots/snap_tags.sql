{% snapshot snap_tags %}

{{
    config(
        target_schema = 'snapshots',
        unique_key = ['user_id', 'movie_id', 'tag'],
        strategy = 'timestamp',
        updated_at = 'tag_timestamp',
        invalidate_hard_deletes = True
    )
}}

SELECT

    -- Generate a stable surrogate key for each unique user-movie-tag combination
    {{ dbt_utils.generate_surrogate_key(['user_id', 'movie_id', 'tag']) }} AS row_key,

    user_id,
    movie_id,
    tag,

    -- Normalize timestamp for consistent snapshot tracking
    CAST(tag_timestamp AS TIMESTAMP_NTZ) AS tag_timestamp

FROM {{ ref('src_tags') }}



{% endsnapshot %}