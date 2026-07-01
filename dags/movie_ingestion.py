from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator


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
    tags=["snowflake", "ingestion", "movie_analytics"],
) as dag:

    load_movies = SQLExecuteQueryOperator(
        task_id="load_movies",
        conn_id="snowflake_conn",
        sql="""
        COPY INTO PROJECT_DB.RAW.RAW_MOVIES
        FROM @NETFLIX_S3_STAGE/Netflix_Dataset/movies.csv
        FILE_FORMAT = (
            TYPE = CSV
            FIELD_OPTIONALLY_ENCLOSED_BY='"'
            SKIP_HEADER=1
        );
        """,
    )

    load_ratings = SQLExecuteQueryOperator(
        task_id="load_ratings",
        conn_id="snowflake_conn",
        sql="""
        COPY INTO PROJECT_DB.RAW.RAW_RATINGS
        FROM @NETFLIX_S3_STAGE/Netflix_Dataset/ratings.csv
        FILE_FORMAT = (
            TYPE = CSV
            FIELD_OPTIONALLY_ENCLOSED_BY='"'
            SKIP_HEADER=1
        );
        """,
    )

    load_tags = SQLExecuteQueryOperator(
        task_id="load_tags",
        conn_id="snowflake_conn",
        sql="""
        COPY INTO PROJECT_DB.RAW.RAW_TAGS
        FROM @NETFLIX_S3_STAGE/Netflix_Dataset/tags.csv
        FILE_FORMAT = (
            TYPE = CSV
            FIELD_OPTIONALLY_ENCLOSED_BY='"'
            SKIP_HEADER=1
        )
        ON_ERROR='CONTINUE';
        """,
    )

    load_links = SQLExecuteQueryOperator(
        task_id="load_links",
        conn_id="snowflake_conn",
        sql="""
        COPY INTO PROJECT_DB.RAW.RAW_LINKS
        FROM @NETFLIX_S3_STAGE/Netflix_Dataset/links.csv
        FILE_FORMAT = (
            TYPE = CSV
            FIELD_OPTIONALLY_ENCLOSED_BY='"'
            SKIP_HEADER=1
        );
        """,
    )

    load_genome_scores = SQLExecuteQueryOperator(
        task_id="load_genome_scores",
        conn_id="snowflake_conn",
        sql="""
        COPY INTO PROJECT_DB.RAW.RAW_GENOME_SCORES
        FROM @NETFLIX_S3_STAGE/Netflix_Dataset/genome_scores.csv
        FILE_FORMAT = (
            TYPE = CSV
            FIELD_OPTIONALLY_ENCLOSED_BY='"'
            SKIP_HEADER=1
        );
        """,
    )

    load_genome_tags = SQLExecuteQueryOperator(
        task_id="load_genome_tags",
        conn_id="snowflake_conn",
        sql="""
        COPY INTO PROJECT_DB.RAW.RAW_GENOME_TAGS
        FROM @NETFLIX_S3_STAGE/Netflix_Dataset/genome_tags.csv
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