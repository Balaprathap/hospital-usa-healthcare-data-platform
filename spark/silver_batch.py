from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StringType


spark = (
    SparkSession.builder
    .appName("Hospital360 Silver Layer")
    .master("spark://hospital360-spark-master:7077")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("WARN")

schema = (
    StructType()
    .add("facility_id", StringType())
    .add("facility_name", StringType())
    .add("address", StringType())
    .add("citytown", StringType())
    .add("state", StringType())
    .add("zip_code", StringType())
    .add("countyparish", StringType())
    .add("hospital_type", StringType())
    .add("hospital_ownership", StringType())
    .add("emergency_services", StringType())
    .add("hospital_overall_rating", StringType())
)

bronze_df = spark.read.parquet("/opt/spark/work-dir/bronze")

silver_df = (
    bronze_df
    .withColumn("json_data", from_json(col("raw_json"), schema))
    .select(
        col("json_data.facility_id"),
        col("json_data.facility_name"),
        col("json_data.address"),
        col("json_data.citytown"),
        col("json_data.state"),
        col("json_data.zip_code"),
        col("json_data.countyparish"),
        col("json_data.hospital_type"),
        col("json_data.hospital_ownership"),
        col("json_data.emergency_services"),
        col("json_data.hospital_overall_rating"),
        col("timestamp").alias("ingestion_timestamp")
    )
    .dropDuplicates(["facility_id"])
)

silver_df.write.mode("overwrite").parquet("/opt/spark/work-dir/silver")

print("Silver layer completed")
print("Rows:", silver_df.count())

spark.stop()