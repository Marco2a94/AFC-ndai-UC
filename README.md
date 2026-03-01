# AFC -- Nugget Data & AI Initiative (N.D.A.I)

![CI](https://github.com/Marco2a94/AFC-ndai-UC/actions/workflows/ci.yml/badge.svg)

------------------------------------------------------------------------

## Project Overview

The Nugget Data & AI Initiative (N.D.A.I) is a data platform developed
for **AFC (Armoric Fried Chicken)** to centralize global sales data and
analyze customer feedback from marketing campaigns.

The solution integrates:

-   Batch ETL processing for sales ingestion
-   A REST API for real-time feedback collection
-   NLP-based sentiment analysis
-   Interactive business dashboards (Metabase)
-   Automated testing and CI pipeline

The platform is fully containerized using Docker and designed to be
reproducible, scalable, and cloud-ready.

------------------------------------------------------------------------

## Architecture Overview

1.  PostgreSQL database (raw & curated layers)
2.  FastAPI REST API (streaming feedback ingestion)
3.  Batch ETL service (sales ingestion & validation)
4.  Sentiment analysis module (TextBlob)
5.  Metabase dashboards (persisted via Docker volume)
6.  GitHub Actions CI pipeline

All services are orchestrated using Docker Compose.

------------------------------------------------------------------------

## Setup & Installation

### Prerequisites

-   Docker
-   Docker Compose
-   Git

### Clone the repository

``` bash
git clone https://github.com/Marco2a94/AFC-ndai-UC.git
cd AFC-ndai-UC
```

### Environment Variables

Create a `.env` file at the root:

``` env
POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password
POSTGRES_DB=afc_db
```

### Build & Start Services

``` bash
docker-compose up --build -d
```

Services available:

-   API → http://localhost:8000
-   Swagger → http://localhost:8000/docs
-   Metabase → http://localhost:3000

------------------------------------------------------------------------

# First Installation -- Restore Dashboards

Dashboards are stored in `metabase_backup.tar.gz`.

⚠️ IMPORTANT: The restore must be done BEFORE using Metabase for the
first time.

## Step 1 -- Start services

``` bash
docker-compose up -d
```

## Step 2 -- Immediately stop Metabase

``` bash
docker stop afc_metabase
```

## Step 3 -- Restore the Metabase volume backup

``` bash
docker run --rm -v afc-ndai-uc_metabase_data:/volume -v ${PWD}:/backup alpine sh -c "tar xzf /backup/metabase_backup.tar.gz -C /volume"
```

## Step 4 -- Restart Metabase

``` bash
docker start afc_metabase
```

Now access:

http://localhost:3000

Your dashboards will be available automatically.

------------------------------------------------------------------------

# Data Ingestion

## Sales Data (Batch ETL)

``` bash
docker exec -it afc_etl python /app/etl/ingest_sales.py /app/data/raw/sales_data.csv
```

ETL Features:

-   Schema validation
-   Missing column detection
-   Type validation
-   Duplicate prevention (SQL constraint)
-   Raw-to-curated transformation

------------------------------------------------------------------------

## Feedback (REST API -- Streaming)

``` bash
docker exec -it afc_etl python /app/etl/ingest_feedback.py /app/data/raw/feedback_data.json
```

POST `/feedback`

Example:

``` json
{
  "campaign_id": "CAMP123",
  "username": "user1",
  "comment": "Great campaign!",
  "feedback_date": "2025-01-01"
}
```

Features:

-   Real-time ingestion
-   Automatic sentiment analysis
-   PostgreSQL persistence

------------------------------------------------------------------------

# Running Tests

``` bash
docker-compose run --remove-orphans test
```

The CI pipeline runs automatically on:

-   Push
-   Pull requests
-   Manual workflow dispatch

------------------------------------------------------------------------

# Design Choices

-   PostgreSQL for relational integrity and analytics
-   FastAPI for performance & OpenAPI documentation
-   TextBlob for lightweight sentiment scoring
-   Raw-to-curated ETL pattern
-   Docker for reproducibility
-   GitHub Actions for CI

------------------------------------------------------------------------

# Limitations

-   No authentication layer
-   Basic sentiment model
-   No connection pooling
-   Limited test coverage

------------------------------------------------------------------------

# Future Improvements

-   Transformer-based NLP models
-   API authentication & rate limiting
-   Cloud-native deployment (Azure/AWS)
-   Infrastructure as Code (Terraform)
-   Monitoring & observability stack

------------------------------------------------------------------------

## Conclusion

The AFC N.D.A.I platform demonstrates an end-to-end data engineering
workflow combining batch processing, streaming ingestion, NLP,
analytics, containerization, and CI.

The architecture is modular, reproducible, and aligned with industrial
best practices.
