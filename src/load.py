"""4단계: Load — 정제된 데이터를 DuckDB에 적재한다.

멱등성(idempotent): 같은 데이터를 두 번 넣어도 결과가 달라지지 않게 만든다.
매일 실행되는 파이프라인의 기본기다.
(Day 4에서 구현)
"""
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "processed", "provider.duckdb")


def load(df, db_path: str = DB_PATH) -> None:
    raise NotImplementedError("Day 4에서 구현 예정")
