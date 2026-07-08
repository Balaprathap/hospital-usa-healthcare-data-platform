from pyspark.sql import SparkSession
from pyspark.sql.functions import count, avg, col, when

spark = (
    SparkSession.builder
    .appName("Hospital360 Gold Layer")
    .master("spark://hospital360-spark-master:7077")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("WARN")

silver_df = spark.read.parquet("/opt/spark/work-dir/silver")

clean_df = silver_df.withColumn(
    "rating_numeric",
    when(col("hospital_overall_rating") == "Not Available", None)
    .otherwise(col("hospital_overall_rating").cast("int"))
)

gold_state_kpis = (
    clean_df
    .groupBy("state")
    .agg(
        count("*").alias("total_hospitals"),
        avg("rating_numeric").alias("avg_hospital_rating")
    )
    .orderBy("state")
)

gold_state_kpis.write.mode("overwrite").parquet("/opt/spark/work-dir/gold/state_kpis")

print("Gold layer completed")
gold_state_kpis.show(50, truncate=False)

spark.stop()