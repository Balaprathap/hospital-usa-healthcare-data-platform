import json
from kafka import KafkaConsumer

TOPIC_NAME = "hospital-data"
BOOTSTRAP_SERVERS = "localhost:9092"


def create_consumer():
    return KafkaConsumer(
        TOPIC_NAME,
        bootstrap_servers=BOOTSTRAP_SERVERS,
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="hospital360-test-group-2",
        value_deserializer=lambda value: json.loads(value.decode("utf-8"))
    )


def main():
    consumer = create_consumer()

    print(f"Listening to Kafka topic: {TOPIC_NAME}")

    for message in consumer:
        record = message.value
        print(record["facility_id"], record["facility_name"], record["state"])


if __name__ == "__main__":
    main()