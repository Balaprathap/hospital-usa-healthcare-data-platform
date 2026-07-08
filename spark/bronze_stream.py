from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = (
    SparkSession.builder
    .appName("Hospital360 Bronze Layer")
    .master("spark://hospital360-spark-master:7077")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("WARN")

# Read from Kafka
df = (
    spark.readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", "hospital360-kafka:29092")
    .option("subscribe", "hospital-data")
    .option("startingOffsets", "latest")
    .load()
)

# Convert Kafka bytes to readable strings
bronze_df = (
    df.select(
        col("value").cast("string").alias("raw_json"),
        col("timestamp")
    )
)

query = (
    bronze_df.writeStream
    .format("parquet")
    .option("path", "/opt/spark/work-dir/bronze")
    .option(
        "checkpointLocation",
        "/opt/spark/work-dir/checkpoints/bronze"
    )
    .outputMode("append")
    .start()
)

query.awaitTermination()