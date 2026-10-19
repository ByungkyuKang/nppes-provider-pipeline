"""1단계: Ingest — NPPES 공개 데이터를 내려받아 data/raw/ 에 저장한다."""
import os

RAW_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "raw")


def download_nppes(dest_dir: str = RAW_DIR) -> str:
    """NPPES 주간 증분 파일을 내려받는다. (Day 2에서 구현)

    CMS Data Dissemination 페이지에서 받을 수 있다:
    https://www.cms.gov/Regulations-and-Guidance/Administrative-Simplification/NationalProvIdentStand/DataDissemination
    """
    os.makedirs(dest_dir, exist_ok=True)
    raise NotImplementedError("Day 2에서 구현 예정")


def load_raw(path: str):
    """내려받은 CSV를 pandas DataFrame으로 읽는다. (Day 2에서 구현)"""
    raise NotImplementedError("Day 2에서 구현 예정")
