from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator


from airflow.operators.trigger_dagrun import TriggerDagRunOperator

default_args = {
    "owner": "Ashfak",
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="movie_ingestion",
    description="Load Movielens CSV files into Snowflake RAW schema",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    default_args=default_args,
    tags=["snowflake", "ingestion", "Movielens"],
) as dag:

    load_movies = SnowflakeOperator(
        task_id="load_movies",
        snowflake_conn_id="snowflake_conn",
        sql="""
        COPY INTO PROJECT_DB.RAW.RAW_MOVIES
        FROM @netflixstage/movies.csv
        FILE_FORMAT = (
            TYPE = CSV
            FIELD_OPTIONALLY_ENCLOSED_BY='"'
            SKIP_HEADER=1
        );
        """,
    )

    load_ratings = SnowflakeOperator(
        task_id="load_ratings",
        snowflake_conn_id="snowflake_conn",
        sql="""
        COPY INTO PROJECT_DB.RAW.RAW_RATINGS
        FROM @netflixstage/ratings.csv
        FILE_FORMAT = (
            TYPE = CSV
            FIELD_OPTIONALLY_ENCLOSED_BY='"'
            SKIP_HEADER=1
        );
        """,
    )

    load_tags = SnowflakeOperator(
        task_id="load_tags",
        snowflake_conn_id="snowflake_conn",
        sql="""
        COPY INTO PROJECT_DB.RAW.RAW_TAGS
        FROM @netflixstage/tags.csv
        FILE_FORMAT = (
            TYPE = CSV
            FIELD_OPTIONALLY_ENCLOSED_BY='"'
            SKIP_HEADER=1
        )
        ON_ERROR='CONTINUE';
        """,
    )

    load_links = SnowflakeOperator(
        task_id="load_links",
        snowflake_conn_id="snowflake_conn",
        sql="""
        COPY INTO PROJECT_DB.RAW.RAW_LINKS
        FROM @netflixstage/links.csv
        FILE_FORMAT = (
            TYPE = CSV
            FIELD_OPTIONALLY_ENCLOSED_BY='"'
            SKIP_HEADER=1
        );
        """,
    )

    load_genome_scores = SnowflakeOperator(
        task_id="load_genome_scores",
        snowflake_conn_id="snowflake_conn",
        sql="""
        COPY INTO PROJECT_DB.RAW.RAW_GENOME_SCORES
        FROM @netflixstage/genome_scores.csv
        FILE_FORMAT = (
            TYPE = CSV
            FIELD_OPTIONALLY_ENCLOSED_BY='"'
            SKIP_HEADER=1
        );
        """,
    )

    load_genome_tags = SnowflakeOperator(
        task_id="load_genome_tags",
        snowflake_conn_id="snowflake_conn",
        sql="""
        COPY INTO PROJECT_DB.RAW.RAW_GENOME_TAGS
        FROM @netflixstage/genome_tags.csv
        FILE_FORMAT = (
            TYPE = CSV
            FIELD_OPTIONALLY_ENCLOSED_BY='"'
            SKIP_HEADER=1
        );
        """,
    )

    trigger_dbt = TriggerDagRunOperator(
        task_id="trigger_movie_dbt_build",
        trigger_dag_id="movie_dbt_build",
        wait_for_completion=False,
    )

    [
        load_movies,
        load_ratings,
        load_tags,
        load_links,
        load_genome_scores,
        load_genome_tags,
    ] >> trigger_dbt