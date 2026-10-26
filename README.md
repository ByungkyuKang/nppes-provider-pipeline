# nppes-provider-pipeline

An end-to-end ELT pipeline for CMS NPPES provider data.
It ingests a weekly NPPES incremental file, cleans it with pandas, checks data quality, and loads it into DuckDB with an idempotent load. The pipeline runs end-to-end with `python -m src.main`, on a daily Windows Task Scheduler job, or in Docker.

## Pipeline flow


```
CMS NPPES weekly incremental file (CSV)
        │
        ▼
  1. Ingest (src/ingest.py)
      Download the weekly file, or fall back to the latest local CSV if the download fails. Raw files live in data/raw/.
        │
        ▼
  2. Transform (src/transform.py)
      Deduplicate by NPI; strip and uppercase code columns;
      add an is_deactivated flag from NPI Deactivation Date and NPI Reactivation Date.
        │
        ▼
  3. Validate (src/validate.py)
      Report row count, null NPIs, duplicate NPIs, invalid Entity Type Codes, and deactivated providers.
        │
        ▼
  4. Load (src/load.py)
      Load into DuckDB at data/processed/provider.duckdb, idempotently: delete rows whose NPI is in the new batch, then insert the batch.
        │
        ▼
  5. Schedule
      Windows Task Scheduler runs run_pipeline.bat daily. Docker is also supported.
```

## Example run

Weekly file used for development: `npidata_pfile_20261012-20261018.csv` (32,691 rows, 330 columns; 331 columns after transform.)

Data quality report:
{'row_count': 32691, 'null_npi_count': 0, 'duplicate_npi_count': 0, 'invalid_entity_type_count': 0, 'deactivated_count': 799}


These counts are for that weekly batch, not a national total.

## Getting started

Local run:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m src.main
```

On Windows, run_pipeline.bat runs the same pipeline with the venv
Python, without manual activation.

Docker run:
```
      docker build -t nppes-provider-pipeline .
      docker run --rm -v C:\path\to\nppes-provider-pipeline\data:/app/data nppes-provider-pipeline
```

Mount data/ as a volume. The container copies only src/, and data
files are excluded from git, so without the volume the container would
have no input file and its DuckDB output would disappear with the
container.

Scheduling:

Windows Task Scheduler runs run_pipeline.bat daily. The Task
Scheduler task itself is a local Windows setting and is not stored
in this repo.


## Data
CMS NPPES (National Plan and Provider Enumeration System) public data.
The full monthly file exceeds 4 GB, so this project uses weekly
incremental files. Weekly files are format-identical to the monthly
full replacement file, so the same code scales to the full file.

CMS rotates weekly files and does not keep historical files. If a
download fails, the pipeline prints a warning and uses the latest
local CSV instead of failing, so a scheduled run is not blocked by
an unavailable upstream file.

Raw data and the DuckDB file are local only and are excluded from
git (see .gitignore).


## Project structure
```
src/
      ingest.py    - download, find the latest CSV, load raw data
      transform.py - deduplicate, normalize codes, deactivation flag
      validate.py  - data quality report
      load.py      - idempotent DuckDB load
      main.py      - runs ingest -> transform -> validate -> load
run_pipeline.bat - Windows runner for Task Scheduler
Dockerfile       - container image for the pipeline
```

## Tech Stack

Python, pandas, DuckDB, Docker, Windows Task Scheduler

Future work: migrate scheduling to Airflow, and try PySpark on the
full monthly file.