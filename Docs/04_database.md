# Database

SQL is stored in:
- `db/schema.sql` (tables + indexes)
- `db/views.sql` (reporting views for dashboards)

These scripts are automatically executed by the Postgres image on **first database initialization**.

## Tables

### `sales_raw` (raw layer)
Stores sales data as raw text as it is received from files.

| Column | Type | Notes |
|---|---|---|
| id | SERIAL PK | |
| raw_username | TEXT | |
| raw_sale_date | TEXT | |
| raw_country | TEXT | |
| raw_product | TEXT | |
| raw_quantity | TEXT | |
| raw_unit_price | TEXT | |
| raw_total_amount | TEXT | |

### `sales` (curated layer)
Cleaned and typed sales table used for analytics and dashboards.

| Column | Type | Notes |
|---|---|---|
| id | SERIAL PK | |
| username | VARCHAR(100) | |
| sale_date | DATE | |
| country | VARCHAR(100) | |
| product | VARCHAR(100) | |
| quantity | INT | |
| unit_price | NUMERIC(10,2) | |
| total_amount | NUMERIC(10,2) | |

Indexes:
- `idx_sales_date` on `sale_date`
- `idx_sales_country` on `country`

### `feedback`
Stores marketing campaign feedback and sentiment label.

| Column | Type | Notes |
|---|---|---|
| id | SERIAL PK | |
| campaign_id | VARCHAR(100) | |
| username | VARCHAR(100) | |
| comment | TEXT | Raw comment text |
| sentiment | VARCHAR(20) | positive / neutral / negative |
| feedback_date | DATE | |
| created_at | TIMESTAMP | default current_timestamp |

Index:
- `idx_feedback_campaign` on `campaign_id`

## Views (reporting layer)

Sales:
- `v_sales_by_country`: total revenue / quantity / orders per country
- `v_sales_by_product`: total revenue / quantity per product
- `v_sales_daily`: daily revenue and quantity

Feedback:
- `v_feedback_sentiment_distribution`: sentiment breakdown (% and counts)
- `v_feedback_daily`: sentiment over time (daily counts by sentiment)
- `v_feedback_by_campaign`: feedback counts and sentiment counts per campaign

These views are designed to be used directly in Metabase.
