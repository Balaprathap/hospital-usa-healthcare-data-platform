import json
import time
from kafka import KafkaProducer

from data_ingestion.pagination import fetch_all_hospital_data


TOPIC_NAME = "hospital-data"
BOOTSTRAP_SERVERS = "localhost:9092"


def create_producer():
    return KafkaProducer(
        bootstrap_servers=BOOTSTRAP_SERVERS,
        value_serializer=lambda value: json.dumps(value).encode("utf-8")
    )


def main():
    producer = create_producer()
    records = fetch_all_hospital_data()

    print(f"Sending {len(records)} records to Kafka topic: {TOPIC_NAME}")

    for record in records:
        producer.send(TOPIC_NAME, value=record)
        print(f"Sent facility_id: {record['facility_id']}")
        time.sleep(0.01)

    producer.flush()
    producer.close()

    print("All records sent to Kafka successfully")


if __name__ == "__main__":
    main()