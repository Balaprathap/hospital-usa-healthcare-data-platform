from data_ingestion.pagination import fetch_all_hospital_data
from data_ingestion.save_raw_data import save_raw_json_batches
from data_ingestion.metadata_writer import save_metadata
from config.logger import logger
import time


def main():
    start_time = time.time()

    logger.info("Starting CMS hospital data ingestion")

    records = fetch_all_hospital_data()

    batch_files = save_raw_json_batches(records)

    duration = time.time() - start_time

    save_metadata(
        total_records=len(records),
        total_batches=len(batch_files),
        status="SUCCESS",
        duration=duration
    )

    logger.info(f"Ingestion completed successfully. Records={len(records)}, Batches={len(batch_files)}")

    print("Ingestion completed")
    print("Total records:", len(records))
    print("Total batch files:", len(batch_files))

    for file_path in batch_files:
        print("Saved:", file_path)


if __name__ == "__main__":
    main()