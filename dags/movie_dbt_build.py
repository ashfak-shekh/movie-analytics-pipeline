from datetime import datetime

from airflow.models.baseoperator import chain

from cosmos import (
    DbtDag,
    ProjectConfig,
    ProfileConfig,
    ExecutionConfig,
    RenderConfig,
)

from cosmos.profiles import SnowflakeUserPasswordProfileMapping


profile_config = ProfileConfig(
    profile_name="movie_analytics",
    target_name="dev",
    profile_mapping=SnowflakeUserPasswordProfileMapping(
        conn_id="snowflake_conn",
        profile_args={
                "database": "PROJECT_DB",
                "schema": "DEV",
                "warehouse": "COMPUTE_WH",
                "role": "DATA_ENGINEER_ROLE",
        },
    ),
)

dbt_dag = DbtDag(
    dag_id="movie_dbt_build",
    project_config=ProjectConfig(
        "/opt/airflow/dbt/movie_analytics",
    ),
    profile_config=profile_config,
    execution_config=ExecutionConfig(),
    render_config=RenderConfig(),
    schedule="@daily",
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=["dbt", "cosmos", "snowflake", "movie_analytics"],
)