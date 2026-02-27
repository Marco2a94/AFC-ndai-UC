DROP TABLE IF EXISTS feedback;
DROP TABLE IF EXISTS sales;

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
    username VARCHAR(100),
    comment TEXT,
    sentiment VARCHAR(20),
    feedback_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);