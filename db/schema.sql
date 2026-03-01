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
    username TEXT NOT NULL,
    sale_date DATE NOT NULL,
    country TEXT NOT NULL,
    product TEXT NOT NULL,
    quantity INT NOT NULL,
    unit_price FLOAT NOT NULL,
    total_amount FLOAT NOT NULL,
    CONSTRAINT unique_sale UNIQUE (username, sale_date, country, product)
);


CREATE INDEX idx_feedback_campaign ON feedback(campaign_id);
CREATE INDEX idx_sales_date ON sales(sale_date);
CREATE INDEX idx_sales_country ON sales(country);