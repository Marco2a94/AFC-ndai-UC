DROP TABLE IF EXISTS sales;
DROP TABLE IF EXISTS sales_raw;

CREATE TABLE sales_raw (
    id SERIAL PRIMARY KEY,
    raw_date TEXT,
    raw_country TEXT,
    raw_product TEXT,
    raw_revenue TEXT,
    raw_margin TEXT,
    raw_volume TEXT
);

CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    date DATE,
    country VARCHAR(100),
    product VARCHAR(100),
    revenue FLOAT,
    margin FLOAT,
    volume INT
);