import json
from logging import getLogger

import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
from pathlib import Path

# SQL Filepaths
hires_with_geo = (
    Path(__name__).resolve().parent / "hires_with_geo.sql"
)

SCOPES = ["https://www.googleapis.com/auth/bigquery",
            "https://www.googleapis.com/auth/drive",
            "https://www.googleapis.com/auth/cloud-platform",]
SERVICE_ACCOUNT_FILE = "/Users/frank/london_cycles/london-cycles-306117-3eea1d911957.json"

credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

with open(hires_with_geo, "r") as file:
    sql = file.read()

logger = getLogger(__name__)

def get_london_cycle_hires(
    credentials: service_account.Credentials,
) -> pd.DataFrame:
    query = sql

    # Create dataframe for migrating meterpoints
    df = pd.read_gbq(
        query,
        project_id="london-cycles-306117",
        dialect="standard",
        credentials=credentials,
        location="EU",
    )

    return df
