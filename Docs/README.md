# AFC N.D.A.I — Documentation

This folder contains the project documentation required for the AFC tender.

**Stack (as implemented in this repository)**
- PostgreSQL 15 (data storage + SQL views for analytics)
- FastAPI (REST API to collect campaign feedback + sentiment analysis)
- Python ETL container (batch ingestion for sales CSV + optional batch feedback ingestion)
- Metabase (dashboards)
- Docker Compose (orchestration)

**Main user stories**
- Centralize global sales data (batch ingestion of CSV exports).
- Collect marketing campaign feedback via REST API.
- Apply sentiment analysis on feedback comments.
- Provide dashboards for sales monitoring and feedback sentiment insights.

Start here: `03_runbook.md`.
