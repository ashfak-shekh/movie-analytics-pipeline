# 🎬 Movie Analytics Pipeline

An end-to-end Data Engineering project that builds a scalable movie analytics pipeline using **Apache Airflow**, **dbt**, **Snowflake**, **Docker**, and **Python**.

This project demonstrates modern ELT practices by ingesting raw movie datasets into Snowflake, transforming them using dbt, and orchestrating the complete workflow with Apache Airflow.

---

# 🚀 Tech Stack

- Apache Airflow 2.10.5
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
Movie Dataset
      │
      ▼
Python ETL
      │
      ▼
Snowflake (Raw Tables)
      │
      ▼
dbt Staging Models
      │
      ▼
Dimension Models
      │
      ▼
Fact Models
      │
      ▼
Mart Models
      │
      ▼
Analytics & Reporting
```

Apache Airflow orchestrates the entire workflow from ingestion to dbt transformations.

---

# 📊 Data Pipeline

1. Load raw movie dataset.
2. Create Snowflake tables.
3. Ingest data into Snowflake.
4. Execute dbt models.
5. Run dbt tests.
6. Build dimensional models.
7. Create analytics-ready marts.

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

- End-to-End ELT Pipeline
- Snowflake Data Warehouse
- dbt Transformations
- Airflow Orchestration
- Dockerized Environment
- Modular SQL Models
- Automated Data Testing
- Scalable Data Architecture

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

- Incremental Models
- CI/CD using GitHub Actions
- Data Quality Monitoring
- Logging & Alerting
- Unit Testing
- SCD Type 2 Models
- dbt Exposures
- Production Deployment

---

# 👤 Author

**Ashfak Shekh**

- Data Engineer
- Snowflake
- dbt
- Apache Airflow
- Python
- SQL
- AWS

---

⭐ If you found this project useful, feel free to star the repository.