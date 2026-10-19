"""Step 1: Ingest — download NPPES public data into data/raw/."""
import os

RAW_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "raw")


def download_nppes(dest_dir: str = RAW_DIR) -> str:
    """Download the NPPES weekly incremental file. (To be implemented on Day 2)

    Available from the CMS Data Dissemination page:
    https://www.cms.gov/Regulations-and-Guidance/Administrative-Simplification/NationalProvIdentStand/DataDissemination
    """
    os.makedirs(dest_dir, exist_ok=True)
    raise NotImplementedError("To be implemented on Day 2")


def load_raw(path: str):
    """Read the downloaded CSV into a pandas DataFrame. (To be implemented on Day 2)"""
    raise NotImplementedError("To be implemented on Day 2")
