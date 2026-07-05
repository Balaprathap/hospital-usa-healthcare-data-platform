import json
import os
from datetime import datetime

from config.config import RAW_DATA_PATH
from config.logger import logger


def save_raw_json_batches(records, batch_size=1000):
    run_time = datetime.now()
    date_path = run_time.strftime("%Y/%m/%d")
    timestamp = run_time.strftime("%Y%m%d_%H%M%S")

    output_dir = f"{RAW_DATA_PATH}/{date_path}/{timestamp}"
    os.makedirs(output_dir, exist_ok=True)

    batch_files = []

    for i in range(0, len(records), batch_size):
        batch_number = (i // batch_size) + 1
        batch = records[i:i + batch_size]

        file_path = f"{output_dir}/batch_{batch_number:03d}.json"

        with open(file_path, "w") as file:
            json.dump(batch, file, indent=4)

        batch_files.append(file_path)
        logger.info(f"Saved batch {batch_number} with {len(batch)} records to {file_path}")

    return batch_files