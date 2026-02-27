DROP TABLE IF EXISTS feedback;
DROP TABLE IF EXISTS sales;
DROP TABLE IF EXISTS sales_raw;

CREATE TABLE feedback (
    id SERIAL PRIMARY KEY,
    campaign_id VARCHAR(100),
    username VARCHAR(100),
    comment TEXT,
    sentiment VARCHAR(20),
    feedback_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE sales_raw (
    id SERIAL PRIMARY KEY,
    raw_username TEXT,
    raw_sale_date TEXT,
    raw_country TEXT,
    raw_product TEXT,
    raw_quantity TEXT,
    raw_unit_price TEXT,
    raw_total_amount TEXT
);

CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100),
    sale_date DATE,
    country VARCHAR(100),
    product VARCHAR(100),
    quantity INT,
    unit_price NUMERIC(10,2),
    total_amount NUMERIC(10,2)
);

CREATE INDEX idx_feedback_campaign ON feedback(campaign_id);
CREATE INDEX idx_sales_date ON sales(sale_date);
CREATE INDEX idx_sales_country ON sales(country);