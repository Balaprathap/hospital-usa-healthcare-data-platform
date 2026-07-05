from data_ingestion.api_client import fetch_hospital_data
from config.config import PAGE_SIZE
from config.logger import logger


def fetch_all_hospital_data():
    all_records = []
    offset = 0

    while True:
        logger.info(f"Fetching records with offset={offset}")

        data = fetch_hospital_data(limit=PAGE_SIZE, offset=offset)
        records = data["results"]

        if not records:
            logger.info("No more records found. Stopping pagination.")
            break

        all_records.extend(records)

        logger.info(f"Fetched {len(records)} records")

        offset += PAGE_SIZE

    return all_records