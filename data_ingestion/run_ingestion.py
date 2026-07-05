from data_ingestion.pagination import fetch_all_hospital_data
from data_ingestion.save_raw_data import save_raw_json_batches
from config.logger import logger


def main():
    logger.info("Starting CMS hospital data ingestion")

    records = fetch_all_hospital_data()

    batch_files = save_raw_json_batches(records)

    logger.info(f"Ingestion completed successfully. Records={len(records)}, Batches={len(batch_files)}")

    print("Ingestion completed")
    print("Total records:", len(records))
    print("Total batch files:", len(batch_files))

    for file_path in batch_files:
        print("Saved:", file_path)


if __name__ == "__main__":
    main()