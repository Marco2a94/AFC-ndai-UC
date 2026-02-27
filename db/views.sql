-- SALES DASHBOARDS VIEWS

-- Revenue by Country
CREATE OR REPLACE VIEW v_sales_by_country AS
SELECT
    country,
    SUM(total_amount) AS total_revenue,
    SUM(quantity) AS total_quantity,
    COUNT(*) AS total_orders
FROM sales
GROUP BY country;

-- Revenue by Product
CREATE OR REPLACE VIEW v_sales_by_product AS
SELECT
    product,
    SUM(total_amount) AS total_revenue,
    SUM(quantity) AS total_quantity
FROM sales
GROUP BY product;

-- Daily Revenue Evolution
CREATE OR REPLACE VIEW v_sales_daily AS
SELECT
    sale_date,
    SUM(total_amount) AS daily_revenue,
    SUM(quantity) AS daily_quantity
FROM sales
GROUP BY sale_date
ORDER BY sale_date;

-- FEEDBACK DASHBOARD VIEWS

-- Sentiment Distribution
CREATE OR REPLACE VIEW v_feedback_sentiment_distribution AS
SELECT
    sentiment,
    COUNT(*) AS total_feedback,
    ROUND(
        COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (),
        2
    ) AS percentage
FROM feedback
GROUP BY sentiment;

-- Sentiment Over Time
CREATE OR REPLACE VIEW v_feedback_daily AS
SELECT
    feedback_date,
    sentiment,
    COUNT(*) AS total_feedback
FROM feedback
GROUP BY feedback_date, sentiment
ORDER BY feedback_date;

-- Campaign Performance
CREATE OR REPLACE VIEW v_feedback_by_campaign AS
SELECT
    campaign_id,
    COUNT(*) AS total_feedback,
    SUM(CASE WHEN sentiment = 'positive' THEN 1 ELSE 0 END) AS positive_count,
    SUM(CASE WHEN sentiment = 'negative' THEN 1 ELSE 0 END) AS negative_count,
    SUM(CASE WHEN sentiment = 'neutral' THEN 1 ELSE 0 END) AS neutral_count
FROM feedback
GROUP BY campaign_id;