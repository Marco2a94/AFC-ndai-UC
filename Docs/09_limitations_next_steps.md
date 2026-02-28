# Limitations and next steps

## Current limitations (based on the implemented code)
- No authentication on the REST API (`POST /feedback` is open).
- No DB connection pooling in the API (one connection per request).
- Sentiment analysis uses a simple baseline (TextBlob), which may fail on sarcasm, slang, or mixed-language comments.
- ETL does not prevent double-ingestion (running ingestion multiple times will insert duplicates).
- Limited automated tests.

## Suggested improvements
- Add API authentication (API key / JWT) + rate limiting.
- Add connection pooling (e.g., SQLAlchemy engine or psycopg pool).
- Add idempotency / deduplication keys for ingestion (hash or natural keys).
- Improve sentiment: multilingual model, fine-tuned classifier, or aspect-based sentiment.
- Add CI pipeline (lint + tests + build).
- Add a “Gold” layer table (pre-aggregated KPIs) to speed up dashboards at scale.
