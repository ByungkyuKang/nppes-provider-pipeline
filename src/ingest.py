import glob
import os
import zipfile

import pandas as pd
import requests

RAW_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "raw")
DEFAULT_URL = "https://download.cms.gov/nppes/NPPES_Data_Dissemination_101226_101826_Weekly_V2.zip"


def download_nppes(url=DEFAULT_URL):
    os.makedirs(RAW_DIR, exist_ok=True)
    zip_path = os.path.join(RAW_DIR, os.path.basename(url))

    if not os.path.exists(zip_path):
        response = requests.get(url)
        response.raise_for_status()
        with open(zip_path, "wb") as f:
            f.write(response.content)

    with zipfile.ZipFile(zip_path) as zf:
        zf.extractall(RAW_DIR)

    return find_latest_csv()


def find_latest_csv():
    pattern = os.path.join(RAW_DIR, "npidata_pfile_*.csv")
    candidates = [p for p in glob.glob(pattern) if "fileheader" not in os.path.basename(p)]

    if not candidates:
        raise FileNotFoundError("No npidata_pfile CSV found in data/raw")

    return sorted(candidates)[-1]


def load_raw(path):
    return pd.read_csv(path, dtype=str)