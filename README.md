# Project Overview

The Nugget Data & AI Initiative (N.D.A.I) is a data platform developed for AFC (Armoric Fried Chicken) to centralize global sales data and analyze customer feedback from marketing campaigns.

The solution combines batch data ingestion for sales, a REST API for real-time campaign feedback collection, sentiment analysis using NLP, and interactive dashboards for business insights.

The platform is fully containerized using Docker and designed to be reproducible, scalable, and cloud-ready.

## Setup & Installation

### Prerequisites

- Docker
- Docker Compose

### Clone the repository

git clone [https://github.com/Marco2a94/AFC-ndai-UC.git](https://github.com/Marco2a94/AFC-ndai-UC.git)
cd AFC-ndai-UC

### Environment variables

Create a `.env` file at the root of the project with the following variables:

POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password
POSTGRES_DB=afc_db

### Build and start all services

docker-compose down -v
docker-compose up --build

## Running the Project

Once the containers are running:

- API: http://localhost:8000
- Swagger Documentation: http://localhost:8000/docs
- Metabase Dashboard: http://localhost:3000

To stop the services:

docker-compose down

## Data Ingestion

### Sales Data (Batch ETL)

To ingest sales data:

docker exec -it afc_api python ingest_sales.py /path/to/file.csv

### Feedback (REST API)

Send feedback via POST request:

POST /feedback

Example JSON body:

{
  "campaign_id": "CAMP123",
  "username": "user1",
  "comment": "Great campaign!",
  "feedback_date": "2025-01-01"
}

## Architecture

The solution follows a layered data architecture:

1. PostgreSQL database (raw and curated layers)
2. FastAPI REST service for feedback ingestion
3. Batch ETL for sales data processing
4. Sentiment analysis module (TextBlob)
5. Metabase dashboards for analytics

All services are containerized and orchestrated using Docker Compose.

## Design Choices

- PostgreSQL was selected as relational database to support structured analytics.
- FastAPI was used for its automatic OpenAPI documentation and performance.
- TextBlob was chosen for lightweight sentiment analysis.
- A raw-to-curated pattern was implemented for sales ingestion.
- Docker ensures reproducibility and ease of deployment.

## Use of Generative AI

Generative AI was used to:
- Assist in code structuring and documentation drafting
- Improve data validation logic
- Suggest architectural best practices

All generated content was reviewed and adapted manually.

## Limitations & Future Improvements

- No connection pooling implemented in the API
- Basic sentiment analysis model (can be improved with advanced NLP models)
- No authentication mechanism on the REST API
- Limited automated testing

Future improvements could include:
- CI/CD pipeline
- Advanced machine learning models
- Cloud deployment