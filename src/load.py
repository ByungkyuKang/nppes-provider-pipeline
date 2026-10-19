"""Step 4: Load — load the cleaned data into DuckDB.

Idempotent: loading the same data twice does not change the result.
A fundamental practice for daily pipelines.
(To be implemented on Day 4)
"""
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "processed", "provider.duckdb")


def load(df, db_path: str = DB_PATH) -> None:
    raise NotImplementedError("To be implemented on Day 4")
