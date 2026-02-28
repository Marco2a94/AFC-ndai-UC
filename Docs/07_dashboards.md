# Dashboards (Metabase)

Metabase runs at: `http://localhost:3000`

## 1) Connect Metabase to Postgres
During Metabase setup (first run), connect using:

- Type: PostgreSQL
- Host: `db`
- Port: `5432`
- Database: `afc_db`
- Username: `postgres`
- Password: the one in your `.env`

## 2) Datasets to use
Use the SQL views created in `db/views.sql`. They are already “dashboard-ready”.

Sales:
- `v_sales_by_country`
- `v_sales_by_product`
- `v_sales_daily`

Feedback:
- `v_feedback_sentiment_distribution`
- `v_feedback_daily`
- `v_feedback_by_campaign`

## 3) Sales dashboard — recommended charts
- KPI: Total revenue (sum of `total_revenue`) — from `v_sales_by_country` or directly from `sales`
- Bar chart: Revenue by country — `v_sales_by_country.total_revenue`
- Bar chart: Revenue by product — `v_sales_by_product.total_revenue`
- Line chart: Daily revenue — `v_sales_daily.daily_revenue`
- Line chart: Daily quantity — `v_sales_daily.daily_quantity`

Filters (recommended):
- Date range (if using `sales` directly) or date filter on `v_sales_daily.sale_date`
- Country (if using `sales` directly)

## 4) Sentiment dashboard — recommended charts
- Pie/Donut: Sentiment distribution — `v_feedback_sentiment_distribution`
- Stacked bar: Daily sentiment counts — `v_feedback_daily` (group by date, split by sentiment)
- Table or bar chart: Campaign performance — `v_feedback_by_campaign` (positive/neutral/negative counts)

Filters (recommended):
- Campaign ID
- Date range (if you query `feedback` table directly)

## 5) Evidence in the repo (recommended)
To match “reports in the Git repo”, export or capture:
- Screenshots of the dashboards (store them in `docs/assets/`)
- Or Metabase exports (if you use them)

If you add images, create:
- `docs/assets/` and reference the images in this file.
