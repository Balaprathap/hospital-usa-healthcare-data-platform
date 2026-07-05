from data_ingestion.pagination import fetch_all_hospital_data
from data_ingestion.save_raw_data import save_raw_json
from config.logger import logger


def main():
    logger.info("Starting CMS hospital data ingestion")

    records = fetch_all_hospital_data()

    file_path = save_raw_json(records)

    logger.info(f"Ingestion completed successfully. Records={len(records)}")

    print("Ingestion completed")
    print("Total records:", len(records))
    print("Saved file:", file_path)


if __name__ == "__main__":
    main()