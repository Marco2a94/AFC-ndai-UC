CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    date DATE,
    country VARCHAR(100),
    product VARCHAR(100),
    revenue FLOAT,
    margin FLOAT,
    volume INT
);

CREATE TABLE feedback (
    id SERIAL PRIMARY KEY,
    campaign_id VARCHAR(100),
    customer_id VARCHAR(100),
    comment TEXT,
    sentiment VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);