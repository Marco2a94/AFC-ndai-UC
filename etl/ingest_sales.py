import pandas as pd
import sys
from db_utils import get_connection

def load_raw(df, cursor):
    for _, row in df.iterrows():
        cursor.execute(
            """
            INSERT INTO sales_raw
            (raw_username, raw_sale_date, raw_country, raw_product,
             raw_quantity, raw_unit_price, raw_total_amount)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            (
                str(row["username"]),
                str(row["sale_date"]),
                str(row["country"]),
                str(row["product"]),
                str(row["quantity"]),
                str(row["unit_price"]),
                str(row["total_amount"])
            )
        )

def transform_to_clean(cursor):
    cursor.execute("""
        INSERT INTO sales (
            username,
            sale_date,
            country,
            product,
            quantity,
            unit_price,
            total_amount
        )
        SELECT
            raw_username,
            raw_sale_date::DATE,
            raw_country,
            raw_product,
            raw_quantity::INT,
            raw_unit_price::FLOAT,
            raw_total_amount::FLOAT
        FROM sales_raw;
    """)

def ingest_sales(csv_path):
    print("Reading CSV...")
    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.strip().str.lower()
    
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")
    df["total_amount"] = pd.to_numeric(df["total_amount"], errors="coerce")

    df["sale_date"] = pd.to_datetime(df["sale_date"], errors="coerce")

    # Drop invalid rows
    df = df.dropna()

    print(f"Valid rows after cleaning: {len(df)}")
    conn = get_connection()
    cursor = conn.cursor()

    print("Loading raw layer...")
    load_raw(df, cursor)

    print("Transforming to curated layer...")
    transform_to_clean(cursor)

    conn.commit()
    cursor.close()
    conn.close()

    print("ETL completed successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ingest_sales.py <path_to_csv>")
        sys.exit(1)

    ingest_sales(sys.argv[1])
