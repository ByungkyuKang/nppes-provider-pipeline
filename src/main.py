"""Pipeline entry point: runs ingest → transform → validate → load in order."""
from .ingest import download_nppes, load_raw
from .transform import transform
from .validate import run_checks
from .load import load


def main() -> None:
    raw_path = download_nppes()
    df = load_raw(raw_path)
    df = transform(df)

    report = run_checks(df)
    print("Data quality report:", report)

    load(df)
    print("Pipeline complete")


if __name__ == "__main__":
    main()
