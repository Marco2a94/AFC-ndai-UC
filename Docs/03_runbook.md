# Runbook (VS Code)

This is the step-by-step guide to run the project on your machine.

## 1) Prerequisites
- Docker Desktop installed and running
- VS Code

## 2) Open the project in VS Code
1. Open VS Code
2. **File → Open Folder**
3. Select the repository root folder (where `docker-compose.yml` is located)

## 3) Create the `.env` file
In the repository root (same folder as `docker-compose.yml`), create a file named `.env`:

```bash
POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password
POSTGRES_DB=afc_db
```

> Keep these values consistent: Docker Compose, FastAPI, ETL, and Metabase all use them.

## 4) Start the stack (Docker Compose)
In VS Code: **Terminal → New Terminal**, run:

```bash
docker compose down -v
docker compose up --build
```

Why `down -v`?
- Postgres init scripts (`db/schema.sql`, `db/views.sql`) run automatically **only on first init**.
- Removing volumes ensures a clean database init for demos.

## 5) Verify endpoints
- FastAPI: `http://localhost:8000`
- Swagger UI: `http://localhost:8000/docs`
- Metabase: `http://localhost:3000`

Optional health check:
- `GET http://localhost:8000/health`

## 6) Load demo data (batch ETL)
Your repository includes demo files:
- `data/raw/sales_data.csv`
- `data/raw/feedback_data.json`

Run ingestion from the ETL container:

```bash
docker exec -it afc_etl python ingest_sales.py /app/data/raw/sales_data.csv
docker exec -it afc_etl python ingest_feedback.py /app/data/raw/feedback_data.json
```

Optional verification:

```bash
docker exec -it afc_postgres psql -U postgres -d afc_db -c "SELECT COUNT(*) FROM sales;"
docker exec -it afc_postgres psql -U postgres -d afc_db -c "SELECT COUNT(*) FROM feedback;"
```

## 7) Test real-time feedback ingestion (API)
Open `http://localhost:8000/docs` and try `POST /feedback`.

Example payload:

```json
{
  "campaign_id": "CAMP123",
  "username": "user1",
  "comment": "Great campaign!",
  "feedback_date": "2025-01-01"
}
```

The API returns:
- `"status": "feedback stored"`
- `"sentiment": "positive" | "neutral" | "negative"`

## 8) Configure Metabase (first time)
1. Open `http://localhost:3000`
2. Create an admin account
3. Add a database connection:
   - Database type: **PostgreSQL**
   - Host: `db`  (important: Metabase is inside Docker)
   - Port: `5432`
   - Database name: `afc_db`
   - Username: `postgres`
   - Password: your `.env` password

Then use the SQL views created by `db/views.sql` as sources for charts (see `07_dashboards.md`).

## 9) Stop the stack
In the terminal running compose:
- Press `Ctrl + C`

Then:

```bash
docker compose down
```

## Troubleshooting

### Ports already in use
If you already have local services on ports 5432 / 8000 / 3000:
- Stop the conflicting service, **or**
- Change host ports in `docker-compose.yml`.

### Tables/views missing
This usually means Postgres did not rerun init scripts. Fix:

```bash
docker compose down -v
docker compose up --build
```
