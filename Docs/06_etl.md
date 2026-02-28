# ETL (Batch ingestion)

ETL container: `etl/`  
It is started by Docker Compose and kept alive with `sleep infinity` so you can execute ingestion commands.

## 1) Sales ingestion

Script: `etl/ingest_sales.py`

What it does:
1. Reads a CSV file into pandas
2. Normalizes column names to lowercase
3. Converts numeric columns (`quantity`, `unit_price`, `total_amount`)
4. Parses `sale_date` into datetime
5. Drops invalid rows (`NaN`)
6. Inserts rows into `sales_raw` (raw layer)
7. Inserts transformed rows into `sales` (curated layer)

Run:
```bash
docker exec -it afc_etl python ingest_sales.py /app/data/raw/sales_data.csv
```

## 2) Feedback batch ingestion (optional)

Script: `etl/ingest_feedback.py`

What it does:
1. Reads a JSON array of feedback entries
2. Computes sentiment using the same TextBlob logic as the API
3. Inserts entries into the `feedback` table

Run:
```bash
docker exec -it afc_etl python ingest_feedback.py /app/data/raw/feedback_data.json
```

## Notes
- The “real-time” path is `POST /feedback` (FastAPI).
- Batch feedback ingestion is mainly useful for loading demo data quickly.
