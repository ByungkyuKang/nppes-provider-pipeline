"""Step 4: Load — load the cleaned data into DuckDB.

Idempotent: loading the same data twice does not change the result.
Delete rows whose NPI is in the new batch, then insert the batch.
"""
import os

import duckdb

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "processed", "provider.duckdb")


def load(df, db_path: str = DB_PATH) -> None:
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    con = duckdb.connect(db_path)
    con.register("df_view", df)
    con.execute("CREATE TABLE IF NOT EXISTS providers AS SELECT * FROM df_view WHERE 1=0")
    con.execute("DELETE FROM providers WHERE NPI IN (SELECT NPI FROM df_view)")
    con.execute("INSERT INTO providers SELECT * FROM df_view")
    con.close()
