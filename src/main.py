"""파이프라인 진입점: ingest → transform → validate → load 순서로 실행한다."""
from .ingest import download_nppes, load_raw
from .transform import transform
from .validate import run_checks
from .load import load


def main() -> None:
    raw_path = download_nppes()
    df = load_raw(raw_path)
    df = transform(df)

    report = run_checks(df)
    print("데이터 품질 리포트:", report)

    load(df)
    print("파이프라인 완료")


if __name__ == "__main__":
    main()
