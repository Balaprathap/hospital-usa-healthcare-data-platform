# 🏥 Hospital360 USA Healthcare Data Platform

A production-style **end-to-end Healthcare Data Engineering Platform** built using **Apache Kafka, Apache Spark Structured Streaming, PostgreSQL, Docker, and Power BI**.

The platform ingests hospital data in real time, processes it using the **Medallion Architecture (Bronze → Silver → Gold)**, stores curated business data in PostgreSQL, and provides analytics-ready datasets for business intelligence dashboards.

---

# 📌 Project Overview

This project demonstrates a modern Data Engineering pipeline that simulates how healthcare organizations ingest, process, and analyze hospital quality data.

The platform includes:

- Real-time data ingestion
- Distributed stream processing
- Medallion Architecture
- Data Lake using Parquet
- PostgreSQL Data Warehouse
- Business KPI generation
- Dockerized infrastructure
- Power BI reporting

---

# 🏗️ Architecture

```text
                 CSV Hospital Dataset
                          │
                          ▼
              Python Kafka Producer
                          │
                          ▼
                  Apache Kafka Topic
                          │
                          ▼
         Spark Structured Streaming
                          │
          ┌───────────────┴───────────────┐
          ▼                               ▼
      Bronze Layer                 Checkpoints
     (Raw JSON Parquet)
          │
          ▼
      Silver Layer
 (Structured Hospital Data)
          │
          ▼
       Gold Layer
(State-Level Business KPIs)
          │
          ▼
   PostgreSQL Data Warehouse
          │
          ▼
      Power BI Dashboard
```

---

# 🚀 Technologies Used

| Category | Technologies |
|----------|--------------|
| Programming | Python |
| Streaming | Apache Kafka |
| Processing | Apache Spark 3.5 |
| Data Lake | Parquet |
| Database | PostgreSQL 16 |
| Containerization | Docker |
| Visualization | Power BI |
| Version Control | Git & GitHub |

---

# 📂 Project Structure

```text
hospital360-usa-healthcare-data-platform
│
├── bronze/
├── silver/
├── gold/
├── checkpoints/
│
├── kafka_app/
│   ├── producer.py
│   └── consumer.py
│
├── spark/
│   ├── test_spark.py
│   ├── stream_from_kafka.py
│   ├── bronze_stream.py
│   ├── silver_batch.py
│   ├── gold_batch.py
│   └── load_gold_to_postgres.py
│
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# 📊 Medallion Architecture

## Bronze Layer

Purpose:

- Stores raw streaming data
- No transformations
- Immutable raw records
- Stored in Parquet format

Input

```
Kafka JSON
```

Output

```
bronze/
```

---

## Silver Layer

Purpose

- Parse JSON
- Clean data
- Remove duplicates
- Standardize schema

Columns include

- Facility ID
- Hospital Name
- Address
- State
- Ownership
- Hospital Type
- Emergency Services
- Overall Rating

Output

```
silver/
```

---

## Gold Layer

Business-ready aggregated datasets.

Example KPIs

- Total hospitals by state
- Average hospital rating
- Healthcare quality metrics

Output

```
gold/state_kpis
```

---

# 🗄 PostgreSQL Warehouse

The Gold layer is loaded into PostgreSQL for reporting.

Current table

```
gold_state_kpis
```

Columns

| Column | Description |
|---------|-------------|
| state | State Code |
| total_hospitals | Total Hospitals |
| avg_hospital_rating | Average Rating |

---

# 📈 Sample Gold Output

| State | Hospitals | Avg Rating |
|--------|-----------|------------|
| TX | 468 | 3.38 |
| CA | 378 | 3.10 |
| FL | 221 | 3.07 |
| NY | 191 | 2.77 |

---

# ⚙️ Pipeline Flow

```text
CSV Dataset
      │
      ▼
Kafka Producer
      │
      ▼
Kafka Topic
      │
      ▼
Spark Streaming
      │
      ▼
Bronze
      │
      ▼
Silver
      │
      ▼
Gold
      │
      ▼
PostgreSQL
      │
      ▼
Power BI
```

---

# ▶️ How to Run

## Clone Repository

```bash
git clone https://github.com/Balaprathap/hospital-usa-healthcare-data-platform.git

cd hospital-usa-healthcare-data-platform
```

---

## Start Infrastructure

```bash
docker compose up -d
```

---

## Create Kafka Topic

```bash
docker exec hospital360-kafka \
kafka-topics \
--create \
--topic hospital-data \
--bootstrap-server localhost:9092 \
--partitions 3 \
--replication-factor 1
```

---

## Run Producer

```bash
python -m kafka_app.producer
```

---

## Run Bronze Streaming

```bash
spark-submit spark/bronze_stream.py
```

---

## Run Silver

```bash
spark-submit spark/silver_batch.py
```

---

## Run Gold

```bash
spark-submit spark/gold_batch.py
```

---

## Load into PostgreSQL

```bash
spark-submit \
--packages org.postgresql:postgresql:42.7.3 \
spark/load_gold_to_postgres.py
```

---

# 📌 Business Use Cases

- Healthcare Quality Analysis
- Hospital Performance Reporting
- State-wise Healthcare Analytics
- Executive KPI Dashboards
- Real-time Hospital Data Processing

---

# 🎯 Key Features

✅ Real-time Streaming Pipeline

✅ Apache Kafka Integration

✅ Spark Structured Streaming

✅ Medallion Architecture

✅ Parquet Data Lake

✅ PostgreSQL Warehouse

✅ Dockerized Infrastructure

✅ Power BI Ready

---

# 🚀 Future Enhancements

- Apache Airflow Orchestration
- dbt Transformations
- Delta Lake
- Azure Data Lake Storage Gen2
- Azure Databricks
- Microsoft Fabric Integration
- Data Quality Framework
- Logging & Monitoring
- CI/CD with GitHub Actions
- Unit & Integration Testing

---

# 📷 Screenshots

> Add screenshots after completing the dashboard.

- Spark UI
- Kafka Streaming
- PostgreSQL Tables
- Power BI Dashboard
- Architecture Diagram

---

# 👨‍💻 Author

**Balaprathap**

Graduate Student – Computer & Information Sciences

Florida Atlantic University

GitHub: https://github.com/Balaprathap

LinkedIn: https://www.linkedin.com/in/balaprathap-chellakkannu/

---

