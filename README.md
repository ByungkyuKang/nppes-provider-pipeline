# nppes-provider-pipeline

헬스케어 provider(의료 제공자) 라이선스 데이터의 end-to-end 데이터 파이프라인.
CMS NPPES 공개 데이터를 수집 → 정제 → 품질 검증 → 적재 → 일간 스케줄링한다.

## 파이프라인 흐름

```
NPPES 공개 데이터 (CSV)
        │
        ▼
  1. Ingest (src/ingest.py)      — 데이터 다운로드 및 raw 저장
        │
        ▼
  2. Transform (src/transform.py) — pandas 정제: 중복 제거, 만료일 계산, 상태 정규화
        │
        ▼
  3. Validate (src/validate.py)   — 품질 규칙 검사: 필수값 누락, 만료 라이선스 탐지
        │
        ▼
  4. Load (src/load.py)           — DuckDB 적재 (멱등성 보장)
        │
        ▼
  5. Schedule                     — cron → Airflow DAG 일간 실행 (W2~W3)
```

## 실행 방법

```bash
# 1. 가상환경 생성 및 활성화
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 2. 의존성 설치
pip install -r requirements.txt

# 3. 파이프라인 실행
python -m src.main
```

## 기술 스택

Python, pandas, DuckDB, (예정: cron → Airflow, Docker, PySpark)

## 데이터

CMS NPPES (National Plan & Provider Enumeration System) 공개 데이터.
전체 월간 파일이 4GB를 넘으므로, 실습용으로는 주간 증분 파일 또는 특정 주(state) 샘플을 사용한다.
