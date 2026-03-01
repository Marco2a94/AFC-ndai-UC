import pandas as pd
import pytest
from etl.ingest_sales import ingest_sales

def test_missing_columns(tmp_path):
    df = pd.DataFrame({
        "username": ["test"],
        "sale_date": ["2025-01-01"]
    })

    file_path = tmp_path / "bad.csv"
    df.to_csv(file_path, index=False)

    with pytest.raises(ValueError):
        ingest_sales(str(file_path))