import json
import os
from datetime import datetime


def save_metadata(total_records, total_batches, status, duration):

    os.makedirs("metadata", exist_ok=True)

    metadata = {
        "pipeline_name": "Hospital360 CMS Ingestion",

        "execution_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

        "status": status,

        "records_processed": total_records,

        "batch_files_created": total_batches,

        "execution_time_seconds": round(duration, 2)
    }

    file_name = datetime.now().strftime("%Y%m%d_%H%M%S")

    with open(f"metadata/{file_name}.json", "w") as file:

        json.dump(metadata, file, indent=4)