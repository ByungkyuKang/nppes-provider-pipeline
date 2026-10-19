# nppes-provider-pipeline

An end-to-end data pipeline for healthcare provider license data.
Ingests CMS NPPES public data → cleans → validates quality → loads → runs on a daily schedule.

## Pipeline Flow

```
NPPES public data (CSV)
        │
        ▼
  1. Ingest (src/ingest.py)      — download data, store raw
        │
        ▼
  2. Transform (src/transform.py) — clean with pandas: dedupe, expiry calc, status normalize
        │
        ▼
  3. Validate (src/validate.py)   — quality rules: missing values, expired licenses
        │
        ▼
  4. Load (src/load.py)           — load into DuckDB (idempotent)
        │
        ▼
  5. Schedule                     — cron → Airflow DAG, daily (W2–W3)
```

## Getting Started

```bash
# 1. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the pipeline
python -m src.main
```

## Tech Stack

Python, pandas, DuckDB (planned: cron → Airflow, Docker, PySpark)

## Data

CMS NPPES (National Plan & Provider Enumeration System) public data.
The full monthly file exceeds 4GB, so this project uses the weekly incremental file or a single-state sample.
