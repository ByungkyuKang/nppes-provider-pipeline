"""Step 2: Transform — clean the data with pandas."""

CODE_COLUMNS = [
    "Entity Type Code",
    "Provider Sex Code",
    "Is Sole Proprietor",
    "Is Organization Subpart",
]


def transform(df):
    df = df.drop_duplicates(subset=["NPI"], keep="first")

    for col in CODE_COLUMNS:
        df[col] = df[col].str.strip().str.upper()

    df["is_deactivated"] = (
        df["NPI Deactivation Date"].notna()
        & df["NPI Reactivation Date"].isna()
    )

    return df
