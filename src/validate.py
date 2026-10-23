"""Validate — data quality checks on the cleaned data.

Returns a report dict with counts of bad rows.
main.py prints this report before loading.
"""


def run_checks(df) -> dict:
    entity = df["Entity Type Code"]
    invalid_entity = entity.notna() & ~entity.isin(["1", "2"])
    return {
        "row_count": int(len(df)),
        "null_npi_count": int(df["NPI"].isna().sum()),
        "duplicate_npi_count": int(df.duplicated(subset=["NPI"]).sum()),
        "invalid_entity_type_count": int(invalid_entity.sum()),
        "deactivated_count": int(df["is_deactivated"].sum()) if "is_deactivated" in df.columns else 0,
    }
