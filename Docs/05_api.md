# REST API (FastAPI)

FastAPI app: `api/main.py`

## Base URL
- Local: `http://localhost:8000`

## OpenAPI / Swagger
- `http://localhost:8000/docs`

## Endpoints

### `GET /health`
Returns:
```json
{ "status": "ok" }
```

### `POST /feedback`
Stores a feedback record and computes sentiment.

Request body (Pydantic model):
```json
{
  "campaign_id": "CAMP123",
  "username": "user1",
  "comment": "Great campaign!",
  "feedback_date": "2025-01-01"
}
```

Response (success):
```json
{
  "status": "feedback stored",
  "sentiment": "positive"
}
```

Response (error):
```json
{ "error": "<error message>" }
```

## Sentiment analysis logic

Sentiment is computed with **TextBlob polarity**:

- polarity > 0.1  → `positive`
- polarity < -0.1 → `negative`
- otherwise       → `neutral`

The computed label is stored in the `feedback.sentiment` column.

## Database connection

The API reads Postgres parameters from `.env`:

- `POSTGRES_HOST`
- `POSTGRES_PORT`
- `POSTGRES_USER`
- `POSTGRES_PASSWORD`
- `POSTGRES_DB`

Note: This version uses a direct connection (`psycopg2`) per request (no pooling).
