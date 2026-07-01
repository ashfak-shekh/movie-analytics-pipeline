# 🎬 Movie Analytics Pipeline

An end-to-end Data Engineering project that builds a scalable movie analytics pipeline using **Apache Airflow**, **dbt**, **Snowflake**, **Docker**, and **Python**.

This project demonstrates a modern end-to-end ELT pipeline that ingests movie datasets from AWS S3 into Snowflake, performs scalable transformations using dbt, and orchestrates the complete workflow with Apache Airflow and Cosmos.

---

# 🚀 Tech Stack

- Apache Airflow 3.2.2
- dbt Core
- dbt-snowflake
- Snowflake
- Docker & Docker Compose
- Python
- SQL
- Cosmos (Airflow + dbt integration)

---

# 📂 Project Structure

```
movie-analytics-pipeline/
│
├── config/                  # Airflow configuration
├── dags/                    # Airflow DAGs
├── plugins/                 # Airflow plugins
│
├── dbt/
│   └── movie_analytics/
│       ├── analyses/
│       ├── macros/
│       ├── models/
│       │   ├── staging/
│       │   ├── dim/
│       │   ├── fct/
│       │   └── mart/
│       ├── snapshots/
│       ├── seeds/
│       ├── tests/
│       ├── dbt_project.yml
│       ├── packages.yml
│       └── package-lock.yml
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# 🏗️ Architecture

```
MovieLens Dataset
        │
        ▼
AWS S3 (Raw Data Landing Zone)
        │
        ▼
Airflow Ingestion DAG
        │
        ▼
Snowflake RAW Layer
        │
        ▼
Cosmos + dbt Build DAG
        │
        ▼
Staging Models
        │
        ▼
Dimension Models
        │
        ▼
Fact Models
        │
        ▼
Analytics-ready Mart Models

Apache Airflow, integrated with Cosmos, orchestrates the ingestion pipeline and dbt transformation workflow.

---

# 📊 Data Pipeline

1. Raw movie datasets are stored in AWS S3.
2. Airflow Ingestion DAG loads data into Snowflake RAW tables.
3. Cosmos triggers dbt transformations.
4. dbt builds staging, dimension, fact, and mart models.
5. dbt executes automated data quality tests.
6. Snapshots capture historical changes.
7. Analytics-ready tables are created in Snowflake.

---

# 📁 dbt Layers

### Staging

- Cleans raw source data
- Renames columns
- Standardizes data types

### Dimension

Contains descriptive business entities such as:

- Movies
- Users
- Genome Scores
- Movie Tags

### Fact

Contains transactional or measurable business data.

### Mart

Business-ready models optimized for reporting and analytics.

---

# ⚙️ Setup

## Clone Repository

```bash
git clone <repository-url>
cd movie-analytics-pipeline
```

## Start Docker

```bash
docker compose up -d
```

## Install dbt Dependencies

```bash
dbt deps
```

## Run dbt Models

```bash
dbt run
```

## Execute Tests

```bash
dbt test
```

## Generate Documentation

```bash
dbt docs generate
dbt docs serve
```

---

# ▶️ Run Airflow

Start the Airflow services:

```bash
docker compose up -d
```

Open Airflow UI:

```
http://localhost:8082
```

---

# 📈 Features

✔ End-to-End ELT Pipeline

✔ AWS S3 Data Landing Zone

✔ Snowflake Data Warehouse

✔ Apache Airflow Orchestration

✔ Cosmos Integration

✔ dbt Transformations

✔ Incremental Models

✔ SCD Type 2 Snapshots

✔ Generic & Custom dbt Tests

✔ dbt Documentation & Lineage

✔ Dockerized Deployment

✔ Modular SQL Models

---

# 🧪 Data Quality

dbt tests include:

- Unique
- Not Null
- Relationships
- Accepted Values

---

# 📚 Skills Demonstrated

- Data Engineering
- ETL / ELT
- Apache Airflow
- dbt
- Snowflake
- SQL
- Python
- Docker
- Data Modeling
- Data Warehouse Design

---

# 📌 Future Enhancements

- CI/CD using GitHub Actions
- Data Quality Monitoring
- Logging & Alerting
- Unit Testing
- dbt Exposures
- Production Deployment

---

# 👤 Author

**Ashfak Shekh**

### 🛠️ Technologies Used

- Apache Airflow
- Cosmos
- dbt Core
- Snowflake
- AWS S3
- Docker
- Python
- SQL
- Git
- GitHub

---

⭐ If you found this project useful, feel free to star the repository.