import json
import os
from datetime import datetime

from config.config import RAW_DATA_PATH
from config.logger import logger


def save_raw_json(records):
    os.makedirs(RAW_DATA_PATH, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f"{RAW_DATA_PATH}/cms_hospital_quality_{timestamp}.json"

    with open(file_path, "w") as file:
        json.dump(records, file, indent=4)

    logger.info(f"Saved raw data to {file_path}")

    return file_path