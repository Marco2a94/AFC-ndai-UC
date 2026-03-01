# AFC – Nugget Data & AI Initiative (N.D.A.I)

![CI](https://github.com/Marco2a94/AFC-ndai-UC/actions/workflows/ci.yml/badge.svg)

---

## Project Overview

The Nugget Data & AI Initiative (N.D.A.I) is a data platform developed for **AFC (Armoric Fried Chicken)** to centralize global sales data and analyze customer feedback from marketing campaigns.

The solution integrates:

- Batch ETL processing for sales ingestion
- A REST API for real-time feedback collection
- NLP-based sentiment analysis
- Interactive business dashboards
- Automated testing and CI pipeline

The platform is fully containerized using Docker and designed to be reproducible, scalable, and cloud-ready.

---

## Architecture Overview

The solution follows a layered architecture:

1. PostgreSQL database (raw & curated layers)
2. FastAPI REST service for streaming feedback ingestion
3. Batch ETL service for structured sales ingestion
4. Sentiment analysis module (TextBlob)
5. Metabase dashboards for analytics
6. GitHub Actions for automated testing (CI)

All services are containerized and orchestrated via Docker Compose.

---

## Setup & Installation

### Prerequisites

- Docker
- Docker Compose

### Clone the repository

```bash
git clone https://github.com/Marco2a94/AFC-ndai-UC.git
cd AFC-ndai-UC
```

### Environment variables

Create a `.env` file at the root of the project:

```env
POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password
POSTGRES_DB=afc_db
```

### Build and start services

```bash
docker-compose down -v
docker-compose up --build
```

---

## Running the Platform

Once containers are running:

- API: http://localhost:8000
- Swagger: http://localhost:8000/docs
- Metabase: http://localhost:3000

Stop services:

```bash
docker-compose down
```

---

## Data Ingestion

### Sales Data (Batch ETL)

```bash
docker exec -it afc_etl python /app/ingest_sales.py /app/data/raw/sales_data.csv
```

Features:

- Schema validation
- Missing column detection
- Data cleaning
- Duplicate prevention via SQL constraint
- Raw-to-curated transformation

---

### Feedback (REST API – Streaming)

POST `/feedback`

Example body:

```json
{
  "campaign_id": "CAMP123",
  "username": "user1",
  "comment": "Great campaign!",
  "feedback_date": "2025-01-01"
}
```

Features:

- Real-time ingestion
- Automatic sentiment analysis
- Data persistence in PostgreSQL

---

## Metabase Dashboard Restore

Dashboards are backed up as a volume archive.

To restore:

```bash
docker run --rm -v afc-ndai-uc_metabase_data:/volume -v ${PWD}:/backup alpine sh -c "cd /volume && tar xzf /backup/metabase_backup.tar.gz"
docker restart afc_metabase
```

---

## Testing & Continuous Integration

The project includes:

- Pytest-based unit tests
- API endpoint testing
- ETL validation testing
- GitHub Actions CI pipeline

To run tests locally:

```bash
docker-compose run --remove-orphans test
```

The CI pipeline automatically runs on:

- Push
- Pull requests
- Manual dispatch

---

## Design Choices

- PostgreSQL for relational analytics and integrity constraints
- FastAPI for performance and automatic OpenAPI documentation
- TextBlob for lightweight sentiment scoring
- Raw-to-curated data pattern for ETL industrialization
- Docker for reproducibility and environment consistency
- GitHub Actions for automated validation

---

## Use of Generative AI

Generative AI was used to:

- Accelerate code structuring
- Improve data validation patterns
- Identify architectural improvements
- Assist documentation drafting

All generated suggestions were reviewed, validated, and adapted manually.

---

## Limitations

- No connection pooling implemented
- Basic sentiment model (rule-based NLP)
- No authentication layer
- Limited test coverage (unit-focused)

---

## Future Improvements

- Advanced NLP models (transformer-based sentiment analysis)
- API authentication & rate limiting
- Cloud-native deployment (Azure / AWS)
- Infrastructure as Code (Terraform)
- Monitoring & observability stack

---

## Conclusion

The AFC N.D.A.I platform demonstrates a complete end-to-end data engineering workflow combining batch processing, streaming ingestion, sentiment analysis, dashboarding, containerization, and continuous integration.

The architecture is modular, reproducible, and designed with scalability and industrial best practices in mind.

